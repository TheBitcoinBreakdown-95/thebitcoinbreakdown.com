"""
Embeds btc-index chunks via Ollama mxbai-embed-large and stores in LanceDB.
Creates FTS index for BM25 search. Supports incremental re-indexing.

Adapted from AI/AI-Notes/kb-mcp/indexer.py for the btc-index corpus.
"""

import hashlib
import json
import time
from pathlib import Path

import httpx
import lancedb

from chunker import chunk_all, chunk_file, discover_files

OLLAMA_URL = "http://localhost:11434/api/embed"
EMBED_MODEL = "mxbai-embed-large"
EMBED_DIMS = 1024
TABLE_NAME = "btc_chunks"

# Truncate text before embedding (mxbai-embed-large context ~512 tokens)
MAX_EMBED_CHARS = 2_000


def get_tbb_root(override: str | None = None) -> Path:
    if override:
        return Path(override)
    return Path(__file__).parent.parent.parent


def get_db_path() -> Path:
    return Path(__file__).parent.parent / ".vectordb"


def get_meta_path() -> Path:
    return Path(__file__).parent.parent / "_index_meta.json"


def file_hash(filepath: Path) -> str:
    return hashlib.sha256(filepath.read_bytes()).hexdigest()[:16]


def embed_one(text: str) -> list[float]:
    """Embed a single text via Ollama. Retries with shorter text on context overflow."""
    limit = MAX_EMBED_CHARS
    while limit >= 200:
        truncated = text[:limit] if len(text) > limit else text
        resp = httpx.post(
            OLLAMA_URL,
            json={"model": EMBED_MODEL, "input": truncated},
            timeout=120.0,
        )
        if resp.status_code == 200:
            return resp.json()["embeddings"][0]
        if resp.status_code == 400 and "context length" in resp.text:
            limit = int(limit * 0.7)
            continue
        resp.raise_for_status()
    raise RuntimeError(f"Cannot embed text even at {limit} chars")


def embed_chunks(chunks: list[dict]) -> list[dict]:
    """Add 'vector' field to each chunk via sequential embedding."""
    total = len(chunks)
    for i, chunk in enumerate(chunks):
        chunk["vector"] = embed_one(chunk["text"])
        if (i + 1) % 20 == 0 or i + 1 == total:
            print(f"  Embedded {i + 1}/{total} chunks")
    return chunks


def _normalize_for_lancedb(chunks: list[dict]) -> list[dict]:
    """Ensure all chunks have consistent fields for LanceDB schema.

    LanceDB infers schema from the first batch. Optional fields like
    block_num and link_num may only appear on some chunks, so we fill
    missing fields with defaults to keep the schema uniform.
    """
    for chunk in chunks:
        chunk.setdefault("block_num", 0)
        chunk.setdefault("link_num", 0)
        # Ensure chapter is always an int (0 for unknown)
        if chunk["chapter"] is None:
            chunk["chapter"] = 0
        # Ensure sub_chapter is always a string
        if not chunk["sub_chapter"]:
            chunk["sub_chapter"] = ""
    return chunks


def build_index(chunks: list[dict]) -> None:
    """Create or overwrite the LanceDB table and FTS index."""
    db_path = get_db_path()
    db = lancedb.connect(str(db_path))

    try:
        db.drop_table(TABLE_NAME)
    except Exception:
        pass

    if not chunks:
        print("No chunks to index.")
        return

    print(f"Embedding {len(chunks)} chunks...")
    chunks = embed_chunks(chunks)
    chunks = _normalize_for_lancedb(chunks)

    table = db.create_table(TABLE_NAME, data=chunks, mode="overwrite")
    print(f"Created table '{TABLE_NAME}' with {len(chunks)} rows")

    table.create_fts_index("text", replace=True)
    print("FTS index created on 'text' column")


def write_meta(tbb_root: Path) -> None:
    """Write _index_meta.json with file hashes for incremental reindex."""
    files = discover_files(tbb_root)
    meta = {}
    for fpath, stype in files:
        key = str(fpath.relative_to(tbb_root)).replace("\\", "/")
        meta[key] = {"hash": file_hash(fpath), "source_type": stype}

    get_meta_path().write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"Wrote _index_meta.json ({len(meta)} files)")


def read_meta() -> dict:
    meta_path = get_meta_path()
    if meta_path.exists():
        return json.loads(meta_path.read_text(encoding="utf-8"))
    return {}


def full_index(tbb_root: Path) -> None:
    """Full re-index of all discoverable files."""
    start = time.time()
    chunks = chunk_all(tbb_root)
    print(f"Chunked {len(chunks)} sections from discovered files")

    # Summary by type
    by_type = {}
    for c in chunks:
        st = c["source_type"]
        by_type[st] = by_type.get(st, 0) + 1
    for st, count in sorted(by_type.items()):
        print(f"  {st}: {count} chunks")

    build_index(chunks)
    write_meta(tbb_root)
    elapsed = time.time() - start
    print(f"Full index complete in {elapsed:.1f}s")


def reindex_file(tbb_root: Path, rel_path: str, source_type: str) -> None:
    """Incrementally re-index a single file."""
    filepath = tbb_root / rel_path
    if not filepath.exists():
        print(f"File not found: {rel_path}")
        return

    db_path = get_db_path()
    db = lancedb.connect(str(db_path))

    try:
        table = db.open_table(TABLE_NAME)
    except Exception:
        print("No existing index found. Running full index instead.")
        full_index(tbb_root)
        return

    # Remove old chunks for this file
    escaped_path = rel_path.replace('"', '\\"')
    table.delete(f'file = "{escaped_path}"')

    # Chunk and embed the updated file
    new_chunks = chunk_file(filepath, tbb_root, source_type)
    if new_chunks:
        print(f"Re-indexing {rel_path}: {len(new_chunks)} chunks")
        new_chunks = embed_chunks(new_chunks)
        new_chunks = _normalize_for_lancedb(new_chunks)
        table.add(new_chunks)
        table.create_fts_index("text", replace=True)
        print("Updated FTS index")

    # Update meta
    meta = read_meta()
    key = rel_path.replace("\\", "/")
    meta[key] = {"hash": file_hash(filepath), "source_type": source_type}
    get_meta_path().write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"Re-index of {rel_path} complete")


def reindex_changed(tbb_root: Path) -> None:
    """Re-index only files whose hash has changed since last index."""
    old_meta = read_meta()
    files = discover_files(tbb_root)
    changed = []

    for fpath, stype in files:
        key = str(fpath.relative_to(tbb_root)).replace("\\", "/")
        current_hash = file_hash(fpath)
        old_entry = old_meta.get(key, {})
        if isinstance(old_entry, str):
            old_hash = old_entry
        else:
            old_hash = old_entry.get("hash", "")
        if old_hash != current_hash:
            changed.append((key, stype))

    if not changed:
        print("All files up to date. Nothing to re-index.")
        return

    print(f"Changed files: {len(changed)}")
    for rel_path, stype in changed:
        print(f"  {rel_path}")
        reindex_file(tbb_root, rel_path, stype)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Index btc-index corpus into LanceDB")
    parser.add_argument("--tbb-root", help="Path to TBB root directory")
    parser.add_argument("--file", help="Re-index a single file (relative path from TBB root)")
    parser.add_argument("--file-type", help="Source type for --file (e.g. catalog, guide)")
    parser.add_argument("--changed", action="store_true", help="Re-index only changed files")
    args = parser.parse_args()

    tbb_root = get_tbb_root(args.tbb_root)
    if args.file:
        stype = args.file_type or "wbigaf_source"
        reindex_file(tbb_root, args.file, stype)
    elif args.changed:
        reindex_changed(tbb_root)
    else:
        full_index(tbb_root)

"""
Bitcoin Index MCP Server.
Provides semantic search over the TBB research corpus via FastMCP with 4 tools:
  - search_corpus:  Hybrid BM25 + vector search with RRF, optional filters
  - list_sources:   Browse indexed material by chapter and source type
  - get_chunk:      Direct retrieval by file + heading
  - find_related:   Given a chunk, find semantically similar chunks (cross-chapter)
"""

import os
from pathlib import Path

import httpx
import lancedb
from fastmcp import FastMCP

OLLAMA_URL = "http://localhost:11434/api/embed"
EMBED_MODEL = "mxbai-embed-large"
TABLE_NAME = "btc_chunks"

DB_PATH = str(Path(__file__).parent.parent / ".vectordb")

# Bitcoin/WBIGAF-specific synonym expansion for query enrichment
SYNONYMS = {
    "Cantillon": "Cantillon effect inflation money printing first receivers",
    "CBDC": "CBDC central bank digital currency surveillance programmable",
    "fiat": "fiat currency government money debasement",
    "proof of work": "proof of work mining energy hashrate",
    "Satoshi": "Satoshi Nakamoto creator inventor pseudonymous",
    "hard money": "hard money sound money scarce fixed supply",
    "lightning": "lightning network layer 2 payments channels",
    "halving": "halving halvening supply schedule emission",
    "custody": "custody self-custody keys cold storage",
    "debasement": "debasement inflation money printing purchasing power",
    "cypherpunk": "cypherpunk crypto anarchism privacy digital cash",
    "scarcity": "scarcity scarce 21 million supply cap fixed",
    "censorship": "censorship resistance censorship-resistant permissionless",
    "inflation": "inflation debasement purchasing power theft hidden tax",
    "petrodollar": "petrodollar empire military reserve currency",
    "Keynesian": "Keynesian Keynes economics stimulus deficit spending",
    "Austrian": "Austrian economics Mises Hayek Rothbard",
}

mcp = FastMCP("btc-index", instructions=(
    "Bitcoin research corpus search server. Use search_corpus for semantic queries "
    "across all WBIGAF source material, scraped content, catalogs, guide articles, "
    "and blog posts. Use list_sources for an overview, get_chunk for exact retrieval, "
    "and find_related for cross-chapter discovery."
))


def get_table():
    db = lancedb.connect(DB_PATH)
    return db.open_table(TABLE_NAME)


def expand_query(query: str) -> str:
    expanded = query
    for term, expansion in SYNONYMS.items():
        if term.lower() in query.lower():
            expanded = f"{expanded} {expansion}"
            break
    return expanded


def embed_query(query: str) -> list[float] | None:
    try:
        resp = httpx.post(
            OLLAMA_URL,
            json={"model": EMBED_MODEL, "input": query},
            timeout=30.0,
        )
        if resp.status_code == 200:
            return resp.json()["embeddings"][0]
    except Exception:
        pass
    return None


def search_fts(table, query: str, top_k: int) -> list[dict]:
    try:
        return table.search(query, query_type="fts").limit(top_k).to_list()
    except Exception:
        return []


def search_vector(table, query_vec: list[float], top_k: int) -> list[dict]:
    return table.search(query_vec).limit(top_k).to_list()


def rrf_merge(lists: list[list[dict]], k: int = 60) -> list[dict]:
    """Reciprocal Rank Fusion -- deduplicated results ordered by RRF score."""
    scores = {}
    items = {}
    for result_list in lists:
        for rank, item in enumerate(result_list):
            cid = item["id"]
            scores[cid] = scores.get(cid, 0) + 1.0 / (k + rank + 1)
            items[cid] = item
    ranked = sorted(scores, key=scores.get, reverse=True)
    return [items[cid] for cid in ranked]


def apply_filters(results: list[dict], source_type: str | None,
                   chapter: int | None) -> list[dict]:
    """Post-filter results by source_type and/or chapter."""
    filtered = results
    if source_type:
        filtered = [r for r in filtered if r.get("source_type") == source_type]
    if chapter is not None:
        filtered = [r for r in filtered if r.get("chapter") == chapter]
    return filtered


def format_result(item: dict, rank: int, full: bool = True) -> str:
    heading_path = item.get("heading_path", item.get("heading", ""))
    source_type = item.get("source_type", "")
    lines = f"(lines {item['line_start']}-{item['line_end']})"

    text = item["text"]
    if not full and len(text) > 500:
        text = text[:500] + "..."

    header = f"### Result {rank}: [{source_type}] {heading_path} {lines}"
    return f"{header}\n\n{text}"


# ---------------------------------------------------------------------------
# Tool 1: search_corpus
# ---------------------------------------------------------------------------

@mcp.tool()
def search_corpus(query: str, top_k: int = 5, source_type: str = "",
                  chapter: int = 0) -> str:
    """Search the Bitcoin research corpus for relevant content.

    Uses hybrid BM25 + vector search with Reciprocal Rank Fusion.
    Returns full text for top 3 results, preview for the rest.
    Falls back to BM25-only if Ollama embedding is unavailable.

    Args:
        query: Natural language search query
        top_k: Number of results to return (default 5, max 10)
        source_type: Filter by type: wbigaf_source, catalog, scraped, research, guide, blog (empty = all)
        chapter: Filter by chapter number (0 = all chapters)
    """
    top_k = min(max(top_k, 1), 10)
    table = get_table()
    expanded = expand_query(query)

    # Fetch more than needed to allow for post-filtering
    fetch_k = top_k * 3 if (source_type or chapter) else top_k

    fts_results = search_fts(table, expanded, top_k=max(fetch_k, 15))

    query_vec = embed_query(expanded)
    if query_vec:
        vec_results = search_vector(table, query_vec, top_k=max(fetch_k, 15))
        merged = rrf_merge([fts_results, vec_results])
        mode = "hybrid (BM25 + vector)"
    else:
        merged = fts_results
        mode = "BM25-only (Ollama unavailable)"

    # Apply filters
    st_filter = source_type if source_type else None
    ch_filter = chapter if chapter else None
    if st_filter or ch_filter:
        merged = apply_filters(merged, st_filter, ch_filter)

    if not merged:
        return f"No results found for: {query}"

    results = merged[:top_k]
    parts = [f"**{len(results)} results** via {mode} for: *{query}*\n"]
    for i, item in enumerate(results):
        full_text = i < 3
        parts.append(format_result(item, i + 1, full=full_text))

    return "\n\n---\n\n".join(parts)


# ---------------------------------------------------------------------------
# Tool 2: list_sources
# ---------------------------------------------------------------------------

@mcp.tool()
def list_sources(chapter: int = 0, source_type: str = "") -> str:
    """Browse all indexed material grouped by chapter and source type.

    Returns file names, chunk counts, and summary statistics.

    Args:
        chapter: Filter to a specific chapter (0 = all)
        source_type: Filter to a specific type (empty = all)
    """
    table = get_table()
    cols = ["file", "source_type", "chapter", "sub_chapter", "heading"]
    arrow = table.to_arrow().select(cols)

    files = arrow.column("file").to_pylist()
    types = arrow.column("source_type").to_pylist()
    chapters = arrow.column("chapter").to_pylist()
    sub_chapters = arrow.column("sub_chapter").to_pylist()

    # Group: (chapter, source_type, file) -> chunk count
    groups = {}
    for f, st, ch, sc in zip(files, types, chapters, sub_chapters):
        if chapter and ch != chapter:
            continue
        if source_type and st != source_type:
            continue
        key = (ch or 0, st, f)
        groups[key] = groups.get(key, 0) + 1

    if not groups:
        return "No indexed sources match the filter."

    parts = ["# Bitcoin Index -- Corpus Overview\n"]

    # Organize by chapter
    by_chapter = {}
    for (ch, st, f), count in sorted(groups.items()):
        by_chapter.setdefault(ch, []).append((st, f, count))

    total_chunks = 0
    total_files = 0
    for ch in sorted(by_chapter):
        ch_label = f"Chapter {ch}" if ch else "Uncategorized"
        parts.append(f"\n## {ch_label}\n")

        # Group by source type within chapter
        by_type = {}
        for st, f, count in by_chapter[ch]:
            by_type.setdefault(st, []).append((f, count))

        for st in sorted(by_type):
            file_entries = by_type[st]
            type_chunks = sum(c for _, c in file_entries)
            parts.append(f"**{st}** ({len(file_entries)} files, {type_chunks} chunks)")
            for f, count in sorted(file_entries):
                parts.append(f"- {f} ({count} chunks)")
            total_chunks += type_chunks
            total_files += len(file_entries)

    parts.insert(1, f"**Total: {total_files} files, {total_chunks} chunks**\n")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Tool 3: get_chunk
# ---------------------------------------------------------------------------

@mcp.tool()
def get_chunk(file: str, heading: str = "") -> str:
    """Get a specific section from the corpus by file path and heading.

    Supports fuzzy matching if the exact heading isn't found.
    If heading is omitted, returns all chunks from that file.

    Args:
        file: File path (e.g. 'WBIGAF/3-what-problems-does-it-solve/3.1-fiat-capitalism/catalog.md')
        heading: Section heading to retrieve (e.g. 'Block 5: The Cost of Capital Is Broken')
    """
    table = get_table()

    # Normalize path separators
    file = file.replace("\\", "/")

    if not heading:
        # Return all chunks from this file
        results = table.search().where(f'file = "{file}"').limit(50).to_list()
        if not results:
            return f"File not found in index: {file}"
        parts = [f"**{len(results)} chunks from {file}**\n"]
        for item in results:
            parts.append(f"### {item['heading']}\n{item['text'][:300]}...")
        return "\n\n".join(parts)

    # Exact match
    results = table.search().where(
        f'file = "{file}" AND heading = "{heading}"'
    ).limit(1).to_list()

    if results:
        item = results[0]
        meta = f"*Type: {item['source_type']} | Ch{item['chapter']}.{item['sub_chapter']}*"
        return f"## {item['heading']}\n{meta}\n\n{item['text']}"

    # Fuzzy match within file
    file_chunks = table.search().where(f'file = "{file}"').limit(100).to_list()
    if not file_chunks:
        return f"File not found in index: {file}"

    heading_lower = heading.lower()
    best_match = None
    best_score = 0
    for chunk in file_chunks:
        h = chunk["heading"].lower()
        if heading_lower in h or h in heading_lower:
            score = len(heading_lower) / max(len(h), 1)
            if score > best_score:
                best_score = score
                best_match = chunk

    if best_match:
        meta = f"*Type: {best_match['source_type']}*"
        return (f"## {best_match['heading']} (fuzzy match)\n"
                f"{meta}\n\n{best_match['text']}")

    headings = sorted(set(c["heading"] for c in file_chunks if c["heading"] != "Preamble"))
    return (f"Heading '{heading}' not found in {file}. "
            f"Available sections:\n" + "\n".join(f"- {h}" for h in headings))


# ---------------------------------------------------------------------------
# Tool 4: find_related
# ---------------------------------------------------------------------------

@mcp.tool()
def find_related(chunk_id: str, top_k: int = 5,
                 cross_chapter: bool = True) -> str:
    """Find semantically similar chunks to a given chunk.

    Useful for cross-chapter discovery -- finding related arguments,
    evidence, or themes across the entire corpus.

    Args:
        chunk_id: The chunk ID to find related content for (from search results)
        top_k: Number of related chunks to return (default 5, max 10)
        cross_chapter: If True (default), search all chapters. If False, same chapter only.
    """
    top_k = min(max(top_k, 1), 10)
    table = get_table()

    # Look up the source chunk
    source_chunks = table.search().where(f'id = "{chunk_id}"').limit(1).to_list()
    if not source_chunks:
        return f"Chunk not found: {chunk_id}"

    source = source_chunks[0]
    source_vec = source["vector"]
    source_chapter = source.get("chapter")

    # Vector similarity search
    candidates = table.search(source_vec).limit(top_k + 5).to_list()

    # Filter out the source chunk itself
    candidates = [c for c in candidates if c["id"] != chunk_id]

    # Optionally filter to same chapter
    if not cross_chapter and source_chapter:
        candidates = [c for c in candidates if c.get("chapter") == source_chapter]

    results = candidates[:top_k]

    if not results:
        return f"No related chunks found for: {chunk_id}"

    source_label = f"{source.get('heading_path', chunk_id)}"
    parts = [f"**{len(results)} chunks related to:** *{source_label}*\n"]

    for i, item in enumerate(results):
        heading_path = item.get("heading_path", item.get("heading", ""))
        source_type = item.get("source_type", "")
        preview = item["text"][:400] + ("..." if len(item["text"]) > 400 else "")
        parts.append(
            f"### {i + 1}. [{source_type}] {heading_path}\n"
            f"*Chunk ID: {item['id']}*\n\n{preview}"
        )

    return "\n\n---\n\n".join(parts)


if __name__ == "__main__":
    mcp.run()

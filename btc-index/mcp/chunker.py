"""
Multi-source-type chunker for the btc-index corpus.

Discovers and chunks files from WBIGAF (7 source types), published guide
articles, and blog posts. Each source type has its own chunking strategy:

  - wbigaf_source: Full file (author notes, usually < 2000 words)
  - catalog:       Per ### header (argument blocks in Part 1, themes in Part 2)
  - scraped:       Per ### Link header (individual scraped articles)
  - research:      Per ## header (gap sections, discovery sections)
  - guide:         Per ## header (compendium articles)
  - blog:          Per ## header (blog posts)
  - user_note:     Per ## header, or full file if no headers (Phase 2)
"""

import hashlib
import re
from pathlib import Path

# Files that are WBIGAF pipeline artifacts (not original source content)
PIPELINE_ARTIFACTS = {"links.md", "draft.md"}

# WBIGAF-level meta files (infrastructure, not content)
WBIGAF_META_FILES = {
    "WBIGAF.md", "WBIGAF-Status.md", "TRACKER.md", "toc.md",
    "bibliography.md", "glossary.md", "wbigaf-l7-coordinator-prompt.md",
}

# Directories to skip inside WBIGAF
WBIGAF_SKIP_DIRS = {"0-project", "WBIGAF"}

# Patterns for chapter/sub-chapter extraction from directory names
CHAPTER_RE = re.compile(r"^(\d+)-")
SUBCHAPTER_RE = re.compile(r"^(\d+\.\d+)-")


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text.strip("-")


def strip_frontmatter(text: str) -> tuple[dict, str]:
    """Remove YAML frontmatter, return (metadata_dict, body_text)."""
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            fm_text = text[3:end].strip()
            body = text[end + 3:].strip()
            meta = {}
            for line in fm_text.split("\n"):
                if ":" in line:
                    key, _, value = line.partition(":")
                    value = value.strip().strip('"').strip("'")
                    meta[key.strip()] = value
            return meta, body
    return {}, text


# ---------------------------------------------------------------------------
# File discovery
# ---------------------------------------------------------------------------

def discover_files(tbb_root: Path) -> list[tuple[Path, str]]:
    """Walk the project and return (filepath, source_type) pairs."""
    files = []
    wbigaf = tbb_root / "WBIGAF"
    vault = tbb_root / "TBB"

    # WBIGAF content files
    if wbigaf.exists():
        for md in wbigaf.rglob("*.md"):
            rel = md.relative_to(wbigaf)

            # Skip planning/meta directories
            if rel.parts[0] in WBIGAF_SKIP_DIRS:
                continue

            # Skip WBIGAF-level meta files
            if md.name in WBIGAF_META_FILES:
                continue

            # Skip chapter metadata directories (transition docs, orphans)
            if any("metadata" in p for p in rel.parts):
                continue

            # Skip pipeline artifacts that aren't content
            if md.name in PIPELINE_ARTIFACTS:
                continue

            # Classify by filename
            if md.name == "catalog.md":
                files.append((md, "catalog"))
            elif md.name == "sources.md":
                files.append((md, "scraped"))
            elif md.name == "research.md":
                files.append((md, "research"))
            else:
                files.append((md, "wbigaf_source"))

    # Published compendium articles
    guide_dir = vault / "guide"
    if guide_dir.exists():
        for md in guide_dir.glob("*.md"):
            files.append((md, "guide"))

    # Blog posts (nested by year)
    posts_dir = vault / "posts"
    if posts_dir.exists():
        for md in posts_dir.rglob("*.md"):
            files.append((md, "blog"))

    return files


# ---------------------------------------------------------------------------
# Metadata extraction
# ---------------------------------------------------------------------------

def extract_wbigaf_meta(filepath: Path, wbigaf_root: Path) -> dict:
    """Extract chapter and sub-chapter numbers from WBIGAF directory path."""
    rel = filepath.relative_to(wbigaf_root)
    chapter = None
    sub_chapter = None

    for part in rel.parts:
        m = SUBCHAPTER_RE.match(part)
        if m:
            sub_chapter = m.group(1)
            chapter = int(sub_chapter.split(".")[0])
        elif chapter is None:
            m = CHAPTER_RE.match(part)
            if m:
                chapter = int(m.group(1))

    return {"chapter": chapter, "sub_chapter": sub_chapter}


def extract_guide_meta(filepath: Path) -> dict:
    """Extract chapter from guide article frontmatter."""
    text = filepath.read_text(encoding="utf-8", errors="replace")
    fm, _ = strip_frontmatter(text)
    chapter = fm.get("chapter")
    if chapter and chapter.isdigit():
        chapter = int(chapter)
    else:
        chapter = None
    return {
        "chapter": chapter,
        "sub_chapter": None,
        "title": fm.get("title", filepath.stem),
    }


def build_heading_path(source_type: str, chapter, sub_chapter, filename: str,
                       heading: str) -> str:
    """Build a human-readable path for search result display."""
    prefix = ""
    if chapter and sub_chapter:
        prefix = f"Ch{sub_chapter}"
    elif chapter:
        prefix = f"Ch{chapter}"
    elif source_type in ("guide", "blog"):
        prefix = source_type

    if prefix:
        return f"{prefix} > {filename} > {heading}"
    return f"{filename} > {heading}"


# ---------------------------------------------------------------------------
# Chunk creation
# ---------------------------------------------------------------------------

def _make_chunk(filepath: Path, tbb_root: Path, source_type: str,
                chapter, sub_chapter, heading: str,
                line_start: int, line_end: int, text: str,
                extra_meta: dict | None = None) -> dict:
    """Create a single chunk dict with full metadata."""
    rel_path = str(filepath.relative_to(tbb_root)).replace("\\", "/")
    file_stem = filepath.stem
    heading_slug = slugify(heading)

    # Unique ID: relative path slug + heading slug
    path_slug = slugify(rel_path.replace("/", "-").replace(".md", ""))
    chunk_id = f"{path_slug}__{heading_slug}" if heading_slug else path_slug

    chunk = {
        "id": chunk_id,
        "file": rel_path,
        "filename": filepath.name,
        "heading": heading,
        "heading_path": build_heading_path(
            source_type, chapter, sub_chapter, filepath.name, heading
        ),
        "line_start": line_start,
        "line_end": line_end,
        "text": text,
        "source_type": source_type,
        "chapter": chapter,
        "sub_chapter": sub_chapter or "",
        "hash": hashlib.sha256(text.encode("utf-8")).hexdigest()[:16],
    }

    if extra_meta:
        chunk.update(extra_meta)

    return chunk


# ---------------------------------------------------------------------------
# Chunking strategies by source type
# ---------------------------------------------------------------------------

def _chunk_at_header_level(lines: list[str], header_prefix: str) -> list[tuple[str, int, int, str]]:
    """Split lines at a given header level. Returns (heading, start, end, text) tuples."""
    sections = []
    current_heading = "Preamble"
    current_lines = []
    current_start = 1

    for i, line in enumerate(lines, start=1):
        if line.startswith(header_prefix) and not line.startswith(header_prefix + "#"):
            # Flush previous section
            text = "\n".join(current_lines).strip()
            if text:
                sections.append((current_heading, current_start, i - 1, text))
            current_heading = line.lstrip("#").strip()
            current_lines = [line]
            current_start = i
        else:
            current_lines.append(line)

    # Flush last section
    text = "\n".join(current_lines).strip()
    if text:
        sections.append((current_heading, current_start, len(lines), text))

    return sections


def chunk_full_file(filepath: Path, tbb_root: Path, source_type: str,
                    chapter, sub_chapter) -> list[dict]:
    """Chunk as a single unit (for source files < 2000 words)."""
    text = filepath.read_text(encoding="utf-8", errors="replace")
    _, body = strip_frontmatter(text)
    if not body.strip():
        return []
    lines = body.splitlines()
    return [_make_chunk(
        filepath, tbb_root, source_type, chapter, sub_chapter,
        filepath.stem, 1, len(lines), body
    )]


def chunk_at_h2(filepath: Path, tbb_root: Path, source_type: str,
                chapter, sub_chapter) -> list[dict]:
    """Chunk at ## headers (guide, blog, research, user_note)."""
    text = filepath.read_text(encoding="utf-8", errors="replace")
    fm, body = strip_frontmatter(text)
    if not body.strip():
        return []

    lines = body.splitlines()
    sections = _chunk_at_header_level(lines, "## ")

    # Use frontmatter title if available
    fm_chapter = fm.get("chapter")
    if fm_chapter and str(fm_chapter).isdigit():
        chapter = int(fm_chapter)

    chunks = []
    for heading, start, end, section_text in sections:
        chunks.append(_make_chunk(
            filepath, tbb_root, source_type, chapter, sub_chapter,
            heading, start, end, section_text
        ))
    return chunks


def chunk_at_h3(filepath: Path, tbb_root: Path, source_type: str,
                chapter, sub_chapter) -> list[dict]:
    """Chunk at ### headers (catalog, scraped content)."""
    text = filepath.read_text(encoding="utf-8", errors="replace")
    if not text.strip():
        return []

    lines = text.splitlines()
    sections = _chunk_at_header_level(lines, "### ")

    chunks = []
    for heading, start, end, section_text in sections:
        extra = {}
        # Extract block number from catalog headings like "Block 5: Title"
        block_match = re.match(r"Block\s+(\d+)", heading)
        if block_match:
            extra["block_num"] = int(block_match.group(1))
        # Extract link number from sources headings like "Link #4 -- Title"
        link_match = re.match(r"Link\s*#?(\d+)", heading)
        if link_match:
            extra["link_num"] = int(link_match.group(1))

        chunks.append(_make_chunk(
            filepath, tbb_root, source_type, chapter, sub_chapter,
            heading, start, end, section_text, extra
        ))
    return chunks


# Dispatch table: source_type -> chunking function
CHUNK_DISPATCH = {
    "wbigaf_source": chunk_full_file,
    "catalog": chunk_at_h3,
    "scraped": chunk_at_h3,
    "research": chunk_at_h2,
    "guide": chunk_at_h2,
    "blog": chunk_at_h2,
    "user_note": chunk_at_h2,
}


def chunk_file(filepath: Path, tbb_root: Path, source_type: str) -> list[dict]:
    """Chunk a single file using the appropriate strategy for its source type."""
    wbigaf_root = tbb_root / "WBIGAF"

    # Extract chapter/sub-chapter metadata
    if source_type in ("wbigaf_source", "catalog", "scraped", "research"):
        meta = extract_wbigaf_meta(filepath, wbigaf_root)
    elif source_type == "guide":
        meta = extract_guide_meta(filepath)
    else:
        meta = {"chapter": None, "sub_chapter": None}

    chapter = meta.get("chapter")
    sub_chapter = meta.get("sub_chapter")

    chunk_fn = CHUNK_DISPATCH.get(source_type, chunk_at_h2)
    return chunk_fn(filepath, tbb_root, source_type, chapter, sub_chapter)


def chunk_all(tbb_root: Path) -> list[dict]:
    """Discover and chunk all indexable files in the project."""
    files = discover_files(tbb_root)
    all_chunks = []
    for filepath, source_type in files:
        try:
            chunks = chunk_file(filepath, tbb_root, source_type)
            all_chunks.extend(chunks)
        except Exception as e:
            print(f"WARNING: Failed to chunk {filepath}: {e}")
    return all_chunks


if __name__ == "__main__":
    import sys
    tbb_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent.parent.parent
    print(f"Discovering files in: {tbb_root}")
    files = discover_files(tbb_root)
    print(f"Found {len(files)} files:")
    for fpath, stype in sorted(files, key=lambda x: (x[1], str(x[0]))):
        print(f"  [{stype:15s}] {fpath.relative_to(tbb_root)}")

    print(f"\nChunking all files...")
    chunks = chunk_all(tbb_root)
    print(f"Total chunks: {len(chunks)}")

    # Summary by source type
    by_type = {}
    for c in chunks:
        st = c["source_type"]
        by_type[st] = by_type.get(st, 0) + 1
    for st, count in sorted(by_type.items()):
        print(f"  {st}: {count} chunks")

"""
Normalizer for mixed-format user notes (Phase 2 -- inbox system).

Converts various input formats to clean markdown for indexing.
Currently handles:
  - .md files: pass-through (strip frontmatter if present)
  - .txt files: wrap in markdown with paragraph-based sections

Future (not yet implemented):
  - .html files: extract text via BeautifulSoup
  - .pdf files: extract text via pdfplumber/pymupdf
"""

from pathlib import Path

from chunker import strip_frontmatter


def normalize(filepath: Path) -> str:
    """Convert a file to normalized markdown text. Returns the markdown body."""
    suffix = filepath.suffix.lower()

    if suffix == ".md":
        text = filepath.read_text(encoding="utf-8", errors="replace")
        _, body = strip_frontmatter(text)
        return body

    if suffix == ".txt":
        text = filepath.read_text(encoding="utf-8", errors="replace")
        return _txt_to_markdown(text, filepath.stem)

    raise ValueError(f"Unsupported format: {suffix}. Supported: .md, .txt")


def _txt_to_markdown(text: str, title: str) -> str:
    """Convert plain text to markdown by adding a title and preserving paragraphs."""
    lines = [f"# {title}", ""]
    paragraphs = text.split("\n\n")
    for para in paragraphs:
        stripped = para.strip()
        if stripped:
            lines.append(stripped)
            lines.append("")
    return "\n".join(lines)

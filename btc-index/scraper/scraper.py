"""
Web scraper for WBIGAF source links (btc-index Phase 3).

Reads links.md for a sub-chapter, fetches each PENDING URL via httpx,
extracts readable text via html2text, writes sources.md, and updates
link statuses in links.md.

Option A design: scrape and save raw text only. Claim extraction
(catalog items #200+) is a separate pass done later by Claude.

Usage (standalone):
    python scraper.py WBIGAF/4-bitcoin-past/4.1-october-31st

Usually called by run-wave.py for batch processing.
"""

import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

import html2text
import httpx

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

TIMEOUT = 30.0
POLITE_DELAY = 1.5  # seconds between requests
MAX_CONTENT_CHARS = 20000
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

# Full browser-like headers (helps with sites that check beyond User-Agent)
BROWSER_HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;"
        "q=0.9,image/avif,image/webp,*/*;q=0.8"
    ),
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
}

# Domains known to require JS rendering (Cloudflare etc.)
# Scraper will still try but expects failure
CLOUDFLARE_DOMAINS = frozenset({
    "bitcoinmagazine.com", "www.bitcoinmagazine.com",
    "medium.com", "vijayboyapati.medium.com",
    "tomerstrolight.medium.com", "danhedl.medium.com",
    "www.reddit.com", "reddit.com", "old.reddit.com",
    "x.com", "twitter.com",
    "www.wsj.com", "wsj.com",
})

# Domains where fetching won't yield useful text
SKIP_DOMAINS = frozenset({
    "open.spotify.com", "podcasts.apple.com", "music.apple.com",
    "apps.apple.com", "play.google.com",
})

SKIP_EXTENSIONS = frozenset({
    ".mp3", ".mp4", ".wav", ".pdf", ".zip", ".tar", ".gz", ".mov", ".avi",
})

YOUTUBE_DOMAINS = frozenset({
    "youtube.com", "www.youtube.com", "youtu.be", "m.youtube.com",
})

# HTML elements to strip before conversion (reduces navigation noise)
NOISE_TAGS_RE = re.compile(
    r"<(nav|footer|aside|noscript|iframe|svg|script|style)"
    r"[\s>].*?</\1>",
    re.DOTALL | re.IGNORECASE,
)


# ---------------------------------------------------------------------------
# links.md parser
# ---------------------------------------------------------------------------

def parse_links_md(links_path: Path) -> tuple[str, list[dict]]:
    """Parse links.md and return (title, list_of_link_dicts)."""
    text = links_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    # Title from first line
    title = "Unknown"
    if lines:
        title = (
            lines[0].lstrip("# ")
            .replace(" -- Link Registry", "")
            .replace(" --- Link Registry", "")
            .strip()
        )
        # Handle em dash
        if "\u2014" in title:
            title = title.split("\u2014")[0].strip()

    # Parse table rows
    links = []
    in_table = False

    for line in lines:
        stripped = line.strip()

        # Detect header row
        if stripped.startswith("|") and ("| # |" in stripped or "|#|" in stripped):
            in_table = True
            continue

        # Skip separator row (|---|---|...)
        if in_table and stripped.startswith("|"):
            inner = stripped.strip("|")
            if all(c in "- |" for c in inner):
                continue

        # Parse data row
        if in_table and stripped.startswith("|") and stripped.endswith("|"):
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if len(cells) >= 5:
                try:
                    num = int(cells[0])
                except ValueError:
                    continue
                links.append({
                    "num": num,
                    "type": cells[1],
                    "url": cells[2],
                    "status": cells[3],
                    "notes": cells[4],
                })
        elif in_table and not stripped.startswith("|"):
            in_table = False

    return title, links


# ---------------------------------------------------------------------------
# Fetching
# ---------------------------------------------------------------------------

def _make_h2t():
    """Configure html2text converter."""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.ignore_emphasis = False
    h.body_width = 0  # no wrapping
    h.skip_internal_links = True
    h.unicode_snob = True
    h.decode_errors = "replace"
    return h


def _strip_noise(html: str) -> str:
    """Remove common noise elements from HTML before conversion."""
    return NOISE_TAGS_RE.sub("", html)


def _fetch_youtube(url: str, client: httpx.Client) -> tuple[str, str, str]:
    """Use YouTube oEmbed API to get video metadata."""
    oembed_url = f"https://www.youtube.com/oembed?url={url}&format=json"
    try:
        resp = client.get(oembed_url, timeout=15.0)
        if resp.status_code == 200:
            data = resp.json()
            title = data.get("title", "Unknown")
            author = data.get("author_name", "Unknown")
            content = (
                f"**Video Title:** {title}\n"
                f"**Channel:** {author}\n\n"
                f"*YouTube video -- transcript not available via automated scraping.*"
            )
            return "partial", content, "YouTube (metadata only via oEmbed)"
    except Exception:
        pass
    return "skipped", "", "YouTube (oEmbed failed)"


def fetch_url(
    url: str, client: httpx.Client, h2t: html2text.HTML2Text
) -> tuple[str, str, str]:
    """
    Fetch a URL and extract text.

    Returns (status, content, error_message).
    status is one of: done, partial, failed, skipped
    """
    parsed = urlparse(url)
    domain = parsed.netloc.lower().removeprefix("www.")
    path_lower = parsed.path.lower()

    # --- Pre-flight checks ---

    if domain in SKIP_DOMAINS or parsed.netloc.lower() in SKIP_DOMAINS:
        return "skipped", "", f"Audio/app platform ({domain})"

    if any(path_lower.endswith(ext) for ext in SKIP_EXTENSIONS):
        ext = path_lower.rsplit(".", 1)[-1]
        return "skipped", "", f"Direct file download (.{ext})"

    if "preview_id=" in url or "preview_nonce=" in url:
        return "skipped", "", "Preview/draft URL (not public)"

    if domain in YOUTUBE_DOMAINS or parsed.netloc.lower() in YOUTUBE_DOMAINS:
        return _fetch_youtube(url, client)

    # --- HTTP fetch with retries ---

    last_error = ""
    for attempt in range(3):
        try:
            resp = client.get(url, follow_redirects=True, timeout=TIMEOUT)

            if resp.status_code == 200:
                ct = resp.headers.get("content-type", "")
                if "text/html" not in ct and "text/plain" not in ct:
                    return "skipped", "", f"Non-text content ({ct[:40]})"

                html = resp.text
                if len(html) < 100:
                    return "partial", html, "Very short response"

                # Strip noise, convert to markdown
                clean = _strip_noise(html)
                markdown = h2t.handle(clean)

                # Clean excessive whitespace
                markdown = re.sub(r"\n{4,}", "\n\n\n", markdown)
                markdown = markdown.strip()

                if len(markdown) > MAX_CONTENT_CHARS:
                    markdown = (
                        markdown[:MAX_CONTENT_CHARS]
                        + "\n\n[... truncated at 20,000 characters ...]"
                    )

                if len(markdown) < 100:
                    return "partial", markdown, "Minimal text extracted (JS-heavy?)"

                return "done", markdown, ""

            elif resp.status_code in (403, 401):
                if domain in CLOUDFLARE_DOMAINS:
                    return "failed", "", f"HTTP {resp.status_code} (Cloudflare/JS-protected)"
                return "failed", "", f"HTTP {resp.status_code} (access denied)"
            elif resp.status_code == 404:
                return "failed", "", "HTTP 404 (page not found)"
            elif resp.status_code == 429:
                last_error = "HTTP 429 (rate limited)"
                if attempt < 2:
                    time.sleep(5 * (attempt + 1))
                    continue
            elif resp.status_code >= 500:
                last_error = f"HTTP {resp.status_code} (server error)"
                if attempt < 2:
                    time.sleep(3)
                    continue
            else:
                return "failed", "", f"HTTP {resp.status_code}"

        except httpx.TimeoutException:
            last_error = "Timeout"
            if attempt < 2:
                time.sleep(3)
                continue
        except httpx.ConnectError:
            return "failed", "", "Connection refused"
        except Exception as e:
            return "failed", "", f"{type(e).__name__}: {str(e)[:80]}"

    return "failed", "", last_error or "Max retries exceeded"


# ---------------------------------------------------------------------------
# Output: sources.md
# ---------------------------------------------------------------------------

def write_sources_md(
    sub_path: Path, results: list[dict], title: str
) -> Path:
    """Create sources.md with all scraped content."""
    sources_path = sub_path / "sources.md"

    counts = {"done": 0, "partial": 0, "failed": 0, "skipped": 0}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1

    today = datetime.now().strftime("%B %d, %Y")

    # Build per-link sections
    sections = []
    for r in results:
        domain = urlparse(r["url"]).netloc
        status_str = r["status"].upper()
        if r["error"]:
            status_str += f" ({r['error']})"

        lines = [
            f"### Link #{r['num']} -- {r['notes']}",
            "",
            f"**Source:** {domain}",
            f"**URL:** {r['url']}",
            f"**Type:** {r['type']}",
            f"**Scrape status:** {status_str}",
            "",
            "---",
            "",
        ]

        if r["content"]:
            lines.append(r["content"].strip())
        else:
            reason = r["error"] or "unknown"
            lines.append(f"*No content extracted. Reason: {reason}*")

        lines.append("")
        sections.append("\n".join(lines))

    if sources_path.exists():
        # Append new link sections to existing file
        existing = sources_path.read_text(encoding="utf-8")
        new_content = (
            existing.rstrip() + "\n\n---\n\n" + "\n\n---\n\n".join(sections)
        )
        sources_path.write_text(new_content, encoding="utf-8")
    else:
        # Create file with header
        header = "\n".join([
            f"# {title} -- Scraped Source Content",
            "",
            "## Metadata",
            "- **Purpose:** Full extracted text from each scraped link, "
            "keyed by link # from `links.md`",
            f"- **Status:** {counts['done']} DONE, {counts['partial']} PARTIAL, "
            f"{counts['failed']} FAILED, {counts['skipped']} SKIPPED",
            f"- **Last updated:** {today}",
            "",
            "---",
            "",
            "## Extracted Content",
            "",
        ])
        body = "\n\n---\n\n".join(sections)
        sources_path.write_text(header + body + "\n", encoding="utf-8")

    return sources_path


# ---------------------------------------------------------------------------
# Output: links.md status update
# ---------------------------------------------------------------------------

def update_links_md(links_path: Path, results: list[dict]):
    """Update link statuses in the links.md table in-place."""
    text = links_path.read_text(encoding="utf-8", errors="replace")

    # Map link number -> new status string
    status_map = {}
    for r in results:
        s = r["status"]
        if s == "done":
            status_map[r["num"]] = "DONE"
        elif s == "partial":
            status_map[r["num"]] = "PARTIAL"
        elif s == "skipped":
            status_map[r["num"]] = "SKIP"
        else:
            status_map[r["num"]] = "FAILED"

    new_lines = []
    for line in text.splitlines():
        if "PENDING" in line and line.strip().startswith("|"):
            parts = line.split("|")
            # Table: | # | Type | URL | Status | Notes |
            # parts: ['', ' # ', ' Type ', ' URL ', ' Status ', ' Notes ', '']
            if len(parts) >= 6:
                try:
                    num = int(parts[1].strip())
                    if num in status_map:
                        parts[4] = parts[4].replace(
                            "PENDING", status_map[num]
                        )
                        line = "|".join(parts)
                except (ValueError, IndexError):
                    pass
        new_lines.append(line)

    updated = "\n".join(new_lines)

    # Update header if no PENDING links remain in the table
    has_pending = any(
        "PENDING" in l
        for l in new_lines
        if l.strip().startswith("|") and "---" not in l
    )
    if not has_pending:
        updated = updated.replace("All PENDING", "Scrape complete")

    links_path.write_text(updated, encoding="utf-8")


# ---------------------------------------------------------------------------
# Main: scrape one sub-chapter
# ---------------------------------------------------------------------------

def scrape_sub_chapter(sub_path: Path, tbb_root: Path) -> dict:
    """
    Scrape all PENDING links for one sub-chapter.

    Returns a summary dict with counts, timing, and output path.
    Designed to be called by run-wave.py or standalone.
    """
    links_path = sub_path / "links.md"

    if not links_path.exists():
        return {"status": "skip", "reason": "No links.md"}

    title, all_links = parse_links_md(links_path)
    pending = [l for l in all_links if l["status"].upper() == "PENDING"]

    if not pending:
        return {
            "status": "skip",
            "reason": "No PENDING links",
            "total": len(all_links),
        }

    rel_path = str(sub_path.relative_to(tbb_root)).replace("\\", "/")

    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"  {rel_path}")
    print(f"  {len(pending)} PENDING of {len(all_links)} total links")
    print(f"{'=' * 60}")

    h2t = _make_h2t()
    results = []
    start_time = time.time()

    with httpx.Client(
        headers=BROWSER_HEADERS,
        follow_redirects=True,
        timeout=TIMEOUT,
    ) as client:
        for i, link in enumerate(pending, 1):
            url = link["url"]
            label = f"[{i}/{len(pending)}] #{link['num']} {link['type']}"
            url_display = url[:70] + ("..." if len(url) > 70 else "")
            print(f"  {label}: {url_display}", end="", flush=True)

            t0 = time.time()
            status, content, error = fetch_url(url, client, h2t)
            elapsed = time.time() - t0

            results.append({
                "num": link["num"],
                "type": link["type"],
                "url": url,
                "notes": link["notes"],
                "status": status,
                "content": content,
                "error": error,
            })

            tag = {
                "done": " OK",
                "partial": " PARTIAL",
                "failed": " FAIL",
                "skipped": " SKIP",
            }.get(status, " ???")
            chars = f" {len(content):,}ch" if content else ""
            reason = f" -- {error}" if error else ""
            print(f"{tag}{chars}{reason} ({elapsed:.1f}s)")

            # Polite delay between requests
            if i < len(pending):
                time.sleep(POLITE_DELAY)

    total_time = time.time() - start_time

    # Write outputs
    sources_path = write_sources_md(sub_path, results, title)
    update_links_md(links_path, results)

    summary = {
        "status": "done",
        "sub_chapter": rel_path,
        "title": title,
        "total_links": len(all_links),
        "attempted": len(pending),
        "done": sum(1 for r in results if r["status"] == "done"),
        "partial": sum(1 for r in results if r["status"] == "partial"),
        "failed": sum(1 for r in results if r["status"] == "failed"),
        "skipped": sum(1 for r in results if r["status"] == "skipped"),
        "total_chars": sum(len(r["content"]) for r in results),
        "elapsed_seconds": round(total_time, 1),
        "timestamp": datetime.now().isoformat(),
        "sources_path": str(sources_path.relative_to(tbb_root)).replace(
            "\\", "/"
        ),
    }

    print(
        f"\n  Result: {summary['done']} done, {summary['partial']} partial, "
        f"{summary['failed']} failed, {summary['skipped']} skipped"
    )
    print(
        f"  Content: {summary['total_chars']:,} chars "
        f"in {summary['elapsed_seconds']}s"
    )
    print(f"  Output: {sources_path.name}")

    return summary


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scraper.py <sub-chapter-path>")
        print(
            "Example: python scraper.py "
            "WBIGAF/4-bitcoin-past/4.1-october-31st"
        )
        sys.exit(1)

    tbb_root = Path(__file__).resolve().parent.parent.parent
    sub_path = tbb_root / sys.argv[1]

    if not sub_path.exists():
        print(f"Error: path not found: {sub_path}")
        sys.exit(1)

    result = scrape_sub_chapter(sub_path, tbb_root)
    print(f"\n{json.dumps(result, indent=2, default=str)}")

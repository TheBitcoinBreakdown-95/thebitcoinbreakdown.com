"""
Bitcoin Notes URL preparation pipeline (btc-index Phase 3B).

Extracts all URLs from 365 Bitcoin Notes .md files, normalizes them,
deduplicates against WBIGAF links.md (verified: DONE/PARTIAL status +
actual content in sources.md), and categorizes the remainder for scraping.

Usage:
    python bitcoin-notes-prep.py              # Full pipeline
    python bitcoin-notes-prep.py --dry-run    # Extract + categorize only
    python bitcoin-notes-prep.py --stats      # Just print stats

Run from btc-index/scraper/:
    ../mcp/.venv/Scripts/python.exe bitcoin-notes-prep.py
"""

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

TBB_ROOT = Path(__file__).resolve().parent.parent.parent
WBIGAF_ROOT = TBB_ROOT / "WBIGAF"
BITCOIN_NOTES_ROOT = TBB_ROOT / "Bitcoin Notes"
OUTPUT_DIR = Path(__file__).resolve().parent


# ---------------------------------------------------------------------------
# URL normalization
# ---------------------------------------------------------------------------

# Query params that are tracking/session junk (strip these)
JUNK_PARAMS = frozenset({
    "utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term",
    "ref", "source", "gi", "sk", "fbclid", "gclid", "mc_cid", "mc_eid",
    "msclkid", "s", "share", "utm_name", "utm_id",
})

# Params to keep (semantic meaning for the content)
KEEP_PARAMS = frozenset({
    "v", "t", "id", "p", "page", "q", "list", "index",
})


def normalize_url(url: str) -> str:
    """
    Normalize a URL for dedup comparison.

    - Force https
    - Lowercase scheme + domain
    - Remove www. prefix
    - Strip trailing slashes (unless root path)
    - Remove fragment/anchor
    - Strip tracking query params, keep semantic ones
    - Sort remaining query params
    """
    url = url.strip()

    # Handle angle-bracket wrapping: <url> or \<url\>
    url = url.strip("<>")
    url = url.replace("\\<", "").replace("\\>", "")

    # Remove trailing punctuation that got captured
    url = url.rstrip(".,;:!?)")

    try:
        parsed = urlparse(url)
    except Exception:
        return url.lower()

    # Force https
    scheme = "https"

    # Lowercase domain, remove www.
    netloc = parsed.netloc.lower()
    if netloc.startswith("www."):
        netloc = netloc[4:]

    # Strip fragment
    fragment = ""

    # Clean query params (domain-aware)
    if parsed.query:
        params = parse_qs(parsed.query, keep_blank_values=False)
        # Combine global + domain-specific junk params
        skip_params = set(JUNK_PARAMS)
        if any(d in netloc for d in ("twitter.com", "x.com")):
            skip_params |= TWITTER_JUNK_PARAMS
        cleaned = {}
        for k, v in params.items():
            k_lower = k.lower()
            if k_lower in skip_params:
                continue
            cleaned[k] = v[0] if len(v) == 1 else v
        # Sort for deterministic comparison
        query = urlencode(sorted(cleaned.items()), doseq=True)
    else:
        query = ""

    # Normalize path: strip trailing slash (but keep "/" for root)
    path = parsed.path
    if path != "/" and path.endswith("/"):
        path = path.rstrip("/")

    return urlunparse((scheme, netloc, path, parsed.params, query, fragment))


# ---------------------------------------------------------------------------
# URL extraction from Bitcoin Notes
# ---------------------------------------------------------------------------

# Patterns to match URLs in Markdown files
# 1. Markdown links: [text](url)
# 2. Bare URLs: https://...
# 3. Angle-bracket URLs: <url> or \<url\>
URL_PATTERNS = [
    # Markdown link: [text](url)
    re.compile(r'\[(?:[^\]]*)\]\((https?://[^)\s]+)\)'),
    # Angle brackets (possibly escaped): \<url\> or <url>
    re.compile(r'\\?<(https?://[^>\s]+)\\?>'),
    # Bare URL (not inside parens or angle brackets)
    re.compile(r'(?<![(\[<])(?:https?://[^\s)\]>"\'\\,]+)'),
]

# URLs that are clearly not articles/content worth scraping
JUNK_URL_PATTERNS = [
    re.compile(r'chatgpt\.com|chat\.openai\.com', re.I),
    re.compile(r'^https?://t\.co/', re.I),
    re.compile(r'^https?://bit\.ly/', re.I),
    re.compile(r'^https?://goo\.gl/', re.I),
    re.compile(r'localhost', re.I),
    re.compile(r'127\.0\.0\.1', re.I),
    re.compile(r'^https?://[^/]*\.local\b', re.I),
    re.compile(r'app\.slack\.com', re.I),
    re.compile(r'notion\.so', re.I),
    re.compile(r'docs\.google\.com', re.I),
    re.compile(r'drive\.google\.com', re.I),
]

# Twitter-specific tracking params (the 't' param is a hash, not semantic)
TWITTER_JUNK_PARAMS = frozenset({
    "t", "ref_src", "ref_url", "twcamp", "twterm", "twgr", "twcon",
    "s", "cxt",
})


def extract_urls_from_file(filepath: Path) -> list[dict]:
    """Extract all URLs from a single Markdown file."""
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []

    urls = []
    seen_in_file = set()

    for pattern in URL_PATTERNS:
        for match in pattern.finditer(text):
            raw = match.group(1) if match.lastindex else match.group(0)
            raw = raw.strip()

            # Clean up common artifacts
            raw = raw.rstrip(".,;:!?)")
            raw = raw.replace("\\>", "").replace("\\<", "")

            if not raw.startswith("http"):
                continue

            # Skip obvious non-URLs
            if len(raw) < 15:
                continue

            normalized = normalize_url(raw)

            # Dedup within file
            if normalized in seen_in_file:
                continue
            seen_in_file.add(normalized)

            urls.append({
                "raw": raw,
                "normalized": normalized,
                "source_file": str(filepath.relative_to(BITCOIN_NOTES_ROOT)),
            })

    return urls


def extract_all_urls() -> list[dict]:
    """Extract URLs from all Bitcoin Notes .md files."""
    all_urls = []

    for md_file in sorted(BITCOIN_NOTES_ROOT.rglob("*.md")):
        urls = extract_urls_from_file(md_file)
        all_urls.extend(urls)

    # Also check .txt files (CYPHERNOMICON.txt has 25 URLs)
    for txt_file in sorted(BITCOIN_NOTES_ROOT.rglob("*.txt")):
        urls = extract_urls_from_file(txt_file)
        all_urls.extend(urls)

    return all_urls


# ---------------------------------------------------------------------------
# WBIGAF verified scrape state
# ---------------------------------------------------------------------------

def parse_links_table(links_path: Path) -> list[dict]:
    """Parse a WBIGAF links.md table. Returns list of link dicts."""
    try:
        text = links_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []

    links = []
    in_table = False

    for line in text.splitlines():
        stripped = line.strip()

        if stripped.startswith("|") and ("| # |" in stripped or "|#|" in stripped):
            in_table = True
            continue

        if in_table and stripped.startswith("|"):
            inner = stripped.strip("|")
            if all(c in "- |" for c in inner):
                continue

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
                    "status": cells[3].upper(),
                    "notes": cells[4],
                    "sub_chapter": str(links_path.parent.relative_to(TBB_ROOT)),
                })
        elif in_table and not stripped.startswith("|"):
            in_table = False

    return links


def verify_source_content(sources_path: Path, link_num: int) -> bool:
    """
    Check if sources.md has real content for a given link number.

    Returns True if the Link #N section exists and contains more than
    just the metadata header (i.e., has actual scraped text).
    """
    if not sources_path.exists():
        return False

    try:
        text = sources_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return False

    # Find the section for this link number
    # Pattern: ### Link #N --
    section_pattern = re.compile(
        rf'^### Link #{link_num}\b.*$', re.MULTILINE
    )
    match = section_pattern.search(text)
    if not match:
        return False

    # Get text from this section to the next ### or end of file
    start = match.end()
    next_section = re.search(r'^### Link #\d+', text[start:], re.MULTILINE)
    if next_section:
        section_text = text[start:start + next_section.start()]
    else:
        section_text = text[start:]

    # Strip metadata lines and check for actual content
    # Metadata lines: **Source:**, **URL:**, **Type:**, **Scrape status:**
    content_lines = []
    for line in section_text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("**Source:**"):
            continue
        if stripped.startswith("**URL:**"):
            continue
        if stripped.startswith("**Type:**"):
            continue
        if stripped.startswith("**Scrape status:**"):
            continue
        if stripped == "---":
            continue
        if stripped.startswith("*No content extracted"):
            return False
        content_lines.append(stripped)

    # Need at least some real content (not just metadata)
    total_chars = sum(len(l) for l in content_lines)
    return total_chars > 50


def build_wbigaf_verified_urls() -> dict[str, dict]:
    """
    Build a map of normalized_url -> info for all WBIGAF links
    that are DONE or PARTIAL with verified content in sources.md.

    Returns: {normalized_url: {sub_chapter, num, status, notes, verified}}
    """
    verified = {}

    for links_path in sorted(WBIGAF_ROOT.rglob("links.md")):
        sub_dir = links_path.parent
        sources_path = sub_dir / "sources.md"

        links = parse_links_table(links_path)
        for link in links:
            if link["status"] not in ("DONE", "PARTIAL"):
                continue

            normalized = normalize_url(link["url"])
            has_content = verify_source_content(sources_path, link["num"])

            if has_content:
                verified[normalized] = {
                    "sub_chapter": link["sub_chapter"],
                    "num": link["num"],
                    "status": link["status"],
                    "notes": link["notes"],
                }

    return verified


# ---------------------------------------------------------------------------
# URL categorization
# ---------------------------------------------------------------------------

YOUTUBE_DOMAINS = frozenset({
    "youtube.com", "youtu.be", "m.youtube.com",
})

TWITTER_DOMAINS = frozenset({
    "x.com", "twitter.com",
})

MEDIUM_DOMAINS = frozenset({
    "medium.com",
})

GITHUB_DOMAINS = frozenset({
    "github.com", "gist.github.com",
})

PAYWALL_DOMAINS = frozenset({
    "wsj.com", "barrons.com", "ft.com", "marketwatch.com",
    "bloomberg.com", "nytimes.com", "economist.com",
    "washingtonpost.com",
})

PODCAST_DOMAINS = frozenset({
    "open.spotify.com", "podcasts.apple.com", "music.apple.com",
    "apps.apple.com", "play.google.com", "anchor.fm",
})

IMAGE_EXTENSIONS = frozenset({
    ".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".ico",
})

BINARY_EXTENSIONS = frozenset({
    ".mp3", ".mp4", ".wav", ".pdf", ".zip", ".tar", ".gz",
    ".mov", ".avi", ".mkv", ".exe", ".dmg",
})


def categorize_url(url: str) -> str:
    """Categorize a normalized URL into a scraping bucket."""
    try:
        parsed = urlparse(url)
    except Exception:
        return "junk"

    domain = parsed.netloc.lower()
    path_lower = parsed.path.lower()

    # Check junk patterns
    for pattern in JUNK_URL_PATTERNS:
        if pattern.search(url):
            return "junk"

    # Domain-based categories
    if domain in YOUTUBE_DOMAINS:
        return "youtube"

    if domain in TWITTER_DOMAINS:
        # Split actual tweets (/status/) from profile links
        if "/status/" in path_lower:
            return "tweet"
        return "tweet_profile"

    if domain in PAYWALL_DOMAINS:
        return "paywalled"
    if domain in PODCAST_DOMAINS:
        return "podcast"
    if domain in GITHUB_DOMAINS:
        return "github"

    # Medium: check both domain and subdomain pattern
    if domain in MEDIUM_DOMAINS or domain.endswith(".medium.com"):
        return "medium"

    # File extensions
    ext = Path(path_lower).suffix
    if ext in IMAGE_EXTENSIONS:
        return "image"
    if ext in BINARY_EXTENSIONS:
        return "binary"

    # Reddit (often blocked)
    if "reddit.com" in domain:
        return "reddit"

    # Everything else is potentially scrapable
    return "scrapable"


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def run_pipeline(dry_run: bool = False, stats_only: bool = False):
    """Execute the full preparation pipeline."""

    print("\n" + "=" * 60)
    print("  Bitcoin Notes URL Preparation Pipeline")
    print("  Phase 3B -- btc-index")
    print("=" * 60)

    # Step 1: Extract all URLs
    print("\n[1/4] Extracting URLs from Bitcoin Notes...")
    all_urls = extract_all_urls()
    print(f"  Raw extractions: {len(all_urls)} URLs from {BITCOIN_NOTES_ROOT}")

    # Step 2: Global dedup (same URL from multiple notes)
    print("\n[2/4] Deduplicating...")
    unique_map = {}  # normalized -> list of source files
    for entry in all_urls:
        norm = entry["normalized"]
        if norm not in unique_map:
            unique_map[norm] = {
                "normalized": norm,
                "raw_examples": [entry["raw"]],
                "source_files": [entry["source_file"]],
            }
        else:
            if entry["raw"] not in unique_map[norm]["raw_examples"]:
                unique_map[norm]["raw_examples"].append(entry["raw"])
            if entry["source_file"] not in unique_map[norm]["source_files"]:
                unique_map[norm]["source_files"].append(entry["source_file"])

    print(f"  Unique URLs (after normalization): {len(unique_map)}")

    # Step 3: Check against WBIGAF verified corpus
    print("\n[3/4] Building WBIGAF verified scrape state...")
    wbigaf_verified = build_wbigaf_verified_urls()
    print(f"  WBIGAF verified URLs (DONE/PARTIAL with content): {len(wbigaf_verified)}")

    # Find overlaps
    already_scraped = {}
    new_urls = {}
    for norm, info in unique_map.items():
        if norm in wbigaf_verified:
            already_scraped[norm] = {
                **info,
                "wbigaf": wbigaf_verified[norm],
            }
        else:
            new_urls[norm] = info

    print(f"  Already scraped in WBIGAF (verified): {len(already_scraped)}")
    print(f"  New URLs to process: {len(new_urls)}")

    # Step 4: Categorize new URLs
    print("\n[4/4] Categorizing new URLs...")
    categories = defaultdict(list)
    for norm, info in new_urls.items():
        cat = categorize_url(norm)
        categories[cat].append({**info, "category": cat})

    print("\n  Category breakdown:")
    for cat in sorted(categories.keys(), key=lambda c: -len(categories[c])):
        print(f"    {cat:15s} {len(categories[cat]):5d}")

    total_new = sum(len(v) for v in categories.values())
    scrapable_count = len(categories.get("scrapable", []))
    tweet_count = len(categories.get("tweet", []))
    medium_count = len(categories.get("medium", []))

    # Summary
    print("\n" + "-" * 60)
    print("  SUMMARY")
    print("-" * 60)
    print(f"  Total extracted:              {len(all_urls)}")
    print(f"  Unique (normalized):          {len(unique_map)}")
    print(f"  Already in WBIGAF (verified): {len(already_scraped)}")
    print(f"  New to process:               {total_new}")
    print(f"    Scrapable (httpx+Patchright):{scrapable_count:5d}")
    print(f"    Tweets (browser):            {tweet_count:5d}")
    print(f"    Medium (Apify):              {medium_count:5d}")
    print(f"    Skip (YT/paywall/etc.):      "
          f"{total_new - scrapable_count - tweet_count - medium_count:5d}")
    print("-" * 60)

    if stats_only:
        return

    # Write output files
    output = {
        "pipeline": "bitcoin-notes-prep",
        "stats": {
            "total_extracted": len(all_urls),
            "unique_normalized": len(unique_map),
            "already_in_wbigaf": len(already_scraped),
            "new_to_process": total_new,
        },
        "categories": {
            cat: len(urls) for cat, urls in categories.items()
        },
        "already_scraped": [
            {
                "url": norm,
                "wbigaf_sub": info["wbigaf"]["sub_chapter"],
                "wbigaf_link": info["wbigaf"]["num"],
                "wbigaf_status": info["wbigaf"]["status"],
            }
            for norm, info in sorted(already_scraped.items())
        ],
    }

    # Write categorized URL lists for the scraper
    for cat in ["scrapable", "tweet", "medium", "github", "reddit"]:
        urls_in_cat = categories.get(cat, [])
        output[f"{cat}_urls"] = [
            {
                "url": u["normalized"],
                "source_files": u["source_files"],
                "raw_examples": u["raw_examples"][:2],
            }
            for u in sorted(urls_in_cat, key=lambda x: x["normalized"])
        ]

    # Write skip categories (for reference)
    skip_cats = ["youtube", "paywalled", "podcast", "image", "binary", "junk",
                 "tweet_profile"]
    output["skipped_urls"] = [
        {
            "url": u["normalized"],
            "category": u["category"],
        }
        for cat in skip_cats
        for u in sorted(categories.get(cat, []), key=lambda x: x["normalized"])
    ]

    output_path = OUTPUT_DIR / "bitcoin-notes-urls.json"
    output_path.write_text(
        json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"\n  Output written: {output_path.name}")

    if not dry_run:
        # Also write a simple scrapable URL list (one per line) for easy piping
        scrapable_list_path = OUTPUT_DIR / "bitcoin-notes-scrapable.txt"
        scrapable_urls = [u["normalized"] for u in categories.get("scrapable", [])]
        scrapable_list_path.write_text(
            "\n".join(sorted(scrapable_urls)) + "\n", encoding="utf-8"
        )
        print(f"  Scrapable URL list: {scrapable_list_path.name} ({len(scrapable_urls)} URLs)")

        # Write tweet URL list
        tweet_list_path = OUTPUT_DIR / "bitcoin-notes-tweets.txt"
        tweet_urls = [u["normalized"] for u in categories.get("tweet", [])]
        tweet_list_path.write_text(
            "\n".join(sorted(tweet_urls)) + "\n", encoding="utf-8"
        )
        print(f"  Tweet URL list: {tweet_list_path.name} ({len(tweet_urls)} URLs)")

        # Write medium URL list
        medium_list_path = OUTPUT_DIR / "bitcoin-notes-medium.txt"
        medium_urls = [u["normalized"] for u in categories.get("medium", [])]
        medium_list_path.write_text(
            "\n".join(sorted(medium_urls)) + "\n", encoding="utf-8"
        )
        print(f"  Medium URL list: {medium_list_path.name} ({len(medium_urls)} URLs)")

    return output


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Bitcoin Notes URL preparation pipeline"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Extract and categorize but don't write URL lists",
    )
    parser.add_argument(
        "--stats", action="store_true",
        help="Print stats only, no file output",
    )
    args = parser.parse_args()

    run_pipeline(dry_run=args.dry_run, stats_only=args.stats)

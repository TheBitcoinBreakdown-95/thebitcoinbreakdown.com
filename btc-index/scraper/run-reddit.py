"""
Reddit URL scraping via old.reddit.com + JSON API (btc-index Phase 3B).

Fetches Reddit thread content by:
1. Trying the Reddit JSON API (append .json to URL)
2. Falling back to old.reddit.com HTML scraping via httpx

Outputs to btc-index/scraped/.

Usage:
    python run-reddit.py              # Scrape all Reddit URLs
    python run-reddit.py --dry-run    # Show plan
    python run-reddit.py --resume     # Skip already-scraped

Run from btc-index/scraper/:
    ../mcp/.venv/Scripts/python.exe run-reddit.py
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

sys.path.insert(0, str(Path(__file__).parent))
import importlib
_bn = importlib.import_module("run-bitcoin-notes")
slugify = _bn.slugify
write_scraped_file = _bn.write_scraped_file
find_already_scraped = _bn.find_already_scraped
from scraper import BROWSER_HEADERS, _make_h2t, _strip_noise

SCRAPER_DIR = Path(__file__).resolve().parent
URLS_JSON = SCRAPER_DIR / "bitcoin-notes-urls.json"

# Reddit JSON API headers
REDDIT_HEADERS = {
    "User-Agent": "btc-index-scraper/1.0 (educational Bitcoin research by u/none)",
    "Accept": "application/json",
}

SKIP_PATTERNS = ["/video/", "/gallery/", "/i.redd.it/"]


def is_video_url(url: str) -> bool:
    """Check if this is a Reddit video/media URL (not a discussion)."""
    return any(p in url for p in SKIP_PATTERNS)


def rewrite_to_json_api(url: str) -> str:
    """Convert a Reddit URL to its JSON API endpoint."""
    # Normalize to www.reddit.com
    url = re.sub(r'https?://(old\.|www\.)?reddit\.com', 'https://www.reddit.com', url)
    # Strip query params and trailing slash
    url = url.split("?")[0].rstrip("/")
    # Append .json
    return url + ".json"


def fetch_reddit_json(url: str, client: httpx.Client) -> tuple[str, str, str]:
    """Fetch a Reddit thread via the JSON API."""
    json_url = rewrite_to_json_api(url)

    try:
        resp = client.get(json_url, headers=REDDIT_HEADERS, timeout=15.0)

        if resp.status_code == 200:
            data = resp.json()

            # Reddit returns a list of listings
            if isinstance(data, list) and len(data) >= 1:
                # First listing = post
                post_data = data[0].get("data", {}).get("children", [{}])[0].get("data", {})
                title = post_data.get("title", "")
                selftext = post_data.get("selftext", "")
                author = post_data.get("author", "[deleted]")
                subreddit = post_data.get("subreddit_name_prefixed", "")
                score = post_data.get("score", 0)
                num_comments = post_data.get("num_comments", 0)

                parts = [
                    f"**{title}**",
                    f"*{subreddit} -- u/{author} -- {score} points, {num_comments} comments*",
                    "",
                ]

                if selftext:
                    parts.append(selftext)
                else:
                    # Link post
                    link_url = post_data.get("url", "")
                    parts.append(f"*Link post:* {link_url}")

                # Top comments (if second listing exists)
                if len(data) >= 2:
                    comments = data[1].get("data", {}).get("children", [])
                    top_comments = [
                        c for c in comments[:10]
                        if c.get("kind") == "t1"
                    ]
                    if top_comments:
                        parts.append("\n---\n\n**Top Comments:**\n")
                        for c in top_comments[:5]:
                            cd = c.get("data", {})
                            cauthor = cd.get("author", "[deleted]")
                            cbody = cd.get("body", "")
                            cscore = cd.get("score", 0)
                            if cbody and cauthor != "[deleted]":
                                parts.append(f"**u/{cauthor}** ({cscore} pts):\n{cbody}\n")

                content = "\n".join(parts)
                if len(content) > 20000:
                    content = content[:20000] + "\n\n[... truncated ...]"

                return "done", content, ""

            return "failed", "", "Unexpected JSON structure"

        elif resp.status_code == 403:
            return "failed", "", "Reddit API 403 (rate limited or blocked)"
        elif resp.status_code == 404:
            return "failed", "", "Reddit 404 (post deleted)"
        elif resp.status_code == 429:
            return "failed", "", "Reddit 429 (rate limited)"
        else:
            return "failed", "", f"Reddit HTTP {resp.status_code}"

    except httpx.TimeoutException:
        return "failed", "", "Timeout"
    except json.JSONDecodeError:
        return "failed", "", "Invalid JSON response"
    except Exception as e:
        return "failed", "", str(e)[:80]


def fetch_reddit_oldhtml(url: str, client: httpx.Client) -> tuple[str, str, str]:
    """Fallback: fetch via old.reddit.com HTML."""
    old_url = re.sub(
        r'https?://(www\.)?reddit\.com', 'https://old.reddit.com', url
    )

    try:
        resp = client.get(
            old_url,
            headers=BROWSER_HEADERS,
            follow_redirects=True,
            timeout=15.0,
        )
        if resp.status_code == 200:
            h2t = _make_h2t()
            clean = _strip_noise(resp.text)
            markdown = h2t.handle(clean)
            markdown = re.sub(r"\n{4,}", "\n\n\n", markdown).strip()

            if len(markdown) > 20000:
                markdown = markdown[:20000] + "\n\n[... truncated ...]"

            if len(markdown) < 100:
                return "partial", markdown, "Minimal content from old.reddit.com"

            return "done", markdown, ""
        return "failed", "", f"old.reddit.com HTTP {resp.status_code}"
    except Exception as e:
        return "failed", "", f"old.reddit.com error: {str(e)[:60]}"


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Reddit URL scraping")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    data = json.loads(URLS_JSON.read_text(encoding="utf-8"))
    urls = data.get("reddit_urls", [])

    if not urls:
        print("No Reddit URLs found.")
        return

    already_done = set()
    if args.resume:
        already_done = find_already_scraped()

    # Classify
    actionable = []
    skipped = []
    for entry in urls:
        url = entry["url"] if isinstance(entry, dict) else entry
        source_files = entry.get("source_files", []) if isinstance(entry, dict) else []
        if url in already_done:
            continue
        if is_video_url(url):
            skipped.append(url)
            continue
        actionable.append({"url": url, "source_files": source_files})

    print(f"\n{'#' * 60}")
    print(f"  REDDIT SCRAPING")
    print(f"  Total URLs: {len(urls)}")
    print(f"  Actionable: {len(actionable)}")
    print(f"  Skipped (video/media): {len(skipped)}")
    print(f"{'#' * 60}")

    if args.dry_run:
        for a in actionable:
            print(f"  {a['url']}")
        return

    results = []
    start = time.time()

    with httpx.Client(follow_redirects=True, timeout=15.0) as client:
        for i, entry in enumerate(actionable, 1):
            url = entry["url"]
            source_files = entry["source_files"]
            print(f"  [{i}/{len(actionable)}] {url[:75]}", end="", flush=True)

            t0 = time.time()

            # Try JSON API first
            status, content, error = fetch_reddit_json(url, client)

            # Fallback to old.reddit.com HTML
            if status == "failed":
                status, content, error = fetch_reddit_oldhtml(url, client)

            elapsed = time.time() - t0

            write_scraped_file(url, content, status, "reddit", source_files, error)
            results.append({"url": url, "status": status, "chars": len(content), "error": error})

            tag = {"done": " OK", "partial": " PARTIAL", "failed": " FAIL"}.get(status, " ???")
            chars = f" {len(content):,}ch" if content else ""
            reason = f" -- {error}" if error else ""
            print(f"{tag}{chars}{reason} ({elapsed:.1f}s)")

            if i < len(actionable):
                time.sleep(2.0)  # Reddit rate limit is strict

    total_time = time.time() - start
    done = sum(1 for r in results if r["status"] == "done")
    failed = sum(1 for r in results if r["status"] == "failed")
    total_chars = sum(r["chars"] for r in results)

    print(f"\n{'#' * 60}")
    print(f"  REDDIT COMPLETE: {done} done, {failed} failed")
    print(f"  Content: {total_chars:,} chars in {total_time:.1f}s")
    print(f"{'#' * 60}")


if __name__ == "__main__":
    main()

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

# Patchright (stealth Playwright fork) -- loaded lazily for browser fallback
_pw_context_manager = None
_pw_browser = None


def _get_browser():
    """Lazily launch a Patchright Chromium instance (reused across calls)."""
    global _pw_context_manager, _pw_browser
    if _pw_browser is None:
        from patchright.sync_api import sync_playwright
        _pw_context_manager = sync_playwright()
        pw = _pw_context_manager.start()
        _pw_browser = pw.chromium.launch(headless=True)
    return _pw_browser


def close_browser():
    """Clean up browser resources. Call at end of wave."""
    global _pw_context_manager, _pw_browser
    if _pw_browser is not None:
        try:
            _pw_browser.close()
        except Exception:
            pass
        _pw_browser = None
    if _pw_context_manager is not None:
        try:
            _pw_context_manager.__exit__(None, None, None)
        except Exception:
            pass
        _pw_context_manager = None

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

TWITTER_DOMAINS = frozenset({
    "x.com", "twitter.com", "www.twitter.com",
})

# Domains worth retrying with a real browser on httpx failure
BROWSER_RETRY_DOMAINS = CLOUDFLARE_DOMAINS | TWITTER_DOMAINS | frozenset({
    "en.wikipedia.org", "www.cnbc.com", "cnbc.com",
    "fee.org", "www.fee.org", "mises.org", "www.mises.org",
    "dergigi.com", "www.dergigi.com",
    "quillette.com", "www.quillette.com",
    "www.investopedia.com", "investopedia.com",
    "www.forbes.com", "forbes.com",
})

# Truly paywalled -- don't waste browser time
PAYWALL_DOMAINS = frozenset({
    "www.wsj.com", "wsj.com",
    "www.barrons.com", "barrons.com",
    "www.ft.com", "ft.com",
    "www.marketwatch.com", "marketwatch.com",
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


def _fetch_tweet_fxtwitter(url: str) -> tuple[str, str, str]:
    """Fetch tweet text via fxtwitter public API (no auth, ~0.5s)."""
    match = re.search(r'(?:x\.com|twitter\.com)/(\w+)/status/(\d+)', url)
    if not match:
        return "failed", "", "Could not parse tweet URL"

    handle, status_id = match.group(1), match.group(2)

    try:
        resp = httpx.get(
            f"https://api.fxtwitter.com/{handle}/status/{status_id}",
            headers={"User-Agent": USER_AGENT},
            timeout=15.0,
        )
        if resp.status_code == 200:
            tweet = resp.json().get("tweet", {})
            text = tweet.get("text", "")
            # Strip t.co tracking links
            text = re.sub(r'https://t\.co/\w+', '', text).strip()
            if not text:
                return "failed", "", "fxtwitter returned empty text"

            author = tweet.get("author", {})
            name = author.get("name", handle)
            content = f"**@{handle}** ({name})\n\n{text}"
            return "done", content, ""
        elif resp.status_code == 404:
            return "failed", "", "Tweet not found (deleted or private)"
        else:
            return "failed", "", f"fxtwitter HTTP {resp.status_code}"
    except Exception as e:
        return "failed", "", f"fxtwitter error: {str(e)[:80]}"


_THREAD_PATTERN = re.compile(
    r'(?:^|\s)1/\s*$'       # ends with "1/"
    r'|(?:^|\s)\(1/\d+\)'   # contains "(1/N)"
    r'|^1/\d+\s'            # starts with "1/N "
    r'|\bthread\b'          # contains "thread"
)


def _is_thread_start(text: str) -> bool:
    """Detect if tweet text looks like the start of a multi-tweet thread."""
    return bool(_THREAD_PATTERN.search(text.lower()))


def _fetch_thread_browser(url: str) -> tuple[str, str, str]:
    """Fetch a full tweet thread via Patchright browser."""
    context = None
    try:
        browser = _get_browser()
        context = browser.new_context(
            user_agent=USER_AGENT,
            viewport={"width": 1280, "height": 900},
        )
        page = context.new_page()

        page.goto(url, wait_until="domcontentloaded", timeout=30000)
        page.wait_for_selector(
            '[data-testid="tweetText"]', timeout=15000
        )
        page.wait_for_timeout(2000)

        articles = page.query_selector_all("article")
        tweets = []
        username_match = re.search(
            r'(?:x\.com|twitter\.com)/([^/]+)/status', url
        )
        username = username_match.group(1) if username_match else "unknown"

        for article in articles:
            el = article.query_selector('[data-testid="tweetText"]')
            if el:
                tweets.append(el.inner_text())

        context.close()
        context = None

        if not tweets:
            return "failed", "", "No tweet text found in browser"

        content = f"**@{username}** (tweet thread)\n\n"
        for i, t in enumerate(tweets, 1):
            content += f"**Tweet {i}:**\n{t}\n\n"

        return "done", content.strip(), ""

    except Exception as e:
        if context is not None:
            try:
                context.close()
            except Exception:
                pass
        err = str(e)[:120]
        if "Timeout" in err:
            return "failed", "", "Browser timeout"
        return "failed", "", f"Browser error: {err}"


def fetch_tweet(url: str) -> tuple[str, str, str]:
    """Fetch a tweet: fxtwitter API first, Patchright browser for threads."""
    status, content, error = _fetch_tweet_fxtwitter(url)

    if status == "failed":
        # fxtwitter failed entirely -- try browser as last resort
        return _fetch_thread_browser(url)

    # fxtwitter succeeded -- check if this is a thread start
    if _is_thread_start(content):
        # Try browser to get the full thread
        b_status, b_content, b_error = _fetch_thread_browser(url)
        if b_status == "done" and len(b_content) > len(content):
            return b_status, b_content, b_error
        # Browser failed or got less -- keep fxtwitter text, mark partial
        return "partial", content, "Thread detected, only first tweet captured"

    return status, content, error


def fetch_url_browser(url: str) -> tuple[str, str, str]:
    """Fetch a JS-rendered page using Patchright (stealth Chromium)."""
    context = None
    try:
        browser = _get_browser()
        context = browser.new_context(
            user_agent=USER_AGENT,
            viewport={"width": 1280, "height": 900},
        )
        page = context.new_page()

        page.goto(url, wait_until="networkidle", timeout=30000)
        # Extra wait for JS-heavy pages
        page.wait_for_timeout(2000)

        html = page.content()
        context.close()
        context = None

        if len(html) < 200:
            return "failed", "", "Browser got empty/minimal page"

        # Reuse the same html2text pipeline
        h2t = _make_h2t()
        clean = _strip_noise(html)
        markdown = h2t.handle(clean)
        markdown = re.sub(r"\n{4,}", "\n\n\n", markdown)
        markdown = markdown.strip()

        if len(markdown) > MAX_CONTENT_CHARS:
            markdown = (
                markdown[:MAX_CONTENT_CHARS]
                + "\n\n[... truncated at 20,000 characters ...]"
            )

        if len(markdown) < 100:
            return "partial", markdown, "Minimal text after browser render"

        return "done", markdown, ""

    except Exception as e:
        if context is not None:
            try:
                context.close()
            except Exception:
                pass
        err = str(e)[:120]
        if "Timeout" in err or "timeout" in err:
            return "failed", "", "Browser timeout"
        return "failed", "", f"Browser error: {err}"


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

def update_links_md(links_path: Path, results: list[dict],
                    retry_mode: bool = False):
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

    # Which old statuses to replace
    old_markers = {"FAILED"} if retry_mode else {"PENDING"}

    new_lines = []
    for line in text.splitlines():
        if line.strip().startswith("|") and any(
            m in line for m in old_markers
        ):
            parts = line.split("|")
            if len(parts) >= 6:
                try:
                    num = int(parts[1].strip())
                    if num in status_map:
                        for m in old_markers:
                            parts[4] = parts[4].replace(
                                m, status_map[num]
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

def scrape_sub_chapter(
    sub_path: Path, tbb_root: Path, retry_failed: bool = False
) -> dict:
    """
    Scrape links for one sub-chapter.

    When retry_failed=False (default): processes PENDING links via httpx.
    When retry_failed=True: re-processes FAILED links using Patchright
    browser fallback (tweets get dedicated handler).

    Returns a summary dict with counts, timing, and output path.
    Designed to be called by run-wave.py or standalone.
    """
    links_path = sub_path / "links.md"

    if not links_path.exists():
        return {"status": "skip", "reason": "No links.md"}

    title, all_links = parse_links_md(links_path)

    if retry_failed:
        target_status = "FAILED"
        targets = [l for l in all_links if l["status"].upper() == "FAILED"]
    else:
        target_status = "PENDING"
        targets = [l for l in all_links if l["status"].upper() == "PENDING"]

    if not targets:
        return {
            "status": "skip",
            "reason": f"No {target_status} links",
            "total": len(all_links),
        }

    rel_path = str(sub_path.relative_to(tbb_root)).replace("\\", "/")
    mode_label = "RETRY (browser)" if retry_failed else "SCRAPE (httpx)"

    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"  {rel_path}")
    print(f"  {len(targets)} {target_status} of {len(all_links)} total [{mode_label}]")
    print(f"{'=' * 60}")

    h2t = _make_h2t()
    results = []
    start_time = time.time()

    if retry_failed:
        # Browser-based retry path
        for i, link in enumerate(targets, 1):
            url = link["url"]
            parsed = urlparse(url)
            domain = parsed.netloc.lower().removeprefix("www.")
            label = f"[{i}/{len(targets)}] #{link['num']} {link['type']}"
            url_display = url[:70] + ("..." if len(url) > 70 else "")
            print(f"  {label}: {url_display}", end="", flush=True)

            t0 = time.time()

            # Skip paywalled and truly dead domains
            if domain in PAYWALL_DOMAINS or parsed.netloc.lower() in PAYWALL_DOMAINS:
                status, content, error = (
                    "skipped", "", f"Paywalled ({domain})"
                )
            elif domain in SKIP_DOMAINS or parsed.netloc.lower() in SKIP_DOMAINS:
                status, content, error = (
                    "skipped", "", f"Audio/app platform ({domain})"
                )
            elif any(parsed.path.lower().endswith(ext) for ext in SKIP_EXTENSIONS):
                status, content, error = (
                    "skipped", "", "Direct file download"
                )
            elif domain in YOUTUBE_DOMAINS or parsed.netloc.lower() in YOUTUBE_DOMAINS:
                # Keep YouTube as metadata-only
                with httpx.Client(
                    headers=BROWSER_HEADERS, timeout=TIMEOUT
                ) as yt_client:
                    status, content, error = _fetch_youtube(url, yt_client)
            elif (
                domain in TWITTER_DOMAINS
                or parsed.netloc.lower() in TWITTER_DOMAINS
            ):
                status, content, error = fetch_tweet(url)
            else:
                status, content, error = fetch_url_browser(url)

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

            if i < len(targets):
                time.sleep(POLITE_DELAY)
    else:
        # Original httpx path
        with httpx.Client(
            headers=BROWSER_HEADERS,
            follow_redirects=True,
            timeout=TIMEOUT,
        ) as client:
            for i, link in enumerate(targets, 1):
                url = link["url"]
                label = f"[{i}/{len(targets)}] #{link['num']} {link['type']}"
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

                if i < len(targets):
                    time.sleep(POLITE_DELAY)

    total_time = time.time() - start_time

    # Write outputs
    sources_path = write_sources_md(sub_path, results, title)
    update_links_md(links_path, results, retry_mode=retry_failed)

    summary = {
        "status": "done",
        "sub_chapter": rel_path,
        "title": title,
        "total_links": len(all_links),
        "attempted": len(targets),
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
        "mode": "retry" if retry_failed else "scrape",
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
    import argparse as _ap
    _parser = _ap.ArgumentParser(description="Scrape one sub-chapter")
    _parser.add_argument("path", help="Sub-chapter path relative to TBB root")
    _parser.add_argument(
        "--retry-failed", action="store_true",
        help="Re-process FAILED links using Patchright browser fallback",
    )
    _args = _parser.parse_args()

    tbb_root = Path(__file__).resolve().parent.parent.parent
    sub_path = tbb_root / _args.path

    if not sub_path.exists():
        print(f"Error: path not found: {sub_path}")
        sys.exit(1)

    try:
        result = scrape_sub_chapter(
            sub_path, tbb_root, retry_failed=_args.retry_failed
        )
        print(f"\n{json.dumps(result, indent=2, default=str)}")
    finally:
        close_browser()

"""
GitHub URL content extraction (btc-index Phase 3B).

Fetches README files, raw blob content, PR/issue descriptions,
and gist content from GitHub URLs. Outputs to btc-index/scraped/.

Usage:
    python run-github.py              # Extract all GitHub URLs
    python run-github.py --dry-run    # Show plan
    python run-github.py --resume     # Skip already-scraped

Run from btc-index/scraper/:
    ../mcp/.venv/Scripts/python.exe run-github.py
"""

import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

import httpx

sys.path.insert(0, str(Path(__file__).parent))
import importlib
_bn = importlib.import_module("run-bitcoin-notes")
slugify = _bn.slugify
write_scraped_file = _bn.write_scraped_file
find_already_scraped = _bn.find_already_scraped

SCRAPER_DIR = Path(__file__).resolve().parent
TBB_ROOT = SCRAPER_DIR.parent.parent
URLS_JSON = SCRAPER_DIR / "bitcoin-notes-urls.json"

HEADERS = {
    "User-Agent": "btc-index-scraper/1.0 (educational research)",
    "Accept": "application/vnd.github.v3+json",
}

RAW_HEADERS = {
    "User-Agent": "btc-index-scraper/1.0 (educational research)",
    "Accept": "text/plain",
}

SKIP_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg", ".gif", ".zip", ".tar", ".gz"}

MAX_CONTENT_CHARS = 30000  # Higher limit for READMEs and docs


def classify_github_url(url: str) -> dict:
    """Classify a GitHub URL into a fetchable type."""
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    parts = path.split("/")

    if parsed.netloc == "gist.github.com" and len(parts) >= 2:
        return {"type": "gist", "user": parts[0], "id": parts[1]}

    if len(parts) < 2:
        return {"type": "skip", "reason": "Not a repo URL"}

    owner, repo = parts[0], parts[1]

    if len(parts) == 2:
        return {"type": "readme", "owner": owner, "repo": repo}

    if parts[2] == "blob" and len(parts) > 4:
        branch = parts[3]
        file_path = "/".join(parts[4:])
        ext = Path(file_path).suffix.lower()
        if ext in SKIP_EXTENSIONS:
            return {"type": "skip", "reason": f"Binary file ({ext})"}
        return {
            "type": "blob", "owner": owner, "repo": repo,
            "branch": branch, "path": file_path,
        }

    if parts[2] == "pull" and len(parts) >= 4:
        # PR with optional sub-path (commits, files)
        pr_num = parts[3]
        return {"type": "pr", "owner": owner, "repo": repo, "number": pr_num}

    if parts[2] == "issues" and len(parts) >= 4:
        return {"type": "issue", "owner": owner, "repo": repo, "number": parts[3]}

    if parts[2] == "releases":
        return {"type": "readme", "owner": owner, "repo": repo}

    if parts[2] == "users" and len(parts) >= 4:
        return {"type": "skip", "reason": "User profile page"}

    return {"type": "readme", "owner": owner, "repo": repo}


def fetch_readme(owner: str, repo: str, client: httpx.Client) -> tuple[str, str, str]:
    """Fetch a repo's README via raw.githubusercontent.com."""
    for readme_name in ["README.md", "readme.md", "README.rst", "README"]:
        url = f"https://raw.githubusercontent.com/{owner}/{repo}/HEAD/{readme_name}"
        try:
            resp = client.get(url, timeout=15.0)
            if resp.status_code == 200:
                content = resp.text
                if len(content) > MAX_CONTENT_CHARS:
                    content = content[:MAX_CONTENT_CHARS] + "\n\n[... truncated ...]"
                header = f"**Repository:** {owner}/{repo}\n\n"
                return "done", header + content, ""
        except Exception:
            continue
    return "failed", "", "No README found"


def fetch_blob(
    owner: str, repo: str, branch: str, path: str, client: httpx.Client
) -> tuple[str, str, str]:
    """Fetch a specific file from a repo."""
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
    try:
        resp = client.get(url, timeout=15.0)
        if resp.status_code == 200:
            content = resp.text
            if len(content) > MAX_CONTENT_CHARS:
                content = content[:MAX_CONTENT_CHARS] + "\n\n[... truncated ...]"
            header = f"**Repository:** {owner}/{repo}\n**File:** {path}\n\n"
            return "done", header + content, ""
        return "failed", "", f"HTTP {resp.status_code}"
    except Exception as e:
        return "failed", "", str(e)[:80]


def fetch_pr(
    owner: str, repo: str, number: str, client: httpx.Client
) -> tuple[str, str, str]:
    """Fetch PR title + body via GitHub API."""
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{number}"
    try:
        resp = client.get(url, headers=HEADERS, timeout=15.0)
        if resp.status_code == 200:
            data = resp.json()
            title = data.get("title", "")
            body = data.get("body", "") or ""
            state = data.get("state", "")
            user = data.get("user", {}).get("login", "")
            content = (
                f"**PR #{number}:** {title}\n"
                f"**Author:** {user}\n"
                f"**State:** {state}\n\n"
                f"{body}"
            )
            if len(content) > MAX_CONTENT_CHARS:
                content = content[:MAX_CONTENT_CHARS] + "\n\n[... truncated ...]"
            return "done", content, ""
        return "failed", "", f"HTTP {resp.status_code}"
    except Exception as e:
        return "failed", "", str(e)[:80]


def fetch_issue(
    owner: str, repo: str, number: str, client: httpx.Client
) -> tuple[str, str, str]:
    """Fetch issue title + body via GitHub API."""
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{number}"
    try:
        resp = client.get(url, headers=HEADERS, timeout=15.0)
        if resp.status_code == 200:
            data = resp.json()
            title = data.get("title", "")
            body = data.get("body", "") or ""
            state = data.get("state", "")
            user = data.get("user", {}).get("login", "")
            content = (
                f"**Issue #{number}:** {title}\n"
                f"**Author:** {user}\n"
                f"**State:** {state}\n\n"
                f"{body}"
            )
            if len(content) > MAX_CONTENT_CHARS:
                content = content[:MAX_CONTENT_CHARS] + "\n\n[... truncated ...]"
            return "done", content, ""
        return "failed", "", f"HTTP {resp.status_code}"
    except Exception as e:
        return "failed", "", str(e)[:80]


def fetch_gist(gist_id: str, client: httpx.Client) -> tuple[str, str, str]:
    """Fetch gist content via GitHub API."""
    url = f"https://api.github.com/gists/{gist_id}"
    try:
        resp = client.get(url, headers=HEADERS, timeout=15.0)
        if resp.status_code == 200:
            data = resp.json()
            desc = data.get("description", "")
            files = data.get("files", {})
            parts = [f"**Gist:** {desc}\n"]
            for fname, fdata in files.items():
                content = fdata.get("content", "")
                parts.append(f"\n## {fname}\n\n{content}")
            full = "\n".join(parts)
            if len(full) > MAX_CONTENT_CHARS:
                full = full[:MAX_CONTENT_CHARS] + "\n\n[... truncated ...]"
            return "done", full, ""
        return "failed", "", f"HTTP {resp.status_code}"
    except Exception as e:
        return "failed", "", str(e)[:80]


def main():
    import argparse
    parser = argparse.ArgumentParser(description="GitHub URL content extraction")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    data = json.loads(URLS_JSON.read_text(encoding="utf-8"))
    urls = data.get("github_urls", [])

    if not urls:
        print("No GitHub URLs found.")
        return

    already_done = set()
    if args.resume:
        already_done = find_already_scraped()
        print(f"Resume mode: {len(already_done)} URLs already scraped")

    # Classify all URLs
    classified = []
    for entry in urls:
        url = entry["url"] if isinstance(entry, dict) else entry
        source_files = entry.get("source_files", []) if isinstance(entry, dict) else []
        info = classify_github_url(url)
        info["url"] = url
        info["source_files"] = source_files
        classified.append(info)

    # Filter
    actionable = [c for c in classified if c["type"] != "skip" and c["url"] not in already_done]
    skipped = [c for c in classified if c["type"] == "skip"]

    print(f"\n{'#' * 60}")
    print(f"  GITHUB CONTENT EXTRACTION")
    print(f"  Total URLs: {len(urls)}")
    print(f"  Actionable: {len(actionable)}")
    print(f"  Skipped: {len(skipped)} ({', '.join(s.get('reason', '') for s in skipped[:3])})")
    print(f"  Already done: {len(urls) - len(actionable) - len(skipped)}")
    print(f"{'#' * 60}")

    if args.dry_run:
        for c in actionable[:20]:
            print(f"  [{c['type']:6s}] {c['url'][:75]}")
        if len(actionable) > 20:
            print(f"  ... and {len(actionable) - 20} more")
        return

    results = []
    start = time.time()

    with httpx.Client(headers=RAW_HEADERS, follow_redirects=True, timeout=15.0) as client:
        for i, entry in enumerate(actionable, 1):
            url = entry["url"]
            url_type = entry["type"]
            source_files = entry["source_files"]
            url_display = url[:75] + ("..." if len(url) > 75 else "")
            print(f"  [{i}/{len(actionable)}] [{url_type:6s}] {url_display}", end="", flush=True)

            t0 = time.time()

            if url_type == "readme":
                status, content, error = fetch_readme(entry["owner"], entry["repo"], client)
            elif url_type == "blob":
                status, content, error = fetch_blob(
                    entry["owner"], entry["repo"], entry["branch"], entry["path"], client
                )
            elif url_type == "pr":
                status, content, error = fetch_pr(
                    entry["owner"], entry["repo"], entry["number"], client
                )
            elif url_type == "issue":
                status, content, error = fetch_issue(
                    entry["owner"], entry["repo"], entry["number"], client
                )
            elif url_type == "gist":
                status, content, error = fetch_gist(entry["id"], client)
            else:
                status, content, error = "skipped", "", f"Unknown type: {url_type}"

            elapsed = time.time() - t0

            write_scraped_file(url, content, status, "github", source_files, error)

            results.append({"url": url, "status": status, "chars": len(content), "error": error})

            tag = {"done": " OK", "partial": " PARTIAL", "failed": " FAIL", "skipped": " SKIP"}.get(status, " ???")
            chars = f" {len(content):,}ch" if content else ""
            reason = f" -- {error}" if error else ""
            print(f"{tag}{chars}{reason} ({elapsed:.1f}s)")

            if i < len(actionable):
                time.sleep(0.5)

    total_time = time.time() - start
    done = sum(1 for r in results if r["status"] == "done")
    failed = sum(1 for r in results if r["status"] == "failed")
    total_chars = sum(r["chars"] for r in results)

    print(f"\n{'#' * 60}")
    print(f"  GITHUB COMPLETE: {done} done, {failed} failed")
    print(f"  Content: {total_chars:,} chars in {total_time:.1f}s")
    print(f"{'#' * 60}")


if __name__ == "__main__":
    main()

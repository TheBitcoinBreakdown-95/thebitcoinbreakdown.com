"""
Phase D: Apify batch scraper for Medium URLs.

Uses the Apify Website Content Crawler to scrape Medium articles that are
blocked by Cloudflare Turnstile CAPTCHA. Writes results to btc-index/scraped/.

IMPORTANT: This is a PAID service. Only run with explicit user approval.
Token loaded from Ai Playground/.env via python-dotenv.

Usage:
    python run-apify-medium.py              # Run batch scrape
    python run-apify-medium.py --dry-run    # Show plan, no API calls
    python run-apify-medium.py --status     # Check existing run status

Run from btc-index/scraper/:
    ../mcp/.venv/Scripts/python.exe run-apify-medium.py
"""

import argparse
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

import httpx

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

TBB_ROOT = Path(__file__).resolve().parent.parent.parent
SCRAPED_DIR = TBB_ROOT / "btc-index" / "scraped"
LOG_FILE = Path(__file__).resolve().parent / "apify-medium-log.json"
FAILURES_FILE = Path(__file__).resolve().parent / "consolidated-failures.md"

# Apify actor for web scraping with Cloudflare bypass
ACTOR_ID = "apify~website-content-crawler"
APIFY_BASE = "https://api.apify.com/v2"

# ---------------------------------------------------------------------------
# URL handling
# ---------------------------------------------------------------------------


def url_to_filename(url: str) -> str:
    """Convert URL to a filesystem-safe filename."""
    parsed = urlparse(url)
    slug = parsed.netloc + parsed.path
    slug = re.sub(r"[^a-zA-Z0-9]", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    if len(slug) > 120:
        slug = slug[:120]
    return slug + ".md"


def get_medium_urls() -> list[str]:
    """Extract the 36 unique Medium URLs from consolidated-failures.md."""
    urls = []
    with open(FAILURES_FILE, encoding="utf-8") as f:
        in_medium = False
        for line in f:
            if "Medium URLs" in line and "Apify" in line:
                in_medium = True
                continue
            if in_medium and line.startswith("## ") and "Medium" not in line:
                in_medium = False
                continue
            if in_medium and line.startswith("---"):
                in_medium = False
                continue
            if in_medium:
                m = re.search(r"`(https://[^`]+)`", line)
                if m:
                    urls.append(m.group(1))
    return urls


def load_api_token() -> str:
    """Load Apify API token from Ai Playground/.env.

    Handles two formats:
    1. APIFY_API_TOKEN=apify_api_xxx  (standard key=value)
    2. apify_api_xxx                  (token as key name, no value)
    """
    try:
        from dotenv import find_dotenv, dotenv_values
        env_path = find_dotenv(usecwd=True)
        if not env_path:
            env_path = str(TBB_ROOT.parent / ".env")
        values = dotenv_values(env_path)

        # Standard format: APIFY_API_TOKEN=xxx
        token = values.get("APIFY_API_TOKEN") or values.get("APIFY_TOKEN")
        if token:
            return token

        # Alt format: token stored as key name (value is None/empty)
        for key in values:
            if key.startswith("apify_api_"):
                return key
    except ImportError:
        pass

    # Fallback: environment variable
    import os
    token = os.environ.get("APIFY_API_TOKEN") or os.environ.get("APIFY_TOKEN")
    if token:
        return token

    print("ERROR: No Apify API token found in .env or environment")
    print("Expected in: Ai Playground/.env")
    sys.exit(1)


def write_scraped_file(url: str, title: str, text: str, chars: int) -> str:
    """Write a scraped content file."""
    fname = url_to_filename(url)
    fpath = SCRAPED_DIR / fname

    domain = urlparse(url).netloc.replace("www.", "")
    content = f"""# {domain} -- Scraped Content

**URL:** {url}
**Category:** medium-apify
**Scrape status:** DONE
**Source notes:**
**Scraped:** {datetime.now().strftime('%Y-%m-%d')}
**Title:** {title}
**Chars:** {chars:,}

---

{text}
"""
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    return fname


def write_failed_file(url: str, error: str) -> str:
    """Write a failed scrape stub."""
    fname = url_to_filename(url)
    fpath = SCRAPED_DIR / fname

    domain = urlparse(url).netloc.replace("www.", "")
    content = f"""# {domain} -- Scraped Content

**URL:** {url}
**Category:** medium-apify
**Scrape status:** FAILED
**Source notes:**
**Scraped:** {datetime.now().strftime('%Y-%m-%d')}
**Error:** {error}

---

"""
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    return fname


# ---------------------------------------------------------------------------
# Apify API
# ---------------------------------------------------------------------------


def start_crawl(token: str, urls: list[str]) -> dict:
    """Start an Apify Website Content Crawler run."""
    endpoint = f"{APIFY_BASE}/acts/{ACTOR_ID}/runs"

    payload = {
        "startUrls": [{"url": u} for u in urls],
        "crawlerType": "playwright:firefox",
        "maxCrawlPages": len(urls),
        "maxCrawlDepth": 0,  # Don't follow links
        "maxConcurrency": 5,
        "requestTimeoutSecs": 60,
        "htmlTransformer": "readableText",
        "removeElementsCssSelector": "nav, footer, header, .metabar, .js-postShareWidget",
    }

    resp = httpx.post(
        endpoint,
        params={"token": token},
        json=payload,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["data"]


def check_run(token: str, run_id: str) -> dict:
    """Check the status of an Apify run."""
    resp = httpx.get(
        f"{APIFY_BASE}/actor-runs/{run_id}",
        params={"token": token},
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json()["data"]


def get_results(token: str, dataset_id: str) -> list[dict]:
    """Fetch results from an Apify dataset."""
    resp = httpx.get(
        f"{APIFY_BASE}/datasets/{dataset_id}/items",
        params={"token": token, "format": "json"},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--status", action="store_true", help="Check existing run")
    args = parser.parse_args()

    urls = get_medium_urls()
    print(f"Medium URLs to scrape: {len(urls)}")

    if args.dry_run:
        for i, u in enumerate(urls, 1):
            fname = url_to_filename(u)
            exists = (SCRAPED_DIR / fname).exists()
            print(f"  {i:2d}. {u}")
            print(f"      -> {fname} {'(exists)' if exists else ''}")
        print(f"\nEstimated Apify cost: ~${len(urls) * 0.005:.2f} - ${len(urls) * 0.02:.2f}")
        return

    token = load_api_token()

    # Check for existing run
    if args.status or LOG_FILE.exists():
        if LOG_FILE.exists():
            with open(LOG_FILE, encoding="utf-8") as f:
                log = json.load(f)
            run_id = log.get("run_id")
            if run_id:
                run = check_run(token, run_id)
                status = run["status"]
                print(f"Existing run {run_id}: {status}")
                if status == "SUCCEEDED":
                    dataset_id = run["defaultDatasetId"]
                    print(f"Fetching results from dataset {dataset_id}...")
                    results = get_results(token, dataset_id)
                    process_results(urls, results, log)
                    return
                elif status in ("RUNNING", "READY"):
                    print("Run still in progress. Check back later.")
                    return
                elif status == "FAILED":
                    print("Run FAILED. Starting new run.")
                else:
                    print(f"Unknown status: {status}. Starting new run.")

    # Start new run
    print(f"\nStarting Apify crawl for {len(urls)} Medium URLs...")
    run_data = start_crawl(token, urls)
    run_id = run_data["id"]
    dataset_id = run_data["defaultDatasetId"]
    print(f"Run ID: {run_id}")
    print(f"Dataset ID: {dataset_id}")

    # Save log for resume
    log = {
        "timestamp": datetime.now().isoformat(),
        "run_id": run_id,
        "dataset_id": dataset_id,
        "url_count": len(urls),
        "urls": urls,
    }
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(log, f, indent=2)

    # Poll for completion
    print("Waiting for crawl to complete...")
    poll_interval = 10
    max_wait = 600  # 10 minutes max
    elapsed = 0
    while elapsed < max_wait:
        time.sleep(poll_interval)
        elapsed += poll_interval
        run = check_run(token, run_id)
        status = run["status"]
        if status == "SUCCEEDED":
            print(f"\nCrawl completed in {elapsed}s!")
            results = get_results(token, dataset_id)
            process_results(urls, results, log)
            return
        elif status == "FAILED":
            print(f"\nCrawl FAILED after {elapsed}s")
            print(f"Error: {run.get('statusMessage', 'unknown')}")
            sys.exit(1)
        else:
            sys.stdout.write(f"\r  Status: {status} ({elapsed}s elapsed)")
            sys.stdout.flush()

    print(f"\nTimeout after {max_wait}s. Run still in progress.")
    print(f"Check later with: python {Path(__file__).name} --status")


def process_results(urls: list[str], results: list[dict], log: dict):
    """Process Apify results and write scraped files."""
    # Map results by URL
    result_map = {}
    for r in results:
        url = r.get("url", "")
        result_map[url] = r
        # Also try without trailing slash
        if url.endswith("/"):
            result_map[url.rstrip("/")] = r

    done = 0
    failed = 0
    total_chars = 0

    for url in urls:
        r = result_map.get(url) or result_map.get(url.rstrip("/"))
        if r and r.get("text"):
            text = r["text"].strip()
            title = r.get("metadata", {}).get("title", "") or r.get("title", "")
            chars = len(text)
            fname = write_scraped_file(url, title, text, chars)
            done += 1
            total_chars += chars
            print(f"  DONE [{chars:,} chars] {url}")
        else:
            error = "No content returned by Apify"
            if r:
                error = r.get("error", error) or error
            fname = write_failed_file(url, error)
            failed += 1
            print(f"  FAIL {url}: {error}")

    # Update log
    log["completed"] = datetime.now().isoformat()
    log["done"] = done
    log["failed"] = failed
    log["total_chars"] = total_chars
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(log, f, indent=2)

    print(f"\n=== Results ===")
    print(f"Done: {done}/{len(urls)}")
    print(f"Failed: {failed}/{len(urls)}")
    print(f"Total chars: {total_chars:,}")


if __name__ == "__main__":
    main()

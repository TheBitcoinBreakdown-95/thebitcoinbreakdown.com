"""Generate consolidated failure doc from all scraping data."""

import json
import re
from pathlib import Path
from urllib.parse import urlparse
from datetime import datetime

scraped = Path(__file__).resolve().parent.parent / "scraped"
scraper = Path(__file__).resolve().parent

# 1. Read all FAILED files from scraped/
failures = {}
for f in scraped.glob("*.md"):
    text = f.read_text(encoding="utf-8", errors="replace")
    if "**Scrape status:** FAILED" not in text:
        continue
    url = error = category = source_notes = ""
    for line in text.splitlines()[:10]:
        if line.startswith("**URL:**"):
            url = line.replace("**URL:**", "").strip()
        elif line.startswith("**Error:**"):
            error = line.replace("**Error:**", "").strip()
        elif line.startswith("**Category:**"):
            category = line.replace("**Category:**", "").strip()
        elif line.startswith("**Source notes:**"):
            source_notes = line.replace("**Source notes:**", "").strip()
    if url:
        parsed = urlparse(url)
        domain = parsed.netloc.lower().removeprefix("www.")
        failures[url] = {
            "url": url, "error": error, "domain": domain,
            "category": category, "source_notes": source_notes
        }

# 2. Read Medium URLs from bitcoin-notes-urls.json
urls_data = json.loads((scraper / "bitcoin-notes-urls.json").read_text(encoding="utf-8"))
medium_bn = {}
for entry in urls_data.get("medium_urls", []):
    url = entry["url"] if isinstance(entry, dict) else entry
    sf = entry.get("source_files", []) if isinstance(entry, dict) else []
    medium_bn[url] = ", ".join(sf[:3]) if sf else ""

# 3. Read WBIGAF Medium refs from failed-urls.md
wbigaf_text = (scraper / "failed-urls.md").read_text(encoding="utf-8")
wbigaf_medium = {}
current_title = ""
current_url = ""
for line in wbigaf_text.splitlines():
    if line.startswith("### ") and "Medium" not in line and "Tweets" not in line and "Not Scrapable" not in line:
        m = re.search(r"### (.+)", line)
        if m:
            current_title = m.group(1).strip()
    elif line.startswith("- http") and "medium" in line.lower():
        current_url = line.lstrip("- ").strip()
    elif line.startswith("- Referenced in:"):
        refs = line.replace("- Referenced in:", "").strip()
        if current_url:
            wbigaf_medium[current_url] = {"title": current_title, "refs": refs}
            current_url = ""

# Categorize BN failures
truly_dead_ftp = []
truly_dead_web = []
page_gone = []
waf_blocked = []
timeout_retry = []
tweet_dead = []
malformed = []
other_errors = []

for url, f in failures.items():
    e = f["error"].lower()
    d = f["domain"]

    if d in ("x.com", "twitter.com"):
        tweet_dead.append(f)
    elif d.startswith("ftp") or "ftp." in d or d.startswith("gopher"):
        truly_dead_ftp.append(f)
    elif "404" in e or "410" in e or "not found" in e:
        page_gone.append(f)
    elif "403" in e or "401" in e or "access denied" in e:
        waf_blocked.append(f)
    elif "timeout" in e:
        timeout_retry.append(f)
    elif "connection refused" in e or "dns" in e:
        truly_dead_web.append(f)
    elif "javascript" in url or not url.startswith("http"):
        malformed.append(f)
    else:
        other_errors.append(f)

# Build Medium dedup list
medium_all = {}
for url, info in wbigaf_medium.items():
    medium_all[url] = {
        "title": info["title"], "wbigaf_refs": info["refs"],
        "bn_refs": "", "origin": "wbigaf"
    }
for url, refs in medium_bn.items():
    if url in medium_all:
        medium_all[url]["bn_refs"] = refs
        medium_all[url]["origin"] = "both"
    else:
        medium_all[url] = {
            "title": "", "wbigaf_refs": "",
            "bn_refs": refs, "origin": "bitcoin-notes"
        }

# Generate doc
L = []
L.append("# Consolidated Failure Report -- btc-index Phase 3 + 3B")
L.append("")
L.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d')}")
L.append(f"**Bitcoin Notes scraped failures:** {len(failures)}")
L.append(f"**Medium URLs (never attempted):** {len(medium_bn)}")
L.append(f"**Total unique Medium (deduped WBIGAF + BN):** {len(medium_all)}")
L.append("")

L.append("## Summary")
L.append("")
L.append("| Category | Count | Recovery Path |")
L.append("|----------|-------|---------------|")
L.append(f"| FTP/Gopher archives | {len(truly_dead_ftp)} | Skip -- historical, not web-accessible |")
L.append(f"| Dead web servers | {len(truly_dead_web)} | Wayback Machine |")
L.append(f"| Page gone (404/410) | {len(page_gone)} | Wayback Machine |")
L.append(f"| WAF/403 blocked | {len(waf_blocked)} | Wayback -> Apify (last resort) |")
L.append(f"| Timeout | {len(timeout_retry)} | Retry with longer timeout |")
L.append(f"| Deleted tweets | {len(tweet_dead)} | Unrecoverable |")
L.append(f"| Malformed URL | {len(malformed)} | Skip |")
L.append(f"| Other errors | {len(other_errors)} | Case-by-case |")
L.append(f"| Medium (Apify queue) | {len(medium_all)} | Apify (paid, last resort) |")
L.append("")
L.append("---")
L.append("")

# Section 1: Truly Dead
skip_total = len(truly_dead_ftp) + len(tweet_dead) + len(malformed)
L.append(f"## 1. Truly Dead -- Skip ({skip_total} URLs)")
L.append("")
L.append("No automated recovery possible.")
L.append("")

L.append(f"### FTP/Gopher Archives ({len(truly_dead_ftp)})")
L.append("")
L.append("Historical cypherpunk-era file servers. Not web-accessible, Wayback cannot archive FTP.")
L.append("")
for f in sorted(truly_dead_ftp, key=lambda x: x["domain"]):
    L.append(f"- `{f['url']}`")
L.append("")

L.append(f"### Deleted Tweets ({len(tweet_dead)})")
L.append("")
L.append("Both fxtwitter API and Patchright browser failed. Accounts deleted or suspended.")
L.append("")
for f in tweet_dead:
    L.append(f"- `{f['url']}`")
L.append("")

if malformed:
    L.append(f"### Malformed URLs ({len(malformed)})")
    L.append("")
    for f in malformed:
        L.append(f"- `{f['url']}`")
    L.append("")

# Section 2: Wayback Machine Candidates
wayback_total = len(truly_dead_web) + len(page_gone)
L.append(f"## 2. Wayback Machine Candidates ({wayback_total} URLs)")
L.append("")
L.append("Try `https://web.archive.org/web/{url}` before any paid service.")
L.append("")

L.append(f"### Dead Web Servers ({len(truly_dead_web)})")
L.append("")
L.append("Connection refused -- server is down or domain expired. Content may exist in Wayback.")
L.append("")
L.append("| Domain | URL |")
L.append("|--------|-----|")
for f in sorted(truly_dead_web, key=lambda x: x["domain"]):
    L.append(f"| {f['domain']} | `{f['url']}` |")
L.append("")

L.append(f"### 404 / Page Gone ({len(page_gone)})")
L.append("")
L.append("Active domains but specific page removed. High Wayback recovery probability.")
L.append("")
L.append("| Domain | URL |")
L.append("|--------|-----|")
for f in sorted(page_gone, key=lambda x: x["domain"]):
    L.append(f"| {f['domain']} | `{f['url']}` |")
L.append("")

# Section 3: WAF/403 Blocked
L.append(f"## 3. WAF/403 Blocked ({len(waf_blocked)} URLs)")
L.append("")
L.append("Sites are live but blocking scrapers. Try Wayback first, then Apify as last resort.")
L.append("")
L.append("| Domain | URL |")
L.append("|--------|-----|")
for f in sorted(waf_blocked, key=lambda x: x["domain"]):
    L.append(f"| {f['domain']} | `{f['url']}` |")
L.append("")

# Section 4: Timeout / Retry
L.append(f"## 4. Timeout / Retry ({len(timeout_retry)} URLs)")
L.append("")
L.append("Could succeed with longer timeout, different network, or retry.")
L.append("")
for f in timeout_retry:
    L.append(f"- `{f['url']}` ({f['error']})")
L.append("")

# Section 5: Other Errors
L.append(f"## 5. Other Errors ({len(other_errors)} URLs)")
L.append("")
for f in sorted(other_errors, key=lambda x: x["domain"]):
    L.append(f"- `{f['url']}` -- {f['error']}")
L.append("")

# Section 6: Medium URLs -- Apify Queue
L.append(f"## 6. Medium URLs -- Apify Queue ({len(medium_all)} unique)")
L.append("")
L.append("All Medium articles fail due to Cloudflare Turnstile CAPTCHA. Apify is the only")
L.append("recovery path. Wait until all free methods are exhausted on other categories first.")
L.append("")
L.append("| # | URL | WBIGAF Refs | BN Sources |")
L.append("|----|-----|-------------|------------|")
for i, (url, info) in enumerate(sorted(medium_all.items()), 1):
    wr = info.get("wbigaf_refs", "") or "--"
    br = info.get("bn_refs", "") or "--"
    L.append(f"| {i} | `{url}` | {wr} | {br} |")
L.append("")

# Section 7: Recovery Plan
L.append("---")
L.append("")
L.append("## Recovery Plan")
L.append("")
L.append("### Phase A: Wayback Machine (free)")
L.append(f"- Target: {wayback_total} URLs (dead servers + 404 pages)")
L.append("- Also try on WAF/403 URLs where the content existed before")
L.append("- Use archive.org Wayback Machine API: `http://archive.org/wayback/available?url=TARGET`")
L.append("")
L.append("### Phase B: Retry with Adjustments")
L.append(f"- Target: {len(timeout_retry)} timeout URLs + {len(other_errors)} other errors")
L.append("- Longer timeout (60s), different User-Agent, retry read errors")
L.append("")
L.append("### Phase C: Check Notebook Context")
L.append("- For remaining failures, check if the Bitcoin Note that linked the URL")
L.append("  already contains the key content inline (quote, summary, argument)")
L.append("- If so, the scrape is unnecessary -- the corpus already has the substance")
L.append("")
L.append("### Phase D: Apify (paid, last resort)")
L.append(f"- Target: {len(medium_all)} Medium URLs + any high-value WAF survivors")
L.append("- Gate: user approval required per feedback_apify_last_resort.md")
L.append("- Token in Ai Playground/.env")
L.append("")

doc = "\n".join(L) + "\n"
out_path = scraper / "consolidated-failures.md"
out_path.write_text(doc, encoding="utf-8")
print(f"Written: {out_path.name} ({len(doc):,} chars, {len(L)} lines)")
print()
print(f"  FTP/gopher:    {len(truly_dead_ftp)}")
print(f"  Dead web:      {len(truly_dead_web)}")
print(f"  404/gone:      {len(page_gone)}")
print(f"  WAF/403:       {len(waf_blocked)}")
print(f"  Timeout:       {len(timeout_retry)}")
print(f"  Tweets:        {len(tweet_dead)}")
print(f"  Malformed:     {len(malformed)}")
print(f"  Other:         {len(other_errors)}")
print(f"  Medium:        {len(medium_all)}")
print(f"  -----------")
print(f"  TOTAL:         {skip_total + wayback_total + len(waf_blocked) + len(timeout_retry) + len(other_errors) + len(medium_all)}")

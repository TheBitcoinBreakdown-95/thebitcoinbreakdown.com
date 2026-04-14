"""
Phase C: Check notebook context for failed URLs.

For each FAILED scraped file, checks if the Bitcoin Note that linked the URL
already has substantial inline content (quotes, summaries, arguments). If so,
updates the scraped file status from FAILED to COVERED.

Usage:
    python check-notebook-context.py              # Update files
    python check-notebook-context.py --dry-run    # Preview only
"""

import argparse
import glob
import json
import re
import sys
from pathlib import Path

TBB_ROOT = Path(__file__).resolve().parent.parent.parent
BN_ROOT = TBB_ROOT / "Bitcoin Notes"
SCRAPED_DIR = Path(__file__).resolve().parent.parent / "scraped"

CONTEXT_THRESHOLD = 300  # chars of substantive text to consider "covered"


def load_url_map():
    """Load URL-to-source-note mapping from bitcoin-notes-urls.json."""
    json_path = Path(__file__).resolve().parent / "bitcoin-notes-urls.json"
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    url_map = {}
    for entry in data.get("scrapable_urls", []):
        url_map[entry["url"]] = entry["source_files"]
    for cat_urls in data.get("categories", {}).values():
        if isinstance(cat_urls, list):
            for entry in cat_urls:
                if isinstance(entry, dict) and "url" in entry:
                    if entry["url"] not in url_map:
                        url_map[entry["url"]] = entry.get("source_files", [])
    return url_map


def load_skip_urls():
    """Load URLs from skip categories (FTP, deleted tweets, malformed)."""
    skip = set()
    failures_path = Path(__file__).resolve().parent / "consolidated-failures.md"
    with open(failures_path, encoding="utf-8") as f:
        in_skip = False
        for line in f:
            if any(x in line for x in ["FTP/Gopher", "Deleted Tweets", "Malformed URL"]):
                in_skip = True
            elif line.startswith("###") or (line.startswith("## ") and "Truly Dead" not in line):
                in_skip = False
            if in_skip:
                m = re.search(r"`(https://[^`]+)`", line)
                if m:
                    skip.add(m.group(1))
    return skip


def measure_context(note_path, url):
    """Measure substantive text chars around a URL mention in a note."""
    if not note_path.exists():
        return 0, ""

    try:
        with open(note_path, encoding="utf-8") as f:
            lines = f.readlines()
    except Exception:
        return 0, ""

    domain = url.split("//")[1].split("/")[0] if "//" in url else ""
    url_variants = [url, url.rstrip("/")]
    if domain:
        url_variants.append(domain)

    best = 0
    best_note = ""

    for i, line in enumerate(lines):
        if not any(v in line for v in url_variants):
            continue

        start = max(0, i - 5)
        end = min(len(lines), i + 20)

        substantive = 0
        for cl in lines[start:end]:
            cl_stripped = cl.strip()
            if not cl_stripped or cl_stripped.startswith("#"):
                continue
            if re.match(r"^[-*]\s*https?://", cl_stripped):
                continue
            if re.match(r"^https?://", cl_stripped):
                continue
            if re.match(r"^\[.*\]\(https?://.*\)$", cl_stripped):
                continue
            substantive += len(cl_stripped)

        if substantive > best:
            best = substantive

    return best, str(note_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    url_map = load_url_map()
    skip_urls = load_skip_urls()

    updated = 0
    covered_list = []
    partial_list = []
    no_context_list = []

    for fpath in sorted(glob.glob(str(SCRAPED_DIR / "*.md"))):
        with open(fpath, encoding="utf-8") as f:
            content = f.read()

        if "**Scrape status:** FAILED" not in content:
            continue

        url = None
        for line in content.split("\n"):
            if "**URL:**" in line:
                url = line.split("**URL:**")[-1].strip()
                break
        if not url:
            continue

        if url in skip_urls:
            continue

        source_files = url_map.get(url, [])
        if not source_files:
            no_context_list.append((url, fpath, 0, "no mapping"))
            continue

        best_context = 0
        best_note_name = ""
        for rel_path in source_files:
            note_path = BN_ROOT / rel_path
            chars, _ = measure_context(note_path, url)
            if chars > best_context:
                best_context = chars
                # Get just the filename
                best_note_name = Path(rel_path).name

        if best_context >= CONTEXT_THRESHOLD:
            covered_list.append((url, fpath, best_context, best_note_name))

            if not args.dry_run:
                new_content = content.replace(
                    "**Scrape status:** FAILED",
                    "**Scrape status:** COVERED",
                )
                if "**Coverage:**" not in new_content:
                    new_content = new_content.replace(
                        "**Scrape status:** COVERED",
                        f"**Scrape status:** COVERED\n**Coverage:** Content inline in Bitcoin Note: {best_note_name}",
                    )
                new_content = re.sub(
                    r"\*\*Error:\*\*.*\n",
                    f"**Error:** Covered by notebook context ({best_context:,} chars in source note)\n",
                    new_content,
                )
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                updated += 1
        elif best_context >= 100:
            partial_list.append((url, fpath, best_context, best_note_name))
        else:
            no_context_list.append((url, fpath, best_context, best_note_name))

    # Report
    print(f"=== Phase C Results ===")
    print(f"Covered (>={CONTEXT_THRESHOLD} chars): {len(covered_list)}")
    print(f"Partial (100-{CONTEXT_THRESHOLD} chars): {len(partial_list)}")
    print(f"No context (<100 chars): {len(no_context_list)}")
    if not args.dry_run:
        print(f"Files updated: {updated}")
    else:
        print("(dry run -- no files modified)")

    # Final corpus status
    done = partial = failed = covered = 0
    for fpath in glob.glob(str(SCRAPED_DIR / "*.md")):
        with open(fpath, encoding="utf-8") as f:
            head = f.read(500)
        if "**Scrape status:** DONE" in head:
            done += 1
        elif "**Scrape status:** PARTIAL" in head:
            partial += 1
        elif "**Scrape status:** COVERED" in head:
            covered += 1
        elif "**Scrape status:** FAILED" in head:
            failed += 1

    print(f"\nCorpus status:")
    print(f"  DONE:    {done}")
    print(f"  PARTIAL: {partial}")
    print(f"  COVERED: {covered}")
    print(f"  FAILED:  {failed}")
    print(f"  Total:   {done + partial + covered + failed}")


if __name__ == "__main__":
    main()

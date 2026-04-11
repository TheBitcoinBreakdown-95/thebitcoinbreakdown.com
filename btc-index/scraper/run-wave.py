"""
Wave runner for btc-index scraping pipeline (Phase 3).

Discovers WBIGAF sub-chapters with PENDING links, scrapes them
in chapter order, and logs results. Resumable: already-scraped
links are marked DONE in links.md and skipped on re-run.

Usage:
    python run-wave.py                 # All chapters 4-9
    python run-wave.py --chapter 4     # Just chapter 4
    python run-wave.py --chapter 4-6   # Chapters 4 through 6
    python run-wave.py --sub 4.1       # Just one sub-chapter
    python run-wave.py --dry-run       # Show plan without scraping

Run from the btc-index/scraper/ directory:
    ../mcp/.venv/Scripts/python.exe run-wave.py
"""

import argparse
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path

# Import from sibling module
sys.path.insert(0, str(Path(__file__).parent))
from scraper import parse_links_md, scrape_sub_chapter

TBB_ROOT = Path(__file__).resolve().parent.parent.parent
WBIGAF_ROOT = TBB_ROOT / "WBIGAF"
LOG_PATH = Path(__file__).parent / "wave-1b-log.json"

# Default chapter range for Wave 1B
DEFAULT_CHAPTERS = range(4, 10)


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def discover_sub_chapters(chapters=None) -> list[dict]:
    """Find all sub-chapter directories with links.md files."""
    if chapters is None:
        chapters = DEFAULT_CHAPTERS

    subs = []

    for ch_dir in sorted(WBIGAF_ROOT.iterdir()):
        if not ch_dir.is_dir():
            continue
        m = re.match(r"^(\d+)-", ch_dir.name)
        if not m or int(m.group(1)) not in chapters:
            continue

        ch_num = int(m.group(1))

        for sub_dir in sorted(ch_dir.iterdir()):
            if not sub_dir.is_dir():
                continue
            sm = re.match(r"^(\d+\.\d+)-", sub_dir.name)
            if not sm:
                continue

            links_path = sub_dir / "links.md"
            if not links_path.exists():
                continue

            title, links = parse_links_md(links_path)
            pending = sum(
                1 for l in links if l["status"].upper() == "PENDING"
            )

            subs.append({
                "chapter": ch_num,
                "sub_chapter": sm.group(1),
                "title": title,
                "path": sub_dir,
                "total_links": len(links),
                "pending_links": pending,
            })

    return subs


# ---------------------------------------------------------------------------
# Wave execution
# ---------------------------------------------------------------------------

def run_wave(subs: list[dict], dry_run: bool = False) -> list[dict]:
    """Run the scraping wave across all discovered sub-chapters."""
    actionable = [s for s in subs if s["pending_links"] > 0]

    if not actionable:
        print("\nNothing to scrape -- all links are already processed.")
        return []

    total_links = sum(s["pending_links"] for s in actionable)
    est_minutes = max(1, total_links * 5 // 60)

    print(f"\n{'#' * 60}")
    print(f"  WAVE 1B SCRAPING RUN")
    print(f"  Sub-chapters: {len(actionable)} (of {len(subs)} discovered)")
    print(f"  Total PENDING links: {total_links}")
    print(f"  Estimated time: ~{est_minutes} minutes")
    print(f"  Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'#' * 60}")

    if dry_run:
        print("\n  DRY RUN -- what would be scraped:\n")
        for s in actionable:
            print(
                f"  Ch{s['sub_chapter']:5s} {s['title'][:40]:40s} "
                f"{s['pending_links']:3d} links"
            )
        print(f"\n  Total: {total_links} links across {len(actionable)} "
              f"sub-chapters")
        return []

    results = []
    links_done = 0
    start = time.time()

    for i, sub in enumerate(actionable, 1):
        elapsed_so_far = time.time() - start
        if links_done > 0:
            rate = elapsed_so_far / links_done
            remaining = (total_links - links_done) * rate
            eta = f" (ETA: ~{remaining / 60:.0f}m remaining)"
        else:
            eta = ""

        print(
            f"\n  [{i}/{len(actionable)}] {sub['sub_chapter']} "
            f"{sub['title'][:35]} -- {sub['pending_links']} links{eta}"
        )

        try:
            summary = scrape_sub_chapter(sub["path"], TBB_ROOT)
            results.append(summary)

            if isinstance(summary.get("attempted"), int):
                links_done += summary["attempted"]

            # Warn on high failure rate but don't stop
            attempted = summary.get("attempted", 0)
            failed = summary.get("failed", 0)
            if attempted >= 3 and failed / attempted > 0.8:
                print(
                    f"\n  WARNING: {failed}/{attempted} links failed "
                    f"for {sub['sub_chapter']}. Continuing anyway."
                )

        except KeyboardInterrupt:
            print(
                f"\n\n  Interrupted by user at {sub['sub_chapter']}."
            )
            print(
                "  Progress saved -- re-run to continue from "
                "where you left off."
            )
            break

        except Exception as e:
            print(f"\n  ERROR on {sub['sub_chapter']}: {e}")
            results.append({
                "status": "error",
                "sub_chapter": str(
                    sub["path"].relative_to(TBB_ROOT)
                ).replace("\\", "/"),
                "error": str(e),
                "timestamp": datetime.now().isoformat(),
            })

    elapsed = time.time() - start

    # Final summary
    total_done = sum(r.get("done", 0) for r in results)
    total_partial = sum(r.get("partial", 0) for r in results)
    total_failed = sum(r.get("failed", 0) for r in results)
    total_skipped = sum(r.get("skipped", 0) for r in results)
    total_chars = sum(r.get("total_chars", 0) for r in results)

    print(f"\n{'#' * 60}")
    print(f"  WAVE 1B COMPLETE")
    print(f"  Sub-chapters processed: {len(results)}")
    print(
        f"  Links: {total_done} done, {total_partial} partial, "
        f"{total_failed} failed, {total_skipped} skipped"
    )
    print(f"  Content: {total_chars:,} characters scraped")
    print(f"  Time: {elapsed / 60:.1f} minutes")
    print(
        f"  Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
    print(f"{'#' * 60}")

    return results


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

def save_log(results: list[dict]):
    """Append run results to the wave log file."""
    run_entry = {
        "wave": "1B",
        "timestamp": datetime.now().isoformat(),
        "results": results,
        "summary": {
            "sub_chapters": len(results),
            "done": sum(r.get("done", 0) for r in results),
            "partial": sum(r.get("partial", 0) for r in results),
            "failed": sum(r.get("failed", 0) for r in results),
            "skipped": sum(r.get("skipped", 0) for r in results),
            "total_chars": sum(r.get("total_chars", 0) for r in results),
        },
    }

    if LOG_PATH.exists():
        log = json.loads(LOG_PATH.read_text(encoding="utf-8"))
        if not isinstance(log, list):
            log = [log]
        log.append(run_entry)
    else:
        log = [run_entry]

    LOG_PATH.write_text(
        json.dumps(log, indent=2, default=str), encoding="utf-8"
    )
    print(f"\n  Log saved: {LOG_PATH.name}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Wave 1B scraping runner for btc-index"
    )
    parser.add_argument(
        "--chapter", type=str,
        help="Chapter number or range (e.g., 4 or 4-6). Default: 4-9",
    )
    parser.add_argument(
        "--sub", type=str,
        help="Single sub-chapter to scrape (e.g., 4.1)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be scraped without fetching",
    )
    args = parser.parse_args()

    # Parse chapter range
    chapters = None
    if args.chapter:
        if "-" in args.chapter:
            lo, hi = args.chapter.split("-", 1)
            chapters = range(int(lo), int(hi) + 1)
        else:
            chapters = [int(args.chapter)]

    # Discover sub-chapters
    subs = discover_sub_chapters(chapters)

    # Optionally filter to single sub-chapter
    if args.sub:
        subs = [s for s in subs if s["sub_chapter"] == args.sub]
        if not subs:
            print(f"Sub-chapter {args.sub} not found or has no links.md")
            sys.exit(1)

    if not subs:
        print("No sub-chapters found in the specified range.")
        sys.exit(1)

    # Discovery summary
    actionable = [s for s in subs if s["pending_links"] > 0]
    done_count = len(subs) - len(actionable)

    print(f"\n  Discovered {len(subs)} sub-chapters "
          f"({len(actionable)} with pending links, {done_count} complete):")
    for s in subs:
        if s["pending_links"] > 0:
            status = f"{s['pending_links']} pending"
        else:
            status = "done"
        print(
            f"    Ch{s['sub_chapter']:5s} {s['title'][:40]:40s} "
            f"{s['total_links']:3d} links ({status})"
        )

    # Execute
    results = run_wave(subs, dry_run=args.dry_run)

    if results:
        save_log(results)


if __name__ == "__main__":
    main()

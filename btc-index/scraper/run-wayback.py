"""
Wayback Machine recovery pass (btc-index Phase 3B, Phase A).

Queries archive.org for snapshots of dead/404/WAF-blocked URLs,
fetches the archived HTML, extracts text via html2text, and writes
results to btc-index/scraped/.

Uses the Wayback Availability API to check for snapshots, then
fetches via the /web/{timestamp}id_/{url} endpoint (the id_ suffix
returns the original page without Wayback's toolbar injection).

Usage:
    python run-wayback.py                  # All categories (dead + 404 + WAF)
    python run-wayback.py --category dead  # Dead servers only
    python run-wayback.py --category 404   # 404 pages only
    python run-wayback.py --category waf   # WAF/403 blocked only
    python run-wayback.py --dry-run        # Show plan
    python run-wayback.py --resume         # Skip already-scraped

Run from btc-index/scraper/:
    ../mcp/.venv/Scripts/python.exe run-wayback.py
"""

import argparse
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

from scraper import _make_h2t, _strip_noise, MAX_CONTENT_CHARS

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRAPER_DIR = Path(__file__).resolve().parent
FAILURES_MD = SCRAPER_DIR / "consolidated-failures.md"

# ---------------------------------------------------------------------------
# URL lists parsed from consolidated-failures.md
# ---------------------------------------------------------------------------

# Dead web servers (Section 2, first table)
DEAD_URLS = [
    "https://acns.nwu.edu/surfpunk",
    "https://awesomelightningnetwork.com/",
    "https://cl.cam.ac.uk/users/iwj10",
    "https://cpsr.org/cpsr/states/california/cal_gov_info_FAQ.html",
    "https://cpsr.org/home",
    "https://cspsprotocol.com/p2p-network",
    "https://digicash.support.nl/",
    "https://dlc.link/solutions",
    "https://draco.centerline.com:8080/~franl/pgp/pgp-",
    "https://econtalk.org/nathaniel-popper-on-bitcoin-and-digital-gold",
    "https://exitcondition.alrubinger.com/2022/01/06/an-open-approach-to-financial-freedom",
    "https://iquest.com/~fairgate/privacy/index.html",
    "https://justice.gov/usao-nj/pr/somerset-county-man-charged-attempts-provide-material-support-hamas-making-false",
    "https://martigny.ai.mit.edu/~bal/pks-commands.html",
    "https://netmarket.com/",
    "https://news.earn.com/quantifying-decentralization-e39db233c28e",
    "https://offlinebitcoins.com/",
    "https://programmingbitcoin.com/understanding-segwit-block-size",
    "https://rgb-faq.com/",
    "https://rschp2.anu.edu.au:8080/crypt.html",
    "https://theprogressivebitcoiner.com/",
    "https://truthcoin.info/blog/protocol-upgrade-terminology",
    "https://win.tue.nl/win/math/dw/index.html",
]
# Skipped from dead list: "https://bitcoin" (bare domain, useless),
# "https://lndhub.io~~" (malformed)

# 404 / Page Gone (Section 2, second table)
FOUROHFOUR_URLS = [
    "https://arkdev.info/blog/liquidity-requirements",
    "https://bitcoinfoundation.org/bitcoin/core-development-update-5",
    "https://btclexicon.com/bitcoin-client",
    "https://btctools.org/opcodes-list",
    "https://coindesk.com/consensus-magazine/2023/10/30/what-will-wall-streets-bitcoin-narrative-be",
    "https://cointelegraph.com/innovation-circle/understanding-crypto-custody-what-different-solutions-entail-for-investors-and-businesses",
    "https://cointelegraph.com/learn/bitcoin-etfs-a-beginners-guide-to-exchange-traded-funds",
    "https://cointelegraph.com/learn/who-is-satoshi-nakamoto-the-creator-of-bitcoin",
    "https://cointelegraph.com/lightning-network-101/what-is-lightning-network-and-how-it-works",
    "https://eff.org/pub/Publications/Bruce_Sterling/cfp_",
    "https://fedimint.org/docs/FAQs/WhyCommunityCustody",
    "https://fedimint.org/docs/intro",
    "https://finance.yahoo.com/news/paying-taco-bell-dogecoin-may-113720323.html",
    "https://gamestation.net/d16-hexidice.html",
    "https://grayscale.com/crypto-products/grayscale-bitcoin-trust",
    "https://heliolending.com/2021/09/10/can-crypto-loans-help-pay-off-student-loans",
    "https://horizen.io/academy/zendoo",
    "https://learn.saylor.org/course/PRDV151",
    "https://lightco.in/2024/02/13/bitstake",
    "https://microsoft.com/en-us/research/publication/byzantine-generals-problem/_",
    "https://microstrategy.com/en/bitcoin/documents/stone-ridge-2020-shareholder-letter",
    "https://mycryptopedia.com/drivechain-explained",
    "https://nakamoto.com/bitcoin-becomes-the-flag-of-technology",
    "https://nakamoto.com/what-are-the-key-properties-of-bitcoin",
    "https://openmarket.com/info/cryptography/applied_crypt",
    "https://sequentia.io/academy",
    "https://tftc.io/issue-754",
    "https://whitehouse.gov/briefing-room/statements-releases/2022/02/26/joint-statement-on-further-restrictive-economic-measures",
]
# Skipped from 404 list: URLs with trailing junk chars (==, \, **) that
# would fail normalization anyway:
#   ark-protocol.com/j, bitrexe.com/about, en.bitcoin.it/wiki/Covenants_support\,
#   protos.com/...====, unchained.com/...==

# WAF/403 blocked (Section 3)
WAF_URLS = [
    "https://americanliterature.com/history/franklin-d-roosevelt/legislative/executive-order-6102",
    "https://americanthinker.com/blog/2021/10/ready_for_the_government_to_control_how_you_spend_your_money.html",
    "https://ark-invest.com/big-ideas-2023/bitcoin",
    "https://atlanticcouncil.org/blogs/econographics/strengthening-ties-china-and-the-gcc",
    "https://beincrypto.com/crypto-adoption-higher-minorities-lgbtq-america",
    "https://bitcoin.stackexchange.com/questions/106783/will-a-hard-fork-be-required-to-change-timestamp-fields",
    "https://bitcoin.stackexchange.com/questions/29554/explanation-of-what-an-op-return-transaction-looks-like",
    "https://bitcoin.stackexchange.com/questions/408/does-hoarding-really-hurt-bitcoin",
    "https://bitcoin.stackexchange.com/questions/79182/january-19th-2038-rip-unix-timestamps",
    "https://bitcoin.stackexchange.com/users/403/theymos",
    "https://bitcoinrollups.org/",
    "https://bitrefill.com/",
    "https://blockchain.info/",
    "https://blog.chain.link/dlc-link-chainlink-grant-bitcoin-discreet-log-contracts",
    "https://blog.trezor.io/how-bitcoin-boomed-in-2021-a64cccca6f71",
    "https://bloom.bg/dg-ws-core-bcom-m1",
    "https://cmegroup.com/education/featured-reports/an-in-depth-look-at-the-economics-of-bitcoin.html",
    "https://coinsutra.com/paid-blockchain-cryptocurrency-online-courses-certifications",
    "https://cs.berkeley.edu/~raph/remailer-list.html",
    "https://cygnus.com/~gnu/export.html",
    "https://dcjournal.com/the-end-of-the-money-middlemen",
    "https://fintel.io/fg/us/gbtc/CommonSharesOutstanding",
    "https://foundation.xyz/2023/02/making-sense-of-stealth-addresses",
    "https://gate.io/learn/articles/13-lines-of-code-help-bitcoin-implement-smart-contracts-understand-the-op-cat-soft-fork/1681",
    "https://group30.org/publications/detail/4950",
    "https://hrf.org/latest/cisa-research-paper",
    "https://hrw.org/news/2017/12/12/chinas-chilling-social-credit-blacklist",
    "https://inleo.io/@edicted/rune-lending-followup",
    "https://login.xyz",
    "https://mantis.co.uk/~mathew",
    "https://mantis.co.uk/pgp/pgp.html",
    "https://njump.me/nevent1qvzqqqqqqypzqgvra9r4sjqapufyl0vnc4kv4fz70e29em4c655y37vz206f0wt4qywhwumn8ghj7mn0wd68ytnzd96xxmmfdejhytnnda3kjctv9uq32amnwvaz7tmwdaehgu3wdau8gu3wv3jhvtcqyp0x6urd9zf37nl6p6r6ycvnphrx24gel0jgl5f0ck5dgmg9uhw4q4mkjnz",
    "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3141240",
    "https://politico.com/news/2022/01/16/bitcoin-crashes-the-midterms-527126",
    "https://pubsonline.informs.org/doi/abs/10.1287/mnsc.2023.4885",
    "https://qz.com/1642441/extradition-law-why-hong-kong-protesters-didnt-use-own-metro-cards",
    "https://qz.com/africa/1922466/how-bitcoin-powered-nigerias-endsars-protests",
    "https://rfc-editor.org/ien/ien2.txt",
    "https://sec.gov/Archives/edgar/data/1588489/000119312524003901/d144925ds3a.htm",
    "https://sec.gov/news/press-release/2023-139",
    "https://seekingalpha.com/symbol/BTC-USD",
    "https://seekingalpha.com/symbol/ETH-USD",
    "https://theafricareport.com/131083/african-countries-are-adopting-crypto-faster-than-their-global-counterparts",
    "https://thesaifhouse.wpcomstaging.com/2017/05/19/economics-of-bitcoin-as-a-settlement-network",
    "https://thoughtco.com/postal-service-losses-by-year-3321043",
    "https://udemy.com/course/bitcoin-certification",
    "https://weforum.org/great-reset",
]
# Skipped from WAF list: URLs with trailing junk (**), URL shorteners
# (bloom.bg, markets.createsend1.com x3), nostr event URLs (njump.me),
# obscure dead domains (nitv.net, mantis.co.uk)
# Actually kept mantis/njump -- Wayback might have them

# ---------------------------------------------------------------------------
# Wayback Machine API
# ---------------------------------------------------------------------------

WAYBACK_CHECK_URL = "http://archive.org/wayback/available"
WAYBACK_RAW_TPL = "https://web.archive.org/web/{timestamp}id_/{url}"

HEADERS = {
    "User-Agent": "btc-index-scraper/1.0 (educational research)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def check_wayback(url: str, client: httpx.Client) -> tuple[str | None, str]:
    """Check if Wayback Machine has a snapshot.

    Tries the original URL first, then a www-toggled variant (add or
    strip www.) since Wayback indexes these separately.

    Returns (timestamp, matched_url) or (None, url).
    """
    parsed = urlparse(url)
    variants = [url]

    # Build a www-toggled variant
    host = parsed.netloc
    if host.startswith("www."):
        alt_host = host[4:]
    else:
        alt_host = "www." + host
    alt_url = parsed._replace(netloc=alt_host).geturl()
    variants.append(alt_url)

    for variant in variants:
        try:
            resp = client.get(
                WAYBACK_CHECK_URL,
                params={"url": variant},
                timeout=15.0,
            )
            if resp.status_code == 200:
                data = resp.json()
                snapshot = data.get("archived_snapshots", {}).get("closest", {})
                if snapshot.get("available"):
                    return snapshot["timestamp"], variant
        except Exception:
            continue

    return None, url


def fetch_wayback(
    url: str, timestamp: str, client: httpx.Client, h2t: html2text.HTML2Text
) -> tuple[str, str, str]:
    """Fetch archived page content from Wayback Machine."""
    # Use id_ endpoint to get original HTML without Wayback toolbar
    wayback_url = WAYBACK_RAW_TPL.format(timestamp=timestamp, url=url)

    try:
        resp = client.get(wayback_url, follow_redirects=True, timeout=30.0)

        if resp.status_code == 200:
            ct = resp.headers.get("content-type", "")
            if "text/html" not in ct and "text/plain" not in ct:
                return "failed", "", f"Non-text content from Wayback ({ct[:40]})"

            html = resp.text
            if len(html) < 200:
                return "failed", "", "Wayback returned minimal content"

            # Strip noise, convert to markdown
            clean = _strip_noise(html)
            markdown = h2t.handle(clean)
            markdown = re.sub(r"\n{4,}", "\n\n\n", markdown)

            # Remove any residual Wayback toolbar artifacts
            markdown = re.sub(
                r'(?s)BEGIN WAYBACK TOOLBAR.*?END WAYBACK TOOLBAR', '', markdown
            )
            markdown = re.sub(
                r'(?s)<!-- BEGIN WAYBACK.*?END WAYBACK -->', '', markdown
            )
            markdown = markdown.strip()

            if len(markdown) > MAX_CONTENT_CHARS:
                markdown = (
                    markdown[:MAX_CONTENT_CHARS]
                    + "\n\n[... truncated at 20,000 characters ...]"
                )

            if len(markdown) < 100:
                return "partial", markdown, "Minimal text from Wayback archive"

            # Prepend archive metadata
            archive_date = f"{timestamp[:4]}-{timestamp[4:6]}-{timestamp[6:8]}"
            header = (
                f"*Archived version from {archive_date} "
                f"via Wayback Machine*\n\n"
            )
            return "done", header + markdown, ""

        elif resp.status_code == 404:
            return "failed", "", "Wayback snapshot not accessible (404)"
        else:
            return "failed", "", f"Wayback HTTP {resp.status_code}"

    except httpx.TimeoutException:
        return "failed", "", "Wayback fetch timeout"
    except Exception as e:
        return "failed", "", f"Wayback error: {str(e)[:80]}"


# ---------------------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------------------

def run_wayback_wave(
    urls: list[str],
    category: str,
    dry_run: bool = False,
    already_done: set = None,
) -> list[dict]:
    """Run Wayback Machine recovery on a list of URLs."""
    if already_done is None:
        already_done = set()

    actionable = [u for u in urls if u not in already_done]
    skipped_existing = len(urls) - len(actionable)

    if skipped_existing > 0:
        print(f"  Skipping {skipped_existing} already-scraped URLs")

    if not actionable:
        print("  Nothing to process.")
        return []

    print(f"\n  WAYBACK {category.upper()} WAVE: {len(actionable)} URLs")

    if dry_run:
        for u in actionable[:15]:
            print(f"    {u[:85]}")
        if len(actionable) > 15:
            print(f"    ... and {len(actionable) - 15} more")
        return []

    h2t = _make_h2t()
    results = []
    start = time.time()
    found = 0
    missed = 0

    with httpx.Client(headers=HEADERS, follow_redirects=True, timeout=30.0) as client:
        for i, url in enumerate(actionable, 1):
            domain = urlparse(url).netloc
            url_display = url[:75] + ("..." if len(url) > 75 else "")
            print(f"  [{i}/{len(actionable)}] {url_display}", end="", flush=True)

            t0 = time.time()

            # Step 1: Check availability (tries www-toggled variant too)
            timestamp, matched_url = check_wayback(url, client)

            if timestamp is None:
                elapsed = time.time() - t0
                print(f" MISS ({elapsed:.1f}s)")
                missed += 1

                # Write a failure record so we don't re-check
                write_scraped_file(
                    url, "", "failed", f"wayback-{category}",
                    [], "No Wayback snapshot found"
                )
                results.append({
                    "url": url, "status": "failed",
                    "chars": 0, "error": "No Wayback snapshot",
                })

                if i < len(actionable):
                    time.sleep(1.0)
                continue

            # Step 2: Fetch the archived content (use matched_url for Wayback)
            status, content, error = fetch_wayback(matched_url, timestamp, client, h2t)
            elapsed = time.time() - t0

            write_scraped_file(
                url, content, status, f"wayback-{category}",
                [], error
            )

            results.append({
                "url": url, "status": status,
                "chars": len(content), "error": error,
            })

            if status == "done":
                found += 1
                print(f" HIT {len(content):,}ch ({elapsed:.1f}s)")
            elif status == "partial":
                found += 1
                print(f" PARTIAL {len(content):,}ch ({elapsed:.1f}s)")
            else:
                missed += 1
                reason = f" -- {error}" if error else ""
                print(f" FAIL{reason} ({elapsed:.1f}s)")

            # Polite delay -- archive.org rate limits aggressively
            if i < len(actionable):
                time.sleep(1.5)

    total_time = time.time() - start
    total_chars = sum(r["chars"] for r in results)
    done = sum(1 for r in results if r["status"] in ("done", "partial"))
    failed = sum(1 for r in results if r["status"] == "failed")

    print(f"\n  WAYBACK {category.upper()} COMPLETE:")
    print(f"    {done} recovered, {failed} not found")
    print(f"    {total_chars:,} chars in {total_time:.1f}s")

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Wayback Machine recovery pass"
    )
    parser.add_argument(
        "--category",
        choices=["dead", "404", "waf", "all"],
        default="all",
        help="Which URL category to process (default: all)",
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    already_done = set()
    if args.resume:
        already_done = find_already_scraped()
        print(f"Resume mode: {len(already_done)} URLs already scraped")

    all_results = []
    categories = {
        "dead": DEAD_URLS,
        "404": FOUROHFOUR_URLS,
        "waf": WAF_URLS,
    }

    if args.category == "all":
        run_list = ["dead", "404", "waf"]
    else:
        run_list = [args.category]

    total_urls = sum(len(categories[c]) for c in run_list)

    print(f"\n{'#' * 60}")
    print(f"  WAYBACK MACHINE RECOVERY PASS")
    print(f"  Categories: {', '.join(run_list)}")
    print(f"  Total URLs: {total_urls}")
    print(f"{'#' * 60}")

    for cat in run_list:
        urls = categories[cat]
        results = run_wayback_wave(
            urls, cat, dry_run=args.dry_run, already_done=already_done,
        )
        all_results.extend(results)

    if not args.dry_run and all_results:
        total_done = sum(1 for r in all_results if r["status"] in ("done", "partial"))
        total_failed = sum(1 for r in all_results if r["status"] == "failed")
        total_chars = sum(r["chars"] for r in all_results)

        print(f"\n{'#' * 60}")
        print(f"  OVERALL: {total_done} recovered, {total_failed} not found")
        print(f"  Total content: {total_chars:,} chars")
        print(f"{'#' * 60}")

        # Write summary log
        log_path = SCRAPER_DIR / "wayback-log.json"
        log_data = {
            "timestamp": datetime.now().isoformat(),
            "categories": run_list,
            "total_urls": len(all_results),
            "recovered": total_done,
            "not_found": total_failed,
            "total_chars": total_chars,
            "results": all_results,
        }
        log_path.write_text(
            json.dumps(log_data, indent=2, default=str),
            encoding="utf-8",
        )
        print(f"  Log: {log_path.name}")


if __name__ == "__main__":
    main()

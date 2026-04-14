# TBB Worklog

**Daily To-Do:** `tasks/TODO.md`

## Last Session
**Date:** 2026-04-13 (session 23)

### What Was Done

**btc-index Phase 3B -- Wayback Machine Recovery + Phase B Retries**
- Built `run-wayback.py`: queries archive.org Availability API, fetches via /web/{timestamp}id_/ endpoint (raw HTML, no toolbar injection)
  - Bug found: Wayback API does exact domain matching -- `coindesk.com` misses but `www.coindesk.com` hits. Added www-toggle fallback.
- **Phase A -- Wayback Machine pass (98 URLs across 3 categories):**
  - Dead servers: 8/23 recovered, 80K chars (EconTalk, earn.com/Quantifying Decentralization, digicash.support.nl, programmingbitcoin.com)
  - 404 pages: 7/28 recovered, 28K chars (BitcoinFoundation, CoinDesk Wall Street narrative, WhiteHouse.gov joint statement)
  - WAF/403 blocked: 20/47 recovered, 250K chars (Executive Order 6102, StackExchange x2, bitcoinrollups.org, SEC filings x2, Politico, Quartz HK, RFC IEN-2, SeekingAlpha x2, Saifedean settlement network)
- **Phase B -- Timeout/error retries (14 URLs):**
  - 9/14 recovered, 45K chars (DTCC via Wayback, FRED via browser, founders.archives.gov Washington letter 15K, developer.tbd.website via Wayback)
  - Investopedia x2 still timing out (Apify candidate)
- **GitHub README fix:** 3 repos (bitcoin/bips, bip420, hamstr) used README.mediawiki or README.MD -- fetched directly, 47K chars
- **Totals: 47 URLs recovered, ~450K new chars added to corpus**
- Corpus: 744 files -- 580 DONE, 38 PARTIAL, 124 FAILED (down from ~193 FAILED)

### Next Session Pickup Prompt

```
check worklog and continue.

FIRST TASK: Commit all uncommitted work (673 files). Suggested split:
1. btc-index scraping pipeline + scraped content + WBIGAF links/sources updates + worklogs (focused commit)
2. Everything else (Bitcoin Notes, Voice DNA, WBIGAF new chapters, Ark notes, misc)
Stage specific files by name per git workflow rules. Do NOT use git add -A.

THEN continue btc-index Phase 3B failure recovery:
C. Check notebook context -- for remaining ~68 Wayback misses, check if the Bitcoin Note that linked the URL already has the content inline (quote, summary, argument). If so, the scrape is unnecessary and those can be marked as covered.
D. Apify batch on 36 Medium URLs + Investopedia x2 (last resort, user-approved)

After recovery:
- Re-index full corpus (btc-index ingest)

Session 23 completed Phases A + B:
- Built run-wayback.py (Wayback Machine API + www-toggle fix)
- Wayback pass: 35/98 recovered (358K chars) across dead/404/WAF categories
- Phase B retries: 9/14 recovered (45K chars) via Wayback + browser fallback
- GitHub README fix: 3 repos (bitcoin/bips, bip420, hamstr) used README.mediawiki/.MD -- 47K chars
- Total: 47 URLs recovered, ~450K new chars
- Corpus: 744 files, 580 DONE / 38 PARTIAL / 124 FAILED

Key scraper scripts (all in btc-index/scraper/): scraper.py, run-wave.py, run-bitcoin-notes.py, run-github.py, run-reddit.py, gen-failure-doc.py, run-wayback.py
```

### What's Next

**btc-index Phase 1-2 (COMPLETE)**
- [x] Build 4 Python files (chunker, indexer, server, normalizer stub)
- [x] Set up venv and install dependencies
- [x] Run initial corpus ingestion (960 chunks, 181 files, ~17 min)
- [x] Test all 4 MCP tools (search_corpus, list_sources, get_chunk, find_related)
- [x] Register in .mcp.json, add .gitignore entries
- [x] Commit Phase 1 (`de60ca4`)
- [x] Build `/ingest` command + incremental pipeline (Phase 2)
- [x] Ingest 362 Bitcoin Notes into corpus (396 chunks)

**btc-index Phase 3 -- WBIGAF Remaining (15 URLs)**
- [x] Build scraper.py + run-wave.py
- [x] Run Wave 1B scraping (52 sub-chapters, 239 links)
- [x] Add Patchright browser fallback + --retry-failed mode
- [x] Run retry wave (73 recovered, 28 still failed, 8 paywalled skipped)
- [x] Try free methods on 4 non-Medium failures (httpx, Patchright, Wayback -- all failed)
- [ ] Run Apify on consolidated Medium list (36 unique) + Investopedia x2 + Quartz (39 total)
- [ ] Update links.md statuses + sources.md content for recoveries

**btc-index Phase 3B -- Bitcoin Notes URL Wave**
- [x] Build URL extraction + normalization + verified dedup + categorization (`bitcoin-notes-prep.py`)
- [x] Build Bitcoin Notes scraper runner (`run-bitcoin-notes.py`)
- [x] Generate URL list files (scrapable: 564, tweets: 133, medium: 31)
- [x] Smoke-test article scraping (`--category scrapable --limit 20`)
- [x] Run full article wave -- 372 done, 32 partial, 158 failed, 5.1M chars
- [x] Upgrade fetch_tweet to fxtwitter API + thread detection
- [x] Run full tweet wave -- 122 done, 11 failed (deleted), 75K chars
- [x] Confirm threads captured (thread detection worked, no re-run needed)
- [x] GitHub extraction -- 44/48 done, 515K chars (run-github.py)
- [x] Reddit extraction -- 8/8 done, 160K chars (run-reddit.py)
- [x] Build consolidated failure doc (207 URLs, 9 categories, 4-phase recovery plan)
- [x] Wayback Machine pass on 98 URLs (Phase A) -- 35 recovered, 358K chars
- [x] Retry timeout/error URLs with Wayback + browser (Phase B, 14 URLs) -- 9 recovered, 45K chars
- [x] Fix GitHub README.mediawiki/.MD lookups -- 3 repos, 47K chars
- [ ] Check notebook context for remaining failures (Phase C)
- [ ] Run Apify on 36 Medium URLs + WAF survivors (Phase D, last resort)

**Post-Scraping**
- [ ] Re-index entire corpus (WBIGAF sources.md + Bitcoin Notes scraped content)
- [ ] Commit all Phase 2 + 3 + 3B work
- [ ] Claim extraction pass: Claude reads sources.md, generates catalog items #200+ per sub-chapter

**WBIGAF Pipeline (after btc-index)**
- [ ] Wave 1A spot-check (2-3 sub-chapters per chapter, 13 total)
- [ ] 3.3/3.4/3.5: Research prompts + deep research (Steps 3B-4)
- [ ] 3.2: Publish blocks to website (Step 6)

**Podcast Launch Series -- Scripts Written, Ready for User Review**
- [ ] User read-through of EP01 script: mark where it doesn't sound like you
- [ ] User read-through of EP02-EP05 scripts (same pass)
- [ ] Try the new RANT workflow: pick one episode, record a raw brain dump, transcribe, re-script
- [ ] Set up Spotify for Podcasters account
- [ ] Record EP01 (OBS, audio-only, one take)
- [ ] Publish first podcast episode

**TBB Media Company -- Legal (parked)**
- [x] Review Dow Jones employment agreement (non-compete, moonlighting)
- [ ] File DBA for "The Bitcoin Breakdown"
- [ ] Draft operating agreement

**TBB Media Company -- Production Setup (parked)**
- [ ] Set up YouTube channel
- [ ] Set up Beehiiv newsletter (free tier)
- [ ] Set up social accounts and Buffer scheduling

**ArkFloat (parked)**
- [ ] Run `/ark-expert` on Bark hArk sighash question
- [ ] Unit economics: does 1-3% LP fee fit inside ASP fee revenue at scale?

**TBB Website (parked)**
- [ ] Update body prose text to `#A8A39A` in global.css

---

## Session History

### 2026-04-12 -- GitHub/Reddit Extraction + Failure Consolidation (session 22)
- Confirmed tweet threads captured (thread detection worked -- top files are full multi-tweet threads)
- Built + ran `run-github.py`: 44/48 done, 515K chars in 31.6s (BIPs, READMEs, PRs, gists)
- Built + ran `run-reddit.py`: 8/8 done via JSON API, 160K chars in 28.3s (zero failures)
- Built `gen-failure-doc.py` and generated `consolidated-failures.md`: 207 URLs across 9 categories
- Failure triage: 41 truly dead (skip), 58 Wayback candidates, 52 WAF/403, 20 timeout, 36 Medium (Apify queue)

### 2026-04-12 -- btc-index Phase 3B Scraping + Failure Triage (session 21)
- Committed Phase 3B pipeline files (`c9e3517`): bitcoin-notes-prep.py, run-bitcoin-notes.py, URL lists, failed-urls.md
- Fixed `__pycache__` gitignore, installed `brotli`, upgraded `scraper.py:fetch_tweet()` to fxtwitter API + thread detection
- Ran full article wave: 372 done (66%), 32 partial, 158 failed -- 5.1M chars in 42.5 min
- Ran full tweet wave: 122 done (92%), 11 failed (deleted accounts) -- 75K chars in 8.4 min
- Consolidated Apify candidate list: 36 unique Medium + 2 Investopedia + 1 Quartz = 39 URLs

*Sessions 8-20 archived to WORKLOG-ARCHIVE.md on 2026-04-13*

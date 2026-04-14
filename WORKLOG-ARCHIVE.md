# TBB Worklog -- Session Archive

Archived from WORKLOG.md when session history exceeded 10 entries.

---

## Archived 2026-04-13 (sessions 8-20)

### 2026-04-11 -- EP02-EP05 Scripts + 2112 Vision + Rant Workflow (session 20)
- Wrote 4 podcast scripts (EP02-EP05) matching EP01's format from WBIGAF/source library
- Reviewed full monetization plan: 11 revenue streams, 3-tier estimates ($8K-$94K Bitcoin-only)
- Added Expanded 2112 Vision to synthesis.md: dual content engine, phased expansion, $14K-$145K estimates
- Updated production workflow: added RANT step (record brain dump -> transcribe -> AI script)

### 2026-04-12 -- btc-index Bitcoin Notes URL Pipeline Built (session 19)
- Built `bitcoin-notes-prep.py`: full extraction + normalization + verified dedup + categorization pipeline
- URL normalizer: strips trailing slashes, tracking params, anchors; forces https/lowercase/no-www; domain-aware param rules
- Verified dedup: compares normalized Bitcoin Notes URLs against WBIGAF links.md DONE/PARTIAL rows AND confirms content exists in sources.md (fixes Session 18 flaw)
- Results: 1,093 raw -> 1,043 unique -> only 20 verified overlap with WBIGAF
- Final categorization: 564 scrapable, 133 tweets, 31 Medium, 53 GitHub, 9 Reddit, 233 skip
- Built `run-bitcoin-notes.py`: scraper runner with --resume, --category, --limit flags
- Dry run verified, output files generated

### 2026-04-12 -- btc-index Bitcoin Notes URL Scoping + Apify Eval (session 18)
- Scoped Bitcoin Notes URL corpus: 1,090 unique URLs across 365 note files
- Categorized URLs: ~640 scrapable, 181 tweets, 103 YouTube, 86 paywalled, 55 GitHub, 16 junk, 9 Medium
- Evaluated Apify for Cloudflare/CAPTCHA bypass; decision: run existing pipeline first, Apify free tier on failures
- Identified dedup flaw: naive method matched against article body text, not source URLs with DONE status

### 2026-04-11 -- btc-index Patchright Retry Wave (session 17)
- Added Patchright browser fallback + tweet handler + domain routing to scraper.py
- Ran retry wave: 73 recovered, 11 partial, 28 failed, 8 skipped (paywalled)
- Overall WBIGAF scrape success: 45% -> ~80% (757K new chars)
- Created failed-urls.md: 15 actionable URLs (11 Medium, 4 other)

### 2026-04-11 -- btc-index Wave 1B Scraping (session 16)
- Built scraping pipeline: scraper.py (httpx + html2text) and run-wave.py (batch orchestrator)
- Ran full Wave 1B: 52 sub-chapters, 239 links in 7.7 minutes
- Results: 84 DONE (33%), 31 PARTIAL (12%), 123 FAILED (49%), 14 SKIP (6%)
- Failures structural: Cloudflare-protected sites (Bitcoin Magazine, Medium, Reddit, Twitter)
- Created 52 sources.md files totaling 710K chars

### 2026-04-11 -- btc-index Phase 2 Ingest + Phase 3 Scraping (session 15)
- Extended chunker/indexer for user note ingestion (362 files, 396 chunks)
- Committed Phase 1: `de60ca4` (7 files, 1,049 insertions)
- Corpus grew from 960 to 1,356 chunks (181 WBIGAF + 362 user notes)

### 2026-04-11 -- btc-index Phase 1 Commit + Phase 2 Ingest (session 14)
- Built btc-index MCP server: 4 tools (search_corpus, list_sources, get_chunk, find_related)
- Indexed 960 chunks from 181 files (WBIGAF, guide, blog sources)
- Registered in .mcp.json, .vectordb/.venv/.pycache/meta gitignored

### 2026-04-08 -- Voice DNA Expansion + EP01 Rewrite (session 13)
- Analyzed Voice DNA Examples.txt (379 lines spoken/journal content) against existing profile
- Updated Voice DNA profile with 8 new rules, 2 new voice modes, 9 new sentence skeletons
- Rewrote EP01 Golden Rules script (~2,314 words, ~17-18 min spoken)

### 2026-04-07 -- Directory Rename Spaces to Hyphens (session 12)
- Committed 643 pending files, gitignored 6 embedded repos
- Renamed 110+ directories via `git mv` (children-first, deepest paths first)
- Updated path references in 12+ files, Astro build verified (64 pages, 0 errors)
- 2 commits: `fc0e204` (pending work), `cd8088d` (renames + reference updates)

### 2026-04-07 -- EP01 Script Draft, WBIGAF MCP Plan, Directory Rename Plan (session 11)
- Created EP01 Golden Rules speakable outline script at `tbb-media-company/podcast/episodes/ep01-golden-rules/script.md`
- Added 3-phase WBIGAF MCP server plan to TODO.md
- Explored directory rename scope (~110 dirs with spaces), wrote 5-phase plan (not executed this session)

### 2026-04-06 -- TBB Media Company Archive Synthesis & Setup (session 10)
- Read and synthesized 280+ files across three legacy archive folders (2025-2035, 2112, The Bitcoin Breakdown)
- Created 3 reference files: synthesis.md, teaching-framework.md, episode-roadmap.md
- Updated TBB Media Company/CLAUDE.md (173 -> 299 lines) and Phase 14 in TODO.md
- Key decisions: 2112 Capital Solutions LLC as umbrella, TBB as DBA, EP01 Golden Rules first, S-Corp deferred

### 2026-03-28 -- ArkFloat Published to Website (session 8)
- Published ArkFloat whitepaper as blog post and standalone HTML
- Added subtitle field to content schema, updated media grid layout
- 4 commits pushed, site deployed via GitHub Actions

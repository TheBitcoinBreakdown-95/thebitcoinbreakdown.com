# TBB Worklog

**Daily To-Do:** `tasks/TODO.md`

## Last Session
**Date:** 2026-04-11 (session 16)

### What Was Done

**btc-index Phase 3 -- Wave 1B Scraping COMPLETE**
- Built scraping pipeline: `btc-index/scraper/scraper.py` (core fetcher + html2text extraction) and `run-wave.py` (wave runner with discovery, progress, logging)
- Installed `html2text` in btc-index venv
- Tested on 4.1 (8 links) -- verified sources.md format, links.md status updates, chunker compatibility
- Ran full Wave 1B: 52 sub-chapters, 239 links processed in 7.7 minutes
- Results: 84 DONE (33%), 31 PARTIAL (12%), 123 FAILED (49%), 14 SKIP (6%)
- Failures are structural: Bitcoin Magazine, Medium, Reddit, Twitter all Cloudflare-protected
- Created 52 `sources.md` files totaling 1.1 MB (710K chars) of scraped content
- All 61 `links.md` files updated with final statuses -- 0 PENDING remain
- YouTube handled via oEmbed API (title + channel metadata)
- Run log saved to `btc-index/scraper/wave-1b-log.json`

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

**btc-index Phase 3 (SCRAPING COMPLETE, post-processing pending)**
- [x] Build scraper.py + run-wave.py
- [x] Run Wave 1B scraping (52 sub-chapters, 239 links)
- [ ] Re-index corpus (run `python indexer.py` to pick up 52 new sources.md -- corpus should grow from 1,356 to ~1,500+ chunks)
- [ ] Commit Phase 2+3 work (Phase 2 user note ingestion + Phase 3 scraper + scraped content)
- [ ] Handle 123 failed links (Claude WebFetch retry, manual copy-paste, or accept gaps)
- [ ] Claim extraction pass: Claude reads sources.md, generates catalog items #200+ per sub-chapter

**WBIGAF Pipeline (after btc-index)**
- [ ] Wave 1A spot-check (2-3 sub-chapters per chapter, 13 total)
- [ ] 3.3/3.4/3.5: Research prompts + deep research (Steps 3B-4)
- [ ] 3.2: Publish blocks to website (Step 6)

**EP01 -- Ready for User Review**
- [ ] User read-through of rewritten script: mark where it doesn't sound like you
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

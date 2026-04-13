# TBB Worklog

**Daily To-Do:** `tasks/TODO.md`

## Last Session
**Date:** 2026-04-11 (session 20)

### What Was Done

**TBB Media Company -- EP02-EP05 Scripts + Business Strategy + Workflow Update**
- Wrote 4 podcast scripts (EP02-EP05) matching EP01's format, pulled from WBIGAF/source library:
  - EP02: Hello World (5-10 min) -- personal intro, bitcoin journey 2012-2021, why TBB exists
  - EP03: Why Bitcoin? The 10-Minute Case (10-15 min) -- emotional/practical elevator pitch
  - EP04: What is Money, Really? (15-20 min) -- barter->gold->fiat->bitcoin, Collapse of Trust framework
  - EP05: Bitcoin Will Save the World (15-20 min) -- Cantillon effect, CFA Franc, CBDCs, the mission
- Each script has: cold open, "Yo it's GC" intro, timed sections, close, production notes (tone shifts, signature phrases, rhythm, what NOT to do)
- Reviewed full monetization plan: 11 revenue streams across content + services
  - 3-tier estimates: Very Low $8K, Low $33K, Medium $94K (Bitcoin-only)
- Added "Expanded 2112 Vision" to `synthesis.md`: dual content engine model (TBB + FreedomLab -> 2112 services umbrella)
  - Phased expansion beyond Bitcoin into AI / privacy / self-hosting / basics
  - Expanded revenue estimates: Very Low $14K, Low $54K, Medium $145K
  - Decision: launch Bitcoin services first, layer on others as demand materializes
- Updated production workflow in both `CLAUDE.md` and `synthesis.md`: added RANT step (step 2 of 6)
  - Record raw brain dump -> transcribe with Whisper -> AI combines best lines with source research -> final script
  - Solves the "brain-dumping > scripting" preference while still producing polished output

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
- [ ] Try Apify free tier on 11 Medium articles from `btc-index/scraper/failed-urls.md`
- [ ] Try WebFetch/Apify on 4 non-Medium failures (Investopedia x2, Yahoo Finance, Quartz)
- [ ] Update links.md statuses + sources.md content for recoveries

**btc-index Phase 3B -- Bitcoin Notes URL Wave**
- [x] Build URL extraction + normalization + verified dedup + categorization (`bitcoin-notes-prep.py`)
- [x] Build Bitcoin Notes scraper runner (`run-bitcoin-notes.py`)
- [x] Generate URL list files (scrapable: 564, tweets: 133, medium: 31)
- [ ] Smoke-test article scraping (`--category scrapable --limit 20`)
- [ ] Run full article wave (564 URLs, ~37 min)
- [ ] Smoke-test tweet scraping (`--category tweet --limit 10`)
- [ ] Run full tweet wave (133 URLs, ~17 min)
- [ ] Run Apify on 31 Medium URLs (needs token in .env)
- [ ] Decide on GitHub URLs (53) -- extract READMEs or skip?
- [ ] Decide on Reddit URLs (9) -- Patchright or skip?

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

# TBB Worklog

**Daily To-Do:** `tasks/TODO.md`

## Last Session
**Date:** 2026-04-11 (session 15)

### What Was Done

**btc-index Phase 1 -- Committed**
- Committed Phase 1 work: `de60ca4` (7 files, 1,049 insertions)
- Staged: 4 Python modules, requirements.txt, .gitignore, .mcp.json

**btc-index Phase 2 -- COMPLETE (user note ingestion)**
- Extended `chunker.py` `discover_files()` to scan `Bitcoin Notes/` as `user_note` source type (skips `Memes/` -- image-only)
- Added `ingest_notes()` to `indexer.py` -- incremental pipeline that compares file hashes, only processes new/changed files, appends to existing LanceDB without full rebuild
- Added `--ingest` CLI flag to indexer.py
- Created `/ingest` slash command at `.claude/commands/ingest.md`
- Ran ingest: 362 files -> 396 chunks embedded in 362s (~1 chunk/sec)
- Corpus grew from 960 to **1,356 chunks** (181 WBIGAF/guide/blog files + 362 user notes)
- Verified with `search_corpus` queries -- user_note content fully searchable

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

**btc-index Phase 3 (next)**
- [ ] Build autonomous scraping loop: coordinator + scraper + checker + organizer agents
- [ ] Run Wave 1B scraping overnight (Ch4 first, then Ch5-9)
- [ ] Commit Phase 2 work

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

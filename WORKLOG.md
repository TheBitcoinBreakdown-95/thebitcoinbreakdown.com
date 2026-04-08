# TBB Worklog

**Daily To-Do:** `tasks/TODO.md`

## Last Session
**Date:** 2026-04-07 (session 11)

### What Was Done

**EP01 Golden Rules Script -- First Draft (COMPLETE)**
- Read and synthesized 3 archive source files: Golden Rules Brain Dump.md, GR Script.md, Da Rules.md
- Read Voice DNA profile and teaching framework to inform script structure
- Created `tbb-media-company/podcast/episodes/ep01-golden-rules/script.md` -- speakable outline format
  - Cold open + intro + 6 rules + close (~15-20 min target)
  - Each rule has bullet-point talking points + one-liner drop (Voice DNA pattern: long build-up -> short declarative payoff)
  - Cold open uses teaching framework Phase 1: Inspire ("burning question" tactic)
  - Production notes with tone shifts per rule and signature phrases to work in
- [x] Pull Golden Rules brain dump script from archive
- [x] Edit into speakable outline (talking points, not prose)
- [x] AI polish pass using Voice DNA profile

**WBIGAF MCP Server -- Added to TODO.md**
- Replaced old "Argument Block RAG System" entry with 3-phase WBIGAF MCP server plan
  - Phase 1: Argument blocks + catalog files (schema, vector store, ingestion, MCP tools)
  - Phase 2: Compendium + blog posts (expand to all content types)
  - Phase 3: Episode integration (cross-reference tool, post-EP03 skill extraction)

**Directory Rename Plan -- Spaces to Hyphens (PLANNED, NOT EXECUTED)**
- Explored full scope: ~110 directories with spaces, 167 git-tracked files, 94 untracked items
- Discovered WBIGAF ch5-9 split state: old flat files tracked-but-deleted, new subdirs untracked
- Wrote full plan at `.claude/plans/valiant-wandering-gem.md` with 5 phases:
  - Phase 0: Commit pending changes (162 items) to clean working tree
  - Phase 1: `git mv` tracked dirs (~85 renames, children-first)
  - Phase 2: `mv` untracked dirs (~35 renames)
  - Phase 3: Update text references in ~16 files
  - Phase 4-5: Commit + verify (Astro build, grep sweep, link spot-check)
- Identified highest risk: unicode ellipsis in WBIGAF ch6 directory name
- Saved memory: `feedback_no_spaces_in_paths.md`

### What's Next

**Directory Rename -- Execute the plan (next action)**
- [ ] Phase 0: Commit 162 pending changes, create safety tag
- [ ] Phase 1: git mv all tracked directories (WBIGAF, Ark, TBB/Website planning)
- [ ] Phase 2: mv all untracked directories (TBB Media Company, JC Bitcoin, FreedomLab, Content)
- [ ] Phase 3: Update text references in CLAUDE.md, TODO.md, WORKLOG.md, WBIGAF.md, etc.
- [ ] Phase 4-5: Commit rename + verify (Astro build, grep sweep, clickable links)

**EP01 -- User Review (after rename)**
- [ ] User read-through of script: add riffs, cut what's wrong, mark emphasis points
- [ ] Set up Spotify for Podcasters account
- [ ] Record EP01 (OBS, audio-only, one take)
- [ ] Publish first podcast episode

**TBB Media Company -- Legal (not blocking EP01)**
- [ ] Review Dow Jones employment agreement (non-compete, moonlighting)
- [ ] File DBA for "The Bitcoin Breakdown" -- Hudson County Clerk (~$50-75)
- [ ] Draft operating agreement

**TBB Media Company -- Production Setup (alongside EP01)**
- [ ] Set up YouTube channel
- [ ] Set up Beehiiv newsletter (free tier)
- [ ] Set up social accounts and Buffer scheduling

**ArkFloat (parked)**
- [ ] Run `/ark-expert` on Bark hArk sighash question
- [ ] Unit economics: does 1-3% LP fee fit inside ASP fee revenue at scale?

**TBB Website / WBIGAF (parked)**
- [ ] Update body prose text to `#A8A39A` in global.css
- [ ] 3.2: Publish blocks to website (Step 6)
- [ ] 3.3/3.4/3.5: Research prompts + deep research (Steps 3B-4)
- [ ] Coordinator design: tracker format, prompt, handoff brief

---

## Session History

### 2026-04-06 -- TBB Media Company Archive Synthesis & Setup (session 10)
- Read and synthesized 280+ files across three legacy archive folders (2025-2035, 2112, The Bitcoin Breakdown)
- Created 3 reference files: synthesis.md, teaching-framework.md, episode-roadmap.md
- Updated TBB Media Company/CLAUDE.md (173 -> 299 lines) and Phase 14 in TODO.md
- Key decisions: 2112 Capital Solutions LLC as umbrella, TBB as DBA, EP01 Golden Rules first, S-Corp deferred

### 2026-03-28 -- ArkFloat Published to Website (session 8)
- Published ArkFloat whitepaper as blog post and standalone HTML
- Added subtitle field to content schema, updated media grid layout
- 4 commits pushed, site deployed via GitHub Actions

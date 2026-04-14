# WBIGAF Status

> **Last updated:** March 15, 2026

---

## Current Work

**Book Reference Documents** — COMPLETE. Three new master documents created and integrated into pipeline:
- `toc.md` — Table of contents: 86 sub-chapters across 9 chapters, with argument block titles for Ch3.1 (23 blocks) and Ch3.2 (19 blocks). Updates at Steps 4 and 5.
- `bibliography.md` — Master bibliography: 66 unique Chicago-format sources from Ch3.1 + Ch3.2, de-duplicated and alphabetized. Updates at Steps 2 and 3.
- `glossary.md` — Glossary template: empty, back-burner document populated during Step 6 (drafting).
- Pipeline integration: one line added to Steps 2, 3, 4, 5, 6 in WBIGAF.md. Architecture tree and Key Files table updated.

**Argument Block Model v2** — COMPLETE. Updated spec + retrofitted Ch3.1 and Ch3.2 catalogs.

**Chapter 3: Problems Bitcoin Solves** — Sub-Chapters 3.3, 3.4, 3.5 — **Step 3 Part A COMPLETE (Gap Analysis + Research Prompts)**

Ch3.1 COMPLETE (deployed, catalog retrofitted to v2). Ch3.2 Draft complete (Step 6), Step 7 user review deferred, catalog retrofitted to v2. Ch3.3, 3.4, 3.5 all through Steps 1-2 (Triage + Scrape) and Step 3 Part A (Gap Analysis + Research Prompt). Research prompts ready for user to run through Gemini/ChatGPT/Perplexity.

**Next action:** User runs 3 research prompts (one per sub-chapter) through off-platform deep research tools, then pastes results back.

**Website:** Phase 11 Compendium Fixes COMPLETE (8 issues, 3 tiers). See `tasks/TODO.md` Phase 11.

**Ch3.1 Voice DNA Review:** 4 items flagged (2 duplications, 1 jargon, 1 self-quote). User has additional opinions — next session will focus on rewriting one argument block together as a voice calibration exercise, then extrapolate to the rest.

`WBIGAF/3-what-problems-does-it-solve/chapter-3-metadata/transition-ch3.md`

---

## Chapter Overview

| # | Chapter | Sub-chapters | Source Words | Status |
|---|---------|-------------|-------------|--------|
| 1 | What is Bitcoin | 2 | 12,063 | Existing guide chapter — surgical edits later |
| 2 | Why Bitcoin | 6 | 17,050 | Existing guide chapter — surgical edits later |
| **3** | **Problems Bitcoin Solves** | **6** | **11,616** | **IN PROGRESS — 3.1 DONE, 3.2 Draft done (Step 7 deferred), 3.3/3.4/3.5 at Step 3A (research prompts ready)** |
| **4** | **Bitcoin Past** | **6** | **8,392** | **IN PROGRESS — Step 1 DONE (all 5 sub-chapters triaged), 4.2 Step 2 DONE (user scraped)** |
| 5 | Bitcoin Properties | 21 | 16,134 | Pending |
| 6 | What is Bitcoin Exactly | 7 | 8,590 | Pending (add "How Bitcoin Works" sub-chapter) |
| 7 | Bitcoin Present | 7 | 5,687 | Pending |
| 8 | Why BTC is Good AF | 13 | 22,256 | Pending |
| 9 | Bitcoin Future | 9 | 2,576 | Pending (9.10 Step 1 done) |

**68 total sub-chapters** across Ch3-9. Each sub-chapter = one WBIGAF source file, expanded to whatever length the arguments merit.

---

## Expansion Order

1. **Ch 3: Problems Bitcoin Solves** (6 sub-chapters, 11,616 source words) — IN PROGRESS
2. Ch 5: Bitcoin Properties (21 sub-chapters, 16,134 source words)
3. Ch 8: Why Bitcoin is Good AF (13 sub-chapters, 22,256 source words)
4. Ch 4: Bitcoin Past (6 sub-chapters, 8,392 source words)
5. Ch 6: What is Bitcoin Exactly (7 sub-chapters — 6 source + NEW "How Bitcoin Works")
6. Ch 7: Bitcoin Present (7 sub-chapters, 5,687 source words)
7. Ch 9: Bitcoin Future (9 sub-chapters, 2,576 source words -- 9.10 System-Agnostic Money added)

---

## Chapter Progress

| Chapter | Transition Doc | Sub-Chapters Started |
|---------|---------------|---------------------|
| Ch 3 | `WBIGAF/3-what-problems-does-it-solve/chapter-3-metadata/transition-ch3.md` | 3.1 COMPLETE (deployed), 3.2 Draft done (Step 7 deferred), 3.3 Step 3A done (120 items, 13 gaps, prompt ready), 3.4 Step 3A done (138 items, 13 gaps, prompt ready), 3.5 Step 3A done (207 items, 13 gaps, prompt ready) |
| Ch 4 | `WBIGAF/4-bitcoin-past/chapter-4-metadata/transition-ch4.md` | 4.1 Step 1 done (59 items, 8 links), 4.2 Step 2 done (105 items, 10 links — user scraped), 4.3 Step 1 done (29 items, 4 links), 4.4 Step 1 done (47 items, 11 links), 4.5 Step 1 done (74 items, 12 links) |
| Ch 5-9 | Not yet created | None |

---

## Completed Work

### Voice DNA Extraction — COMPLETE
Full author voice profile built from 28-post corpus (~37,000 words of original writing).

**Steps completed:**
- [x] **8a:** Built condensed L1-L7 framework from source methodology (~37,700 words)
- [x] **8b:** Corpus analysis in 3 parallel batches (28 posts analyzed)
- [x] **8c:** Synthesized 3 batch observations into final profile (7 deliverables)
- [x] **8d:** Validation — test passage reviewed, voice/rhythm confirmed
- [x] **8e:** Methodology integration — 17 improvements applied (469 → 761 lines)

**Profile:** `WBIGAF/0-project/voice-dna/voice-dna-profile.md` (761 lines, 8 sections)
**Validation:** Two test passages scored perfectly (Mining 15/15, Separation of Money & State 19/19)

**All Voice DNA files:** `WBIGAF/0-project/voice-dna/`

### Chapter 3.1 Fiat Capitalism — COMPLETE (Steps 1-7)

**Step 6 — Draft:** ~10,000 words, 23 sections, 241 endnotes, V4 effects applied
**Step 7 — Published:** Draft deployed to website at `/guide/fiat-capitalism` (Feb 16, 2026)

### Chapter 3.1 Steps 1-5 — ALL COMPLETE

**Step 1 — Triage:**
- Source: `Fiat Capitalism.md` (~5,200 words) → 199 items across 18 themes, 22 links documented

**Step 2 — Scraping:**
- 13 links scraped (WebFetch + Playwright), 3 skipped → inventory expanded to 382 items

**Step 3 — Deep Research:**
- 15 gaps identified and filled (Gemini + Claude WebSearch) → 121 new items (#500-620), 18 bibliography sources (#23-40)
- Key finds: Polanyi, Piketty, Graeber, Fraser, Hickel (non-libertarian voices), 4 steel-manned counterarguments

**Step 4 — Argument Blocks (retrofitted to v2 March 2026):**
- 23 blocks built from 601 items, polemic sequence (escalating impact → kill shot)
- v2 retrofit: argument types, appeals, conclusions/transitions, cross-chapter refs, Bitcoin resolution, inline source text, chapter grid
- Eurodollar system gap filled (15 items, 6 sources)
- Austrian economics additions (30 items: malinvestment, capital consumption, demographics, pensions, risk asymmetry)
- Orphan registry: 5→3.2, 6→3.3, 1→3.4, 55→3.5, 20+→Ch5/Ch6

**Step 5 — User Review:**
- Farrington "Capital Strip Mine" added (23 items: #666-673, #691-705) — farmer vs strip miner, capital consumption, financialization doom loop, "killer app for Bitcoin: pricing capital"
- Austrian "recession as cure" argument added (17 items: #674-690) — Mises, Rothbard, Woods, Garrison
- 10 amendments written in Part 1.5 targeting blocks 3, 5, 6, 8, 11, 12, 13, 15, 17, 21
- 6 new bibliography sources (#47-52)
- Block sequence approved — no reorders, cuts, or merges
- **Final totals:** 705 inventory items, 47 sections, 52 bibliography sources

---

## References & Citations

**Format:** Chicago Manual of Style, 18th Edition, Notes-Bibliography system.

| Task | Status |
|------|--------|
| Define citation format | DONE |
| Build per-sub-chapter bibliographies | In progress (Ch 3.1 links.md — 52 sources, Ch 3.2 links.md — 28 sources) |
| Compile master bibliography | In progress — `bibliography.md` created with 66 sources from Ch3.1 + Ch3.2, updates at Steps 2 and 3 |
| Retroactively add citations to Ch1 and Ch2 | Pending (after Ch3-9) |
| Create References chapter/appendix | Pending (after all chapters) |

---

## Ch1 & Ch2 Surgical Edits (after Ch3-9 expansion)

- [ ] Review Ch1 with user — identify gaps, add new language where needed
- [ ] Review Ch2 with user — identify gaps, add new language where needed

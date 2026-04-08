# WBIGAF Pipeline Tracker

> **Last updated:** 2026-03-20
> **Active executors:** 0/3
> **Current wave:** Wave 1A COMPLETE. Next: spot-check, then Wave 1B (scrape) or Wave 2 (Ch3/Ch4 pull-forward)

## Pipeline Steps

| # | Step | Output | Human Gate? |
|---|------|--------|-------------|
| 1 | Triage | catalog.md + links.md | No |
| 2 | Scrape | sources.md, links.md updated | No (but fragile -- review after) |
| 3A | Research: Gap Analysis + Prompt | research.md Parts 1-2 | No |
| 3B | Research: User Runs Off-Platform | research.md Part 3 (pasted) | YES -- user action required |
| 3C | Research: Claude Supplements | research.md Part 3 supplement, catalog.md #500+ | No |
| 4 | Argument Map | catalog.md Part 1 (blocks) | No |
| 5 | User Review | catalog.md Part 1.5 (amendments) | YES -- user approval required |
| 6 | Web Publish | HTML blocks in guide .md file | No (but verify build) |

## Status Legend

| Status | Meaning |
|--------|---------|
| DONE | Step complete, output verified |
| ACTIVE | Executor currently working |
| READY | No blocker, awaiting executor |
| BLOCKED [H] | Waiting on human action |
| PENDING | Not yet started, future wave |

---

## Chapter 3: What Problems Does Bitcoin Solve?

| Sub-Ch | Title | Step | Status | Items | Blocks | Blocker | Next Action |
|--------|-------|------|--------|-------|--------|---------|-------------|
| 3.1 | Fiat Capitalism | 6 | DONE | 705 | 23 | -- | Deployed to website |
| 3.2 | Inflation & Cantillon Effect | 6 | DONE | ~200 | 17 | -- | Deployed to website (2026-03-20) |
| 3.3 | CBDCs Surveillance Censorship | 3B | BLOCKED | 120 | -- | [H] | User runs research prompt |
| 3.4 | Systematic Economic Risk | 3B | BLOCKED | 138 | -- | [H] | User runs research prompt |
| 3.5 | For the Billions | 3B | BLOCKED | 207 | -- | [H] | User runs research prompt |

## Chapter 4: Bitcoin Past

| Sub-Ch | Title | Step | Status | Items | Blocks | Blocker | Next Action |
|--------|-------|------|--------|-------|--------|---------|-------------|
| 4.1 | October 31st | 1 | DONE | 59 | -- | -- | Ready for Step 2 (scrape) |
| 4.2 | Who is Satoshi Nakamoto | 2 | DONE | 105 | -- | -- | Ready for Step 3A |
| 4.3 | Fair Launch January 3rd | 1 | DONE | 29 | -- | -- | Ready for Step 2 (scrape) |
| 4.4 | Cypherpunks and Digital Cash | 1 | DONE | 47 | -- | -- | Ready for Step 2 (scrape) |
| 4.5 | Struggles and Resilience | 1 | DONE | 74 | -- | -- | Ready for Step 2 (scrape) |

## Chapters 5-9 (Wave 1A Triage -- COMPLETE, pending spot-check)

**Wave 1A completed:** 2026-03-20. 5 background executors, all succeeded. Spot-check before advancing to Wave 1B.

| Chapter | Title | Sub-Ch | Items | Links | Status | Flags |
|---------|-------|--------|-------|-------|--------|-------|
| 5 | Bitcoin Properties | 21 | 522 | 55 | DONE (triage) | 5.14, 5.19 are stubs (1 item each). 5.16 richest (122 items). |
| 6 | So What is Bitcoin Exactly | 6 | 222 | 27 | DONE (triage) | 6.2 stub (9 items, 0 links). 6.6 thin (7 items). 6.3 largest (80 items). |
| 7 | Bitcoin Present | 7 | 198 | 47 | DONE (triage) | 7.7 has screenshot-only sources. Some t.co shortened URLs. |
| 8 | Why Bitcoin is Good as Fuck | 13 | 290 | 46 | DONE (triage) | 8.3 empty (0 bytes). 8.6 no links. 8.1 has pre-scraped Gladstein. |
| 9 | Bitcoin Future | 9 | 141 | 31 | DONE (triage) | 9.2, 9.3 stubs (2 items each). 9.8 no external sources. |

**Wave 1A totals:** 56 sub-chapters triaged, 1,373 catalog items, 206 links. Individual sub-chapter rows will be added after spot-check.

---

## Chapter 1: What Is Bitcoin? (Deferred -- after Ch3-9 expansion)

| Item | Status | Notes |
|------|--------|-------|
| Unpublished "What is Bitcoin?" draft | PENDING | `TBB/posts/2023/what-is-bitcoin.md` (~7,738 words, draft: true). Comprehensive "forget everything you know" piece with dozens of Bitcoin definitions. Never published -- only a condensed version went live as 1.11 "Other Bitcoin Definitions." Plan: integrate into Ch1 expansion. |

---

## Human Gates -- Current

### Step 3B: Research Prompts (3 pending)

| Sub-Ch | Prompt Location | Items | Gaps |
|--------|----------------|-------|------|
| 3.3 | `WBIGAF/3-what-problems-does-it-solve/3.3-cbdcs-surveillance-censorship-control/research.md` Part 2 | 120 | 13 |
| 3.4 | `WBIGAF/3-what-problems-does-it-solve/3.4-systematic-economic-risk/research.md` Part 2 | 138 | 13 |
| 3.5 | `WBIGAF/3-what-problems-does-it-solve/3.5-for-the-billions-not-the-billionaires/research.md` Part 2 | 207 | 13 |

Run each prompt through Gemini Deep Research / ChatGPT / Perplexity. Paste results back into the corresponding `research.md` Part 3. Say "[sub-chapter] research done" to unblock.

---

## Dispatch Rules (WBIGAF-Specific)

These rules supplement the generic `/coordinator dispatch` command with project-specific logic.

### Pull Strategy
1. **Closest to done first.** Select the sub-chapter at the highest pipeline step with READY status.
2. **Same chapter preferred.** When multiple sub-chapters are READY at the same step, prefer same-chapter to reduce context switching.
3. **WIP limit:** Max 3 active executors. Max 3 per chapter. Sub-chapters within a chapter can parallelize; cross-chapter parallelism is not used.
4. **Never dispatch past a human gate.** Steps 3B and 5 require user action. Mark BLOCKED [H] and surface in the Human Gates section.

### Wave Discipline
- **Wave 1A (Triage):** Ch5-9 only. Do not start until coordinator is validated with at least one dispatch.
- **Wave 1B (Scrape):** Chapter-by-chapter, with review after each chapter. Do not start a chapter's scrape until its triage is spot-checked.
- **Wave 2 (Steps 3-6):** Pull strategy applies. 3 parallel executors per chapter.

### Completion Protocol
When an executor finishes:
1. Update the file's metadata header: `Pipeline step: Step [N] -- COMPLETE`
2. Coordinator reads the metadata, updates this tracker (status, counts, next action)
3. If the next step is a human gate, add to the Human Gates section

### Handoff Brief Template

```
## Handoff Brief: [Sub-chapter] -- Step [N]

**Task:** [One sentence]
**Output:** [File(s) to create or update]
**Acceptance criteria:**
- [ ] [Criterion]

**Files to read (ONLY these):**
- [path] -- [why]

**Files to create/update:**
- [path] -- [what]

**Do NOT:**
- [Scope boundary]

**Completion marker:** Update [file] metadata: "Pipeline step: Step N -- COMPLETE"
```

### Step-Specific Executor Instructions

| Step | Model | Key Instructions |
|------|-------|-----------------|
| 1 (Triage) | Sonnet | Read source file. Create sub-chapter dir. Generate catalog.md (raw inventory, one item per line) + links.md. Check orphan registry. |
| 2 (Scrape) | Sonnet | WebFetch all links. Playwright for failures. Update links.md status. Append to sources.md. New catalog items #200+. |
| 3A (Gap Analysis) | Opus | Read catalog + source. Classify coverage. Write research.md Parts 1-2. |
| 3C (Supplement) | Sonnet | Process user's pasted research. Extract catalog items #500+. WebSearch to fill remaining gaps. |
| 4 (Argument Map) | Opus | Build blocks from inventory. Refutation Analysis. Chapter Grid. Sequence for polemic impact. Read argument-block-model.md. |
| 5 (User Review) | -- | Not delegated. Happens in main conversation with user. |
| 6 (Web Publish) | Sonnet | Generate HTML block sections matching Ch3.1 format. Verify with `npm run build`. |

# WBIGAF.md — Book Project Operating Manual

> **Session start:** Read this file first. Then read `WBIGAF-Status.md` for current progress.

---

## 1. What Is This Project

**"Why Bitcoin Is Good As Fuck" (WBIGAF)** — a 100,000-150,000 word book explaining why Bitcoin matters.

- **Format:** Long-form non-fiction book with Chicago-style endnotes
- **Scope:** 9 chapters, 67 sub-chapters (each WBIGAF source file = one sub-chapter)
- **Source material:** 83 research note files in `WBIGAF/1-9.*/` directories
- **Output:** Polished sub-chapter drafts (`draft.md`) in each sub-chapter's directory
- **Voice:** Written in the author's voice — see Voice DNA profile before drafting
- **Progress tracking:** `WBIGAF-Status.md` (this directory)

### What Claude Does Here
- Triage source files (catalog arguments, document links)
- Scrape and extract content from links
- Organize argument maps for user review
- Draft sub-chapters using Voice DNA profile
- Maintain citations (Chicago 18th ed.)
- Track progress in WBIGAF-Status.md and chapter transition docs

### What Claude Does NOT Do Here
- Provide financial advice or investment recommendations
- Fabricate arguments not found in sources (content lock)
- Inject opinions not in source material (belief leakage prevention)
- Modify original WBIGAF source files (read-only)
- Work on the website (that's `CLAUDE.md` at repo root)

---

## 2. Architecture

```
WBIGAF/
├── WBIGAF.md                          ← THIS FILE (read first)
├── WBIGAF-Status.md                   ← Progress overview (read second)
├── TRACKER.md                         ← Pipeline state tracker (coordinator reads this)
├── toc.md                             ← Table of contents (all chapters, sub-chapters, block titles)
├── bibliography.md                    ← Master bibliography (de-duplicated Chicago citations)
├── glossary.md                        ← Glossary of terms (back-burner, populate during drafting)
│
├── 0. Project/                        ← Project-level docs
│   ├── Voice DNA/                     ← Author's voice profile + working files
│   │   ├── voice-dna-profile.md       ← THE profile (761 lines — load during drafting)
│   │   ├── voice-dna-framework.md     ← Condensed L1-L7 framework
│   │   ├── voice-validation-test.md   ← Test passages + scores
│   │   ├── Voice DNA Forensic...md    ← Source methodology (~37,700 words)
│   │   ├── methodology-insights.md    ← Section-by-section assessment
│   │   └── batch-1/2/3-observations.md ← Corpus analysis working files
│   └── Planning/                      ← Original project planning docs
│       ├── Why Bitcoin is good as fuck.md  ← Master overview/outline
│       └── Book.md, Structure.md, etc.     ← Early planning docs
│
├── 1. What is bitcoin/               ← Ch1 source files (2 files)
├── 2. Why bitcoin/                   ← Ch2 source files (6 files)
├── 3. What Problems Does it solve/   ← Ch3 (reorganized into sub-chapter dirs)
│   ├── Chapter 3 Metadata/
│   │   ├── 3. What Problems Does it solve.md  ← Overview/intro source
│   │   ├── ch3-triage.md                       ← Original triage (reference)
│   │   ├── transition-ch3.md                   ← Chapter progress snapshot
│   │   └── orphans.md                          ← Cross-sub-chapter orphan registry
│   ├── 3.1 Fiat Capitalism/
│   │   ├── Fiat Capitalism.md        ← Source (read-only, never modified)
│   │   ├── catalog.md                ← Pipeline: 199 inventory items (Argument Blocks added at Step 4)
│   │   ├── links.md                  ← Pipeline: 22 links documented
│   │   ├── sources.md                ← Pipeline: scraped content (created during scraping)
│   │   ├── research.md               ← Pipeline: (created during deep research)
│   │   └── draft.md                  ← Pipeline: (created during drafting)
│   ├── 3.2 Inflation and the Cantillon Effect/
│   ├── 3.3 CBDCs Surveillance Censorship Control/
│   ├── 3.4 Systematic Economic Risk/
│   └── 3.5 For the Billions Not the Billionaires/
├── 4. Bitcoin Past/                   ← Flat source files (reorganize when pipeline starts)
├── 5. Bitcoin properties/
├── 6. So…what is bitcoin exactly/
├── 7. Bitcoin Present/
├── 8. Why bitcoin is good as fuck/
└── 9. Bitcoin Future/
```

### Per-Sub-Chapter File Structure

When the pipeline starts for a sub-chapter, its directory gets up to 5 working files alongside the source:

```
[N.M sub-chapter name]/
├── [Source File].md    ← Original WBIGAF source (READ-ONLY — never modify)
├── catalog.md          ← Source Inventory (raw items) → Argument Blocks added at Step 4
├── links.md            ← Link registry + scrape status + Chicago citations + bibliography
├── sources.md          ← Full extracted content from scraped links (created at Step 2)
├── research.md         ← Deep research additions (created at Step 3)
└── draft.md            ← Final written sub-chapter text (created at Step 6)
```

---

## 3. Author's Voice

**Do NOT write content without loading the Voice DNA profile first.**

Profile: `WBIGAF/0. Project/Voice DNA/voice-dna-profile.md` (761 lines, 8 sections)

Quick summary (the profile contains the full rules):
- **Tone:** Passionate educator with urgency. Emotionally invested, never detached.
- **Register:** Oscillates between conversational casual and poetic/prophetic.
- **Persona:** Self-taught Bitcoin convert. Obsessive autodidact. Trail guide, not professor.
- **Devices:** Extended analogies, one-sentence drops, parallel chains, steelmanning.
- **Grammar:** Ellipses (signature mark), sentence fragments, run-ons for momentum.
- **Taboos:** AI-tells (delve, tapestry, landscape, etc.), corporate buzzwords, detached tone.
- **Anti-caricature:** Max 2-3 voice features per paragraph. Distribute naturally.

The profile contains: Voice DNA Card, Constitution (63 rules with signal rankings), Taboo List, Rhetorical Move Library, Mode Feature Deltas, Negative Stylometry, Generation Workflow, Evaluation Rubric (22 items).

---

## 4. The Pipeline (Per Sub-Chapter)

Every sub-chapter goes through these 7 steps IN ORDER. One sub-chapter at a time. Do not skip steps. Do not work on multiple sub-chapters in parallel.

### Step 1: TRIAGE
Read the source file. Create a **Source Inventory** — every distinct claim, quote, data point, bullet, and observation gets its own numbered line item (no consolidation — be granular). This is a raw capture, not argument architecture. List every link with its type (article, YouTube, podcast, tweet, Reddit, PDF). Note which links have content already extracted vs. which are just URLs.

- Create sub-chapter directory if not exists
- Move source file into directory if not already there
- **Check the orphan registry** (`Chapter N Metadata/orphans.md`) for items routed to this sub-chapter from earlier sub-chapters — import them into the catalog
- **Output:** `catalog.md` (Source Inventory) + `links.md`

### Step 2: SCRAPE
Scrape all links that lack full extracted content:
- Web articles → WebFetch
- YouTube videos → `youtube-transcript-api` (Python)
- Podcasts → check YouTube first, then original article, then Spotify transcript extension
- Reddit/Tweets → WebFetch
- Append full extracted content to `sources.md` (one section per link, keyed by link #)
- Update link status in `links.md` registry (PENDING → DONE/PARTIAL/FAILED)
- Update `catalog.md` with new arguments found during scraping (numbering from #200+)
- Every link gets a Chicago citation in `links.md` — even ones not scraped
- Every SKIPPED or FAILED link gets a documented reason in `links.md`
- Update `bibliography.md` with any new sources added to `links.md`

### Step 3: DEEP RESEARCH
Identify gaps in the inventory and find new material. Two-part process:

**Part A — Claude generates the prompt:**
1. Read `catalog.md` and the source file to understand current coverage
2. Analyze what's well-covered vs. thin/missing (gap analysis)
3. Generate a research prompt in `research.md` with two sections:
   - **Section A:** Specific identified gaps (themes mentioned in source notes but undeveloped)
   - **Section B:** Open discovery — free reign for the research tool to find novel arguments, thinkers, data, historical examples, counterarguments, and angles not identified in the gap analysis
4. The prompt should list what's already covered (so the research tool doesn't waste time) and what sources have already been used
5. Stay within the sub-chapter's scope (per Scope Control rules)

**Part B — User runs the prompt off-platform:**
- Copy prompt from `research.md` into Gemini Deep Research, ChatGPT Deep Research, or Perplexity Pro
- Paste results back into `research.md` Part 3
- Claude supplements via WebSearch if needed (Part 3 supplement)
- Extract new catalog items from research results → `catalog.md` numbered from #500+
- Update `links.md` bibliography with new sources

**Full methodology:** See Section 10 (Deep Research Playbook) for detailed process.
- Update `bibliography.md` with new sources from research results
- **Output:** `research.md` (gap analysis + prompt + results + new items)

### Step 4: ARGUMENT MAP
Build **Argument Blocks** from the Source Inventory. Each block = one thesis with its logic chain, key quotes, evidence, rhetorical moves, and source refs. Sequence blocks for **escalating persuasive impact** (polemic structure, not taxonomy).

- **Threshold:** If inventory exceeds 30 items → formal Argument Blocks required. Under 30 → organize directly with a simple outline.
- **Run Refutation Analysis** early in this step — scan each thesis for counter-mainstream claims, identify strongest objections, determine which blocks (if any) need the REFUTATION field and what placement (Upfront/Inline/Deferred). Most sub-chapters flag 0 blocks. See argument-block-model.md Section 3.3.
- Restructure `catalog.md` into Part 1 (Argument Blocks) + Part 2 (Source Inventory)
- Flag orphan inventory items (don't fit any block — may be cuttable or belong in another sub-chapter)
- **Route orphans to the orphan registry** (`Chapter N Metadata/orphans.md`) — each orphan gets: item #, text, source sub-chapter, destination sub-chapter, and the source link/citation it came from
- Flag cross-sub-chapter duplicates
- Present blocks to user in proposed sequence
- Update `toc.md` with the sub-chapter's block titles from the Chapter Grid
- **Full model spec:** `WBIGAF/0. Project/Planning/argument-block-model.md` (v2.2)
- **Architectural decisions:** `WBIGAF/0. Project/Planning/decisions.md`

### Step 5: USER REVIEW
User reviews the Argument Blocks:
- Reorder blocks for narrative momentum
- Cut blocks that belong in another sub-chapter
- Merge blocks that are really one argument
- Flag blocks that need more evidence
- Add color, quotes, personal anecdotes, or last-minute research
- Approve the structural sequence

**Amendments system (Part 1.5 of catalog.md):**
All Step 5 changes go into the Amendments section — never edit existing blocks directly.
- `+Block N` — add material (quote, evidence, logic point) to existing block
- `+Block N.1` — new standalone block that drafts after Block N
- `+Block N: cut` / `+Block N: merge into M` — structural changes
- New inventory items continue sequential numbering in Part 2
- At draft time (Step 6), amendments merge into their target blocks
- This keeps all block numbers and inventory references stable throughout review
- If blocks were reordered, cut, merged, or added, update `toc.md` to match

### Step 6: DRAFT
Write using Voice DNA profile — each Argument Block becomes one section of the draft:
- **Load `WBIGAF/0. Project/Voice DNA/voice-dna-profile.md` before writing**
- Block thesis → section topic sentence; logic chain → paragraph structure; key quotes pre-selected
- Chicago-style endnotes for every claim, quote, and data point
- No padding — length driven by argument depth
- Add any newly defined terms to `glossary.md`
- Sequence for escalating impact, not taxonomy
- V4 effects applied where appropriate
- **Output:** `draft.md`

### Step 7: REVIEW
User reviews:
- Surgical edits, voice adjustments
- Verify no arguments lost, no content fabricated
- When approved → move to next sub-chapter

---

## 5. Conventions

### Citations
**Chicago Manual of Style, 18th Edition, Notes-Bibliography system.**

| Source Type | Format |
|-------------|--------|
| Book | Last, First. *Title*. Publisher, Year. |
| Article | Last, First. "Title." *Publication*, Date. URL. |
| Blog | Last, First. "Title." *Blog Name*, Date. URL. |
| Tweet | First Last (@handle), "Text...," Twitter/X, Date, URL. (notes only) |
| YouTube | Speaker/Channel. "Title." YouTube video. Date. URL. |
| Podcast | Host. "Episode Title." *Podcast Name*. Episode #. Date. URL. |
| Reddit | u/username, "Title," Reddit, r/subreddit, Date, URL. (notes only) |

### Link Documentation Rules
- Every link in the source file gets a row in the Link Registry — no exceptions
- Each link gets a Chicago citation even before scraping
- Scrape Status: PENDING, DONE, SKIPPED, FAILED, or PARTIAL
- Every SKIPPED or FAILED link must have a documented reason
- Partial scrapes (truncated, paywall) = PARTIAL status with notes

### Source Files
- Original WBIGAF source `.md` files are **NEVER modified**
- They stay in their sub-chapter directory as the read-only reference
- Pipeline files (catalog, links, research, draft) are created alongside them

### Chapter Reorganization
When the pipeline starts for a new chapter:
1. Create numbered sub-chapter directories (`N.M Sub-Chapter Name/`)
2. Move each source file into its sub-chapter directory
3. Create `Chapter N Metadata/` for chapter-level docs (overview source, triage, transition)

### Transition Documents
One per chapter, in `Chapter N Metadata/transition-chN.md`. Tracks:
- Current sub-chapter and pipeline step
- Files to read for context
- What's done, what's next
- Updated at context window boundaries

### Sub-Chapter Scope Control
**The original source file defines the scope of each sub-chapter.** Arguments collected during scraping and research often span multiple sub-chapters. The rules:

1. **Scraping casts a wide net** — it's fine to capture everything from a scraped article, even arguments that belong in other sub-chapters. This prevents losing material.
2. **The catalog is a raw inventory** — it holds everything found, tagged by source. No scope filtering happens here.
3. **Step 4 (Argument Map) is where scope gets enforced.** When building Argument Blocks, only include items that fit the sub-chapter's thesis as defined by the source file. Flag items that belong elsewhere as cross-sub-chapter orphans (note which sub-chapter they should go to).
4. **Gray areas:** Use best judgment. If an argument supports the sub-chapter's core thesis even tangentially, it can stay. If it's clearly the primary concern of another sub-chapter, flag it as an orphan.
5. **Deep Research (Step 3) should focus on the sub-chapter's specific scope** — don't research tangential topics that belong in other sub-chapters.

**Example for Chapter 3:**
- 3.1 **Fiat Capitalism** — structural critique of fiat money system (central banking, debt slavery, broken cost of capital, unsound money, weaponized reserves, Bitcoin as opt-out)
- 3.2 **Inflation & Cantillon Effect** — inflation mechanics, who benefits from money printing, purchasing power erosion
- 3.3 **CBDCs, Surveillance, Censorship** — financial surveillance, control, programmable money
- 3.4 **Systematic Economic Risk** — systemic fragility, cascading bailouts, moral hazard
- 3.5 **For the Billions** — IMF/World Bank exploitation, global south, debt colonialism, financial inclusion

Items scraped from Gladstein's IMF article that are detailed case studies of country-level exploitation → mostly 3.5, not 3.1. Items about inflation as invisible tax → mostly 3.2, not 3.1. The sub-chapter's source notes are the authoritative scope definition.

### Orphan Registry
One file per chapter: `Chapter N Metadata/orphans.md`. Tracks catalog items that were found in one sub-chapter's scraping/research but belong in a different sub-chapter.

**Format:**
```markdown
## Orphans routed to 3.2 (Inflation & Cantillon Effect)
| Item # | From | Text | Source |
|--------|------|------|--------|
| 370 | 3.1 | "Inflation as invisible tax..." | Boyapati, Link #18 |

## Orphans routed to 3.5 (For the Billions)
| Item # | From | Text | Source |
|--------|------|------|--------|
| 413 | 3.1 | "Marcos took Philippine debt..." | Gladstein, Link #14 |
```

**Lifecycle:**
1. **Created at Step 4** of the first sub-chapter that generates orphans
2. **Appended** as each subsequent sub-chapter routes more orphans
3. **Consumed at Step 1** of the destination sub-chapter — orphan items get imported into that sub-chapter's catalog (renumbered to fit)
4. **Marked as consumed** in the registry (don't delete — keep the paper trail)
5. Items that have been consumed by their destination sub-chapter get marked: `[CONSUMED by 3.5]`

**Why this works:**
- Nothing gets lost between sub-chapters
- Each sub-chapter starts by checking for incoming orphans
- The registry lives at chapter level so it's visible across all sub-chapters
- Source attribution travels with the orphan (you always know where it came from and which link/citation it references)

### Bitcoin Terminology
- **Bitcoin** (capital B) = the network, protocol, system
- **bitcoin** (lowercase b) = the unit of currency (BTC)

---

## 6. How to Resume a Book Session

1. **Read this file** (`WBIGAF/WBIGAF.md`) — understand the project and pipeline
2. **Read `WBIGAF/WBIGAF-Status.md`** — find the current chapter and pipeline step
3. **Read the chapter's transition doc** (e.g., `WBIGAF/3.../Chapter 3 Metadata/transition-ch3.md`) — get detailed context
4. **Load ONLY the files needed for the current pipeline step:**
   - Triage → source file only
   - Scraping → `links.md` + `catalog.md` (scraped content goes to `sources.md`)
   - Deep Research → `catalog.md` + `research.md`
   - Argument Map → `catalog.md` + `sources.md` + `research.md`
   - Drafting → `catalog.md` + `sources.md` + `voice-dna-profile.md`
   - Review → `draft.md`
5. **Do NOT load Voice DNA files until Step 6 (Drafting)** — they are large and not needed earlier

---

## 7. Key Files

| Need | File |
|------|------|
| Book project context | `WBIGAF/WBIGAF.md` (this file) |
| Progress overview | `WBIGAF/WBIGAF-Status.md` |
| Pipeline tracker | `WBIGAF/TRACKER.md` (coordinator reads this for dispatch) |
| Table of contents | `WBIGAF/toc.md` |
| Master bibliography | `WBIGAF/bibliography.md` |
| Glossary | `WBIGAF/glossary.md` |
| Voice DNA profile | `WBIGAF/0. Project/Voice DNA/voice-dna-profile.md` |
| Voice DNA framework | `WBIGAF/0. Project/Voice DNA/voice-dna-framework.md` |
| Source methodology | `WBIGAF/0. Project/Voice DNA/Voice DNA Forensic Stylometry and Production System.md` |
| Argument block model | `WBIGAF/0. Project/Planning/argument-block-model.md` |
| Architectural decisions | `WBIGAF/0. Project/Planning/decisions.md` |
| Master book outline | `WBIGAF/0. Project/Planning/Why Bitcoin is good as fuck.md` |
| Ch3 transition doc | `WBIGAF/3. What Problems Does it solve/Chapter 3 Metadata/transition-ch3.md` |
| Website project | `CLAUDE.md` (repo root) |
| Website tasks | `tasks/TODO.md` |

---

## 8. Relationship to Website

This book project is **separate from the website** (thebitcoinbreakdown.com).

- The website has its own operating manual: `CLAUDE.md` at the repo root
- The website has its own task list: `tasks/TODO.md` (Phases 1-8)
- The published guide at `/guide/` on the website contains earlier, shorter versions of these chapters (~31,600 words total)
- Eventually, the expanded book content will replace the existing guide chapters on the website
- **For now, treat them as independent projects** — book work stays in `WBIGAF/`, website work uses `CLAUDE.md`

---

## 9. Scraping Playbook (Lessons from Ch3.1)

### Multi-Round Strategy
Scraping works best in rounds, escalating tools as needed:

1. **Round 1 — WebFetch:** Try all links with the built-in WebFetch tool first. This handles most standard articles, blogs, and news sites. Expect ~50-70% success rate.
2. **Round 2 — Playwright:** For links that fail (JS-rendered SPAs, 403 Forbidden, domain blocks), use Playwright browser automation. This handles JavaScript rendering and bypasses most blocks.
3. **Round 3 — Wayback Machine:** For domains that block all scraping (e.g., Forbes), use Playwright to navigate to `web.archive.org/web/[URL]` and extract the cached version.
4. **Manual paste:** For paywalled content (WSJ, etc.), the user pastes the content directly.

### Playwright Setup
The Playwright MCP server can be added via:
```
claude mcp add playwright -- npx @playwright/mcp@latest --headless
```
**However**, MCP tools may not appear in the current session after installation — a Claude Code restart may be required. If MCP tools aren't available, fall back to running Playwright directly via Node.js scripts:

```bash
cd "c:\Users\GC\Documents\TBB"
npm install playwright
npx playwright install chromium
```

Then create a `.mjs` script:
```javascript
import { chromium } from 'playwright';
const browser = await chromium.launch({ headless: false }); // or true
const page = await browser.newPage();
await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });
const text = await page.evaluate(() => document.body.innerText);
// Write to scraped_N.txt
await browser.close();
```

### Site-Specific Issues (Known)

| Site | Problem | Solution |
|------|---------|----------|
| Bitcoin Magazine | JS SPA — WebFetch returns only CSS/metadata | Playwright headless works |
| Forbes | Blocks all scraping (headless + non-headless) | Wayback Machine via Playwright |
| Medium | 403 Forbidden in headless mode | Playwright non-headless (`headless: false`) |
| Lyn Alden (lynalden.com) | 403 in headless mode | Playwright non-headless |
| WSJ / paywalled sites | Paywall blocks content | User manual paste |

### Headless vs Non-Headless
- **Headless (default):** Faster, no visible browser window. Works for most sites.
- **Non-headless:** Shows browser window, less likely to be bot-detected. Required for sites that check for headless Chrome (Medium, Lyn Alden). Use `headless: false` and add scrolling + `domcontentloaded` wait.

### File Organization After Scraping
- **Scraped text files** (`scraped_N.txt`): Store in the sub-chapter directory (e.g., `3.1 Fiat Capitalism/`), NOT in the TBB root.
- **Small-medium articles** (<5k words): Store full text directly in `sources.md`.
- **Large articles** (>5k words): Store key excerpts + direct quotes in `sources.md`, full text in separate `scraped_N.txt` file. Reference the file from sources.md.
- **Temp files to clean up:** Scrape scripts (`.mjs`), `package.json`, `package-lock.json`, `node_modules/` in TBB root — delete after all scraping is done.

### Using Background Agents for Catalog Extraction
After scraping large articles, use Task tool agents to extract catalog items in parallel:

**Prompt pattern:**
```
Read [scraped file path]. Extract every distinct claim, argument, data point,
and quotable passage relevant to [sub-chapter topic]. Format as numbered
catalog items starting at #[N]. One item per line. Include direct quotes
where the language is powerful. Tag each item with (Author).
```

**Key findings:**
- Agents extract significantly more items than manual scanning (Gladstein: 59 items vs 29 manual; Boyapati: 35 vs 23)
- Run agents in parallel for multiple articles — they work independently
- Agent outputs may sometimes be empty due to context issues — always check the output file before marking complete
- After agents finish, review their output against what you already extracted and add genuinely new items
- Use `subagent_type: "general-purpose"` for extraction tasks

### Catalog Numbering Convention
- **#1-199:** From original source notes (Step 1 Triage)
- **#200-299:** From first-pass scraping (WebFetch)
- **#300+:** From second-pass scraping (Playwright), grouped by link number with gaps between sources (e.g., #300-308 for link #12, #320-348 for link #14, etc.)
- **#400+:** Extended extractions from background agents
- Gaps in numbering are fine — the argument block step (Step 4) will reorganize everything
- Don't renumber existing items when adding new ones

### What Worked Well
- WebFetch → Playwright → Wayback Machine escalation covered all 13 scrapable links with zero permanent failures
- Background agents for catalog extraction from long articles saved time and caught items manual scanning missed
- Separating `sources.md` (full text) from `links.md` (metadata/bibliography) from `catalog.md` (inventory items) kept each file focused and manageable
- Moving scraped files to sub-chapter directory after scraping kept the repo clean

### What to Improve Next Time
- Install Playwright MCP server AND restart Claude Code before the scraping session so MCP tools are available
- Launch catalog extraction agents immediately after scraping each article (don't wait until all scraping is done)
- For very large articles (>20k words like Gladstein), always use an agent for extraction — manual scanning misses too much

---

## 10. Deep Research Playbook (Lessons from Ch3.1)

### Purpose
Step 3 (Deep Research) ensures no stone is left unturned before building Argument Blocks. It bridges the gap between "what we scraped" and "what the chapter needs." The output is a comprehensive research prompt that gets run through off-platform AI research tools (Gemini Deep Research, ChatGPT Deep Research, Perplexity Pro) plus any supplementary WebSearch Claude can do directly.

### Process (Claude's Role)

**1. Read the inventory and source file:**
- Read `catalog.md` (full inventory) and the original source file (scope definition)
- Read `links.md` to know which sources have already been tapped

**2. Classify coverage:**
- **Well-covered:** Themes with strong multi-source coverage, quotable material, and specific data. These don't need more research.
- **Thin/missing:** Themes mentioned in the source notes (even as a single bullet point) that were never developed with data, quotes, or depth. These are the identified gaps.

**3. Write the gap analysis** (Part 1 of `research.md`):
- Table of well-covered themes (with catalog section refs and key sources)
- Numbered list of gaps, grouped by priority:
  - **Priority 1:** Major gaps — mentioned in source notes but never developed
  - **Priority 2:** Theoretical depth — present but thin, needs more substance
  - **Priority 3:** Data and examples — existing arguments that need concrete numbers, quotes, or case studies

**4. Write the research prompt** (Part 2 of `research.md`):

Structure the prompt for how deep research tools actually work — clear context upfront, then the task, then output guidance. Four sections:

1. **CONTEXT** — What the chapter is about, scope boundaries (in/out), what's already well-covered, which authors/sources are already used. This is the briefing — give the tool everything it needs to avoid wasting time on what we already have.

2. **THE GAPS** — Concise descriptions of each identified gap. Keep these tight — a sentence or two each with key terms the tool can search on. Don't over-specify the format of the response; each gap needs different treatment (some need data, some need a quote, some need a historical example). Let the tool match depth to what the material warrants.

3. **OPEN DISCOVERY** — This is critical and must be a first-class section, not an afterthought. The identified gaps represent what we *know* we're missing. The best research finds things we didn't know to look for. Direct the tool to:
   - Find thinkers and authors not already in our sources (especially non-libertarian voices)
   - Discover novel angles from unexpected ideological directions
   - Steel-man the strongest counterarguments with rebuttals
   - Find specific historical case studies
   - Surface devastating data and visualizations
   - Catch anything else that strengthens the chapter

4. **OUTPUT GUIDANCE** — Light touch, covering both format and substance:
   - **Format:** Detailed document with headings — one section per gap, open discovery as its own substantial standalone block (not afterthoughts tacked onto gap sections). This structure lets Claude extract catalog items cleanly, one section at a time.
   - **Depth:** Don't pad sections to fill space. If a gap only needs two data points and a quote, that's a short section. If another gap needs two pages, let it run. Match length to what the material warrants.
   - **Substance:** Lead with strongest material. Include quotes with attribution and numbers with sources. Connect to Bitcoin where natural, don't force it. Prioritize non-crypto sources for economic claims. Flag cross-chapter material.

### Process (User's Role)

**6. User runs the prompt off-platform:**
- Copy the full prompt from `research.md` Part 2
- Paste into Gemini Deep Research, ChatGPT, Perplexity Pro, or similar
- Paste results back into `research.md` (or provide them in chat)

**7. Claude processes the results:**
- Extract new catalog items from the research output → numbered from #500+ in `catalog.md`
- Add new sources to `links.md` bibliography
- Claude can supplement with WebSearch for specific data points the off-platform tool missed
- Flag any items that belong in other sub-chapters as potential orphans (final routing happens at Step 4)

### Key Principles

- **The prompt is not a checklist** — Section B (open discovery) is just as important as Section A (identified gaps). The best material often comes from unexpected directions.
- **Non-obvious sources carry rhetorical weight** — A leftist economist making the same critique as an Austrian economist is more persuasive than two Austrians agreeing. Seek voices from outside the typical Bitcoin/libertarian canon.
- **Counterarguments make the chapter stronger** — Understanding the best defenses of fiat capitalism lets us address them honestly rather than straw-manning.
- **Scope stays focused** — Research should stay within the sub-chapter's thesis. If the research tool returns material that clearly belongs in another sub-chapter, flag it but don't expand on it. The orphan registry handles cross-chapter routing.
- **Verifiability matters** — Prefer data points from government sources, academic papers, and mainstream journalism. Crypto-native sources are fine for Bitcoin-specific arguments but not for economic data claims.

### Catalog Numbering for Research Items
- **#500+:** Items from deep research (off-platform results + WebSearch)
- Continue the convention of gaps between sources
- Tag each item with its source for traceability

### research.md Structure
```
Part 1: Gap Analysis (scope, well-covered table, gap list by priority)
Part 2: Deep Research Prompt (context → gaps → open discovery → output guidance)
Part 3: Claude WebSearch Supplement (filled in after off-platform results)
Part 4: New Inventory Items (#500+, one per line, tagged with source)
```

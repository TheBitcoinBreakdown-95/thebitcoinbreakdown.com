# The Bitcoin Breakdown - Website Implementation Tasks

> This file tracks **website** tasks only (Phases 1-8). For **WBIGAF book** progress, see [`WBIGAF/WBIGAF-Status.md`](../WBIGAF/WBIGAF-Status.md).

## Quick Start (Resume)
```bash
cd c:\Users\GC\Documents\TBB\astro
npm run dev
```
Open http://localhost:4321 - See [CLAUDE.md](../CLAUDE.md) for full context.

---

## Phase 1: Git & Folder Setup
- [x] Initialize Git repo at `c:\Users\GC\Documents\TBB`
- [x] Create folder structure in vault (`posts/`, `pages/`, `drafts/`, `assets/`, `templates/`)
- [x] Create `.gitignore`
- [x] Create GitHub repository (public) → `TheBitcoinBreakdown-95/thebitcoinbreakdown.com`
- [x] Push initial commit

## Phase 2: Astro Project
- [x] Initialize Astro project in `astro/` subfolder
- [x] Configure `astro.config.mjs` with site URL
- [x] Create content collection config (`content.config.ts`)
- [x] Build layouts: BaseLayout, BlogPost, Page
- [x] Build pages: index, blog listing, dynamic post pages, RSS, sitemap
- [x] Build components: Header, Footer, Navigation, PostCard, SEO
- [x] Add basic styling
- [x] Experiment with theme/design (edit `astro/src/styles/global.css`)

## Phase 2b: V4 "Dark Luxury" Design System
Design guide: `TBB/Website planning/V4/tbb-master-design-guide.md`

### Step 1: Foundation (CSS + Fonts + Base Layout)
- [x] Rewrite `global.css` with V4 design tokens (gold/black palette, Cormorant Garamond + JetBrains Mono)
- [x] Update `BaseLayout.astro` (font imports, canvas elements, skip link, scroll progress, data ticker, global JS)

### Step 2: Components
- [x] Rewrite `Header.astro` (gold wordmark logo, nav sparks, responsive variants)
- [x] Rewrite `Footer.astro` (minimal centered, V4 style)
- [x] Rewrite `PostCard.astro` (laser trace border, title scramble, hash watermarks)
- [x] Rewrite `PostMeta.astro` (12px uppercase article meta)
- [x] Create `Divider.astro` (decrypting divider with sparks)
- [x] Create `ScrollProgress.astro`
- [x] Create `DataTicker.astro` (bottom ticker bar)
- [x] Create `PullQuote.astro` (compile effect)
- [x] Create `Terminal.astro` (terminal console block)

### Step 3: Pages
- [x] Rewrite `index.astro` (full-height hero, glitch text, dual CTAs, scroll indicator)
- [x] Update `blog/index.astro` (V4 card grid)
- [x] Update `about.astro` (V4 prose styles)
- [x] Create `404.astro` ("Block Not Found" page)
- [x] Rewrite `BlogPost.astro` layout (V4 prose, article meta, TOC, tags, hash decorations)

### Step 4: Interactive Effects (JS)
- [x] Create `interactions.js` (matrix rain, lightning transitions, glitch text, card scramble, typing headers, count-up stats, scroll reveals, divider decrypt/spark, encryption bars, static discharge, nav sparks, logo easter egg, pull quote compile, footnote flash, crosshair cursor)
- [x] Ensure all effects respect `prefers-reduced-motion`

### Step 5: Polish
- [x] Update favicon (gold ₿ on black) → `astro/public/favicon.svg`
- [x] Test responsive (mobile/tablet/desktop) — audit complete, one issue: no mobile nav at ≤768px
- [x] Test print stylesheet — comprehensive, covers all decorative elements
- [x] Verify build succeeds (5 pages, 2.74s, clean)
- [x] Add mobile navigation menu (hamburger/drawer for ≤768px)

## Phase 3: WordPress Migration
- [x] Recover WordPress admin access
- [x] Export content via Tools > Export > All content (saved to TBB/)
- [x] Write custom conversion script (`scripts/convert-wordpress.js`) using Turndown
- [x] Convert 28 posts + 5 pages from WordPress XML → Markdown with frontmatter
- [x] Remove placeholder welcome post
- [x] Verify all content renders correctly (32 pages built, clean)
- [x] Fix image paths (images localized to `astro/public/images/`)

## Phase 2c: Homepage Redesign + Content Enhancement
- [x] Redesign homepage: owl hero image, "Start Here" section, featured quote, resources teaser
- [x] Add lazy loading for all markdown images (custom rehype plugin)
- [x] Add image sizing CSS utilities (.img-small, .img-medium, .img-half)
- [x] Add prose image treatment (grayscale + gold overlay, full color on hover)
- [x] Install Obsidian callout boxes (`@r4ai/remark-callout` + 13 callout types styled)
- [x] Add image caption support (auto `<figure>`/`<figcaption>` from alt text)
- [x] Add reading time calculation to all blog posts
- [x] Add next/previous post navigation for series posts
- [x] Add series progress bar (encrypt-bar style)
- [x] Add auto table of contents for posts with 3+ headings

## Phase 4: GitHub Actions + Hostinger FTP Deploy
- [x] Get Hostinger FTP credentials from hPanel
- [x] Add FTP credentials as GitHub repository secrets
- [x] Create GitHub Actions workflow file (`.github/workflows/deploy.yml`)
- [x] Backup existing WordPress files on Hostinger
- [x] Test deployment — pushed to GitHub, Actions workflow triggered

## Phase 5: Obsidian Workflow
- [x] Set up Git credentials on Windows
- [x] Create blog post template in `TBB/templates/blog-post.md`
- [ ] Test full workflow: edit → commit/push → auto-deploy

## Phase 2d: UX Polish (Round 1) — DONE
- [x] Fix 1: Header nav — Blog, Learn More, About only
- [x] Fix 2: Logo glitch — 1s trigger, dramatic animation (skew, RGB split, brightness)
- [x] Fix 3: Homepage — 9-section interactive showcase (owl hero, terminal, stats, cards, quote, callout, articles, resources, glitch closer)
- [x] Fix 4: "What is Bitcoin?" CTA → `/blog/2023/intro`
- [x] Fix 5: TOC inside article column (720px)
- [x] Fix 6: Images max-width 560px, centered
- [x] Fix 7: Font weight 300 → 400 (body + prose)

## Phase 2e: UX Polish (Round 2) — DONE
- [x] Fix 8: TOC scroll offset — `scroll-margin-top: 80px` on headings
- [x] Fix 9: Series progress bar — animate to correct % (was always 100%)
- [x] Fix 10: Owl hero — higher position, buttons below owl, removed placeholder text
- [x] Fix 11: Header always shows full name (never "TBB")
- [x] Fix 12: Blog post content scroll reveal animations
- [x] Fix 13: Learn More page — all 40+ real resources from WordPress
- [x] Fix 14: About page — verified rendering (builds clean)

## Phase 2f: UX Polish (Round 3) — DONE
- [x] Fix 15: Homepage hero restructure — merged sections 1+2, "THE BITCOIN BREAKDOWN" is now the headline, buttons centered in viewport
- [x] Fix 16: Scroll-margin-top increased from 80px → 140px (headings fully visible after TOC click)
- [x] Fix 17: Static discharge enhanced — thicker lines (1.5px), longer branches (6 segments), brighter glow, 8 frames
- [x] Fix 18: Blockquote styling enhanced — 3px gold border, gold text, tinted background

## Phase 2g: Content Enhancement — DONE
- [x] Apply V4 effects (data-compile, count-up, glitch, glitch-hover) to 6 high-priority posts (intro, absolute-scarcity, the-trust-machine, mystery-of-satoshi, bitcoin-is-money, bitcoin-is-digital-gold)
- [x] Apply effects to 6 medium-priority posts (bitcoin-is-time, bitcoin-is-information, bitcoin-is-the-internet-of-money, bitcoin-is-ethical-money, bitcoin-will-save-the-world, why-was-bitcoin-invented)
- [x] Apply effects to remaining 13 posts (what-is-bitcoin-2, what-is-bitcoin-3, great-excel-spreadsheet, bitcoin-is-a-network, why-should-you-care, why-will-bitcoin-win, orange-not-gold, other-peoples-definitions, manhattan-project, designed-money, unparalleled-new, about, trust-machine-speech)
- [ ] Add new effect types: Satoshi callout, comparison encrypt-bars, terminology tooltips (future)

## Phase 6: Go Live — DONE
- [x] Test live site thoroughly (homepage, guide, blog posts, about page all verified live)
- [x] Set up redirects from old WordPress URLs (`.htaccess` with RewriteRules)
- [x] Document workflow for reference (updated CLAUDE.md with current status, architecture, workflow)

## Phase 7: WBIGAF Content Integration — "The Guide"
WBIGAF = "Why Bitcoin Is Good As Fuck" — 83 markdown files in `WBIGAF/` organized into 9 chapters.
**Decision: New `/guide/` section** — dedicated multi-chapter guide, separate from blog.
Nav will become: Blog | Guide | Learn More | About

### Phase 7a: Structure (build the template) — DONE
- [x] Add `guide` content collection in `content.config.ts`
- [x] Create `TBB/guide/` directory for processed markdown files
- [x] Create guide landing page at `astro/src/pages/guide/index.astro` (9 chapter cards)
- [x] Create dynamic chapter route at `astro/src/pages/guide/[...slug].astro`
- [x] Add "Guide" to header nav (Blog | Guide | Learn More | About)
- [x] Test with 2 placeholder chapters (what-is-bitcoin, why-bitcoin)

### Phase 7b: Content (chapter by chapter)
Pipeline per chapter: triage → consolidate → edit → frontmatter → effects → images → review
- [x] Chapter 1: What is Bitcoin (2 source files → 1 polished page, ~2800 words, V4 effects applied)
- [x] Chapter 2: Why Bitcoin (6 files → 1 polished page, ~3500 words, V4 effects applied)
- [x] Chapter 3: Problems Bitcoin Solves (6 files → 1 polished page, ~3300 words, V4 effects applied)
- [x] Chapter 4: Bitcoin Past (6 files → 1 polished page, ~3200 words, V4 effects applied)
- [x] Chapter 5: Bitcoin Properties (21 files → 1 comprehensive page, ~4500 words, V4 effects applied)
- [x] Chapter 6: What is Bitcoin Exactly (6 files → 1 polished page, ~3800 words, V4 effects applied)
- [x] Chapter 7: Bitcoin Present (7 files → 1 polished page, ~3500 words, V4 effects applied)
- [x] Chapter 8: Why BTC is Good AF (13 files → 1 polished page, ~4200 words, V4 effects applied)
- [x] Chapter 9: Bitcoin Future (9 files + AI subdir → 1 polished page, ~2800 words, V4 effects applied)

**Phase 7b COMPLETE — 83 source files processed into 9 polished guide chapters (~31,600 total words)**
**Build: 59 pages, 0 errors, ~7.5s**

### Phase 7c: Polish — DONE
- [x] Cross-link guide chapters with related blog posts (2-4 related articles per chapter)
- [x] Add guide teaser to homepage (new section between Start Here and McAfee quote)
- [x] Review guide landing page chapter cards (fixed broken slugs for Ch 3 & 4, updated all titles/descriptions)

---

## Phase 10: Compendium Restructure — DONE
- [x] Fix mobile image overflow (`.prose img` → `max-width: min(560px, 100%)`)
- [x] Create shared chapter metadata (`astro/src/data/chapters.ts`)
- [x] Create chapter landing page template (`astro/src/pages/guide/chapter/[num].astro`)
- [x] Update guide landing page — all chapters link to landing pages, subtitle "The Compendium"
- [x] Delete all 9 Claude-written overview chapters from `TBB/guide/`
- [x] Add sub-chapter sibling navigation to article template (`[...slug].astro`)
- [x] Rename Guide → Compendium in nav (`Header.astro`) and homepage
- [x] Rearrange homepage: Hero → Quote → Compendium tile → Chapters → Stats → Terminal → Resources → Closer
- [x] Remove "This site is different" callout and "Start Here" dual cards from homepage
- [x] Add 9 redirect rules to `.htaccess` for deleted overview chapter URLs
- [x] Add `README.md` to GitHub repo (project overview + design philosophy)
- [x] Build verified — 55 pages, 0 errors

---

## Phase 11: Compendium Fixes (8 Issues) — DONE
Plan: `.claude/plans/nested-cooking-kernighan.md`

### Tier 1: Quick Fixes — DONE
- [x] Issue 1: Homepage "Resources" stat → count-up "110+" (was static "50+")
- [x] Issue 2: Homepage "Sub-Chapters" stat → "77+" total planned (was "21")
- [x] Issue 3: "Orange Not Gold" moved from compendium to blog posts (speech, not sub-chapter)
- [x] Issue 4: "Mystery of Satoshi" moved from blog posts to compendium 4.2 (chapter 4, order 3)
- [x] Issue 5: Removed duplicated opening sentences from 14 guide articles (76% had duplication)
- [x] Build verified — 55 pages, 7.32s, 0 errors

### Tier 2: Frontend Rearchitecture — DONE
- [x] Issue 6: Unified TOC + Chapter Guide navigation (single nav panel, expandable current sub-chapter)
- [x] Build verified — 55 pages, 7.83s, 0 errors

### Tier 3: Content & Voice Strategy — DONE
- [x] Issue 7: V4 effects audit + integration guide → `TBB/templates/v4-effects-guide.md`
- [x] Issue 8: Voice DNA review of Ch3.1 — 4 items flagged (2 duplications, 1 jargon, 1 self-quote)

---

## Phase 12: Content Projects

Source folder: `content/` (standalone guides and courses, not tied to the Astro site yet)

### Node SSH Course (`content/Node SSH/`)
A 7-part guide for node runners on SSHing into a Bitcoin node and using bitcoin-cli.

- [x] 01 - Security Concerns (risks, mitigations, checklist)
- [x] 02 - SSH Setup (key generation, first connection, config)
- [x] 03 - Navigating Your Node (containers, server commands, data locations)
- [x] 04 - bitcoin-cli Basics (command categories, reading output, first commands)
- [x] 05 - Explore the Blockchain (verify supply, inspect blocks, genesis block)
- [x] 06 - Network, Mempool, and Fees (peers, mempool, fee estimation, mining stats)
- [x] 07 - Tips and Troubleshooting (aliases, common errors, server maintenance)
- [ ] Add SSH vs RPC explainer (what RPC is, when to use each, security comparison)
- [ ] Review and edit all 7 files for voice consistency
- [ ] Decide: publish as blog series, compendium section, or standalone page?

### RPC Direct Access (research)
- [ ] Investigate if StartOS exposes Bitcoin Core RPC to LAN
- [ ] If possible: set up direct RPC access from Claude Code (no SSH needed for queries)
- [ ] Document RPC setup in SSH Instructions.md

### Merchants Onboarding Guide (`content/Merchants/`)
A practical guide for businesses that want to accept bitcoin without Square/Strike/third-party processors.

- [ ] Research: payment methods (on-chain, Lightning, BTCPay Server, self-hosted vs hosted)
- [ ] Research: accounting and tax considerations (cost basis, record-keeping)
- [ ] Research: point-of-sale options (BTCPay POS, Breez, Phoenix, paper wallets for small shops)
- [ ] 01 - Why Accept Bitcoin (benefits, who's doing it, what to expect)
- [ ] 02 - Choosing a Setup (BTCPay Server vs alternatives, self-custody vs custodial tradeoffs)
- [ ] 03 - Setting Up BTCPay Server (step-by-step, connecting to your own node)
- [ ] 04 - Day-to-Day Operations (invoicing, refunds, denomination, staff training)
- [ ] 05 - Accounting and Taxes (record-keeping, tools, working with accountants)
- [ ] 06 - Common Questions (volatility, chargebacks, customer experience, tipping)
- [ ] Review and edit for voice consistency
- [ ] Decide: publish as blog series, compendium section, or standalone page?

---

---

## Phase 13: Bitcoin Knowledge Base Integration

Source repo: `tnull/bitcoin-knowledge-base` (MIT/Apache dual license)
Live API: `https://bitcoinknowledge.dev` -- free, no API key, run by tnull (LDK contributor)

**What it is:** A continuously-updated index of Bitcoin developer discourse -- BIPs, BOLTs, bLIPs,
GitHub issues/PRs/commits, bitcoin-dev/lightning-dev mailing lists, Delving Bitcoin forum, IRC logs,
BitcoinTalk, Optech newsletters. Queryable via free public REST API. No signup required.

**Scope (confirmed by API testing):** Technical developer discourse only. Does NOT cover Bitcoin
economic philosophy, Austrian economics, Cantillon effect, or Satoshi's early writings. Ch1-Ch3
compendium content is out of scope. Best fit: Node SSH course, future Lightning/SegWit/Taproot
sub-chapters, any protocol-focused technical content.

**Architecture -- final decisions:**
- bkb-mcp binary: NOT used. No Rust required. No installation required.
- Claude Code sessions: NO bkb integration. Dev sessions stay clean.
- Satoshi agent: Python script calls bitcoinknowledge.dev REST API directly via `requests`.
  Tool definitions are JSON in the script. No MCP, no binary, no extra process.
- Verification: built into the Satoshi agent (--verify flag), NOT a Claude Code slash command.
- Dependency: one person's free hosted server. If it goes down, self-host bkb-server on a VPS.
  Repo is MIT/Apache so that option always exists.

---

### Phase 13a: API Reference -- DONE (tested, no install required)

Live endpoints at `https://bitcoinknowledge.dev`:
- `GET /search?q=...` -- full-text search (filters: source_type, repo, author, after, before, limit)
- `GET /bip/{number}` -- full BIP + cross-references + concept tags (e.g. BIP 341 = full Taproot spec)
- `GET /bolt/{number}` -- full BOLT spec + references + concepts
- `GET /blip/{number}` / `/lud/{number}` / `/nut/{number}` -- other specs
- `GET /timeline/{concept}` -- chronological history (e.g. taproot: 2013-2017 dev history)
- `GET /references/{entity}` -- all documents citing a given spec or GitHub item
- `GET /find_commit?q=...` -- find commits by description, optional repo filter
- `GET /document/{id}` -- full document by `source_type:source_id`

- [x] Test live API against compendium topics
- [x] Confirm scope: technical developer discourse only
- [ ] Add bkb as research reference in CLAUDE.md for technical content sessions

---

### Phase 13b: Satoshi Agent -- CLI

Standalone Python script. No Rust, no MCP binary, no Claude Code integration.
Calls Claude API directly. Defines bkb tools as JSON. Calls bitcoinknowledge.dev via `requests`.

**Dependencies (Python only):**
```bash
pip install anthropic requests python-dotenv
```

**Two modes:**
- Q&A: `python satoshi-agent.py "What is Taproot?"`
  → searches bkb → answers with source citations (BIP numbers, mailing list authors, dates)
- Verify: `python satoshi-agent.py --verify "Taproot activated in November 2021"`
  → SUPPORTED / UNSUPPORTED / NO RECORD + primary source evidence

**System prompt outline:**
- Identity: Bitcoin expert who speaks from the primary technical record
- Voice: precise, direct, cites BIPs/BOLTs by number, names mailing list authors + dates
- Behavior: always call bkb tools before answering; acknowledge when KB has no record
- Out of scope: price, investment, altcoins, economic philosophy outside the technical record

**Script structure (`scripts/satoshi-agent.py`):**
- Load ANTHROPIC_API_KEY from .env (never hardcoded)
- Define 10 bkb tools as Claude tool_use JSON (search, bip, bolt, blip, timeline,
  references, find_commit, get_document, lud, nut)
- Each tool handler: calls bitcoinknowledge.dev REST endpoint via requests, returns JSON
- Agentic loop: send message → if tool_use response → call handler → feed result back → repeat
- Parse --verify flag to set mode; system prompt variation per mode

- [x] Draft Satoshi system prompt (<500 tokens, covers both modes)
- [x] Build `scripts/satoshi-agent.py` (Python + Anthropic SDK + requests, no other deps)
- [ ] Add ANTHROPIC_API_KEY to `.env` file in project root
- [ ] Test against 10 canonical questions: Taproot, SegWit, Lightning channel mechanics,
  HTLCs, block size debate, PoW security model, PSBT, Script types, fee estimation, BOLT 12
- [ ] Evaluate: cites sources correctly? Stays in scope? Admits uncertainty on KB gaps?

---

### Phase 13c: Content Pipeline (technical chapters only)

For sessions writing technical compendium sub-chapters or the Node SSH course.
Uses WebFetch to query bitcoinknowledge.dev directly in Claude Code -- no MCP needed.

**Research workflow (new technical sub-chapter):**
1. WebFetch `bitcoinknowledge.dev/search?q=[topic]` -- mailing list + Delving Bitcoin threads
2. WebFetch `bitcoinknowledge.dev/bip/[N]` if the chapter covers a spec
3. WebFetch `bitcoinknowledge.dev/timeline/[concept]` for protocol history
4. Draft grounded in primary record; include author names and dates where available
5. WebFetch `bitcoinknowledge.dev/references/[entity]` for related cross-links

**Best-fit content:** Node SSH course (bitcoin-cli, RPC, UTXO, mempool, PoW),
future Lightning/Taproot/SegWit sub-chapters, any protocol-focused content.
Not useful for Ch1-Ch3 economic/philosophical chapters.

- [ ] Apply research workflow during Node SSH course review (Phase 12)
- [ ] Add "Primary Sources" section template to `TBB/templates/blog-post.md`
- [ ] Add bkb research workflow to CLAUDE.md content conventions (technical posts only)

---

### Phase 13d: Satoshi Agent -- Web Widget (decision-gated, after 13b)

Only proceed after 13b is built and quality is verified against the 10 test questions.

- [ ] Decision: CLI only, or embed "Ask Satoshi" on TBB website?
- [ ] If widget: Astro API route (server-side) -- ANTHROPIC_API_KEY never exposed to client
- [ ] If widget: dedicated `/ask` page (V4 terminal aesthetic -- natural fit for the design system)
- [ ] If widget: rate limiting + abuse prevention before going live

---

---

## Phase 14: TBB Business Foundation

The Bitcoin Breakdown as a media, education, and consulting business under 2112 Capital Solutions LLC. Operating manual: [TBB Media Company/CLAUDE.md](TBB Media Company/CLAUDE.md). Synthesis: [synthesis.md](TBB Media Company/business/synthesis.md). Episode roadmap: [episode-roadmap.md](TBB Media Company/podcast/episode-roadmap.md). Teaching framework: [teaching-framework.md](TBB Media Company/business/teaching-framework.md).

Directory: `TBB Media Company/` -- podcast, YouTube, newsletter, social, brand, consulting, and business planning. Legacy archives preserved in three `(old)` subfolders.

### Legal & Compliance

**Already done (2112 Capital Solutions LLC, formed July 2023):**
- [x] LLC formation (NJ, Entity ID: 0450997703)
- [x] EIN (93-2439353)
- [x] State tax / employer registration (access code on file)
- [x] Business registration certificate
- [x] 2025 annual report
- [x] BOI reporting (12/3/24, Tracking ID: BOIRY7yz2QRzzT8M6fkG)
- [x] Registered agent (Republic Registered Agent LLC, Bizee auto-renews)

**Remaining:**
- [ ] Review Dow Jones employment agreement -- non-compete, non-solicitation, moonlighting policy (blocks paid workshops and consulting)
- [ ] File DBA for "The Bitcoin Breakdown" -- Hudson County Clerk (~$50-75)
- [ ] Trademark "The Bitcoin Breakdown" -- USPTO Class 41: education and entertainment services (~$250-350)
- [ ] Open bank account under DBA (present DBA certificate + 2112 Capital Solutions LLC docs)
- [ ] Draft operating agreement (liability protection -- single-member LLC)
- [ ] Consider S-Corp election when revenue exceeds ~$75K (talk to CPA)

**Recurring (track these):**
- [ ] NJ annual report -- file yearly (next due ~mid 2026)
- [ ] Registered agent renewal -- Bizee auto-renews, verify credit card is current
- [ ] Hostinger website renewal -- July 16, 2027

### Episode 1: Golden Rules of Bitcoin (SHIP THIS FIRST)

- [ ] Pull Golden Rules brain dump script from `The Bitcoin Breakdown (old)/Lessons/Golden Rules Video/`
- [ ] Edit into speakable outline (talking points, not prose)
- [ ] AI polish pass using Voice DNA profile
- [ ] User read-through: add riffs, cut what's wrong, mark emphasis points
- [ ] Set up Spotify for Podcasters account
- [ ] Record EP01 (OBS, audio-only, one take)
- [ ] AI post-production: show notes, 3-5 social posts, newsletter snippet
- [ ] Publish to Spotify for Podcasters
- [ ] Cross-post as TBB blog post with embedded audio (optional)
- [ ] Record EP02: Hello World (short intro/trailer, can ship same day)

### Production System (set up alongside or after EP01)

- [ ] Set up YouTube channel (branded, linked to TBB)
- [ ] Set up newsletter tool (Beehiiv free tier -- up to 2,500 subscribers)
- [ ] Set up social scheduling (Buffer free tier or similar)
- [ ] Set up social accounts: X, LinkedIn, TikTok, Reddit, Nostr
- [ ] Research AI agent tools for content repurposing (Hermes explainer skill, Paperclip, Claude API agents) -- Phase 2, after 5-10 manual episodes

### Competitive Research (standalone sprint, not blocking EP01)

- [ ] YouTube: Bitcoin education channels -- top 20 by subscribers, content types, posting frequency, revenue signals, gaps
- [ ] Podcasts: Bitcoin education shows -- formats, audience sizes, monetization (sponsors, ads, Podcasting 2.0/V4V)
- [ ] Courses: Who sells what, at what price, on what platform (Udemy, Teachable, Maven, self-hosted)
- [ ] Newsletters: Bitcoin education newsletters -- subscriber counts, sponsorship rates, platforms (Beehiiv, Substack, ConvertKit)
- [ ] Consulting/Training: Corporate Bitcoin education providers -- pricing, positioning, client types
- [ ] Gap analysis: What's missing in the market that TBB can uniquely fill (dense scripted content, Ark/L2 explainers, funny + educational)
- [ ] Deliverable: competitive landscape summary doc in `TBB Media Company/business/competitive-research.md`

### Content Channels (launch order)

- [ ] Podcast: scripted oratory episodes -- dense, pre-written, delivered with conviction (primary format, launching with EP01)
- [ ] YouTube: slide-based explainers (PowerPoint/Excalidraw + voiceover), how-to walkthroughs, Ark/L2 visual explainers
- [ ] Newsletter: episode digest + curated links (Beehiiv, launches when subscribers exist)
- [ ] Social: AI-generated clips and posts from each episode (X, LinkedIn, TikTok, Reddit, Nostr)
- [ ] TBB website: episodes become blog posts with show notes and embedded audio/video

### Revenue Foundations (as channels mature)

- [ ] Consulting: private Bitcoin setup and navigation sessions ($100/hr, $500 node setup, $100 self-custody, $50/mo maintenance)
- [ ] In-person workshops: Bitcoin basics, self-custody, AI tools (FreedomLab, JC Bitcoin, community venues)
- [ ] Digital products: ebooks, guides, course materials on Gumroad (free platform, 10% tx fee)
- [ ] Podcast sponsorships (once consistent cadence and growing audience)
- [ ] YouTube ad revenue (requires 1K subscribers + 4K watch hours)
- [ ] Corporate training: Bitcoin for businesses, treasury education ($2-5K/day)
- [ ] Explore: Ark community onboarding (workshops, starter kits, grants from HRF/OpenSats), college teaching, masterclass format

---

---

## Ideas / Future Features

### WBIGAF MCP Server
An MCP server for querying WBIGAF content -- argument blocks, compendium chapters, and blog posts. Enables episode research, book writing, and content creation without loading everything into context. Modeled on the Knowledge Distillery MCP server (`AI/AI Notes/kb-mcp/`).

**Phase 1: Argument blocks + catalog files**
- [ ] Design schema (block title, thesis, chapter, type, appeal, citations, source refs)
- [ ] Choose embedding + vector store (local-first: sqlite-vec, chromadb, or similar)
- [ ] Build ingestion pipeline (parse catalog.md files -> extract blocks -> embed)
- [ ] Build MCP server with search tools (semantic search, filter by chapter/type/appeal)
- [ ] Auto-reindex when catalog files change

**Phase 2: Compendium + blog posts**
- [ ] Ingest published compendium chapters from `TBB/guide/` (9 chapters, ~31K words)
- [ ] Ingest blog posts from `TBB/posts/` (~28 posts)
- [ ] Add full-text search across all content types
- [ ] Add `get_related` tool (find content related to a topic across all sources)

**Phase 3: Episode integration**
- [ ] Add episode script drafts to the index as they're created
- [ ] Add cross-reference tool (given a topic, return argument blocks + compendium sections + blog posts)
- [ ] Evaluate: wire into episode scripting workflow after EP03

### Ch1 Expansion -- Unpublished "What is Bitcoin?" Draft
The full ~7,738-word draft at `TBB/posts/2023/what-is-bitcoin.md` (draft: true) was never published. Contains dozens of Bitcoin definitions and a passionate intro that only partially made it into the Compendium as 1.11 "Other Bitcoin Definitions." Plan: fold this into the Ch1/Ch2 expansion pass after Ch3-9 pipeline completes.
- [ ] Read the full draft and compare to existing Ch1 guide content
- [ ] Identify unique material not already in the Compendium (definitions, voice, framing)
- [ ] Decide: expand existing 1.11, create new sub-chapters, or restructure Ch1 around this draft
- [ ] Run through pipeline (triage, argument map, etc.) or treat as direct voice-DNA source material

### Lightning Tip Bot
Add a Lightning Network tipping widget so readers can zap sats directly from the website.
- [ ] Research options (BTCPay Server widget, Alby, LNbits, Voltage, self-hosted LND)
- [ ] Choose approach (self-custody via own node vs hosted)
- [ ] Design placement (footer, article sidebar, dedicated "Support" page)
- [ ] Implement on site
- [ ] Test with small amounts

---

## JC Bitcoin CRM

Repo: `Jersey-City-Bitcoin/jcbtc-crm` (private) | Local: `JC Bitcoin/JC BTC/CRM/`
Scripts: `CRM/scripts/import_luma.py`, `import_organizers.py` | Command: `/import-contacts`

### Seeding

- [x] Build CRM repo, schema, importers, and `/import-contacts` command (2026-04-03)
- [x] Import Bitcoin Park 2026 organizer list — 37 contacts (jcbtc-001 to jcbtc-037)
- [ ] First Luma import — export attendees from meetup #5 or #6, drop CSV in `CRM/sources/`, run `import_luma.py --event jcbtc-00N`
- [ ] Migrate scattered contacts — review `Notes/2023-2025/Names.md`, `Notes/Sponsorship/`, `Notes/Initiatives/Businesses.md` and file via `/import-contacts`
- [ ] Enrich existing 37 organizer contacts — add emails, handles, phone numbers as acquired

### Enrichment

- [ ] Flag `privacy: sensitive` on Win Kokoaung (HRF) and any other public officials / journalists
- [ ] Resolve single-name contacts: Reed BTC, Clockwerk, Carl, Jhonny D, Foise — find full names if possible
- [ ] Build event file for Bitcoin Park 2026 (`events/2026-XX-XX-bp2026.md`) once date is confirmed

### V2 Importers (backlog)

- [ ] Meetup.com CSV importer
- [ ] Eventbrite CSV importer
- [ ] vCard (`.vcf`) batch importer
- [ ] `/crm-status` command — total contacts, recent additions, next event
- [ ] `/find-contact [query]` — search by name, email, or handle

---

> **Voice DNA** and **WBIGAF Book Project** have their own tracking system. See [`WBIGAF/WBIGAF-Status.md`](../WBIGAF/WBIGAF-Status.md) for all book-related progress.

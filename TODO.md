# The Bitcoin Breakdown - Implementation Tasks

## Quick Start (Resume)
```bash
cd c:\Users\GC\Documents\TBB\astro
npm run dev
```
Open http://localhost:4321 - See [CLAUDE.md](CLAUDE.md) for full context.

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
- [ ] Document workflow for reference

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

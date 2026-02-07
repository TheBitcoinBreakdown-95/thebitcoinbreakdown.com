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
- [ ] Fix image paths (currently pointing to WordPress CDN — need to download & localize)

## Phase 4: GitHub Actions + Hostinger FTP Deploy
- [x] Get Hostinger FTP credentials from hPanel
- [x] Add FTP credentials as GitHub repository secrets
- [x] Create GitHub Actions workflow file (`.github/workflows/deploy.yml`)
- [x] Backup existing WordPress files on Hostinger
- [ ] Test deployment (commit + push to trigger)

## Phase 5: Obsidian Workflow
- [x] Set up Git credentials on Windows
- [x] Create blog post template in `TBB/templates/blog-post.md`
- [ ] Test full workflow: edit → commit/push → auto-deploy

## Phase 6: Go Live
- [ ] Test live site thoroughly
- [ ] Set up redirects from old WordPress URLs
- [ ] Document workflow for reference

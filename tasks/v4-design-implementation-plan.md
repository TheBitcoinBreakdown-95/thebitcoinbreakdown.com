# V4 "Dark Luxury" Design System Implementation Plan

**Status:** NOT STARTED — Begin with Phase 1 (global.css rewrite)
**Created:** February 7, 2026
**Approved by user:** Yes

---

## Context

The user created a comprehensive design guide (V4) with a "Dark Luxury / Cypherpunk" aesthetic for thebitcoinbreakdown.com. The current site has a cyberpunk theme (Bitcoin orange on dark navy, Space Mono + Inter). The V4 design is a complete visual overhaul: gold (#FFD700) on pure black, Cormorant Garamond serif everywhere, JetBrains Mono for code, plus ~15 interactive JS effects (matrix rain, lightning transitions, glitch text, etc.).

This plan implements V4 in phases. All effects will be included.

**Reference files:**
- Design guide: `TBB/Website planning/V4/tbb-master-design-guide.md`
- HTML reference: `TBB/Website planning/V4/design-complete.html`

---

## Phase 1: Foundation (CSS + Fonts + Base Layout)

Replace the entire styling foundation. All other phases build on this.

### 1.1 Rewrite `astro/src/styles/global.css`
- Replace all CSS variables with V4 design tokens (Section 20 of guide)
- Swap fonts: `Cormorant Garamond` (primary) + `JetBrains Mono` (code)
- New color palette: pure black `#000`, gold `#FFD700`, cream `#E8E4DC`
- Add spacing scale (`space-1` through `space-10`)
- Add layout containers (content: 720px, wide: 1100px)
- Add easing functions (`ease-luxury`, `ease-out`)
- Typography: body at 17px/weight-300, clamp-based heading sizes
- Scrollbar styling (gold thumb on black track)
- `::selection` styling (gold)
- `cursor: crosshair` on all interactive elements
- Focus-visible styles (2px gold outline, 3px offset)
- Prose styles (`.prose` class for article content)
- Table, code, pre, blockquote base styles
- Print stylesheet (`@media print`)
- `prefers-reduced-motion` support
- Scroll reveal classes (`.reveal`, `.visible`, `.stagger`)
- Divider styles
- Tag, button, form base styles

### 1.2 Update `astro/src/layouts/BaseLayout.astro`
- Add Google Fonts link for Cormorant Garamond + JetBrains Mono
- Add skip link (`<a href="#main" class="skip-link">Skip to content</a>`)
- Add canvas elements for matrix rain, lightning, static discharge
- Add transition overlay div
- Add scroll progress bar div
- Add DataTicker component (or inline)
- Add `id="main"` to `<main>` element
- Include global interaction script at bottom of body

---

## Phase 2: Components

Rebuild all existing components and create new ones to match V4.

### 2.1 Rewrite `astro/src/components/Header.astro`
- Logo: "THE BITCOIN BREAKDOWN" as gold uppercase wordmark (not ₿ icon)
- Responsive: Full wordmark → "TBB" abbreviation → ₿ icon mark
- Nav links: 12px uppercase serif, 3px letter-spacing
- Nav hover: underline from center (scaleX), gold text + text-shadow
- Nav spark: small gold circle that flashes at underline origin on hover
- Logo easter egg: 3-second hover triggers glitch animation
- Mobile: hide nav links (burger menu or just hide for now)

### 2.2 Rewrite `astro/src/components/Footer.astro`
- Minimal: centered text, 12px uppercase, 4px letter-spacing
- "The Bitcoin Breakdown · 2026" style
- Account for data ticker space (bottom padding + 28px)

### 2.3 Rewrite `astro/src/components/PostCard.astro`
- Black-card background (`#0A0A0A`), no border-radius (sharp corners)
- Content: tag (10px uppercase gold-muted), title (22px serif), excerpt (14px muted), meta date, hash watermark (8px mono, 15% opacity)
- Hover effects: laser trace border (animated gold gradient), ambient glow, gold underline, title → gold, translateY(-3px), title scramble via JS
- Add `data-original` attribute on title for scramble effect
- Add `.card-glow` and `.card-underline` overlay divs

### 2.4 Rewrite `astro/src/components/PostMeta.astro`
- 12px uppercase, 2px letter-spacing, muted color
- Separator: `·` between date, reading time, category
- Border-bottom below meta

### 2.5 Create `astro/src/components/Divider.astro`
- Decrypting divider: gold gradient line that scales from 0 to full width on scroll
- Dot scatter animation (30 dots converge to center)
- Random spark effect every 3-7 seconds

### 2.6 Create `astro/src/components/ScrollProgress.astro`
- Fixed top, full width, 2px height
- Gold gradient with glow shadow
- Width calculated from scroll position (JS in BaseLayout)

### 2.7 Create `astro/src/components/DataTicker.astro`
- Fixed bottom bar, 28px height
- JetBrains Mono 10px, scrolling animation (40s loop)
- Content: block height, hash rate, mempool, difficulty, fees, nodes, supply
- Hidden on mobile
- Static data initially (can be dynamic later)

### 2.8 Create `astro/src/components/PullQuote.astro`
- Centered, gold italic serif text with text-shadow
- 60px gold-muted lines above and below
- Attribution: 12px uppercase muted
- Compile effect on scroll (text scrambles then resolves)

### 2.9 Create `astro/src/components/Terminal.astro`
- Black-soft background with 1px border
- Header bar: three colored dots + title
- Lines with `$` prompt in gold, output in muted
- Blinking gold cursor

---

## Phase 3: Pages

Rebuild all pages using V4 components and styles.

### 3.1 Rewrite `astro/src/pages/index.astro`
- Full-height hero with:
  - Decorative hash string (random hex, 10px mono, 20% opacity)
  - Overline: "Education · Clarity · Sovereignty"
  - Title: "Understand Bitcoin. Not the *noise.*" (with glitch on "noise.")
  - Body text: 18px, secondary color
  - Dual CTAs: primary "Start Learning" + ghost "Latest Articles"
  - Block height indicator (bottom-left)
  - Scroll indicator (bottom-center, bobbing arrow)
  - Pulsing radial gold gradient behind hero content
- Divider between hero and cards
- Article cards section with section label + card grid + "View all articles" standalone link
- Remove current hero styles entirely

### 3.2 Update `astro/src/pages/blog/index.astro`
- Page header with V4 typography
- Card grid using updated PostCard
- Section labels with typing effect

### 3.3 Update `astro/src/pages/about.astro`
- V4 prose styles
- Section structure with dividers

### 3.4 Create `astro/src/pages/404.astro`
- Giant faded "404" in gold (up to 160px, 15% opacity)
- Title: "Block Not Found"
- Description about moved/missing page
- "Return Home" CTA button
- Radial gold glow behind

### 3.5 Rewrite `astro/src/layouts/BlogPost.astro`
- Article meta bar (date · reading time · category)
- Table of contents (optional, for longer posts)
- Prose content area with V4 styles
- Pull quotes, blockquotes, footnotes support
- Tags at bottom
- Hash decorations at start/end of article
- Border-bottom below post header

---

## Phase 4: Interactive Effects (JS)

Create `astro/src/scripts/interactions.js` and include it in BaseLayout. All effects use vanilla JS with IntersectionObserver.

### Effects to implement:
1. **Matrix rain** — Gold hex characters cascade on load (~1.5s), then dissolve
2. **Static discharge** — Tiny gold tendrils on text selection mouseup
3. **Lightning bolt page transition** — 5-layer bolt strikes on nav link click
4. **Logo easter egg** — 3s hover triggers glitch animation
5. **Hero hash** — Random hex string that changes every 4s
6. **Card title scramble** — Random characters resolve to title on card hover
7. **Typing section headers** — Type character-by-character on scroll
8. **Count-up statistics** — Numbers animate from 0 to target on scroll
9. **Pull quote compile** — Text scrambles then resolves on scroll
10. **Footnote flash** — Gold glow pulse on scroll
11. **Divider decrypt** — Dots converge + line scales on scroll
12. **Divider spark** — Random sparks every 3-7s
13. **Encryption bars** — Gold progress fill on scroll
14. **Scroll progress bar** — Width based on scroll position
15. **Data ticker** — Scrolling data strip at bottom
16. **Scroll reveals** — Fade-up on IntersectionObserver
17. **Nav spark** — Flash at underline origin on hover
18. **Crosshair cursor** — On all interactive elements (CSS)

All animations respect `prefers-reduced-motion: reduce`.

---

## Phase 5: WordPress Migration

This phase is independent and can start alongside Phase 1.

### 5.1 Convert WordPress XML to Markdown
- Install `wordpress-export-to-markdown` (npm tool)
- Run against `TBB/thebitcoinbreakdown.WordPress.2026-02-05.xml`
- Output to a temporary folder, then review

### 5.2 Process converted posts
- Move to `TBB/posts/YYYY/` structure
- Update frontmatter to match Astro content collection schema:
  ```yaml
  title, description, pubDate, author, tags, image, draft
  ```
- Fix image paths (download/copy images to `TBB/assets/images/`)
- Apply photo treatment CSS to all images (grayscale + gold overlay)

### 5.3 Verify content renders correctly
- Build and check each post
- Ensure prose styles work with existing Markdown formatting
- Test tables, code blocks, blockquotes, lists, images

---

## File Summary

### Modified files (10):
| File | Change |
|---|---|
| `astro/src/styles/global.css` | Complete rewrite with V4 tokens |
| `astro/src/layouts/BaseLayout.astro` | Canvas elements, fonts, skip link, global JS |
| `astro/src/layouts/BlogPost.astro` | V4 article layout, prose, meta, TOC |
| `astro/src/components/Header.astro` | V4 wordmark, nav, spark effects |
| `astro/src/components/Footer.astro` | V4 minimal footer |
| `astro/src/components/PostCard.astro` | V4 card with laser trace, scramble |
| `astro/src/components/PostMeta.astro` | V4 article meta style |
| `astro/src/pages/index.astro` | V4 hero, card section |
| `astro/src/pages/about.astro` | V4 prose styles |
| `astro/src/pages/blog/index.astro` | V4 page styles |

### New files (8):
| File | Purpose |
|---|---|
| `astro/src/pages/404.astro` | "Block Not Found" page |
| `astro/src/components/Divider.astro` | Decrypting divider |
| `astro/src/components/ScrollProgress.astro` | Scroll progress bar |
| `astro/src/components/DataTicker.astro` | Bottom data ticker |
| `astro/src/components/PullQuote.astro` | Pull quote with compile effect |
| `astro/src/components/Terminal.astro` | Terminal console block |
| `astro/src/scripts/interactions.js` | All interactive JS effects |
| `astro/public/favicon.svg` | Updated favicon (gold B on black) |

---

## Verification

After each phase:
1. `npm run dev` — check localhost:4321 visually
2. `npm run build` — ensure no build errors
3. Test responsive behavior (mobile/tablet/desktop)
4. Test `prefers-reduced-motion` (all animations should stop)
5. Check crosshair cursor on interactive elements
6. Verify scroll reveals fire correctly
7. Test in both Chrome and Firefox

After Phase 5 (WordPress):
8. Verify all migrated posts render correctly
9. Check frontmatter is valid
10. Confirm images load and have photo treatment

---

## Execution Order

**Start with Phase 1** (foundation) — everything depends on the CSS tokens.
Then Phase 2 (components) → Phase 3 (pages) → Phase 4 (JS effects).
Phase 5 (WordPress) can run in parallel after Phase 1 is done.

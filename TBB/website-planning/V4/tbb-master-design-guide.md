# The Bitcoin Breakdown — Master Design Guide

**Codename:** Dark Luxury
**Version:** 4.0 (Definitive)
**Last Updated:** February 7, 2026
**Platform:** Astro (migrating from WordPress)
**URL:** thebitcoinbreakdown.com

---

## 1. Project Identity

### What It Is
A Bitcoin education, resource hub, and personal branding site. Designed to inform, educate, and provide rigorous breakdowns of the protocol, economics, and philosophy of Bitcoin.

### Aesthetic Influences
- **Art Deco** — Geometric minimalism, gold as a luxury signal, restrained ornamentation
- **Cypherpunk** — Cryptographic texture, terminal aesthetics, proof-of-work metaphors
- **Greco-Futurism** — Timelessness meets technology, classical authority with forward momentum
- **Dark Luxury** — Pure black foundations, gold accents, serif elegance, generous negative space

### Personality Spectrum
- Professional yet approachable
- Intellectual without being exclusionary
- Technically precise but never cold
- Authoritative through restraint, not decoration

### What This Site Is NOT
- A crypto trading dashboard or price tracker
- A meme-heavy Bitcoin culture site
- A generic tech blog with Bitcoin theming
- Anything that looks like it's trying to sell you a course

---

## 2. Color System

### Primitives

| Token | Value | Usage |
|---|---|---|
| `black` | `#000000` | Page background — pure, no texture |
| `black-soft` | `#060606` | Terminal backgrounds, subtle elevation |
| `black-card` | `#0A0A0A` | Card surfaces, form inputs, TOC, cookie banner |
| `black-elevated` | `#111111` | Skeleton loaders, inline code background |
| `black-code` | `#0D0D0D` | Code block backgrounds |
| `gold` | `#FFD700` | Primary accent — interactive elements, emphasis |
| `gold-muted` | `#C9A84C` | Secondary accent — labels, borders, muted interactive |
| `cream` | `#E8E4DC` | Primary text — warm off-white, never pure white |
| `muted` | `#8A857D` | Secondary text — body prose, descriptions |
| `dim` | `#5A5650` | Tertiary text — hints, placeholders, disabled |

### Semantic Tokens

| Token | Value | Usage |
|---|---|---|
| `background` | `#000000` | Page background |
| `surface` | `#0A0A0A` | Elevated surfaces (cards, modals) |
| `surface-elevated` | `#111111` | Second-level elevation |
| `accent` | `#FFD700` | Primary interactive color |
| `accent-muted` | `#C9A84C` | Secondary interactive, visited links |
| `text-primary` | `#E8E4DC` | Headlines, strong body text |
| `text-secondary` | `#8A857D` | Body paragraphs, descriptions |
| `text-muted` | `#5A5650` | Hints, captions, timestamps |
| `border-default` | `rgba(255, 215, 0, 0.06)` | Subtle structural borders |
| `border-hover` | `rgba(255, 215, 0, 0.15)` | Hover state borders |
| `border-focus` | `rgba(255, 215, 0, 0.5)` | Focus ring color |
| `selection-bg` | `rgba(255, 215, 0, 0.25)` | Text selection background |
| `selection-text` | `#FFD700` | Text selection foreground |

### Opacity Scale (Gold)

| Token | Value | Usage |
|---|---|---|
| `gold-glow` | `rgba(255, 215, 0, 0.4)` | Hover glows, text shadows |
| `gold-dim` | `rgba(255, 215, 0, 0.15)` | Focus ring background |
| `gold-subtle` | `rgba(255, 215, 0, 0.06)` | Table row hover, tag active fill |
| `gold-overlay` | `rgba(255, 215, 0, 0.04)` | Card ambient glow |

### Status Colors

| Status | Color | Dim | Border |
|---|---|---|---|
| Success | `#4ADE80` | `rgba(74, 222, 128, 0.1)` | `rgba(74, 222, 128, 0.2)` |
| Warning | `#FACC15` | `rgba(250, 204, 21, 0.1)` | `rgba(250, 204, 21, 0.2)` |
| Error | `#F87171` | `rgba(248, 113, 113, 0.1)` | `rgba(248, 113, 113, 0.2)` |
| Info | `#60A5FA` | `rgba(96, 165, 250, 0.1)` | `rgba(96, 165, 250, 0.2)` |

All status indicators must combine **icon + text + color** (never color alone) for WCAG compliance.

### Syntax Highlighting

| Token | Color | Usage |
|---|---|---|
| Keyword | `#FFD700` | `import`, `def`, `return`, `if` |
| String | `#A8D8A8` | String literals |
| Comment | `#5A5650` | Code comments (italic) |
| Number | `#F0A8A8` | Numeric literals |
| Function | `#A8C8F0` | Function/method names |
| Operator | `#8A857D` | Operators and punctuation |

---

## 3. Typography

### Font Families

| Role | Family | Fallback | Weight Range |
|---|---|---|---|
| Primary (all text) | Cormorant Garamond | Georgia, serif | 300–700 |
| Monospace (code/data) | JetBrains Mono | Fira Code, monospace | 300–500 |

**Google Fonts Import:**
```
https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400&family=JetBrains+Mono:wght@300;400;500&display=swap
```

**Design Decision:** The same serif family is used for everything — headlines, body, navigation, captions. This is intentional. The site's typographic variety comes from weight, size, spacing, and case, not from switching families. Monospace is reserved exclusively for code, terminal output, and cryptographic data (hashes, block heights, ticker).

### Type Scale

| Level | Size | Weight | Spacing | Line Height | Usage |
|---|---|---|---|---|---|
| Display | `clamp(36px, 7vw, 72px)` | 300 | 1px | 1.08 | Hero headlines |
| H1 | `clamp(28px, 5vw, 52px)` | 300 | 1px | 1.15 | Page titles |
| H2 | `clamp(24px, 4vw, 36px)` | 400 | 0.5px | 1.2 | Section heads |
| H3 | `clamp(18px, 2.5vw, 26px)` | 500 | 0.3px | 1.3 | Sub-section heads |
| Body | 17px | 300 | normal | 1.85 | Prose paragraphs |
| Nav | 12px | 400 | 3px | — | Navigation links |
| Caption | 12px | 400 | 4px (uppercase) | — | Dates, reading time, meta |
| Overline | 11px | 400 | 6px (uppercase) | — | Hero overlines |
| Section Label | 10px | 400 | 5px (uppercase) | — | Section identifiers |
| Tag | 10px | 400 | 3px (uppercase) | — | Category/topic chips |

### Pull Quote

| Property | Value |
|---|---|
| Size | `clamp(22px, 3.5vw, 32px)` |
| Weight | 300 |
| Style | Italic |
| Color | `#FFD700` (gold) |
| Text Shadow | `0 0 40px rgba(255, 215, 0, 0.1)` |
| Decorators | 60px gold-muted lines above and below, centered |
| Attribution | 12px uppercase, 3px letter-spacing, muted color |

### Blockquote

Standard blockquotes use a 2px gold-muted left border, 24px left padding, 20px italic text, with a 13px normal-style muted attribution line below.

---

## 4. Spacing System

**Base unit:** 16px

| Token | Value | Usage |
|---|---|---|
| space-1 | 4px | Icon gaps, tight padding |
| space-2 | 8px | Button icon spacing, small gaps |
| space-3 | 16px | Standard padding, form hint margin |
| space-4 | 24px | Card padding, paragraph spacing |
| space-5 | 32px | Section sub-spacing, terminal padding |
| space-6 | 48px | Between related sections |
| space-7 | 64px | Footer padding, major breaks |
| space-8 | 96px | Section vertical padding |
| space-9 | 128px | Major section separation |
| space-10 | 192px | Hero vertical padding |

---

## 5. Layout & Grid

### Containers

| Container | Max Width | Usage |
|---|---|---|
| Content | 720px | Prose, articles, forms — optimal reading measure |
| Wide | 1100px | Card grids, header, data tables, full-width sections |
| Full | 100% | Hero sections, backgrounds, dividers |

### Page Margin
- Desktop: `24px`
- Mobile: `20px`

### Breakpoints

| Name | Range | Key Changes |
|---|---|---|
| Mobile | 0–480px | Single column, stacked buttons, ticker hidden |
| Tablet | 481–768px | Nav collapses, 2-column grids |
| Laptop | 769–1024px | Full nav, standard layout |
| Desktop | 1025–1440px | All features active |
| Wide | 1441px+ | Content remains contained, generous margins |

### Grid

Card grids use `repeat(auto-fit, minmax(280px, 1fr))` for responsive behavior without explicit breakpoint overrides. Named `.grid--2` and `.grid--3` classes are available for fixed-column layouts with mobile collapse to single column.

---

## 6. Components

### Buttons

| Variant | Background | Text | Border | Hover Effect |
|---|---|---|---|---|
| Primary | `#FFD700` | `#000000` | None | Gold glow + translateY(-2px) |
| Ghost | Transparent | `#FFD700` | `1px solid rgba(255,215,0,0.25)` | Border sharpens, subtle gold fill, glow |

Both variants: 12px weight-500 uppercase, 4px letter-spacing, 16px × 44px padding. Small variant: 10px × 24px padding, 11px text.

### Article Cards

Structure: Black card background, 1px transparent border, tag (10px uppercase gold-muted), title (22px weight-400), excerpt (14px muted), meta/date, hash watermark (8px mono, 15% opacity).

**Hover effects (layered):**
1. **Laser trace border** — animated gold gradient traces the perimeter (mask-composite technique)
2. **Ambient glow** — radial gradient appears at top of card
3. **Gold underline** — 1px gradient line fades in at bottom
4. **Title color** — transitions to gold
5. **Transform** — translateY(-3px) + deep box-shadow
6. **Title scramble** — text scrambles through random characters then resolves (cypherpunk)

### Forms

**Input fields:** Black-card background, 1px default border, 14px × 18px padding, 16px serif text, italic muted placeholder. No border-radius (sharp corners = luxury). Hover: border brightens. Focus: gold border + 3px gold focus ring + subtle outer glow.

**States:** Error: red border. Success: green border. Each paired with 13px message text.

**Label:** 11px uppercase, 3px letter-spacing, secondary color.

**Search:** Icon inside field (left-aligned), gold on focus.

**Subscribe:** Horizontal email + button row, stacks vertically on mobile.

### Links

| Variant | Style | Hover |
|---|---|---|
| Inline | Gold text, 1px gold-20% underline | Underline solidifies, subtle text glow |
| Standalone | 12px uppercase muted + `→` arrow | Gold text, arrow shifts 4px right |
| Nav | 12px uppercase, underline from center | Spark at origin point, gold text + glow |

Visited inline links shift to gold-muted.

### Status Toasts

Left 3px colored border, tinted background (status-dim), icon + title + message. Variants: success (green), error (red), warning (yellow), info (blue).

### Code

**Inline:** Gold text on elevated black background, 1px default border, 2px × 8px padding, 0.85em mono font.

**Block:** Black-code background, 1px border, 24px padding, language label in top-right corner (10px uppercase). JetBrains Mono 14px, line-height 1.7. Syntax colors defined in the highlighting palette.

### Terminal Console

Black-soft background, 1px border. Header bar with three colored dots (red/yellow/green, outlined at 40% opacity), title in 10px uppercase muted aligned right. Lines show `$` prompt in gold, output in muted. Blinking gold block cursor on the last line.

### Tables

Gold-muted uppercase 11px headers with gold-15% bottom border. 16px cell padding. Hover rows get gold-subtle background. First column emphasized (primary text, weight 400).

### Table of Contents

Card container with 1px border. "In This Article" title (11px uppercase gold-muted). Links at 15px, preceded by a 12px gold line that extends to 20px on hover. Active link: gold text with extended line. Sub-items indented 24px at 14px muted.

### Footnotes

Superscript gold references (0.75em, weight 500) that flash gold when scrolled past (scroll-triggered animation). Bottom section with 1px top border, "References" label, numbered items at 14px muted.

### Tags

10px uppercase chips with 1px default border, gold-muted text, 6px × 14px padding. Hover: border brightens, text goes gold, subtle fill. Active variant: gold border, gold text, gold-subtle background.

### Empty States

Centered layout: large muted icon (48px, 30% opacity), 24px title, 15px muted description, optional CTA button. Used for search no-results, empty bookmarks, empty categories.

### 404 Page

Giant faded "404" in gold (up to 160px, 15% opacity). Title overlapping: "Block Not Found" in primary text. Description: "The page you're looking for doesn't exist — or has been moved to a different chain." Primary CTA to return home. Radial gold glow behind.

### Cookie Banner

Fixed bottom, card background, 1px top border. Flex layout: text + accept/decline buttons. Honest language: "This site uses essential cookies only. No tracking, no analytics, no third parties." Accept and Decline buttons have **equal visual prominence** (no dark patterns).

### Skeleton Loading

Card-shaped container with animated shimmer lines. Lines at various widths (40%, 70%, 90%) in elevated black with a sweeping gold-tinted highlight (shimmer animation, 2s loop).

### Scroll Progress Bar

Fixed top, full width, 2px height. Gold gradient (`#FFD700` → `#C9A84C`) with `0 0 8px rgba(255, 215, 0, 0.3)` glow. Width calculated from scroll position.

---

## 7. Logo & Branding

### Logo Lockup Variants

| Variant | Spec | Breakpoint |
|---|---|---|
| Full Wordmark | "THE BITCOIN BREAKDOWN" — 16px, weight 400, 3px letter-spacing, gold, uppercase | Desktop |
| Abbreviation | "TBB" — 20px, weight 400, 4px letter-spacing | Tablet |
| Icon Mark | ₿ inside a 32px × 32px box with 1px gold border | Mobile |
| Favicon | "B" in 16px gold-filled square, JetBrains Mono, black on gold | All (tab icon) |

### Clear Space
Minimum clear space around any logo variant = 1× the height of the logo mark.

---

## 8. Photography Treatment

All photographs receive a consistent treatment to unify diverse imagery within the dark luxury palette:

- **Filter:** `grayscale(70%) contrast(1.1) brightness(0.8)`
- **Overlay:** `linear-gradient(135deg, rgba(255,215,0,0.08), rgba(201,168,76,0.15))` with `mix-blend-mode: overlay`
- **Hover:** Grayscale reduces to 40%, brightness increases slightly
- **Captions:** 12px italic, muted color, 2px letter-spacing

---

## 9. Icons

- **Style:** Thin line, 1.5px stroke, rounded caps and joins, no fill
- **Source:** Feather Icons or Lucide as base set, SVG inline preferred
- **Sizes:** 16px (sm), 24px (default), 32px (lg)
- **Color:** Inherits `currentColor` — muted by default, gold on hover/active

---

## 10. Cypherpunk Interactions

The cypherpunk aesthetic is expressed **exclusively through interactions**, not background textures. The background is always pure black. This is an intentional design principle: restraint makes every effect more powerful.

### Matrix Rain (Page Load)
Gold hex characters (`0-9 A-F ₿`) cascade briefly on page load (~1.5 seconds) at ~12% opacity, sparse (only ~30% of columns active per frame). Then dissolves with a 1-second opacity transition. Also triggers as a brief transition when navigating between pages. Characters use system monospace at 14px.

### Glitch Text
**Persistent:** Used on the hero keyword (e.g., "noise."). Two pseudo-element layers with `clip-path: inset()` animations that fire at the 95–99% mark of a 4-second cycle — brief, infrequent disruption.

**Hover-triggered:** Same technique compressed into a 0.4-second burst. Used on interactive text elements like article titles and section accents.

### Card Title Scramble
On card hover, the title text scrambles through random characters (from the set `A-Z a-z 0-9 @ # $ % &`) then resolves left-to-right at 1.5 characters per 30ms frame. Same serif font throughout — no font change. On mouse leave, immediately snaps back to original.

### Lightning Bolt Page Transition
When clicking any navigation link, a lightning bolt strikes from the top of the viewport to the exact click coordinates.

**Rendering layers (5-pass):**
1. Hot white core (3px, no blur)
2. Bright gold (2.5px, 8px blur)
3. Gold glow (5px, 25px blur)
4. Wide aura (12px, 50px blur)
5. Ambient bloom (24px, 80px blur)

**Additional details:** 2-3 branching forks from random points along the main bolt. Radial gradient impact flash at click point. Uses recursive midpoint displacement algorithm for natural jagged shape. Fades over 18 frames. Screen briefly transitions to black then recovers.

### Static Discharge (Text Selection)
On mouseup after selecting text (minimum 2 characters), 2-4 tiny gold lightning tendrils radiate from the release point. Each has 3 segments, 0.5px width, 50% gold opacity. Fades over 5 frames. Much subtler than the page transition bolt.

### Nav Spark
When hovering a navigation link, a small gold spark (3px circle with 6px + 12px box-shadow glow) briefly flashes at the left origin point of the underline. Fades over 0.4 seconds.

### Crosshair Cursor
All interactive elements (links, buttons, cards, scramble text) use `cursor: crosshair` instead of the default pointer.

### Logo Easter Egg
Hovering the logo for 3+ seconds triggers a 0.5-second glitch animation — position jitter, hue rotation, brightness spike.

### Typing Section Headers
Section labels type themselves character by character (35ms per character) when they enter the viewport (50% threshold, fires once).

### Count-Up Statistics
Numbers count from 0 to their target value over 1.5 seconds with cubic ease-out. Triggered by scroll intersection (50% threshold, fires once).

### Pull Quote Compile Effect
Pull quote text appears as scrambled characters from the set `A-Z a-z . , ; : ! ?` and resolves left-to-right at 2 characters per 25ms frame. Same gold italic serif styling throughout — no font or color change. Triggered on scroll.

### Footnote Flash
Footnote reference numbers briefly pulse with a gold glow (`0 0 12px gold, 0 0 24px gold-30%`) when scrolled into view. 0.6-second animation, fires once.

### Decrypting Dividers
Section dividers start as 30 scattered dots (2px gold-muted, randomly offset ±200px horizontal, ±20px vertical) that converge to center while a gold gradient line scales from 0 to full width. Dots fade out after 0.8 seconds.

### Sparking Dividers
A random divider sparks every 3–7 seconds: a 4px × 5px gold circle with glow appears at a random position along the line, visible for 150ms.

### Encryption Progress Bars
2px gold gradient bars that fill with quartic ease-out over 3 seconds. Accompanied by a mono 10px label (e.g., "DECRYPTING BLOCK DATA...") and a percentage counter. Triggered on scroll.

### Data Stream Ticker
Fixed to the bottom of the viewport. 28px height, black-soft background, 1px top border. JetBrains Mono 10px, 2px letter-spacing. Scrolls continuously (40-second loop). Content: block height, hash rate, mempool tx count, difficulty, fees, node count, supply, next halving. Hidden on mobile.

### Hash Decorations
Decorative hexadecimal strings (9px mono, 2px letter-spacing, 15% opacity, non-selectable) used as ambient watermarks at the beginning and end of article content. Also as card hash watermarks (8px).

### Block Height Counters
10px mono text with a pulsing 6px square indicator. Shows data like "BLOCK #881,247" at 35% opacity.

---

## 11. Motion & Animation

### Easing Functions

| Name | Value | Usage |
|---|---|---|
| Luxury | `cubic-bezier(0.23, 1, 0.32, 1)` | Scroll reveals, card hovers, nav transitions |
| Out | `cubic-bezier(0.16, 1, 0.3, 1)` | Encryption bars, divider reveals |

### Scroll Reveals
Elements enter with `opacity: 0 → 1` and `translateY(32px → 0)` over 1.2 seconds using luxury easing. Triggered at 15% intersection threshold with -40px bottom root margin.

**Stagger:** Child elements in a `.stagger` container delay by 0s, 0.1s, 0.15s, 0.2s increments.

### Hover Transitions
Standard hover transitions use 0.3–0.5 seconds. Card transforms use luxury easing. Glow effects fade with standard ease.

### Hero Pulse
Radial gold gradient behind the hero content pulses with a 6-second animation — opacity oscillates between 0.5 and 0.8, scale between 1.0 and 1.06. Uses irregular timing (not a simple sine wave) for organic feel.

### Reduced Motion
All animations and transitions are disabled via `prefers-reduced-motion: reduce`. Reveals show immediately at full opacity. Matrix rain canvas is hidden. All `animation-duration` and `transition-duration` forced to `0.01ms`.

---

## 12. Accessibility

### Focus States
- **Style:** 2px solid gold outline, 3px offset, 2px border-radius
- **Selector:** `:focus-visible` only (no outline on mouse click)

### Skip Link
Hidden off-screen by default. Appears at top-left on Tab keypress: gold background, black text, 8px × 20px padding, 13px uppercase with 2px letter-spacing.

### Color Independence
All status states (success, error, warning, info) combine icon + text + color. Color is never the sole indicator.

### Touch Targets
Recommended minimum: 44px × 44px. Absolute minimum: 24px × 24px.

---

## 13. Gestalt Principles (Codified)

### Proximity
- Cards within the same section use `space-4` (24px) gaps
- Sections are separated by `space-8` (96px) padding
- Related meta elements (date · reading time · category) use `space-4` gaps with `·` separators
- Unrelated sections have decrypting dividers between them

### Similarity
- **Gold = interactive.** Anything gold can be clicked, hovered, or acted upon
- **Muted = informational.** Gray/muted text is for reading, not interacting
- **Mono = data/proof.** JetBrains Mono always signals cryptographic, technical, or machine-generated content
- **Uppercase = structural.** Labels, tags, nav, overlines are uppercase; prose content never is

### Continuity
- The eye flows: overline → headline → body → CTA → cards (top to bottom)
- Gold accents create a visual thread that guides scanning
- Decrypting dividers signal "new topic" without breaking flow
- Scroll progress bar reinforces top-to-bottom reading direction

### Figure-Ground
- Pure black background pushes all content forward
- Cards use `#0A0A0A` — barely distinguishable but perceptually "elevated"
- Gold elements are always foreground; they never recede
- Hover states amplify figure-ground separation (glow, shadow, translate)

### Closure
- Card laser borders don't need to be visible at rest — the brain completes the rectangle from the card content alignment
- Hash watermarks are truncated by overflow — the reader understands they continue beyond the visible area
- The encryption progress bar implies a process that began before and concludes after you see it

---

## 14. Semiotics Map

### Color as Symbol

| Element | Symbolism |
|---|---|
| **Gold** (`#FFD700`) | Sound money, incorruptibility, permanence. Gold is the one material humanity has universally agreed stores value. Using it as the accent says: "this content is valuable." |
| **Pure Black** (`#000000`) | Sovereignty, independence, void. No background noise — only signal. The absence of color is a statement of confidence. |
| **Cream** (`#E8E4DC`) | Warm but not white. Avoids the clinical sterility of `#FFFFFF`. Implies parchment, age, knowledge passed through time. |

### Typography as Symbol

| Element | Symbolism |
|---|---|
| **Cormorant Garamond** | Timelessness, classical authority. Serifs say: "this is a serious publication, not a tweet." Weight 300 (light) says: "confident enough to whisper." |
| **JetBrains Mono** | Cryptographic proof, machine precision. Appears only alongside verifiable data — hashes, code, block heights. Its presence says: "this is mathematically true." |
| **Uppercase** | Structure, system, protocol. Labels and nav in uppercase feel institutional. Body text in mixed case feels human. The contrast is intentional. |

### Motif as Symbol

| Motif | Symbolism |
|---|---|
| **Lightning bolt** | Energy, proof-of-work, the Bitcoin Lightning Network. The page transition bolt is also a metaphor for the speed of digital money. |
| **Glitch effect** | Disruption of the existing order. Bitcoin glitches the financial system. The effect is brief and controlled — revolution, not chaos. |
| **Matrix rain** | The underlying data layer of reality. Bitcoin is information money. The rain appears once and dissolves — you're meant to glimpse it, not stare at it. |
| **Hash strings** | Cryptographic proof. These decorative hex strings say: "everything here is verifiable." They're not readable — they're atmospheric. |
| **Terminal console** | Direct access to the protocol. No GUI intermediary. The terminal is the cypherpunk's native environment. |
| **Crosshair cursor** | Precision, targeting. You're not just browsing — you're locking onto information. |

---

## 15. Trust Signals & Emotional Design

### Visual Credibility Cues
- **No stock photography.** All images receive the desaturation + gold duotone treatment, creating a cohesive visual language that says "curated"
- **Typography signals seriousness.** Light serif at large sizes communicates confidence without shouting
- **Generous spacing.** Luxury brands use whitespace to signal that content doesn't need to compete for attention
- **Hash watermarks.** Even as decoration, they subconsciously reinforce "verification" and "proof"
- **Terminal console.** Showing actual Bitcoin CLI commands signals technical competence
- **No ads, no pop-ups, no email gates.** The design itself is a trust signal

### The Aesthetic-Usability Effect
Research shows users perceive aesthetically pleasing designs as more usable and trustworthy. The dark luxury aesthetic isn't just visual preference — it's a trust-building mechanism. Readers are more likely to engage deeply with content that feels premium.

### What "Rigorous, Not Shilling" Looks Like
- Content is presented, not sold. CTAs say "Start Learning" not "Join Now Before It's Too Late"
- No countdown timers, no urgency language, no fake scarcity
- Equal-prominence Accept/Decline on cookie banner
- Status toasts for factual states, not persuasion
- Pull quotes from primary sources (cypherpunks, the whitepaper), not influencers

---

## 16. Cognitive Load Rules

### Content Density
- **Maximum cards per row:** 3 (auto-fit handles this responsively)
- **Maximum items in navigation:** 5-6 top-level links
- **Maximum TOC depth:** 2 levels (H2 + H3). Never nest H4 in navigation
- **Maximum tags displayed:** 6-8 per article. Use "Show more" beyond that

### Progressive Disclosure
- Article content starts with meta + TOC before diving into prose
- Long articles use H2/H3 hierarchy for scanning before reading
- Footnotes are referenced inline but content lives at the bottom
- Terminal/code blocks are self-contained — you can skip them without losing the narrative

### Chunking
- Paragraphs are separated by `space-4` (24px). No paragraph exceeds ~150 words
- Pull quotes break long prose sections, providing a summary "anchor" every 3-4 paragraphs
- Visual dividers (decrypting lines) create distinct content chapters within a page
- Stats are presented in a grid, not inline, for scanability

### Hierarchy Rules
1. **One hero per page.** Never compete for primary attention
2. **One CTA per viewport.** Don't stack multiple calls to action
3. **Gold is used sparingly.** If everything is gold, nothing is gold
4. **Animations fire once.** No looping distractions in content areas (only the hero glow and data ticker loop)

---

## 17. Performance Budget

### Fonts
- **Maximum 2 families** (Cormorant Garamond + JetBrains Mono)
- **Maximum 10 weight/style combinations** total
- Use `font-display: swap` for all Google Fonts imports
- Subset to Latin characters if possible

### Animations & Effects
- **Maximum 3 canvas elements** active at any time (matrix rain is temporary)
- **Matrix rain stops rendering** after dissolve (boolean flag prevents requestAnimationFrame loop)
- **Intersection Observer** for all scroll-triggered effects (no scroll event listeners)
- **All animations respect `prefers-reduced-motion`**
- **No CSS animations on elements not in viewport** (reveal class prevents unnecessary rendering)

### Images
- All images lazy-loaded (`loading="lazy"`)
- WebP format preferred, with JPEG fallback
- Maximum width: 1100px (wide container)
- Thumbnail/card images: 400px wide maximum
- Hero images: use CSS gradients instead of images where possible

### CSS
- No external CSS frameworks. All styles are custom and purposeful
- CSS custom properties (variables) for all tokens — enables theme-level changes without code changes
- Backdrop-filter blur limited to header only (GPU-intensive)

### JavaScript
- No frameworks in the design system. Vanilla JS only
- All event listeners use delegation where possible
- IntersectionObserver preferred over scroll listeners
- Canvas animations use `requestAnimationFrame` with early-exit guards

### Target Metrics
- First Contentful Paint: < 1.5s
- Cumulative Layout Shift: < 0.1
- Total page weight (uncached): < 500KB
- Font files: < 200KB total

---

## 18. Print Stylesheet

When a reader prints an article, the following rules apply:

### What Changes
- Background becomes white, all text becomes black
- Gold accents become dark gray or black
- All animations, canvases, and interactive effects are hidden
- Navigation, header, footer, data ticker, cookie banner: hidden
- Scroll progress bar: hidden
- Cards: simplified to plain bordered boxes
- Images: filter removed, printed in full color
- Code blocks: light gray background with black text
- Links: show URL in parentheses after link text

### What Stays
- Full article content, headings, paragraphs
- Tables (with simplified borders)
- Blockquotes and pull quotes (without gold color)
- Footnotes and references
- Table of contents (as a simple list)

### CSS Media Query
```css
@media print {
  body { background: white; color: black; font-size: 12pt; }
  .site-header, .data-ticker, .scroll-progress,
  .cookie-demo, canvas, .scroll-indicator { display: none; }
  a { color: black; text-decoration: underline; }
  a::after { content: " (" attr(href) ")"; font-size: 0.8em; }
  pre { border: 1px solid #ccc; background: #f5f5f5; }
  .pull-quote { border-top: 1px solid #ccc; border-bottom: 1px solid #ccc; }
  .pull-quote-text { color: #333; text-shadow: none; }
}
```

---

## 19. Freedom as Design Philosophy

This is not a decorative motif — it's a structural principle. Freedom is expressed through what the site **refuses to do:**

- **No paywalls.** All content is freely accessible. Education should not be gated.
- **No email walls.** You never need to "sign up to continue reading."
- **No tracking analytics.** Cookie banner says "essential cookies only."
- **No dark patterns.** Accept and Decline have equal prominence. No pre-checked boxes. No guilt-tripping language.
- **No interstitials.** Content loads and you read it. Nothing interrupts.
- **Open layout.** The generous spacing and uncluttered design is the visual expression of freedom — nothing is crowded, nothing is trapped.

The absence of barriers IS the freedom statement. No icon or motif needed.

---

## 20. CSS Custom Properties (Copy-Paste Ready)

```css
:root {
  /* Colors */
  --black: #000000;
  --black-soft: #060606;
  --black-card: #0A0A0A;
  --black-elevated: #111111;
  --black-code: #0D0D0D;
  --gold: #FFD700;
  --gold-muted: #C9A84C;
  --gold-dim: rgba(255, 215, 0, 0.15);
  --gold-glow: rgba(255, 215, 0, 0.4);
  --gold-subtle: rgba(255, 215, 0, 0.06);
  --gold-overlay: rgba(255, 215, 0, 0.04);
  --text-primary: #E8E4DC;
  --text-secondary: #8A857D;
  --text-muted: #5A5650;
  --border-default: rgba(255, 215, 0, 0.06);
  --border-hover: rgba(255, 215, 0, 0.15);
  --border-focus: rgba(255, 215, 0, 0.5);

  /* Status */
  --success: #4ADE80;
  --success-dim: rgba(74, 222, 128, 0.1);
  --warning: #FACC15;
  --warning-dim: rgba(250, 204, 21, 0.1);
  --error: #F87171;
  --error-dim: rgba(248, 113, 113, 0.1);
  --info: #60A5FA;
  --info-dim: rgba(96, 165, 250, 0.1);

  /* Typography */
  --font: 'Cormorant Garamond', Georgia, serif;
  --font-mono: 'JetBrains Mono', monospace;

  /* Spacing */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 16px;
  --space-4: 24px;
  --space-5: 32px;
  --space-6: 48px;
  --space-7: 64px;
  --space-8: 96px;
  --space-9: 128px;
  --space-10: 192px;

  /* Layout */
  --content-width: 720px;
  --wide-width: 1100px;
  --page-margin: 24px;

  /* Easing */
  --ease-luxury: cubic-bezier(0.23, 1, 0.32, 1);
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
}
```

---

## Reference Files

| File | Description |
|---|---|
| `design-complete.html` | Comprehensive visual reference with all components and interactions |
| `tbb-design-tokens-v3-dark-luxury.json` | Machine-readable design tokens |
| `design-system-v3.html` | Component library (forms, links, status, code, tables, etc.) |
| `design-system-v2.html` | Layout, motion, and micro-detail demos |
| `moodboard.html` | Original mood board and aesthetic direction |

---

*This document is the single source of truth for The Bitcoin Breakdown's visual identity. Every design decision, from the gold hex value to the philosophy of freedom-through-absence, is documented here. When in doubt, refer to this guide.*

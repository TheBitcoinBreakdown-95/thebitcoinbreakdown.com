# V4 Effects — Content Author Guide

> Quick reference for adding interactive effects to blog posts and compendium sub-chapters. All effects are defined in `astro/src/scripts/interactions.js` and styled in `astro/src/styles/global.css`.

---

## Effects You Can Use in Markdown

These 5 effects work inside any `.md` file in `TBB/posts/` or `TBB/guide/`. Wrap text in raw HTML — Astro renders it inline with your markdown.

---

### 1. Typing Animation (`data-type`)

Heading types out character-by-character when scrolled into view.

```html
<h2 data-type>Your Heading Text</h2>
```

- Works on `h2`, `h3`, or any heading
- Triggers once at 35ms per character
- The `h1` title on guide articles already has this by default (set in the template)

---

### 2. Count-Up Number (`count-up`)

Animates a number from 0 to a target value over 1.5 seconds.

```html
<span class="count-up" data-target="21000000">0</span> bitcoins
```

**Options:**
- `data-target="N"` — the number to count to (required)
- `data-suffix="+"` — appends text after the number (optional, e.g., `+`, `%`, `M`)

**Example with suffix:**
```html
<span class="count-up" data-target="85" data-suffix="%">0</span> of all bitcoin has been mined
```

---

### 3. Text Compile / Unscramble (`data-compile`)

Text starts as random characters and "compiles" into the final text when scrolled into view.

```html
<blockquote data-compile data-final="The real quote text goes here.">
  ████████████████████████████████████
</blockquote>
```

**Rules:**
- `data-final="..."` — the text it compiles into (required)
- The visible content between tags is the scrambled placeholder (shown before animation)
- Works on `<blockquote>`, `<aside>`, `<p>`, or any block element
- Best for impactful quotes or key statements

---

### 4. Continuous Glitch (`glitch`)

Text permanently glitches with RGB color split and clip-path distortion.

```html
<span class="glitch" data-text="Fix the money. Fix the world.">Fix the money. Fix the world.</span>
```

**Rules:**
- `data-text="..."` must match the visible text exactly
- Creates `::before` and `::after` pseudo-elements for the effect
- Use sparingly — for closers, manifestos, or high-impact one-liners
- 4-second infinite animation loop

---

### 5. Glitch on Hover (`glitch-hover`)

Same visual as continuous glitch, but only triggers when the reader hovers.

```html
<span class="glitch-hover" data-text="absolute scarcity">absolute scarcity</span>
```

**Rules:**
- `data-text="..."` must match visible text exactly
- 0.4-second burst on hover, then stops
- Good for key terms, emphasis phrases, or provocative language
- Can be used more liberally than continuous glitch

---

## Effects Built Into Templates (Automatic)

These effects are applied by layouts and components — you don't need to add them manually.

| Effect | Where | What It Does |
|--------|-------|--------------|
| **Scroll Reveal** | All blog post content, guide headers | Fades in + slides up on scroll |
| **Lightning Transition** | All `.tbb-link` links | Gold lightning bolt draws before page navigation |
| **Matrix Rain** | Page load (homepage) | Brief golden text cascade, fades after 1.5s |
| **Static Discharge** | Text selection anywhere | Gold branches radiate from cursor on text release |
| **Logo Easter Egg** | Header logo | Glitch animation after hovering logo for 1 second |
| **Card Scramble** | Blog post cards | Title text scrambles on card hover |
| **Divider Decrypt** | `<Divider />` component | Dots scatter, gold line appears on scroll |
| **Footnote Flash** | `.fn-ref` links | Gold glow pulse when footnote scrolls into view |
| **Encryption Bar** | Series progress, homepage | Animated fill bar with percentage counter |
| **Scroll Progress** | All pages | Thin gold bar at top showing scroll position |

---

## Accessibility

All effects respect `prefers-reduced-motion: reduce`. When enabled:
- Canvas effects (matrix, static, lightning) are hidden entirely
- Scroll reveals show content immediately (no animation)
- Typing, compile, and scramble effects are skipped
- Count-up numbers display instantly at target value
- Content is always fully readable without any animation

---

## Usage Guidelines

**Density per article:**
- 1-2 `data-compile` quotes (signature moments)
- 3-8 `glitch-hover` terms (key concepts, provocative phrases)
- 0-1 `glitch` (continuous — only for closers or manifestos)
- 0-5 `count-up` numbers (statistics, data points)
- 0-2 `data-type` headings (section headers beyond the auto h1)

**Current usage across the site:**
- `fiat-capitalism.md` is the heaviest user: 20 glitch-hover, 7 count-up, 2 compile, 1 glitch
- Most guide articles use 1-3 effects total
- Blog posts from 2023 mostly use compile quotes and 1-2 glitch-hover terms

**When in doubt:** Less is more. Effects should punctuate, not saturate.

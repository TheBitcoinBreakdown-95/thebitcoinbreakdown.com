# The Bitcoin Breakdown — Design System v1: "Dark Luxury"

## Aesthetic Direction

**Minimalist Art Deco · Cypherpunk · Dark Luxury**

Pure black base with bright gold (#FFD700) accents. Elegant serif typography (Cormorant Garamond) used throughout — headlines and body. Subtle gold glow effects on interaction. Circuit-network background patterns at near-invisible opacity (~4%). Minimal ornamentation — luxury communicated through restraint, whitespace, and typographic refinement.

---

## Color Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `--black` | `#000000` | Page background |
| `--black-soft` | `#060606` | Nav bar, subtle surfaces |
| `--black-card` | `#0A0A0A` | Card backgrounds |
| `--black-elevated` | `#111111` | Elevated surfaces, modals |
| `--gold` | `#FFD700` | Primary accent, CTAs, highlights |
| `--gold-muted` | `#C9A84C` | Secondary accent, tags, overlines |
| `--text-primary` | `#E8E4DC` | Headings, primary body text |
| `--text-secondary` | `#8A857D` | Body paragraphs, descriptions |
| `--text-muted` | `#5A5650` | Captions, timestamps, excerpts |

### Transparency Scale

| Token | Value | Usage |
|-------|-------|-------|
| `--border-default` | `rgba(255, 215, 0, 0.06)` | Card borders, subtle dividers |
| `--border-hover` | `rgba(255, 215, 0, 0.15)` | Hover state borders |
| `--gold-subtle` | `rgba(255, 215, 0, 0.06)` | Ambient glow backgrounds |
| `--gold-dim` | `rgba(255, 215, 0, 0.15)` | Mid-intensity glow |
| `--gold-glow` | `rgba(255, 215, 0, 0.4)` | Text shadow glow |
| `--gold-overlay` | `rgba(255, 215, 0, 0.04)` | Card hover radial gradient |

---

## Typography

**Single font family throughout**: Cormorant Garamond (Google Fonts)

```
Import: https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400&display=swap
```

| Level | Size | Weight | Spacing | Line Height |
|-------|------|--------|---------|-------------|
| Display | clamp(36px, 6vw, 64px) | 300 | 1px | 1.1 |
| H1 / Hero | clamp(28px, 5vw, 52px) | 300 | 1px | 1.15 |
| H2 | clamp(24px, 4vw, 40px) | 400 | 1px | 1.2 |
| H3 | clamp(18px, 2.5vw, 28px) | 500 | 0.5px | 1.3 |
| Body | 17px | 300 | 0 | 1.75 |
| Caption | 12px uppercase | 400 | 4px | 1.4 |
| Overline | 11px uppercase | 400 | 6px | 1.4 |
| Nav link | 12px uppercase | 400 | 3px | — |
| Section label | 10px uppercase | 400 | 5px | — |
| Tag | 10px uppercase | 400 | 3px | — |

### Typography Notes
- Light weights (300) dominate — creates the luxury feel
- Uppercase with wide letter-spacing for labels, nav, and tags
- Gold color on key headline words for emphasis (with text-shadow glow)
- Italics used sparingly for emphasis within hero headlines

---

## Effects & Interactions

### Gold Glow (Signature Effect)
- **Text glow**: `text-shadow: 0 0 40px rgba(255,215,0,0.4), 0 0 80px rgba(255,215,0,0.15)`
- **Ambient card glow**: Radial gradient at top of card, opacity 0 → visible on hover
- **CTA glow**: `box-shadow: 0 0 30px rgba(255,215,0,0.3), 0 0 60px rgba(255,215,0,0.1)`

### Hover Behavior
- Cards: lift 3px, border brightens, ambient glow appears, gold underline fades in at bottom
- CTAs: lift 1px, glow intensifies
- Nav links: color shifts to gold, text-shadow glow appears
- Article titles: color transitions from cream to gold

### Motion
- **Easing**: `cubic-bezier(0.23, 1, 0.32, 1)` — slow, deliberate, luxurious
- **Duration**: 0.4–0.5s for hovers, 0.8s for entrances
- **Entrance animation**: fadeInUp (opacity 0 + translateY 20px → visible), staggered 0.1s

### Dividers
- Gold gradient lines: `linear-gradient(90deg, transparent, rgba(255,215,0,0.2), transparent)`
- Height: 1px
- Used between major sections

---

## Decorative Elements

### Circuit Pattern Background
- SVG pattern: circuit lines, nodes, connection points
- Color: #FFD700 at stroke-width 0.3–0.5px
- **Opacity: 0.04** (barely visible — subconscious texture)
- Fixed position, covers full viewport

### Ornamentation Philosophy
- **Minimal**. No sunbursts, no chevrons, no heavy Art Deco borders.
- Luxury is communicated through: negative space, typographic weight contrast, gold glow, and the quality of transitions.
- The circuit pattern is the single decorative motif — connecting the cypherpunk identity.

---

## Component Patterns

### Buttons
- **Primary**: Gold background, black text, uppercase, wide letter-spacing, glow on hover
- **Ghost**: Transparent, gold text, thin gold border (0.3 opacity), fills subtly on hover

### Cards
- Background: `#0A0A0A`
- Border: `1px solid rgba(255,215,0,0.04)`
- Padding: 32px 28px
- No border-radius (or 2px max) — sharp edges = luxury
- Hover: lift, border brightens, ambient glow, gold underline reveal

### Navigation
- Logo: Cormorant Garamond, 15px, weight 400, gold, letter-spacing 2px
- Links: 12px uppercase, letter-spacing 3px, muted → gold on hover with text-shadow

---

## Layout

- Max content width: 1100px
- Page horizontal padding: 24px
- Section vertical padding: 60px
- Card grid gap: 20px
- Border radius: 0–4px (sharp edges preferred)

---

## CSS Variables (Copy-Paste Ready)

```css
:root {
  --black: #000000;
  --black-soft: #060606;
  --black-card: #0A0A0A;
  --black-elevated: #111111;
  --gold: #FFD700;
  --gold-muted: #C9A84C;
  --gold-dim: rgba(255, 215, 0, 0.15);
  --gold-glow: rgba(255, 215, 0, 0.4);
  --gold-subtle: rgba(255, 215, 0, 0.06);
  --text-primary: #E8E4DC;
  --text-secondary: #8A857D;
  --text-muted: #5A5650;
  --font-display: 'Cormorant Garamond', Georgia, serif;
  --border-default: rgba(255, 215, 0, 0.06);
  --border-hover: rgba(255, 215, 0, 0.15);
  --ease-luxury: cubic-bezier(0.23, 1, 0.32, 1);
}
```

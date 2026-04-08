# JC Bitcoin — Presentation Style Guide

Single reference for creating all JC Bitcoin Google Slides presentations. Based on **visual inspection and API extraction** from 3 existing decks (2024-12-18, 2025-01-15, 2025-02-19).

> **Before modifying this guide**, follow the [Slide Ingestion Checklist](Slide-Ingestion-Checklist.md) to re-extract from reference decks. Never guess — always verify against thumbnails.

---

## 1. Brand Colors

### The Palette is Simple: Black + Orange

The decks use an extremely limited palette. Almost everything is black background with orange text.

| Role | Hex | RGB (0-1) | Usage |
|------|-----|-----------|-------|
| **Background** | #000000 | (0.0, 0.0, 0.0) | ALL slide backgrounds — set via theme, renders as solid black |
| **Primary Text** | #ff9900 | (1.0, 0.6, 0.0) | Titles, body text, bullets — the dominant text color everywhere |
| **Cover Text** | #ff9900 | (1.0, 0.6, 0.0) | Cover slide text — orange on transparent (black bg shows through) |
| **Alert Red** | #ff0000 | (1.0, 0.0, 0.0) | Rare emphasis (3 uses across all decks) |

> **Note**: `#ff9900` is the brand orange, not Bitcoin standard `#f7931a`. The decks do NOT use navy, dark blue, gray, or white for backgrounds or body text. It is black and orange only.

### Background Implementation

The reference decks use **theme-inherited backgrounds** (not solid fills on individual slides). The theme renders as black (#000000). When building via API, set solid black on every slide:

```
{ red: 0.0, green: 0.0, blue: 0.0 }  // #000000 — every slide
```

There are NO background images, NO gradients, NO secondary background colors.

### Text Color Rule

**Orange is the primary text color**, not an accent. The theme default foreground is orange. When elements return empty font/color sets from the API, they inherit orange from the theme. Titles are orange. Body text is orange. Bullets are orange. The only exception is the cover subtitle which may appear slightly muted.

---

## 2. Fonts

| Font | Usage | Context |
|------|-------|---------|
| **Calibri** | Everything — theme default for all text | Titles, body, cover, labels — all Calibri |

> **VERIFIED 2026-03-06**: The theme master placeholders explicitly set **Calibri** for both TITLE and BODY. All content slides show `font=(inherited)` in the API, which resolves to Calibri. Previous versions of this guide incorrectly listed Old Standard TT and Montserrat — those fonts are NOT used in any reference deck.

### Typography Hierarchy (from actual measurements)

| Element | Font | Size (pt) | Color | Bold | Alignment |
|---------|------|-----------|-------|------|-----------|
| Cover title | Calibri | 36 | #ff9900 | No | Center |
| Cover subtitle/details | Calibri | 18 / 14 / 11 | #ff9900 | No | Center |
| Slide title (standard) | Calibri (theme) | ~36 (inherited) | #ff9900 (inherited) | Yes | Start |
| Body text / bullets | Calibri (theme) | 25-26 | #ff9900 (inherited) | No | Start |
| Splash text | Calibri | 96+ | #ff9900 | Yes | Center |
| Small labels | Calibri | 11-23 | #ff9900 | Varies | Varies |

> **Critical**: Body/bullet text is **25-26pt**, not 16pt. These are meetup presentations projected on a screen — text must be readable from the back of the room.

---

## 3. Logo Assets

| File | Drive ID | Dimensions |
|------|----------|------------|
| JC Bitcoin Logo (circle) | `1XCi7pXbNwhX8VyVlF0XOmwV2_778xAA2` | Square — use at any size |

### Logo Placement (from reference decks)

| Slide | Position (EMU) | Size (EMU) | Notes |
|-------|---------------|------------|-------|
| Cover | x=2437898, y=90236 | 4268203 x 4268203 | Square, centered horizontally, near top |
| Interior slides | Not present in references | — | Reference decks do NOT use watermark logos on interior slides |

> The cover logo is **square** and **~4.27M EMU** (~4.7 inches) — much larger than the 1.8M previously used. It dominates the upper portion of the cover slide.

---

## 4. Slide Layout Patterns

Page dimensions: **9144000 x 5143500 EMU** (720 x 405 pt, standard 16:9).

The reference decks use **4 layout types**, not 6. These are the real patterns found across all 3 decks.

### 4.1 Cover Slide

The logo is the hero element. A white text box at the bottom holds the event title.

```
+─────────────────────────────────+
│          [BLACK BG]             │
│                                 │
│      ┌─────────────────┐        │
│      │                 │        │
│      │   LOGO IMAGE    │        │  ← 4268203 x 4268203 EMU (square)
│      │   (centered)    │        │     pos: (2437898, 90236)
│      │                 │        │
│      └─────────────────┘        │
│                                 │
│  ┌───────────────────────────┐  │
│  │ Jersey City Bitcoin       │  │  ← White text box (#ffffff fill)
│  │ Socratic Seminar #N       │  │     pos: (1142999, 3748440)
│  │                           │  │     size: 6858000 x 2442000
│  └───────────────────────────┘  │     Calibri 36/18/14/11pt, orange text
+─────────────────────────────────+
```

**Exact measurements:**
- Logo image: pos=(2437898, 90236), size=4268203 x 4268203
- Text box: pos=(1142999, 3748440), size=6858000 x 1200000, shapeBg=NOT_RENDERED (transparent)
- Text box font: Calibri, sizes 36/18pt, color #ff9900

### 4.2 Sponsor Slide

Full-width title text + large sponsor image below. Appears as slide 1 in all 3 decks.

```
+─────────────────────────────────+
│          [BLACK BG]             │
│  ┌───────────────────────────┐  │
│  │  Sponsored by:            │  │  ← Title shape (bold, theme orange)
│  └───────────────────────────┘  │     pos: (284662, 43275)
│                                 │     size: 8492100 x 994199
│  ┌───────────────────────────┐  │
│  │                           │  │
│  │    [SPONSOR LOGO IMAGE]   │  │  ← Nearly full-width image
│  │                           │  │     pos: (285750, 1167187)
│  │                           │  │     size: 8572500 x 3600450
│  └───────────────────────────┘  │
+─────────────────────────────────+
```

**Exact measurements:**
- Title: pos=(284662, 43275), size=8492100 x 994199, bold, theme-inherited orange
- Image: pos=(285750, 1167187), size=8572500 x 3600450

### 4.3 Content Slide (with optional image)

The workhorse layout. Title across the top, bullets below. Many content slides include an image on the right side.

**Variant A: Content + Image (e.g., Agenda slides)**
```
+─────────────────────────────────+
│          [BLACK BG]             │
│  ┌───────────────────────────┐  │
│  │  Agenda:                  │  │  ← Title (bold, theme orange)
│  └───────────────────────────┘  │     pos: (306112, 112837)
│                                 │     size: 8531700 x 994199
│  ┌──────────────┐ ┌──────────┐  │
│  │ • Bullet 1   │ │          │  │  ← Body text (26pt, theme orange)
│  │ • Bullet 2   │ │  IMAGE   │  │     pos: (151256, 1107112)
│  │ • Bullet 3   │ │          │  │     size: 6675300 x 3910500
│  │ • Bullet 4   │ │          │  │
│  │ • Bullet 5   │ │          │  │  ← Image on right
│  │              │ │          │  │     pos: (5791612, 1200412)
│  └──────────────┘ └──────────┘  │     size: 2614239 x 2985862
+─────────────────────────────────+
```

**Variant B: Content text-only (e.g., Guidelines slides)**
```
+─────────────────────────────────+
│          [BLACK BG]             │
│  ┌───────────────────────────┐  │
│  │  Title Text               │  │  ← Title (bold, theme orange)
│  └───────────────────────────┘  │     pos: (284662, 43275)
│  ┌───────────────────────────┐  │     size: 8492100 x 994199
│  │ • Bullet point text       │  │
│  │ • Another bullet          │  │  ← Body (25-26pt, theme orange)
│  │ • More content here       │  │     pos: (284662, 1037550)
│  │                           │  │     size: 6944100 x 3886200
│  │                           │  │
│  └───────────────────────────┘  │
+─────────────────────────────────+
```

**Variant C: Content with image right + smaller body text (e.g., initiative slides)**
```
Title: pos=(284662 or 471487, ~43275-205382), size ~(8492100, 994199)
Body: pos=(~68000-331181, ~722212-1268118), size ~(5000000-6334500, ~3263400-4192800)
Image: pos=(~5601112-6415579, ~974887-1151850), size ~(2614123-3267857, ~3456562-3646780)
```

**Key measurements:**
- Title shape: ~full slide width (8492100-8531700), height ~994199, starts at top (~43275)
- Body shape: width ~6675300-6944100, height ~3886200-3910500, starts below title (~1037550-1107112)
- Body text: **25-26pt**, orange, Old Standard TT (theme)
- Image (when present): positioned right side starting at x ~5791612, width ~2614239

### 4.4 Splash / Section Divider

Used for major topic transitions. Oversized text, centered, no images.

```
+─────────────────────────────────+
│          [BLACK BG]             │
│                                 │
│           INTRO                 │  ← Montserrat 144pt, bold, centered
│             TO                  │     Theme orange
│           CRYPTO                │     Multiple text boxes stacked
│                                 │
+─────────────────────────────────+
```

- Font: Montserrat, 144pt, bold
- Alignment: Center
- Multiple shapes stacked vertically for multi-line text
- Used sparingly (1-2 per deck)

### 4.5 Full-Text Slide (Centered)

For announcements, programs, or detailed text without bullets.

```
+─────────────────────────────────+
│          [BLACK BG]             │
│                                 │
│  ┌───────────────────────────┐  │
│  │  Main Title / Program     │  │  ← Centered, ~34-40pt
│  │  Name                     │  │     pos: (1143000, 841774)
│  └───────────────────────────┘  │     size: 6858000 x 1007400
│  ┌───────────────────────────┐  │
│  │  Description text and     │  │  ← Body text below
│  │  details go here          │  │     pos: (1143000, 2334524)
│  └───────────────────────────┘  │     size: 6858000 x 1608600
+─────────────────────────────────+
```

---

## 5. Content Conventions

### Text Patterns
- **Bullets**: Up to 10+ items per slide is acceptable (agenda slides have 10-11 items)
- **Title format**: Often ends with colon ("Agenda:", "Sponsored by:")
- **Emphasis**: Bold key phrases, not entire bullets
- **Text is orange** — not white, not gray, not black on these dark slides

### Standard Slide Order (from all 3 decks)
1. Cover (logo + event title)
2. Sponsor acknowledgment
3. Photo/promo image (full slide)
4. Agenda
5. Guidelines / housekeeping
6. Content sections...
7. (Optional splash dividers between major sections)

### What the Decks Do NOT Have
- No divider bars or accent lines between elements
- No background rectangles or content zones with different fill colors
- No gradient backgrounds
- No footer text on content slides
- No watermark/icon logos on interior slides
- No two-column comparison layouts
- No "Q&A" specific layout (just a content slide with centered text)

---

## 6. Google Slides API Reference

### Color Constants (RGB 0-1 format)

```python
C = {
    'black':   {'red': 0.0, 'green': 0.0, 'blue': 0.0},    # #000000 — all backgrounds
    'orange':  {'red': 1.0, 'green': 0.6, 'blue': 0.0},    # #ff9900 — all text
    'white':   {'red': 1.0, 'green': 1.0, 'blue': 1.0},    # #ffffff — NOT used (cover text box is transparent)
    'red':     {'red': 1.0, 'green': 0.0, 'blue': 0.0},    # #ff0000 — rare alerts
}
```

### Key Element Positions (EMU)

```python
# Cover slide
COVER_LOGO = {'x': 2437898, 'y': 90236, 'w': 4268203, 'h': 4268203}
COVER_TEXT = {'x': 1142999, 'y': 3748440, 'w': 6858000, 'h': 1200000}  # transparent bg (NOT_RENDERED)

# Sponsor slide
SPONSOR_TITLE = {'x': 284662, 'y': 43275, 'w': 8492100, 'h': 994199}
SPONSOR_IMAGE = {'x': 285750, 'y': 1167187, 'w': 8572500, 'h': 3600450}

# Content slide (with image)
CONTENT_TITLE = {'x': 306112, 'y': 112837, 'w': 8531700, 'h': 994199}
CONTENT_BODY  = {'x': 151256, 'y': 1107112, 'w': 6675300, 'h': 3910500}  # 26pt
CONTENT_IMAGE = {'x': 5791612, 'y': 1200412, 'w': 2614239, 'h': 2985862}

# Content slide (text only)
CONTENT_TITLE_ALT = {'x': 284662, 'y': 43275, 'w': 8492100, 'h': 994199}
CONTENT_BODY_ALT  = {'x': 284662, 'y': 1037550, 'w': 6944100, 'h': 3886200}  # 25-26pt

# Centered text slide
CENTER_TITLE = {'x': 1143000, 'y': 841774, 'w': 6858000, 'h': 1007400}
CENTER_BODY  = {'x': 1143000, 'y': 2334524, 'w': 6858000, 'h': 1608600}
```

---

## 7. Reference

| Resource | Location |
|----------|----------|
| Google API setup guide | `../../Ai Playground/FreedomLab/Google-API-Setup-Guide.md` |
| Auth script | `Presentation/google_slides_auth.py` |
| Deck builder | `Presentation/rebuild_deck.py` |
| Logo script | `Presentation/add_logos.py` |
| Ingestion checklist | `Presentation/Slide-Ingestion-Checklist.md` |
| Extraction script | `Presentation/extract_styles.py` |
| Extraction output | `Presentation/extract_styles_output.json` |
| Reference deck — 2025-02-19 | `1aMa0HkZXH928PrRJkWmhHIZzEe4iuQZlHFG0evN2m1k` |
| Reference deck — 2025-01-15 | `16cCbevm-E4bFNvv4J_XHXfIo6JD-YsorjXtfoLrCNXQ` |
| Reference deck — 2024-12-18 | `1NzXPWR3A5ONu9kxXV8aWEqrtEkWz1CNIUwGv0KJITEA` |
| Test deck (v2, outdated) | `1a9NXTsYIzEFi0mlJppk9Y0BaufEQikWh4ii2OBf3zTU` |

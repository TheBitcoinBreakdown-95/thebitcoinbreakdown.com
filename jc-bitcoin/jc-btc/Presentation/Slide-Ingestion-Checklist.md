# Slide Ingestion Checklist

Mandatory checklist for analyzing reference decks before building or updating the style guide. Every item must be captured with **exact values** — no guessing, no "looks like". Extract from the API, verify against thumbnails.

---

## Phase 1: Visual Inventory (Thumbnails First)

Before touching any API data, capture thumbnails of at least 5 slide types and answer:

- [ ] What is the dominant background color? Is it solid, gradient, or image-based?
- [ ] What is the primary text color? (Title text, body text — are they the same?)
- [ ] What is the accent color and where exactly is it used?
- [ ] Are there background images on slides? On all slides or just some?
- [ ] How many distinct layout patterns exist? Name each one.
- [ ] Does the deck use rectangles/shapes as content zones, or is content placed directly on the background?
- [ ] Are images used on content slides? Where are they positioned (left, right, full-bleed)?
- [ ] Is there a logo/watermark on interior slides? Where?
- [ ] What does the cover slide look like — logo-driven, text-driven, or image-driven?
- [ ] How dense are content slides? How many bullet points per slide?

**Key rule**: If the thumbnails show black backgrounds with orange text, the style guide should say "black backgrounds with orange text" — not "dark navy fallback with white text". Trust what you see.

---

## Phase 2: Theme & Master Extraction

- [ ] **Page background source**: Is it `solidFill`, `stretchedPictureFill`, or inherited from theme/master?
- [ ] **Theme colors**: What are the theme's default foreground and background colors?
- [ ] **Master slide elements**: Does the master define any persistent elements (logos, bars, footers)?
- [ ] **Inherited styles**: When elements return empty font/color sets, what do they inherit? (Check master text runs)

---

## Phase 3: Per-Layout Precise Measurements

For EACH distinct layout type, extract:

### Position & Size (EMU values)
- [ ] Slide dimensions (confirm 9144000 x 5143500 for 16:9)
- [ ] Each element's exact position: `translateX`, `translateY`
- [ ] Each element's actual size: `width * scaleX`, `height * scaleY`
- [ ] Relative positions (what percentage of slide width/height does each element occupy?)

### Text Properties
- [ ] Font family (explicit or inherited from theme?)
- [ ] Font size in PT (extract `fontSize.magnitude`)
- [ ] Text color (explicit RGB or theme color reference?)
- [ ] Bold / italic / underline
- [ ] Paragraph alignment (START, CENTER, END)
- [ ] Line spacing
- [ ] Bullet style (preset name, or custom glyphs?)
- [ ] Text direction and wrapping behavior

### Shape Properties
- [ ] Shape background fill color (or transparent?)
- [ ] Shape outline (rendered or NOT_RENDERED?)
- [ ] Corner radius (if applicable)
- [ ] Shadow effects

### Image Properties
- [ ] Position and size (EMU)
- [ ] Aspect ratio
- [ ] Is it a Drive-hosted image or embedded?
- [ ] Content role (logo, photo, screenshot, decorative?)

---

## Phase 4: Cross-Deck Consistency Check

When analyzing multiple reference decks:

- [ ] Which elements have **identical** positions across all decks? (These are templates)
- [ ] Which elements vary? (These are content-specific)
- [ ] Are slide structures reused verbatim? (e.g., same sponsor slide in all decks)
- [ ] What is the standard slide order pattern? (cover → sponsor → ? → agenda → content...)

---

## Phase 5: Color Audit

- [ ] List EVERY unique color found, with usage count and context
- [ ] Distinguish between: page backgrounds, shape fills, text colors, outline colors
- [ ] Note which colors are applied explicitly vs. inherited from theme
- [ ] Map: "this color is used for THIS purpose" — not just "this color exists"
- [ ] Compare what the API reports vs. what the thumbnail shows (theme inheritance can hide the real colors)

---

## Phase 6: Layout Classification

For each layout type discovered, document:

```
Layout name:
Slide indices where it appears:
Background: (color/image/theme)
Element count:
Element list:
  [0] type, position, size, purpose
  [1] type, position, size, purpose
  ...
Text hierarchy:
  Title: font, size, color, alignment, position
  Body: font, size, color, alignment, position
  Labels/footers: font, size, color, alignment, position
Image placement: (none / left / right / center / full-bleed)
```

---

## Phase 7: Validation Against Thumbnails

After completing the style guide:

- [ ] Build a test deck using the documented styles
- [ ] Capture thumbnails of the test deck
- [ ] Place test thumbnails side-by-side with reference thumbnails
- [ ] Check EACH of these against the reference:
  - Background color match?
  - Text color match?
  - Font appearance match?
  - Element positions match?
  - Overall visual weight and density match?
  - Image placement match (if applicable)?
- [ ] If anything doesn't match, trace it back to the extraction data and fix

---

## Common Mistakes to Avoid

1. **Inventing colors the deck doesn't use**: If the reference is black+orange, don't add navy/blue "fallbacks"
2. **Ignoring theme inheritance**: Empty font/color in API data doesn't mean "use defaults" — it means "uses theme values". Find what the theme sets.
3. **Over-engineering layouts**: If the reference uses 3 layout types, don't build 6. Match what exists.
4. **Wrong text color**: The most visible mistake. If body text is orange, body text is orange — not white.
5. **Missing images**: If content slides have images, image support is mandatory, not optional.
6. **Shape fills you invented**: Don't add background rectangles, divider bars, or zones that don't exist in the reference.
7. **Wrong font for body**: Extract which font is actually used for bullets. Don't assume.
8. **Font size too small**: Presentation text needs to be readable from the back of a room. 16pt body is too small if the reference uses 26pt.
9. **Measuring logo size wrong**: Extract the actual image dimensions from the API, don't guess from thumbnails.
10. **Ignoring the cover text box fill**: If the cover's text box has a white background fill, that's intentional design — don't make it transparent.

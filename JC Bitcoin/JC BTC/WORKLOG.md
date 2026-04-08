# WORKLOG

**Last saved:** 2026-04-04
**Status:** CRM built and seeded. 37 Bitcoin Park 2026 organizer contacts imported.

## Current State

### CRM (built 2026-04-04)
- **Repo:** `Jersey-City-Bitcoin/jcbtc-crm` (private) — live on GitHub
- **Local path:** `JC BTC/CRM/` (gitignored from public TBB repo)
- **Contacts:** 37 contacts from bp2026 organizer list (jcbtc-001 through jcbtc-037)
- **Scripts:** `import_luma.py`, `import_organizers.py`, `normalize.py`
- **Command:** `/import-contacts` — ad-hoc filing (natural language, CSV, vCard)

### Presentation Scripts (last worked 2026-03-06)
- `create_template.py` — working, builds correct 7-slide template deck
- `rebuild_deck.py` — still needs rewrite (uses wrong colors/fonts)
- `add_logos.py`, `google_slides_auth.py` — working

## Next
1. First Luma import — export attendees from meetup #5 or #6, drop in `CRM/sources/`, run `import_luma.py`
2. Migrate scattered contacts — `Notes/2023-2025/Names.md`, `Notes/Sponsorship/`, `Notes/Initiatives/Businesses.md`
3. Enrich existing 37 organizer contacts with emails/handles as acquired
4. Rewrite `rebuild_deck.py` using corrected styles from `create_template.py`

---

## Key Brand Data
<!-- protected -->

Verified via thumbnails + API master inspection (2026-03-06):

- **Background:** `#000000` black on ALL slides
- **Text color:** `#ff9900` orange for ALL text (titles, bullets, labels)
- **Font:** Calibri for everything (theme master sets it for TITLE and BODY)
- **Body text:** 25-26pt | **Title text:** ~36pt bold | **Splash divider:** 72pt bold centered
- **Cover:** logo centered + orange text on transparent box (`propertyState: NOT_RENDERED`)
- **Layout types:** 4 — cover, sponsor, content, splash
- No divider bars, background zones, watermarks, or footers

**Exact position constants (EMU):**
- Cover logo: (2437898, 90236), size 4268203 x 4268203
- Cover text box: (1142999, 3748440), size 6858000 x 1200000
- Content title: (306112, 112837), size 8531700 x 994199
- Content body: (151256, 1107112), size 6675300 x 3910500
- Content image: (5791612, 1200412), size 2614239 x 2985862

---

## Reference IDs
<!-- protected -->

- **Template deck:** `1Go3kE8H8w8pzrNRrXS1Jwd9t_Dmz5EtDxFkGEDfY2EI` (verified, current)
- **Logo (Drive):** `1XCi7pXbNwhX8VyVlF0XOmwV2_778xAA2` (circle, public)
- **Outdated test decks (do not use):**
  - v1: `1qRfJbAOMEYghweBug5mgf1fk0PxdqXIc2LgcJnN29l0`
  - v2: `1a9NXTsYIzEFi0mlJppk9Y0BaufEQikWh4ii2OBf3zTU`
  - bad template (white box, wrong font): `1xoHTrC_7NLfJI2itGeklUVXUEzzypuU2Sqs_SHW_FeM`

---

## Decisions
<!-- protected -->

- `#ff9900` for orange (matches existing decks — NOT Bitcoin standard `#f7931a`)
- Calibri is the ONLY font — titles, body, cover, splash, everything
- Cover text box is transparent (NOT white) — `propertyState: NOT_RENDERED`
- Black backgrounds with no fallback alternatives
- Always follow `Slide-Ingestion-Checklist.md` before modifying styles
- Always verify against thumbnails before declaring presentation work done
- CRM is a private repo inside Jersey-City-Bitcoin org (not in public TBB repo)
- Contact filenames: `firstname-lastname.md` (slugified). IDs: sequential `jcbtc-NNN`
- Raw import files (`*.csv`, `*.vcf`) are always gitignored — never committed
- Commit messages use event-level descriptions only — never individual names

---

## Session History
<!-- protected -->

**2026-03-06 — Presentation scripts**
- Created `create_template.py` — builds correct 7-slide template deck via Slides API
- First attempt had wrong font (Old Standard TT) and white cover box — caught via thumbnail comparison
- Extracted master/theme data: confirmed Calibri is ONLY font, cover text box is NOT_RENDERED
- Fixed: Calibri everywhere, transparent cover text box, 72pt splash (was 96pt, overflowed)
- Updated Slide-Style-Guide.md: corrected font section, cover text box, API constants
- Template deck verified: all 7 slides match reference style

**2026-04-03 — CRM build**
- Planned and built CRM: private GitHub repo `Jersey-City-Bitcoin/jcbtc-crm`
- TBB root `.gitignore` updated to exclude `JC BTC/CRM/` from public repo
- Built contact + event schema (YAML frontmatter Markdown), Luma CSV importer, organizer TSV importer, normalization utils
- Added `/import-contacts` Claude command
- Seeded with 37 contacts from Bitcoin Park 2026 organizer list

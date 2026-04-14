# WORKLOG

**Last saved:** 2026-04-11
**Status:** Website redesign brainstorm in progress. 8 mockup directions built. Deciding visual direction before implementation.

## Current State

### Website Redesign (active 2026-04-11)
- **Goal:** New website for JC Bitcoin, PR to new repo under Jersey-City-Bitcoin org
- **Mockups:** 8 HTML mockups in `Website/mockups/` (01 through 08)
- **Research done:** Competitive audit (jerseycitybitcoin.com, bitcoinpark.com, austinbitcoinclub.com, bitdevs.org), open-meetup template analysis (bitcoinbayfoundation/open-meetup -- Next.js/Tailwind)
- **Values decided:** Warmth + credibility for newcomers, story-first CTA ("learn what JC Bitcoin is"), both audiences (new + existing), no price talk
- **Directions explored:**
  - 01-03: Generic (clean community, dark luxury lite, dark warm hybrid) -- rejected as "vibecoded"
  - 04: Transit Map -- wayfinding/departure board concept (liked)
  - 05: Beer Hall Poster -- Oswald condensed, event poster energy (liked)
  - 06: Skyline Blueprint -- architectural/navy, JC coordinates
  - 07: Bodega Zine -- light background, newspaper layout, Fraunces serif
  - 08: Liberty Stencil -- logo-driven, Bebas Neue, Lady Liberty narrative (latest)
- **Tech stack:** TBD (Astro vs Jekyll vs fork open-meetup template)
- **Next:** User reviewing mockups 4-8, then pick direction and move to design doc + build

### CRM (built 2026-04-04)
- **Repo:** `Jersey-City-Bitcoin/jcbtc-crm` (private) -- live on GitHub
- **Local path:** `CRM/` (gitignored from public TBB repo)
- **Contacts:** 37 contacts from bp2026 organizer list (jcbtc-001 through jcbtc-037)

### Presentation Scripts (last worked 2026-03-06)
- `create_template.py` -- working
- `rebuild_deck.py` -- still needs rewrite

## Next
1. **Website:** Pick visual direction from mockups, write design doc, decide tech stack, build, open PR
2. First Luma import -- export attendees from meetup #5 or #6, drop in `CRM/sources/`, run `import_luma.py`
3. Migrate scattered contacts -- `Notes/2023-2025/Names.md`, `Notes/Sponsorship/`, `Notes/Initiatives/Businesses.md`
4. Enrich existing 37 organizer contacts with emails/handles as acquired
5. Rewrite `rebuild_deck.py` using corrected styles from `create_template.py`

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

**2026-04-11 — Website redesign brainstorm**
- User is now collaborator on Jersey-City-Bitcoin GitHub org, wants to build new site and PR it
- Ran KB search, competitive audit (4 live sites), explored open-meetup template (bitcoinbayfoundation)
- Values session: warmth + credibility, story-first, no price talk, both new and existing audiences
- Built 8 HTML mockup directions in `Website/mockups/`:
  - 01-03 rejected as generic "vibecoded" dark+orange templates
  - 04 Transit Map, 05 Beer Hall Poster, 06 Skyline Blueprint, 07 Bodega Zine, 08 Liberty Stencil
  - User liked Transit Map and Beer Hall concepts for being "out of the box"
  - Liberty Stencil (08) built from actual logo analysis: Bebas Neue, Lady Liberty narrative, orange strips
- Moved mockups from old spaced path (`JC Bitcoin/JC BTC/Website/`) to correct `jc-bitcoin/jc-btc/Website/`
- Session paused at: user reviewing mockups 4-8 to pick direction

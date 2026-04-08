# JC Bitcoin — Progress & Next Steps

## Completed

- [x] **CLAUDE.md overhaul** — Rewrote operating manual with project identity, vault conventions, content standards, sensitive content rules, and reusable template structure. Merged duplicate sections, removed redundancy with Claude Code defaults, fixed syntax errors. (2026-02-01)
- [x] **Vault structure planned and implemented** — Created 4 main directories (Website, CRM, Content, Notes) + Inbox. Updated CLAUDE.md Sections 1–3: expanded Purpose and What Claude Does Here, replaced old 10-folder numbered layout, removed predefined tag taxonomy, updated frontmatter types. (2026-02-02)
- [x] **Google Slides ingestion & tooling** — Extracted styles from 3 existing JC Bitcoin presentations via API. Updated Slide-Style-Guide.md with real data (fonts: Old Standard TT, Calibri, Arial; accent orange #ff9900; sizes 16-18pt body, 36pt title, 144pt cover). Created `rebuild_deck.py` (create new decks from JSON outlines or restyle existing), `add_logos.py`, and `extract_styles.py`. Verified end-to-end by creating a test deck with all 6 layout types. (2026-03-05)

---

## Next Steps

- [x] **CRM built** — Private repo `Jersey-City-Bitcoin/jcbtc-crm` created and initialized at `CRM/`. Schema (contacts + events), Luma CSV importer (`scripts/import_luma.py`), and `/import-contacts` Claude command. TBB root `.gitignore` updated to exclude CRM from public repo. (2026-04-03)
- [ ] **First CRM import** — Do a Luma export from meetup #5 or #6 and run `import_luma.py` to seed the contacts directory
- [ ] **Migrate scattered contacts** — Review `Notes/2023-2025/Names.md`, `Notes/Sponsorship/`, and `Notes/Initiatives/Businesses.md` for contact data to manually file via `/import-contacts`
- [ ] **Start populating the vault** — Begin creating notes in each directory based on upcoming initiatives, meetups, and content plans
- [x] **Logo extracted and uploaded** — Extracted logo from existing cover slide via Slides API, uploaded to Drive (`1XCi7pXbNwhX8VyVlF0XOmwV2_778xAA2`), tested on test deck with `add_logos.py`. Updated Style Guide. (2026-03-06)

---

## Backlog

- [ ] Delete `OPENING INSTRUCTIONS - Paste this.md` (no longer needed — Claude Code reads CLAUDE.md automatically)
- [ ] Set up `tasks/lessons.md` for cross-session learning log
- [ ] Evaluate MCP servers and external integrations for automation
- [ ] Initialize git repo for version control (enables worktrees, PRs, and change tracking)
- [ ] Create `docs/` spine files (PROJECT_OVERVIEW, ARCHITECTURE, DECISIONS, WORKFLOWS) as vault complexity grows

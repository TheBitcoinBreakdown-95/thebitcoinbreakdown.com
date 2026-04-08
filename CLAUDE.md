# CLAUDE.md -- Master Educational Hub

This file is the root authority for all educational projects in this repository. Each project has its own operating manual (linked below). This file covers project discovery, cross-cutting concerns, and shared infrastructure.

> **Session start reminder**: Check `WORKLOG.md` for where you left off. For specific projects, consult their operating manuals listed below.

---
---

# PART 1: PROJECT MAP

---

## 1. Identity

This is the master workspace for all educational content created by The Bitcoin Breakdown. It houses the website, a book, educational courses, community materials, and the tooling that ties them together.

### What Claude Does Here
- Build and maintain the TBB website (Astro, Obsidian, GitHub Actions)
- Write and edit Bitcoin educational content (blog posts, compendium, book)
- Develop standalone courses (Node SSH, AI onboarding, merchant guides)
- Support educator training projects (FreedomLab, AI Fluency)
- Manage community education materials (JC Bitcoin meetups)
- Maintain documentation, project context, and cross-session memory

### What Claude Does NOT Do Here
- Provide financial advice or investment recommendations
- Generate or handle private keys, seed phrases, or wallet credentials
- Push to GitHub or deploy without user confirmation
- Over-engineer or add features the user didn't ask for
- Create files unnecessarily -- prefer editing existing files

---

## 2. Projects

| Project | Directory | Operating Manual | Status |
|---------|-----------|-----------------|--------|
| **TBB Website** | `TBB/` + `astro/` | Section 5 below | LIVE at thebitcoinbreakdown.com |
| **TBB Media Company** | `TBB Media Company/` | `TBB Media Company/CLAUDE.md` | Active -- EP01 Golden Rules in production, 2112 LLC active |
| **WBIGAF Book** | `WBIGAF/` | `WBIGAF/WBIGAF.md` | Ch1-2 done, Ch3 in progress |
| **FreedomLab** | `FreedomLab/` | `FreedomLab/CLAUDE.md` | Skills built, slide deck active |
| **JC Bitcoin** | `JC Bitcoin/` | `JC Bitcoin/JC BTC/CLAUDE.md` | Active (vault + meetup materials) |
| **Node SSH Course** | `content/Node SSH/` | -- | 7/7 files written, review pending |
| **How to Learn and Do Anything** | `content/How to Learn and Do Anything/` | -- | Planning phase |
| **Merchants Onboarding Guide** | -- | -- | Not started |
| **AI Fluency for Educators** | `AI Fluency for educators/` | -- | Early stage (4 framework docs) |

### Inactive/Archive
| Directory | Notes |
|-----------|-------|
| `Automating TBB/` | Archived -- logo work moved to `TBB Media Company/brand/logo/` |
| `references/` | Claude Code best practices, supermemory docs |

---

## 3. Task Tracking

Each project tracks its own work. The master index:

| Project | Task File |
|---------|-----------|
| TBB Website | `tasks/TODO.md` |
| TBB Media Company | `tasks/TODO.md` (Phase 14) |
| WBIGAF Book | `WBIGAF/WBIGAF-Status.md` |
| FreedomLab | `FreedomLab/tasks/` |
| Content courses | `tasks/TODO.md` (Phase 12) |
| Cross-session log | `WORKLOG.md` |
| Lessons learned | `tasks/lessons.md` |

---

## 4. Infrastructure

| Component | Location | Purpose |
|-----------|----------|---------|
| GitHub Actions | `.github/workflows/deploy.yml` | Auto-build + FTP deploy to Hostinger on push |
| SSH access | `SSH Instructions.md` | Windows SSH to StartOS Bitcoin node |
| Scripts | `scripts/` | Build/deployment automation |
| References | `references/` | Claude Code best practices docs |

---
---

# PART 2: TBB WEBSITE

> This section covers the primary project -- thebitcoinbreakdown.com. For other projects, see their operating manuals in the project map above.

---

## 5. TBB Website Details

### Tech Stack
- **Obsidian** as the content editor (write posts in Markdown)
- **Astro** as the site generator (converts Markdown to HTML)
- **GitHub** for version control (open source)
- **Hostinger** for hosting (existing host, FTP deploy)
- **GitHub Actions** for auto-build and deploy on push

### Current Status (Mar 2026)
- **Site: LIVE** at thebitcoinbreakdown.com
- Site framework: COMPLETE (Astro v5.17.1, 55 pages, builds in ~7.8s)
- GitHub repo: `TheBitcoinBreakdown-95/thebitcoinbreakdown.com`
- Theme: V4 "Dark Luxury" COMPLETE
- WordPress migration: COMPLETE -- 28 posts + 5 pages, 2,316 images localized
- Deployment: GitHub Actions to FTP to Hostinger (auto-deploys on push)
- Compendium: 9 chapter landing pages, 21 sub-chapters (Ch1: 11, Ch2: 8, Ch3: 1, Ch4: 1)
- Homepage: 8 sections (Hero, Quote, Compendium tile, Featured Chapters, Stats, Terminal, Resources, Closer)

### Architecture

```
TBB/                         -- Obsidian vault (CONTENT)
  posts/                     -- Blog posts as Markdown
  guide/                     -- Compendium sub-chapters (21 files)
  pages/                     -- Static pages
  drafts/                    -- WIP (gitignored)
  templates/                 -- New post template

astro/                       -- Site generator
  src/styles/global.css      -- Colors, fonts, theme
  src/layouts/               -- Page templates
  src/components/            -- Header, footer, etc.
  src/pages/                 -- Routes
  src/scripts/interactions.js -- V4 JS effects
  src/data/chapters.ts       -- Shared chapter metadata
  src/content.config.ts      -- Content collection schemas
  public/images/             -- Localized images (~510 MB)
  public/.htaccess           -- Redirect rules
  dist/                      -- Built HTML (deployed to Hostinger)
```

### Key Files to Edit
| Change | File |
|--------|------|
| Colors/fonts/theme | `astro/src/styles/global.css` |
| Header/nav | `astro/src/components/Header.astro` |
| Footer | `astro/src/components/Footer.astro` |
| Homepage | `astro/src/pages/index.astro` |
| Blog post look | `astro/src/layouts/BlogPost.astro` |
| Compendium article look | `astro/src/pages/guide/[...slug].astro` |
| Compendium landing page | `astro/src/pages/guide/index.astro` |
| Chapter landing pages | `astro/src/pages/guide/chapter/[num].astro` |
| Shared chapter data | `astro/src/data/chapters.ts` |
| JS effects | `astro/src/scripts/interactions.js` |
| New blog post | `TBB/posts/YYYY/filename.md` |
| New compendium sub-chapter | `TBB/guide/filename.md` |

### Workflows

**Publishing a blog post:**
1. Create `TBB/posts/YYYY/slug-name.md` with standard frontmatter
2. Add images to `astro/public/images/YYYY/MM/`
3. Commit and push -- GitHub Actions auto-deploys (~40s)

**Publishing a compendium sub-chapter:**
1. Create/edit `TBB/guide/slug-name.md` with frontmatter (title, description, chapter, order, draft)
2. Commit and push -- auto-deploys
3. Sub-chapter appears on its chapter landing page (`/guide/chapter/N`)

### Content Conventions

**Frontmatter format:**
```yaml
---
title: "Post Title"
description: "SEO description (150-160 chars)"
pubDate: 2026-02-05
author: "The Bitcoin Breakdown"
tags: ["bitcoin"]
image: ""
draft: false
---
```

**Bitcoin terminology:**
- **Bitcoin** (capital B) = the network, protocol, and system
- **bitcoin** (lowercase b) = the unit of currency (BTC)
- Define technical terms on first use in educational content

**Tone:**
- Clear, accessible, non-intimidating
- Assume the reader is smart but new to the topic
- No jargon without explanation
- No price predictions or financial advice

### Commands
```bash
npm run dev      # Live preview at localhost:4321
npm run build    # Generate HTML to dist/
```

### What is Astro?
Astro converts Markdown files into HTML websites. Write header/footer once, reuse on all pages. Add new posts by creating simple Markdown files. Outputs plain HTML. The `node_modules` folder is auto-generated library code (never edit). The `dist` folder is the final HTML output deployed to Hostinger.

---
---

# PART 3: OPERATING PRINCIPLES

> General principles (verification, security, coding style, git workflow, subagents) are defined in workspace rules at `.claude/rules/`. The sections below cover project-specific details only.

---

## 6. Verification

- Run `npm run build` after any Astro file change to verify the site still builds
- Check that frontmatter, file placement, and naming follow content conventions
- For Bitcoin content: verify terminology matches conventions (capital B = network, lowercase b = currency)
- For other projects: defer to their operating manuals for verification steps

---

## 7. Task Management

### In-Session
- Use Claude Code's built-in todo system. Mark tasks complete as they are finished.

### Cross-Session
- Check the project map (section 3) for the right task file
- **Lessons log:** `tasks/lessons.md` -- update after any correction with what went wrong, the fix, and the date

### Execution Order
1. Check the relevant task tracker
2. Plan before implementing
3. Track progress -- mark items complete as you go
4. Capture lessons in `tasks/lessons.md` when corrections occur

---

## 8. Security

- NEVER generate, display, or store private keys, seed phrases, or wallet mnemonics
- NEVER include real wallet addresses belonging to individuals
- General security rules (secrets, credentials, OWASP) are in workspace `rules/security.md`

---

## 9. Self-Modification Rules

Claude may modify this CLAUDE.md when a mistake reveals a missing rule, a recurring failure appears, or a clarification would prevent future errors. Must disclose: what changed, why, and the new rule in plain language. Changes must be minimal and targeted.

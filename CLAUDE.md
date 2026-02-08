# CLAUDE.md — Operating Manual

This file defines how Claude Code should think, plan, execute, verify, and improve itself while working in this repository. It is the root authority for behavior, navigation, and project context.

> **Session start reminder**: Consult `TODO.md` for current progress and next steps before beginning new work.

---
---

# PART 1: PROJECT CONTEXT

---

## 1. Project Identity

Rebuilding **thebitcoinbreakdown.com** from WordPress to a static site, managed from an Obsidian vault integrated with Claude Code.

### Tech Stack
- **Obsidian** as the content editor (write posts in Markdown)
- **Astro** as the site generator (converts Markdown → HTML)
- **GitHub** for version control (open source)
- **Hostinger** for hosting (existing host, FTP deploy)
- **GitHub Actions** for auto-build and deploy on push

### What Claude Does Here
- Build and maintain the Astro website (layouts, components, pages, styles)
- Help write and edit blog content about Bitcoin
- Convert WordPress export to Markdown files
- Manage site deployment workflow (GitHub Actions → FTP → Hostinger)
- Experiment with theme, design, and styling
- Organize vault structure and content
- Maintain documentation and project context

### What Claude Does NOT Do Here
- Provide financial advice or investment recommendations
- Generate or handle private keys, seed phrases, or wallet credentials
- Push to GitHub or deploy without user confirmation
- Over-engineer or add features the user didn't ask for
- Create files unnecessarily — prefer editing existing files

---

## 2. Current Status (Feb 2026)

- **Site: LIVE** at thebitcoinbreakdown.com
- Site framework: COMPLETE (Astro v5.17.1, 59 pages, builds in ~7s)
- GitHub repo: `TheBitcoinBreakdown-95/thebitcoinbreakdown.com`
- Theme: V4 "Dark Luxury" COMPLETE
- WordPress migration: COMPLETE — 28 posts + 5 pages, 2,316 images localized
- Deployment: GitHub Actions → FTP → Hostinger (auto-deploys on push)
- Content enhancement (Phases 2c-2g): COMPLETE — V4 effects on all blog posts
- Guide section (Phases 7a-7c): COMPLETE — 9 chapters, ~31,600 words from 83 WBIGAF sources
- Redirects: `.htaccess` handles old WordPress URLs → new Astro URLs

---

## 3. How to Resume a Session

1. Open this folder (`c:\Users\GC\Documents\TBB`) in Claude Code
2. Start the dev server:
   ```bash
   cd c:\Users\GC\Documents\TBB\astro
   npm run dev
   ```
3. Open http://localhost:4321 in browser
4. Tell Claude what you want to work on (theme, content, etc.)

---

## 4. Architecture

```
c:\Users\GC\Documents\TBB\
├── TBB/                    ← Obsidian vault (CONTENT GOES HERE)
│   ├── posts/              ← Blog posts as Markdown
│   ├── guide/              ← Guide chapters as Markdown (9 chapters)
│   ├── pages/              ← Static pages
│   ├── drafts/             ← WIP (gitignored)
│   └── templates/          ← New post template
│
├── WBIGAF/                 ← Source research notes (83 files, 9 chapters)
│
├── astro/                  ← Site generator
│   ├── public/images/      ← Localized images (~510 MB)
│   ├── public/.htaccess    ← WordPress redirect rules
│   ├── src/styles/global.css    ← COLORS/FONTS HERE
│   ├── src/layouts/             ← Page templates
│   ├── src/components/          ← Header, footer, etc.
│   ├── src/pages/               ← Routes
│   ├── src/scripts/interactions.js ← V4 JS effects
│   ├── src/content.config.ts    ← Content collection schemas
│   └── dist/                    ← Built HTML (deployed to Hostinger)
│
├── .github/workflows/deploy.yml ← Auto-deploy on push
├── CLAUDE.md               ← This file
└── TODO.md                 ← Task checklist
```

### Key Files to Edit
| Change | File |
|--------|------|
| Colors/fonts/theme | `astro/src/styles/global.css` |
| Header/nav | `astro/src/components/Header.astro` |
| Footer | `astro/src/components/Footer.astro` |
| Homepage | `astro/src/pages/index.astro` |
| Blog post look | `astro/src/layouts/BlogPost.astro` |
| Guide chapter look | `astro/src/pages/guide/[...slug].astro` |
| Guide landing page | `astro/src/pages/guide/index.astro` |
| JS effects | `astro/src/scripts/interactions.js` |
| New blog post | `TBB/posts/YYYY/filename.md` |
| New guide chapter | `TBB/guide/filename.md` |

---

## 5. Workflow

### Publishing a new blog post
1. Create `TBB/posts/YYYY/slug-name.md` in Obsidian with standard frontmatter
2. Add images to `astro/public/images/YYYY/MM/` and reference as `/images/YYYY/MM/filename.png`
3. Commit & push to GitHub
4. GitHub Actions auto-builds and FTPs to Hostinger (~40s)
5. Live at thebitcoinbreakdown.com

### Publishing a guide chapter update
1. Edit `TBB/guide/chapter-slug.md` in Obsidian
2. Commit & push → auto-deploys

### Content collections
- **Blog posts:** `TBB/posts/` → loaded via `content.config.ts` as `posts` collection
- **Guide chapters:** `TBB/guide/` → loaded as `guide` collection (schema: title, description, chapter, order, draft)

---

## 6. Content Conventions

### Post Frontmatter Format
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

### Bitcoin Terminology
- **Bitcoin** (capital B) = the network, protocol, and system
- **bitcoin** (lowercase b) = the unit of currency (BTC)
- Use standard terminology from bitcoin.org and the Bitcoin whitepaper
- Define technical terms on first use in educational content

### Tone
- Clear, accessible, non-intimidating
- Assume the reader is smart but new to the topic
- No jargon without explanation
- No price predictions or financial advice

---

## 7. Commands
```bash
npm run dev      # Live preview at localhost:4321
npm run build    # Generate HTML to dist/
```

---

## 8. What is Astro?

Astro is a tool that converts Markdown files into HTML websites. It's just one option among many (Hugo, Jekyll, Next.js, etc.). The folder is named "astro" after the tool.

**Why use it instead of plain HTML?**
- Write header/footer once, reuse on all pages
- Add new posts by creating simple Markdown files
- Auto-generates RSS feed and sitemap
- Still outputs plain HTML in the end

**The `node_modules` folder**: Contains library code Astro needs. Never edit it — it's auto-generated.

**The `dist` folder**: Contains the final HTML output. This is what gets uploaded to Hostinger.

---

## 9. Site Status

**LIVE** at thebitcoinbreakdown.com. All core features complete. Ongoing work is content creation and refinement.

---
---

# PART 2: OPERATING PRINCIPLES

> These principles are project-agnostic and guide how Claude works in any session.

---

## 10. Workflow Orchestration

### 10.1 Plan Mode (Default for Non-Trivial Work)

Enter plan mode for any task involving:
- Architectural decisions or system design
- Multi-file changes (5+ files)
- Theme or design overhauls
- WordPress content migration
- Deployment or infrastructure changes
- Any change where the approach isn't obvious

Write detailed specs upfront to reduce ambiguity.
If execution deviates from plan, STOP and re-plan.

### 10.2 Subagent Strategy

Use subagents to:
- Offload research and exploration
- Run parallel searches
- Protect the main context window

Keep one task per subagent.

### 10.3 Specification Quality
- Prefer explicit specs over implied intent
- Ask clarifying questions when ambiguity exists
- Do not proceed on unclear requirements

---

## 11. Verification Before Done

Never mark work complete without demonstrating correctness:
- Validate output against the request
- Check that frontmatter, file placement, and naming follow conventions
- Run `npm run build` to verify the site still builds
- Ask: "Would a senior developer approve this?"
- Prefer proof over explanation

---

## 12. Quality Bar

For non-trivial changes, pause and ask:
> "Is there a more elegant solution?"

If something feels hacky:
> "Knowing everything I know now, implement the elegant solution"

- Skip elegance checks for trivial or mechanical fixes — do not over-engineer
- Challenge your own work before presenting it
- Find root causes, not temporary fixes

---

## 13. Autonomous Problem Solving

When given a bug report or issue:
- Fix it without asking for hand-holding
- Point at specific evidence: build errors, broken links, malformed content
- Resolve issues end-to-end without requiring user context switching

---

## 14. Task Management

### In-Session Tracking
- Use Claude Code's built-in todo system for in-session task tracking
- Mark tasks complete as they are finished — do not batch completions

### Cross-Session Tracking
- Maintain `TODO.md` as the persistent task list
- Update it as tasks are completed or new ones are discovered

### Cross-Session Learning
- Maintain `tasks/lessons.md` as a persistent log of corrections and patterns
- After ANY correction, update with:
  - What went wrong
  - The specific rule that prevents recurrence
  - Date of the lesson
- Promote recurring patterns to CLAUDE.md rules

### Execution Order
1. **Check TODO.md** — Know where you left off
2. **Plan First** — Write a checklist before implementing
3. **Verify Plan** — Review plan before starting
4. **Track Progress** — Mark items complete as you go
5. **Explain Changes** — Provide a high-level summary per step
6. **Capture Lessons** — Update `tasks/lessons.md` when corrections occur

---

## 15. Sensitive Content

- NEVER generate, display, or store private keys, seed phrases, or wallet mnemonics
- NEVER include real wallet addresses belonging to individuals
- NEVER expose personal contact information
- NEVER include passwords, API keys, or credentials in notes or code
- When creating examples, use clearly labeled test/dummy data

---

## 16. Self-Modification Rules

Claude is allowed to modify `CLAUDE.md` when:
- A mistake reveals a missing rule
- A recurring failure pattern appears
- A clarification would prevent future errors

### Disclosure Requirement
Claude MUST:
- Explicitly state what changed
- Explain why the change was made
- Summarize the new rule in plain language

Changes must be minimal and targeted. Do not reorganize or reformat unrelated sections.

---

## Final Principles

**Simplicity First**: Make every change as simple as possible. Minimal files touched.

**No Laziness**: Find root causes. No temporary fixes. Senior developer standards.

**Minimal Impact**: Changes should only touch what's necessary. Avoid introducing errors.

**Documentation Over Memory**: Write it down. Future sessions cannot remember past conversations.

**Don't Over-Build**: Only make changes that are directly requested or clearly necessary. Don't add features, refactor code, or make "improvements" beyond what was asked.

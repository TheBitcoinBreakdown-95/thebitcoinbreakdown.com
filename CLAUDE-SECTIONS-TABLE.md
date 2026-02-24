# CLAUDE.md Section Reference Table

| Section | Title | Purpose | Key Content |
|---------|-------|---------|-------------|
| **PART 1** | **PROJECT CONTEXT** | Project-specific information and configuration | Contains all details about The Bitcoin Breakdown website project |
| **1** | **Project Identity** | Define what the project is and the tech stack | Describes rebuilding thebitcoinbreakdown.com from WordPress to Astro static site. Lists tech stack (Obsidian, Astro, GitHub, Hostinger, GitHub Actions). Defines what Claude does and doesn't do in this project. |
| **2** | **Current Status** | Snapshot of project completion state | Documents live site status, completed phases, repo location, theme version (V4 "Dark Luxury"), WordPress migration completion (28 posts, 5 pages, 2,316 images), deployment method, and guide section (9 chapters, ~31,600 words). |
| **3** | **How to Resume a Session** | Quick-start instructions for new sessions | 4-step process: Open folder, start dev server (`npm run dev`), open localhost:4321, tell Claude what to work on. |
| **4** | **Architecture** | Complete project structure and file organization | Full directory tree showing TBB vault (content), WBIGAF (research), astro (site generator) folders. Includes "Key Files to Edit" table mapping common changes to specific files. |
| **5** | **Workflow** | Step-by-step processes for common tasks | Publishing blog posts (5 steps), publishing guide chapters (2 steps), content collections definition (posts and guide schemas). |
| **6** | **Content Conventions** | Standards for writing and formatting content | Post frontmatter YAML format, Bitcoin terminology rules (capital/lowercase B), tone guidelines (clear, accessible, no jargon, no financial advice). |
| **7** | **Commands** | Essential npm commands | `npm run dev` (local preview), `npm run build` (generate HTML). |
| **8** | **What is Astro?** | Explanation of the site generator tool | Plain-language explanation of what Astro does, why it's used instead of plain HTML, and what `node_modules` and `dist` folders contain. |
| **9** | **Site Status** | Current production status | One-line summary: LIVE at thebitcoinbreakdown.com, all core features complete, ongoing content work. |
| **PART 2** | **OPERATING PRINCIPLES** | Project-agnostic behavior rules | Universal rules for how Claude should work in any session, regardless of project. |
| **10** | **Workflow Orchestration** | How to approach and organize work | **10.1 Plan Mode**: When to enter plan mode (architectural decisions, multi-file changes, theme overhauls, etc.). **10.2 Subagent Strategy**: When and how to use subagents (research, parallel searches, context protection). **10.3 Specification Quality**: Preference for explicit specs, ask clarifying questions. |
| **11** | **Verification Before Done** | Quality control before marking tasks complete | Never mark complete without proof: validate output, check conventions, run `npm run build`, ask "Would a senior developer approve?", prefer proof over explanation. |
| **12** | **Quality Bar** | Standards for code quality and elegance | For non-trivial changes: pause and ask "Is there a more elegant solution?" Skip for trivial fixes. Challenge your own work. Find root causes, not temporary fixes. |
| **13** | **Autonomous Problem Solving** | How to handle bugs and issues | Fix without hand-holding, point at specific evidence, resolve end-to-end without requiring user context switching. |
| **14** | **Task Management** | System for tracking work across sessions | **In-Session Tracking**: Use built-in todo system, mark complete immediately. **Cross-Session Tracking**: Maintain TODO.md as persistent list. **Cross-Session Learning**: Maintain `tasks/lessons.md` for corrections and patterns. **Execution Order**: 6-step process from checking TODO.md to capturing lessons. |
| **15** | **Sensitive Content** | Security and privacy rules | NEVER generate/display private keys, seed phrases, wallet credentials, real wallet addresses, personal info, passwords, API keys. Use clearly labeled test data for examples. |
| **16** | **Self-Modification Rules** | When and how Claude can edit CLAUDE.md | Allowed when: mistake reveals missing rule, recurring failure pattern, clarification prevents errors. **Disclosure Requirement**: Must explicitly state changes, explain why, summarize new rule. Changes must be minimal and targeted. |
| **Final** | **Final Principles** | Core behavioral tenets | **Simplicity First**: Minimal changes. **No Laziness**: Root causes only. **Minimal Impact**: Touch only necessary files. **Documentation Over Memory**: Write it down. **Don't Over-Build**: Only what's requested. |

## Section Count Summary

- **Total Sections**: 16 numbered sections + Final Principles
- **Part 1 (Project Context)**: 9 sections (1-9)
- **Part 2 (Operating Principles)**: 7 sections (10-16) + Final Principles
- **Subsections**: 3 in Section 10 (Workflow Orchestration), 3 in Section 14 (Task Management)

## Navigation Quick Reference

| Need to find... | Go to Section |
|-----------------|---------------|
| What this project is | 1 - Project Identity |
| Current completion status | 2 - Current Status |
| How to start working | 3 - How to Resume a Session |
| Where files are located | 4 - Architecture |
| How to publish content | 5 - Workflow |
| Writing standards | 6 - Content Conventions |
| Terminal commands | 7 - Commands |
| What Astro is | 8 - What is Astro? |
| Is the site live? | 9 - Site Status |
| When to plan vs. execute | 10 - Workflow Orchestration |
| How to verify work is done | 11 - Verification Before Done |
| Code quality standards | 12 - Quality Bar |
| How to handle bugs | 13 - Autonomous Problem Solving |
| How to track tasks | 14 - Task Management |
| Security/privacy rules | 15 - Sensitive Content |
| Can Claude edit CLAUDE.md? | 16 - Self-Modification Rules |
| Core working principles | Final Principles |

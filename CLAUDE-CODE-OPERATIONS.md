# Claude Code Operations Whitepaper

**A one-stop reference for working with Claude Code on The Bitcoin Breakdown project.**

Last updated: February 18, 2026

---

## Table of Contents

1. [The System We Built](#the-system-we-built)
2. [How to Start a Session](#how-to-start-a-session)
3. [How to End a Session](#how-to-end-a-session)
4. [File Map: What Controls What](#file-map-what-controls-what)
5. [Permissions: How They Work](#permissions-how-they-work)
6. [MCP Servers: What They Do](#mcp-servers-what-they-do)
7. [Commands, Skills, and Agents](#commands-skills-and-agents)
8. [Slash Commands Quick Reference](#slash-commands-quick-reference)
9. [Keyboard Shortcuts](#keyboard-shortcuts)
10. [Best Practices: Working With Claude](#best-practices-working-with-claude)
11. [Best Practices: Prompting](#best-practices-prompting)
12. [Best Practices: Context Management](#best-practices-context-management)
13. [Best Practices: Debugging](#best-practices-debugging)
14. [The CLAUDE.md Philosophy](#the-claudemd-philosophy)
15. [Settings Reference](#settings-reference)
16. [Our Two-Project Architecture](#our-two-project-architecture)
17. [Lessons Learned](#lessons-learned)
18. [Reference Library](#reference-library)

---

## The System We Built

This project uses a **proprietary multi-document system** for managing Claude Code across sessions. Here's how the pieces fit together:

```
┌─────────────────────────────────────────────────────┐
│                   SESSION START                      │
│                                                      │
│   CLAUDE.md ──── Machine operating manual            │
│       │          (Claude reads this automatically)   │
│       │                                              │
│   MEMORY.md ──── Persistent cross-session memory     │
│       │          (Claude reads this automatically)   │
│       │                                              │
│   TODO.md ────── Website task checklist              │
│       │          (Claude checks on request)          │
│       │                                              │
│   WBIGAF.md ──── Book project operating manual       │
│       │          (Claude reads for book work)        │
│       │                                              │
│   lessons.md ─── Correction log                      │
│                  (prevents repeated mistakes)         │
└─────────────────┬───────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────┐
│                   SESSION END                        │
│                                                      │
│   /transition ── Updates all 4 docs + generates      │
│                  a one-sentence handoff prompt        │
│                  for the next session                 │
└─────────────────────────────────────────────────────┘
```

**Why this works:**
- Claude has no memory between sessions — every session starts fresh
- CLAUDE.md and MEMORY.md are loaded automatically at session start
- The `/transition` command ensures nothing is lost between sessions
- `lessons.md` prevents the same mistake from happening twice
- The system is version-controlled, free, and fully under your control

---

## How to Start a Session

1. **Open the TBB folder** in Claude Code (VSCode extension or terminal)
2. Claude automatically reads `CLAUDE.md` and `MEMORY.md`
3. Tell Claude what you want to work on:
   - For website work: "Check TODO.md and continue"
   - For book work: "Read WBIGAF.md and continue from where we left off"
4. **Start the dev server** if doing website work:
   ```bash
   cd astro && npm run dev
   ```

**Pro tip:** Paste the transition prompt from the previous session to give Claude exact context on where to pick up.

---

## How to End a Session

Type `/transition` (or say "Transition"). Claude will:

1. Read all 4 status documents
2. Update each one to reflect what was accomplished
3. Generate a **one-sentence transition prompt** — copy this and paste it at the start of your next session

**Never close a session without running /transition.** This is how institutional memory survives.

---

## File Map: What Controls What

### Machine-Readable Files (Claude reads these)

| File | Purpose | Auto-loaded? |
|------|---------|-------------|
| `CLAUDE.md` | Operating manual — tells Claude how to behave, project architecture, conventions | Yes |
| `MEMORY.md` | Cross-session memory — current state, completed phases, technical notes | Yes |
| `tasks/TODO.md` | Website task checklist (Phases 1-10+) | On request |
| `tasks/lessons.md` | Correction log — prevents repeated mistakes | On request |
| `WBIGAF/WBIGAF.md` | Book project operating manual — pipeline steps, conventions | On request |
| `WBIGAF/WBIGAF-Status.md` | Book progress tracker — chapter/step status | On request |

### Configuration Files

| File | Purpose | Checked into git? |
|------|---------|-------------------|
| `.claude/settings.local.json` | Project permissions, output style, MCP permissions | No (gitignored) |
| `.claude/settings.json` | Team-shared settings (if you ever have collaborators) | Yes |
| `~/.claude/settings.json` | Global personal settings (applies to all projects) | N/A |
| `.mcp.json` | MCP server definitions (Context7, DeepWiki) | Yes |
| `.claude/commands/transition.md` | The `/transition` command definition | Yes |

### Reference Material

| File | Purpose |
|------|---------|
| `references/claude-code-best-practice/` | Best practices repo (gitignored, local only) |
| `references/claude-supermemory/` | Memory patterns repo (gitignored, local only) |
| `README.md` | Public-facing project description |
| `CLAUDE-CODE-OPERATIONS.md` | This document |

---

## Permissions: How They Work

Claude Code has a permission system that controls what tools it can use without asking. Permissions live in `.claude/settings.local.json`.

### Our Current Setup (32 wildcard entries)

Instead of individually approving every command (which grew to 98 entries over time), we use wildcards:

```
Bash(git *)        ← All git commands
Bash(npm *)        ← All npm commands
Bash(node *)       ← All node commands
WebFetch(domain:*) ← All web fetches
mcp__context7__*   ← All Context7 MCP tools
mcp__deepwiki__*   ← All DeepWiki MCP tools
```

### The 5-Level Settings Hierarchy

Settings override each other in this order (highest priority first):

1. **Command line flags** — single-session overrides
2. **`.claude/settings.local.json`** — personal project settings (gitignored)
3. **`.claude/settings.json`** — team-shared project settings (committed)
4. **`~/.claude/settings.local.json`** — personal global overrides
5. **`~/.claude/settings.json`** — global personal defaults

**Important:** `deny` rules always win, regardless of where they're defined. A `deny` in settings level 5 overrides an `allow` in level 1.

### Permission Syntax

| Tool | Syntax | Example |
|------|--------|---------|
| Bash | `Bash(pattern)` | `Bash(git *)`, `Bash(npm run *)` |
| WebFetch | `WebFetch(domain:pattern)` | `WebFetch(domain:*)` |
| Edit | `Edit(path pattern)` | `Edit(src/**)` |
| Read | `Read(path pattern)` | `Read(.env)` |
| MCP | `mcp__server__tool` | `mcp__context7__*` |

---

## MCP Servers: What They Do

MCP (Model Context Protocol) servers give Claude access to external tools. We have two configured in `.mcp.json`:

### Context7
- **What:** Fetches up-to-date documentation for any library (Astro, npm packages, etc.)
- **Why:** Prevents Claude from hallucinating outdated APIs. When Claude needs to use an Astro feature, it can check the actual current docs instead of relying on training data.
- **How it runs:** Locally via `npx` — no API key needed.

### DeepWiki
- **What:** Provides structured wiki-style documentation for any GitHub repository.
- **Why:** When researching a dependency or looking at another project's architecture, Claude can get a structured overview instead of reading raw code.
- **How it runs:** Remote server at `mcp.deepwiki.com` — no API key needed.

### Adding More MCPs Later

Edit `.mcp.json` to add servers. The format is:

```json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "@package/name"]
    }
  }
}
```

Then add `"mcp__server-name__*"` to your permissions in `.claude/settings.local.json`.

**Recommended MCPs to consider later:**
- **Playwright** — browser automation for testing web pages
- **Claude in Chrome** — connects Claude to your real Chrome browser for debugging

---

## Commands, Skills, and Agents

### Commands (`.claude/commands/`)

Commands are markdown files that define workflows you trigger with `/command-name`.

**Our commands:**
- `/transition` — end-of-session handoff (updates status docs, generates transition prompt)

**How to create a new command:**
1. Create a file in `.claude/commands/your-command.md`
2. Add YAML frontmatter with `description` (and optionally `model`)
3. Write the workflow instructions in markdown
4. Invoke with `/your-command` in the chat

### Skills (`.claude/skills/`)

Skills are like commands but with additional features — supporting files, invocation control, and subagent execution. We don't use custom skills yet, but they're available if a workflow becomes complex enough to warrant one.

### Agents (`.claude/agents/`)

Custom agents are isolated Claude instances with their own tools, permissions, and model. We don't use custom agents yet — vanilla Claude Code is better for our workflow size.

**When to consider agents:** If you have a multi-step workflow that needs different tool permissions or a different model (e.g., using Haiku for fast research, Opus for writing).

---

## Slash Commands Quick Reference

### Most Useful (use these regularly)

| Command | What it does |
|---------|-------------|
| `/transition` | **Our custom command** — end-of-session handoff |
| `/compact` | Compress conversation to free context. Do this manually at ~50% |
| `/context` | Visualize how much context window is used |
| `/cost` | Show token usage and spending for this session |
| `/model` | Switch models or adjust effort level |
| `/plan` | Enter read-only planning mode |
| `/fast` | Toggle fast output mode (same model, faster) |

### Configuration (one-time setup)

| Command | What it does |
|---------|-------------|
| `/config` | Open interactive settings UI |
| `/permissions` | View or update tool permissions |
| `/statusline` | Set up the status line (shows model, context, cost) |
| `/terminal-setup` | Enable shift+enter for newlines |
| `/keybindings` | Customize keyboard shortcuts |
| `/sandbox` | Enable file/network sandboxing |

### Diagnostics

| Command | What it does |
|---------|-------------|
| `/doctor` | Check installation health |
| `/debug` | Troubleshoot current session |
| `/tasks` | List background tasks |
| `/help` | Show all available commands |

### Session Management

| Command | What it does |
|---------|-------------|
| `/clear` | Clear conversation and start fresh |
| `/resume` | Resume a previous session |
| `/rewind` | Go back to an earlier point in conversation |
| `/fork` | Branch the current conversation into a new session |
| `/export` | Export conversation to a file |

---

## Keyboard Shortcuts

### Essential

| Shortcut | What it does |
|----------|-------------|
| `Ctrl+C` | Cancel current generation |
| `Ctrl+D` | Exit Claude Code |
| `Esc Esc` | Rewind conversation |
| `Ctrl+L` | Clear terminal screen |

### Model & Mode

| Shortcut | What it does |
|----------|-------------|
| `Alt+P` | Switch model |
| `Alt+T` | Toggle extended thinking |
| `Shift+Tab` | Toggle permission modes |
| `Ctrl+T` | Toggle task list |

### Text Input

| Shortcut | What it does |
|----------|-------------|
| `\` + Enter | Multiline input |
| `Shift+Enter` | Multiline (requires `/terminal-setup`) |
| `Ctrl+G` | Open prompt in text editor |

---

## Best Practices: Working With Claude

These are distilled from the claude-code-best-practice repo (2,700+ stars), Boris Cherny's tips (Claude Code creator), and our own experience.

### The Golden Rules

1. **CLAUDE.md should stay under 150 lines.** Ours is ~140. Longer files get less reliable adherence.

2. **Vanilla Claude Code beats complex workflows.** Don't over-engineer with agents, skills, and hooks unless you have a clear need. Simple prompting + good documentation is usually enough.

3. **Commit often.** After every completed task, commit immediately. Don't batch up work.

4. **Always start with plan mode for non-trivial work.** Say "plan this" or use `/plan` before implementing. It's cheaper to fix a plan than to fix code.

5. **Keep subtasks small enough to complete in <50% context.** If a task is too big, break it down. You never want to hit the context limit mid-task.

6. **Compact at 50%, not 95%.** Use `/compact` proactively. Run `/context` to check your usage. Don't wait for the auto-compaction — it loses more information.

7. **Run long commands as background tasks.** This gives you better log visibility and doesn't block the conversation.

8. **Verify before marking done.** Always run `npm run build` after website changes. Check the output. "Would a senior developer approve this?"

9. **Provide screenshots when reporting visual bugs.** Claude can see images — paste them directly.

### What Makes a Good Prompt

- **Be specific.** "Fix the blog layout" is vague. "The blog post heading overlaps the navigation bar on mobile widths below 480px" is actionable.
- **Reference files by name.** "Update the header component" is better than "update the header."
- **State the goal, not just the action.** "Make the terminal section load faster — it currently takes 3s to appear" gives Claude room to find the best solution.
- **Paste error messages.** Don't describe errors — paste the actual text.

### What to Avoid

- **Don't say "make it better."** Be specific about what "better" means.
- **Don't approve changes you haven't read.** Claude can make mistakes. Review diffs.
- **Don't let context bloat.** If you've been in one session for hours and it's getting slow or forgetful, run `/transition` and start fresh.
- **Don't ask Claude to remember things.** It can't. Use the documentation system instead.

---

## Best Practices: Context Management

Context is the #1 resource in any Claude Code session. Everything Claude has read, written, or been told takes up space in the context window. When it fills up, Claude starts forgetting or making mistakes.

### How Context Works

- Claude's context window is like a fixed-size whiteboard
- Every message, file read, tool output, and response takes up space
- When it fills up, auto-compaction kicks in — but loses detail
- The goal is to stay under 50% as long as possible

### Context Hygiene

| Do | Don't |
|----|-------|
| Read specific files by name | Ask Claude to "look through the whole project" |
| Use `/compact` at 50% with instructions | Wait for auto-compaction at 95% |
| Run `/context` periodically to check usage | Ignore context until things break |
| Start fresh sessions for unrelated tasks | Cram everything into one session |
| Use the transition system to carry state | Try to keep one session alive forever |

### The `/compact` Command

When compacting, give instructions about what to remember:

```
/compact Focus on the WBIGAF Ch3.2 work — keep the block structure,
bibliography sources, and current step number. Drop the website discussion.
```

This produces a much better compaction than just `/compact` alone.

---

## Best Practices: Debugging

1. **Use `/doctor` first.** It catches config issues, unreachable permissions, and update problems.

2. **Run terminal commands as background tasks.** Instead of running a build in the foreground, use background execution for better log capture.

3. **Paste the actual error.** Screenshots of errors are good. Pasted text is better (Claude can search for it).

4. **Check the deploy.** After every `git push`, verify the GitHub Actions run succeeded with `gh run list --limit 1`.

5. **Use MCP servers for research.** Context7 prevents hallucinated library APIs. DeepWiki helps understand unfamiliar repos.

---

## The CLAUDE.md Philosophy

`CLAUDE.md` is the single most important file in the project. It's the operating manual that Claude reads at the start of every session.

### What Goes in CLAUDE.md

- **Project identity** — what this project is, what Claude does and doesn't do here
- **Current status** — what's live, what's in progress
- **Architecture** — folder structure, key files, how things connect
- **Conventions** — frontmatter formats, naming patterns, terminology rules
- **Workflow** — how to publish posts, run builds, deploy

### What Does NOT Go in CLAUDE.md

- Session-specific context (that's what MEMORY.md is for)
- Long reference material (link to it instead)
- Behavioral rules that apply to all projects (put those in `~/.claude/CLAUDE.md`)

### The 150-Line Rule

Keep CLAUDE.md under 150 lines. Beyond that, Claude's adherence drops. If you need more context, use:
- `MEMORY.md` for cross-session state
- `.claude/rules/*.md` for topic-specific rules
- Separate docs that Claude reads on demand (like `WBIGAF/WBIGAF.md`)

---

## Settings Reference

### Our Project Settings (`.claude/settings.local.json`)

```json
{
  "outputStyle": "Explanatory",
  "permissions": {
    "allow": [
      "Bash(git *)", "Bash(npm *)", "Bash(npx *)", "Bash(node *)",
      "Bash(python *)", "Bash(python3 *)", "Bash(pip *)", "Bash(gh *)",
      "Bash(wc *)", "Bash(sort *)", "Bash(ls *)", "Bash(dir *)",
      "Bash(cat *)", "Bash(grep *)", "Bash(find *)", "Bash(echo *)",
      "Bash(printf *)", "Bash(powershell *)", "Bash(curl *)",
      "Bash(claude *)", "Bash(xxd *)", "Bash(netstat *)",
      "Bash(findstr *)", "Bash(taskkill *)", "Bash(move *)",
      "Bash(for *)", "Bash(timeout *)", "Bash(where *)",
      "Bash(xargs *)", "Bash(mkdir *)", "Bash(copy *)",
      "WebFetch(domain:*)",
      "mcp__context7__*", "mcp__deepwiki__*"
    ]
  }
}
```

### Key Settings You Can Change

| Setting | What it does | How to set |
|---------|-------------|-----------|
| `outputStyle` | Claude's response tone | `"Explanatory"`, `"Learning"`, or `"default"` |
| `model` | Default model | `"opus"`, `"sonnet"`, `"haiku"` |
| `plansDirectory` | Where plan files go | Default: `.claude/plans/` |
| `statusLine` | Status bar content | Run `/statusline` to configure |
| `alwaysThinkingEnabled` | Extended reasoning | `true` or `false` |

### Output Styles Explained

| Style | Best for |
|-------|---------|
| **Explanatory** | Learning a codebase, understanding decisions. Claude explains its reasoning. *(Current setting)* |
| **Learning** | Being coached through code changes. Claude teaches as it works. |
| **Default** | Standard responses. Minimal explanation. |
| **Custom** | Define your own tone via `/config`. |

---

## Our Two-Project Architecture

This repo contains two distinct projects with separate tracking systems:

### Website (thebitcoinbreakdown.com)

| Component | File |
|-----------|------|
| Operating manual | `CLAUDE.md` |
| Task tracker | `tasks/TODO.md` |
| Correction log | `tasks/lessons.md` |
| Start command | "Check TODO.md and continue" |

### WBIGAF Book

| Component | File |
|-----------|------|
| Operating manual | `WBIGAF/WBIGAF.md` |
| Progress tracker | `WBIGAF/WBIGAF-Status.md` |
| Per-chapter handoff | `WBIGAF/[chapter]/Chapter N Metadata/transition-chN.md` |
| Start command | "Read WBIGAF.md and continue from where we left off" |

### How They Stay Separate

- `CLAUDE.md` tells Claude which project system to check based on what you ask for
- The `/transition` command updates both systems at session end
- `MEMORY.md` tracks high-level state for both projects
- Each project has its own operating manual with its own conventions

---

## Lessons Learned

These are patterns discovered through real mistakes. Each one produced a rule that prevents recurrence.

1. **Always look at existing content before building.** Don't build a replacement without understanding what you're replacing.

2. **Explain tools before using them.** When introducing a framework or tool, explain what it is before creating files.

3. **Astro glob paths are relative to the project root** (`astro/`), not the file's directory.

4. **Match reference implementations exactly.** When a reference exists, copy the algorithm line-by-line. Don't paraphrase math.

5. **FTP deploys need retry logic.** Transient failures are common with shared hosting. The workflow should self-heal.

6. **Verify deploy status after every push.** Don't wait for the user to discover failures.

Full log: `tasks/lessons.md`

---

## Reference Library

Two repositories are cloned in `references/` (gitignored — local only, not pushed to GitHub):

### claude-code-best-practice

Best files to re-read when you need a refresher:

| File | Content |
|------|---------|
| `reports/claude-boris-tips-feb-26.md` | 12 tips from the Claude Code creator |
| `reports/claude-settings.md` | All 37 settings explained with examples |
| `reports/claude-commands.md` | Every slash command documented |
| `reports/claude-agent-memory.md` | How persistent memory scopes work |
| `CLAUDE.md` | Advanced config example (agents, skills, hooks) |
| `README.md` | "MY EXPERIENCE" section — real-world workflow advice |

### claude-supermemory

Cloned for pattern reference only (we don't use the paid subscription). Useful for:
- How to organize memories by project using container tags
- Signal extraction keywords (what's worth saving)
- Conversation transcript formatting patterns

### Keeping References Updated

```bash
cd references/claude-code-best-practice && git pull
cd ../claude-supermemory && git pull
```

---

## One-Time Setup Checklist

Things to do once (most are already done):

- [x] Clone reference repos to `references/`
- [x] Consolidate permissions to wildcard patterns
- [x] Create `/transition` command
- [x] Configure Context7 + DeepWiki MCP servers
- [x] Set output style to Explanatory
- [ ] Run `/statusline` to enable status bar (shows model, context %, cost)
- [ ] Run `/terminal-setup` if using IDE terminal (enables shift+enter for multiline)
- [ ] Consider `/sandbox` for file/network isolation

---

*This document is for human reference. Claude reads `CLAUDE.md` and `MEMORY.md` — not this file.*

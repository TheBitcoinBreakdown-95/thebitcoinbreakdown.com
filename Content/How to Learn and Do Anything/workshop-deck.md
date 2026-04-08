---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Inter:wght@300;400;600;700&family=Playfair+Display:wght@400;600;700&display=swap');
  :root {
    --bg: #0A0A0A;
    --surface: #141414;
    --gold: #FFD700;
    --gold-muted: #C9A84C;
    --gold-dim: rgba(255, 215, 0, 0.15);
    --text: #E8E4DC;
    --text-secondary: #8A857D;
    --text-muted: #5A5650;
    --amber: #D4A853;
    --red: #C84B31;
    --green: #4A8B6E;
  }

  section {
    font-family: 'Inter', 'Segoe UI', Arial, sans-serif;
    color: var(--text);
    padding: 50px 70px;
    line-height: 1.6;
    background-color: var(--bg);
    border-top: 2px solid var(--gold-dim);
  }

  h1 {
    font-family: 'Playfair Display', Georgia, serif;
    color: var(--gold);
    font-weight: 700;
    font-size: 2.4em;
    margin-bottom: 0.3em;
    line-height: 1.15;
  }
  h2 {
    font-family: 'Playfair Display', Georgia, serif;
    color: var(--gold-muted);
    font-weight: 600;
    font-size: 1.6em;
    margin-bottom: 0.5em;
    padding-bottom: 6px;
    border-bottom: 2px solid var(--gold-dim);
  }
  h3 {
    font-family: 'Inter', Arial, sans-serif;
    color: var(--amber);
    font-weight: 600;
    font-size: 1.15em;
    margin-bottom: 0.3em;
  }
  p { margin-bottom: 0.5em; }
  strong { color: var(--gold); }
  em { color: var(--text-secondary); font-style: italic; }

  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.85em;
    margin-top: 0.5em;
  }
  th {
    background: var(--surface);
    color: var(--gold-muted);
    padding: 10px 14px;
    text-align: left;
    border-bottom: 2px solid var(--gold-dim);
    font-weight: 600;
  }
  td {
    padding: 8px 14px;
    border-bottom: 1px solid rgba(255,255,255,0.06);
  }

  blockquote {
    border-left: 3px solid var(--gold-muted);
    background: var(--surface);
    padding: 14px 20px;
    margin: 12px 0;
    border-radius: 0 6px 6px 0;
    font-size: 0.95em;
  }
  blockquote p { margin: 0; }

  code {
    font-family: 'JetBrains Mono', monospace;
    background: var(--surface);
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 0.85em;
    color: var(--gold-muted);
  }

  ul, ol { margin-top: 0.3em; }
  li { margin-bottom: 0.35em; }

  /* Slide type classes */
  section.title {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    background: linear-gradient(135deg, var(--bg) 0%, #1a1400 50%, var(--bg) 100%);
    border-top: 3px solid var(--gold);
  }
  section.title h1 { font-size: 3em; margin-bottom: 0.15em; }
  section.title h3 { color: var(--text-secondary); font-weight: 300; font-size: 1.3em; }

  section.section-break {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    background: linear-gradient(135deg, var(--bg) 0%, #0d0d00 100%);
    border-top: 3px solid var(--gold-muted);
  }
  section.section-break h1 { font-size: 2.6em; }

  section.activity {
    border-left: 4px solid var(--amber);
    padding-left: 66px;
  }

  section.warning {
    border-left: 4px solid var(--red);
    padding-left: 66px;
  }

  section.takeaway {
    border-top: 4px solid var(--gold);
    background: linear-gradient(180deg, rgba(255,215,0,0.03) 0%, var(--bg) 30%);
  }

  footer {
    font-size: 0.65em;
    color: var(--text-muted);
  }

---

<!-- _class: title -->
<!-- _paginate: false -->

# Your Agent Control Center

### Stop Vibing. Start Directing.

*The Bitcoin Breakdown*

---

## What We're Building Today

An **Agent Control Center** is three things working together:

1. **VS Code** -- a free program that shows your files
2. **Claude Code** -- an AI agent that understands English
3. **Your folders** -- real files on your real computer

You type what you want. In English. Files appear on your computer. You own them.

This is not a chatbot. This is a workspace.

---

## The Spectrum

| | Vibing | Vibe Coding | Directing |
|---|---|---|---|
| **What it is** | Chatting with AI in a browser | Letting AI write code | Directing AI from your desktop |
| **Where it lives** | Browser tab | Code editor | Your file system |
| **What you get** | Chat history (trapped) | Source code | Real files in your folders |
| **When you close it** | Gone | Code remains | Everything remains |
| **Builds over time** | No | No | Yes |

**Most people are stuck on level one.** Today you're going to level three.

---

## You Already Know How to Do This

The skill is **talking clearly**. Not coding. Not "prompt engineering."

If you can explain what you want to a coworker, you can direct an AI agent.

> "I'm planning a monthly meetup. I need a logistics plan, three session agendas, and a budget. Put everything in organized files."

That's it. You describe. The agent builds. You review. You redirect.

**The thinking is yours. The speed is the AI's.**

---

<!-- _class: section-break -->

# Let's Install It
### ~10-15 minutes

---

<!-- _class: activity -->

## Step 1: Install VS Code

Go to **code.visualstudio.com**. Click the download button.

- **Windows:** Run the installer. Defaults are fine. Check "Add to PATH."
- **Mac:** Download, unzip, drag to Applications. Click Open if macOS warns you.
- **Linux:** Download .deb or .rpm. Install via package manager.

Open VS Code when it's done. You'll see a sidebar, a big empty area, and a welcome tab you can close.

*Raise your hand if you're stuck. We'll come around.*

---

<!-- _class: activity -->

## Step 2: Install the Claude Code Extension

1. Click the **Extensions** icon in the sidebar (four squares)
2. Search for **"Claude Code"**
3. Find the one by **Anthropic** -- that's the official one
4. Click **Install**

A new Claude icon appears in your sidebar.

---

<!-- _class: activity -->

## Step 3: Sign In

1. Click the **Claude icon** in the sidebar
2. Click **Sign In** -- your browser opens
3. Log in to **claude.ai** with your Pro account ($20/month)
4. Come back to VS Code. You're connected.

**Important:** claude.ai (the website) is the chatbot. Claude Code (in VS Code) is the agent. Same company, different experience. The website is vibing. VS Code is directing.

---

<!-- _class: activity -->

## Step 4: Your First Conversation

1. Create a folder on your computer: **"My Agent Control Center"**
2. In VS Code: **File > Open Folder** -- select it
3. Click the Claude icon. Type this:

> Hello, can you create a file called hello.md with a short introduction about what this workspace is for?

4. Claude asks permission to create a file. Click **Allow.**
5. Watch the file appear in your sidebar. Click it. Read it.

**You just directed an AI agent from your desktop.** That file is on your computer. Not trapped in a chat log.

---

<!-- _class: section-break -->

# Now Do Something Real
### ~10-15 minutes

---

## Pick Something You Actually Need

Not a test. Not "Hello World." Something real.

- A plan you haven't made
- Research you've been putting off
- A letter you haven't written
- A comparison you need to make
- A budget for an upcoming event
- A guide you wish existed

**Pick one now.** Something specific. Something you'll actually use.

---

<!-- _class: activity -->

## Start Talking

Describe your project the way you'd brief a smart assistant on their first day.

> "I need to understand how property taxes work in New Jersey. I just bought my first house and I have no idea what to expect. Create a plain-English guide covering what I'll owe, when it's due, how assessments work, and what I can do if I think it's wrong."

Or:

> "I run a small landscaping business. Create a business plan outline using my actual details: 15 regular clients, two employees, expanding into commercial next year."

**Be specific.** The more detail you give, the better the first draft.

---

## Direct the Revision

Read what Claude created. Some will be right. Some won't.

**Don't just accept it.** This isn't vibing. Find what's off. Be specific:

> "The budget is missing food costs. Add a section for meals."

> "This is too generic. Use the actual details I gave you."

The file updates on your computer. Not a new chat message -- the actual file.

**This is the workflow.** Direct. Review. Redirect. Files get better each pass.

---

## It Reads What's Already There

When you open a folder, the agent can see **everything in it**.

Got existing notes? Half-finished plans? Documents from last month?

You don't copy and paste. You don't re-explain. You say:

> "Look at what's in this folder and help me organize it."

**Most AI tools start from blank. Your Agent Control Center starts from what you already have.**

---

<!-- _class: section-break -->

# Give It Memory

---

## CLAUDE.md: Your Agent's Memory

Create a file called `CLAUDE.md`. The agent reads it automatically at the start of every conversation.

> "Create a CLAUDE.md for this project. I'm going to tell you about myself and what I need."

Then tell it:
- **Who you are** and what you're working on
- **How you like things** -- concise or detailed? Formal or casual?
- **What to avoid** -- fluff, disclaimers, emojis, whatever annoys you

---

## Example CLAUDE.md

```
# About Me
I'm Sarah. High school biology teacher in Austin.
Building supplemental study guides for AP Bio.

# This Project
Study guides for Unit 4 (Cell Communication).
Each guide: 2-3 pages, for smart 17-year-olds.

# How I Work
- Concise answers. I'd rather ask a follow-up.
- Tables and bullet points for comparisons.
- Don't hedge. State facts as facts.
- No filler like "Great question!" Just answer.
```

Next time you open this folder, the agent already knows all of this. **No re-explaining.**

---

## The Accumulation Effect

Every session, the agent reads your files and your CLAUDE.md.

Your workspace **gets smarter over time** -- not because the AI improves, but because the context around it grows.

**The more specific your CLAUDE.md, the better the output.**

- "I'm a teacher" = generic results
- "I teach AP Bio to 17-year-olds who are smart but bored, and I need 2-3 page study guides with quizzes" = results you can actually use

This is the difference between a temp worker and a team member.

---

<!-- _class: section-break -->

# Three Rules

---

## 1. Verify What You Get

The agent will say "Done!" and the output will look polished.

**Don't just trust it.** Read it. Check it. If it wrote a guide about property taxes, spot-check a few facts. If it created a budget, run the numbers.

AI output that looks right but isn't is worse than no output -- because you'll trust it.

> **The rule:** If something matters, verify it before you use it.

---

## 2. One Thing at a Time

Don't ask for a business plan, website copy, and financial projections in one conversation.

Big vague requests = big vague results.

**Break it down.** One project. One task. Check the output. Then the next thing.

Small, verified steps compound faster than ambitious leaps.

---

## 3. Think Before You Ask

Before you type, spend 10 seconds:

- What do I actually need?
- What does "done" look like?
- What constraints matter?

You're not typing keywords into Google. You're **briefing a team member.** The clearer the brief, the better the first draft.

---

<!-- _class: takeaway -->

## What You Have Now

- VS Code + Claude Code installed and working
- A project folder with real files in it
- A CLAUDE.md that teaches the agent who you are
- A workspace that gets smarter over time

There's more this setup can do -- memory systems, automated workflows, rules that enforce your preferences, and more.

That's Part 2. But you don't need any of it to start getting value **right now.**

---

<!-- _class: title -->
<!-- _paginate: false -->

# Stop Vibing. Start Directing.

### Take home the best practices handout. Keep experimenting.

*thebitcoinbreakdown.com*

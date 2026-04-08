# Your Agent Control Center -- Best Practices

*Take-home reference from the workshop. Keep this handy while you explore.*

---

## The Basics

**What you installed:** VS Code (free workspace) + Claude Code extension (needs Claude Pro, $20/month). Together they form your Agent Control Center -- an AI agent that works with real files on your computer.

**How it works:** You type directions in English. The agent creates, edits, and organizes files in whatever folder you have open. Everything stays on your computer.

**The key difference from chatbots:** Your files persist. The agent reads them. Your workspace accumulates knowledge over time. A chatbot forgets you when you close the tab.

---

## How to Talk to the Agent

### Be a Director, Not a Searcher

You're not typing keywords into Google. You're briefing a team member.

| Instead of this | Try this |
|----------------|----------|
| "property tax info" | "Create a plain-English guide to property taxes in New Jersey. I just bought my first house. Cover what I'll owe, when it's due, how assessments work, and what to do if I disagree." |
| "business plan" | "Create a business plan outline for my landscaping company. 15 regular clients, 2 employees, expanding into commercial properties next year. Budget: $50K for expansion." |
| "make it better" | "The intro is too generic. Rewrite it using the specific details I gave you about my business." |

### The Formula

**What you want** + **who it's for** + **what constraints matter** + **what format** = good first draft.

### One Thing at a Time

Don't dump five tasks into one message. Each conversation should focus on one project, one deliverable. Check the output before moving to the next thing.

---

## CLAUDE.md -- Your Agent's Memory

Create a file called `CLAUDE.md` in any project folder. The agent reads it automatically at the start of every conversation.

### What to Include

```
# About Me
[Your name, what you do, what you're working on -- 2-3 sentences]

# This Project
[What you're trying to accomplish. Who it's for. What "done" looks like.]

# How I Work
[Your preferences: concise or detailed? Bullet points or paragraphs?
What annoys you about AI output? List it here.]
```

### Tips

- **Start small.** A few lines is fine. Add more as you discover what helps.
- **Be specific about annoyances.** "Don't use emojis." "Don't start with 'Great question!'" "No disclaimers." These small instructions have outsized impact.
- **Update it.** When the project changes or you want different output, edit the file. Ten seconds saves you from repeating yourself forever.
- **One per project.** Different folders get different CLAUDE.md files. Your trip planning folder has different instructions than your business folder.

### Quick Start

If you're not sure what to write, try this shortcut: after your first session on a new project, tell the agent:

> "Create a CLAUDE.md that captures everything you've learned about this project and how I like to work."

Then review what it wrote and edit it to be more specific.

---

## Verification -- The Most Important Habit

The agent's output will look confident and polished. That doesn't mean it's right.

### What to Check

- **Facts and claims:** If the agent wrote about a topic you're learning, spot-check key facts against a known source. Wikipedia, a textbook, an expert you trust.
- **Numbers:** If it created a budget or calculation, run the math yourself on at least the totals.
- **Advice:** If it gave recommendations (legal, financial, medical, technical), treat them as a starting point for your own research, not as final answers.
- **Your domain:** If you're an expert in the topic, read critically. If you're not, be extra cautious.

### A Useful Trick

Ask the agent: **"What are you least confident about in this document?"**

It will flag the areas where it was guessing or working from limited information. Those are the spots to verify first.

### The Rule

If you can't explain or defend the output without the AI, you don't understand it yet. That's fine for drafts and exploration. It's dangerous for anything you'll publish, submit, or act on.

---

## Working With Folders

Your Agent Control Center works best when you think of **folders as projects**.

```
My Agent Control Center/
  Trip to Portugal/         -- one project
    itinerary.md
    budget.md
    packing-list.md
    CLAUDE.md               -- knows this is a trip for 2 in September

  Business Plan/            -- another project
    outline.md
    market-research.md
    financial-projections.md
    CLAUDE.md               -- knows your business details

  AP Bio Study Guides/      -- another project
    unit-4-overview.md
    signal-transduction.md
    quiz-bank.md
    CLAUDE.md               -- knows your students and format preferences
```

Each folder is self-contained. The agent reads whatever folder you have open. Switch projects by opening a different folder.

---

## The Revision Workflow

This is the core loop. Get comfortable with it.

1. **Direct:** Describe what you want. Be specific about the outcome, not the steps.
2. **Review:** Read what the agent created. Find what's off.
3. **Redirect:** Tell it exactly what to change. "The budget is missing food costs" is better than "fix the budget."
4. **Repeat:** Each pass makes the files better. The agent reads what it already wrote. It doesn't start from scratch.

### Good Revision Prompts

- "The tone is too formal. Rewrite the intro as if you're explaining this to a friend."
- "This section is too long. Cut it in half and keep only the actionable parts."
- "Add a section comparing option A and option B in a table."
- "I'm confused by [specific section]. Expand it with a concrete example."

---

## Common Mistakes to Avoid

**Accepting the first draft without reading it.** That's vibing, not directing. Always read. Always revise.

**Being too vague.** "Help me with my project" gives you generic output. "Create a 3-month marketing plan for a landscaping company expanding into commercial properties in central New Jersey, budget $5K" gives you something useful.

**Trying to do too much at once.** One folder, one project, one task at a time. Check the output. Then move on.

**Never updating your CLAUDE.md.** It should evolve as your project evolves. If you notice the agent keeps getting something wrong, add a rule.

**Trusting output you can't verify.** AI is a starting point, not a finish line. Verify anything that matters before you use it.

---

## What's Next

What you set up today is the foundation. There's more your Agent Control Center can do:

- **Memory systems** that remember across sessions without CLAUDE.md
- **Custom commands** that trigger complex workflows with a single word
- **Rules files** that enforce your preferences automatically
- **Connections** to the web, databases, and other tools

That's Part 2. For now, practice with what you have. Pick a real project this week. Create the folder. Write the CLAUDE.md. Direct the agent. Revise the output.

The more you use it, the more useful it becomes.

**Stop vibing. Start directing.**

---

*thebitcoinbreakdown.com*

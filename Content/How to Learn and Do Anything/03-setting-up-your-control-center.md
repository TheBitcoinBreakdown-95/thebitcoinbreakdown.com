# Setting Up Your Control Center

That hello file you created in the last lesson proved everything works. But it wasn't real work. You don't need an AI agent to write you a greeting.

In this lesson you're going to do two things: give your Agent Control Center a real project, and then teach it who you are so every future conversation starts smarter than the last.

---

## Pick Something Real

This is the single most important instruction in the entire course. Do not skip it.

Pick something you actually need to get done. Not a hypothetical exercise. Something that's been sitting in the back of your mind -- a plan you haven't made, a letter you haven't written, research you've been putting off.

A few examples:

- A business plan for a side project you've been thinking about
- A research document about a topic you need to understand for work
- A lesson plan if you teach anything
- A budget for an upcoming trip or event
- A comparison of options you're deciding between
- A guide you wish existed for something you know about

Pick one. Something specific. Something where you'll actually use the output.

---

## Start Talking

Open your project folder in VS Code. Open the Claude Code panel and describe your project. Not in keywords. Talk to it the way you'd talk to a smart assistant on their first day.

> "I'm planning a two-week trip to Portugal in September for two people. We want to split time between Lisbon and Porto, with maybe a day trip to Sintra. Budget is around $5,000 total not including flights. Can you create a rough itinerary, a packing list, and a budget breakdown? Put each one in its own file."

Or:

> "I need to understand how property taxes work in New Jersey. I just bought my first house and I have no idea what to expect. Can you research this and create a plain-English guide that covers what I'll owe, when it's due, how assessments work, and what I can do if I think the assessment is wrong?"

Notice what's happening. You're not writing a "prompt." You're not trying to hack the AI with magic words. You're just explaining what you need.

---

## Direct the Revision

Files appear in your sidebar. Click on one. Read it.

Some of it will be exactly what you wanted. Some of it won't be quite right. That's fine. This is a first draft, not a final product. You're not done -- this isn't vibing. You don't just accept whatever came out.

Find something that's off. Tell the agent what to change. Be specific.

> "The budget is missing food costs. Add a section for meals, assuming we eat out twice a day at mid-range restaurants."

> "This packing list has way too many clothes. We're packing carry-on only. Revise for a minimalist approach."

The agent updates the actual file on your computer. You can see the changes right there.

This is the workflow. You direct. The agent executes. You review. You redirect. The files get better with each pass. Every revision builds on what's already there -- the agent reads the files it created. It doesn't start from scratch.

---

## It Reads What's Already There

This is the part that surprises people. When you open a folder in VS Code, the agent can read everything in it. Every file. Every subfolder.

If you already have notes, documents, half-finished plans -- the agent can see all of it. You don't have to copy and paste anything. You don't have to re-explain what exists. You point it at a folder and say "look at what's here and help me with it."

Most AI tools start from blank. Your Agent Control Center starts from what you've already got.

And the same workspace where you plan is the same workspace where you execute. No switching tools. No "I'll get to that later." The plan file and the project files live side by side, and the agent knows about all of them.

---

## Teaching It Who You Are

So far, every conversation starts from zero. The agent doesn't know your name, what you're working on, or how you like things done.

That's about to change.

There's a file you can create called `CLAUDE.md`. It's a plain text file that sits in your project folder. The AI agent reads this file automatically at the start of every conversation. Before you say a word, it already knows whatever you put in there.

Ask the agent:

> "Create a file called CLAUDE.md. I'm going to tell you about myself and this project, and I want you to put it in that file."

Then talk. Tell it:

- **Who you are.** Your name, what you do, what you're working on.
- **What this project is.** What you're trying to accomplish. Who it's for.
- **How you like to work.** Short answers or detailed? Bullet points or paragraphs? Formal or casual?
- **What to avoid.** Fluff, disclaimers, overly formal language, emojis, whatever annoys you.

Here's an example:

```
# About Me

I'm Sarah. I'm a high school biology teacher in Austin, Texas.
I'm using this workspace to build supplemental lesson materials
for my AP Bio classes.

# This Project

Creating study guides for Unit 4 (Cell Communication and Cell Cycle).
Each guide should be 2-3 pages, written for 17-year-olds who are
smart but might not love biology yet.

# How I Work

- Keep answers concise. I'd rather ask a follow-up than wade
  through a wall of text.
- Use tables and bullet points for comparisons.
- Don't hedge. State facts as facts.
- Don't add filler like "Great question!" Just answer.
```

That's it. A short document that tells the AI who you are and what you need.

---

## Why This Changes Everything

Next time you open this workspace, the agent already knows you're Sarah, you teach AP Bio, you're building study guides, and you want concise answers without fluff. You walk in and say "write the next study guide on signal transduction pathways" and it knows exactly what that means, who it's for, and how you want it written.

No preamble. No re-explaining. You pick up right where you left off.

And it gets better over time. As you notice things, you update the CLAUDE.md. "Always include a 5-question quiz at the end of each study guide." Done. Every future study guide gets a quiz.

This is the concept that separates an Agent Control Center from every chatbot you've ever used. Chatbots are stateless -- every conversation is isolated. Your Agent Control Center is stateful. Your files are there. Your CLAUDE.md is there. The work you did last week is there. The workspace gets smarter, not because the AI is getting smarter, but because the context around it is growing.

Here's what makes that context powerful: the more specific you are, the better the output. A CLAUDE.md that says "I'm a teacher" gets generic results. One that says "I teach AP Bio to 17-year-olds who are smart but bored, and I need 2-3 page study guides with quizzes" gets results you can actually use. Specificity is the single highest-leverage thing you can do.

---

## A Few Tips

**Start small.** A few lines about who you are and what the project is. Add more as you discover what the agent needs to know.

**Be specific about what annoys you.** "Don't use emojis." "Don't start with 'Great question.'" "Don't add disclaimers." Small instructions, huge impact.

**Update it.** If the project shifts or you want a different format, change the file. Ten seconds. Saves you from repeating yourself forever.

**One per project.** Different folders can have different CLAUDE.md files. Your trip folder has one about the trip. Your business folder has one about the business. Each workspace is customized.

---

## What You Have Now

A project folder with real content. A CLAUDE.md that teaches the AI who you are. Every future conversation in this workspace starts smarter than the last one.

Your Agent Control Center has memory. It accumulates. Not through some magic algorithm, but because you told it what you need, in plain English, in a file you control.

Now let's talk about what you can actually do with this thing.

# Teaching Your Computer Who You Are

So far, every conversation you've had with your Agent Control Center starts from zero. The agent doesn't know your name, what you're working on, how you like things organized, or what kind of tone you prefer. Every time you open a new conversation, it's like meeting a stranger.

That's about to change.

---

## CLAUDE.md

There's a file you can create called `CLAUDE.md`. It's just a plain text file that sits in your project folder. Nothing fancy. No special format. Just a document written in English.

But here's what makes it powerful: the AI agent reads this file automatically at the start of every single conversation. Before you say a word, it already knows whatever you put in there.

Think about that for a second. Instead of re-explaining yourself every time, you write it down once. And every future session starts with that context already loaded.

---

## Write Your First One

Open your project folder in VS Code. Ask the agent:

> "Create a file called CLAUDE.md. I'm going to tell you about myself and this project, and I want you to put it in that file."

Then just... talk. Tell it:

- **Who you are.** Your name, what you do, what you're working on. You don't need a biography. A couple of sentences.
- **What this project is.** What are you trying to accomplish? Who's it for? What does "done" look like?
- **How you like to work.** Do you prefer short, direct answers or detailed explanations? Do you want it to ask clarifying questions or just take its best shot? Do you hate bullet points? Love tables? Want everything in plain language?
- **What to avoid.** If there are things that annoy you about AI output... too much fluff, too many disclaimers, overly formal language, unnecessary caveats... say so.

Here's an example of what a CLAUDE.md might look like:

```
# About Me

I'm Sarah. I'm a high school biology teacher in Austin, Texas.
I'm using this workspace to build supplemental lesson materials
for my AP Bio classes.

# This Project

I'm creating a set of study guides for Unit 4 (Cell Communication
and Cell Cycle). Each guide should be 2-3 pages, written for
17-year-olds who are smart but might not love biology yet. Keep
the language accessible but don't dumb it down.

# How I Work

- Keep answers concise. I'd rather ask a follow-up than wade
  through a wall of text.
- Use tables and bullet points for comparisons and lists.
- Don't hedge. If something is a fact, state it as a fact.
- Don't add motivational filler like "Great question!" Just
  answer.
- I'll tell you when something needs to change. Don't ask
  me to confirm every step.
```

That's it. That's the whole thing. A short document that tells the AI who you are and what you need.

---

## Why This Changes Everything

Remember in the last lesson, when you had to describe your entire project before the agent could do anything? With a CLAUDE.md file, you never have to do that again.

Next time you open this workspace, the agent already knows you're Sarah, you teach AP Bio, you're building study guides for Unit 4, and you like concise answers without fluff. You can walk in and say "write the next study guide on signal transduction pathways" and it knows exactly what that means, who it's for, and how you want it written.

No preamble. No re-explaining. You pick up right where you left off.

And it gets better over time. As you notice things you want the agent to do differently, you update the CLAUDE.md. "Actually, always include a 5-question quiz at the end of each study guide." Done. From now on, every study guide gets a quiz. You taught the agent once and it remembers forever.

---

## The Accumulation Effect

This is the concept that separates an Agent Control Center from every chatbot you've ever used.

Chatbots are stateless. Every conversation is isolated. The AI you talked to yesterday has no idea what you talked about. You're building on sand.

Your Agent Control Center is stateful. Your files are there. Your CLAUDE.md is there. The work you did last week is there. Every session, the agent reads what exists and builds on it. Your workspace gets smarter over time, not because the AI is getting smarter, but because the context around it is growing.

It's like the difference between working with a temp who changes every day versus working with someone who's been on your team for months. The temp is perfectly capable, but you have to explain everything from scratch every morning. Your team member walks in already knowing the project, your preferences, and your working style.

That's what CLAUDE.md does. It turns the AI from a temp into a team member.

---

## A Few Tips

**Start small.** You don't need to write a perfect CLAUDE.md on day one. Start with a few lines about who you are and what the project is. Add more as you discover what the agent needs to know.

**Be specific about what annoys you.** The most useful lines in a CLAUDE.md are often the "don't do this" lines. "Don't use emojis." "Don't start responses with 'Great question.'" "Don't add disclaimers I didn't ask for." These small instructions have a huge impact on how the output feels.

**Update it when something changes.** If the project scope shifts, or you realize you want a different format, update the file. It takes ten seconds and saves you from repeating yourself in every future conversation.

**You can have more than one.** Different project folders can have different CLAUDE.md files. Your trip planning folder has one that describes the trip. Your business plan folder has one that describes the business. Each workspace is customized to its project.

---

## What You Have Now

You've got a project folder with real content in it. You've got a CLAUDE.md file that teaches the AI who you are and what you need. And every future conversation in this workspace starts smarter than the last one.

This is what separates an Agent Control Center from a chatbot. Your workspace has memory. It accumulates. It learns what you want, not through some magic algorithm, but because you told it, in plain English, in a file you control.

Now let's see what you can actually do with this thing.

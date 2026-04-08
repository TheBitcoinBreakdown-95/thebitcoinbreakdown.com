# Connecting to the Outside World

Up until now, your Agent Control Center has been working with what's on your computer. Your files, your folders, your documents. And that's already more powerful than anything a chatbot can do.

But your computer isn't an island. And neither is your Agent Control Center.

---

## What If It Could Talk to Other Things?

Think about what would happen if your AI agent could reach beyond your local files and connect to the tools and services you already use.

Pull information from a Google search and put it directly into your research files. Read your GitHub project and help you manage it. Query a database and summarize what's in it. Reach into a server on your home network and check if everything's running.

That's what MCP servers and SSH do. They extend your Agent Control Center from "a workspace on my computer" to "a workspace that can touch anything."

---

## MCP Servers: Plugging In

MCP stands for Model Context Protocol. The name is technical. The concept is simple.

An MCP server is a plug-in that gives your AI agent the ability to talk to an external service. Want the agent to search the web? There's an MCP server for that. Want it to interact with your GitHub repositories? There's one for that too. Databases, knowledge bases, APIs... each MCP server is a bridge between your agent and something outside your computer.

You don't need to understand how they work under the hood. You just need to know they exist, and that setting one up means your agent gains a new ability.

Here's what it looks like in practice:

> "Search the web for the latest reviews of the DeWalt DCS391B circular saw and summarize the pros and cons into a file."

Without a web search MCP server, the agent can only work with what it already knows (which has a cutoff date and might be outdated). With one, it can go look things up in real time and bring the results into your files.

> "Check my GitHub repository for any open issues and create a summary file."

Without a GitHub MCP server, you'd have to go to GitHub yourself, read through the issues, and paste them in. With one, the agent does it directly.

The pattern is always the same: install the MCP server, and your agent gains a new superpower. Your Agent Control Center gets more capable over time, not because the AI gets smarter, but because you keep connecting it to more things.

---

## SSH: Reaching Into Other Machines

This one's more niche, but if you've got a server at home... a Raspberry Pi, a Bitcoin node, a NAS, a home lab... SSH lets your agent reach into it.

SSH stands for Secure Shell. It's a way to connect to another computer over your network and run commands on it. Developers and sysadmins use it every day. And your AI agent can use it too.

Imagine you've got a Bitcoin node running in your closet. Instead of walking over to it, plugging in a monitor, and typing commands manually, you sit at your desk and tell your agent:

> "SSH into my node and check if Bitcoin Core is fully synced. Show me the current block height and compare it to the network."

The agent connects, runs the commands, and reports back. All from your Agent Control Center.

Or maybe you've got a home media server:

> "SSH into my Plex server and check how much disk space is left. If it's under 10%, list the largest files so I can decide what to delete."

Your workspace just became a control panel for every machine on your network.

---

## The Big Picture

What you're building is bigger than a folder with some files in it. You started with a workspace. You taught it who you are. You used it to learn, organize, and plan. And now it can reach beyond your computer and interact with the rest of your digital life.

Your Agent Control Center isn't just a place where you talk to AI. It's becoming the central interface for how you interact with... kind of everything.

And the thing is, every connection you add makes all the other connections more valuable. An agent that can search the web AND read your existing research files can do things neither capability could do alone. An agent that can access your GitHub AND your project files can manage your code and your documentation in the same conversation.

This is what compounds. Not the AI. The environment around it.

---

## A Note on Setup

Setting up MCP servers and SSH connections is more technical than anything else in this course. It involves editing configuration files and sometimes running commands in the terminal. It's not hard, but it does require following instructions carefully.

We're not going to walk through specific setups here... that's the kind of thing that belongs in the follow-up course (Intro to Claude Code), where we go deep on configuration, tools, and workflows.

What matters right now is that you know this is possible. When you're ready, you'll know what to search for and what to ask. And your Agent Control Center will be ready to grow with you.

---

## What You Can Do Right Now

Even without MCP servers or SSH, you already have a lot. Your Agent Control Center reads your files, creates new ones, remembers who you are, and builds on previous work.

But now you know that's not the ceiling. The ceiling is your Agent Control Center talking to everything... your web, your code, your servers, your data. And all of it accessible through the same plain-English conversation you've been having since Lesson 03.

There's one more thing to cover before we send you out into the world. The honest picture.

# What You Need and How to Install It

Alright, enough theory. Let's build the thing.

By the end of this lesson you're going to have a working Agent Control Center on your computer. You're going to talk to an AI agent, ask it to create a file, and watch that file appear in a folder on your machine. It takes about fifteen minutes.

Here's what you need.

---

## The Shopping List

**A computer.** Windows, Mac, or Linux. Desktop or laptop. It doesn't need to be fancy. If it can run a web browser, it can run everything we're about to install.

**VS Code (free).** This is the workspace. Think of it as a really smart file explorer with a built-in place to talk to AI. Programmers use it every day, but that doesn't mean it's only for programmers. It's free, it works on every operating system, and millions of people use it, which means if you ever get stuck there's an answer somewhere online.

**A Claude subscription ($20/month).** This is the AI agent. Claude is made by Anthropic, and the Pro subscription gives you access to Claude Code, which is the agent that lives inside VS Code. Twenty bucks a month. No contract. Cancel any time.

That's it. No special hardware. No additional software. No terminal wizardry.

---

## Step 1: Install VS Code

Go to code.visualstudio.com. Click the big download button. It'll detect your operating system automatically.

**Windows:** Run the installer. Click through the prompts. All the defaults are fine.

**Mac:** Download the .zip, unzip it, drag VS Code into your Applications folder.

**Linux:** Download the .deb or .rpm package, or install via your package manager.

Once it's installed, open it. You'll see something like this:

- A sidebar on the left with file icons
- A big empty area in the middle where files open
- A welcome tab with some getting-started stuff you can ignore

That's your workspace. The sidebar is where your files and folders live. The main area is where you read and edit them. Simple.

---

## Step 2: Install the Claude Code Extension

Inside VS Code, look at the left sidebar. There's an icon that looks like four squares (or building blocks). That's the Extensions panel. Click it.

In the search bar at the top, type "Claude Code." You'll see the official extension from Anthropic. Click Install.

That's it. Claude Code is now inside VS Code.

You'll notice a new panel appears at the bottom of your screen, or you might see a Claude icon in the sidebar. That panel is where you'll type your directions to the AI agent. It's just a text box. You type in English, and the agent responds.

---

## Step 3: Sign In

The first time you use Claude Code, it'll ask you to sign in to your Anthropic account. If you don't have one yet, go to claude.ai and sign up for the Pro plan ($20/month).

Once you're signed in, you're connected. The agent is live. You can start talking to it.

---

## Why VS Code?

You might be wondering why we're not using ChatGPT's website, or Claude's website, or some other app. Fair question.

Here's why VS Code changes everything.

**It sees your files.** When you open a folder in VS Code, the AI agent can read everything in that folder. It knows what files exist, what's in them, and how they're organized. A chatbot in a browser tab knows nothing about you or your work until you copy and paste it in.

**It creates real files.** When you tell the agent to make something, it doesn't just show you text in a chat window. It creates an actual file on your computer. A file you can open in any program, email to someone, or print out.

**It remembers.** Because your files persist on your computer, the agent can read them next time you open the workspace. Your context accumulates. You don't start from scratch every session.

**It's free and universal.** VS Code costs nothing, runs on everything, and has the largest community of any code editor in the world. If you ever want to do more with it, the resources are endless.

---

## The Terminal Is Not Scary

There's one part of VS Code that might make you nervous if you've never programmed before. The terminal.

The terminal is that dark panel at the bottom of the screen where you sometimes see text appearing. It looks like something from a hacker movie. It's not.

The terminal is just a place where programs talk to you in text instead of buttons. That's all. When Claude Code does something, it sometimes shows you what it's doing in the terminal. You don't need to type anything there. You don't need to understand what it says. It's just the agent working.

Think of it like the dashboard on your car. There are gauges and numbers and lights, and most of the time you don't need to look at any of them. You just drive. If something goes wrong, the check engine light comes on and you deal with it. Otherwise, you ignore it.

Same with the terminal. It's there. It's fine. Ignore it until you're curious enough to look.

And here's the thing... as you get more comfortable, you'll start glancing at the terminal and understanding what's happening. Not because someone forced you to learn it, but because you'll naturally pick it up. That's how this whole process works. You learn by doing, not by studying.

---

## Your First Conversation

Let's make sure everything is working.

**1. Create a folder on your computer.** Anywhere you like. Your Desktop, your Documents folder, wherever. Call it something like "My Agent Control Center" or "AI Projects" or whatever makes sense to you. This is where your work will live.

**2. Open that folder in VS Code.** You can do this by opening VS Code, clicking File > Open Folder, and selecting the folder you just created. Or you can right-click the folder in your file explorer and choose "Open with Code" if that option appears.

**3. Open the Claude Code panel.** Click the Claude icon in the sidebar, or look for the panel at the bottom of the screen. You should see a text box where you can type.

**4. Say hello.** Seriously. Just type "Hello, can you create a file called hello.md with a short introduction about what this workspace is for?" and press Enter.

Watch what happens.

The agent will respond in the chat. It'll tell you what it's about to do. And then... a file appears in your sidebar. `hello.md`. Click on it. There's your content, sitting in a real file on your real computer.

You just directed an AI agent from your desktop. That file isn't trapped in a chat log somewhere. It's not locked inside someone else's platform. It's a plain text file in a folder you control.

That's the whole thing. Everything else in this course builds on exactly what you just did.

---

## If Something Didn't Work

If you got stuck at any step, here's a quick checklist:

- **VS Code won't install:** Make sure you downloaded the right version for your operating system (Windows, Mac, or Linux). Try restarting your computer and running the installer again.
- **Can't find the Claude Code extension:** Make sure you're searching in the Extensions panel inside VS Code (the four-squares icon), not in a web browser.
- **Claude Code asks for a sign-in but fails:** Check that your Anthropic account has an active Pro subscription at claude.ai. Try signing out and signing back in.
- **You typed something but nothing happened:** Make sure you're typing in the Claude Code panel, not in the regular VS Code terminal. The Claude panel is specifically for talking to the agent.
- **A file didn't appear:** Check the sidebar on the left. You might need to click the file explorer icon (the top icon in the sidebar) to see your files. The file should be in the folder you opened.

If none of that helps, the most reliable fix is usually the simplest one: close everything, reopen VS Code, reopen your folder, and try again. Nine times out of ten, that clears it up.

---

## What You Have Now

You've got VS Code installed with the Claude Code extension. You've got a folder on your computer that serves as your workspace. And you've had your first conversation with an AI agent that created a real file on your machine.

That's your Agent Control Center. It's bare right now. Just a folder with a file in it. But in the next lesson, you're going to give it a real project, and you'll start to see what this workspace can actually do.

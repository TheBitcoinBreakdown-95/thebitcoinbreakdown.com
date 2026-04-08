# Installing Your Agent Control Center

Enough theory. Let's build the thing.

By the end of this lesson you're going to have a working Agent Control Center on your computer. You're going to talk to an AI agent, ask it to create a file, and watch that file appear in a folder on your machine. It takes about fifteen minutes.

---

## The Shopping List

**A computer.** Windows, Mac, or Linux. Desktop or laptop. It doesn't need to be fancy. If it can run a web browser, it can run everything we're about to install.

**VS Code (free).** This is the workspace. Think of it as a really smart file explorer with a built-in place to talk to AI. Programmers use it every day, but that doesn't mean it's only for programmers. It's free, it works on every operating system, and millions of people use it.

**A Claude subscription ($20/month).** This is the AI agent. Claude is made by Anthropic, and the Pro subscription gives you access to Claude Code. Twenty bucks a month. No contract. Cancel any time.

That's it. No special hardware. No additional software.

---

## Step 1: Install VS Code

Go to code.visualstudio.com. Click the big download button. It detects your operating system automatically.

**Windows:** Run the installer. Click through the prompts. All the defaults are fine. When it asks about additional tasks, check the box that says "Add to PATH" and "Register Code as an editor for supported file types." These make your life easier later.

**Mac:** Download the .zip file. Unzip it (double-click). Drag the VS Code icon into your Applications folder. The first time you open it, macOS might show a warning that says "VS Code is an app downloaded from the Internet. Are you sure you want to open it?" Click Open. This is normal -- macOS warns you about every app that didn't come from the App Store.

**Linux:** Go to code.visualstudio.com and download the .deb package (Ubuntu/Debian) or .rpm package (Fedora/Red Hat). Install it through your package manager or double-click the file. If you're on Linux, you probably already know how to install software, so I'll spare you the lecture.

Once it's installed, open VS Code. You'll see:

- A sidebar on the left with icons
- A big empty area in the middle
- A welcome tab you can close

That's your workspace. Don't worry about the rest yet.

---

## Step 2: Get Comfortable With VS Code

Before we add the AI, let's make sure you're not lost in the interface. VS Code has a lot of buttons, but you only need to know about four things right now.

**The File Explorer (top icon in the sidebar).** This shows the files and folders in whatever project you have open. It works like the file explorer on your computer because that's exactly what it is.

**The Extensions panel (icon that looks like four squares).** This is where you install add-ons that give VS Code new abilities. We're about to use it.

**The main editor area (the big space in the middle).** This is where files open when you click on them. You can read and edit files here.

**The "Open Folder" command.** This is how you tell VS Code what to work on. Go to File > Open Folder and select any folder on your computer. VS Code now shows you everything in that folder. This is important: VS Code works with folders, not individual files. When you open a folder, the AI agent can see everything inside it.

The first time you open a folder, VS Code might ask "Do you trust the authors of the files in this folder?" Click "Yes, I trust the authors." This is a security feature -- VS Code wants to make sure you're not opening someone else's untrusted code. Since these are your own files, it's safe.

---

## Step 3: Install the Claude Code Extension

Click the Extensions icon in the sidebar (four squares). In the search bar at the top, type "Claude Code."

You'll see results appear. Look for the one that says **"Claude Code"** by **Anthropic** -- that's the official one. There may be other extensions with similar names. Make sure it says Anthropic as the publisher.

Click Install.

After a few seconds, you'll notice a new icon in your sidebar -- the Claude icon. You might also see a panel appear at the bottom or side of your screen. That's the Claude Code panel. This is where you'll type your directions to the AI agent.

---

## Step 4: Sign In

Click the Claude icon in the sidebar to open the Claude Code panel. The first time, it will ask you to sign in.

**If you already have a Claude Pro account:** Click the sign-in button. It'll open your web browser and ask you to log in to claude.ai. Log in, authorize the connection, and come back to VS Code. You're connected.

**If you don't have an account yet:** Go to claude.ai in your web browser. Sign up for an account and subscribe to the Pro plan ($20/month). Then come back to VS Code and sign in.

**Important distinction:** claude.ai (the website) is the chatbot in a browser. Claude Code (in VS Code) is the agent on your computer. Same company, same AI, completely different experience. The website is vibing. VS Code is directing. You're paying for the Pro plan because it gives you access to Claude Code, which is what makes the Agent Control Center possible.

Once you're signed in, the Claude Code panel should show a text input area. You're ready.

---

## Step 5: Your First Conversation

Let's make sure everything works.

**1. Create a folder.** Open your file explorer (not VS Code -- your regular file explorer). Create a new folder somewhere easy to find. Your Desktop or Documents folder is fine. Call it "My Agent Control Center" or "AI Projects" or whatever makes sense to you.

**2. Open that folder in VS Code.** Go to File > Open Folder and select the folder you just created. You should see an empty file explorer in the sidebar.

**3. Open the Claude Code panel.** Click the Claude icon in the sidebar. You should see a text box where you can type.

**4. Type this exactly:**

> Hello, can you create a file called hello.md with a short introduction about what this workspace is for?

Press Enter (or click the send button).

**5. Watch what happens.** The agent will respond in the panel. It will tell you what it's about to do. It might ask for permission to create a file -- click Allow or Yes. And then... a file appears in your sidebar. `hello.md`. Click on it. There's your content, sitting in a real file on your real computer.

**What you might see that's unfamiliar:** The agent might show you a "diff" -- a view that highlights what it's adding to a file in green. This is normal. It's showing you the changes before (or after) it makes them. You might also see text scrolling in a terminal panel at the bottom of the screen. That's the agent working. You don't need to understand it.

**What the permission prompts mean:** Claude Code will sometimes ask "Allow Claude to create this file?" or "Allow Claude to run this command?" This is a safety feature. The agent is asking before it touches your computer. For now, click Allow. As you get comfortable, you'll develop a sense for when to allow and when to pause and read what it's proposing.

You just directed an AI agent from your desktop. That file isn't trapped in a chat log. It's not locked inside someone else's platform. It's a plain text file in a folder you control.

---

## What You Have Now

VS Code is installed. Claude Code is installed. You've signed in. You've got a folder on your computer that serves as your workspace. And you've had your first conversation with an AI agent that created a real file on your machine.

That's your Agent Control Center. It's bare right now -- just a folder with a file in it. In the next lesson, you're going to give it a real project, teach it who you are, and start to see what this workspace can actually do.

If anything didn't work, check the Troubleshooting appendix at the end of this course before you give up. Most issues have simple fixes.

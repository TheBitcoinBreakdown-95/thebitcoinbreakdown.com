# Troubleshooting and Common Errors

This is a reference, not a lesson. Come here when something isn't working. Find your problem, try the fix, and get back to it.

---

## VS Code Issues

**VS Code won't install.**
Make sure you downloaded the right version for your operating system. On Windows, run the installer as administrator if the normal install fails (right-click the installer > Run as administrator). On Mac, make sure you dragged the app into Applications, not just running it from the Downloads folder. Restart your computer and try again.

**VS Code is overwhelming -- too many buttons and panels.**
Close everything except the file explorer (sidebar, top icon) and the Claude Code panel. You can close the terminal panel at the bottom by clicking the X on it. You can close the welcome tab. You only need two things visible: your files on the left, and Claude Code where you type.

**"Do you trust the authors of the files in this folder?"**
Click "Yes, I trust the authors." This appears every time you open a new folder. It's a security feature. Since you're opening your own files, it's safe. If you don't click yes, the Claude Code extension won't be able to work with your files.

---

## Claude Code Extension Issues

**Can't find the Claude Code extension.**
Open the Extensions panel in VS Code (the four-squares icon in the sidebar, or press Ctrl+Shift+X on Windows/Linux, Cmd+Shift+X on Mac). Search for "Claude Code" -- make sure you're looking for the one published by **Anthropic**. There may be other extensions with similar names. If it doesn't appear at all, make sure your VS Code is up to date (Help > Check for Updates).

**Installed the wrong extension.**
If you installed something that's not the official Anthropic extension, uninstall it (click the gear icon on the extension > Uninstall) and search again for the one by Anthropic.

**The Claude Code panel isn't showing up.**
After installing the extension, look for the Claude icon in the sidebar. Click it. If you don't see it, try restarting VS Code (close it completely and reopen). The extension might need VS Code to restart before it activates.

---

## Sign-In and Authentication Issues

**Claude Code asks for a sign-in but the browser doesn't open.**
Try clicking the sign-in button again. If the browser still doesn't open, look in the Claude Code panel for a URL you can copy and paste into your browser manually. Some systems block VS Code from opening browser tabs.

**I signed in but Claude Code says I'm not authorized.**
You need a Claude Pro or Max subscription. The free Claude account does not include Claude Code access. Go to claude.ai, check your account settings, and make sure you have an active paid subscription.

**"Session expired" or authentication errors.**
Sign out and sign back in. In VS Code, open the Command Palette (Ctrl+Shift+P on Windows/Linux, Cmd+Shift+P on Mac), type "Claude Code: Sign Out" and run it. Then sign in again.

**I have a Claude account but it's not working.**
Make sure you're signing in with the same account that has the Pro subscription. If you have multiple accounts (work and personal, for example), you might be signed into the wrong one.

---

## File and Permission Issues

**Claude says it can't access my files.**
Make sure you opened a folder in VS Code (File > Open Folder), not just a single file. Claude Code needs a workspace folder to operate. Also check that you clicked "Yes, I trust the authors" when VS Code asked about the folder.

**Claude asks permission to create/edit files and I'm not sure what to click.**
When Claude Code wants to create or modify a file, it asks for permission. This is a safety feature. If you see "Allow Claude to create [filename]" and the filename looks reasonable for what you asked, click Allow. If something looks wrong or unexpected, click Deny and ask Claude what it's trying to do.

**Files aren't appearing in the sidebar after Claude creates them.**
Click the file explorer icon (top icon in the sidebar) to make sure you're looking at the right panel. The file should appear in the folder you have open. If you still don't see it, try clicking the refresh icon at the top of the file explorer, or collapse and expand the folder.

---

## Terminal and Error Messages

**Scary-looking text is appearing in the terminal.**
The terminal panel at the bottom of VS Code sometimes shows technical output while Claude Code works. This is normal. You don't need to read it or understand it. If Claude Code completed your request and the files look right, the terminal output doesn't matter.

**Red text in the terminal.**
Red text usually means an error, but not always a problem you need to fix. If Claude Code tells you it completed your task successfully and the output files look correct, you can ignore red terminal text. If Claude Code itself reports a failure, that's when the error matters.

**"Command not found" or similar errors.**
If you see this in the terminal, Claude Code might be trying to use a program that isn't installed on your computer. This is rare for basic use. If it happens, tell Claude Code about the error and ask it to try a different approach.

---

## Usage Limits

**"You've reached your usage limit" or similar message.**
The Claude Pro plan has a usage allowance that refreshes periodically. If you hit the limit, you'll need to wait for it to reset (usually a few hours) or upgrade to the Max plan for higher limits. The Claude Code panel will typically tell you when your limit resets.

**How to avoid hitting limits quickly.**
Shorter, focused requests use less of your allowance than long, open-ended ones. Breaking work into smaller tasks is better for your limit and better for your results.

---

## Windows-Specific Issues

**PowerShell execution policy error.**
If you see an error about "execution policy" or "running scripts is disabled," open PowerShell as Administrator and run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`. This allows VS Code extensions to function properly.

**Antivirus blocking VS Code or Claude Code.**
Some antivirus software flags VS Code or its extensions. If VS Code or Claude Code stops working after an antivirus scan, add VS Code to your antivirus exceptions list. The VS Code installation folder is typically in `C:\Users\[YourName]\AppData\Local\Programs\Microsoft VS Code\`.

**"Open with Code" doesn't appear in right-click menu.**
Reinstall VS Code and check the boxes for "Add 'Open with Code' action to Windows Explorer file context menu" and "Add 'Open with Code' action to Windows Explorer directory context menu" during installation.

---

## Mac-Specific Issues

**"VS Code is an app downloaded from the Internet" warning.**
Click Open. This is macOS Gatekeeper warning you about apps downloaded outside the App Store. VS Code is safe.

**"VS Code can't be opened because Apple cannot check it for malicious software."**
Go to System Settings > Privacy and Security. Scroll down and you'll see a message about VS Code being blocked. Click "Open Anyway."

**macOS asks for your password during installation.**
Some installations require administrator access. Enter your Mac login password. This is your computer password, not your Claude or Apple ID password.

---

## Linux-Specific Issues

**"Package not found" or dependency errors.**
Make sure you downloaded the right package for your distribution (.deb for Ubuntu/Debian, .rpm for Fedora/Red Hat). If installing via command line, use `sudo dpkg -i filename.deb` for .deb packages or `sudo rpm -i filename.rpm` for .rpm packages. Run `sudo apt --fix-broken install` afterward if you get dependency errors on Ubuntu/Debian.

**VS Code won't launch.**
Try running `code` from the terminal to see if there's an error message. On some Linux distributions, you may need to install additional libraries. The error message will usually tell you what's missing.

---

## The Universal Fix

If none of the above helps, try this sequence:

1. Close VS Code completely
2. Restart your computer
3. Open VS Code
4. Open your project folder (File > Open Folder)
5. Try again

Nine times out of ten, a fresh restart clears whatever was stuck. If you're still having trouble after that, search for your specific error message online -- someone else has almost certainly had the same problem.

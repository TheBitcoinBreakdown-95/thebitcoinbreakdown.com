# Setup

This lesson gets you from zero to connected. By the end, you'll have an SSH key, your node will recognize it, and you'll have typed your first command on a remote machine.

---

## Step 1: Generate an SSH Key

Open a terminal on your computer (Terminal on Mac/Linux, PowerShell or Git Bash on Windows).

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_mynode
```

- `-t ed25519` -- the algorithm. Ed25519 is modern, fast, and secure.
- `-f ~/.ssh/id_ed25519_mynode` -- where to save the key. Give it a descriptive name so you know what it's for.

It will ask you to set a **passphrase**. Do it. This encrypts the key file so that even if someone copies it off your machine, they can't use it without the passphrase.

This creates two files:
- `~/.ssh/id_ed25519_mynode` -- your **private key**. Never share this. Never move it off this machine.
- `~/.ssh/id_ed25519_mynode.pub` -- your **public key**. This goes on the node. Safe to share.

**Windows note:** `~` means `C:\Users\YourUsername`. The `.ssh` folder should already exist. If not, create it.

### How key pairs work

Your private key and public key are mathematically linked. When you connect, your computer proves it has the private key without ever sending it. The node checks this proof against the public key you registered. If they match, you're in.

This is more secure than a password:
- The private key never leaves your machine
- There's nothing to guess or brute-force (256 bits of randomness)
- Each key pair is unique to you

---

## Step 2: Add Your Public Key to StartOS

1. View your public key:
   ```bash
   # Mac/Linux
   cat ~/.ssh/id_ed25519_mynode.pub

   # Windows (PowerShell)
   type C:\Users\YourUsername\.ssh\id_ed25519_mynode.pub
   ```
2. Copy the entire output (it starts with `ssh-ed25519` and ends with your username)
3. Open your StartOS dashboard in a browser
4. Go to **System > SSH Keys**
5. Paste the public key and save

That's it. Your node now recognizes your laptop.

---

## Step 3: Find Your Node's Address

You need your node's IP address on your local network. Check one of these:

- **StartOS dashboard:** the address bar in your browser already has it (something like `192.168.1.50`)
- **Router admin page:** look for connected devices -- find the one running StartOS
- **StartOS hostname:** StartOS assigns a `.local` hostname (like `wood-opals.local`), visible in the dashboard. This works on Mac and Linux but is unreliable on Windows.

Write down the IP address. You'll use it once, then we'll create a shortcut.

---

## Step 4: Connect

```bash
ssh -i ~/.ssh/id_ed25519_mynode start9@192.168.1.50
```

Replace `192.168.1.50` with your node's actual IP.

- `-i` points to your private key
- `start9` is the default username on StartOS

**First connection:** You'll see a message asking if you trust the server's fingerprint. Type `yes`. This only happens once -- SSH remembers the server after that.

**Passphrase prompt:** Enter the passphrase you set during key generation. This is your key's passphrase, not a server password.

If everything worked, your terminal prompt changes to something like:

```
start9@wood-opals:~$
```

You're on your node. Type `exit` to disconnect and return to your laptop's terminal.

---

## Step 5: Create a Shortcut

Typing the full connection string every time is tedious. Create a config file so you never have to again.

Create or edit `~/.ssh/config` (on your laptop, not the node):

```
Host mynode
    HostName 192.168.1.50
    User start9
    IdentityFile ~/.ssh/id_ed25519_mynode
    IdentitiesOnly yes
```

Replace the IP with your node's address. Now connecting is just:

```bash
ssh mynode
```

And running a command without opening a full session:

```bash
ssh mynode "echo hello"
```

If that prints `hello`, your shortcut works.

---

## Step 6: Set Up for Claude (Optional)

If you want Claude Code (or another AI assistant) to run commands on your node, there's one extra step. Claude can't type passphrases interactively, so you need to load your key into an SSH agent first.

### Mac/Linux

The SSH agent usually runs automatically. Just add your key:

```bash
ssh-add ~/.ssh/id_ed25519_mynode
```

Enter your passphrase once. The agent holds the decrypted key in memory until you log out or flush it.

### Windows

Windows has its own SSH agent, but it needs to be started and you need to make sure your terminal uses the right SSH binary.

**In PowerShell (run as Administrator):**

```powershell
# Check if the agent is running
Get-Service ssh-agent

# If it says "Stopped", start it and set it to auto-start:
Set-Service -Name ssh-agent -StartupType Automatic
Start-Service ssh-agent

# Add your key (prompts for passphrase once)
C:\Windows\System32\OpenSSH\ssh-add.exe C:\Users\YourUsername\.ssh\id_ed25519_mynode
```

**Important for Git Bash users:** Git Bash ships its own SSH binary that does not talk to the Windows agent. If you use Git Bash (or Claude Code on Windows, which uses Git Bash), add these aliases to your `~/.bashrc`:

```bash
export GIT_SSH="/c/Windows/System32/OpenSSH/ssh.exe"
alias ssh='/c/Windows/System32/OpenSSH/ssh.exe'
alias scp='/c/Windows/System32/OpenSSH/scp.exe'
```

Then reload: `source ~/.bashrc`

### Verify Claude can connect

With the agent loaded, test it:

```bash
ssh mynode "echo connected"
```

If it prints `connected` without asking for a passphrase, Claude can use it too.

### When you're done for the day

Flush the keys from the agent:

```bash
# Mac/Linux
ssh-add -D

# Windows
C:\Windows\System32\OpenSSH\ssh-add.exe -D
```

This removes the decrypted key from memory. Your key file stays passphrase-protected on disk. More on why this matters in the next lesson.

---

## What Just Happened

You created a cryptographic key pair, registered the public half with your node, and established an encrypted tunnel between your laptop and your server. Every command that travels through this tunnel is encrypted -- nobody on your network can see what you're doing.

Your node is now accessible from your terminal. Next up: understanding what this access means and how to keep it safe.

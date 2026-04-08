# SSH Explained and Setup

SSH (Secure Shell) is how you remotely control a computer using a text-based terminal. Instead of sitting in front of your server, you type commands from your laptop and they execute on the server as if you were there.

For Bitcoin node runners, SSH is the bridge between your everyday computer and the node sitting in your closet, basement, or wherever you plugged it in.

---

## How SSH Authentication Works

SSH uses **key pairs** -- two files that are mathematically linked:

- **Private key** -- stays on your computer. Never share this. Think of it as a password that lives in a file.
- **Public key** -- goes on the server. Safe to share. Think of it as a lock that only your private key can open.

When you connect, your computer proves it has the private key without ever sending it over the network. The server checks this proof against the public key you registered earlier. If they match, you're in.

This is more secure than a password because:
- The private key never leaves your machine
- There's nothing to guess or brute-force (the key is 256 bits of randomness)
- Each key pair is unique to you

---

## Step 1: Generate an SSH Key

Open a terminal on your computer (Terminal on Mac/Linux, PowerShell or Git Bash on Windows).

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_mynode
```

- `-t ed25519` -- use the Ed25519 algorithm (modern, fast, secure)
- `-f ~/.ssh/id_ed25519_mynode` -- save the key with a descriptive name

It will ask you to set a **passphrase**. Do it. This encrypts the key file so that even if someone copies it, they can't use it without the passphrase.

This creates two files:
- `~/.ssh/id_ed25519_mynode` -- your private key (keep this secret)
- `~/.ssh/id_ed25519_mynode.pub` -- your public key (put this on the server)

**Windows note:** On Windows, `~` means `C:\Users\YourUsername`. The `.ssh` folder should already exist. If not, create it.

---

## Step 2: Add Your Public Key to the Server

You need to get the contents of the `.pub` file onto your server. How you do this depends on your node OS:

### StartOS
1. Open your StartOS dashboard in a browser
2. Go to System > SSH Keys
3. Paste the contents of your `.pub` file

### Umbrel
1. SSH is available by default with password auth
2. SSH in with the default password first, then add your key to `~/.ssh/authorized_keys`

### RaspiBlitz
1. SSH in with the default password
2. Run `sudo nano ~/.ssh/authorized_keys` and paste your public key

### Manual (any Linux server)
```bash
# From your local machine, copy the key to the server
ssh-copy-id -i ~/.ssh/id_ed25519_mynode user@your-server-ip
```

To view your public key for copying:
```bash
# Mac/Linux
cat ~/.ssh/id_ed25519_mynode.pub

# Windows (PowerShell)
type C:\Users\YourUsername\.ssh\id_ed25519_mynode.pub
```

---

## Step 3: Connect

```bash
ssh -i ~/.ssh/id_ed25519_mynode user@your-server-ip
```

- Replace `user` with your server's username (`start9`, `umbrel`, `admin`, etc.)
- Replace `your-server-ip` with the server's IP address on your network (e.g., `192.168.1.50`)

**First connection:** You'll see a message asking if you trust the server's fingerprint. Type `yes`. This only happens once -- SSH remembers the server after that.

**Finding your server's IP:** Check your router's admin page for connected devices, or look in your node OS dashboard. Some node OSes also broadcast a `.local` hostname (e.g., `umbrel.local`), but raw IP addresses are more reliable.

---

## Step 4: Make It Easier with an SSH Config

Instead of typing the full command every time, create a config file.

Create or edit `~/.ssh/config`:

```
Host mynode
    HostName 192.168.1.50
    User start9
    IdentityFile ~/.ssh/id_ed25519_mynode
    IdentitiesOnly yes
```

Now you can just type:
```bash
ssh mynode
```

That's it. The config file fills in the rest.

---

## You're In

After connecting, you'll see a command prompt on your server -- something like:

```
start9@wood-opals:~$
```

This is a Linux terminal. Everything you type runs on the server, not your local machine. Type `exit` to disconnect and return to your own terminal.

Next up: finding Bitcoin Core on your server and running your first command.

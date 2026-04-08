# SSH Instructions

## Generate a new SSH key (without overwriting existing keys)

Use the full path to avoid Windows path resolution issues. This will prompt you to set a passphrase.

```
ssh-keygen -t ed25519 -f "C:\Users\GC\.ssh\id_ed25519_server"
```

## Show the public key

```
type "C:\Users\GC\.ssh\id_ed25519_server.pub"
```

Copy the output and add it to `~/.ssh/authorized_keys` on the server.

## Connect to the server

Use the raw IP address, not the .locl hostname (Windows does not resolve mDNS reliably).
Specify the key explicitly with -i since it is not the default filename.

```
ssh -i "C:\Users\GC\.ssh\id_ed25519_server" start9@wood-opals.local
```

Enter your passphrase when prompted. This is the passphrase you set during key generation, not the server's login password.

## Using Bitcoin Core on the server

The server runs StartOS (Debian 12), which manages services inside Podman containers. Bitcoin Core 30.0.0 runs in a container named `bitcoind.embassy`.

### Run a single bitcoin-cli command

Once SSH'd into the server:

```bash
sudo podman exec bitcoind.embassy bitcoin-cli <command>
```

Examples:

```bash
sudo podman exec bitcoind.embassy bitcoin-cli getblockchaininfo
sudo podman exec bitcoind.embassy bitcoin-cli getnetworkinfo
sudo podman exec bitcoind.embassy bitcoin-cli getmempoolinfo
sudo podman exec bitcoind.embassy bitcoin-cli getpeerinfo
```

### Open an interactive shell inside the container

```bash
sudo podman exec -it bitcoind.embassy bash
```

This drops you into the container itself. From there you can run `bitcoin-cli` directly without the `podman exec` prefix. Bitcoin Core's data directory inside the container is `/root/.bitcoin/`.

Type `exit` to leave the container and return to the server shell.

### Other services on this server

- **Electrs 0.10.9** (Electrum indexing server): `sudo podman exec electrs.embassy <command>`
- List all running containers: `sudo podman ps`

---

## Using SSH from Claude Code (non-interactive setup)

Claude Code cannot type passphrases or interact with prompts. To let it run commands on the server, we use the Windows SSH agent to hold the decrypted key in memory and an SSH config file to avoid typing connection details.

### Prerequisites (already done, one-time setup)

1. **SSH config file** at `C:\Users\GC\.ssh\config`:
   ```
   Host startbox
       HostName wood-opals.local
       User start9
       IdentityFile ~/.ssh/id_ed25519_server
       IdentitiesOnly yes
       BatchMode yes
       StrictHostKeyChecking accept-new
   ```
   This creates the alias `startbox` so commands are just `ssh startbox "command"`.

2. **Bash aliases** in `C:\Users\GC\.bashrc` (already added):
   ```bash
   export GIT_SSH="/c/Windows/System32/OpenSSH/ssh.exe"
   alias ssh='/c/Windows/System32/OpenSSH/ssh.exe'
   alias scp='/c/Windows/System32/OpenSSH/scp.exe'
   ```
   Git Bash ships its own SSH that does NOT talk to the Windows agent. These aliases force it to use the Windows OpenSSH binaries instead.

### Each session: start the agent and load the key

The agent service is set to auto-start, but the key does not persist across reboots. At the start of each session, run this in a **PowerShell (Admin)** window:

```powershell
# Verify the agent is running (should say "Running")
Get-Service ssh-agent

# If it says "Stopped", start it:
Start-Service ssh-agent

# Add the key (prompts for passphrase once)
C:\Windows\System32\OpenSSH\ssh-add.exe C:\Users\GC\.ssh\id_ed25519_server
```

After entering the passphrase, Claude Code can run commands like:
```bash
/c/Windows/System32/OpenSSH/ssh.exe startbox "echo connected"
```

### Security risks while the agent is active

- **Any process running as your Windows user** can ask the agent to use the key. This means any program you run (scripts, apps, malware) could SSH to the server without your knowledge.
- The decrypted key lives **in memory only** -- it is not written to disk. Your key file remains passphrase-protected.
- The server is on your **local network**, which limits exposure compared to an internet-facing server.
- This is the same security model used by macOS Keychain and Linux desktop SSH agents -- standard practice, but worth understanding.

### Cleanup: end of session

When you are done working with the server, flush the keys from the agent. Run in any terminal:

```
C:\Windows\System32\OpenSSH\ssh-add.exe -D
```

This removes all decrypted keys from memory immediately. The agent service keeps running but holds nothing.

### Full teardown (if you no longer need this)

Run in **PowerShell (Admin)**:

```powershell
# Remove keys from agent
C:\Windows\System32\OpenSSH\ssh-add.exe -D

# Stop the agent
Stop-Service ssh-agent

# Prevent it from starting on boot
Set-Service -Name ssh-agent -StartupType Disabled
```

Optionally delete `C:\Users\GC\.ssh\config` and remove the alias block from `C:\Users\GC\.bashrc`.

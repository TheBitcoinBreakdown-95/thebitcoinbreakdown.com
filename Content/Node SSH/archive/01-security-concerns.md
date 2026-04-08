# Security Concerns: SSHing into Your Bitcoin Node

Running a Bitcoin full node is one of the most sovereign things you can do. But once you start SSHing into it to run commands, you're opening a door -- and you should understand exactly what that means.

This guide covers the real security concerns, what matters, what doesn't, and how to stay safe.

---

## What SSH Access Actually Means

SSH (Secure Shell) gives you a command-line terminal on your server, remotely. If your server runs Bitcoin Core, SSH lets you interact with it directly -- checking the mempool, verifying the money supply, inspecting blocks.

But SSH access is **full system access**. Depending on your setup, logging in via SSH may give you root-level control over the entire server. That's powerful and worth respecting.

On a typical StartOS setup, the SSH user (`start9`) has passwordless `sudo`, meaning there's no second gate between "logged in" and "full control."

---

## 1. Network Exposure: Who Can Reach Your Server?

This is the single most important factor.

| Setup | Risk Level | Who can attempt to connect |
|-------|-----------|---------------------------|
| LAN-only (recommended) | Lower | Only devices on your home network |
| Port 22 forwarded on router | High | Anyone on the internet |
| SSH over Tor hidden service | Medium | Anyone who discovers the .onion address |

**If your node is LAN-only** (the default for most home setups), the attack surface is limited to your local network. An attacker would need to be on your WiFi or compromise a device that is.

**Never port-forward port 22.** Automated bots scan the entire internet for open SSH ports 24/7. If you need remote access to your node, use a VPN or Tor -- never raw SSH over the open internet.

---

## 2. SSH Key Security

Your SSH private key is the credential that proves you're allowed to connect. Protecting it is non-negotiable.

**Best practices:**
- **Use Ed25519 keys** -- the current standard. Faster, smaller, and more secure than older RSA keys.
- **Set a strong passphrase** on the key. This means even if someone copies your key file, they can't use it without the passphrase.
- **Never share the private key file.** The public key (`.pub`) is safe to share -- that's its whole purpose.
- **Disable password authentication** on the server so that only key-based login works. Most node operating systems (StartOS, Umbrel, RaspiBlitz) do this by default.

**What if your key is stolen?**
- With a passphrase: the attacker still needs to crack it. A strong passphrase makes this infeasible.
- Without a passphrase: the attacker has immediate access to your server.

---

## 3. What an Attacker Could Do with SSH Access

If someone obtained your private key and passphrase, here's what's at stake:

### On the server
- Stop, start, or reconfigure any service (Bitcoin Core, Electrs, etc.)
- Read Bitcoin Core's configuration files (which contain RPC credentials)
- Modify the server's configuration or install malware
- Use the server to attack other devices on your network
- Wipe or encrypt the blockchain data (painful -- hundreds of gigabytes to re-download)

### On Bitcoin Core specifically
- If a hot wallet is loaded with funds: potentially send bitcoin
- Shut down the node
- Change configuration to connect to malicious peers
- View transaction history of any loaded wallet

### What they can NOT do
- **Steal bitcoin from a hardware wallet** that connects through this node. The node validates transactions but never holds the hardware wallet's private keys.
- **Compromise the Bitcoin network.** A single node has no special authority -- it's one of tens of thousands.
- **Access funds in external wallets** that merely connect to this node via Electrum Server (Electrs). Those wallets hold their own keys.

This is the key distinction: **your node is a verification tool, not a custody tool.** If you use a hardware wallet, SSH access to your node is a privacy/convenience concern, not a funds-at-risk concern.

---

## 4. SSH Agent Risks (Desktop/Laptop)

If you use an SSH agent to avoid retyping your passphrase every time:

- The agent holds your **decrypted key in memory**. Any process running as your user can silently request the agent to sign an authentication challenge.
- This means malware, a compromised browser extension, or a rogue script could SSH to your server without your knowledge.
- The agent does **not** prompt you when a process uses the key -- it signs silently.

**Mitigations:**
- Flush the agent when you're done working: `ssh-add -D`
- Don't leave the agent loaded while running untrusted software
- Understand that this is the same security model used by every developer with GitHub SSH keys -- standard practice, but worth knowing about

---

## 5. Passwordless Sudo

Many node operating systems configure the SSH user with passwordless `sudo` (root access without a password prompt). This is a convenience choice, but it means:

- There's no distinction between "logged in" and "has root access"
- A compromised SSH session immediately has full system control
- There's no additional prompt before destructive commands

This is generally acceptable for a single-user home server, but you should know it's there.

---

## 6. Bitcoin-Specific Concerns

### Hot wallets
Check if any wallets are loaded on your node:
```bash
bitcoin-cli listwallets
```
If wallets are loaded and unencrypted, anyone with SSH access can spend from them. This is why the standard recommendation is: **use a hardware wallet, and let the node handle validation only.**

### RPC credentials
Bitcoin Core uses a username/password for its RPC interface, stored in `bitcoin.conf`. With SSH access, these are readable. If the RPC port is exposed beyond localhost, this is an additional attack surface.

### Configuration tampering
An attacker with access could modify `bitcoin.conf` to add malicious peer addresses, disable transaction relay, or change RPC settings. On a StartOS system, these changes may be overwritten when the service restarts, which actually provides some protection.

---

## 7. Risk Summary

| Threat | Typical Exposure | Why |
|--------|-----------------|-----|
| Internet attacker brute-forces SSH | None (if LAN-only) | SSH not exposed to internet |
| Device on LAN attacks SSH port | Very low | Would need to steal the key |
| Malware on PC uses SSH agent | Low | Agent only active during sessions |
| Physical theft of PC + key file | Low | Key is passphrase-protected |
| Physical theft of server | Medium | Disk data exposed (mitigate with encryption) |
| Funds stolen via bitcoin-cli | None (if using hardware wallet) | Node doesn't hold spending keys |

---

## 8. Checklist Before You Start

- [ ] Use Ed25519 SSH keys with a strong passphrase
- [ ] Confirm key-only authentication (no password login) on the server
- [ ] Confirm port 22 is NOT forwarded on your router
- [ ] Check that no hot wallets are loaded on the node (`bitcoin-cli listwallets`)
- [ ] Use a hardware wallet for any funds -- the node is for validation only
- [ ] Keep your node OS updated (security patches)
- [ ] Flush the SSH agent when done with your session

---

## The Bottom Line

SSHing into your Bitcoin node is safe when done correctly. The key principles:

1. **Keep SSH LAN-only.** Never expose it to the internet.
2. **Protect your key.** Strong passphrase, never share the private key file.
3. **Don't store funds on the node.** Use a hardware wallet. Let the node verify, not hold.
4. **Clean up after yourself.** Flush the SSH agent when you're done.

Your node is a window into the Bitcoin network -- SSH just gives you a way to look through it. As long as you're not storing the keys to the kingdom on the same machine, the risk is manageable and the capability is worth it.

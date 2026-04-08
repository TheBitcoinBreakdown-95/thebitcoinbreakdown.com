# Security

You now have remote access to your Bitcoin node. That's a powerful thing, and it's worth understanding exactly what it means before you start using it.

This isn't a scare-you-into-quitting lesson. The risks are manageable and the setup you just completed is solid. But SSH access is full system access, and you should know what that implies.

---

## What You Just Opened

SSH gives you a command-line terminal on your server. On StartOS, the SSH user (`start9`) has passwordless `sudo` -- meaning there's no second gate between "logged in" and "full control." Once you're in, you can do anything on the server.

For this course, we only use read-only commands. You're asking questions, not changing anything. But the access itself is broader than what we use it for.

---

## Who Can Reach Your Node?

This is the most important factor.

| Setup | Risk | Who can attempt to connect |
|-------|------|---------------------------|
| LAN-only (your setup) | Lower | Only devices on your home network |
| Port 22 forwarded on router | High | Anyone on the internet |
| SSH over Tor hidden service | Medium | Anyone who discovers the .onion address |

Your node is LAN-only by default. An attacker would need to be on your WiFi or compromise a device that is.

**Never forward port 22 on your router.** Automated bots scan the entire internet for open SSH ports around the clock. If you need remote access, use a VPN or Tor -- never raw SSH over the open internet.

---

## What's at Stake

If someone obtained your SSH key and passphrase, here's what they could do:

**On the server:**
- Stop, start, or reconfigure services (Bitcoin Core, Electrs, etc.)
- Read configuration files (which contain RPC credentials)
- Modify settings or install malware
- Use your server to attack other devices on your network
- Wipe the blockchain data (hundreds of gigabytes to re-download)

**On Bitcoin Core:**
- View transaction history of any loaded wallet
- If a hot wallet is loaded with funds: potentially send bitcoin
- Change configuration to connect to malicious peers
- Shut down the node

**What they can NOT do:**
- **Steal bitcoin from a hardware wallet** connected through this node. The node validates transactions but never holds the hardware wallet's private keys.
- **Compromise the Bitcoin network.** Your node is one of tens of thousands. It has no special authority.
- **Access funds in external wallets** that connect via Electrum Server. Those wallets hold their own keys.

This is the key distinction: your node is a verification tool, not a custody tool. If you use a hardware wallet, SSH access is a privacy and convenience concern, not a funds-at-risk concern.

---

## Protecting Your Key

Your SSH private key is the credential. Protecting it is straightforward:

- **You already set a passphrase** -- this means even if someone copies your key file, they can't use it without cracking the passphrase
- **The private key never leaves your machine** -- SSH proves you have it without transmitting it
- **Key-only authentication** is enabled by default on StartOS -- password login is disabled, so there's nothing to brute-force

Keep the private key on your laptop. Don't copy it to cloud storage, USB drives, or other machines. If you need SSH access from a second device, generate a second key pair and register it separately.

---

## The SSH Agent Trade-Off

If you set up the SSH agent in Step 6 (so Claude can connect without a passphrase prompt), there's a trade-off to understand:

- The agent holds your **decrypted key in memory**. Any process running as your user can silently ask the agent to sign an authentication challenge.
- This means malware, a compromised browser extension, or a rogue script could SSH to your server without your knowledge.
- The agent does **not** prompt you when a process uses the key -- it signs silently.

This is the same security model used by every developer with GitHub SSH keys. It's standard practice. But you should:

- **Flush the agent when you're done working:** `ssh-add -D`
- **Don't leave the agent loaded while running untrusted software**
- **Think of agent time as a session** -- load the key when you need it, flush it when you're done

---

## Hot Wallets

Check if any wallets are loaded on your node:

```bash
ssh mynode "sudo podman exec bitcoind.embassy bitcoin-cli listwallets"
```

If wallets are loaded and unencrypted, anyone with SSH access can spend from them. This is why the standard recommendation is: **use a hardware wallet, and let the node handle validation only.**

Your node's job is to verify. Your hardware wallet's job is to hold keys. Keep those jobs separate.

---

## Checklist

Before moving on, confirm:

- [ ] You used an Ed25519 key with a strong passphrase
- [ ] Your node has key-only authentication (StartOS default -- no action needed)
- [ ] Port 22 is NOT forwarded on your router
- [ ] No hot wallets are loaded on the node (or if they are, you understand the risk)
- [ ] If using the SSH agent, you know to flush it when done (`ssh-add -D`)
- [ ] You're using a hardware wallet for any real funds

---

## The Bottom Line

SSH to a LAN-only node with a passphrase-protected key is a low-risk setup. The encrypted tunnel, the key pair authentication, and the LAN-only exposure give you a strong security posture without any additional configuration.

The rules are simple: protect your key, don't expose the port, don't store funds on the node, and flush the agent when you're done.

Now let's use this access for what it was built for.

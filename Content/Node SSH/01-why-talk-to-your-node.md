# Why Talk to Your Node

You bought a Bitcoin node. You plugged it in, synced the blockchain, and now it sits in your closet humming away. It's validating every transaction and every block -- enforcing Bitcoin's rules without asking anyone for permission.

But right now, you're taking its word for it. You haven't actually looked.

This course changes that. By the end, you'll be able to ask your node direct questions -- how many bitcoin exist, what's in the mempool, how much would it cost to get a transaction confirmed right now -- and get answers that come from your own copy of the blockchain. Not a website. Not an app. Your hardware, your data, your verification.

---

## What We're Building Toward

Here's what it looks like when we're done. You open Claude (or any AI assistant with terminal access) and say:

> "Check my node's block height and tell me what's in the mempool."

Claude connects to your node over SSH, runs the commands, and comes back with:

> "Your node is at block 940,219 -- fully synced. The mempool has 45,231 unconfirmed transactions totaling 23.8 MB, with a minimum relay fee of 1 sat/vbyte. Next-block fee estimate is about 12 sats/vbyte."

Or you ask:

> "Verify the total bitcoin supply."

And a few minutes later:

> "Your node counted every unspent output in the blockchain. Total supply: 20,000,457.41 BTC across 164.9 million UTXOs. This matches the expected issuance schedule -- no extra bitcoin have been created."

That's the goal. Your node already knows all of this. We're just opening a channel so you can ask.

---

## What SSH Is (One Paragraph)

SSH (Secure Shell) is a way to remotely control a computer using text commands. Instead of sitting in front of your node, you type commands from your laptop and they execute on the node as if you were there. It uses a key pair for security -- a private key on your laptop (like a password file) and a public key on your node (like a lock). If they match, you're in. The connection is encrypted end-to-end, so nobody on your network can see what you're doing.

That's all SSH is. A secure text tunnel between your laptop and your node.

---

## Why This Matters

Bitcoin's entire value proposition rests on one idea: you don't have to trust anyone. Not a bank, not an exchange, not a block explorer website. You can verify everything yourself.

But most node runners don't. They plug in the hardware, check the dashboard occasionally, and trust that it's working. The blockchain data sitting on that device is the most complete, independently verified financial record in existence -- and they never look at it directly.

When you check your balance on a block explorer, you're trusting that website to show you accurate data. When you look up a transaction on a third-party app, you're trusting their server. When you check the current block height on some dashboard, you're trusting whoever runs it.

None of that trust is necessary. Your node has the same data. It verified every byte of it. The only thing missing is a way to ask it questions.

That's what this course sets up.

---

## How This Course Works

The setup takes about 30 minutes. You'll generate an SSH key, register it with your node, and connect. After that, you (or Claude) can query your node anytime.

Throughout this course, Claude runs most of the commands for you. You tell Claude what you want to know, and it handles the SSH connection and the `bitcoin-cli` syntax. This is practical -- the commands are long, the output is raw JSON, and Claude can translate both directions.

But there's a tension worth naming. A course about not trusting third parties is asking you to trust an AI to talk to your node. We think that's the right trade-off for learning -- Claude is a tool running on your machine, executing commands you can see and audit. It's not a custodian or a gatekeeper. It can't move your bitcoin or change your node's configuration with the read-only commands we use here.

Still, you should know how to do this yourself. The core lessons use Claude as the interface, but every command Claude runs is a `bitcoin-cli` command you could type manually. Appendix A covers the full command reference and the container architecture, so you can go direct whenever you want. And in Lesson 4, you'll run at least one command yourself -- no Claude, no shortcut -- so you feel what direct access is like.

---

## What You Need

- A **StartOS node** running Bitcoin Core, fully synced
- A **laptop or desktop** on the same local network as your node
- **Claude Code** (or any AI assistant with terminal access) -- recommended but not required
- About **30 minutes** for the initial setup

No programming experience required. No Linux experience required. If you can type and follow instructions, you can do this.

---

## Course Outline

**Core Lessons:**

1. **Why Talk to Your Node** -- you're here
2. **Setup** -- generate an SSH key, register it with StartOS, connect
3. **Security** -- what SSH access means, how to stay safe, the checklist
4. **Your First Verification** -- verify the money supply, check the mempool, estimate fees
5. **What Your Node Sees** -- network connections, peer activity, mining, difficulty

**Reference Appendix:**

- **A: Under the Hood** -- container model, bitcoin-cli command reference, manual operation
- **B: Tips and Troubleshooting** -- shortcuts, common errors, server maintenance

Let's get connected.

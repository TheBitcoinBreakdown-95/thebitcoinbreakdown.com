# Your First Verification

This is the lesson the setup was for. You're about to independently verify facts about Bitcoin using your own node -- no websites, no APIs, no trust required.

If you're using Claude, tell it what you want to know and it will run the commands over SSH. If you want to understand what's happening under the hood, Appendix A covers every command in detail.

---

## Is Your Node Synced?

Before verifying anything, make sure your node is caught up with the network. Ask Claude:

> "Check if my node is fully synced."

Claude runs `getblockchaininfo` and checks two things:
- `blocks` equals `headers` (your node has downloaded and validated all known blocks)
- `verificationprogress` is at or near 1 (100% verified)

If your node is still syncing, the numbers below won't match the current state of the network. Wait until it's done.

### What "synced" actually means

Your node downloaded every block ever produced -- starting from the genesis block in January 2009 -- and independently validated every transaction in every one of them. It checked every signature, verified every input was unspent, confirmed every coinbase reward was correct, and enforced every consensus rule. That's what `verificationprogress: 1` means. Not "I downloaded the data." But "I checked all of it."

---

## Verify the Money Supply

This is the command that makes running a node worth it.

Ask Claude:

> "Verify the total bitcoin supply on my node."

Claude runs `gettxoutsetinfo`, which scans every unspent transaction output (UTXO) in the entire blockchain. This takes several minutes -- it's counting over 160 million individual outputs and summing them.

The result will look something like:

| Field | Value | Meaning |
|-------|-------|---------|
| Total supply | ~20,000,457 BTC | Every bitcoin that currently exists |
| UTXO count | ~164.9 million | Individual unspent outputs |
| Transactions | ~114.4 million | Total transactions ever processed |
| UTXO set size | ~11.3 GB | How much space the state takes on disk |

### What you just did

You independently verified that approximately 20 million bitcoin exist. Not because a website told you. Not because an exchange reported it. Because your node counted every single unspent output and summed them up.

This is what "don't trust, verify" looks like in practice.

Bitcoin's issuance schedule says roughly 19.8 million BTC should have been mined by now (the number creeps toward 21 million over the next century). Your node's count should match the expected issuance. If it didn't -- if someone had inflated the supply -- your node would have rejected the invalid blocks during sync. The fact that it synced successfully is itself a verification.

### The UTXO set hash

The result also includes a field called `hash_serialized_3` -- a cryptographic fingerprint of the entire UTXO set. If your hash matches another node's hash at the same block height, you've both independently proven you agree on the exact state of every bitcoin in existence. No coordination needed. No trust required. Just math.

---

## Check the Mempool

The mempool is where unconfirmed transactions wait to be included in a block. Every node maintains its own mempool.

Ask Claude:

> "What's in my node's mempool right now?"

The key numbers:

| Field | What it tells you |
|-------|------------------|
| Transaction count | How many transactions are waiting for confirmation |
| Total size | Combined size in bytes -- relates to how many blocks it would take to clear |
| Total fees | Sum of all fees waiting to be collected by miners |
| Minimum fee | The lowest fee rate your mempool will accept (rises when the mempool is full) |

### Why this matters

When the mempool is large and fees are high, the network is busy. When it's small and fees are low, it's quiet. Your node sees this in real time, from its own perspective -- based on the transactions its peers have relayed to it.

This is the same data that fee estimation websites show you, but you're not trusting their server. You're reading it directly from your own node's memory.

---

## Estimate Fees

If you're about to send a transaction, you want to know what fee rate will get it confirmed in a reasonable time.

Ask Claude:

> "What's the fee estimate for next-block confirmation? And for within an hour?"

Your node tracks recent blocks to estimate fee rates. The results:

- **Next block (1 block):** The fee rate needed to likely get into the very next block. This is the "urgent" rate.
- **Within an hour (6 blocks):** A more economical rate for transactions that can wait.
- **Within a day (144 blocks):** The cheapest rate that will still confirm eventually.

The fee rate is expressed in **sats/vbyte** -- satoshis per virtual byte of transaction data. A typical transaction is about 140 vbytes, so multiply the rate by 140 to estimate your total fee in satoshis.

Your node's estimate comes from its own observation of recent blocks and mempool conditions. It's not relying on a third-party API -- it watched the blocks come in and calculated the rates itself.

---

## Inspect a Block

Every block has a height (its position in the chain) and a hash (its unique identifier).

Ask Claude:

> "Show me the latest block."

Or pick a specific one:

> "Show me block 100,000."

The interesting fields:

| Field | What it tells you |
|-------|------------------|
| Height | Position in the chain (0 = genesis block) |
| Transaction count | How many transactions the miner included |
| Timestamp | When the miner started working on it |
| Difficulty | Mining difficulty when this block was found |
| Confirmations | How many blocks have been built on top of it |
| Previous block hash | The block before this one -- this is what makes it a chain |

### The Genesis Block

Block 0 -- mined by Satoshi Nakamoto on January 3, 2009. Ask Claude to pull it up. It contains the famous coinbase message: "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks."

Every block since then links back to this one through an unbroken chain of hashes. Your node verified all of them.

---

## Look Up a Transaction

If you have a transaction ID (txid), your node can decode it:

> "Look up this transaction: [paste txid]"

You'll see:
- **Inputs:** where the bitcoin came from
- **Outputs:** where it went and how much
- **Fee:** how much the sender paid the miner
- **Block:** which block confirmed it (or "mempool" if it's still unconfirmed)

You can also check whether a specific output has been spent:

> "Is this output still unspent? [txid, output index]"

If it returns data, the bitcoin is still sitting there. If it returns nothing, it's been spent.

---

## Do It Yourself

You've been letting Claude handle the commands. Now try one yourself.

Open your terminal and type this exactly:

```bash
ssh mynode "sudo podman exec bitcoind.embassy bitcoin-cli getblockcount"
```

That's it. One command. Your laptop connects to your node over SSH, reaches into the Bitcoin Core container, asks for the current block height, and prints the number.

No AI. No website. No intermediary. Your laptop asked your node a question and got a direct answer.

The number you see is the block height your node has verified -- every block from genesis to that number, independently validated by your hardware. Every block explorer in the world should show the same number. If one doesn't, the question isn't whether your node is wrong.

This is the feeling the rest of the course is built on. Everything Claude does for you is this same command with different arguments. The convenience is real, but so is the ability to go direct.

---

## What's Next

You've verified the money supply, checked the mempool, estimated fees, inspected blocks, and run a command yourself. These are the fundamentals.

The next lesson looks at your node's role in the network -- who it's connected to, what it's relaying, and how it participates in Bitcoin's decentralized infrastructure.

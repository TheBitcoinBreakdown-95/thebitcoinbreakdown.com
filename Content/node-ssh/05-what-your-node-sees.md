# What Your Node Sees

Your node isn't just a database of old blocks. It's an active participant in the Bitcoin network -- connected to other nodes, relaying transactions, validating new blocks as they arrive, and maintaining its own view of the network's current state.

This lesson is about understanding that view.

---

## Your Peers

Your node is connected to a handful of other nodes around the world. These are your peers -- the nodes you exchange transactions and blocks with.

Ask Claude:

> "How many peers is my node connected to? Are any on Tor?"

A healthy node typically has 8-10 outbound connections (peers you reached out to) and may accept inbound connections too (peers who found you). The total is usually between 8 and 125, depending on your configuration.

### Why peer count matters

Every transaction you receive and every block you validate comes through your peers. If you had zero peers, your node would be isolated -- it couldn't learn about new blocks or relay transactions. More peers means more redundancy: if one goes down or tries to feed you bad data, the others keep you honest.

You don't need many. Bitcoin is designed so that even a single honest peer is enough to keep you on the correct chain. But more connections mean faster propagation and better resilience.

### What you can learn from peer details

Claude can pull detailed information about each peer: their IP address (or Tor `.onion` address), what version of Bitcoin Core they're running, how long you've been connected, and how much data you've exchanged.

Interesting things to ask about:

- **Tor peers:** Connections over the Tor network show up with `.onion` addresses. StartOS routes through Tor by default, so many of your peers may be Tor connections.
- **Inbound vs. outbound:** Outbound peers are ones you chose. Inbound peers found you. A mix of both is healthy.
- **Version diversity:** Your peers may run different versions of Bitcoin Core (or even different implementations). As long as they follow the consensus rules, this works fine -- and it's good for the network.
- **Data exchanged:** High byte counts mean active peers. If a peer has been connected for days but barely exchanged data, it might be a passive connection.

---

## The Mempool in Motion

You checked the mempool in the previous lesson. Here's the deeper picture of what's actually happening.

Every time someone broadcasts a transaction, it ripples through the network from node to node. Your node receives it from a peer, validates it (checks that the inputs are unspent, the signatures are valid, the fee meets the minimum), and adds it to its mempool. Then it relays the transaction to its other peers.

This means your mempool is *your node's view* of unconfirmed transactions. It's not identical to every other node's mempool -- transactions propagate at different speeds, nodes have different minimum fee policies, and mempool size limits vary. But in practice, well-connected nodes agree on most of the mempool most of the time.

### When the mempool gets full

Your node allocates a fixed amount of memory for the mempool (300 MB by default). When it fills up, the node starts dropping the lowest-fee transactions to make room for higher-fee ones. The `mempoolminfee` field rises -- your node is being selective about what it keeps.

This is the market for block space in action. When demand exceeds supply (more transactions than can fit in the next block), fees rise. When demand drops, fees fall. Your node watches this happen in real time.

Ask Claude:

> "Is the mempool full right now? What's the minimum fee to get in?"

---

## Fee Dynamics

Fee estimation isn't just a number -- it's your node's analysis of recent history.

Bitcoin Core looks at the last several hundred blocks and tracks which fee rates got confirmed in how many blocks. From this, it builds a statistical model: "Based on recent history, a transaction paying X sats/vbyte has a Y% chance of confirming within N blocks."

This is more sophisticated than most fee estimation websites, which often just look at the current mempool. Your node's estimate accounts for how quickly the mempool has been clearing, how fee rates have been trending, and how much variance there's been.

### Reading fee trends

Ask Claude to compare estimates at different time horizons:

> "What are the fee estimates for 1 block, 6 blocks, and 144 blocks?"

If the gap between next-block and next-day is large, the network is congested -- there's a premium for urgency. If they're close together, the network is quiet and patience doesn't save much.

You can also ask for a snapshot over time:

> "What were the fee estimates yesterday? How do they compare to now?"

This gives you a sense of whether fees are trending up or down -- useful context before sending a transaction.

---

## Mining and Difficulty

Your node tracks the current mining difficulty and estimates the total network hash rate.

### Difficulty

Mining difficulty adjusts every 2,016 blocks (roughly two weeks). The adjustment keeps the average block time at 10 minutes regardless of how much computing power is on the network. If miners join, difficulty goes up. If they leave, it goes down.

Ask Claude:

> "What's the current mining difficulty? When was the last adjustment?"

### Network hash rate

Your node estimates the total hash rate by looking at how quickly blocks are being found relative to the difficulty target. This is an estimate, not a measurement -- nobody can directly observe the total hash power.

> "What's the estimated network hash rate?"

The number is staggeringly large. As of early 2026, the Bitcoin network computes hundreds of exahashes per second -- more computational work per second than any other system in human history. This is what secures the ledger you just queried.

---

## Bandwidth

Your node sends and receives data constantly -- relaying transactions, sharing blocks, responding to peer requests.

Ask Claude:

> "How much data has my node sent and received since it last started?"

This is useful for monitoring. If you're on a metered connection or a low-bandwidth setup, knowing your node's data usage helps you plan. A fully synced node with default settings typically uses 50-200 GB per month, mostly from relaying transactions and serving blocks to peers.

---

## Your Node's Identity

Your node broadcasts a version string to its peers -- something like `/Satoshi:28.0.0/`. This tells the network what software you're running.

Ask Claude:

> "What version of Bitcoin Core is my node running? What networks is it connected to?"

The networks field shows whether your node is reachable over IPv4, IPv6, Tor, or I2P. StartOS nodes are typically Tor-connected, which provides privacy -- your peers see your `.onion` address, not your home IP.

---

## Putting It Together

Your node is a window into the Bitcoin network. Through it, you can see:

- **The complete ledger:** every transaction ever confirmed, every UTXO in existence
- **The current market for block space:** mempool size, fee rates, confirmation estimates
- **The network's infrastructure:** your peers, their software, the data flowing between you
- **The security model:** hash rate, difficulty, block production rate

Every piece of this data is independently verified by your hardware. Your node didn't download someone else's conclusions -- it checked everything from scratch.

This is what it means to run a full node. Not just "I have one." But "I can see what it sees."

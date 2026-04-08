# Network, Mempool, and Fees

Your node is a participant in the Bitcoin network -- connected to other nodes, relaying transactions, and validating blocks. This section shows you how to see what's happening in real time.

---

## Your Network Connections

### How many peers are you connected to?
```bash
bitcoin-cli getconnectioncount
```

A healthy node typically has 8-10 outbound connections and may accept inbound connections too (if port 8333 is reachable).

### Network overview
```bash
bitcoin-cli getnetworkinfo
```

Key fields:
| Field | Meaning |
|-------|---------|
| `version` | Your Bitcoin Core version number |
| `subversion` | The user agent string your node broadcasts |
| `connections` | Total peers |
| `connections_in` | Inbound connections (others connecting to you) |
| `connections_out` | Outbound connections (you connecting to others) |
| `relayfee` | Minimum fee rate your node will relay |
| `networks` | Which networks are active (IPv4, IPv6, Tor, I2P) |

### Detailed peer info
```bash
bitcoin-cli getpeerinfo
```

This shows every peer: their IP address (or Tor .onion), what version they're running, how long you've been connected, how much data you've exchanged, and their sync status. It's a lot of output -- one block per peer.

Interesting things to look for:
- `"network": "onion"` -- peers connected via Tor
- `"inbound": true/false` -- did they connect to you, or you to them?
- `"synced_headers"` and `"synced_blocks"` -- are they fully synced?
- `"bytessent"` and `"bytesrecv"` -- data exchanged with this peer

### Bandwidth totals
```bash
bitcoin-cli getnettotals
```

Shows total bytes sent and received since the node started. Useful for monitoring bandwidth usage.

---

## The Mempool

The mempool (memory pool) is where unconfirmed transactions wait to be included in a block. Every node maintains its own mempool, and they're generally similar but not identical.

### Mempool overview
```bash
bitcoin-cli getmempoolinfo
```

```json
{
  "loaded": true,
  "size": 45231,
  "bytes": 23847562,
  "usage": 98234567,
  "total_fee": 1.87654321,
  "maxmempool": 300000000,
  "mempoolminfee": 0.00001000,
  "minrelaytxfee": 0.00001000
}
```

| Field | Meaning |
|-------|---------|
| `size` | Number of unconfirmed transactions |
| `bytes` | Total size of all mempool transactions |
| `total_fee` | Sum of all fees waiting to be collected by miners |
| `maxmempool` | Maximum memory allocated for the mempool (300 MB default) |
| `mempoolminfee` | Lowest fee rate the mempool will accept (rises when full) |

### List all unconfirmed transactions
```bash
bitcoin-cli getrawmempool
```

This returns a list of every transaction ID in your mempool. It can be thousands of entries.

### Inspect a specific mempool transaction
```bash
bitcoin-cli getmempoolentry "txid"
```

Shows the fee, size, time it entered your mempool, and whether it depends on other unconfirmed transactions.

---

## Fee Estimation

Bitcoin Core tracks recent blocks to estimate what fee rate will get a transaction confirmed within a given number of blocks.

```bash
# What fee rate for next-block confirmation?
bitcoin-cli estimatesmartfee 1

# Within 6 blocks (~1 hour)?
bitcoin-cli estimatesmartfee 6

# Within 144 blocks (~1 day)?
bitcoin-cli estimatesmartfee 144
```

The result:
```json
{
  "feerate": 0.00012345,
  "blocks": 6
}
```

The `feerate` is in BTC per kilobyte. To convert to the more common sats/vbyte format:
- Multiply by 100,000,000 (to get sats per KB)
- Divide by 1,000 (to get sats per vbyte)
- Example: 0.00012345 BTC/KB = 12.345 sats/vbyte

### Why this matters
When you send a transaction, the fee you attach determines how quickly it gets confirmed. Miners prioritize transactions that pay the highest fee per unit of block space. During busy periods, fees rise; during quiet periods, they drop.

Your node's fee estimate is based on **its own observation** of recent blocks and mempool conditions -- not a third-party API.

---

## Mining and Difficulty

### Current mining info
```bash
bitcoin-cli getmininginfo
```

| Field | Meaning |
|-------|---------|
| `difficulty` | Current mining difficulty target |
| `networkhashps` | Estimated network hash rate (hashes per second) |
| `blocks` | Current block height |

### Network hash rate
```bash
# Default: estimated over last 120 blocks
bitcoin-cli getnetworkhashps

# Over the last 2016 blocks (one difficulty period)
bitcoin-cli getnetworkhashps 2016
```

The difficulty adjusts every 2,016 blocks (~2 weeks) to keep the average block time at 10 minutes. If more miners join, difficulty goes up. If miners leave, it goes down.

---

## Quick Status Check

Want a fast snapshot of your node's state? Run these three:

```bash
bitcoin-cli getblockcount
bitcoin-cli getconnectioncount
bitcoin-cli getmempoolinfo
```

Block height, peer count, mempool size -- that tells you your node is synced, connected, and seeing transactions. Everything is healthy.

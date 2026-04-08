# Explore the Blockchain

This is where it gets real. You're about to independently verify facts about Bitcoin using your own node -- no websites, no APIs, no trust required.

---

## Verify the Money Supply

This is the command that makes running a node worth it:

```bash
bitcoin-cli gettxoutsetinfo
```

**Warning:** This takes several minutes. It scans every unspent transaction output (UTXO) in the entire blockchain -- over 160 million of them. Be patient.

The result:
```json
{
  "height": 940219,
  "bestblock": "00000000000000000000ba29...",
  "txouts": 164944839,
  "total_amount": 20000457.40572827,
  "transactions": 114427598,
  "disk_size": 11330369127
}
```

**What you just did:** You independently verified that approximately 20,000,457 BTC exist. Not because a website told you, not because an exchange reported it -- because your node counted every single unspent output and summed them up.

This is what "don't trust, verify" actually looks like.

### Reading the result

| Field | Meaning |
|-------|---------|
| `total_amount` | The total bitcoin supply at this block height |
| `txouts` | Number of unspent transaction outputs (UTXOs) in existence |
| `transactions` | Total transactions that have ever been processed |
| `disk_size` | How much space the UTXO set takes on disk |
| `hash_serialized_3` | Cryptographic fingerprint of the entire UTXO set |

That `hash_serialized_3` value is a fingerprint of the entire UTXO set. If your hash matches another node's hash at the same block height, you've both independently proven you agree on the exact state of every bitcoin in existence.

---

## Inspect a Block

Every block has a hash (its unique ID) and a height (its position in the chain). You can look up either one.

### Get the latest block
```bash
# Get the hash of the most recent block
bitcoin-cli getbestblockhash

# Then get its details
bitcoin-cli getblock "paste-the-hash-here"
```

### Get a block by height
```bash
# Get the hash of block 100,000
bitcoin-cli getblockhash 100000

# Then get its details
bitcoin-cli getblock "paste-the-hash-here"
```

### What's in a block?

```json
{
  "hash": "000000000003ba27aa200b1c...",
  "confirmations": 840220,
  "height": 100000,
  "version": 1,
  "nTx": 4,
  "time": 1293623863,
  "difficulty": 14484.16236122,
  "previousblockhash": "000000000002d01c..."
}
```

| Field | Meaning |
|-------|---------|
| `height` | Position in the chain (0 = genesis block) |
| `nTx` | Number of transactions in this block |
| `time` | Unix timestamp (when the miner started working on it) |
| `difficulty` | Mining difficulty when this block was found |
| `confirmations` | How many blocks have been built on top of this one |
| `previousblockhash` | The block before this one (this is what makes it a chain) |

### Block statistics
```bash
# Detailed stats for any block
bitcoin-cli getblockstats 940000
```

This gives you transaction counts, fee totals, sizes, weights, and more -- a full statistical snapshot of a single block.

---

## Read the Genesis Block

Block 0 -- the very first block, mined by Satoshi Nakamoto on January 3, 2009:

```bash
bitcoin-cli getblockhash 0
bitcoin-cli getblock "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
```

This block contains the famous coinbase message: "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks."

---

## Look Up a Transaction

If you have a transaction ID (txid), you can decode it:

```bash
bitcoin-cli getrawtransaction "txid-here" 1
```

The `1` at the end means "give me readable output" instead of raw hex. You'll see:
- Inputs (where the bitcoin came from)
- Outputs (where it went)
- The amount transferred
- Fee information
- Which block it was confirmed in

### Check if a specific output is unspent
```bash
bitcoin-cli gettxout "txid" 0
```

If it returns data, that output is unspent (the bitcoin is still sitting there). If it returns nothing, it's been spent.

---

## Chain Transaction Stats

Want to know how busy the network has been?

```bash
# Transaction stats over the last 30 days
bitcoin-cli getchaintxstats

# Or specify a window (number of blocks)
bitcoin-cli getchaintxstats 144
```

`144` is roughly one day (144 blocks x 10 minutes = 24 hours). This shows you the average transaction rate over that window.

---

None of these commands change anything. You're reading the blockchain -- the same data every node on the network agrees on. Explore freely.

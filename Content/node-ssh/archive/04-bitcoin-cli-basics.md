# bitcoin-cli Basics

`bitcoin-cli` is the command-line tool that ships with Bitcoin Core. It's how you talk to your node -- asking it questions, checking its status, and inspecting the blockchain.

Every command in this guide follows the same pattern:

```bash
bitcoin-cli <command> [arguments]
```

If you're running commands from outside the container, prepend the container exec:
```bash
# StartOS
sudo podman exec bitcoind.embassy bitcoin-cli <command>

# Umbrel
sudo docker exec bitcoin_bitcoind_1 bitcoin-cli <command>
```

For readability, the rest of this guide shows just `bitcoin-cli`. Adjust for your setup.

---

## Getting Help

Bitcoin Core has built-in documentation for every command.

```bash
# List all available commands
bitcoin-cli help

# Get detailed help for a specific command
bitcoin-cli help getblockchaininfo
```

The `help` output shows the command's arguments, what each field in the response means, and examples. It's the most reliable reference because it matches your exact version of Bitcoin Core.

---

## Command Categories

Commands are grouped by what they do:

### Blockchain -- what's on the chain
| Command | What it tells you |
|---------|------------------|
| `getblockchaininfo` | Chain, block height, sync status, pruning, disk size |
| `getblockcount` | Current block height (just the number) |
| `getbestblockhash` | Hash of the latest block |
| `getblock "hash"` | Full details of a specific block |
| `getblockhash <height>` | Get a block's hash by its height |
| `getdifficulty` | Current mining difficulty |

### Network -- who you're connected to
| Command | What it tells you |
|---------|------------------|
| `getnetworkinfo` | Version, protocol, number of connections |
| `getpeerinfo` | Detailed info on every connected peer |
| `getconnectioncount` | Just the number of peers |
| `getnettotals` | Total bytes sent/received |

### Mempool -- what's waiting to be confirmed
| Command | What it tells you |
|---------|------------------|
| `getmempoolinfo` | Size, transaction count, memory usage |
| `getrawmempool` | List every unconfirmed transaction ID |
| `estimatesmartfee <blocks>` | Estimated fee to confirm in N blocks |

### Mining -- network hashpower
| Command | What it tells you |
|---------|------------------|
| `getmininginfo` | Difficulty, network hashrate, current block size |
| `getnetworkhashps` | Estimated total network hash rate |

### UTXO Set -- the state of all bitcoin
| Command | What it tells you |
|---------|------------------|
| `gettxoutsetinfo` | Total supply, UTXO count, set size (slow -- minutes) |
| `gettxout "txid" n` | Whether a specific output is unspent |

### Transactions -- raw data
| Command | What it tells you |
|---------|------------------|
| `getrawtransaction "txid" 1` | Decode a transaction (1 = human-readable) |
| `decoderawtransaction "hex"` | Decode raw transaction hex |

---

## Reading the Output

Most commands return JSON -- structured data with labeled fields. For example:

```bash
bitcoin-cli getblockchaininfo
```

Returns something like:
```json
{
  "chain": "main",
  "blocks": 940219,
  "headers": 940219,
  "bestblockhash": "00000000000000000000ba29...",
  "difficulty": 145042165424853.3,
  "verificationprogress": 1,
  "pruned": false,
  "size_on_disk": 826789612252
}
```

Key things to look for:
- `"chain": "main"` -- you're on mainnet (not testnet)
- `"blocks"` == `"headers"` -- your node is fully synced
- `"verificationprogress": 1` -- verification is 100% complete
- `"pruned": false` -- you're running a full (non-pruned) node

---

## Your First Commands

Try these in order to get a feel for it:

```bash
# 1. How many blocks has the network produced?
bitcoin-cli getblockcount

# 2. What does your node know about itself?
bitcoin-cli getnetworkinfo

# 3. How many peers are you connected to?
bitcoin-cli getconnectioncount

# 4. What's in the mempool right now?
bitcoin-cli getmempoolinfo

# 5. What would it cost to get into the next block?
bitcoin-cli estimatesmartfee 1

# 6. How about within the next 6 blocks (~1 hour)?
bitcoin-cli estimatesmartfee 6
```

---

Every command is read-only. You're asking questions, not changing anything. You can't break your node by running `bitcoin-cli` queries -- explore freely.

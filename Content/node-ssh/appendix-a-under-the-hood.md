# Appendix A: Under the Hood

This appendix covers what Claude does behind the scenes when it queries your node. If you want to run commands manually, understand the container model, or look up a specific `bitcoin-cli` command, this is the reference.

---

## The Container Model

StartOS doesn't run Bitcoin Core directly on the server. It runs inside a **Podman container** -- an isolated environment that packages the software with everything it needs.

Think of your server as an apartment building. Each service (Bitcoin Core, Electrum Server, Lightning) lives in its own apartment. They share the building's resources but can't interfere with each other.

This means you can't just type `bitcoin-cli` on the server. You need to reach into the container first:

```bash
sudo podman exec bitcoind.embassy bitcoin-cli <command>
```

`exec` means "execute this command inside the named container."

### Opening an interactive shell

If you plan to run several commands, drop into the container directly:

```bash
sudo podman exec -it bitcoind.embassy bash
```

Now you can type `bitcoin-cli` commands without the `podman exec` prefix. Type `exit` to leave and return to the server shell.

### Container management

| Command | What it does |
|---------|-------------|
| `sudo podman ps` | List running containers |
| `sudo podman logs bitcoind.embassy --tail 50` | Last 50 lines of Bitcoin Core logs |
| `sudo podman logs bitcoind.embassy --follow` | Follow logs in real time (Ctrl+C to stop) |
| `sudo podman restart bitcoind.embassy` | Restart Bitcoin Core (safe -- it picks up where it left off) |

### Where data lives

Inside the container, Bitcoin Core's data is at `/root/.bitcoin/`:

| Path | What it is |
|------|-----------|
| `bitcoin.conf` | Configuration (settings, RPC credentials) |
| `blocks/` | The blockchain data (hundreds of GB) |
| `chainstate/` | UTXO set database |
| `wallets/` | Wallet files (if any) |
| `debug.log` | Bitcoin Core's log file |

You generally don't need to touch these. `bitcoin-cli` is the intended interface.

---

## Running Commands Manually

Every command Claude runs follows this pattern:

```bash
ssh mynode "sudo podman exec bitcoind.embassy bitcoin-cli <command>"
```

Or if you're already SSH'd in:

```bash
sudo podman exec bitcoind.embassy bitcoin-cli <command>
```

Or inside the container:

```bash
bitcoin-cli <command>
```

### Create a shortcut

Add an alias to your server's `.bashrc` to skip the `podman exec` prefix:

```bash
ssh mynode
echo 'alias btc="sudo podman exec bitcoind.embassy bitcoin-cli"' >> ~/.bashrc
source ~/.bashrc
```

Now commands are just:

```bash
btc getblockcount
btc getmempoolinfo
btc estimatesmartfee 6
```

### Run a command without logging in

You don't have to open a full SSH session:

```bash
ssh mynode "sudo podman exec bitcoind.embassy bitcoin-cli getblockcount"
```

Connects, runs the command, prints the result, disconnects.

---

## Command Reference

All commands are read-only. You cannot break your node by running these.

### Getting help

```bash
bitcoin-cli help                        # List all commands
bitcoin-cli help getblockchaininfo      # Detailed help for one command
```

The built-in help matches your exact version of Bitcoin Core -- it's the most reliable reference.

### Blockchain

| Command | What it returns |
|---------|----------------|
| `getblockchaininfo` | Chain, height, sync status, pruning, disk size |
| `getblockcount` | Current block height (just the number) |
| `getbestblockhash` | Hash of the latest block |
| `getblock "hash"` | Full details of a specific block |
| `getblockhash <height>` | Block hash by height |
| `getblockstats <height>` | Detailed statistics for one block |
| `getdifficulty` | Current mining difficulty |
| `getchaintxstats` | Transaction rate over time (default: 30 days) |
| `getchaintxstats 144` | Transaction rate over last ~24 hours |

### UTXO set

| Command | What it returns |
|---------|----------------|
| `gettxoutsetinfo` | Total supply, UTXO count, set size (takes minutes) |
| `gettxout "txid" n` | Whether a specific output is unspent |

### Mempool

| Command | What it returns |
|---------|----------------|
| `getmempoolinfo` | Size, tx count, memory usage, min fee |
| `getrawmempool` | List of all unconfirmed transaction IDs |
| `getmempoolentry "txid"` | Details on one mempool transaction |
| `estimatesmartfee <blocks>` | Fee rate for confirmation in N blocks |

### Network

| Command | What it returns |
|---------|----------------|
| `getnetworkinfo` | Version, protocol, connections, networks |
| `getpeerinfo` | Detailed info on every connected peer |
| `getconnectioncount` | Number of peers (just the number) |
| `getnettotals` | Total bytes sent and received |

### Mining

| Command | What it returns |
|---------|----------------|
| `getmininginfo` | Difficulty, hash rate, current block |
| `getnetworkhashps` | Estimated network hash rate |
| `getnetworkhashps 2016` | Hash rate over one difficulty period |

### Transactions

| Command | What it returns |
|---------|----------------|
| `getrawtransaction "txid" 1` | Decoded transaction (1 = human-readable) |
| `decoderawtransaction "hex"` | Decode raw transaction hex |

---

## Reading JSON Output

Most commands return JSON. Here's how to read it:

```bash
bitcoin-cli getblockchaininfo
```

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

Key things to check:
- `"chain": "main"` -- you're on mainnet, not testnet
- `"blocks"` equals `"headers"` -- fully synced
- `"verificationprogress": 1` -- 100% verified
- `"pruned": false` -- running a full (non-pruned) node

---

## Server Commands

These run on the server itself, outside the container:

| Command | What it does |
|---------|-------------|
| `df -h` | Disk space usage (is your drive getting full?) |
| `free -h` | Memory (RAM) usage |
| `uptime` | How long the server has been running |
| `top` | Live CPU/memory view (press `q` to quit) |
| `ls -la` | List files with details |
| `pwd` | Print current directory |

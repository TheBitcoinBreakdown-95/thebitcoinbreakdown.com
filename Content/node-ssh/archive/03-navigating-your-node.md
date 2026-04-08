# Navigating Your Node

You're SSH'd into your server. Now what? Before you start talking to Bitcoin Core, it helps to understand how your node OS organizes things.

---

## The Container Model

Most node operating systems (StartOS, Umbrel, RaspiBlitz) don't run Bitcoin Core directly on the server. Instead, they run it inside a **container** -- an isolated environment that packages the software with everything it needs.

Think of it like this: your server is an apartment building, and each service (Bitcoin Core, Electrum Server, Lightning, etc.) lives in its own apartment. They share the building's resources but can't mess with each other.

| Node OS | Container System | Bitcoin Container Name |
|---------|-----------------|----------------------|
| StartOS | Podman | `bitcoind.embassy` |
| Umbrel | Docker | `bitcoin_bitcoind_1` |
| RaspiBlitz | Docker (or native) | Varies |

This means you can't just type `bitcoin-cli` on the server -- you need to reach **into** the container first.

---

## Running Commands Inside the Container

The pattern is:

```bash
# StartOS (Podman)
sudo podman exec bitcoind.embassy bitcoin-cli <command>

# Umbrel (Docker)
sudo docker exec bitcoin_bitcoind_1 bitcoin-cli <command>
```

`exec` means "execute this command inside the named container."

### Example: check your block height

```bash
# StartOS
sudo podman exec bitcoind.embassy bitcoin-cli getblockcount

# Umbrel
sudo docker exec bitcoin_bitcoind_1 bitcoin-cli getblockcount
```

---

## Opening an Interactive Shell

If you plan to run several commands, it's easier to open a shell inside the container:

```bash
# StartOS
sudo podman exec -it bitcoind.embassy bash

# Umbrel
sudo docker exec -it bitcoin_bitcoind_1 bash
```

The `-it` flags give you an **i**nteractive **t**erminal. Now you're inside the container and can run `bitcoin-cli` directly:

```bash
bitcoin-cli getblockcount
bitcoin-cli getmempoolinfo
bitcoin-cli getnetworkinfo
```

Type `exit` to leave the container and return to the server shell.

---

## Useful Server Commands

These work on the server itself (outside the container):

| Command | What it does |
|---------|-------------|
| `ls` | List files in current directory |
| `ls -la` | List files with details (size, permissions, dates) |
| `cd /path/to/dir` | Change directory |
| `pwd` | Print current directory |
| `df -h` | Disk space usage (how full is your drive?) |
| `free -h` | Memory (RAM) usage |
| `uptime` | How long the server has been running |
| `top` | Live view of CPU/memory usage (press `q` to quit) |

## Useful Container Commands

| Command | What it does |
|---------|-------------|
| `sudo podman ps` | List running containers (StartOS) |
| `sudo docker ps` | List running containers (Umbrel) |
| `sudo podman logs bitcoind.embassy --tail 50` | Last 50 lines of Bitcoin Core logs (StartOS) |
| `sudo docker logs bitcoin_bitcoind_1 --tail 50` | Last 50 lines of Bitcoin Core logs (Umbrel) |

---

## Where Bitcoin Core Stores Its Data

Inside the container, Bitcoin Core's data lives at `/root/.bitcoin/`. This directory contains:

| File/Folder | What it is |
|-------------|-----------|
| `bitcoin.conf` | Configuration file (settings, RPC credentials) |
| `blocks/` | The actual blockchain data (hundreds of GB) |
| `chainstate/` | UTXO set database |
| `wallets/` | Wallet files (if any) |
| `debug.log` | Bitcoin Core's log file |

You generally don't need to touch these files directly -- `bitcoin-cli` is the intended interface. But knowing they're there helps you understand what's happening under the hood.

---

Now that you know where things are, let's start running real commands.

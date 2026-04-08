# Tips and Troubleshooting

Practical shortcuts, common errors, and how to fix them.

---

## Tips

### Create a shortcut alias

Typing `sudo podman exec bitcoind.embassy bitcoin-cli` every time is tedious. Add an alias to your server's `.bashrc`:

```bash
# SSH into your server, then:
echo 'alias btc="sudo podman exec bitcoind.embassy bitcoin-cli"' >> ~/.bashrc
source ~/.bashrc
```

Now you can just type:
```bash
btc getblockcount
btc getmempoolinfo
btc estimatesmartfee 6
```

For Umbrel, replace the container name:
```bash
echo 'alias btc="sudo docker exec bitcoin_bitcoind_1 bitcoin-cli"' >> ~/.bashrc
```

### Use an SSH config file

Instead of typing the full connection string, create `~/.ssh/config` on your local machine:

```
Host mynode
    HostName 192.168.1.50
    User start9
    IdentityFile ~/.ssh/id_ed25519_mynode
    IdentitiesOnly yes
```

Then just: `ssh mynode`

### Run a command without logging in

You don't have to open a full SSH session. Run a command directly:

```bash
ssh mynode "sudo podman exec bitcoind.embassy bitcoin-cli getblockcount"
```

This connects, runs the command, prints the result, and disconnects. Useful for quick checks.

### Check your node from your phone

Most SSH apps (Termius, JuiceSSH) support key-based authentication. Import your private key and you can check your node from anywhere on your home network.

---

## Common Errors

### "Connection refused" when SSHing

```
ssh: connect to host 192.168.1.50 port 22: Connection refused
```

**Cause:** SSH server isn't running, or the IP address is wrong.

**Fix:**
- Verify the IP address. Check your router's device list -- IPs can change if you don't have a static lease.
- Restart the server if you have physical access.
- On StartOS, SSH may be disabled by default. Enable it in the dashboard under System > SSH.

### "Permission denied (publickey)"

```
start9@192.168.1.50: Permission denied (publickey).
```

**Cause:** Your key isn't recognized by the server.

**Fix:**
- Make sure you added the **public key** (`.pub` file), not the private key, to the server
- Check that the username is correct (`start9`, `umbrel`, `admin`, etc.)
- Verify you're pointing to the right private key with `-i`
- Check file permissions on the key: `chmod 600 ~/.ssh/id_ed25519_mynode`

### "Could not open a connection to your authentication agent"

```
Could not open a connection to your authentication agent.
```

**Cause:** `ssh-add` can't find a running SSH agent.

**Fix:**
- **Windows:** You may have two `ssh-add` binaries (Git Bash's and Windows OpenSSH's). Use the full path: `C:\Windows\System32\OpenSSH\ssh-add.exe`
- **Mac/Linux:** Start the agent first: `eval $(ssh-agent -s)`

### "Host key verification failed"

```
WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
```

**Cause:** The server's fingerprint changed since your last connection. This can happen if you reinstalled the OS on your server.

**Fix:**
- If you know why it changed (you reinstalled, changed hardware, etc.), remove the old entry:
  ```bash
  ssh-keygen -R 192.168.1.50
  ```
- If you don't know why it changed, investigate before connecting. This warning exists to protect you from man-in-the-middle attacks.

### "error: Could not connect to the server" (bitcoin-cli)

```
error: Could not connect to the server 127.0.0.1:8332
```

**Cause:** Bitcoin Core isn't running, or you're running the command outside the container.

**Fix:**
- Make sure you're running the command inside the container (via `podman exec` or `docker exec`)
- Check if the container is running: `sudo podman ps` or `sudo docker ps`
- Check Bitcoin Core's logs: `sudo podman logs bitcoind.embassy --tail 20`

### "bitcoin-cli: command not found"

**Cause:** You're on the server shell, not inside the container.

**Fix:** Either exec into the container first (`sudo podman exec -it bitcoind.embassy bash`) or use the full `podman exec` / `docker exec` command.

---

## Server Maintenance

### Check disk space
```bash
df -h
```

A full (unpruned) node uses 800+ GB and growing. If your drive fills up, Bitcoin Core will stop.

### Check if services are running
```bash
# StartOS
sudo podman ps

# Umbrel
sudo docker ps
```

### View Bitcoin Core logs
```bash
# Last 50 lines (StartOS)
sudo podman logs bitcoind.embassy --tail 50

# Follow logs in real time (Ctrl+C to stop)
sudo podman logs bitcoind.embassy --follow
```

### Restart Bitcoin Core
```bash
# StartOS (use the dashboard instead if possible)
sudo podman restart bitcoind.embassy

# Umbrel
sudo docker restart bitcoin_bitcoind_1
```

Restarting is generally safe. Bitcoin Core will pick up where it left off.

---

## When to Ask for Help

If you see errors about database corruption, unexpected shutdowns, or "block validation failed," don't try to fix these yourself. Ask in the support channels for your node OS:

- **StartOS:** community.start9.com
- **Umbrel:** community.umbrel.com
- **RaspiBlitz:** GitHub issues or Telegram group
- **General Bitcoin Core:** bitcointalk.org or bitcoin-dev mailing list

# Appendix B: Tips and Troubleshooting

---

## Tips

### Check your node from your phone

Most SSH apps (Termius, JuiceSSH) support key-based authentication. Import your private key and you can check your node from anywhere on your home network.

### Quick status check

Three commands give you a fast snapshot:

```bash
ssh mynode "sudo podman exec bitcoind.embassy bitcoin-cli getblockcount"
ssh mynode "sudo podman exec bitcoind.embassy bitcoin-cli getconnectioncount"
ssh mynode "sudo podman exec bitcoind.embassy bitcoin-cli getmempoolinfo"
```

Block height, peer count, mempool size. If all three return reasonable numbers, your node is synced, connected, and healthy.

Or just ask Claude: "Is my node healthy?"

---

## Common Errors

### "Connection refused" when SSHing

```
ssh: connect to host 192.168.1.50 port 22: Connection refused
```

**Cause:** SSH server isn't running, or the IP address is wrong.

**Fix:**
- Check your node's IP address. IPs can change if you don't have a static lease on your router. Look up the current address in your router's device list or the StartOS dashboard.
- Restart the server if you have physical access.
- Confirm SSH is enabled in the StartOS dashboard under System > SSH.

### "Permission denied (publickey)"

```
start9@192.168.1.50: Permission denied (publickey).
```

**Cause:** The server doesn't recognize your key.

**Fix:**
- Confirm you added the **public key** (`.pub` file), not the private key, to StartOS
- Check that you're pointing to the right private key: `ssh -i ~/.ssh/id_ed25519_mynode ...`
- Verify the username is `start9`
- Check file permissions on your key: `chmod 600 ~/.ssh/id_ed25519_mynode`

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

**Cause:** Your node's fingerprint changed since your last connection. This happens if you reinstalled StartOS or reset the server.

**Fix:**
- If you know why it changed (reinstall, hardware swap), remove the old entry:
  ```bash
  ssh-keygen -R 192.168.1.50
  ```
- If you don't know why, investigate before connecting. This warning protects you from man-in-the-middle attacks.

### "error: Could not connect to the server 127.0.0.1:8332"

```
error: Could not connect to the server 127.0.0.1:8332
```

**Cause:** Bitcoin Core isn't running, or you ran `bitcoin-cli` outside the container.

**Fix:**
- Make sure you're using the `podman exec` prefix: `sudo podman exec bitcoind.embassy bitcoin-cli ...`
- Check if the container is running: `sudo podman ps`
- Check Bitcoin Core's logs: `sudo podman logs bitcoind.embassy --tail 20`

### "bitcoin-cli: command not found"

**Cause:** You're on the server shell, not inside the container.

**Fix:** Either exec into the container first (`sudo podman exec -it bitcoind.embassy bash`) or use the full `podman exec` command from the server shell.

---

## Server Maintenance

### Check disk space

```bash
ssh mynode "df -h"
```

A full (unpruned) node uses 800+ GB and growing. If your drive fills up, Bitcoin Core will stop syncing.

### Check if services are running

```bash
ssh mynode "sudo podman ps"
```

You should see `bitcoind.embassy` in the list. If Electrs is installed, you'll see `electrs.embassy` too.

### View Bitcoin Core logs

```bash
# Last 20 lines
ssh mynode "sudo podman logs bitcoind.embassy --tail 20"
```

### Restart Bitcoin Core

Use the StartOS dashboard when possible (Services > Bitcoin Core > Restart). If you need to do it via SSH:

```bash
ssh mynode "sudo podman restart bitcoind.embassy"
```

This is safe. Bitcoin Core picks up where it left off.

---

## When to Ask for Help

If you see errors about database corruption, unexpected shutdowns, or "block validation failed," don't try to fix these yourself. These are rare but serious.

- **StartOS support:** community.start9.com
- **Bitcoin Core general:** bitcointalk.org or the bitcoin-dev mailing list

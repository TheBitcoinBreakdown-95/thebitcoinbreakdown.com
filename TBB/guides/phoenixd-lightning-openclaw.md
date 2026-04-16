---
title: "Self-Custodial Lightning for OpenClaw: phoenixd + Dashboard + Lightning Address"
description: "Step-by-step guide to adding a Lightning wallet, dashboard tab, and public Lightning address to your OpenClaw agent. No KYC, no custodian, no channel management."
pubDate: 2026-04-16
author: "The Bitcoin Breakdown"
tags: ["lightning", "openclaw", "phoenixd", "self-custody", "tutorial"]
draft: false
---

> Step-by-step guide to adding a Lightning wallet, dashboard tab, and public Lightning address to your OpenClaw agent. No KYC, no custodian, no channel management.

**Time:** ~2 hours (most of it waiting for channel confirmation)

**Requirements:** OpenClaw running on Ubuntu, SSH access to the machine, a domain (for Lightning address)

---

## Table of Contents

1. [Why phoenixd](#1-why-phoenixd)
2. [Install phoenixd](#2-install-phoenixd)
3. [Run as a systemd service](#3-run-as-a-systemd-service)
4. [Dashboard proxy routes](#4-dashboard-proxy-routes)
5. [Dashboard Lightning tab (frontend)](#5-dashboard-lightning-tab-frontend)
6. [Fund your first channel](#6-fund-your-first-channel)
7. [LNURL-pay server (Lightning address)](#7-lnurl-pay-server-lightning-address)
8. [Tailscale Funnel (public exposure)](#8-tailscale-funnel-public-exposure)
9. [DNS: the .well-known file](#9-dns-the-well-known-file)
10. [How a payment flows](#10-how-a-payment-flows)
11. [Maintenance](#11-maintenance)
12. [Troubleshooting](#12-troubleshooting)

---

## 1. Why phoenixd

phoenixd is the server version of the Phoenix mobile wallet by ACINQ. It wins for OpenClaw because:

- **Self-custodial** -- you hold your own keys
- **No KYC** -- ACINQ's LSP opens channels automatically, no account needed
- **Zero channel management** -- ACINQ handles opens, splices, and liquidity
- **Clean HTTP API** -- single process, REST endpoints, HTTP Basic Auth
- **Lightweight** -- Kotlin Native binary, no JVM, no Docker

Alternatives like LND or CLN require manual channel management and are significantly more complex. phoenixd trades some control for simplicity -- the right trade for most agent setups.

---

## 2. Install phoenixd

SSH into your OpenClaw machine:

```bash
# Check you have enough disk (needs < 100MB)
df -h /

# Download latest release
# Check https://github.com/ACINQ/phoenixd/releases for current version
mkdir -p ~/phoenixd && cd ~/phoenixd
wget https://github.com/ACINQ/phoenixd/releases/download/v0.7.3/phoenixd-0.7.3-linux-x64.zip
unzip phoenixd-0.7.3-linux-x64.zip
```

### First run (seed generation)

The first run generates your 12-word seed and API passwords. It requires two interactive confirmations:

```bash
cd ~/phoenixd/phoenixd-0.7.3-linux-x64
echo -e "yes\nyes" | ./phoenixd
# Wait a few seconds for it to initialize, then Ctrl+C
```

This creates `~/.phoenix/` with:
- `seed.dat` -- **your master key. Back this up offline immediately.**
- `phoenix.conf` -- API passwords (full access + limited access) and webhook secret

### Verify the config

```bash
cat ~/.phoenix/phoenix.conf
```

You should see three lines: `http-password`, `http-password-limited-access`, and `webhook-secret`.

---

## 3. Run as a systemd service

If your user does not have sudo access (common on OpenClaw), use `systemctl --user`:

```bash
mkdir -p ~/.config/systemd/user

cat > ~/.config/systemd/user/phoenixd.service << 'EOF'
[Unit]
Description=phoenixd Lightning node
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=/home/YOUR_USERNAME/phoenixd/phoenixd-0.7.3-linux-x64/phoenixd --silent
Restart=on-failure
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=default.target
EOF
```

**Replace `YOUR_USERNAME`** with your actual Linux username (e.g., `openclaw`).

```bash
systemctl --user daemon-reload
systemctl --user enable phoenixd
systemctl --user start phoenixd
```

Verify it's running:

```bash
systemctl --user status phoenixd
# Should show "active (running)"

# Test the API
HTTP_PASS=$(grep "^http-password=" ~/.phoenix/phoenix.conf | head -1 | cut -d= -f2)
curl -u :$HTTP_PASS http://localhost:9740/getinfo
```

### Auto-start on boot

User services only start when the user is logged in. To start at boot without a login session:

```bash
loginctl enable-linger $USER
```

---

## 4. Dashboard proxy routes

The OpenClaw dashboard is an Express.js app (typically at `~/.openclaw/workspace/dashboard/server.js`). phoenixd runs on `127.0.0.1:9740` -- we proxy through the dashboard so phoenixd never touches the network directly.

Add this to `server.js` **before** `app.listen(...)`:

```javascript
// --- Lightning / phoenixd proxy ---
const fs = require('fs');

function phoenixdFetch(endpoint, options = {}) {
  const conf = fs.readFileSync(
    process.env.HOME + '/.phoenix/phoenix.conf', 'utf8'
  );
  const pw1 = conf.match(/http-password=(.+)/)?.[1]?.trim();
  const pw2 = conf.match(
    /http-password-limited-access=(.+)/
  )?.[1]?.trim();
  const password = pw1 || pw2;
  const url = 'http://localhost:9740' + endpoint;
  options.headers = options.headers || {};
  options.headers['Authorization'] =
    'Basic ' + Buffer.from(':' + password).toString('base64');
  if (options.body && !options.headers['Content-Type']) {
    options.headers['Content-Type'] =
      'application/x-www-form-urlencoded';
  }
  return fetch(url, options).then(res => {
    if (!res.ok) throw new Error('phoenixd ' + res.status);
    return res.json();
  });
}

app.get('/api/lightning/info', async (req, res) => {
  try { res.json(await phoenixdFetch('/getinfo')); }
  catch (e) { res.status(500).json({ error: e.message }); }
});

app.get('/api/lightning/balance', async (req, res) => {
  try { res.json(await phoenixdFetch('/getbalance')); }
  catch (e) { res.status(500).json({ error: e.message }); }
});

app.get('/api/lightning/payments', async (req, res) => {
  try {
    const [inc, out] = await Promise.all([
      phoenixdFetch('/payments/incoming?limit=50'),
      phoenixdFetch('/payments/outgoing?limit=50')
    ]);
    res.json({ incoming: inc, outgoing: out });
  } catch (e) { res.status(500).json({ error: e.message }); }
});

app.post('/api/lightning/invoice', async (req, res) => {
  try {
    const { amountSat, description } = req.body;
    if (!amountSat)
      return res.status(400).json({ error: 'amountSat required' });
    const params = new URLSearchParams({
      amountSat: String(amountSat),
      description: description || 'Invoice'
    });
    res.json(await phoenixdFetch('/createinvoice', {
      method: 'POST', body: params.toString()
    }));
  } catch (e) { res.status(500).json({ error: e.message }); }
});

app.get('/api/lightning/channels', async (req, res) => {
  try { res.json(await phoenixdFetch('/channels')); }
  catch (e) { res.status(500).json({ error: e.message }); }
});

app.get('/api/lightning/offer', async (req, res) => {
  try {
    const conf = fs.readFileSync(
      process.env.HOME + '/.phoenix/phoenix.conf', 'utf8'
    );
    const password =
      conf.match(/^http-password=(.+)/m)?.[1]?.trim();
    const auth =
      Buffer.from(':' + password).toString('base64');
    const r = await fetch('http://127.0.0.1:9740/getoffer', {
      headers: { 'Authorization': 'Basic ' + auth }
    });
    const raw = await r.text();
    const offer = raw.startsWith('"')
      ? JSON.parse(raw) : raw.trim();
    res.json({ offer });
  } catch (e) { res.status(500).json({ error: e.message }); }
});

app.post('/api/lightning/payinvoice', async (req, res) => {
  try {
    const { invoice } = req.body;
    if (!invoice)
      return res.status(400).json({ error: 'invoice required' });
    const params = new URLSearchParams({ invoice });
    res.json(await phoenixdFetch('/payinvoice', {
      method: 'POST', body: params.toString()
    }));
  } catch (e) { res.status(500).json({ error: e.message }); }
});

app.post('/api/lightning/lnurlpay', async (req, res) => {
  try {
    const { lnurl, amountSat, message } = req.body;
    if (!lnurl || !amountSat)
      return res.status(400).json({
        error: 'lnurl and amountSat required'
      });
    const params = new URLSearchParams({
      lnurl, amountSat: String(amountSat)
    });
    if (message) params.set('message', message);
    res.json(await phoenixdFetch('/lnurlpay', {
      method: 'POST', body: params.toString()
    }));
  } catch (e) { res.status(500).json({ error: e.message }); }
});

app.post('/api/lightning/paylnaddress', async (req, res) => {
  try {
    const { address, amountSat, message } = req.body;
    if (!address || !amountSat)
      return res.status(400).json({
        error: 'address and amountSat required'
      });
    const params = new URLSearchParams({
      address, amountSat: String(amountSat)
    });
    if (message) params.set('message', message);
    res.json(await phoenixdFetch('/paylnaddress', {
      method: 'POST', body: params.toString()
    }));
  } catch (e) { res.status(500).json({ error: e.message }); }
});
```

Restart the dashboard after adding this:

```bash
# However your dashboard restarts -- typically:
systemctl --user restart openclaw-dashboard
# or: pm2 restart dashboard
# or: kill the process and re-run node server.js
```

---

## 5. Dashboard Lightning tab (frontend)

Add to your dashboard's `index.html`.

### Dependencies

Download qrcode.js (CDN may be unreachable from your server):

```bash
cd ~/.openclaw/workspace/dashboard/public
curl -sL \
  https://cdn.jsdelivr.net/npm/qrcodejs@1.0.0/qrcode.min.js \
  -o qrcode.min.js
# If curl fails, download on another machine and SCP it over
```

Add the script tag in `index.html` before your main `<script>`:

```html
<script src="/qrcode.min.js"></script>
```

### Navigation

Add a Lightning button to your nav:

```html
<button onclick="showSection('lightning',this)">
  <span class="icon">&#x26A1;</span>
  <span class="nav-label">Lightning</span>
</button>
```

And a section div in your content area:

```html
<div id="lightning" class="section"></div>
```

Wire it up in your existing `showSection` function (or equivalent):

```javascript
if (id === 'lightning') loadLightning();
```

### JavaScript

Add this to your `<script>` block. This is the full Lightning tab -- balance, channels, receive (invoice + Bolt12 offer with QR), send (invoice/LNURL/address/Bolt12), and payment history.

The code is ~300 lines of vanilla JavaScript. It renders six cards: Balance, Channels, Receive (with Invoice/Offer sub-tabs), Pay (with Invoice/LNURL/Address/Bolt12 sub-tabs), and Payments history. Each card fetches from your proxy routes and renders inline.

Key functions:

- `loadLightning()` -- fetches balance, info, payments, and channels in parallel, renders all cards
- `lnCreateInvoice()` -- creates an invoice and shows it with a QR code
- `lnLoadOffer()` -- fetches your static Bolt12 offer and shows it with a QR code
- `lnPayInvoice()`, `lnPayLnurl()`, `lnPayAddress()`, `lnPayOffer()` -- payment functions for each method
- `lnShowQR()` -- renders a QR code using the qrcodejs library

One gotcha worth noting: phoenixd's `/createinvoice` returns the invoice string as `data.serialized`, not `data.invoice`. If you see "Cannot read properties of undefined (reading 'toUpperCase')", this is why.

The full frontend code is available in the [source repository](https://github.com/TheBitcoinBreakdown-95/openclaw-lightning). If you want to paste it directly, see the `dashboard-lightning.js` section in the README.

---

## 6. Fund your first channel

phoenixd uses ACINQ's LSP for automatic channel management. When you receive a Lightning payment and have no channel, ACINQ opens one automatically.

1. Create an invoice from your new Lightning tab (e.g., 50,000 sats)
2. Pay it from another wallet (Phoenix mobile, Wallet of Satoshi, etc.)
3. ACINQ opens a channel -- default capacity: 2,000,000 sats

**Fees on first receive:**
- Mining fee: varies with mempool (typically 100-500 sats)
- Service fee: ~1% of received amount
- Channel creation fee: 1,000 sats (one-time)

Check estimated fees before receiving:

```bash
HTTP_PASS=$(grep "^http-password=" \
  ~/.phoenix/phoenix.conf | head -1 | cut -d= -f2)
curl -u :$HTTP_PASS \
  "http://localhost:9740/estimateliquidityfees?amountSat=50000"
```

**Known issue:** ACINQ's dual-funding protocol sometimes returns `TxAbort: "channel funding error"` on the first attempt. Fix: restart phoenixd (`systemctl --user restart phoenixd`), create a fresh invoice, and pay again. Do not reuse the old invoice.

---

## 7. LNURL-pay server (Lightning address)

This is optional but powerful -- it gives your agent a human-readable Lightning address like `agent@yourdomain.com` that anyone can pay from any wallet.

Add this to `server.js` **after** `app.listen(...)`:

```javascript
// --- LNURL-pay server ---
// Replace these three values with your own:
const LNURL_ADDRESS = 'agent@yourdomain.com';
const LNURL_CALLBACK =
  'https://YOUR_FUNNEL_URL/lnurlp/agent/callback';
const LNURL_METADATA = JSON.stringify([
  ['text/identifier', LNURL_ADDRESS],
  ['text/plain', 'Pay via Lightning']
]);

function getLimitedPhoenixdPassword() {
  const conf = fs.readFileSync(
    process.env.HOME + '/.phoenix/phoenix.conf', 'utf8'
  );
  return conf.match(
    /http-password-limited-access=(.+)/
  )?.[1]?.trim();
}

const lnurlApp = express();
lnurlApp.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  next();
});

// Discovery endpoint
// Wallets fetch this to learn how to pay you
lnurlApp.get('/lnurlp/agent', (req, res) => {
  res.json({
    tag: 'payRequest',
    callback: LNURL_CALLBACK,
    metadata: LNURL_METADATA,
    minSendable: 1000,        // 1 sat (in millisats)
    maxSendable: 10000000000  // 10M sats (in millisats)
  });
});

// Callback endpoint
// Wallets call this with the amount, you return an invoice
lnurlApp.get('/lnurlp/agent/callback', async (req, res) => {
  const amountMsat = parseInt(req.query.amount);
  if (!amountMsat || amountMsat < 1000) {
    return res.status(400).json({
      status: 'ERROR',
      reason: 'amount required, minimum 1 sat'
    });
  }
  try {
    const password = getLimitedPhoenixdPassword();
    const params = new URLSearchParams({
      description: LNURL_METADATA,
      amountSat: String(Math.floor(amountMsat / 1000))
    });
    const r = await fetch(
      'http://127.0.0.1:9740/createinvoice',
      {
        method: 'POST',
        headers: {
          'Authorization': 'Basic ' +
            Buffer.from(':' + password).toString('base64'),
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: params.toString()
      }
    );
    if (!r.ok) throw new Error('phoenixd ' + r.status);
    const data = await r.json();
    res.json({ pr: data.serialized, routes: [] });
  } catch (e) {
    res.status(500).json({
      status: 'ERROR', reason: e.message
    });
  }
});

lnurlApp.listen(8089, '127.0.0.1', () => {
  console.log('LNURL-pay server on 127.0.0.1:8089');
});
```

**Security note:** This server uses the limited-access password, which can create invoices but cannot spend funds. Even if the endpoint is compromised, your sats are safe.

---

## 8. Tailscale Funnel (public exposure)

The LNURL callback must be reachable from the public internet. Tailscale Funnel provides this without opening firewall ports or configuring nginx/caddy.

### Prerequisites

1. Tailscale installed and running on your OpenClaw machine
2. Tailscale Funnel enabled in your Tailscale ACL policy (admin console at login.tailscale.com):

```json
"nodeAttrs": [
  {
    "target": ["autogroup:member"],
    "attr": ["funnel"]
  }
]
```

### Enable Funnel

```bash
tailscale funnel --bg 8089
```

This creates a public HTTPS URL like:

```
https://your-machine.tailnet-name.ts.net -> 127.0.0.1:8089
```

Verify:

```bash
tailscale funnel status
```

Your Funnel URL is the `LNURL_CALLBACK` base URL you set in step 7. For example, if your Funnel URL is `https://agent-box.taild1234.ts.net`, then:

```javascript
const LNURL_CALLBACK =
  'https://agent-box.taild1234.ts.net/lnurlp/agent/callback';
```

Tailscale handles TLS certificates automatically.

---

## 9. DNS: the .well-known file

For `agent@yourdomain.com` to work, wallets look up:

```
https://yourdomain.com/.well-known/lnurlp/agent
```

This must return a JSON response (or redirect) that tells the wallet where to find the LNURL callback. The simplest approach: **a static file on your website**.

### Option A: Static file (GitHub Pages, any static host)

Create this file in your website's repo:

```
.well-known/lnurlp/agent
```

(No file extension. Just `agent` as the filename.)

Contents:

```json
{
  "tag": "payRequest",
  "callback": "https://YOUR_FUNNEL_URL/lnurlp/agent/callback",
  "metadata": "[[\"text/identifier\",\"agent@yourdomain.com\"],[\"text/plain\",\"Pay via Lightning\"]]",
  "minSendable": 1000,
  "maxSendable": 10000000000
}
```

**GitHub Pages note:** GitHub Pages may serve this as `application/octet-stream` instead of `application/json`. Wallets accept both -- this is fine.

### Option B: Redirect (if you control server config)

If your domain runs nginx, Apache, or similar, redirect the `.well-known` path to your Tailscale Funnel URL:

```nginx
# nginx example
location /.well-known/lnurlp/agent {
    return 301 https://YOUR_FUNNEL_URL/lnurlp/agent;
}
```

### Option C: Let your agent figure it out

If you have a domain and your agent has SSH access to the server or access to the DNS/hosting provider's API, you can tell it:

> "Set up a Lightning address for me at agent@mydomain.com. The LNURL callback is at https://MY_FUNNEL_URL/lnurlp/agent/callback. Create the .well-known file on my website."

The agent needs to know:
1. Where your website files are hosted (GitHub repo, VPS path, etc.)
2. The Tailscale Funnel URL (from `tailscale funnel status`)
3. The desired Lightning address username

---

## 10. How a payment flows

```
Sender's wallet
  -> fetches https://yourdomain.com/.well-known/lnurlp/agent
     (your website -- static file or redirect)

  -> reads callback URL from the JSON response

  -> calls https://YOUR_FUNNEL_URL/lnurlp/agent/callback?amount=50000000
     (Tailscale Funnel -> your machine)

  -> LNURL server creates invoice via phoenixd API

  -> returns invoice to wallet

  -> wallet pays the invoice over Lightning

  -> phoenixd receives the payment

  -> payment appears in your dashboard
```

---

## 11. Maintenance

### Check if phoenixd is running

```bash
systemctl --user status phoenixd
HTTP_PASS=$(grep "^http-password=" \
  ~/.phoenix/phoenix.conf | head -1 | cut -d= -f2)
curl -u :$HTTP_PASS http://localhost:9740/getinfo
```

### View logs

```bash
# Recent
journalctl --user -u phoenixd -n 50 --no-pager

# Live
journalctl --user -u phoenixd -f
```

### Upgrade phoenixd

```bash
cd ~/phoenixd
wget https://github.com/ACINQ/phoenixd/releases/download/vX.Y.Z/phoenixd-X.Y.Z-linux-x64.zip
unzip phoenixd-X.Y.Z-linux-x64.zip
# Update ExecStart path in ~/.config/systemd/user/phoenixd.service
systemctl --user daemon-reload
systemctl --user restart phoenixd
```

### Backup

Critical files:
- `~/.phoenix/seed.dat` -- master key (back up offline, never store digitally)
- `~/.phoenix/phoenix.conf` -- API passwords

---

## 12. Troubleshooting

| Problem | Fix |
|---------|-----|
| `phoenixd 401` on API calls | Check password in `~/.phoenix/phoenix.conf` matches what you're sending |
| Channel state `Aborted` | `systemctl --user restart phoenixd`, then create a fresh invoice |
| Invoice creation returns undefined | phoenixd returns `serialized`, not `invoice` -- check your frontend code |
| Tailscale Funnel not working | Check ACL policy allows Funnel; run `tailscale funnel status` |
| `.well-known` returns 404 | Verify file exists at the correct path with no extension; check CORS headers |
| QR code library not loading | Download `qrcode.min.js` locally instead of using CDN |
| phoenixd not starting after reboot | Run `loginctl enable-linger $USER` |
| `TxAbort: channel funding error` | Restart phoenixd, create new invoice, pay again (ACINQ transient issue) |

---

## Architecture Summary

```
Public Internet
  |
  v
[Your Domain] .well-known/lnurlp/agent
(static file, GitHub Pages / any host)
  |
  | callback URL points to:
  v
[Tailscale Funnel] https://machine.tailnet.ts.net
(automatic TLS)
  |
  | proxies to:
  v
[LNURL Express Server] 127.0.0.1:8089
(creates invoices only)
  |
  | calls phoenixd API:
  v
[phoenixd] 127.0.0.1:9740
(Lightning node, self-custodial)
  |
  | proxied by:
  v
[OpenClaw Dashboard] 0.0.0.0:4242
(your agent's UI)
```

**Security boundaries:**
- phoenixd: localhost only, never exposed
- Dashboard proxy: Tailscale network only (private)
- LNURL server: public via Funnel, but can only create invoices (limited-access password)
- No credentials in code -- passwords read from `phoenix.conf` at runtime

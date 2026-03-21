# Arkade Specification and Implementation

Research notes on Ark Labs' Arkade -- the first mainnet Ark protocol implementation.

---

## 1. Arkade Public Beta (October 2025)

### 1.1 What Shipped

Arkade launched in public beta in October 2025 as the first mainnet implementation of the Ark Protocol specification originally proposed by Burak in 2023. The launch came after two years of development.

Core capabilities at launch:

- **VTXO-based off-chain transactions**: Users transact via Virtual Transaction Outputs, with periodic batch settlement on Bitcoin L1.
- **Virtual Mempool**: An off-chain environment where independent operations run as a DAG (directed acyclic graph) rather than Bitcoin's linear confirmation queue. Independent transaction branches execute in parallel without waiting for block confirmations.
- **Batch Settlement**: A single on-chain settlement transaction can finalize thousands of off-chain operations. Fees are distributed across all participants in the batch.
- **Self-Custody**: Users retain unilateral withdrawal capability at all times, even if the operator goes offline.
- **Lightning Interoperability**: Integrated with Lightning Network via Boltz, enabling liquidity to move between Lightning channels and Arkade's off-chain environment.
- **Arkade Assets**: A framework for issuing, transferring, and burning stablecoins and other digital assets natively within VTXOs.
- **Arkade Wallet**: Open-source reference wallet -- a self-custodial Progressive Web App (PWA).
- **BTCPayServer Plugin**: Merchants can accept instant Bitcoin payments through native Arkade integration.

### 1.2 What's Missing / Current Limitations

- Explicitly labeled as **beta software** -- "not ready to handle your life savings."
- Guardrails in place to maintain system integrity during the growth phase.
- No public dashboards showing network stats (user count, volume, number of active ASPs).
- The covenant-less design requires all round participants to be online during tree signing, limiting scalability.
- Features expected to "evolve significantly" -- enhanced scripting environments and additional security mechanisms are on the roadmap.
- No published information on maximum VTXO sizes, round intervals in production, or fee schedules for the mainnet ASP.

### 1.3 Server Implementation: arkd

The Arkade server is implemented in Go as `arkd` (github.com/arkade-os/arkd). Notable milestones:

- **v0.3.0** (September 2025): Introduced VTXO tree signing by round participants, new onboarding process, dynamic min-relay-fee and dust calculations, async payment signature validation, reversible VTXO support, forfeit transaction fund tracking, and adversarial scenario testing. 31 merged PRs from 5 contributors.
- Security: Alpine Docker images with Trivy scanning, CVE mitigations.
- SDK enhancements: ListVtxos export, SpentBy field on VTXOs, transaction history tracking, RoundInterval data storage.

---

## 2. SDK Surface

Arkade provides SDKs in three languages, all targeting the same core operations.

### 2.1 TypeScript SDK

Repository: github.com/arkade-os/ts-sdk (previously ArkLabsHQ/wallet-sdk)

Current version: v0.4.0-next.5 (pre-release). Designed for building browser and Node.js wallet applications. Operations exposed include wallet creation, VTXO management, OOR payments, boarding, offboarding, round participation, and Lightning integration.

### 2.2 Go SDK

Repository: github.com/arkade-os/go-sdk

Designed for backend services and server-side integrations. Supports both on-chain and off-chain transactions via the Ark protocol. The arkd server itself is written in Go, so the Go SDK has the tightest integration.

### 2.3 Rust SDK

No standalone Rust SDK repository is publicly listed under the arkade-os organization. The Rust implementation of Ark exists under Second's `bark` project (see bark-implementation.md). Ark Labs references a Rust SDK in marketing materials but it may refer to bark-wallet or a forthcoming port.

**Conflict note**: The Arkade launch blog post lists "Rust SDK" as available, but the GitHub organization (arkade-os) only shows TypeScript and Go SDKs. It is unclear whether this refers to community contributions, the bark-wallet crate, or unreleased code.

### 2.4 Common API Surface

Based on arkd's server API and the SDK documentation, the primary operations are:

| Operation | Description |
|-----------|-------------|
| Create wallet | Generate keys, connect to ASP |
| Board | Send BTC to a boarding address, receive board VTXO |
| Send (OOR) | Instant off-chain payment to another Ark address |
| Send (in-round) | Payment settled in the next round |
| Receive | Accept incoming OOR or round payments |
| Refresh | Swap expiring VTXOs for fresh ones in a round |
| Offboard | Cooperative exit to an on-chain address |
| Unilateral exit | Emergency broadcast of pre-signed tree |
| Lightning send | Pay BOLT11 invoices via ASP gateway |
| Lightning receive | Generate invoices, receive via ASP |
| List VTXOs | Query VTXO states, amounts, expiry |
| History | Transaction movement history |

---

## 3. Tether's $5.2M Investment

### 3.1 Funding Details

In March 2026, Ark Labs raised $5.2M in seed funding. Investors:

- **Tether** (lead/major backer)
- Ego Death Capital
- Epoch VC
- Lion26
- Sats Ventures
- Contribution Capital
- Anchorage Digital (participation)
- Ralph Ho (former PayPal VP of Finance)
- Tim Draper (backer)

### 3.2 Stablecoin Integration Strategy

The funding explicitly targets infrastructure for **USDT on Bitcoin**. Ark Labs is building:

- **Arkade Assets framework**: Native asset issuance within VTXOs, no external indexers required.
- USDT support as a first-class asset type within Arkade's off-chain environment.
- The ability to issue, transfer, and burn stablecoins with the same instant settlement and batch efficiency as native BTC VTXOs.

### 3.3 Arkade Assets Technical Architecture

Assets are encoded using **TLV (Type-Length-Value) format** in OP_RETURN outputs:

```
OP_RETURN <Magic_Bytes: "ARK"> <Type: 0x00> <Length> <Asset_Payload>
```

Key properties:

- Assets flow through VTXOs identically to bitcoin -- spent as inputs, created as outputs.
- Asset identity is immutable, derived from genesis point: `(genesis_txid, group_index)`.
- **Control assets** enable managed tokens: supply adjustments (stablecoins), transfer restrictions (security tokens), upgradeable parameters (governance).
- **Teleportation mechanism**: A commit-reveal system for asset continuity across batch transitions. Assets move to teleport outputs with `commitment = sha256(payment_script || nonce)`, then receiving transactions claim by revealing the preimage.
- Off-chain validation by the Arkade Signer; on-chain validation via OP_RETURN metadata and indexers.

### 3.4 Implications for a Repo Market

The Arkade Assets framework makes Ark potentially viable for denominating repo contracts in stablecoins. If USDT is a first-class VTXO asset, a repo market could denominate loan amounts, collateral values, and interest payments in USDT while using BTC VTXOs as collateral. This avoids the volatility problem of BTC-denominated lending.

---

## 4. Code Architecture

### 4.1 GitHub Organization

The Arkade codebase is hosted under `github.com/arkade-os/` (previously `github.com/ArkLabsHQ/`).

Key repositories:

| Repo | Language | Purpose |
|------|----------|---------|
| `arkd` | Go | ASP server implementation |
| `ts-sdk` | TypeScript | Browser/Node.js wallet SDK |
| `go-sdk` | Go | Backend integration SDK |
| `wallet` | TypeScript | Reference PWA wallet |

### 4.2 Server Architecture (arkd)

- Written in Go.
- Manages round coordination, VTXO tree construction, forfeit processing, connector management.
- Handles Lightning gateway functionality.
- Stores round data, VTXO states, forfeit transactions.
- Exposes gRPC and REST APIs for wallet SDKs.
- Docker deployment with security scanning.

### 4.3 Wallet Architecture

The reference wallet is a **Progressive Web App** (PWA) -- runs in the browser, no native installation required. It uses the TypeScript SDK under the hood. Self-custodial: keys are generated and stored client-side.

---

## 5. Network Stats

### 5.1 Current State (March 2026)

No public dashboards or explorers expose Arkade network statistics. The following is known:

- Arkade is live on **Bitcoin mainnet** as of the October 2025 beta launch.
- At least one ASP is operated by Ark Labs for the mainnet deployment.
- No published figures for user count, transaction volume, or total value locked.
- Signet testing environments also exist (used by both Ark Labs and Second).

### 5.2 Ecosystem Partners

Active integrations at launch: Breez, LayerZ Wallet, BTCPayServer, Boltz, BullBitcoin, and Lendasat. These suggest real transaction volume but no numbers are public.

---

## 6. Fulmine Wallet Daemon

### 6.1 Purpose

Fulmine is a Bitcoin wallet daemon designed for **swap providers and payment hubs**. It bridges Ark and Lightning, enabling operators to optimize Lightning channel liquidity while minimizing on-chain fees.

Repository: github.com/ArkLabsHQ/fulmine

### 6.2 Architecture

- Built-in ASP enables trustless swaps between Ark and Lightning balances.
- Integrates with LND (Lightning Network Daemon).
- Exposes gRPC and REST APIs for programmatic access.
- Docker deployment.

### 6.3 Use Cases

- Lightning routing nodes can use Fulmine to rebalance channels via Arkade settlement (cheaper than on-chain splicing).
- Payment hubs can accept Ark payments and forward them to Lightning, or vice versa.
- Swap providers (like Boltz) integrate Fulmine for Ark-Lightning atomic swaps.

### 6.4 Relevance to a Repo Market

Fulmine is the closest existing component to "financial infrastructure" in the Ark ecosystem. A repo market would need similar daemon-style software that:
- Manages collateral VTXOs programmatically.
- Executes swaps atomically (collateral <-> loan proceeds).
- Monitors expiry timers and triggers automatic refresh.
- Interfaces with Lightning for settlement.

Fulmine's architecture provides a template for this kind of service.

---

## Devil's Advocate: Arkade Risks

### Beta Software Risk

Arkade is explicitly beta. The guardrails, unspecified fee structures, and "evolving" features mean the platform could change materially. Building a repo market on top of infrastructure that may break or pivot is high-risk.

### Single-ASP Centralization

The mainnet deployment appears to run a single ASP operated by Ark Labs. If this ASP goes down, all users must unilaterally exit (expensive, slow). There is no public information about third-party ASP operators on mainnet.

### Tether Alignment

Tether's investment signals that Arkade's development priorities will skew toward stablecoin infrastructure. If the repo market use case diverges from Tether's interests (e.g., pure BTC lending without stablecoins), it may not get prioritized in the SDK or server features.

### SDK Maturity

The TypeScript SDK is at v0.4.0-next (pre-release). The Go SDK is available but documentation depth is unclear. Production applications are being built on pre-1.0 APIs that may break.

### Missing Rust SDK

If the repo market requires Rust (for performance, security, or compatibility with existing Bitcoin tooling), the Arkade ecosystem is lacking. The bark-wallet crate exists but is a Second project with a different protocol dialect.

---

## Sources

- [Ark Labs - Arkade Goes Live (Blog)](https://blog.arklabs.xyz/press-start-arkade-goes-live/)
- [Ark Labs - Arkade Documentation](https://docs.arkadeos.com/)
- [Ark Labs - Arkade Assets (Blog)](https://blog.arklabs.xyz/native-assets-on-bitcoin-introducing-arkade-assets/)
- [The Block - Arkade Public Beta Launch](https://www.theblock.co/post/375271/ark-labs-arkade-public-beta-layer-2-bitcoin)
- [The Block - Tether Backs Ark Labs $5.2M](https://www.theblock.co/post/393198/tether-backs-ark-labs-5-2-million-seed-raise-to-expand-stablecoin-and-programmable-finance-infrastructure-on-bitcoin)
- [PR Newswire - Ark Labs Raises $5.2M](https://www.prnewswire.com/news-releases/ark-labs-raises-5-2m-backed-by-tether-to-build-programmable-finance-on-bitcoin-302712201.html)
- [GitHub - arkade-os/arkd](https://github.com/arkade-os/arkd)
- [GitHub - arkade-os/ts-sdk](https://github.com/arkade-os/ts-sdk)
- [GitHub - arkade-os/go-sdk](https://github.com/arkade-os/go-sdk)
- [GitHub - arkade-os/wallet](https://github.com/arkade-os/wallet)
- [GitHub - ArkLabsHQ/fulmine](https://github.com/ArkLabsHQ/fulmine)
- [arkd v0.3.0 Release Notes](https://github.com/arkade-os/arkd/releases/tag/v0.3.0)
- [Arkade TypeScript SDK Documentation](https://arkade-os.github.io/ts-sdk/)

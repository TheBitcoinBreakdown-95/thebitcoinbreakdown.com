# Prior Art and Resources

Tracking existing work, discussion venues, and resources relevant to the ASP liquidity market design.

---

## Discussion Venues (where to propose/comment)

### GitHub Issues

| Issue | Repo | Author | Status | Relevance |
|-------|------|--------|--------|-----------|
| [#197: Allowing ASPs to borrow liquidity from external sources](https://github.com/arkade-os/arkd/issues/197) | arkade-os/arkd | ben2077 | Open | **Direct hit.** Per-round liquidity request from external providers. Concept sketch, no spec. Associated PR #198 closed. |

### Delving Bitcoin

| Thread | Author | Relevance |
|--------|--------|-----------|
| [Ark as a Channel Factory](https://delvingbitcoin.org/t/ark-as-a-channel-factory-compressed-liquidity-management-for-improved-payment-feasibility/2179) | Rene Pickhardt | Identifies ASP liquidity lock-up as critical challenge. No financing solution proposed. |
| [The Ark case for CTV](https://delvingbitcoin.org/t/the-ark-case-for-ctv/1528) | Steven Roose | Technical protocol discussion. Mentions liquidity fees proportional to VTXO time remaining. |

### Stacker News

| Thread | Author | Relevance |
|--------|--------|-----------|
| [Ark AMA](https://stacker.news/items/192040) | Burak | Acknowledges large BTC requirement for ASPs, suggests federations. No market solution. |

---

## Published Research (defines the problem)

### Second Liquidity Research Series

The most thorough existing analysis of ASP liquidity economics. Three parts, no Part 4.

| Part | Title | Date | Link | Key Finding |
|------|-------|------|------|-------------|
| 1 | Lightning liquidity: Ark servers and LSPs compared | 2025-07-10 | [blog.second.tech](https://blog.second.tech/ark-liquidity-research-01/) | Ark is 3.7-6.65x more capital-efficient than LSPs for quarterly top-ups and DCA |
| 2 | Bitcoin yield survey: The opportunity cost of Ark liquidity | 2025-08-11 | [blog.second.tech](https://blog.second.tech/survey-of-bitcoin-yield/) | Opportunity cost benchmarked at 1-4% APR. Acknowledges future need for external capital. |
| 3 | Diving deeper into Lightning liquidity: Amboss Magma | 2025-09-11 | [blog.second.tech](https://blog.second.tech/diving-deeper-into-lightning-liquidity-amboss-magma-2/) | Magma median ~2.6% APR for large channels. Informs Ark fee structure. |

### Ark Labs Blog

| Post | Link | Relevance |
|------|------|-----------|
| Understanding Ark Liquidity Requirements | [blog.arklabs.xyz](https://blog.arklabs.xyz/liquidity-requirements/) | Calculates ASP funding needs. Descriptive only. |
| Adios, Expiry: Rethinking Liveness and Liquidity | [blog.arklabs.xyz](https://blog.arklabs.xyz/adios-expiry-rethinking-liveness-and-liquidity-in-arkade/) | Delegation for automatic VTXO renewal. Improves capital velocity. |

### Bitcoin Optech

| Entry | Link | Relevance |
|-------|------|-----------|
| Ark topic page | [bitcoinops.org](https://bitcoinops.org/en/topics/ark/) | Technical coverage. No mentions of external financing. |
| V-PACK standard for stateless VTXO verification | [bitcoinops.org](https://bitcoinops.org/en/newsletters/2026/03/06/#a-standard-for-stateless-vtxo-verification) | Mar 2026. Stateless verification relevant to LP evaluation of ASP tree claims. |
| hArk software release (Second) | [bitcoinops.org](https://bitcoinops.org/en/newsletters/2026/02/20/#second-releases-hark-based-ark-software) | Feb 2026. Latest Second implementation milestone. |
| Ark as a channel factory | [bitcoinops.org](https://bitcoinops.org/en/newsletters/2026/01/09/#using-ark-as-a-channel-factory) | Jan 2026. Ark-Lightning composability -- relevant to settlement rail design. |
| Arkade launches | [bitcoinops.org](https://bitcoinops.org/en/newsletters/2025/11/21/#arkade-launches) | Nov 2025. Ark Labs public beta launch. |
| CTV + CSFS benefits for Ark | [bitcoinops.org](https://bitcoinops.org/en/newsletters/2025/04/04/#ark) | Apr 2025. Covenant improvements relevant to Approach B feasibility. |
| Bark launches on signet | [bitcoinops.org](https://bitcoinops.org/en/newsletters/2025/03/21/#bark-launches-on-signet) | Mar 2025. Second's signet milestone. |
| Ark Wallet SDK released | [bitcoinops.org](https://bitcoinops.org/en/newsletters/2025/02/21/#ark-wallet-sdk-released) | Feb 2025. SDK availability lowers ASP integration barrier. |
| Bark implementation announced | [bitcoinops.org](https://bitcoinops.org/en/newsletters/2024/10/18/#bark-ark-implementation-announced) | Oct 2024. Second's initial announcement. |
| LN scalability via covenants | [bitcoinops.org](https://bitcoinops.org/en/newsletters/2023/09/27/#using-covenants-to-improve-ln-scalability) | Sep 2023. Covenant-based scaling context. |
| Joinpool proposal (original Ark concept) | [bitcoinops.org](https://bitcoinops.org/en/newsletters/2023/05/31/#proposal-for-a-managed-joinpool-protocol) | May 2023. Burak's original proposal. |

#### Related Optech Topics

| Topic | Link | Relevance |
|-------|------|-----------|
| OP_CHECKTEMPLATEVERIFY | [bitcoinops.org](https://bitcoinops.org/en/topics/op_checktemplateverify/) | CTV is key to Ark efficiency and Approach B VTXO scripting. |
| Joinpools | [bitcoinops.org](https://bitcoinops.org/en/topics/joinpools/) | Ark is a form of joinpool. Background context. |
| Covenants | [bitcoinops.org](https://bitcoinops.org/en/topics/covenants/) | Foundational dependency for trustless Ark and richer VTXO scripts. |

### Ark Protocol Specification Site

| Page | Link | Relevance |
|------|------|-----------|
| Ark Protocol home | [ark-protocol.org](https://ark-protocol.org/index.html) | Canonical protocol spec site. Covers VTXO model, rounds, OOR payments. |
| Introduction to Ark | [ark-protocol.org](https://ark-protocol.org/intro/index.html) | Technical introduction. Shared UTXOs, forfeit mechanism, connector outputs. |
| Virtual Transaction Outputs (VTXOs) | [ark-protocol.org](https://ark-protocol.org/intro/vtxos/index.html) | VTXO definition, covenant trees, forfeit clause (A+S multisig or user after 24h), 14-day expiry/refresh. |
| Connectors | [ark-protocol.org](https://ark-protocol.org/intro/connectors/index.html) | Rounds, forfeit transactions, connector outputs enforcing atomicity. |
| Out-of-Round Payments (Arkoor) | [ark-protocol.org](https://ark-protocol.org/intro/oor/index.html) | OOR mechanics, mild trust assumption (server+sender non-collusion), refresh path. |
| Covenant-less Ark (clArk) | [ark-protocol.org](https://ark-protocol.org/intro/clark/index.html) | Pre-signed multisig replacing CTV/TXHASH. Ephemeral keys. Relevant to Phase 1 feasibility. |

#### Covenant Proposal References (from ark-protocol.org)

| Proposal | Link | Relevance |
|----------|------|-----------|
| OP_CHECKTEMPLATEVERIFY | [covenants.info](https://covenants.info/proposals/ctv/) | CTV proposal detail. Ark gains efficiency with CTV. |
| TXHASH | [covenants.info](https://covenants.info/proposals/txhash) | Alternative covenant proposal referenced by clArk page. |

---

## Adjacent Projects (related but not competing)

### Lendasat -- DLC VTXOs for user-facing lending

- **What:** P2P lending ON Ark using DLC VTXOs (combines DLCs with Ark's VTXO model)
- **Who:** Funded by Fulgur Ventures, Initial Capital, and Ark Labs (March 2026)
- **Links:** [stacker.news](https://stacker.news/items/602605), [lendasat.com](https://lendasat.com), [whitepaper](https://whitepaper.lendasat.com/lendasat-whitepaper.pdf)
- **Gap vs our design:** Lendasat enables lending ON Ark for end users. Does NOT provide capital TO ASPs. But the DLC VTXO primitive could be adapted for ASP-facing lending.

### Lightning Pool -- Batch auction for channel leases

- **What:** Non-custodial batched auction for Lightning channel capacity leases
- **Who:** Lightning Labs
- **Links:** [whitepaper](https://lightning.engineering/lightning-pool-whitepaper.pdf), [deep dive](https://lightning.engineering/posts/2020-11-02-pool-deep-dive/)
- **Gap vs our design:** Lightning-only, no Ark awareness. But the auction architecture (sealed-bid uniform-price) is directly relevant as a precedent for rate discovery.

### Amboss Magma -- Lightning liquidity marketplace

- **What:** P2P marketplace for Lightning channel liquidity
- **Links:** [docs](https://old-docs.amboss.tech/docs/magma/intro)
- **Gap vs our design:** Lightning-only. But Magma's pricing data (median ~2.6% APR) is the closest benchmark for what BTC liquidity costs in practice.

### Lygos Finance -- DLC-based institutional BTC lending

- **What:** Non-custodial BTC-collateralized lending using DLCs, $100K-$100M
- **Links:** [coindesk](https://www.coindesk.com/business/2025/08/27/lygos-aims-to-banish-ghosts-of-crypto-lending-collapse-with-non-custodial-bitcoin-model), [blockspace](https://blockspace.media/insight/lygos-finance-acquires-atomic-finance-to-launch-non-custodial-dlc-powered-bitcoin-loans/)
- **Gap vs our design:** User-facing institutional loans. No ASP integration.

### Lava Loans -- DLC-based BTC loans

- **What:** Bitcoin-collateralized loans via DLCs, raised $17.5M
- **Gap vs our design:** User-facing. No Ark connection.

### Ark-Sim -- Liquidity simulator

- **What:** Julia-based agent simulation of ASP liquidity dynamics
- **Links:** [github](https://github.com/aruokhai/ark-sim)
- **Gap vs our design:** Models internal flows only. No external financing simulation. Could be extended.

---

## Implementation Directory

| Implementation | Org | Code | Docs | Notes |
|----------------|-----|------|------|-------|
| Arkade (Go) | Ark Labs | [github.com/arkade-os](https://github.com/arkade-os) | [docs.arkadeos.com](https://docs.arkadeos.com) | Public beta Oct 2025. Contains issue #197. |
| Bark (Rust) | Second | [gitlab.com/ark-bitcoin](https://gitlab.com/ark-bitcoin) | [docs.second.tech](https://docs.second.tech/) | First mainnet Ark transactions. hArk release Feb 2026. |

### Community

| Channel | Link |
|---------|------|
| Telegram | [t.me/ark_bitcoin](https://t.me/ark_bitcoin) |

## Cloned Repos (local references)

| Repo | Local Path | Purpose |
|------|-----------|---------|
| ArkLabsHQ/ark | `Ark Labs/ark/` | Ark Labs main implementation and specs |
| arkade-os/arkd | `Ark Labs/arkd/` | Arkade server -- contains issue #197 |
| ark-bitcoin/bark | `Second/bark/` | Second's Bark implementation (Rust) |
| barkgui (already local) | `TBB/JC Bitcoin/barkgui/` | Bark wallet GUI showing API surface |

---

## The Gap

The problem is well-documented. The solution space is empty.

- Second's research (3 parts) quantifies the cost but proposes no financing mechanism
- Ark Labs' blog describes the liquidity requirement but offers only protocol-level improvements (delegation, revocation)
- Burak suggests federation but has not specified how it would work financially
- ben2077's issue #197 is the only direct proposal for external liquidity -- it's a concept sketch with no follow-through
- Lendasat builds lending ON Ark but not TO ASPs
- Nobody has published a protocol specification for a BTC-native liquidity market serving ASP working capital

This is the gap we're filling.

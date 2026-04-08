# ArkPool: Per-Round Liquidity for Ark Service Providers

**Version:** 0.2 (Draft)
**Date:** March 2026
**Status:** Specification for review

---

## Introduction

Ark is a Bitcoin Layer 2 protocol where a central server (the ASP) locks BTC into shared UTXO trees on behalf of users. Users hold virtual UTXOs (VTXOs) -- off-chain claims within those trees -- and transact by participating in rounds or sending out-of-round (OOR) payments. VTXOs expire after a configurable period, at which point the ASP recovers the locked BTC.

The ASP's business is simple: lock BTC, serve users, collect fees, recover BTC when trees expire. The problem is that every round requires fresh BTC while the old BTC is still locked. At scale, the ASP runs out of its own capital.

ArkPool proposes a protocol-level change: external liquidity providers (LPs) contribute BTC directly into Ark rounds. The LP's security comes from the round's own forfeit mechanism -- the same mechanism that already protects the ASP. No external escrow, no oracles, no new trust assumptions.

---

## The Problem

Every Ark round creates a new covenant tree. The ASP funds the tree with BTC from its wallet. That BTC is frozen until the tree expires.

```
Round 1: ASP locks 10 BTC into Tree A     (expires in 7-30 days)
Round 2: ASP locks 10 BTC into Tree B     (expires in 7-30 days)
Round 3: ASP locks 10 BTC into Tree C     (expires in 7-30 days)
...
Trees overlap. All are locked simultaneously.
```

The lockup multiplier equals the expiry period divided by the capital cycling time. With more trees active at once, more BTC is frozen.

**Shipping defaults (from source code, March 2026):**

| Implementation | VTXO Expiry | Lockup Multiplier | Source |
|---|---|---|---|
| Arkade (arkd) | 7 days (`ARKD_VTXO_TREE_EXPIRY = 604672` seconds) | ~1.3x weekly throughput | `internal/config/config.go:241` |
| Bark (captaind) | 30 days (`vtxo_lifetime = 4320` blocks) | ~5.6x weekly throughput | `server/captaind.default.toml:14` |

Both are operator-configurable. The choice is a tradeoff: shorter expiry is more capital-efficient but requires users to refresh more often. Longer expiry is better UX but locks more capital.

| ASP Throughput | Capital Needed (7-day) | Capital Needed (30-day) |
|---|---|---|
| 100 BTC/week | ~130 BTC | ~560 BTC |
| 500 BTC/week | ~650 BTC | ~2,800 BTC |
| 1,000 BTC/week | ~1,300 BTC | ~5,600 BTC |

At some throughput level -- sooner for longer expiry, later for shorter -- the ASP's own BTC is not enough.

---

## The Cause

The capital gap is structural, not a bug. It comes from three properties of Ark's design:

1. **Trees overlap.** New trees are created every round while old trees haven't expired yet. The ASP must fund all active trees simultaneously.

2. **Expiry is the only recovery mechanism.** Under V1 (all shipping implementations), the ASP gets its BTC back only when the tree's absolute timelock expires. V2 revocation (proposed by Burak, not implemented, requires an unspecified ZK-based VPU) could enable early recovery. Until then, capital is locked for the full expiry period.

3. **Change outputs inflate the requirement.** When a user spends part of a VTXO, the remainder becomes a change output in the new tree -- requiring additional capital from the ASP without generating additional fees.

Protocol-level improvements help but don't eliminate the gap. Shorter expiry reduces it. Delegation (Arkade) and hArk (Second) improve UX and throughput efficiency. But the multiplier is always greater than 1x. At meaningful throughput, external capital is needed.

---

## The Solution

External LPs contribute BTC directly into Ark rounds. When a round's demand exceeds the ASP's available capital, the ASP solicits LP funding. The LP's UTXO enters the round's commitment transaction. The LP's repayment comes from the round's own forfeit mechanism.

```
LP                          ASP                         Ark Users
 |                           |                            |
 |                           |<-- round batch request ----|
 |                           |   (exceeds ASP capital)    |
 |                           |                            |
 |<-- liquidity request -----|                            |
 |   "Need X BTC, Y% fee"   |                            |
 |                           |                            |
 |--- UTXO for round ------->|                            |
 |                           |--- poolTx (includes LP) -->|
 |                           |   LP's UTXO in tree        |
 |                           |                            |
 |                      [users refresh VTXOs]             |
 |                           |                            |
 |<-- forfeit proceeds ------|                            |
 |   (paid to LP, not ASP)   |                            |
```

### How It Works

1. ASP begins round construction. The batch exceeds available capital by X BTC.
2. ASP sends a `LiquidityRequest` to known LPs: amount needed, round details, proposed fee.
3. LP responds with a `LiquidityOffer`: UTXO to contribute, accepted rate, forfeit recipient address.
4. ASP includes the LP's UTXO in the round's commitment transaction (`poolTx`).
5. Forfeit transactions are constructed so that the LP-funded portion of expired VTXO proceeds pays to the LP's address, not the ASP's.
6. When users refresh into future rounds, their old VTXOs become claimable. The LP sweeps its share -- receiving principal plus fee.

### Why This Works

The LP's security is the forfeit transaction itself -- a pre-signed Bitcoin transaction created during round construction. This is the same mechanism that already secures the ASP's capital in every Ark round. The LP is not trusting the ASP to repay; the LP holds a valid Bitcoin transaction that pays it directly when VTXOs expire.

- No separate escrow transaction needed
- No oracles or external attestation
- Lending is atomic with the round
- The LP's claim does not depend on the ASP's solvency or cooperation after the round is constructed
- All terms are in BTC, all timelocks are block heights

### What the LP Needs to Understand

The LP must understand that its claim is on forfeit proceeds from specific VTXOs in a specific round. If users in that round unilaterally exit (broadcast the pre-signed exit transaction chain on-chain instead of refreshing), those users' portions are voided from the LP's claim. The LP bears actuarial risk proportional to the unilateral exit rate.

In practice, unilateral exits are rare -- they are expensive (multiple on-chain transactions) and slow (CSV delays at each tree level). A 2-5% exit rate is a reasonable stress assumption. The fee compensates for this risk.

### Required Protocol Changes

Both Arkade and Bark would need:

**New message types:**
- `LiquidityRequest`: ASP to LP network. Contains round ID, amount needed, proposed fee, round expiry block height.
- `LiquidityOffer`: LP to ASP. Contains UTXO, accepted rate, LP pubkey, forfeit recipient address.

**Modified round construction:**
- `poolTx` (commitment transaction) must accept external UTXOs from LPs alongside the ASP's own inputs.
- The covenant tree must track which portions are LP-funded.

**Modified forfeit construction:**
- Forfeit transactions must allow the recipient to be configurable per-VTXO or per-subtree.
- LP-funded portions direct their forfeit proceeds to the LP's address.

These are additive changes -- they extend the existing round and forfeit mechanisms rather than replacing them. Rounds without LP participation work exactly as they do today.

---

## Impact

### For ASPs

External capital removes the growth ceiling. An ASP with 300 BTC that would otherwise cap at 230 BTC/week (7-day expiry) or 55 BTC/week (30-day expiry) can serve whatever demand arrives, borrowing the difference from LPs. The borrowing cost (1-3% annualized on the LP-funded portion) is covered by transaction fees earned during the round.

The ASP doesn't need to choose between capital efficiency and user experience. It can run longer expiry (better UX, higher fees per refresh) and fund the larger capital requirement externally.

### For LPs

A non-custodial BTC yield product. The LP's BTC goes into an Ark round, secured by a pre-signed forfeit transaction. If the ASP vanishes, the forfeit transaction is still valid -- the LP claims when VTXOs expire. No platform custody, no counterparty credit risk beyond actuarial exit risk.

The comparison is cold storage at 0%. At 1-3% annualized for a 7-30 day term with Bitcoin-script-enforced security, the product is competitive for any BTC holder who isn't actively deploying their capital elsewhere.

### For the Ark Ecosystem

The capital constraint is the binding limit on how many ASPs can operate and at what scale. Removing it means:
- Smaller operators can compete (don't need 500+ BTC to start)
- ASPs can grow with demand instead of capping at their capital
- More ASPs means more competition, better fees for users, and geographic diversity
- The "only Tether can afford to run an ASP" scenario is avoided

---

## Viability

### Implementation Comparison

| Parameter | Arkade (arkd) | Bark (captaind) | Source |
|---|---|---|---|
| VTXO expiry default | 604,672 seconds (~7 days) | 4,320 blocks (~30 days) | config.go:241 / captaind.default.toml:14 |
| Lockup multiplier | ~1.3x | ~5.6x | Derived: expiry_weeks * ~1.3 change factor |
| Round frequency | 30s sessions, continuous | 10s round interval | config.go:228 / captaind.default.toml:68 |
| Max VTXOs per round | 128 participants | 65,536 leaf VTXOs | config / nb_round_nonces=8, radix^8 |
| Fee model | CEL expression programs (operator-set, zero default) | PPM tiers by VTXO age (0-0.8%) | arkfee/README.md / captaind.default.toml:188 |
| Refresh fee near expiry | Operator-defined | ~0% (0 ppm, 150 sat base) | fees.rs |
| Refresh fee on new VTXOs | Operator-defined | 0.8% (8000 ppm) | fees.rs |
| Delegation | Yes (BIP322, shipping) | No | Arkade "Adios Expiry" feature |
| hArk (async rounds) | No | Yes (shipping) | bark v0.1.0-beta.6 |
| V2 revocation | Not implemented | Not implemented | Blog post only (Burak, Medium) |

### When Is This Needed?

At 7-day expiry: ArkPool becomes relevant when an ASP's throughput exceeds ~75% of its BTC holdings per week. An operator with 500 BTC can self-fund ~380 BTC/week. Beyond that, borrow or stop growing.

At 30-day expiry: ArkPool becomes relevant much sooner. An operator with 500 BTC can self-fund only ~90 BTC/week.

The trigger is observable: ASPs report that capital constraints are limiting their throughput.

### The Expiry Tradeoff

Operators choosing longer expiry (for better UX) need ArkPool sooner but also earn more per unit of throughput -- Bark's lockup-weighted fee tiers (up to 0.8%) compensate for the capital cost. The higher fee revenue makes borrowing costs more affordable.

Operators choosing shorter expiry (for capital efficiency) need ArkPool later but earn less per transaction. They may never need it at moderate throughput.

Both strategies are viable. ArkPool serves long-expiry ASPs first, then short-expiry ASPs as throughput scales.

---

## Risks and Failure Modes

### Unilateral Exit Risk (LP-specific)

If users in an LP-funded round unilaterally exit instead of refreshing, the LP's forfeit proceeds are reduced. At a 5% exit rate on a 100 BTC round where the LP funded 30 BTC, the LP receives ~28.5 BTC instead of 30 + fee. The fee is priced to cover expected exit rates.

**Stress case:** A mass unilateral exit event (ASP misbehavior, competing ASP offering better terms) could void 20%+ of the LP's claim. This is the primary risk. Mitigation: the LP can diversify across multiple rounds and multiple ASPs.

### ASP Goes Offline After Round Construction

The LP's forfeit transactions were pre-signed during round construction. They are valid Bitcoin transactions regardless of whether the ASP is operational. The LP can broadcast them when VTXOs expire. ASP cooperation is not needed after the round is built.

### On-Chain Fee Spikes

High fees affect Ark rounds (the ASP may reduce round frequency) but do not affect LP recovery. Forfeit transactions are pre-signed -- the LP broadcasts them whenever fees are acceptable. At 500 sat/vB, a forfeit sweep costs a fraction of a percent of the LP's claim.

### Cold Start

With 2 ASP implementations on mainnet and no established LP base, the market doesn't exist yet. The protocol changes need to be proposed, accepted by Ark Labs and/or Second, and implemented. This is a social and coordination challenge, not a technical one.

### Over-Leverage

An ASP that borrows too much relative to its own capital and operational capacity could fail to maintain operations, triggering mass unilateral exits that harm LPs. Mitigation: LPs evaluate the ASP's balance sheet before lending. Proof of reserves (UTXO ownership attestation + tree expiry schedule) gives LPs visibility into the ASP's position.

---

## Open Questions

1. **Forfeit recipient configurability.** Can the existing forfeit transaction structure support per-VTXO or per-subtree recipient addresses without breaking atomicity guarantees?

2. **LP discovery.** How do ASPs find LPs? Initially bilateral (direct relationships). At scale, a bulletin board or batch auction (modeled on [Lightning Pool](https://lightning.engineering/lightning-pool-whitepaper.pdf)).

3. **Rate discovery.** What sets the lending rate? Initially bilateral negotiation. The natural band is 1-3% annualized -- above 0% (cold storage alternative) and below the ASP's fee revenue per unit of capital.

4. **Proof of reserves format.** What attestation of tree expiry schedules is sufficient for LPs to evaluate an ASP?

5. **Covenant interaction.** If Bitcoin adopts [CTV](https://bitcoinops.org/en/topics/op_checktemplateverify/) or [OP_CAT](https://bitcoinops.org/en/topics/covenants/), richer VTXO scripts could encode LP claims directly as a spending condition -- eliminating the need for modified forfeit construction.

6. **Legal classification.** Is a BTC-for-BTC fixed-term loan structured as round participation a security, a swap, or something else?

---

## References

### Ark Protocol

- [Ark Protocol specification](https://ark-protocol.org/index.html) -- VTXO mechanics, round structure, OOR payments
- [Introduction to Ark](https://ark-protocol.org/intro/index.html) -- Shared UTXOs, forfeit mechanism, connectors
- [VTXOs](https://ark-protocol.org/intro/vtxos/index.html) -- Covenant trees, forfeit clause, expiry/refresh
- [Connectors](https://ark-protocol.org/intro/connectors/index.html) -- Round atomicity, connector outputs
- [OOR Payments](https://ark-protocol.org/intro/oor/index.html) -- Arkoor mechanics, trust model
- [Bitcoin Optech: Ark](https://bitcoinops.org/en/topics/ark/) -- Technical summary, newsletter coverage
- [Ark Labs blog](https://blog.arklabs.xyz/) -- Liquidity requirements, delegation ("Adios Expiry")
- [Second blog](https://blog.second.tech/) -- Liquidity research series (3 parts), yield survey, hArk
- [Burak: Introducing Ark V2](https://brqgoo.medium.com/introducing-ark-v2-2e7ab378e87b) -- Revocation mechanism (not implemented)
- [ben2077, issue #197](https://github.com/arkade-os/arkd/issues/197) -- Per-round external liquidity concept (this spec builds on it)

### Implementations (source code)

- [Arkade (arkd)](https://github.com/arkade-os) ([docs](https://docs.arkadeos.com)) -- Go, 7-day default expiry, CEL fee programs, delegation
- [Bark (captaind)](https://gitlab.com/ark-bitcoin) ([docs](https://docs.second.tech/)) -- Rust, 30-day default expiry, PPM fee tiers, hArk async rounds

### Lightning Liquidity Markets (precedent)

- [Lightning Pool whitepaper](https://lightning.engineering/lightning-pool-whitepaper.pdf) -- Batch auction architecture for channel leases
- [Amboss Magma](https://old-docs.amboss.tech/docs/magma/intro) -- P2P Lightning liquidity marketplace, ~2.6% APR median
- [Voltage LINER data](https://voltage.cloud/blog/where-does-lightning-network-yield-come-from) -- 1.2-1.7% network yield benchmark

### Adjacent Projects

- [Lendasat](https://whitepaper.lendasat.com/lendasat-whitepaper.pdf) -- DLC VTXOs for user-facing lending on Ark
- [Lygos Finance](https://www.coindesk.com/business/2025/08/27/lygos-aims-to-banish-ghosts-of-crypto-lending-collapse-with-non-custodial-bitcoin-model) -- Non-custodial DLC-based BTC lending

### Bitcoin Optech Coverage

- [V-PACK standard](https://bitcoinops.org/en/newsletters/2026/03/06/#a-standard-for-stateless-vtxo-verification) -- Stateless VTXO verification (Mar 2026)
- [hArk release](https://bitcoinops.org/en/newsletters/2026/02/20/#second-releases-hark-based-ark-software) -- Second's async round implementation (Feb 2026)
- [Arkade launches](https://bitcoinops.org/en/newsletters/2025/11/21/#arkade-launches) -- Public beta (Nov 2025)
- [OP_CHECKTEMPLATEVERIFY](https://bitcoinops.org/en/topics/op_checktemplateverify/) -- Covenant proposal relevant to future LP claim scripting
- [Covenants](https://bitcoinops.org/en/topics/covenants/) -- Foundational dependency for richer VTXO scripts

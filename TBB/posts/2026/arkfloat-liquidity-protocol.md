---
title: "ArkFloat: Liquidity Protocol for Ark Service Providers"
description: "A protocol proposal for BTC-native lending on Ark. External LPs fund rounds directly; repayment is secured by the round's own forfeit mechanism, routed to the LP's address."
pubDate: 2026-03-28
author: "The Bitcoin Breakdown"
tags: ["bitcoin", "ark", "lightning", "protocol", "layer2"]
category: "blog"
draft: false
---

Float capital. Float the Ark.

**Version:** 0.3 (Draft)
**Date:** March 2026
**Status:** Specification for review
**Changelog:** v0.3 -- revised LP security framing, corrected protocol change scope, expanded exit risk section, removed unverified design directions, updated open questions based on source code review.

---

## Introduction

Ark is a Bitcoin Layer 2 protocol where a central server (the ASP) locks BTC into shared UTXO trees on behalf of users. Users hold virtual UTXOs (VTXOs) -- off-chain claims within those trees -- and transact by participating in rounds or sending out-of-round (OOR) payments. VTXOs expire after a configurable period, at which point the ASP recovers the locked BTC.

Ark needs capital to grow. Every round an ASP runs locks BTC into a covenant tree for 7-30 days. The next round needs fresh BTC while the last round's capital is still frozen. Run enough rounds and you outgrow your own balance sheet.

Today, that ceiling is the binding constraint on how many ASPs can operate and at what scale. A well-run ASP with 300 BTC hits the wall at 230 BTC/week throughput (7-day expiry) or 55 BTC/week (30-day expiry). To go further, they either shorten expiry (worse user experience), stop growing, or find outside capital.

ArkFloat is a proposal for an Ark-native lending system that funds rounds with external capital. External liquidity providers contribute BTC directly into Ark rounds. Their repayment is secured by the round's own forfeit mechanism, the same pre-signed Bitcoin transactions that already protect the ASP's capital, routed to the LP's address instead. No custodian. No oracle. No added counterparty risk. ArkFloat is a lending protocol between Ark operators and external capital providers, built directly into Ark's round construction.

For LPs, this creates something that barely exists in Bitcoin: a non-custodial, fixed-term yield product. The LP's BTC goes into an Ark round, earns 1-3% annualized, and is returned at expiry whether the ASP is operational or not. The security comes from Bitcoin script, not from trusting the ASP to pay up.

For the Ark ecosystem, it removes the "only Tether can afford to run an ASP" problem. Smaller operators can borrow the capital gap, grow with demand, and compete on service quality rather than balance sheet size.

Ark exists to bring Bitcoin to people who don't have a UTXO -- the unbanked, the underserved, anyone priced out of on-chain fees. But the Ark is fully reserved by design: every satoshi an ASP serves must be locked on-chain first. That's what makes it trustless. It's also what limits how many people can board. People who already hold UTXOs can change that. By lending idle capital to ASPs, they float the operators who serve the people who have nothing yet. The capital circulates. The Ark grows. More people board before the tide rises.

The mechanism works by extending what Ark already does. It does not add a new trust layer -- it redirects an existing one. The open design problem is LP exposure to unilateral exit risk: if users in a funded round exit on-chain rather than refreshing, those forfeit proceeds are voided. This risk is priced into the fee and bounded by diversification, but it is real and is addressed in detail in the Risks section.

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

External LPs contribute BTC directly into Ark rounds. When a round's demand exceeds the ASP's available capital, the ASP solicits LP funding. The LP's UTXO enters the round's commitment transaction. The LP's repayment comes from forfeit proceeds on LP-funded VTXOs.

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
3. LP responds with a `LiquidityOffer`: UTXO to contribute, accepted rate, LP pubkey, forfeit recipient address.
4. ASP includes the LP's UTXO in the round's commitment transaction (`poolTx`).
5. Forfeit transactions for LP-funded VTXOs are constructed with the LP's address as recipient rather than the ASP's.
6. When users refresh into future rounds, their old VTXOs become claimable. The LP sweeps its share -- receiving principal plus fee.

### What the LP's Security Actually Is

The LP holds pre-signed Bitcoin transactions. These are valid on-chain regardless of ASP cooperation after the round is constructed. The LP can broadcast them at expiry without asking anyone's permission.

However, each forfeit transaction spends a specific VTXO output. That output only becomes a real UTXO when the user's leaf transaction is confirmed on-chain -- either because the user exited unilaterally (broadcasting their path through the tree) or because the ASP sweeps at expiry. The LP's claim is therefore on forfeit proceeds from specific VTXOs in a specific round. It is not a general claim on the round's capital.

This distinction matters: the LP's recovery depends on how users in that round behave. Users who refresh into a new round make their old VTXOs available for the LP to claim via forfeit. Users who exit unilaterally spend their VTXO through the exit path, which voids the forfeit. The LP gets nothing on VTXOs that exit.

- No external escrow
- No oracle
- No ASP cooperation required after round construction
- Recovery does depend on user behavior (refresh vs. unilateral exit)
- All terms in BTC, all timelocks in block heights

### What the LP Needs to Understand

The LP's claim is proportional to the refresh rate in the funded round, not to the round's total capital. At a 5% unilateral exit rate on a 30 BTC LP position, the LP recovers ~28.5 BTC before fee. The fee is priced to cover expected exit rates.

The 2-5% figure is the base case. Exit rates are not random -- they cluster around specific triggers. When an ASP misbehaves, raises fees sharply, or a competing ASP launches with better terms, exit rates can reach 30-60% within a single expiry period. The LP faces correlated tail risk: the same event that causes exits in one round typically affects all active rounds with that ASP simultaneously. Diversification across rounds with the same ASP does not reduce this tail risk.

The fee compensates for expected-case exits. The tail risk is managed by LP position sizing and multi-ASP diversification, not by the protocol.

### Required Protocol Changes

Both Arkade and Bark would need the following changes. These are not minor additions -- they touch the core round construction, forfeit construction, and verification paths in both implementations.

**New message types:**
- `LiquidityRequest`: ASP to LP network. Contains round ID, amount needed, proposed fee, round expiry block height.
- `LiquidityOffer`: LP to ASP. Contains UTXO, accepted rate, LP pubkey, forfeit recipient address.

**Modified round construction:**
- `poolTx` must accept external UTXOs from LPs alongside the ASP's own inputs. Currently both implementations fund the poolTx exclusively from the ASP wallet (Arkade: `builder.go:776-847`; Bark: `round/mod.rs:766-784`). Arkade has an existing boarding input path that may be repurposable; Bark does not.
- The tree's leaf structures must carry LP-funding metadata. Neither implementation currently supports per-leaf funding provenance (Arkade: flat leaf list at `builder.go:508`; Bark: `VtxoLeafSpec` at `tree/signed.rs:78-93`).

**Modified forfeit construction:**
- Forfeit transactions must support per-VTXO recipient addresses.
- In Arkade: the low-level `BuildForfeitTx` primitive (`pkg/ark-lib/tree/forfeit_tx.go:9-22`) already accepts any script as a parameter. The calling layer (`VerifyForfeitTxs`, `getForfeitScript` at `builder.go:272-1186`) is hardcoded to the ASP's address and must be refactored to accept per-VTXO scripts.
- In Bark: the connector forfeit path (`lib/src/forfeit.rs:288-321`) hardcodes the server pubkey as output recipient and requires a function signature change. The hArk forfeit path (`lib/src/forfeit.rs:38-64`) uses a protocol-defined taproot encoding a musig sighash -- changing the recipient changes the sighash, which requires users to co-sign a different transaction. The interaction between the hArk unlock preimage mechanism and a modified forfeit output is an open question (see Open Questions).

Rounds without LP participation continue to work exactly as they do today. The changes are additive at the protocol level but require meaningful implementation work.

---

## Impact

### For ASPs

External capital removes the growth ceiling. An ASP with 300 BTC that would otherwise cap at 230 BTC/week (7-day expiry) or 55 BTC/week (30-day expiry) can serve whatever demand arrives, borrowing the difference from LPs. The borrowing cost (1-3% annualized on the LP-funded portion) is covered by transaction fees earned during the round.

The ASP doesn't need to choose between capital efficiency and user experience. It can run longer expiry (better UX, higher fees per refresh) and fund the larger capital requirement externally.

### For LPs

A non-custodial BTC yield product. The LP's BTC goes into an Ark round, secured by pre-signed forfeit transactions. If the ASP vanishes, the forfeit transactions are still valid -- the LP claims when VTXOs expire. No platform custody. Counterparty risk is limited to actuarial exit risk.

The comparison is cold storage at 0%. At 1-3% annualized for a 7-30 day term with Bitcoin-script-enforced security, the product is competitive for any BTC holder who isn't actively deploying capital elsewhere -- provided they understand that recovery is not guaranteed and scales with the refresh rate of the funded round.

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
| Forfeit recipient parameterized | Low-level yes, calling layer no | No (hardcoded) | forfeit_tx.go:9-22 / forfeit.rs:314 |

### When Is This Needed?

At 7-day expiry: ArkFloat becomes relevant when an ASP's throughput exceeds ~75% of its BTC holdings per week. An operator with 500 BTC can self-fund ~380 BTC/week. Beyond that, borrow or stop growing.

At 30-day expiry: ArkFloat becomes relevant much sooner. An operator with 500 BTC can self-fund only ~90 BTC/week.

The trigger is observable: ASPs report that capital constraints are limiting their throughput.

### The Expiry Tradeoff

Operators choosing longer expiry (for better UX) need ArkFloat sooner but also earn more per unit of throughput -- Bark's lockup-weighted fee tiers (up to 0.8%) compensate for the capital cost. The higher fee revenue makes borrowing costs more affordable.

Operators choosing shorter expiry (for capital efficiency) need ArkFloat later but earn less per transaction. They may never need it at moderate throughput.

Both strategies are viable. ArkFloat serves long-expiry ASPs first, then short-expiry ASPs as throughput scales.

---

## Risks and Failure Modes

### Unilateral Exit Risk (LP-specific)

This is the primary risk. If users in an LP-funded round exit unilaterally instead of refreshing, the LP's forfeit proceeds on those VTXOs are voided.

**How unilateral exit works (verified in Bark source, `bark/src/exit/`):** The exiting user broadcasts the transaction chain from the round TX root down to their own leaf. This confirms every intermediate node on their path on-chain. Other users in sibling subtrees are not affected -- their branches remain off-chain and can still be swept by the ASP at expiry. The exiting user's VTXO is spent through the exit path, making the forfeit transaction for that VTXO unspendable.

**Base case:** Exits are expensive for users -- multiple on-chain transactions with CSV delays at each tree level. Day-to-day exit rates of 1-3% are realistic.

**Stress case:** Exits cluster. The scenarios that drive exits above 5% are correlated with ASP distress:

| Scenario | Likely Exit Rate |
|----------|-----------------|
| Normal operation | 1-3% |
| ASP raises fees significantly | 10-20% |
| Competing ASP launches with better terms | 20-40% |
| ASP misbehavior (attempted theft) | 50-80% |
| ASP goes offline permanently | 80-100% |

When a stress event occurs, it typically affects all of the ASP's active rounds simultaneously. Diversifying across rounds with the same ASP does not protect against this tail risk -- all positions are affected in the same event.

**Fee pricing and the break-even problem:** At a 5% expected exit rate, an LP lending 30 BTC needs ~1.5 BTC in fee just to break even on expected value. That is 5% of principal for a 14-30 day term. Annualized, this exceeds any realistic ASP fee revenue. The fee structure only works actuarially at scale -- an LP running many rounds across multiple ASPs, where base-case exits average out and no single stress event dominates the portfolio.

**Single-round LP positions are speculative, not actuarial.** The product requires LP scale and diversification to function as designed.

**Mitigation options:**
- LP diversifies across multiple ASPs (reduces correlation)
- LP caps position size per round (bounds single-event loss)
- ASP provides proof of reserves (UTXO ownership + tree expiry schedule) so LP can evaluate ASP health before lending
- Partial collateral posted by ASP to cover stress scenarios (a hybrid approach, not currently in this spec)

### ASP Goes Offline After Round Construction

The LP's forfeit transactions are pre-signed and valid on-chain regardless of ASP operational status. The LP can broadcast them at expiry without the ASP. ASP cooperation is not required after the round is built.

### On-Chain Fee Spikes

High fees affect Ark rounds (the ASP may reduce round frequency) but do not affect LP recovery. Forfeit transactions are pre-signed -- the LP broadcasts them when fees are acceptable. At 500 sat/vB, a forfeit sweep costs a fraction of a percent of the LP's claim.

### Cold Start

With 2 ASP implementations on mainnet and no established LP base, the market doesn't exist yet. The protocol changes need to be proposed, accepted by Ark Labs and/or Second, and implemented. This is a social and coordination challenge, not a technical one.

### Over-Leverage

An ASP that borrows too much relative to its own capital and operational capacity could fail to maintain operations, triggering mass unilateral exits that harm LPs. Mitigation: LPs evaluate the ASP's balance sheet before lending. Proof of reserves (UTXO ownership attestation + tree expiry schedule) gives LPs visibility into the ASP's position.

---

## Open Questions

1. **Bark hArk forfeit compatibility.** The hArk forfeit path in Bark uses a musig sighash computed over a protocol-defined output taproot. Changing the forfeit recipient changes the sighash, requiring users to co-sign a modified transaction. How does this interact with the hArk unlock preimage mechanism? Can an LP-addressed forfeit be constructed without breaking the hArk protocol guarantees?

2. **Arkade forfeit verification refactor scope.** `VerifyForfeitTxs` currently rebuilds every forfeit with the ASP's own script and rejects any that don't match. Supporting per-VTXO LP recipients requires per-VTXO script threading through round construction. What is the minimal change to the verification path?

3. **LP discovery.** How do ASPs find LPs? Initially bilateral (direct relationships). At scale, a bulletin board or batch auction (modeled on [Lightning Pool](https://lightning.engineering/lightning-pool-whitepaper.pdf)).

4. **Rate discovery.** What sets the lending rate? Initially bilateral negotiation. The natural band is above 0% (cold storage alternative) and below the ASP's fee revenue per unit of capital. In practice, 1-3% annualized is the likely range given Lightning liquidity market benchmarks (~2.6% on Amboss Magma, 1.2-1.7% on Voltage).

5. **Proof of reserves format.** What attestation of tree expiry schedules is sufficient for LPs to evaluate an ASP's capital position and leverage?

6. **Covenant interaction.** If Bitcoin adopts [CTV](https://bitcoinops.org/en/topics/op_checktemplateverify/) or [OP_CAT](https://bitcoinops.org/en/topics/covenants/), richer VTXO scripts could encode LP claims directly as a spending condition -- eliminating the need for modified forfeit construction entirely.

7. **Legal classification.** Is a BTC-for-BTC fixed-term loan structured as round participation a security, a swap, or something else?

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

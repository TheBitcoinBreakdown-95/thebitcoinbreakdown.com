# LP Unilateral Exit Risk: Detailed Analysis

**Date:** March 2026
**Status:** Working document. Directions 1 and 2 rejected. Directions 3 and 4 under investigation.
**Depends on:** protocol-spec.md, viability-assessment.md (section 5.3)

---

## The Problem

When an LP contributes BTC to an Ark round, the LP's repayment depends on forfeit transactions -- pre-signed transactions that pay the LP when users refresh their VTXOs into new rounds. If users instead unilaterally exit (broadcast the pre-signed exit transaction chain on-chain), the forfeit claim on those VTXOs is voided. The LP loses the principal allocated to exited VTXOs.

Normal exit rates (2-5%) are manageable. The problem is correlated exits: ASP misbehavior, competing ASP launching, fee spikes making refreshing uneconomical. In those scenarios, exit rates of 30-80% are plausible.

---

## Verified Mechanics (from source code)

All claims below verified against Arkade (arkd) and Bark (captaind) source repos, March 2026.

### Pool transaction structure

[VERIFIED] The poolTx (commitment transaction) has these outputs:
- Index 0: Batch output -- P2TR taproot encoding the VTXO tree root. Contains the total value of all VTXOs. (Arkade `builder.go:722-729`)
- Index 1: Connector output -- dust-value P2TR for forfeit chain. Only present if there are spent VTXOs being refreshed. (Arkade `builder.go:758-767`)
- Index 2+: On-chain outputs for cooperative exits. (Arkade `builder.go:769`)
- Final: Change output from ASP wallet.

[VERIFIED] The poolTx is funded by `SelectUtxos()` from the ASP's wallet + boarding inputs from users. (Arkade `builder.go:776`)

### Forfeit transactions

[VERIFIED] Forfeits are per-VTXO, not per-subtree. Each forfeit TX has exactly 2 inputs: one VTXO + one connector. (Arkade `forfeit_tx.go:9-22`, Bark `forfeit.rs:288-321`)

[VERIFIED] In Arkade, the forfeit output recipient is parameterized (`signerScript`). In Bark connector forfeits, it's hardcoded to `server_pubkey`. Changing the recipient to an LP address is a one-parameter change in Arkade and a one-line change in Bark.

[VERIFIED] Bark also has hArk forfeits (hash-locked) where the output goes to a taproot combining server unlock clause + user exit clause. More complex to modify for LP recipients. (Bark `forfeit.rs:24-64`)

### Unilateral exit

[VERIFIED] A user exiting unilaterally broadcasts the entire transaction path from tree root to their leaf VTXO. Each intermediate transaction creates outputs for both child branches. (Bark `exit/vtxo.rs:45-60`)

[VERIFIED] Sibling branches are NOT invalidated by a single user's exit. Other users can still exit independently via their own paths. (Same source.)

[VERIFIED] The batch output (index 0) is spent when the root transaction is broadcast. Once any user exits, the batch output is on-chain and the tree is partially unwound.

### Capital recycling

[VERIFIED] When VTXOs expire, the ASP sweeps via `BuildSweepTx()`. The swept BTC goes to the ASP's wallet. (Arkade `sweeper.go:64-119, 614-653`)

[INFERRED] Capital recycling is implicit -- swept BTC enters the wallet pool, and `SelectUtxos()` picks from it for future rounds. There is no explicit marking or earmarking of recycled capital.

---

## Directions Explored

### Direction 1: Tree-Structural Seniority -- REJECTED

**Idea:** Place LP claims at higher tree levels (root or intermediate nodes) so leaf-level exits don't affect them.

**Why it fails:** The covenant tree concentrates risk UPWARD. When a user exits, they broadcast transactions from root down to their leaf. Every intermediate node on that path is spent on-chain. A claim at a higher level is voided by ANY exit in the subtree below it. The LP at an intermediate node is affected by more users, not fewer.

This is the opposite of traditional structured finance where senior tranches are insulated by subordination. In a covenant tree, "senior" (higher) means more children can void your claim. The tree's branching structure works against seniority.

**Code reference:** Tree construction at Arkade `builder.go:256-318`. Each intermediate transaction spends its parent output and creates child outputs. Broadcasting any path from root to leaf spends all intermediate outputs along that path.

### Direction 2: LP-Payback Output in PoolTx -- REJECTED

**Idea:** Add a time-locked output in the poolTx that pays the LP X+fee after the tree's expiry block height, independent of user behavior.

**Why it fails:** The BTC for this output must come from somewhere.

- If the LP contributes X BTC and we create an X+fee payback output, the poolTx needs X (for the tree) + X+fee (for the payback) = ~2X+fee total input.
- The LP provided X. The ASP must provide X+fee. The LP's contribution doesn't reduce the ASP's capital requirement -- it doubles it.
- The payback output must be funded from a different source than the LP's contribution. But if the ASP has capital to fund the payback output, the ASP didn't need the LP's capital in the first place.

This direction could only work if the payback output is funded from expiring trees (see Direction 3 below). But then the payback depends on those other trees expiring successfully, reintroducing risk.

**Code reference:** PoolTx construction at Arkade `builder.go:708-769`. Adding outputs is structurally trivial (just another TxOut in the PSBT). The funding problem is economic, not technical.

### Direction 3: Fee-Funded Insurance Pool -- UNDER INVESTIGATION

**Idea:** The ASP maintains an insurance pool -- a multisig UTXO -- that backstops LP losses from unilateral exits. The insurance pool is funded by the ASP's operating fee revenue.

**How it would work:**

1. Before the LP commits capital, the ASP creates an insurance UTXO:
   - 2-of-2 multisig (LP + ASP) with a CLTV timelock
   - Sized to cover tail exit risk (e.g., 15-20% of LP contribution)
   - Funded from ASP's accumulated fee revenue

2. LP contributes X BTC to the round. Forfeit transactions on LP-funded VTXOs pay to the LP's address.

3. At tree expiry:
   - **Normal case (exit rate < 5%):** LP's forfeit proceeds >= X + fee. LP is whole. Insurance pool returns to ASP.
   - **Moderate stress (exit rate 10-20%):** LP's forfeit proceeds fall short. LP claims the deficit from the insurance pool. Remaining insurance returns to ASP.
   - **Severe stress (exit rate 30%+):** LP claims the full insurance pool. LP may still take a loss, but it's bounded by the insurance size.

**Why this is promising:**

- The ASP's cost is 15-20% of LP contribution locked as insurance, not 110%.
- An ASP doing 100 BTC/week in throughput at 0.3% average fee earns ~0.3 BTC/week. Over 30 days (one LP term), that's ~1.3 BTC in fee revenue. If the LP contributed 10 BTC, the insurance pool (1.5-2 BTC) is roughly one month's fee revenue.
- The insurance pool is a standard Bitcoin script (multisig + CLTV). No new trust assumptions.

**Open questions:**

1. **Circular dependency.** If the ASP's fee revenue drops (because users are exiting, which IS the scenario that triggers LP losses), the insurance pool may not be adequately funded for the next LP. The same stress event that hurts the LP also depletes the insurance funding source.

2. **Timing of insurance funding.** The insurance must exist BEFORE the LP commits. If the ASP hasn't earned enough fees yet (cold start), it can't insure the first LP.

3. **Insurance pool script design.** The LP must be able to claim unilaterally if the ASP vanishes. A time-locked 2-of-2 with LP fallback after expiry + grace period works, but the claim condition needs to be objective. How does the LP prove that forfeit proceeds fell short? On-chain, the LP can demonstrate which VTXOs were exited (those tree paths are on-chain) vs. which were forfeited.

4. **Multiple LPs per round.** If multiple LPs fund the same round, the insurance pool must cover all of them. Per-LP insurance pools multiply the ASP's capital lockup.

### Direction 4: Actuarial Pricing with Structural Caps -- UNDER INVESTIGATION

**Idea:** Accept exit risk as inherent to the product. Price it into the fee. Bound exposure with structural limits.

**How it would work:**

- LP funds at most 30% of any single round (no round is fully LP-dependent)
- LP diversifies across 10+ rounds per term (single-round exit spikes are absorbed)
- Fee pricing assumes 10-15% baseline exit rate, not the optimistic 2-5%
- LP's expected return: 3-5% annualized (higher than Direction 3 to compensate for uninsured risk)

**The LP's risk profile:**

| Scenario | Exit Rate | LP Return (on 10 BTC, 30-day term) |
|----------|-----------|--------------------------------------|
| Normal operations | 3% | +0.025-0.04 BTC (~3-5% ann.) |
| Moderate stress | 15% | +0.005-0.015 BTC (~0.5-2% ann.) |
| Severe stress | 30% | -0.05 to -0.1 BTC (-6% to -12% ann.) |
| Catastrophic (ASP collapse) | 70%+ | -0.15 to -0.2 BTC (-18% to -24% ann.) |

**Why this might work:**

- Simple. No insurance pool, no multisig, no additional lockup.
- Transparent. The LP knows exactly what they're accepting.
- The catastrophic scenario requires an ASP collapse, which is observable. LPs can withdraw from future rounds when they see warning signs.

**Why this might not work:**

- "BTC yield product where you can lose 20% of principal in a stress event" is a hard sell.
- The comparison isn't cold storage at 0% -- it's "cold storage at 0% with zero risk." The yield has to be compelling enough to justify the tail risk.
- If fees must be 3-5% to attract LPs at this risk level, and ASPs earn 0.3-0.8% per refresh cycle, the math may not work. The ASP can't pay LPs more than it earns.

**Open question:** Is there a fee level that's attractive to LPs AND affordable for ASPs? This is a spreadsheet question. Unit economics analysis needed comparing: LP required return at various exit rate assumptions vs. ASP fee revenue per unit of borrowed capital.

---

## The Core Tension (Restated After Code Review)

The LP's BTC enters the covenant tree. The tree is a pre-signed transaction chain. Users hold pre-signed exit transactions that can spend their VTXOs on-chain at any time. This is a foundational Ark guarantee (P1: unilateral exit is sacrosanct). It cannot be restricted without fundamentally changing Ark.

Therefore: **any capital in the tree is exposed to unilateral exit by design.** The LP's principal is at risk the moment it enters the tree. The only question is how to manage that risk:

1. **Don't put LP capital in the tree at all.** This is the standalone escrow model (Phase 1 / old Approach A). The LP lends to the ASP via a separate escrow. The ASP uses the borrowed BTC to fund its own trees. The LP's claim is on the escrow, not the tree. The LP's exposure is to the ASP's solvency, secured by collateral in the escrow. But this requires the ASP to post collateral, which defeats the capital efficiency goal.

2. **Put LP capital in the tree and insure it.** The insurance pool model (Direction 3). The LP's capital is at risk in the tree, but a separate insurance mechanism limits the downside. The insurance costs less than full collateral but introduces complexity and depends on the ASP's fee revenue stream.

3. **Put LP capital in the tree and price the risk.** The actuarial model (Direction 4). No insurance, no escrow. Pure risk pricing. Simple but requires an LP appetite for BTC-denominated principal risk.

4. **Hybrid.** Combine 2 and 3 -- partial insurance + partial actuarial pricing. The insurance covers the first 10% of losses; beyond that, the LP bears the risk. This is probably the realistic landing zone.

---

## Next Steps

- [ ] Run unit economics: at what fee level does Direction 4 break even for LPs across a range of exit rate assumptions?
- [ ] Design the insurance pool script for Direction 3 -- what are the exact spending conditions?
- [ ] Model the circular dependency risk: how correlated are "fee revenue drops" and "exit rate spikes"?
- [ ] Use `/ark-expert` to verify any new mechanical claims before writing them into specs
- [ ] Determine if Direction 3 + 4 hybrid is a coherent design or collapses into one direction

---

## Methodology Note

This document was produced under a "verify before claiming" protocol. All statements about Ark mechanics are tagged [VERIFIED], [INFERRED], or [UNVERIFIED] in the "Verified Mechanics" section. Directions 1 and 2 were initially proposed speculatively and later rejected after code review confirmed they don't work. This document records both the rejection and the code evidence, to prevent re-exploring dead ends.

Future design work should use the `/ark-expert` command to verify claims against source code before including them in specs or assessments. See `.claude/commands/ark-expert.md` for the agent's rules and source material index.

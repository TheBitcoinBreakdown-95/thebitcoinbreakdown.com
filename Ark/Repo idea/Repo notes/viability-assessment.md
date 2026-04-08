# ArkPool Viability Assessment

*Does the mechanism work? When does the Ark ecosystem need it? What breaks it?*

---

## Executive Summary

ArkPool's core mechanism -- timelocked 2-of-2 multisig escrow, Lightning settlement, block-height-denominated terms -- is sound. It uses Bitcoin primitives in production since 2015. No oracles, no novel cryptography, no protocol changes required for Phase 1.

The mechanism becomes necessary when an ASP's throughput exceeds its self-funding capacity. That threshold varies dramatically by implementation: Arkade's 7-day VTXO expiry gives a ~1.3x lockup multiplier (an ASP with 200 BTC can process ~150 BTC/week). Bark's 30-day expiry gives ~5.6x (the same ASP can only process ~35 BTC/week). The operator's choice of expiry period -- a tradeoff between capital efficiency and user convenience -- determines when external capital becomes necessary.

High sustained on-chain fees (200-500 sat/vB) do not break ArkPool -- its on-chain footprint is 2 transactions per loan cycle (~0.003 BTC at 500 sat/vB). High fees threaten Ark itself by making rounds expensive, which is an upstream problem. ArkPool's contingency is that it simply has less demand when Ark throughput contracts during fee spikes.

---

## 1. Does the Mechanism Work?

### 1.1 The Core Flow

An ASP needs BTC to fund rounds. An LP has idle BTC. The LP lends BTC to the ASP for a fixed term denominated in block heights, secured by an on-chain escrow that the LP can claim unilaterally after timeout.

Every component is a known Bitcoin primitive:

| Component | Primitive | In Production Since |
|-----------|----------|-------------------|
| Escrow | Timelocked 2-of-2 multisig (OP_IF, OP_CHECKSIG, OP_CLTV) | 2015 (BIP 65) |
| Principal transfer | Lightning payment or on-chain tx | 2018 / always |
| Repayment | Lightning invoice or on-chain tx | 2018 / always |
| Default claim | Timeout-path broadcast (LP signs alone after block height) | 2015 |
| Proof of reserves | UTXO ownership via signed message | Standard practice |
| Term enforcement | Block heights (CLTV absolute timelocks) | 2015 |

No oracles. No DLCs. No trusted third parties. No clock time -- everything is block heights, same coordinate system Ark uses for VTXO expiry.

### 1.2 The Escrow Script

```
OP_IF
  <ASP_pubkey> OP_CHECKSIGVERIFY
  <LP_pubkey> OP_CHECKSIG
OP_ELSE
  <timeout_blockheight> OP_CHECKLOCKTIMEVERIFY OP_DROP
  <LP_pubkey> OP_CHECKSIG
OP_ENDIF
```

**Cooperative path:** Both sign. Normal repayment -- ASP pays back principal + fee, both parties release escrow.

**Timeout path:** LP signs alone after `timeout_blockheight`. ASP defaulted -- LP claims collateral unilaterally. No ASP cooperation needed. Bitcoin consensus enforces it.

Seven opcodes. All battle-tested. Same trust model as Lightning penalty transactions.

### 1.3 Repayment Sources

The protocol spec was imprecise about where repayment comes from. Clarification:

- **Principal return:** The BTC the ASP borrowed goes into covenant trees. When those trees expire (7-30 days depending on implementation -- ~1,008 to ~4,320 blocks), the locked BTC cycles back to the ASP. This is the capital cycle, not revenue -- it's the same BTC coming back.

- **Interest (LP's fee):** Comes from the ASP's fee revenue, which accumulates continuously as rounds process. The ASP doesn't need to wait for tree expiry to have fee income. Fees are earned per-round, per-transaction, throughout the loan term.

- **The ASP's overall liquidity position:** An operating ASP has multiple trees at different stages of expiry, continuous fee income, and potentially Lightning routing revenue. The loan repayment draws on all of these. The escrow exists because the LP cannot verify the ASP's internal cash flow -- but the LP doesn't need to. The escrow guarantees recovery regardless.

### 1.4 What Could Go Wrong Mechanically?

| Failure Mode | Consequence | Mitigation |
|-------------|-------------|------------|
| ASP doesn't repay | LP claims escrow after timeout block height. LP recovers collateral (105-130% of principal). | Built into the protocol. This IS the security model. |
| Escrow script bug | Funds locked or misrouted | 7 well-understood opcodes. Formal review. Small initial loans. |
| Both parties lose keys | Escrow funds unrecoverable | Standard key management. Not unique to ArkPool. |
| LP broadcasts timeout tx before timeout | Transaction is invalid -- Bitcoin consensus rejects it | Enforced by OP_CHECKLOCKTIMEVERIFY. Not gameable. |

**Assessment:** The mechanism works. It is a straightforward application of timelocked multisig, which has been securing Lightning channels since 2018 and Bitcoin HTLCs since 2015. The on-chain footprint is minimal (2 transactions per loan cycle), the trust assumptions are Bitcoin-consensus-only, and the failure modes are well-understood and bounded by the escrow.

---

## 2. When Does Ark Need This?

### 2.1 The Lockup Multiplier

An ASP's locked capital requirement is driven by overlapping tree lifetimes. The ASP locks fresh BTC into a new covenant tree every round. That BTC stays frozen until the tree expires. Multiple trees are active simultaneously:

```
Week 1: Lock 100 BTC into Tree A       (expires end of week 1)  [7-day expiry]
--- At any point: only ~1 week of trees active ---

vs.

Week 1: Lock 100 BTC into Tree A       (expires week 5)         [30-day expiry]
Week 2: Lock 100 BTC into Tree B       (expires week 6)
Week 3: Lock 100 BTC into Tree C       (expires week 7)
Week 4: Lock 100 BTC into Tree D       (expires week 8)
--- At end of week 4: ~400 BTC locked simultaneously ---
```

The base lockup multiplier equals the expiry period in weeks. An estimated ~1.3x "change multiplier" adds on top (when users don't spend their full VTXO, the remainder creates a change output in the new tree that also requires fresh capital without generating additional fees). The 1.3x figure is our own estimate based on typical partial-spend patterns -- it does not appear in any published Ark spec.

**Actual shipping defaults (from source code):**

| Implementation | VTXO Expiry Default | Source | Base Multiplier | With ~1.3x Change |
|---|---|---|---|---|
| **Arkade (arkd)** | **604,672 seconds (~7 days)** | `internal/config/config.go` line 241: `defaultVtxoTreeExpiry = 604672` | ~1x | **~1.3x** |
| **Bark (captaind)** | **4,320 blocks (~30 days)** | `server/captaind.default.toml` line 14: `vtxo_lifetime = 4320` | ~4.3x | **~5.6x** |

Both are operator-configurable. Arkade uses seconds (switchable to blocks). Bark uses blocks natively.

```
locked_btc = weekly_throughput_btc * lockup_multiplier

Arkade default (7-day):   ~1.3x   (only ~1 week of trees overlap)
Bark default (30-day):    ~5.6x   (~4.3 weeks of trees overlap * 1.3x change)
Hypothetical 14-day:      ~2.6x   (~2 weeks overlap * 1.3x change)
```

**Note on V2 revocation:** Burak's V2 proposal would reduce the multiplier further via per-VTXO secret aggregation, letting the ASP recover spent portions of old trees before full expiry. V2 is NOT implemented in either Arkade or Bark as of March 2026. It requires a ZK-based "VPU" that has not been specified or built. Do not assume V2 in any near-term planning.

### 2.2 The Expiry Tradeoff

The operator's choice of expiry period is a tradeoff:

- **Shorter expiry (7 days, Arkade default):** Capital-efficient (~1.3x multiplier). But users must refresh weekly or lose their VTXOs. Delegation (Arkade's shipping feature) mitigates this -- third parties can auto-refresh -- but the liveness requirement is still tighter.
- **Longer expiry (30 days, Bark default):** Capital-intensive (~5.6x multiplier). But users have a month before they need to refresh. Better for infrequent users, savings-style use cases, and situations where delegation isn't set up.

Bark's fee structure explicitly prices this tradeoff. From `captaind.default.toml` and `lib/src/fees.rs`, refresh fees are tiered by PPM (parts-per-million) based on how many blocks remain until expiry:

| Blocks until expiry | Refresh PPM | Effective % | Meaning |
|---|---|---|---|
| <= 96 blocks (~16 hours) | 0 ppm | 0% (base fee only: 150 sat) | Near-expiry refresh is almost free -- the ASP was about to recover this capital anyway |
| 97-198 blocks (~1-1.4 days) | 1,000 ppm | 0.1% | |
| 199-2,160 blocks (~1.4-15 days) | 4,000 ppm | 0.4% | |
| > 2,160 blocks (~15+ days) | 8,000 ppm | 0.8% | Early refresh is expensive -- the ASP locks capital for a long additional stretch |

This is the ASP passing the cost of capital lockup directly to the users who cause it. Users who refresh early (lots of remaining VTXO life) pay more because they're forcing the ASP to commit fresh capital for another full expiry cycle when the old capital had significant time left. Users who wait until near-expiry pay almost nothing because the capital was about to return anyway.

This partially offsets the capital problem (the ASP earns more from users who create more capital pressure) but doesn't eliminate it -- the ASP still needs the BTC upfront to lock into the tree before earning the fee.

Arkade's fee system is fully programmable via CEL expressions (set by the operator via admin API). The defaults are zero -- the operator must configure their own fee programs. Arkade supports time-based formulas using VTXO `expiry`, `birth`, and `amount` variables, enabling the same lockup-weighted pricing if the operator chooses.

### 2.3 The Self-Funding Ceiling

An ASP can self-fund as long as it has enough BTC to cover the lockup. When throughput grows beyond what its holdings support, it either stops growing or borrows.

### 2.4 Adoption Thresholds (All BTC-Denominated)

| Weekly Throughput | Locked BTC (7-day, ~1.3x) | Locked BTC (30-day, ~5.6x) | Who Can Self-Fund This? |
|---|---|---|---|
| 10 BTC/week | 13 BTC | 56 BTC | Any Bitcoin-native startup |
| 50 BTC/week | 65 BTC | 280 BTC | Mid-size Bitcoin companies |
| 100 BTC/week | 130 BTC | 560 BTC | Large exchanges, treasury firms |
| 500 BTC/week | 650 BTC | 2,800 BTC | Only a handful of entities globally |
| 1,000 BTC/week | 1,300 BTC | 5,600 BTC | Effectively nobody (30-day) / Large treasury companies (7-day) |
| 5,000 BTC/week | 6,500 BTC | 28,000 BTC | Impossible to self-fund at either setting |

**The threshold for a single ASP:**

At 7-day expiry (Arkade default, ~1.3x):
- An operator with 200 BTC can process ~150 BTC/week before hitting the wall.
- An operator with 500 BTC can process ~380 BTC/week.
- An operator with 1,000 BTC can process ~770 BTC/week.
- External financing becomes necessary at genuinely high throughput.

At 30-day expiry (Bark default, ~5.6x):
- An operator with 200 BTC can process only ~35 BTC/week.
- An operator with 500 BTC can process ~90 BTC/week.
- An operator with 1,000 BTC can process ~180 BTC/week.
- External financing becomes necessary at moderate throughput.

**The implication:** ArkPool is far more relevant to ASPs running longer expiry periods (for better UX) than to ASPs running Arkade's aggressive 7-day default. At 7-day expiry, most operators can self-fund through significant throughput. At 30-day expiry, the capital wall hits much sooner -- and those ASPs are also earning higher fees from the lockup-weighted fee tiers, making ArkPool borrowing costs more affordable.

**If V2 revocation ships in the future,** the multiplier drops further (potentially to ~0.7-1.5x depending on spend rate and expiry), pushing these thresholds higher. This would delay but not eliminate the need for external capital.

**The threshold for the network:** External financing becomes structurally necessary when the aggregate throughput of all ASPs requires more locked BTC than the combined operator ecosystem holds. This happens when Ark moves from "experimental L2" to "meaningful payment infrastructure" -- probably somewhere around 500-2,000 BTC/week aggregate throughput across all ASPs.

### 2.4 What Drives Throughput Growth?

Ark's throughput depends on user adoption, which depends on Ark offering something users want:

- **Privacy:** Ark transactions do not appear on-chain individually. Users share UTXOs through covenant trees, breaking the on-chain graph. Better privacy than standard Lightning (where channel opens/closes are visible).
- **UX:** No channel management, no inbound liquidity problems, no routing failures. Onboarding is a single round participation. Simpler than Lightning for end users.
- **Batch efficiency:** One on-chain transaction can settle hundreds of user transactions. At scale, the per-user cost approaches zero.

Recent implementation advances improve both UX and operational viability:

- **Delegation (Arkade, shipping):** Users sign a BIP322 message authorizing a third party to refresh their VTXOs automatically. Users don't need to come online every 7-30 days (depending on expiry setting). This makes the ASP's capital cycle more predictable (fewer surprise unilateral exits) and makes Ark usable for non-technical users. Especially important at Arkade's 7-day default, where weekly refresh would otherwise be burdensome.
- **hArk (Second, shipping):** Eliminates the requirement for all users to be online simultaneously during round construction. Users submit intents asynchronously; the ASP builds the round without real-time coordination. This removes a major scaling bottleneck -- Bark can handle up to 65,536 leaf VTXOs per round (`nb_round_nonces = 8`, radix^8 from `captaind.default.toml`).

Neither changes the lockup multiplier, but both make Ark more practical as a payment system, which drives the throughput growth that creates demand for ArkPool.

### 2.4 The "Idle BTC Yield Product" Framing

The previous analysis benchmarked lender rates against active yield strategies (Lightning routing at 1.5%, Magma at 2.6%, Ledn at 2-5.25%). This is the wrong comparison for most potential lenders.

The vast majority of BTC sits in cold storage earning 0%. The real comparison is:

| Option | Yield | Risk | Complexity | Custody |
|--------|-------|------|-----------|---------|
| Cold storage | 0% | Price only | None | Self |
| ArkPool lending | 1.5-3% annualized | ASP operational failure (escrow protects principal) | Low (send BTC to escrow, wait for term, collect) | Self (timelocked multisig) |
| Lightning routing | 1-2% | Operational (uptime, force-close, rebalancing) | High (run a node, manage channels) | Self |
| Magma leasing | 2.6% | Counterparty, channel closure | Medium | Self |
| CeFi lending (Ledn) | 2-5.25% | Platform insolvency (BlockFi/Celsius lesson) | Low | Custodial |

ArkPool is the simplest non-custodial BTC yield product in the table. The LP deposits BTC into an on-chain escrow, waits for a fixed number of blocks, and collects principal + fee. No node to run, no channels to manage, no platform to trust with custody. The escrow script guarantees recovery even if the ASP vanishes.

At 1.5-2% annualized, this is competitive against doing nothing (which is what most BTC does). The lender floor is not 3-5%. It's whatever beats 0% with credible non-custodial security. That floor is probably 1-2%.

### 2.6 Does the Spread Clear?

Working in BTC only. Consider an ASP processing 100 BTC/week:

**30-day expiry (Bark default, ~5.6x):** 560 BTC locked. Higher fee revenue due to lockup-weighted tiers.

```
Weekly fee revenue:     100 BTC * ~0.004 (blended, higher due to 0.4-0.8% lockup tiers) = 0.4 BTC/week
Annual fee revenue:     0.4 * 52 = 20.8 BTC/year
Operating costs:        ~2-4 BTC/year
Net operating income:   ~17-19 BTC/year on 560 BTC locked
```

ASP has 300 BTC, borrows 260 BTC at 2% annualized:

```
Annual borrowing cost:  260 * 0.02 = 5.2 BTC
Remaining income:       17-19 - 5.2 = 11.8-13.8 BTC/year
```

At 3%: borrowing cost 7.8 BTC, remaining 9.2-11.2 BTC/year. Still comfortable.

**7-day expiry (Arkade default, ~1.3x):** 130 BTC locked. Lower fees (shorter lockup = lower tier charges).

```
Weekly fee revenue:     100 BTC * ~0.002 (blended, lower tiers dominate) = 0.2 BTC/week
Annual fee revenue:     0.2 * 52 = 10.4 BTC/year
Operating costs:        ~2-4 BTC/year
Net operating income:   ~6.4-8.4 BTC/year on 130 BTC locked
```

At 7-day expiry, the ASP with 130 BTC likely doesn't need to borrow at all (130 BTC locked, operator probably has that). If processing 500 BTC/week (650 BTC locked, ASP has 400, borrows 250 at 2%):

```
Annual fee revenue:     500 * 0.002 * 52 = 52 BTC/year
Borrowing cost:         250 * 0.02 = 5 BTC
Remaining after costs:  52 - 5 - ~5 (opex) = ~42 BTC/year
```

**The spread works across both expiry settings.** The 30-day ASP borrows more but also earns more per unit of throughput (lockup-weighted fees compensate). The 7-day ASP borrows less but earns less per unit. The economics break only at lending rates above ~7-10%, far above the expected range for idle BTC.

---

## 3. High Fee Environment: 200-500 sat/vB Sustained

This is the stress test. Sustained high fees affect Ark operations and, indirectly, ArkPool demand.

### 3.1 Impact on ArkPool Directly

ArkPool's on-chain footprint per loan cycle:

| Transaction | Estimated vBytes | Cost at 200 sat/vB | Cost at 500 sat/vB |
|-------------|-----------------|--------------------|--------------------|
| Escrow funding (P2WSH) | ~150 vB | 30,000 sats (0.0003 BTC) | 75,000 sats (0.00075 BTC) |
| Escrow release (cooperative close) | ~110 vB | 22,000 sats (0.00022 BTC) | 55,000 sats (0.00055 BTC) |
| **Total per loan cycle** | ~260 vB | **0.00052 BTC** | **0.0013 BTC** |
| Default claim (timeout path) | ~130 vB | 0.00026 BTC | 0.00065 BTC |

On a 30 BTC loan, 0.0013 BTC in on-chain costs is 0.004% of principal. **ArkPool's mechanism is fee-insensitive.** Even at 500 sat/vB sustained, the on-chain cost of lending is negligible relative to loan size.

### 3.2 Impact on Ark Operations (Upstream)

This is where high fees matter. Ark rounds require on-chain commitment transactions.

| Round tx size (estimated) | Cost at 20 sat/vB | Cost at 200 sat/vB | Cost at 500 sat/vB |
|--------------------------|-------------------|--------------------|--------------------|
| Small round (~500 vB) | 0.0001 BTC | 0.001 BTC | 0.0025 BTC |
| Medium round (~2,000 vB) | 0.0004 BTC | 0.004 BTC | 0.01 BTC |
| Large round (~5,000 vB) | 0.001 BTC | 0.01 BTC | 0.025 BTC |

**Batching as the primary mitigation:**

In practice, rounds run much more frequently than hourly. Arkade runs sessions back-to-back (30-second session duration, continuous). Bark runs rounds every 10 seconds. At normal fee rates, this is fine -- each round's on-chain cost is tiny. At 500 sat/vB, the ASP must reduce frequency:

| Strategy | Rounds/day | Daily on-chain cost (medium rounds) | Throughput capacity |
|----------|-----------|-------------------------------------|-------------------|
| Hourly rounds | 24 | 0.24 BTC/day at 500 sat/vB | High (low latency) |
| Every 4 hours | 6 | 0.06 BTC/day | Moderate (users wait up to 4 hours) |
| Every 12 hours | 2 | 0.02 BTC/day | Lower (half-day settlement) |
| Daily rounds | 1 | 0.01 BTC/day | Lowest (24-hour settlement) |

At 500 sat/vB sustained, an ASP processing 100 BTC/week shifts from hourly to 4-12 hour rounds. Annual on-chain cost:

```
Every 4 hours: 0.06 * 365 = 21.9 BTC/year
Every 12 hours: 0.02 * 365 = 7.3 BTC/year
```

Against 15.6 BTC/year in fee revenue (100 BTC/week at 0.3%), 21.9 BTC in on-chain costs is unsustainable. The ASP must either:
1. Reduce round frequency to every 12+ hours (7.3 BTC/year -- survivable)
2. Increase fees to compensate (0.5%+ blended, which may drive users to Lightning)
3. Lean harder on OOR (out-of-round) payments, which have zero on-chain cost per payment

### 3.3 OOR as the High-Fee Escape Valve

Out-of-round (OOR/Arkoor) payments are instant, off-chain transfers between users on the same ASP. They require no on-chain transaction -- just a co-signed VTXO transfer. During high-fee periods:

- The ASP reduces round frequency (saving on-chain costs)
- Users transact via OOR between rounds (no latency penalty for most payments)
- Rounds batch more transactions per commitment (amortizing the on-chain cost)
- Users refresh their OOR VTXOs into trustless in-round VTXOs when fees drop

This means Ark's effective throughput does not collapse linearly with fee increases. OOR absorbs the payment demand; rounds handle settlement when economically viable.

### 3.4 Impact on ArkPool Demand During High Fees

High fees affect ArkPool indirectly:

1. **Reduced round frequency** means less BTC is committed to new trees per day. The ASP's capital need shrinks temporarily because it's processing fewer rounds.
2. **But locked capital doesn't return faster.** Trees still expire on their original schedule. The ASP has the same capital locked but is generating less new throughput. This could actually INCREASE the need for external capital during the transition (the ASP's existing capital is locked in old trees while new fee revenue drops).
3. **Escrow costs are negligible** even at 500 sat/vB (~0.0013 BTC per loan cycle). ArkPool's mechanism is unaffected.

### 3.5 Contingency: Sustained 200-500 sat/vB for 30+ Days

| Scenario | Ark Response | ArkPool Impact |
|----------|-------------|----------------|
| 200 sat/vB, 1 week | Reduce to 6-hour rounds. OOR absorbs payments. | Minimal. Loan cycles continue normally. |
| 200 sat/vB, 30 days | 12-hour rounds. OOR-dominant. Some users defer non-urgent txs. | Reduced new lending demand (fewer rounds need funding). Existing loans unaffected. |
| 500 sat/vB, 1 week | 12-24 hour rounds. OOR only for most users. Fee increase likely. | No new lending. Existing escrows unaffected (0.0013 BTC to close). |
| 500 sat/vB, 30 days | Survival mode. Daily rounds at most. ASPs with thin margins may pause operations. | Lending market freezes (no demand). Existing escrows survive -- LP claims at timeout cost 0.00065 BTC. Outstanding loans either repaid or defaulted normally. |
| 500 sat/vB, 90+ days | Existential threat to Ark (and all L2s that require on-chain settlement). | ArkPool is the least of anyone's problems. But the mechanism still works -- escrow claims are cheap even at 500 sat/vB. |

**Key insight:** ArkPool is more fee-resilient than Ark itself. Ark needs on-chain transactions every round. ArkPool needs on-chain transactions twice per loan (setup + teardown), and the loan term is 2,016-4,032 blocks. The amortized on-chain cost per block of lending is negligible.

---

## 4. Technical Viability

### 4.1 What Needs to Be Built (Phase 1)

| Deliverable | Description | Effort |
|-------------|------------|--------|
| Escrow script library | Create, fund, verify, cooperatively close, and timeout-claim the timelocked 2-of-2 multisig | 2-4 weeks |
| Term sheet format | JSON schema for loan parameters (amount, term in blocks, rate, collateral ratio, escrow script hash) | 1 week |
| Proof-of-reserves tool | UTXO ownership attestation + tree expiry schedule verification | 1-2 weeks |
| CLI | Wrap the above into a command-line tool for ASP operators and LPs | 1-2 weeks |
| Documentation | Usage examples, security model explanation | 1 week |

**Total: 5-8 weeks.** No smart contracts, no sidechains, no oracles, no new infrastructure.

### 4.2 What Does NOT Need to Be Built

- **No oracle.** The escrow timeout is enforced by Bitcoin consensus at a block height. Repayment is verified by the LP receiving BTC. If the LP receives payment, both parties cooperatively close the escrow. If not, the LP waits for the timeout and claims. No third party attests to anything.
- **No DLC.** DLCs add complexity (oracle dependency, attestation protocol) for marginal benefit (partial repayment handling). Phase 1 handles only binary outcomes: repaid or defaulted. Partial repayment is handled socially (negotiate a new escrow) or by the LP claiming the full collateral and the ASP losing the surplus.
- **No web interface.** At 2-5 ASPs, everyone talks directly. A bulletin board or auction protocol is premature.
- **No Ark protocol changes.** ArkPool sits alongside the ASP, not inside it. The ASP borrows BTC, deposits it into its wallet, and uses it to fund rounds through normal arkd/bark operations.

---

## 5. Risk Assessment

### 5.1 Risks to the Mechanism

| Risk | Severity | Probability | Notes |
|------|----------|-------------|-------|
| Escrow script bug | High (funds at risk) | Very low | 7 well-understood opcodes. Same pattern as Lightning. Formal review + small initial loans. |
| ASP defaults | Moderate (LP claims collateral, market trust damaged) | Low per loan | This is the designed failure mode. LP recovers 105-130% of principal. |
| Sustained 500+ sat/vB | Low for ArkPool, high for Ark | Low (historically transient) | ArkPool's 2 on-chain txs per loan are cheap even at extreme rates. Ark's rounds are the bottleneck. |
| Key loss (ASP or LP) | High | Very low | Standard key management. Not unique to this protocol. |

### 5.2 Risks to Adoption

| Risk | Severity | Probability | Notes |
|------|----------|-------------|-------|
| Too few ASPs (<3) for 3+ years | High (no market) | Medium | Bilateral tool still works for 2 parties. Sunk cost is 5-8 weeks. |
| Ark Labs builds proprietary liquidity layer | Medium (ArkPool redundant for Arkade) | Medium | ArkPool serves all implementations. Position as open standard. |
| Ark adoption stalls | High (no demand) | Medium | ArkPool investment is minimal until Ark proves traction. |
| HODLers don't trust "earn yield on BTC" after Celsius/BlockFi | Medium (slow LP onboarding) | Medium | The escrow is non-custodial and verifiable on-chain. Education problem, not mechanism problem. |

### 5.3 LP Unilateral Exit Risk (Per-Round Integration)

The per-round integration model (protocol-spec.md v0.2) exposes LPs to a risk that the standalone escrow model does not: when users in an LP-funded round unilaterally exit (broadcast the pre-signed exit transaction chain on-chain instead of refreshing), the LP's forfeit claim on those VTXOs is voided. The LP's principal recovery depends on user behavior the LP cannot control.

**Why this is the central design problem:**

The spec assumes 2-5% exit rates during normal operations. But the scenario that matters is correlated exits -- ASP misbehavior, a competing ASP launching with better terms, a fee spike making refreshing uneconomical. In those cases, exit rates are 30-80%, not 5%. The LP's real risk is the tail, not the average.

**Three models explored, none fully satisfactory:**

| Model | LP Protection | ASP Capital Gain | Problem |
|-------|--------------|-----------------|---------|
| Secured loan (old Approach A) | Full -- ASP posts 110% collateral | Net negative -- posting 110% to borrow 100% | Only works if ASP has idle reserves separate from operating capital |
| Unsecured round participation (Approach B) | None -- LP bears exit risk | Full -- ASP gets fresh capital with no collateral | LP principal not guaranteed in stress scenarios |
| Hybrid (partial collateral) | Partial | Partial | Collapses into one of the above depending on ratio. Not a real third option |

**Directions investigated and their status:**

**REJECTED: Tree-structural seniority.** Initial idea: place LP claims at higher tree levels so leaf-level exits don't affect them. **Disproven after code review.** Unilateral exit broadcasts the entire path from root to leaf -- every intermediate transaction in the path is spent on-chain. A claim at a higher tree level is voided by ANY exit in the subtree below it, making the LP MORE exposed, not less. The covenant tree concentrates risk upward, not downward. (Verified: Arkade `builder.go:256-318`, Bark `exit/vtxo.rs:45-60`.)

**REJECTED: LP-payback output in poolTx.** Idea: add a time-locked output in the poolTx that pays the LP independently of user behavior. **Fails on funding.** If the LP contributes X BTC and we add X+fee as a separate output, the poolTx needs ~2X total -- the LP's contribution doesn't reduce the ASP's capital requirement, it increases it. The payback output must be funded from somewhere other than the LP's own contribution, which means the ASP needs separate capital anyway. (Verified: poolTx structure at Arkade `builder.go:708-769` -- outputs are batch, connector, on-chain exits, change.)

**UNDER INVESTIGATION: Fee-funded insurance pool.** The ASP earns fees on every refresh. Over the LP's term (~7-30 days), the ASP's cumulative fee revenue could backstop LP losses from exits. The ASP pre-funds a multisig UTXO (LP + ASP) sized to the LP's tail risk. If forfeit proceeds fall short, the LP claims from the insurance pool after tree expiry + grace period. The ASP's cost: locking fee revenue (~10-20% of LP contribution) as insurance, far less than 110% collateral. Open questions: (a) Can the insurance pool be structured as a Bitcoin script without new trust assumptions? (b) Does the ASP's fee revenue reliably cover tail exit scenarios (30%+ correlated exits)? (c) Does this create circular dependency if the ASP's overall position deteriorates? See `lp-exit-risk-analysis.md` for detailed treatment.

**UNDER INVESTIGATION: Actuarial pricing with structural caps.** Accept the risk but bound it. The LP funds at most X% of any single round, diversified across N rounds. Fee pricing assumes 10-15% expected exit rate (not 2-5%), so the LP's expected return remains positive even in moderate stress. Open question: whether the higher fee makes ArkPool uncompetitive versus ASP self-funding.

**The core tension:** Full collateral = LP safe but ASP gains nothing. No collateral = ASP gains capital but LP exposed. The insurance pool model is the most promising middle ground -- the ASP posts partial collateral from operating revenue rather than idle reserves. Resolution of this problem is required before the protocol spec can advance beyond draft. Full analysis in `lp-exit-risk-analysis.md`.

### 5.4 What Does NOT Kill It

- **Fee compression.** Even at 0.15% ASP fees, the spread works if lenders accept 1-2% (idle BTC yield). The spread analysis only fails if lenders demand returns that exceed ASP revenue, which requires lender expectations above ~8%.
- **BTC price volatility.** Everything is BTC-denominated. The ASP borrows BTC, locks BTC collateral, earns BTC fees, repays BTC. No FX exposure in the core protocol.
- **On-chain fee spikes.** ArkPool's mechanism survives any fee environment. Ark itself may struggle, which reduces demand for ArkPool, but the existing loans and escrows are unaffected.

---

## 6. Competitive Landscape

Nobody is building this. Confirmed via prior art search (`prior-art-and-resources.md`):

- **ben2077's issue #197** (arkade-os/arkd): Only direct proposal. Concept sketch, no spec, associated PR closed.
- **Lendasat:** DLC VTXOs for user-facing lending ON Ark. Different problem (capital TO users, not TO ASPs).
- **Lightning Pool:** Channel lease auctions. No Ark awareness.
- **Lygos, Lava Loans:** Institutional BTC lending via DLCs. No ASP integration.
- **Ark Labs / Second:** Could build this internally. Ark Labs has Fulgur/Tether backing. If they do, ArkPool is redundant for Arkade but not for Bark or future implementations.

The gap is real. Whether it stays empty depends on whether Ark reaches the throughput threshold where external capital is needed.

---

## 7. Recommendation

### 7.1 Build Phase 1

The CLI toolkit (escrow library, term sheet format, proof-of-reserves, documentation). 5-8 weeks. Minimal sunk cost.

### 7.2 Publish the Research

The 17 documents in this series are the most thorough public analysis of ASP liquidity economics. Publishing establishes priority, draws attention to the capital constraint, and invites scrutiny that strengthens the design.

- GitHub repo (spec + research notes)
- Comment on ben2077's issue #197
- Delving Bitcoin post for developer audience

### 7.3 Watch the Throughput Number

ArkPool becomes necessary at a specific, observable threshold: when ASP operators report that capital constraints are limiting their throughput. Until then, the tool exists, the research is published, and the mechanism is ready. The adoption question answers itself as Ark grows.

---

## Sources

### Implementation Source Code (cloned locally)

| Value | Source | File |
|-------|--------|------|
| Arkade VTXO expiry: 604,672s (~7 days) | arkade-os/arkd | `internal/config/config.go:241` |
| Arkade session duration: 30s, continuous | arkade-os/arkd | `internal/config/config.go:228` |
| Arkade max round participants: 128 | arkade-os/arkd | `internal/config/config.go` |
| Arkade fees: CEL programs, zero by default | arkade-os/arkd | `pkg/ark-lib/arkfee/README.md` |
| Arkade fee variables: amount, expiry, birth, weight | arkade-os/arkd | `pkg/ark-lib/arkfee/celenv/variables.go` |
| Bark VTXO lifetime: 4,320 blocks (~30 days) | ark-bitcoin/bark | `server/captaind.default.toml:14` |
| Bark round interval: 10 seconds | ark-bitcoin/bark | `server/captaind.default.toml:68` |
| Bark max VTXOs per round: 65,536 (radix^8) | ark-bitcoin/bark | `server/captaind.default.toml` (`nb_round_nonces = 8`) |
| Bark refresh fee: 150 sat base + 0-8000 ppm by expiry | ark-bitcoin/bark | `server/captaind.default.toml:188-235`, `lib/src/fees.rs` |
| Bark board fee: 100 sat + 1000 ppm (0.1%) | ark-bitcoin/bark | `server/captaind.default.toml` |
| Bark fallback fee rates: 4/10/25 sat/vB | ark-bitcoin/bark | `server/captaind.default.toml:262-274` |

### Research Documents (this series, 17 total)

| Document | Contribution |
|----------|-------------|
| `protocol-spec.md` | Mechanism design, escrow construction, transaction flows |
| `unit-economics.md` | Fee revenue dynamics, cost structure, lender benchmarks |
| `constraints.md` | Protocol constraints, BTC-for-BTC reframe, go/no-go |
| `interbank-liquidity.md` | Liquidity sources, fed funds parallel, cold start analysis |
| `prior-art-and-resources.md` | Gap confirmation, competitive landscape, all external links |
| `problem-spec.md` | Throughput scaling scenarios |

### Derived Estimates (not from published sources)

| Estimate | Basis | Confidence |
|----------|-------|-----------|
| ~1.3x change multiplier | Assumption: average partial spend creates ~30% overhead in change outputs | Moderate -- reasonable but not validated against real Ark traffic data |
| Lockup multiplier formula: `expiry_weeks * 1.3` | Derived from mechanical reality of overlapping trees + change estimate | High for base multiplier, moderate for change factor |

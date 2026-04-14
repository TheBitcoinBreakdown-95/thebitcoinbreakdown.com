# ArkFloat Brainstorm Output

Running results from the 8-phase brainstorming pipeline. Each problem gets Phase A-H records appended sequentially.

---

## P1: Fee Adequacy

### Phase A: Operationalize

**Problem statement:** The LP lending math clears only when ASPs sustain a blended user fee rate of ~0.35-0.40%. Below this, the ASP cannot pay lenders a competitive return (3-5%) while retaining acceptable profit. The question is whether this rate is sustainable under competitive pressure, or whether fee compression will push blended rates below the threshold.

**What's broken:** At the current central estimate of 0.3% blended fees, there is no positive spread between what the ASP can afford to pay lenders and what lenders demand. The financing market does not clear. The entire ArkFloat thesis depends on fees being ~15-30% higher than the only published reference point (Second's schedule, which blends to ~0.3%).

**Assumptions this rests on:**
1. Second's fee schedule (0-0.5% tiered by VTXO age) is representative of what ASPs will charge
2. The blended average lands at ~0.3% given typical user behavior (mix of near-expiry refreshes at 0% and early refreshes at 0.5-0.8%)
3. Lightning at ~0.006% median routing fee is the relevant competitive benchmark for pure payments
4. Ark's value proposition (simpler UX, better privacy, no node required) justifies a 50-100x premium over Lightning routing fees

**What "solved" looks like:**
- A credible argument that 0.35-0.40% blended is sustainable (not just possible), OR
- An alternative revenue mechanism that supplements transaction fees, OR
- A demonstration that the 0.3% estimate is conservative and realistic blended rates are higher, OR
- An honest conclusion that LP lending is unviable at current fee levels and requires either fee increases or stablecoin throughput to work

**Variables:**
- User behavior mix (what fraction of refreshes happen near-expiry vs. early)
- Number of competing ASPs (more competition = lower fees)
- OOR fee levels (not published; estimated 0.1-0.2%)
- OOR-to-round transaction ratio (more OOR = lower blended fee)
- Stablecoin throughput (higher volume at same rates improves economics)
- V2 revocation adoption timeline (reduces capital lockup, changes fee dynamics)

**Dependencies:**
- P2 (LP yield): P1 sets the ceiling on what LPs can earn. If P1 fails, P2 is moot.
- P3 (Change output drag): The 1.3x change multiplier inflates the denominator in ROI calculations, directly reducing effective fee yield.
- P8 (Small ASP adverse selection): Small ASPs need higher fees to service LP debt, but higher fees make them less competitive -- a spiral that depends on the fee adequacy floor.
- P9 (Scale economics): OOR cost collapse at volume means large ASPs can sustain lower fees. The 0.35% threshold may apply to small ASPs but not large ones.

### Phase B: Research

**Research date:** April 2026

**Key finding -- 0% Ark-to-Ark fees change everything:** Second's published fee schedule (second.tech/docs/learn/fees) shows Ark send/receive at **0%**. Lightning send is 0.2-0.5% (tiered by VTXO age). Offboard (on-chain) send is 0.2-0.5% + on-chain fees. Refresh is 0-0.5% (free within 2 days of expiry).

This means the blended fee rate depends entirely on the traffic mix. If a majority of transactions are Ark-to-Ark (which is the intended scaling path -- OOR payments between users on the same ASP), the ASP collects **zero fee revenue** on that volume. The 0.3% blended estimate assumed all transactions generate fees. In reality, only Lightning sends, offboards, and non-near-expiry refreshes generate revenue.

**Revised blended fee scenarios:**

| Traffic mix | Blended fee | Viability for LP lending |
|---|---|---|
| 80% Lightning/offboard, 20% Ark-to-Ark | ~0.30-0.35% | Marginal -- near the 0.35% threshold |
| 50/50 | ~0.15-0.20% | Below breakeven -- LP market does not clear |
| 20% Lightning/offboard, 80% Ark-to-Ark | ~0.05-0.08% | Non-viable |

The 0% Ark-to-Ark fee is rational for Second (it incentivizes Ark adoption over Lightning bridging), but it structurally undermines the fee revenue base that LP lending depends on. An ASP optimizing for user growth will push Ark-to-Ark volume, which pushes blended fees down.

**Arkade fee model:** Arkade uses CEL expression programs (operator-defined). Default is zero. No published schedule. Arkade's $5.2M seed round (Tether, Ego Death Capital, March 2026) and integrations with Boltz, Breez, BTCPay, Hodl Hodl suggest a growth-first strategy. Fee revenue is not the near-term priority.

**Competitive yield landscape (updated April 2026):**

| Product | BTC yield | Notes |
|---|---|---|
| Amboss Rails | 1-4% APY | Self-custodial, Lightning routing + Magma leases. 1 BTC min, 1yr commitment. |
| Amboss Magma | ~2.6% at scale, >4% below 1 BTC | Liquidity leases |
| Ledn | **0% on BTC** (dropped BTC Growth Accounts) | Only stablecoin yields now (6.5-8.5%) |
| Nexo | ~3-7% headline | Tier-dependent; counterparty risk |
| Babylon staking | 0% BTC-denominated | Yield is BABY token emissions, not BTC |
| Holding BTC | 0% | Zero risk, instant liquidity |

**Critical shift:** The safe BTC yield market has contracted sharply. Ledn dropped BTC yields entirely. Babylon yields are token emissions, not BTC-native. The realistic safe BTC yield for a cautious holder is now **0-3%**, not 2-5%. This actually helps ArkFloat's LP competitiveness -- there's less competition for BTC yield products.

**Lightning fee compression:** Industry analysts predict 40-60% fee decreases over 2 years from routing improvements and enterprise adoption. Public Lightning volume up 266% YoY in 2025 despite transaction count declines (shift to higher-value). This means Lightning leasing yields may compress too, keeping ArkFloat relatively competitive.

**Ark adoption data:** Two implementations live (Arkade, Second). No public throughput dashboards, no TVL figures, no user counts beyond ~1,300 payments at Baltic Honeybadger 2025. The ecosystem is pre-market.

**What this means for P1:**
- The 0.35-0.40% breakeven threshold is achievable only if the ASP's traffic mix is dominated by Lightning sends and offboards (the transactions that generate fees)
- An ASP optimizing for Ark-native payments will have a lower blended fee, potentially below breakeven
- The fee adequacy question is really a traffic mix question: what fraction of an ASP's volume touches Lightning or on-chain?
- Stablecoin throughput (Tether's investment in Ark Labs) could change the equation by introducing a new fee-generating transaction type at high volume

**What this means for P2:**
- LP yield of 1-3% is more competitive than previously assessed because the BTC yield market has contracted
- The primary competition is Amboss Rails (1-4%) and Magma (2.6%), not CeFi
- ArkFloat's differentiator (on-chain collateral, no custodian) is stronger in a post-Celsius/BlockFi world where CeFi trust is low
- But the yield only materializes if P1 is resolved -- and the 0% Ark-to-Ark fee is a structural headwind

**Prior art gaps:** No academic work on Ark ASP fee sustainability. No public analysis of optimal fee structures for covenant-tree-based L2s. Second's 3-part liquidity research series remains the closest industry analysis.

**Sources:**
- [Second fee schedule](https://second.tech/docs/learn/fees)
- [Amboss Rails announcement](https://amboss.tech/blog/introducing-rails)
- [Ledn savings (current)](https://www.ledn.io/savings)
- [Babylon Labs](https://babylonlabs.io/) / [Kiln Babylon data](https://www.kiln.fi/protocols/babylon)
- [Ark Labs $5.2M raise](https://tether.io/news/tether-announces-strategic-investment-in-ark-labs-reintroducing-stablecoins-to-programmable-bitcoin-infrastructure/)
- [Atlas21 - Block Lightning yield](https://atlas21.com/lightning-routing-yields-10-annually-blocks-announcement/)
- [CoinLaw Lightning stats](https://coinlaw.io/bitcoin-lightning-network-usage-statistics/)

---

## P2: LP Yield Structurally Thin

### Phase A: Operationalize

**Problem statement:** Even if fee adequacy (P1) is resolved and ASPs can pay lenders, the resulting LP yield of 1-3% annualized may not be attractive enough to draw capital. The product competes with Lightning leasing (~2.6% Magma), CeFi lending (2-5.25% Ledn), and holding BTC at 0%. The yield must exceed risk-adjusted alternatives to attract a new class of lender.

**What's broken:** The yield range (1-3%) overlaps with the lower end of existing alternatives but carries novel risks that those alternatives don't:
- **Unilateral exit risk** (P5): LP can lose principal if users exit on-chain. No equivalent in Lightning leasing or CeFi lending.
- **Novelty risk**: ArkFloat doesn't exist yet. First-mover LPs face protocol risk, implementation risk, and market risk simultaneously.
- **Illiquidity**: 14-28 day lockup with no early exit. Lightning channels can be force-closed; CeFi has withdrawal windows.
- **Small market**: 2-5 ASPs initially. Limited diversification opportunity.

At 1-3%, the yield is comparable to alternatives that carry less risk and are better understood. At 3-5% (feasible only at higher fee rates per P1), it becomes competitive.

**Assumptions this rests on:**
1. Lightning leasing median ~2.6% APR is the closest comparable product
2. CeFi lending 2-5.25% is the broader competitive set
3. Holding BTC at 0% is the floor -- any positive yield is theoretically attractive
4. LPs are rational actors comparing risk-adjusted returns across options
5. The on-chain collateral story (pre-signed forfeits, no custodian) is a meaningful differentiator vs. CeFi counterparty risk

**What "solved" looks like:**
- A yield level that is demonstrably competitive after risk adjustment, OR
- Non-yield value propositions that attract capital for reasons beyond pure return (ecosystem alignment, strategic positioning, deal flow access), OR
- A segmented analysis showing which LP profiles find the product attractive (HODLers vs. active yield farmers vs. institutional allocators), OR
- An honest conclusion that LP yield is only attractive in the stablecoin-throughput scenario where volumes drive higher absolute returns

**Variables:**
- Fee rate (P1 outcome directly determines yield ceiling)
- Exit risk profile (P5 outcome determines risk premium required)
- Competing yield products (evolving market -- Babylon staking, new CeFi entrants)
- BTC price environment (low-volatility = more yield-seeking behavior; high-volatility = risk aversion)
- Number of ASPs available for diversification
- LP sophistication (institutional vs. retail risk appetite)

**Dependencies:**
- P1 (Fee adequacy): Sets the yield ceiling. If P1 gives 0.35%, LP yield is ~2-4%. If P1 gives 0.5%, LP yield is ~4-8%.
- P5 (Unilateral exit risk): The primary risk that LPs must be compensated for. Higher exit risk = higher required yield = harder to attract capital.
- P6 (Insurance pool circular dependency): If insurance is part of the risk mitigation, its reliability determines how much yield premium LPs demand.
- P7 (LP diversification): Whether LPs can diversify across ASPs affects the risk-adjusted return calculation.
- P19 (Cold start): The first LPs face the worst risk/return ratio. Bootstrapping requires either above-market rates or non-economic motivations.

### Phase B: Research

**Research date:** April 2026

Shared research with P1 (see P1 Phase B for full data). LP-specific findings:

**The competitive landscape has narrowed in ArkFloat's favor.** Ledn dropped BTC yields. Babylon pays in BABY tokens, not BTC. The only credible BTC-native yield products are Amboss Rails (1-4%, requires Lightning node operation or 1yr commitment) and Magma leasing (2.6% at scale). An LP product offering 2-4% with on-chain collateral and 14-28 day terms occupies a genuine gap.

**LP segmentation analysis:**

| LP profile | Attractive yield | Risk appetite | ArkFloat fit |
|---|---|---|---|
| HODLer (cold storage, 0% yield) | Any positive yield | Very low | Moderate -- yield is attractive but exit risk is novel |
| Lightning operator (1.5-2.6%) | 3%+ to switch | Medium (already managing channel risk) | Strong -- similar operational model, better yield potential |
| CeFi refugee (post-Celsius, earning 0%) | 1-3% with proof of collateral | Low | Strong -- on-chain collateral is the key differentiator |
| Institutional allocator | Risk-adjusted 4%+ | Medium-high | Weak at current scale -- market too small, no track record |

**Non-yield value propositions (from research):**
- **Ecosystem alignment:** LPs who are Ark users or developers may lend at below-market rates to support the protocol they depend on. This is how Lightning Pool bootstrapped.
- **Deal flow access:** Early LPs to a growing ASP secure priority access at better rates later. A form of strategic optionality.
- **Privacy premium:** ArkFloat lending is pseudonymous, on-chain, and non-custodial. For LPs who value privacy (cannot or will not KYC for CeFi), this may be the only BTC yield option available.

**The honest assessment:** LP yield at 1-3% is not compelling for institutional capital or yield-maximizing allocators. It IS competitive for the specific niche of BTC holders who (a) want yield, (b) refuse custodial counterparty risk, and (c) accept novel protocol risk in exchange for on-chain collateral. This niche exists but is small. Scaling beyond it requires either higher yields (dependent on P1 fee resolution) or the stablecoin throughput scenario where volume makes absolute returns meaningful even at thin rates.

**Prior art -- bootstrapping liquidity markets:**
- Lightning Pool launched with underpriced initial channel leases to build volume
- Amboss Magma started P2P with bilateral negotiation before adding automated matching
- Both demonstrate that BTC liquidity markets can bootstrap from small bilateral beginnings -- but neither faced the unilateral exit risk that ArkFloat LPs bear

---

## P5: Unilateral Exit Risk

### Phase A: Operationalize

**Problem statement:** When LP capital enters an Ark round (per-round integration model), the LP's repayment depends on forfeit transactions that are only claimable if users refresh their VTXOs. Users who unilaterally exit void the forfeit on their VTXOs -- the LP loses that principal. This risk is correlated, tail-heavy, and not diversifiable within a single ASP.

**What's broken:** Two directions have already been explored and rejected:
- **Direction 1 (tree-structural seniority):** Fails because covenant trees concentrate risk upward. Higher tree levels are voided by MORE exits, not fewer. Opposite of tradfi structured finance.
- **Direction 2 (LP-payback output in poolTx):** Fails because funding the payback requires the ASP to lock ~2x the LP contribution, defeating the purpose of external capital.

Two directions remain under investigation:
- **Direction 3 (fee-funded insurance pool):** Promising but has circular dependency -- the same stress event that causes exits also depletes insurance funding.
- **Direction 4 (actuarial pricing with structural caps):** Simple but requires LPs to accept principal loss risk. "BTC yield product where you can lose 20% in a stress event" is a hard sell.

**What's actually at stake:** This is the core risk-engineering problem for ArkFloat. The LP's security model (pre-signed forfeits) is sound for the cooperative case but degrades under adversarial conditions. The base case (2-5% exits) is manageable. The stress case (30-80% exits from ASP misbehavior, competition, or shutdown) is catastrophic for single-round LPs.

The fundamental tension: unilateral exit is sacrosanct in Ark (design principle P1 in constraints.md). Any mechanism that restricts exit to protect LPs violates Ark's core value proposition. The LP must live with exit risk -- the question is how to price, bound, and diversify it.

**Assumptions this rests on:**
1. Normal exit rates are 1-3% (source: protocol spec, inferred from on-chain exit costs)
2. Stress exit rates of 30-80% are plausible under specific scenarios (ASP misbehavior, competition)
3. Exit events are correlated across all rounds with the same ASP
4. Cross-ASP diversification reduces correlation but requires multiple ASPs to exist
5. At 5% expected exit rate, breakeven fee on a 30 BTC position is ~1.5 BTC per term (5% of principal) -- annualized, this exceeds realistic ASP fee revenue

**What "solved" looks like:**
- A risk management framework that makes LP positions actuarially viable at realistic fee levels, OR
- A hybrid insurance + pricing mechanism that bounds downside without circular dependency, OR
- A structural change to how LP capital enters rounds that reduces exit exposure (without violating unilateral exit), OR
- An honest conclusion that per-round LP integration only works for sophisticated, multi-ASP diversified LPs -- and the product is institutional, not retail

**Variables:**
- Exit rate distribution (base case vs. stress case frequency)
- Correlation structure across rounds and ASPs
- Insurance pool funding rate (function of ASP fee revenue)
- LP position sizing and diversification constraints
- Number of ASPs available for cross-ASP diversification
- User behavior under stress (do users exit immediately or wait?)

**Dependencies:**
- P1 (Fee adequacy): Higher fees mean more margin to fund insurance or pay risk premiums
- P2 (LP yield): Exit risk is the primary driver of required yield premium
- P6 (Insurance circular dependency): If insurance is part of the solution, P6 is the follow-on problem
- P7 (LP diversification not protocol-enforced): Whether diversification is advisory or enforced affects risk profile
- P14 (ASP as borrower + co-signer): In Phase 1 escrow model, this is a different risk. In per-round integration, exit risk replaces it.

### Phase B: Research

**Research date:** April 2026

**Critical finding -- this is novel problem framing.** The Ark community has not publicly analyzed the scenario where an external LP (not the ASP itself) loses principal due to mass unilateral exits. All existing Ark liquidity analysis treats the ASP as its own capital provider. Second's liquidity simulations assume 100% cooperative refresh. The Ark whitepaper treats capital lockup as a cost-of-capital problem (fees compensate time-value), not a principal-loss problem. ArkFloat's P5 appears to be the first explicit framing of this risk.

**Lightning Pool comparison -- structurally different:** Lightning Pool has no inherent principal loss risk. The LP's capital is locked in a 2-of-2 channel; the LP can always force-close and recover their balance (minus on-chain fees and CSV delay). Worst case is opportunity cost, not principal loss. In Ark, unilateral exit by the user voids the forfeit -- the LP who funded the round loses the capital allocated to exited VTXOs. This is a structurally harder problem with no Lightning analogue.

**Closest public discussion:** instagibbs on Delving Bitcoin ("Ark as Channel Factory") identifies that "the ASP/LSP have to be the same identity or trust each other" to avoid abandonment exposure. This is the closest anyone has come to identifying P5, but framed as ASP-LSP trust, not external LP risk.
- [Delving Bitcoin thread](https://delvingbitcoin.org/t/ark-as-a-channel-factory-compressed-liquidity-management-for-improved-payment-feasibility/2179)

**DeFi mechanisms transferable to ArkFloat:**

**1. Aave Umbrella DAO-offset (strongest template).** Redesigned 2025 to break the circular dependency that plagued the old Safety Module. Key design:
- Stakers lock *the same asset being lent* (aUSDC covers USDC bad debt) -- eliminates cross-asset correlation
- First N units of bad debt absorbed by DAO treasury (funded from *accumulated historical revenue*, not current fees) before staker slashing begins
- Automated slashing -- no governance vote, threshold-based
- **Translation to ArkFloat:** ASP accumulates a first-loss reserve from historical round fees. Beyond the reserve, LP capital takes a pro-rata haircut. The reserve is funded from past operations, not from current-round fees -- this breaks the circular dependency identified in Direction 3.
- [Aave Umbrella docs](https://aave.com/docs/aave-v3/umbrella)

**2. Tranching (BarnBridge, Pareto/Morpho pattern).** Junior tranches absorb losses before senior tranches. Key insight: you don't need to prevent losses -- you need to structure who absorbs them and price accordingly. Junior LP positions absorb the first N% of exit losses at higher yield; senior LPs are protected up to that threshold at lower yield. Limitation: catastrophic correlated exits hit both tranches. But tranching makes the product viable for risk-averse capital (senior tranche) while rewarding risk-seeking capital (junior tranche).
- [Risk Tranching in DeFi](https://www.nadcab.com/blog/risk-tranching-in-defi-protocols)

**3. Compound reserve factor (simplest path).** A percentage of every round's fees accumulates into a reserve covering LP losses from exits. Non-circular. Builds over time. Doesn't cover catastrophic scenarios -- just enough to make expected-case losses acceptable, with actuarial caps beyond that.

**4. CDS-style external underwriting (Carapace/UNION model).** Separate pool of "exit risk underwriters" sell protection to LPs. LPs pay a premium per round; underwriters pay out if exit rate exceeds X%. Non-circular because underwriters are distinct from LPs and ASPs. Cleanest design but hardest cold-start problem (requires a market of exit-risk speculators).
- [Carapace CDS model](https://medium.com/union-finance-updates-ideas/unions-crypto-default-swap-7a6f7467b38a)

**5. EigenLayer attributable security pattern.** Operators (ASPs) and stakers (LPs) limit per-AVS (per-round) exposure with programmatic slashing. LP knowingly takes bounded risk in exchange for yield. The key design: slashing conditions are defined upfront and enforced automatically.

**Recommended synthesis for brainstorm Phase D:**

The combination of **fee-funded first-loss reserve** (Umbrella/Compound pattern) + **junior/senior LP tranching** addresses the circular dependency while accepting that catastrophic exits produce losses -- just structured and priced ones. This maps to a hybrid of Direction 3 + Direction 4 from the existing research:
- Direction 3's insurance pool is funded from *historical* revenue (not current), breaking circularity
- Direction 4's actuarial pricing applies above the first-loss buffer
- Tranching segments the LP market into risk appetites

**What remains unsolved:**
- Pricing the junior tranche requires exit rate distribution data that doesn't exist yet (no ASP has enough history)
- The first-loss reserve takes time to accumulate -- cold-start LPs have no buffer
- Catastrophic scenarios (70%+ exits) overwhelm any realistic reserve or tranche structure
- No mechanism prevents correlated exits -- they can only be priced and absorbed

**Sources:**
- [Lightning Pool Whitepaper](https://lightning.engineering/lightning-pool-whitepaper.pdf)
- [Second.tech forfeits](https://second.tech/docs/learn/forfeits)
- [Ark whitepaper](https://docs.arklabs.xyz/ark.pdf)
- [Aave Umbrella](https://aave.com/docs/aave-v3/umbrella)
- [Aave Umbrella governance](https://governance.aave.com/t/bgd-aave-safety-module-umbrella/18366)
- [BIS Working Paper 1062 -- Systemic Fragility](https://www.bis.org/publ/work1062.pdf)
- [Lido Insurance Fund](https://hackmd.io/@lido/HkeyM0a1s)

---

## P14: ASP as Borrower AND Co-Signer

### Phase A: Operationalize

**Problem statement:** In the per-round integration model, the ASP constructs the round (including LP-funded VTXOs) and co-signs forfeit transactions. The ASP is simultaneously the borrower (needing capital), the round constructor (controlling which VTXOs get LP funding), and the co-signer (whose cooperation is needed for cooperative VTXO spends). This creates a circular risk: the entity the LP depends on for repayment is also the entity that controls the repayment mechanism.

**What's broken:** The circular risk manifests in three ways:

1. **Round construction manipulation.** The ASP chooses which VTXOs in a round are LP-funded. A malicious ASP could assign LP funding to VTXOs held by sybil users who will immediately exit, voiding the forfeits. The LP has no way to verify that the VTXO holders are legitimate independent users.

2. **Forfeit construction integrity.** The LP must trust that the pre-signed forfeit transactions are correctly constructed and will actually be claimable. The LP can verify the Bitcoin script, but cannot verify that the ASP hasn't constructed the round in a way that makes the forfeits unclaimable (e.g., spending the connector output before the LP can claim).

3. **Cooperative path dependency.** For cooperative VTXO operations (refreshes, OOR payments), the ASP must co-sign. An ASP in distress could delay or refuse cooperation, forcing users into unilateral exits -- which is exactly the scenario that hurts the LP.

**Important distinction:** This problem applies differently to the two design models:
- **Phase 1 (standalone escrow):** The LP lends via a separate 2-of-2 multisig. The ASP is the borrower but the escrow is independent of Ark rounds. The LP claims via timeout path regardless of ASP cooperation. Circular risk is limited to ASP insolvency (can't repay), which is standard lending risk mitigated by the escrow collateral.
- **Per-round integration:** The LP's capital IS in the round. The ASP constructs the round. Circular risk is structural and harder to mitigate.

**Assumptions this rests on:**
1. The ASP is honest-but-rational (optimizes for its own interest within protocol constraints)
2. A distressed ASP will prioritize its own survival over LP interests
3. The LP cannot independently verify the legitimacy of VTXO holders in a round
4. Connector outputs (required for forfeit claims) are under ASP control until spent

**What "solved" looks like:**
- A verification mechanism that lets LPs independently confirm round construction integrity, OR
- Structural separation between borrower and round constructor roles (third-party verification), OR
- A proof that the ASP's incentives align with the LP's in all realistic scenarios (including distress), OR
- An honest assessment that Phase 1 escrow is the only model where circular risk is adequately mitigated, and per-round integration requires additional trust assumptions

**Variables:**
- ASP reputation/track record (trust builds over time)
- Round construction transparency (can the LP audit the round before committing?)
- Connector output lifecycle (when can the ASP spend connectors vs. when does the LP need them?)
- Proof of reserves (does the LP have visibility into the ASP's overall health?)
- V-PACK standard (stateless VTXO verification, announced March 2026 -- does this help?)

**Dependencies:**
- P5 (Unilateral exit risk): The exit risk that circular risk amplifies
- P11 (hArk forfeit compatibility): If hArk forfeits can't be redirected to LP addresses, per-round integration may not be technically feasible in Bark
- P12 (Forfeit verification refactor): The scope of changes needed to support LP-addressed forfeits
- P13 (Fixed VTXO script template): Whether third-party claims can be script-enforced
- P17 (Proof of reserves): LP's ability to evaluate ASP health before lending

### Phase B: Research

**Research date:** April 2026

**Existing prior art directly on point:**

1. **arkd Issue #197** (the issue ArkFloat builds on): Already proposes that external liquidity providers "verify the validity of the forfeit transactions and the poolTx" before providing signatures. The LP acts as a round co-signer -- verifying the round before committing capital. This is the closest existing mechanism to what ArkFloat needs. Gap: #197 does not address how the LP detects sybil VTXOs.
   - [arkade-os/arkd#197](https://github.com/arkade-os/arkd/issues/197)

2. **arkd Issue #204** -- Double-spend prevention bonds: ASPs lock funds in a bond UTXO (proposed on Liquid) that can be burned if double-spending is detected by any third party. Addresses one failure mode but NOT round construction integrity.
   - [arkade-os/arkd#204](https://github.com/arkade-os/arkd/issues/204)

3. **V-PACK standard** (Bitcoin Optech #395, March 2026): Library for auditing and independently verifying Ark VTXOs. Verifies individual VTXO ownership paths via Merkle path reconstruction. **Critical limitation:** V-PACK verifies per-VTXO validity, NOT round-level integrity. Cannot confirm that all VTXOs sum correctly, that no sybil outputs exist, or that connector outputs are properly constructed. Developer acknowledged "path exclusivity" gap.
   - [libvpack-rs](https://github.com/jgmcalpine/libvpack-rs)

4. **CTV/CSFS evolution** (Delving Bitcoin): CTV commits tree structure cryptographically -- users can verify inclusion via commitment hash. But CTV makes the commitment *binding once published*, not the construction process *auditable*. The ASP still decides what goes into the tree.
   - [Evolving Ark with CTV and CSFS](https://delvingbitcoin.org/t/evolving-the-ark-protocol-using-ctv-and-csfs/1602)

**Structural analogies from other systems:**

- **Lightning watchtowers:** Third parties monitor the chain and broadcast justice transactions on behalf of offline users. Relevant pattern: an LP-operated watchtower could monitor for ASP actions that invalidate forfeit claims (spending connector outputs prematurely). The watchtower pattern works for *detection after the fact* but not *prevention during round construction*.

- **Lido V3 stVaults:** Node operators must repay borrowed stETH + fees before exiting a vault. A "repayment-before-exit" pattern. Relevant: could ArkFloat require the ASP to satisfy LP claims before accessing the next round's capital? This creates a sequential dependency rather than a trust assumption.

- **Beanstalk attack ($182M, 2022):** Canonical example of "borrower controls the governance mechanism." Attacker flash-borrowed governance tokens, passed a malicious proposal, drained the protocol in one transaction. Defense patterns: time delays, multi-block confirmation, flash loan guards. Lesson: any system where the borrower controls the enforcement mechanism is vulnerable to atomic attacks.

- **MakerDAO Black Thursday (2020):** Enforcement mechanisms that depend on the same infrastructure under stress will fail when you need them most. Directly relevant to the "ASP in distress refuses cooperation" scenario.

**The fundamental gap (confirmed by research):**

No existing mechanism lets an LP verify that the set of VTXOs in a round is legitimate (not sybil) without either:
- (a) Trusting the ASP's attestation of user demand, OR
- (b) Directly observing user VTXO requests through an ASP-independent channel

V-PACK gets per-VTXO verification but not round-level integrity. CTV gets commitment binding but not input validation. The missing piece is an authenticated, ASP-independent channel through which the LP can observe or verify the set of VTXO requests that should be in a given round.

**Five candidate mechanisms identified (ranked by feasibility):**

| Mechanism | What it solves | What it doesn't | Feasibility |
|---|---|---|---|
| LP as round co-signer (from #197) | LP verifies poolTx + forfeits before committing | Cannot detect sybil VTXOs | High -- already proposed |
| CTV commitment + LP verification node | Deterministic tree from known inputs; ASP cannot deviate | LP must learn VTXO requests independently of ASP | Medium -- requires CTV activation |
| Bonded ASP (from #204) | Makes misbehavior economically irrational | Does not prevent it; requires dispute resolution | Medium -- bond design is known |
| LP watchtower for connector outputs | Detects premature connector spending | Only detects after-the-fact; no prevention | High -- standard watchtower pattern |
| Federated round construction | Eliminates single-point trust | Reduces capital efficiency; coordination overhead | Low -- no existing design |

**Assessment for Phase A's "solved" criteria:**
- Phase 1 escrow model adequately mitigates circular risk (LP claims via timeout path, independent of ASP cooperation). This is confirmed by both the research and the viability assessment.
- Per-round integration requires the LP to trust the ASP on round construction integrity. The best available mitigation is LP-as-co-signer (#197 pattern) + bonded ASP + watchtower -- a layered defense, not a single solution. Sybil detection remains an open problem.
- The honest conclusion may be that per-round integration carries *reducible but not eliminable* trust in the ASP, and the product should be marketed accordingly (the LP trusts the ASP's round construction, secured by economic bonds and watchtower monitoring, not by pure script enforcement).

**Sources:**
- [arkade-os/arkd#197](https://github.com/arkade-os/arkd/issues/197)
- [arkade-os/arkd#204](https://github.com/arkade-os/arkd/issues/204)
- [V-PACK -- Bitcoin Optech #395](https://bitcoinops.org/en/newsletters/2026/03/06/)
- [CTV/CSFS on Delving Bitcoin](https://delvingbitcoin.org/t/evolving-the-ark-protocol-using-ctv-and-csfs/1602)
- [Lido V3 Whitepaper](https://hackmd.io/@lido/v3-whitepaper)
- [BIS Working Paper 565 -- Collateral Trap](https://www.bis.org/publ/work565.pdf)

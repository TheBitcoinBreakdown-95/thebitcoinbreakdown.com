# Interbank-Style Liquidity Markets for Ark Service Providers

*Research note, March 2026. Part of the Ark ASP liquidity research series.*

---

## 1. Traditional Interbank Lending: How It Works

### The Federal Funds Market

The federal funds market is where banks with excess reserves lend overnight to banks with reserve deficits. The price of this market -- the federal funds rate -- is the single most important interest rate in the U.S. financial system. It anchors the yield curve, prices trillions in floating-rate contracts, and serves as the Federal Reserve's primary policy instrument.

The mechanics are simple. Banks are required to hold reserves at the Federal Reserve. On any given day, some banks have more reserves than required (from net deposit inflows, maturing assets, or reduced lending) and some have less (from net withdrawals, new loans, or settlement obligations). Rather than each bank holding enormous reserve buffers to absorb daily fluctuations, they lend surplus reserves to each other. The bank with excess reserves earns interest on capital that would otherwise sit idle at the Fed. The bank with a deficit avoids the penalty rate of the Fed's discount window. Both sides benefit. ([Federal Reserve History: Federal Funds Rate](https://www.federalreservehistory.org/essays/fed-funds-rate))

Key properties of the fed funds market:

- **Very short term.** The dominant tenor is overnight. Term fed funds (1-week, 2-week) exist but are a small fraction of volume.
- **Unsecured.** Banks lend to each other based on creditworthiness and reputation. There is no collateral. This is a trust-based market among regulated institutions.
- **Rate set by supply and demand.** When reserves are abundant, the rate falls. When reserves are scarce, it rises. The Fed manipulates this by adding or draining reserves through open market operations.
- **Large participant base.** Thousands of banks participate, from the largest G-SIBs to small community banks. The market is deep and liquid precisely because the participant base is broad.

### Historical Development: It Took Decades

The fed funds market did not spring into existence fully formed. Understanding its development timeline matters for assessing the realism of a similar market for Ark ASPs.

The market originated in the 1920s as a mechanism to arbitrage differences in discount window rates between Federal Reserve districts. Daily trading volume rarely exceeded $20 million in 1921, grew to $40-80 million by 1925, and reached $250 million at times by the late 1920s. By 1925, banks outside New York were lending fed funds locally, and inter-district lending was common by decade's end. Daily rate quotes were first published in April 1928 in the New York Herald-Tribune. ([St. Louis Fed: A New Daily Federal Funds Rate Series and History of the Federal Funds Market, 1928-54](https://www.stlouisfed.org/publications/review/2021/01/14/a-new-daily-federal-funds-rate-series-and-history-of-the-federal-funds-market-1928-54))

Then the market went dormant. From the late 1930s through the 1940s, wartime monetary policy flooded the system with reserves, eliminating the need for interbank lending. The market was "moribund" for roughly 15 years. It re-emerged in the 1950s only after the Federal Reserve tightened liquidity conditions and reserves were reduced from levels considered "super-abundant." By the end of the 1950s, the market had attracted new participants and financial innovations that bolstered its size, liquidity, and stability. ([Federal Reserve: The Re-emergence of the Federal Funds Market in the 1950s](https://www.federalreserve.gov/econres/notes/feds-notes/re-emergence-of-the-federal-funds-market-in-the-1950s-20190322.html))

The pattern: the market required (a) a meaningful number of participants with daily fluctuations in reserves, (b) a reason to lend rather than hoard (scarcity, not abundance), and (c) sufficient trust between participants to lend unsecured. When any of these conditions was absent, the market withered.

### The Parallel to ASPs

ASPs have rolling fluctuations in available BTC. Trees expire on different schedules, rounds happen at different frequencies, and demand for new rounds varies by time of day and week. An ASP whose trees just expired holds surplus BTC. An ASP facing a large onboarding round needs BTC urgently. Rather than each ASP maintaining enormous buffers to handle peak demand, they could lend surplus to each other.

The structural parallel is real. The question is whether the preconditions exist.

### Critical Differences

| Property | Fed Funds Market | Proposed ASP Market |
|----------|-----------------|-------------------|
| Security model | Unsecured (trust + regulation) | Secured via on-chain escrow (trust-minimized) |
| Tenor | Overnight (dominant) | 1-14 days (matching VTXO expiry cycles) |
| Participant count | Thousands of banks | 2 ASPs today (Ark Labs/Arkade, Second/Bark) |
| Rate setting | Supply/demand of reserves, Fed manipulation | No central bank, no reserve requirement |
| Settlement | Fedwire (instant, irrevocable) | Lightning or on-chain Bitcoin |
| Regulatory framework | Dense (Fed supervision, capital requirements) | None |
| Market maturity | ~100 years of development | Does not yet exist |

The most important difference: the fed funds market is unsecured because banks are regulated, examined, and backed by deposit insurance and Fed lending facilities. ASPs have none of this infrastructure. The proposed ASP market compensates by being *secured* -- on-chain escrow replaces institutional trust. This is a fundamentally different trust model, and it comes with different costs (on-chain fees, escrow setup complexity, collateral requirements).

---

## 2. The Three Liquidity Sources

### Source A: Inter-ASP Lending (The Interbank Analogue)

**Who they are.** Ark Service Providers -- entities running Ark server software (Arkade from Ark Labs, Bark from Second) that process rounds, manage VTXO trees, and lock BTC on behalf of users.

**What they want.** Short-term BTC to bridge timing mismatches. ASP A has 50 BTC returning from expiring trees on Tuesday; ASP B needs 30 BTC for a large onboarding round on Monday. Without a lending market, ASP B must either reject the onboarding demand or maintain a buffer large enough to cover any peak.

**Term.** 1-7 days. This is bridging finance -- the ASP knows when its own trees expire and can repay from those proceeds. The short term keeps risk minimal and matches the operational rhythm of Ark rounds.

**Rate.** Should be the lowest of the three sources. Both parties understand Ark mechanics intimately, the term is short, and the risk is well-characterized. Estimated range: 1-3% annualized, competitive with or below Lightning routing yields.

**Risk tolerance.** Moderate. ASPs understand the protocol-level risks. The primary risk is counterparty default -- the borrowing ASP fails to repay because its expected tree expirations were disrupted (e.g., mass unilateral exits by users that delay or reduce the ASP's reclamation). This risk is mitigable through over-collateralization.

**Settlement mechanics.** Both ASPs operate Lightning nodes (ASPs serve as Lightning gateways for Ark-to-Lightning payments, per [Ark Labs: Lightning Integration](https://docs.arklabs.xyz/ark/)). Lightning settlement is natural for amounts within channel capacity -- fast, cheap, no additional on-chain footprint. For larger amounts exceeding channel capacity, on-chain settlement with escrow is necessary.

**Trust model.** The ASP community is tiny. As of March 2026, there are two implementations with mainnet presence:

1. **Ark Labs / Arkade.** Launched public beta in October 2025 after two years of development. Backed by Draper Associates, Axiom, Fulgur Ventures. Integration partners include Breez, BlueWallet, BTCPayServer, and BullBitcoin. ([The Block: Ark Labs launches Arkade public beta](https://www.theblock.co/post/375271/ark-labs-arkade-public-beta-layer-2-bitcoin))

2. **Second / Bark.** Demonstrated the first Ark transactions on Bitcoin mainnet. Operates the Bark command-line wallet and ASP implementation. Produced extensive research on Ark liquidity economics. ([Second: Demoing the first Ark transactions on bitcoin mainnet](https://blog.second.tech/demoing-the-first-ark-transactions-on-bitcoin-mainnet/))

With two participants, there is no market. There is a bilateral relationship. ASP A and ASP B can negotiate directly -- "I need 30 BTC for 5 days, my trees expire Thursday, I'll pay you X basis points." No protocol, no order book, no auction. Just two operators on a Signal group.

**How many ASPs are needed?** A functional lending market requires at least 3-5 ASPs with differentiated round schedules and throughput patterns. Below that, bilateral negotiation is more efficient than any market mechanism. The fed funds market only became meaningful when dozens of banks in different cities had uncorrelated reserve fluctuations. For Ark, the question is when (not whether) additional ASPs launch. The protocol is open-source and the specification is public. But running an ASP requires significant capital (the problem-spec estimates $8-40M in locked BTC for a medium ASP), operational expertise, and tolerance for protocol-level risk. The barrier to entry is high.

**Comparison to Lightning channel rebalancing.** Lightning routing nodes already engage in a form of inter-operator liquidity management: circular rebalancing (paying yourself through a route to shift channel balances), submarine swaps (exchanging on-chain BTC for Lightning BTC), and peer-to-peer liquidity swaps. The inter-ASP lending concept is structurally similar -- BTC moving between L2 infrastructure operators to optimize capital deployment. The difference is that Lightning rebalancing is intra-protocol (within Lightning), while ASP lending would be cross-protocol or at least cross-implementation.

---

### Source B: Lightning Liquidity Providers

**Who they are.** Lightning routing nodes with idle channel capacity -- channels that are open but not routing significant payment volume. This includes professional routing nodes (ACINQ, River, Voltage-managed nodes), semi-professional node operators, and liquidity marketplaces participants (Amboss Magma sellers, Lightning Pool providers).

**What they want.** Better yield on deployed BTC. A Lightning node operator has BTC locked in channels. If those channels are not routing enough to justify the capital, the operator faces a choice: close the channel and redeploy, or find a higher-yield use for the capital.

**Term.** 14-28 days. This matches two existing conventions: (a) VTXO expiry periods in Ark (the borrowing ASP can guarantee repayment from tree expiration proceeds), and (b) Lightning channel lease terms. Lightning Pool leases are denominated in blocks -- the standard lease is 2016 blocks, approximately 2 weeks. Amboss Magma leases vary but commonly span 2-4 weeks. Lightning LPs are already comfortable locking BTC for these durations. ([Lightning Pool whitepaper](https://lightning.engineering/lightning-pool-whitepaper.pdf); [Amboss Magma documentation](https://old-docs.amboss.tech/docs/magma/intro))

**Rate.** Must exceed the LP's opportunity cost -- what they would earn routing Lightning payments or leasing channels. Current benchmarks (as of early 2026):

| Benchmark | Rate | Source |
|-----------|------|--------|
| Amboss Magma median lease rate | ~2.6% APR | [Second: Diving deeper into Lightning liquidity: Amboss Magma](https://blog.second.tech/diving-deeper-into-lightning-liquidity-amboss-magma-2/) |
| LINER (Voltage Lightning Network Earning Rate) | 1.2-1.7% network average | [Voltage: Where Does the Yield Come From?](https://www.voltage.cloud/blog/where-does-lightning-network-yield-come-from) |
| Block/Cash App aggressive routing | 9.7% annualized | [Atlas21](https://atlas21.com/lightning-routing-yields-10-annually-blocks-announcement/) |
| LQWD (publicly reported) | 24% annualized | Company filings; outlier driven by proprietary flow |
| Mid-size routing nodes (typical) | 1.5-2.0% annualized | [Voltage LINER data](https://www.voltage.cloud/blog/where-does-lightning-network-yield-come-from) |

The Block/Cash App and LQWD figures are outliers driven by captive payment flow (Cash App users) and cannot be replicated by generic routing nodes. The realistic comparison is the 1.5-2.6% range. An ASP lending rate of 3-4% would represent a meaningful premium over median Lightning yields while remaining affordable for the ASP (whose gross ROI on locked capital is 3-6%, per the [unit economics analysis](unit-economics.md)).

**Risk tolerance.** Moderate-to-high. Lightning LPs are already comfortable with BTC locked in L2 infrastructure, force-close risk, channel partner default, and the operational complexity of node management. Lending to an ASP is structurally similar to opening a channel -- BTC is locked for a fixed term with a known counterparty. The risk profile is arguably better: an ASP loan with on-chain escrow collateral is more predictable than a channel that can be force-closed by a counterparty at any time.

**Settlement mechanics.** Lightning is the natural settlement rail. Both the LP and the ASP are Lightning nodes. The LP routes BTC to the ASP's Lightning node; the ASP repays via Lightning at maturity. For amounts exceeding channel capacity, on-chain settlement or submarine swaps bridge the gap.

**Why this is the most natural bridge.** Lightning and Ark are both Bitcoin L2 protocols competing for the same underlying scarce resource: BTC liquidity. Capital flows between them represent an efficiency gain for the entire Bitcoin L2 ecosystem. A Lightning node with 10 BTC in underperforming channels could close those channels, lend 5 BTC to an ASP for 28 days at 3.5%, and earn more than it would routing payments. The ASP gets liquidity; the LP gets yield; the Bitcoin ecosystem gets better capital allocation. This is not theoretical -- it is exactly the logic that drives Lightning Pool and Magma today, applied to a new counterparty type.

---

### Source C: HODLers and Passive BTC Holders

**Who they are.** Individuals and entities holding BTC in cold storage, exchange balances, or custodial accounts with no active yield strategy. This ranges from retail holders with 0.1 BTC on Coinbase to corporate treasuries (MicroStrategy, Block, Tesla) holding thousands of BTC. The common thread: their BTC earns 0% yield.

**What they want.** Yield with minimal risk. The bar is low -- anything above 0% is an improvement over holding -- but the trust bar is extremely high. This cohort was traumatized by the 2022 collapse of centralized lending platforms.

**The BlockFi/Celsius problem.** Between 2020-2022, platforms including BlockFi, Celsius Network, Voyager Digital, and Genesis promised 5-8% APY on BTC deposits. Users transferred BTC to these platforms, which lent it out -- often as undercollateralized loans to hedge funds (notably Three Arrows Capital, which received ~$2.4B from Genesis alone). When BTC prices fell and 3AC defaulted, the platforms could not return user deposits. Billions were lost. The root cause in every case was custodial risk: users gave up control of their BTC, the platform rehypothecated it, and the collateral chains failed. ([Chicago Fed: A Retrospective on the Crypto Runs of 2022](https://www.chicagofed.org/publications/chicago-fed-letter/2023/479); [CoinTelegraph: Bitcoin loans are back](https://cointelegraph.com/news/bitcoin-loans-back-rewriting-book-celsius-burned))

Any pitch to HODLers that sounds like "earn yield on your BTC" must answer: how is this different from what BlockFi promised?

**The answer: on-chain escrow eliminates custodial risk.** The HODLer's BTC is locked in an on-chain escrow -- a timelocked multisig or a Discreet Log Contract (DLC) -- not transferred to the ASP. The ASP cannot rehypothecate it. If the ASP defaults, the HODLer's escrow claim activates automatically at the timelock expiry. No bankruptcy proceedings, no creditor queue, no trust required.

This is the same model being pioneered by Lygos Finance (which acquired Atomic Finance to build DLC-powered non-custodial Bitcoin lending) and Hodl Hodl (which has operated non-custodial Bitcoin-collateralized loans since 2018 through multiple bear markets). The critical distinction: the HODLer's private keys never leave their control. The escrow is enforced by Bitcoin script, not by corporate policy. ([CoinDesk: Lygos Aims to Banish Ghosts of Past With Non-Custodial Model](https://www.coindesk.com/business/2025/08/27/lygos-aims-to-banish-ghosts-of-crypto-lending-collapse-with-non-custodial-bitcoin-model); [Blockspace: Lygos Finance acquires Atomic Finance](https://blockspace.media/insight/lygos-finance-acquires-atomic-finance-to-launch-non-custodial-dlc-powered-bitcoin-loans/))

**Term.** 14-28 days, fixed. Matching the VTXO expiry cycle. The fixed term is important for HODLers -- they know exactly when their BTC returns. No rolling, no open-ended lock.

**Rate.** Must exceed the risk-adjusted alternatives:

| Alternative | Yield | Risk | Notes |
|-------------|-------|------|-------|
| Holding (cold storage) | 0% | Zero (self-custody) | The default |
| Ledn (< 0.5 BTC) | 5.25% | Custodial, platform solvency | Note: Ledn discontinued interest products in late 2025 to eliminate credit risk. ([Ledn](https://www.ledn.io)) |
| Ledn (institutional tier) | ~2% | Custodial | Same discontinuation |
| Babylon BTC staking | ~1% APR on BTC | Protocol, slashing, opportunity | $5.3B+ TVL, mainnet since April 2025. ([Babylon Labs](https://babylonlabs.io/); [CoinLaw: Bitcoin Staking Statistics](https://coinlaw.io/bitcoin-staking-statistics/)) |
| DeFi lending (wBTC on Aave/Compound) | 1-4% variable | Smart contract, bridge, depegging | Requires wrapping BTC |

The competitive landscape has thinned since 2022. Most CeFi yield products are gone. Babylon offers ~1% on native BTC. DeFi requires bridging to Ethereum (a trust and complexity barrier). An ASP lending rate of 2-3% with on-chain escrow security would be competitive against virtually all alternatives. The bar is genuinely low if the security model is sound.

**Settlement mechanics.** On-chain. HODLers may not run Lightning nodes. The escrow setup is an on-chain transaction: HODLer and ASP fund a 2-of-2 multisig with timelock conditions. At maturity, the ASP returns the principal plus interest. If the ASP defaults, the timelock expires and the HODLer claims the ASP's collateral. Interest payments could be settled over Lightning if the HODLer has a node, but the principal legs are on-chain.

**Trust model.** Trust-minimized via on-chain escrow. The HODLer does not need to evaluate the ASP's balance sheet, audit its operations, or trust its management. The escrow enforces the contract. The HODLer's risk is limited to: (a) Bitcoin script bugs (extremely low probability for standard constructions), (b) the ASP's collateral being insufficient (requires over-collateralization), and (c) on-chain fee spikes making escrow claims expensive.

**Challenge: reaching this cohort.** HODLers are the largest BTC capital pool but the hardest to activate. Cold storage holders are by definition not engaging with DeFi, L2 protocols, or yield products. The BlockFi/Celsius trauma created deep skepticism toward any "yield on BTC" proposition. Marketing "non-custodial yield via on-chain escrow" requires Bitcoin-native credibility and education. This is a long-term source, not a launch source.

---

## 3. The Unilateral Exit Constraint

This is the engineering bedrock of the entire market design.

### The Sacrosanct Principle

Once BTC is committed to a VTXO tree, it cannot be clawed back by any lender, under any circumstances. The VTXO script is fixed: `(user + ASP) cooperative OR (user alone after timeout)`. There is no third spending path. No lender claim. No emergency override. The user's unilateral exit right is absolute and unconditional. ([Ark Protocol: VTXOs](https://ark-protocol.org/intro/vtxos/index.html))

This is not a design choice that can be revisited. It is the reason Ark exists. Without unilateral exit, Ark reduces to a custodial service -- a database with extra steps. The entire protocol's value proposition rests on the guarantee that no counterparty, including the ASP, can prevent a user from exiting with their BTC.

### What This Means for Lenders

The lender's BTC, once deployed by the ASP into a round, is irrecoverable by the lender for the duration of the VTXO tree's lifetime (up to 28 days). The lender has no on-chain claim against the tree-committed BTC. The tree's script does not recognize the lender's existence.

Therefore: **the lender's security must come from assets SEPARATE from the tree-committed BTC.**

### What Can Serve as Collateral?

1. **ASP's on-chain reserves (BTC not yet committed to trees).** The most straightforward collateral. The ASP locks a portion of its uncommitted BTC in an escrow before borrowing. If the ASP defaults, the lender claims the escrow. Problem: if the ASP is borrowing precisely because it lacks uncommitted BTC, what is it pledging?

2. **ASP's claims on expiring trees (BTC returning in X days).** The ASP knows that N BTC will become available when trees expire on specific dates. These are forward claims -- not current assets. A lender accepting forward claims as collateral is taking a timing risk: if users execute mass unilateral exits from those trees, the ASP's reclamation is delayed or reduced. Forward claims are weaker than current assets.

3. **ASP's Lightning channel balances.** An ASP operating Lightning channels for gateway functionality has BTC locked in channels. These balances could theoretically be pledged as collateral, but they are operationally needed for Lightning routing. Force-closing channels to honor a collateral claim is destructive to the ASP's business.

4. **Other ASPs' guarantees (cross-ASP credit).** ASP B guarantees ASP A's loan. This is unsecured credit extended by one ASP to another -- exactly the fed funds model. It works at scale with many participants but is fragile with only 2-3 ASPs.

### The Circular Risk

The central use case -- an ASP borrowing BTC to fund rounds -- creates an inherent tension:

1. ASP borrows 30 BTC from a lender.
2. ASP commits 30 BTC to a VTXO tree in the next round.
3. The 30 BTC is now locked for up to 28 days with no lender claim.
4. The lender's security depends on the ASP's *other* assets.

If the ASP has borrowed against all its available assets, it has no free collateral. The question is whether this is a manageable leverage constraint or a structural flaw.

### Preventing Over-Leverage

The answer is a maximum borrowing ratio: the ASP can borrow up to X% of its total balance sheet, where the balance sheet includes uncommitted reserves, near-term tree expiry claims, and Lightning channel balances. For example:

- **Conservative: 30% borrowing limit.** An ASP with a 100 BTC balance sheet (across all asset types) can borrow up to 30 BTC. The remaining 70 BTC serves as the collateral base.
- **Moderate: 50% borrowing limit.** Allows more leverage but with thinner collateral margins.
- **Aggressive: 70%+.** Approaches the territory where a single bad round (mass unilateral exits, fee spike) could leave the ASP unable to repay.

**Who enforces this?** In tradfi, regulators enforce capital adequacy ratios (Basel III leverage ratio, LCR, etc.). In the ASP market, enforcement must be market-based:

- **Lenders enforce it by requiring proof of reserves.** Before lending, the lender demands an attestation of the ASP's balance sheet -- uncommitted BTC, tree expiry schedule, Lightning channel balances. The ASP either provides this transparently or does not get the loan.
- **On-chain verifiability helps.** Some of the ASP's balance sheet is on-chain and auditable (UTXOs, channel states). Forward claims on expiring trees are harder to verify externally but can be proven by sharing the round transaction IDs.
- **Reputation in a small community.** With 2-5 ASPs, reputation is powerful. An ASP that over-leverages and defaults will not borrow again.

### Is This Sound?

Conditionally. The model works if:

1. ASPs maintain meaningful reserves beyond what they borrow (enforced by lender due diligence, not protocol).
2. Borrowing terms are short enough that tree expiry proceeds cover repayment (1-7 day inter-ASP loans are safest).
3. Over-collateralization ratios account for the forward-claim weakness (e.g., 120-150% collateral-to-loan ratio).
4. The market starts with conservative leverage limits and loosens them only as operational history builds trust.

It does not work if ASPs treat borrowed BTC as free leverage to grow beyond their capital base. That path leads to the same outcome as 2022 CeFi: promises backed by insufficient reserves.

---

## 4. Rate Discovery: How Would Pricing Work?

### Stage 1: Bilateral Negotiation (Now -- 5 ASPs)

With 2-3 ASPs, rate discovery is a phone call. ASP A messages ASP B: "I need 50 BTC for 3 days. My trees expire Thursday, paying you back from those proceeds. What's your rate?" They agree on a rate, settle over Lightning, and that's it. No protocol, no infrastructure, no overhead.

This is how the fed funds market started in the 1920s. New York City banks called each other. The rate was whatever two parties agreed on. The New York Herald-Tribune started publishing the rate in 1928 only because the market had grown large enough to be newsworthy.

Bilateral negotiation is the right model when participants know each other, volumes are small, and the cost of building market infrastructure exceeds the efficiency gains.

### Stage 2: Bulletin Board / Order Book (5-15 ASPs)

As the participant base grows, bilateral negotiation becomes inefficient. A simple bulletin board -- ASPs and LPs post lending offers (amount, term, rate) and borrowing requests -- enables many-to-many matching without building complex infrastructure. This can be as simple as a shared dashboard or a Lightning-native messaging protocol.

The bulletin board reveals price information: market participants can see the distribution of offered rates, which creates convergence toward a market-clearing rate. It does not force price uniformity (each deal is still bilaterally agreed) but it reduces information asymmetry.

### Stage 3: Batch Auction (Lightning Pool Model)

Lightning Pool demonstrates how a batch auction works for Bitcoin L2 liquidity:

- Every 10 minutes, a sealed-bid auction collects all outstanding bids (borrowers willing to pay up to rate X) and asks (lenders willing to accept down to rate Y).
- If supply and demand curves cross, the auction clears at a single uniform price -- the rate at which the most capital is matched.
- All matched orders execute in a single on-chain transaction, minimizing fees.
- The uniform clearing price means all participants get the same rate: lenders who asked for less receive the clearing rate (better than requested); borrowers who bid more pay the clearing rate (less than offered).

This is the same mechanism the U.S. Treasury uses for bond auctions. It promotes fairness and incentivizes truthful bidding -- there is no advantage to strategic underbidding or overbidding because the clearing price is set by the market, not by individual offers. ([Lightning Pool Whitepaper](https://lightning.engineering/lightning-pool-whitepaper.pdf); [Lightning Labs: Pool Technical Deep-Dive](https://lightning.engineering/posts/2020-11-02-pool-deep-dive/); [Pool Batch Execution docs](https://docs.lightning.engineering/lightning-network-tools/pool/batch_execution))

For an ASP liquidity market, a batch auction makes sense only when there are enough participants to generate meaningful supply/demand curves in each auction window. With fewer than 10 participants, most auction windows would have 0-1 orders on each side.

### Stage 4: Automated Rate (Aave Model)

A lending pool with an automated rate function: rate = f(utilization). When the pool is mostly idle, rates are low. As utilization increases, rates rise on a curve (typically convex -- accelerating as utilization approaches 100%). This model requires:

- A pooled capital structure (multiple lenders deposit into a shared pool).
- A smart contract or equivalent enforcing the rate function. On Bitcoin, this would require either a federated sidechain, a covenant-enabled script, or a trusted coordinator.
- Sufficient pool size to absorb individual loan demand without extreme rate volatility.

This is the most capital-efficient model at scale but the most infrastructure-heavy to build. Premature for the current stage.

### The Natural Rate Band

The ASP lending rate should float within a band defined by:

- **Floor: ~1.5-2.5% (Lightning routing yield).** Below this, lenders earn more routing Lightning payments. Capital flows out of ASP lending into Lightning.
- **Ceiling: ~3-6% (ASP gross ROI on locked capital).** Above this, borrowing destroys the ASP's unit economics. At a 0.3% blended fee and 2.0x lockup multiplier (V2, 50% spend), the ASP's gross ROI is ~6%. Borrowing costs above this make the ASP's operations unprofitable. At the more conservative V1 multiplier, the ceiling drops to ~3%. ([Unit economics analysis](unit-economics.md))
- **Expected clearing range: 2-4%.** Above Lightning yield (attracting lenders) and below ASP ROI (sustainable for borrowers). The exact rate depends on supply/demand balance, which fluctuates with ASP growth rates, Lightning network conditions, and BTC market volatility.

---

## 5. Settlement Rails

### Lightning Settlement

**Best for:** Inter-ASP short-term lending, Lightning LP lending. Amounts within channel capacity (typically up to a few BTC per channel, more with wumbo channels).

**Mechanics:** The lender routes a payment to the borrower's Lightning node. At maturity, the borrower routes the principal plus interest back. Standard Lightning invoices with payment hashes provide atomic settlement and proof of payment.

**Advantages:** Speed (seconds), low cost (few sats in routing fees), no on-chain footprint, both parties already have Lightning infrastructure.

**Limitations:** Channel capacity constrains maximum settlement size. A 10 BTC loan may require multi-path payments across several channels, which can fail if routing liquidity is insufficient. No built-in escrow -- the Lightning payment is fire-and-forget. Collateral arrangements require a separate mechanism.

### On-Chain Settlement

**Best for:** HODLer lending (escrow setup), larger amounts exceeding Lightning channel capacity, any transaction requiring verifiable collateral lockup.

**Mechanics:** Standard Bitcoin transactions. Escrow uses 2-of-2 multisig with timelock conditions (similar to Lightning channel funding transactions, but with different spending paths). The escrow transaction is broadcast, confirmed, and visible on-chain. At maturity, a cooperative close returns BTC to the lender. On default, the lender waits for the timelock and claims collateral.

**Advantages:** Verifiable, trust-minimized, no channel capacity constraints, works for any participant regardless of Lightning node status.

**Limitations:** On-chain fees (variable, potentially significant during fee spikes), confirmation time (10-60 minutes for reasonable confidence), requires UTXO management.

### Hybrid Settlement

The pragmatic approach for most transactions:

1. **Escrow setup: on-chain.** The borrower and lender fund a timelocked multisig. This is the trust anchor -- it secures the entire loan.
2. **Principal transfer: Lightning or on-chain** depending on amount and participant capabilities.
3. **Interest payments: Lightning.** Small, frequent payments route easily over Lightning.
4. **Principal return: on-chain** (cooperative close of the escrow) or Lightning if within capacity.

### Can Ark Itself Serve as a Settlement Rail?

Could an ASP borrow BTC via Ark's out-of-round (OOR) payment mechanism? The borrowed BTC would arrive as a VTXO. But the ASP needs raw BTC -- an on-chain UTXO -- to fund the commitment transaction for a new round. A VTXO is a claim within an existing tree, not a UTXO the ASP can use to build a new tree.

The ASP would need to exit the VTXO (unilateral exit: slow, expensive; cooperative exit: requires another ASP's signature) to convert it into an on-chain UTXO before it could use the borrowed capital. This adds cost, delay, and complexity that defeats the purpose.

**Verdict: Ark-native settlement does not work for the borrowing leg.** The ASP needs on-chain BTC or Lightning BTC that can be swapped to on-chain. Ark VTXOs are the wrong form factor.

---

## 6. Market Size and Viability

### Participant Threshold

**Minimum for inter-ASP market: 3-5 ASPs.** With 2 ASPs, there is one possible lending relationship. With 5, there are 10 possible bilateral pairs. At 10 ASPs, 45 pairs. The market becomes meaningfully liquid when at least 3-5 ASPs have uncorrelated liquidity needs -- different round schedules, different user bases, different peak demand times.

**Minimum for multi-source market (including LPs and HODLers): 5-10 ASPs + 20-50 LPs.** The LP pool needs to be large enough that any single ASP can borrow from multiple LPs simultaneously (diversification) and that LP capital is not concentrated in one or two large providers.

### Current ASP Count

As of March 2026: **2 implementations, both early-stage.**

- **Ark Labs / Arkade.** Public beta since October 2025. The first mainnet implementation of the Ark protocol specification. Has integration partnerships but no public data on round volumes, locked BTC, or user count. ([The Block](https://www.theblock.co/post/375271/ark-labs-arkade-public-beta-layer-2-bitcoin))
- **Second / Bark.** Demonstrated first mainnet Ark transactions. Command-line wallet and ASP implementation. Research-heavy team with extensive publications on Ark economics. ([Second](https://second.tech/))

No other ASP implementations are publicly known. The protocol is open-source ([Ark Protocol specification](https://ark-protocol.org/); [arkdev.info](https://arkdev.info/)), but no third-party ASP has been announced.

### Projected Growth

Factors favoring ASP growth:
- Tether's investment in Ark Labs (announced 2025) could drive USDT-on-Ark adoption, creating demand for more ASPs.
- The open-source specification lowers the technical barrier (though not the capital barrier).
- If Lightning continues to grow, ASPs serving as Lightning gateways may attract users seeking Ark's privacy and batch settlement benefits.

Factors constraining ASP growth:
- Capital requirements are high ($8-40M in locked BTC for a medium ASP, per the [problem-spec](problem-spec.md)).
- The protocol is complex and relatively new. Operational risk is significant.
- Revenue (3-6% ROI on locked capital) is modest relative to the risk and capital commitment.
- User adoption is uncertain. Without users, an ASP has no fee revenue.

**Realistic timeline for 5+ ASPs:** 2-4 years. This is speculative. It depends on Ark adoption, which depends on user demand, which depends on the protocol's privacy and UX advantages over Lightning being compelling enough to attract users willing to pay higher fees.

### Total Market Size

At the medium ASP scale from the problem-spec ($10M/week throughput, $26M locked capital under V2):

- With 5 ASPs: ~$130M total locked capital, of which perhaps 20-30% ($26-39M) might flow through a lending market in a given month (not all ASPs are capital-constrained simultaneously).
- With 10 ASPs: ~$260M total locked, $50-80M addressable lending market.
- With 20 ASPs: ~$520M total locked, $100-160M addressable.

For comparison, the U.S. fed funds market has $100+ billion in daily volume. Lightning Pool's total lifetime volume is not publicly reported but is orders of magnitude smaller. The ASP lending market would start in the tens of millions -- significant for participants, negligible in global terms.

### When Does a Protocol Make Sense?

| Phase | Participants | Volume | Mechanism |
|-------|-------------|--------|-----------|
| 1 | 2-3 ASPs | < $10M/month | Bilateral negotiation |
| 2 | 5-10 ASPs + LPs | $10-50M/month | Bulletin board, standardized terms |
| 3 | 10-20 ASPs + LPs + HODLers | $50-200M/month | Batch auction or automated rate |
| 4 | 20+ ASPs + broad LP base | > $200M/month | Protocol-level integration |

Building protocol infrastructure for Phase 1 volumes is waste. The inflection point is Phase 2 -- when enough participants exist that bilateral negotiation becomes a bottleneck and standardized terms would meaningfully reduce friction.

---

## 7. Comparison to Existing Bitcoin Liquidity Markets

| Feature | ASP Interbank (proposed) | Lightning Pool | Amboss Magma | CeFi Lending (Ledn, pre-2026) | Lygos (DLC-based) |
|---------|------------------------|---------------|-------------|------------------------------|-------------------|
| Asset | BTC | BTC (channel capacity) | BTC (channel capacity) | BTC | BTC |
| Term | 1-28 days | ~2016 blocks (~14 days) | Variable (hours to weeks) | Variable | Fixed term |
| Security model | On-chain escrow | CLTV in channel funding tx | Escrow via Amboss | Custodial (platform holds BTC) | DLC (2-of-2 multisig + oracle) |
| Rate | 2-4% est. | Batch auction clearing | Marketplace (median ~2.6%) | 0.5-5.25% (by tier) | Negotiated |
| Participants | ASPs, LPs, HODLers | Lightning node operators | Lightning node operators | Anyone with BTC | Institutional borrowers |
| Settlement | Lightning + on-chain | On-chain (batch tx) | Lightning | Custodial internal ledger | On-chain |
| Custody | Non-custodial (escrow) | Non-custodial | Non-custodial | Custodial | Non-custodial |
| Collateral type | ASP reserves, expiry claims | Channel funding output | Channel funding output | None (trust-based) | BTC in DLC |
| Borrower type | ASPs needing round capital | Nodes needing inbound liquidity | Nodes needing inbound liquidity | Anyone | Institutions needing USD |
| Status | Conceptual | Live (since 2020) | Live (since 2021) | Discontinued yield products | Live (since 2025) |

### Differentiation

The proposed ASP market is distinguished by:

1. **Purpose-specific.** Serves a unique function (funding Ark VTXO trees) that no existing market addresses. Lightning Pool and Magma fund Lightning channels; CeFi funds anything; Lygos funds BTC-collateralized USD loans. None fund Ark rounds.

2. **Same-asset lending.** BTC-for-BTC eliminates FX risk, mark-to-market, and most haircut dynamics. Lightning Pool is also BTC-for-BTC. CeFi lending typically involves BTC-for-USD or BTC-for-stablecoin. Same-asset lending is structurally simpler.

3. **Hybrid trust model.** Not fully trustless (the ASP's collateral includes forward claims that are not script-enforced), not fully custodial (on-chain escrow for the primary collateral). This occupies a middle ground between Lightning's fully script-enforced channels and CeFi's fully custodial model.

4. **Multi-source.** Draws from three distinct liquidity pools (ASPs, Lightning LPs, HODLers) with different risk profiles, terms, and rates. This diversification is unique -- Lightning Pool draws only from Lightning node operators.

---

## 8. The Cold Start Problem

### Phase 1: Bilateral ASP Relationships (Now -- Year 1)

**Participants:** Ark Labs and Second. Possibly a third ASP if one launches.

**Mechanism:** Direct negotiation. No protocol, no marketplace. Two operators coordinate on timing, amount, and rate. Settlement over Lightning.

**What triggers this:** One ASP has a surplus and the other has a deficit at the same time. Given that both are early-stage with small user bases, the likelihood of meaningful lending demand is low. The more likely scenario is that both ASPs are capital-constrained simultaneously (both trying to grow) or both have surplus (both have low usage). Uncorrelated demand requires different user bases and round schedules.

**Duration of this phase:** Until 3+ ASPs exist with differentiated demand patterns. Estimated: 1-3 years.

### Phase 2: Lightning LP Outreach (Year 1-2)

**Participants:** 3-5 ASPs + 10-20 Lightning node operators willing to lend.

**Mechanism:** ASPs approach Lightning LPs directly. The pitch: "You're earning 1.5% routing payments through your idle channel capacity. Close those underperforming channels and lend to us at 3% for 28 days, secured by on-chain escrow." Standardized term sheets (amount, rate, term, collateral ratio) reduce negotiation overhead.

**What triggers this:** ASP demand for capital exceeding what inter-ASP lending can supply. An ASP processing $10M/week cannot fund growth from the surplus of another ASP that also processes $10M/week. External capital is needed.

**Challenges:** Lightning LPs must be convinced that (a) ASP lending is safe (security model education), (b) the rate premium over Lightning routing justifies the switching cost, and (c) the operational mechanics are manageable (locking BTC in escrow, monitoring term, handling repayment).

**Duration:** Until volumes justify automated matching. Estimated: 1-2 years beyond Phase 1.

### Phase 3: Bulletin Board (Year 2-3)

**Participants:** 5-10 ASPs + 20-50 LPs.

**Mechanism:** A simple web interface or Lightning-native protocol where participants post offers and requests. Matching is manual but discovery is automated. Market data (rates, volumes, terms) is visible to all participants.

**What triggers this:** Phase 2's bilateral negotiation becoming a bottleneck -- too many counterparties to manage individually, rate information too opaque.

### Phase 4: Batch Auction (Year 3-5)

**Participants:** 10-20 ASPs + 50+ LPs + HODLer participation.

**Mechanism:** Periodic auctions (daily or per-block-epoch) clearing at a uniform price. Modeled on Lightning Pool's architecture. Potentially built as an extension to Lightning Pool itself or as a standalone protocol.

**What triggers this:** Phase 3's bulletin board showing consistent volume and predictable clearing patterns. The auction formalizes what the bulletin board reveals informally.

### Phase 5: Protocol Integration (Year 5+)

**Participants:** Broad market.

**Mechanism:** Lending integrated into ASP software. An ASP that needs capital broadcasts a borrowing request to the network; available lenders respond; the protocol matches and settles automatically. Rate discovery is continuous.

**What triggers this:** Scale sufficient to justify the engineering investment. The protocol must be worth building -- meaning the market is large enough, persistent enough, and standardized enough that automating it saves meaningful costs.

**Realistic assessment of timeline:** Phase 1 can begin today if both ASPs have the operational bandwidth. Phase 2 depends on ASP growth, which depends on Ark adoption. Phases 3-5 are speculative -- they assume a world where Ark has meaningful adoption, multiple ASPs compete, and the liquidity market is a binding constraint worth solving with infrastructure.

---

## 9. Devil's Advocate

### "There is no market. There are two ASPs."

This is the strongest objection. An interbank market with two banks is not a market. It is a bilateral credit line. The entire framework -- rate discovery, settlement rails, multi-source lending -- is infrastructure for a market that does not exist and may not exist for years. Building any of this now is premature. The honest assessment: this is a research document about a market that *could* exist if Ark succeeds, not a design for a market that *should* be built today.

### "Lightning LPs already have established yield. Why switch?"

A Lightning node earning 2.5% on well-managed channels has no reason to risk lending to an unproven ASP at 3%. The premium is too thin for the uncertainty. The pitch only works if (a) the LP has truly idle capacity earning below 1.5%, and (b) the ASP lending model is well-enough understood that the LP considers it comparable risk to a channel lease. Both conditions require Ark to mature significantly.

### "HODLers got burned. 'Non-custodial yield' sounds like what they all claimed."

BlockFi's marketing literally said "your crypto is not lent out" (it was). Celsius claimed institutional-grade risk management (there was none). Every failed platform described itself as different from the last failed platform. On-chain escrow *is* genuinely different -- the security is enforced by Bitcoin script, not by corporate policy. But explaining this to a retail HODLer who lost BTC on Celsius requires overcoming deep, justified skepticism. The non-custodial distinction is real but the marketing battle is uphill.

### "Maybe ASPs just need to be better capitalized."

If the ASP's unit economics require borrowing to function, that is not a liquidity problem -- it is a capitalization problem. The fed funds market works because banks are fundamentally solvent and profitable; they borrow overnight to smooth fluctuations, not to fund core operations. If ASPs cannot operate without external leverage, the lending market is a band-aid on an unsustainable business model. The V2 revocation mechanism reduces capital requirements significantly (from ~4x to ~2x throughput), and dynamic fee tiers incentivize behavior that reduces lockup further. Perhaps the right answer is that ASPs should be capitalized at 2-3x their throughput and funded by equity investors, not by short-term lending. Borrowing to fund trees is a workaround for undercapitalization.

Counter-argument: even well-capitalized banks use the fed funds market. The issue is not solvency but *efficiency*. An ASP holding enough buffer to cover every possible demand spike is overcapitalized -- that BTC could be earning yield elsewhere. Borrowing to cover temporary peaks while maintaining a solid capital base is sound treasury management, not desperation.

### "The fed funds market took decades. This is premature."

The fed funds market emerged in the 1920s, went dormant in the 1930s-40s, revived in the 1950s, and only became the central mechanism of U.S. monetary policy in the 1960s-70s. That is 40-50 years from inception to maturity. Bitcoin Ark launched in 2025. Designing a lending market now is like designing the fed funds market in 1922 -- you are building for a future that may not arrive, or may arrive in a form you cannot predict.

Counter-argument: Bitcoin moves faster than 1920s banking. Lightning Pool went from concept to live market in under a year. Amboss Magma built a liquidity marketplace in months. The infrastructure exists (Lightning, on-chain multisig, DLCs) and the participants are technically sophisticated. If Ark adoption reaches critical mass, the lending market could develop in 1-2 years, not decades. The question is whether Ark reaches critical mass, not whether the market can be built.

### "BTC-for-BTC lending eliminates FX risk but introduces return-of-capital risk."

In a BTC-for-BTC loan, there is no mark-to-market because the loan is denominated in the same unit as the collateral. But "no FX risk" does not mean "no risk." The lender's risk is that the ASP defaults and the collateral (ASP's other BTC assets) is insufficient. If the ASP's trees suffer mass unilateral exits (reducing the BTC it reclaims) while it has outstanding loans, the ASP may not have enough BTC to repay. Same-asset lending eliminates price risk but not credit risk. The lender still needs to evaluate whether the ASP can repay, which requires understanding the ASP's full balance sheet -- including forward claims that are inherently uncertain.

---

## Sources

- [St. Louis Fed: A New Daily Federal Funds Rate Series, 1928-54](https://www.stlouisfed.org/publications/review/2021/01/14/a-new-daily-federal-funds-rate-series-and-history-of-the-federal-funds-market-1928-54)
- [Federal Reserve: The Re-emergence of the Federal Funds Market in the 1950s](https://www.federalreserve.gov/econres/notes/feds-notes/re-emergence-of-the-federal-funds-market-in-the-1950s-20190322.html)
- [Federal Reserve History: Federal Funds Rate](https://www.federalreservehistory.org/essays/fed-funds-rate)
- [The Block: Ark Labs launches Arkade public beta](https://www.theblock.co/post/375271/ark-labs-arkade-public-beta-layer-2-bitcoin)
- [Second: Demoing first Ark transactions on mainnet](https://blog.second.tech/demoing-the-first-ark-transactions-on-bitcoin-mainnet/)
- [Ark Protocol specification](https://ark-protocol.org/)
- [Ark Protocol: VTXOs](https://ark-protocol.org/intro/vtxos/index.html)
- [Second: Diving deeper into Lightning liquidity -- Amboss Magma](https://blog.second.tech/diving-deeper-into-lightning-liquidity-amboss-magma-2/)
- [Second: Bitcoin Yield Survey](https://blog.second.tech/survey-of-bitcoin-yield/)
- [Voltage: Where Does the Yield Come From?](https://www.voltage.cloud/blog/where-does-lightning-network-yield-come-from)
- [Atlas21: Lightning routing yields 10% annually](https://atlas21.com/lightning-routing-yields-10-annually-blocks-announcement/)
- [Lightning Pool Whitepaper](https://lightning.engineering/lightning-pool-whitepaper.pdf)
- [Lightning Labs: Pool Technical Deep-Dive](https://lightning.engineering/posts/2020-11-02-pool-deep-dive/)
- [Lightning Pool Batch Execution docs](https://docs.lightning.engineering/lightning-network-tools/pool/batch_execution)
- [Amboss Magma documentation](https://old-docs.amboss.tech/docs/magma/intro)
- [CoinDesk: Lygos Aims to Banish Ghosts of Past](https://www.coindesk.com/business/2025/08/27/lygos-aims-to-banish-ghosts-of-crypto-lending-collapse-with-non-custodial-bitcoin-model)
- [Blockspace: Lygos Finance acquires Atomic Finance](https://blockspace.media/insight/lygos-finance-acquires-atomic-finance-to-launch-non-custodial-dlc-powered-bitcoin-loans/)
- [Chicago Fed: A Retrospective on the Crypto Runs of 2022](https://www.chicagofed.org/publications/chicago-fed-letter/2023/479)
- [CoinTelegraph: Bitcoin loans are back](https://cointelegraph.com/news/bitcoin-loans-back-rewriting-book-celsius-burned)
- [Babylon Labs](https://babylonlabs.io/)
- [CoinLaw: Bitcoin Staking Statistics 2026](https://coinlaw.io/bitcoin-staking-statistics/)
- [Ledn](https://www.ledn.io)
- [Ark Labs blog: Liquidity Requirements](https://blog.arklabs.xyz/liquidity-requirements/)
- [Second: Ark Liquidity Research](https://blog.second.tech/ark-liquidity-research-01/)
- [Second fee schedule](https://second.tech/docs/learn/fees)

# Existing Ark Liquidity Proposals: A Comprehensive Survey

*Research compiled March 2026. All claims cited to sources. Where information is absent, that is noted explicitly.*

---

## Table of Contents

1. [The Liquidity Problem Defined](#1-the-liquidity-problem-defined)
2. [V2 Revocation as Liquidity Solution](#2-v2-revocation-as-liquidity-solution)
3. [VTXO Liveness Delta Adjustments](#3-vtxo-liveness-delta-adjustments)
4. [Federation and Multi-ASP Models](#4-federation-and-multi-asp-models)
5. [Lightning as Liquidity Bridge](#5-lightning-as-liquidity-bridge)
6. [Ark as Channel Factory](#6-ark-as-channel-factory)
7. [Warm Wallet Concept](#7-warm-wallet-concept)
8. [Tether Investment and Stablecoin Implications](#8-tether-investment-and-stablecoin-implications)
9. [Fee-Based Liquidity Management](#9-fee-based-liquidity-management)
10. [Lines of Credit](#10-lines-of-credit)
11. [What the Community Sees as the Biggest Challenges](#11-what-the-community-sees-as-the-biggest-challenges)
12. [Explicit Repo or Lending Proposals](#12-explicit-repo-or-lending-proposals)
13. [Conclusion: Gap Map](#13-conclusion-gap-map)

---

## 1. The Liquidity Problem Defined

The ASP liquidity problem is structural: when users refresh VTXOs, the ASP must lock fresh BTC into the new round transaction's tree immediately, but the old BTC backing the previous VTXOs does not become available until those VTXOs expire (~28 days / 4 weeks). This creates a rolling capital requirement where the ASP always has more BTC locked up than it is earning fees on.

**Quantification from Ark Labs:**

The Ark Labs blog provides a simulation-based analysis. For a simple scenario: the ASP needs 2.67 BTC of liquidity to support 0.33 BTC traded inside Ark. With higher transaction frequency (10 payments instead of 3), the requirement jumps to 8.52 BTC of liquidity to support the same 0.33 BTC traded. The liquidity multiplier depends on three factors: money velocity (how often capital changes hands), the timelock duration, and the ratio of transaction value to change outputs. ([Ark Labs: Understanding Ark Liquidity Requirements](https://blog.arklabs.xyz/liquidity-requirements/))

**Second's comparative analysis:**

Second's research frames ASP liquidity in "sat-days" (satoshis locked multiplied by days locked) and compares Ark to Lightning LSPs across user behavior scenarios:
- Weekly top-ups: LSP is 2.5x more capital-efficient than Ark
- Monthly top-ups: Roughly equivalent (LSP 1.05x better)
- Quarterly top-ups: Ark is 3.7x more capital-efficient
- DCA stacker: Ark is 6.65x more capital-efficient

The key structural difference: "An LSP's liquidity requirements are driven primarily by changes in users' balances, whereas Ark server liquidity requirements are driven by payment volume." ([Second Blog: Ark Liquidity Research](https://blog.second.tech/ark-liquidity-research-01/))

**The yield benchmark:**

Second's Bitcoin yield survey establishes the prevailing opportunity cost of BTC capital at roughly 1-4% annually, with Lightning liquidity leasing (Amboss Magma median: 2.6% APR) as the closest analogue. This means an ASP must generate enough fee revenue to cover not just operational costs but also the 1-4% opportunity cost on all locked-up BTC, or capital will flow elsewhere. ([Second Blog: Bitcoin Yield Survey](https://blog.second.tech/survey-of-bitcoin-yield/))

---

## 2. V2 Revocation as Liquidity Solution

**Proposed by:** Burak (brqgoo), the original Ark protocol designer.

**How it works:** Ark V2 introduces revocation logic modeled on (but distinct from) Lightning's revocation scheme. Each VTXO owner holds an individual revocation secret. When a user spends a VTXO, they reveal their secret to the ASP. When a sufficient number of VTXO owners in a shared UTXO reveal their secrets, the ASP aggregates them into an aggregate revocation secret (calculated as sec1 + sec2 + ... + secn) and uses it to unlock the revocation branch, reclaiming the corresponding portion of liquidity immediately -- without waiting for the 4-week timelock to expire. ([Burak: Introducing Ark V2](https://brqgoo.medium.com/introducing-ark-v2-2e7ab378e87b); [NoBSBitcoin: Ark V2](https://www.nobsbitcoin.com/burak-introduces-ark-v2-design/); [The Bitcoin Manual: Ark V2](https://thebitcoinmanual.com/articles/ark-v2/))

**Scalability:** The revocation branch can encompass millions or even billions of leaves, each representing a combination of revealed secrets. A shared UTXO with 16 VTXOs contains a revocation branch with 805 leaves total, corresponding to all possible combinations of revealed secrets.

**How much does this actually reduce capital lockup?**

No public quantitative analysis exists that estimates the real-world improvement. Here is a rough framework:

- If users spend VTXOs uniformly across the 4-week window, and revocation triggers when, say, 60% of VTXOs in a shared UTXO are spent, the ASP could reclaim that portion after ~2-3 weeks on average instead of 4 weeks. This would reduce the peak liquidity requirement by roughly 30-40%.
- If users are active (high money velocity), secrets are revealed faster, and the ASP recovers liquidity sooner. Low-activity users (hodlers who rarely transact) reveal secrets slowly, meaning the ASP gains less from revocation on those shared UTXOs.
- The worst case is unchanged: if no user in a shared UTXO spends their VTXO, the ASP must wait the full 4 weeks. Revocation helps the average case, not the worst case.

**Assessment:** V2 revocation is the most significant liquidity improvement proposed. It directly attacks the core problem (time-locked capital) and does so without requiring any external infrastructure. But it is not sufficient on its own -- it reduces the problem, it does not eliminate it. The ASP still needs capital to bridge the gap between fresh round creation and revocation-based recovery.

---

## 3. VTXO Liveness Delta Adjustments

**Proposed by:** Burak and discussed in the Stacker News AMA.

**How it works:** The "liveness delta" is the timelock duration for VTXOs. The default is 4 weeks (~28 days). Cutting it in half (2 weeks) halves the liquidity lockup requirement, because the ASP can sweep expired VTXOs in half the time. ([Stacker News: Ark AMA](https://stacker.news/items/192040))

ASPs can customize their liveness delta as a policy parameter. This is not protocol-level -- each ASP sets its own preference based on fee market and liquidity conditions.

**Trade-offs:**
- **Shorter delta = less capital lockup** but **more frequent user action required.** Users must refresh their VTXOs before expiry or lose them. A 2-week delta means users must interact with the ASP at least every 2 weeks.
- **User experience impact.** 4 weeks is already short compared to Lightning channel lifetimes (often months or years). 2 weeks creates significant UX pressure, especially for infrequent users.
- **Delegation as mitigation.** Arkade's delegation feature lets users authorize a third party to renew VTXOs on their behalf, reducing the UX burden of shorter deltas. This enables more aggressive delta reduction without forcing users to be constantly online. ([Ark Labs: Adios Expiry](https://blog.arklabs.xyz/adios-expiry-rethinking-liveness-and-liquidity-in-arkade/))

**Assessment:** This is a straightforward lever that ASPs control directly. A move from 4 weeks to 2 weeks cuts the problem in half. Combined with V2 revocation, the effective capital lockup could drop to 30-40% of the original 4-week baseline. But it has a floor: you cannot reduce the delta below the point where users can reasonably refresh, even with delegation.

---

## 4. Federation and Multi-ASP Models

### 4.1 ASP Federation

**Proposed by:** Referenced by Burak in the Stacker News AMA: "One must own a large chunk of BTC to run an ASP infra. Otherwise, its better to join an ASP federation." ([Stacker News: Ark AMA](https://stacker.news/items/192040))

**What this means:** The concept is mentioned but not fully specified. The implication is that multiple entities pool their BTC to collectively fund ASP operations, sharing the capital requirements (and presumably the fee revenue). This is analogous to a consortium model -- like how the Liquid Federation operates, where functionaries jointly manage the L-BTC peg.

**Open questions (no public answers found):**
- How would governance work? Multisig? DAO?
- How would fee revenue be distributed -- proportional to capital contributed? Based on uptime?
- What happens if one federation member withdraws capital?
- Is the federation transparent to users, or does it appear as a single ASP?

**Assessment:** Federation is acknowledged as a direction, not a concrete proposal. No detailed architecture or implementation plan has been published.

### 4.2 Inter-ASP Liquidity Routing

**Proposed in:** Bitcoin Magazine analysis of Ark's architecture.

When one ASP runs low on liquidity and fees spike, it can "punt" payments to another ASP with more liquidity available, establishing linkages between ASPs. This creates a "round robin" dynamic: "I scratch your back, you scratch mine." ASPs facing liquidity crunches route payments to peers with available capital, and the favor is returned when conditions reverse. ([Bitcoin Magazine: What Ark Could Learn From Lightning](https://bitcoinmagazine.com/takes/what-ark-could-potentially-learn-from-lightning))

**How it differs from federation:** This is not capital pooling. Each ASP maintains its own balance sheet. Instead, it is payment routing -- an ASP short on liquidity outsources transaction processing to one with excess, rather than refusing transactions or hiking fees.

**Assessment:** This is a liquidity-distribution mechanism, not a liquidity-creation mechanism. It helps allocate existing capital more efficiently across ASPs but does not increase the total amount of BTC available for ASP operations. It is useful but does not address the fundamental problem of capital requirements.

---

## 5. Lightning as Liquidity Bridge

Ark is designed with native Lightning interoperability. Users can attach HTLCs (or PTLCs) to pool transactions, enabling payments between Ark and Lightning. Multiple ASPs can be used to pay Lightning invoices from different VTXO sources using multi-part payments. ([Ark Protocol: Out-of-Round Payments](https://ark-protocol.org/intro/oor/index.html); [Bitcoin Magazine: Ark](https://bitcoinmagazine.com/technical/bitcoin-layer-2-ark))

**As a liquidity bridge:** Lightning enables ASPs to move liquidity between systems. An ASP with excess Ark liquidity but insufficient Lightning liquidity (or vice versa) could rebalance by routing through the other network. This is operationally valuable but does not create new liquidity -- it reallocates existing capital across deployment options.

**Fulmine:** Ark Labs built Fulmine, "a Bitcoin wallet daemon that enables swap providers and payment hubs to optimize Lightning Network channel liquidity while minimizing on-chain fees." This is specifically designed for the kind of cross-network liquidity optimization that ASPs would need. ([GitHub: ArkLabsHQ/fulmine](https://github.com/ArkLabsHQ/fulmine))

**Specific proposals for Lightning-based ASP funding:** No public discussion found of using Lightning to explicitly lend BTC to ASPs or to create a repo-like facility between Lightning and Ark. The integration is operational (payment routing, liquidity balancing) rather than financial (lending, repo).

---

## 6. Ark as Channel Factory

**Proposed by:** Discussion on Delving Bitcoin, summarized in Bitcoin Optech Newsletter #387 (January 2026).

**How it works:** Ark's batch round structure can function as an efficient channel factory for Lightning. Instead of individual on-chain transactions for channel opens, closes, and splices, many channel owners batch their liquidity changes using VTXOs. This compresses the on-chain footprint of Lightning channel management. ([Delving Bitcoin: Ark as Channel Factory](https://delvingbitcoin.org/t/ark-as-a-channel-factory-compressed-liquidity-management-for-improved-payment-feasibility/2179); [Bitcoin Optech Newsletter #387](https://bitcoinops.org/en/newsletters/2026/01/09/))

**Liquidity benefits:**
- LSPs could provide liquidity to more end users with less on-chain cost
- Built-in VTXO expiration lets LSPs reclaim liquidity from idle channels without expensive force-close transactions
- Routing nodes could use regular Ark rounds to shift liquidity between channels rather than individual splice operations

**Trade-off identified:** The ASP/LSP "have to be the same identity or trust each other" to prevent situations where unresponsive users cause the LSP to "hand all their money to the ASP at tree timeout."

**Impact on ASP liquidity:** This proposal does not directly solve the ASP's capital problem. It improves capital efficiency for Lightning LSPs who use Ark as infrastructure. But if the ASP and LSP are the same entity (or trust each other), it enables more efficient capital deployment across both systems -- the same BTC pool can serve Ark users and Lightning channel management.

---

## 7. Warm Wallet Concept

**Extensive search conducted.** No detailed "warm wallet" proposal specific to ASP liquidity was found in Ark protocol documentation, GitHub issues, blog posts, or community discussions.

The term appears in general Bitcoin context (a wallet between cold storage and hot wallet in terms of connectivity and security) but no Ark-specific proposal uses "warm wallet" as a named concept for liquidity providers sharing BTC holdings with ASPs.

**What may be related:** The Stacker News AMA references ASP federations where multiple parties contribute capital. The concept of liquidity providers depositing BTC into a shared pool accessible to the ASP is consistent with the description in the original research prompt, but it has not been publicly articulated under the "warm wallet" label in any source found.

**Assessment:** This appears to be either an informal/private discussion concept that has not been published, or a construct inferred from the general direction of Ark's liquidity solutions. No public specification exists.

---

## 8. Tether Investment and Stablecoin Implications

On March 12, 2026, Tether announced a strategic investment in Ark Labs as part of a $5.2M seed round, bringing total funding to $7.7M. The investment is focused on bringing stablecoin and programmable finance infrastructure to Bitcoin. ([The Block: Tether Backs Ark Labs](https://www.theblock.co/post/393198/tether-backs-ark-labs-5-2-million-seed-raise-to-expand-stablecoin-and-programmable-finance-infrastructure-on-bitcoin); [Tether.io: Strategic Investment](https://tether.io/news/tether-announces-strategic-investment-in-ark-labs-reintroducing-stablecoins-to-programmable-bitcoin-infrastructure/); [CoinDesk: Tether Invests](https://www.coindesk.com/business/2026/03/12/tether-invests-in-ark-labs-to-make-bitcoin-ready-for-stablecoins-and-payments))

Arkade launched in public beta in October 2025 with support for stablecoins and digital assets, including infrastructure designed to support USDT on Bitcoin. ([The Block: Arkade Public Beta](https://www.theblock.co/post/375271/ark-labs-arkade-public-beta-layer-2-bitcoin))

**Does stablecoin integration change the liquidity equation?**

This is a critical question with several angles:

**Scenario 1: USDT as the "cash" side of a repo.** If ASPs could borrow BTC against USDT collateral (or vice versa), stablecoins could serve as the cash leg of a Bitcoin-native repo. The ASP locks expiring VTXOs (or the BTC it expects to reclaim) as collateral and receives USDT for short-term liquidity. At maturity, the ASP repurchases the BTC and returns the USDT. This is structurally a cross-currency repo.

**Scenario 2: USDT float as working capital.** If Ark processes significant USDT volume, the ASP handles both BTC and USDT flows. Stablecoin liquidity is generally easier to source than BTC liquidity (stablecoin markets are deeper, with more lending infrastructure). An ASP could maintain USDT reserves and swap to BTC only when needed for round funding, reducing the amount of BTC that must be locked up.

**Scenario 3: Stablecoin fees reduce BTC capital pressure.** If users pay fees in USDT rather than BTC, the ASP accumulates stablecoin revenue that can be used to acquire BTC for liquidity needs, creating a more predictable funding pipeline than BTC-only fee revenue (which is volatile in dollar terms).

**No public proposals found** that explicitly connect Tether's investment to ASP liquidity solutions. The investment announcement focuses on "programmable payments, lending, capital markets, digital assets, and autonomous commerce" without specific ASP funding mechanisms. ([Ark Labs Blog: Fundraise Announcement](https://blog.arklabs.xyz/ark-labs-raises-5-2m-backed-by-tether-to-build-programmable-finance-on-bitcoin/))

**Assessment:** The Tether investment creates optionality. USDT on Ark opens a path to cross-currency repo (BTC/USDT), stablecoin-denominated lending to ASPs, and more liquid funding markets. But nobody has publicly proposed these mechanisms yet.

---

## 9. Fee-Based Liquidity Management

**Proposed by:** Multiple sources, including Burak (Stacker News AMA) and Second (liquidity research).

**How it works:** ASPs use dynamic fees as a demand-management tool:
- **High liquidity demand:** Increase fees to discourage large transactions and reduce capital outflow
- **Low liquidity demand:** Decrease fees to attract volume and revenue
- **VTXO age-based pricing:** The ASP charges lower fees when users refresh or spend VTXOs that are close to expiry (because the ASP will soon reclaim that liquidity anyway) and higher fees for fresh VTXOs (where the capital lockup is longest). ([Second Blog: Ark Liquidity Research](https://blog.second.tech/ark-liquidity-research-01/); [Second Docs: Ark Fees](https://docs.second.tech/ark-protocol/fees/))

Ark fees are a matter of policy, not protocol -- each ASP sets its own structure. The main cost components are: liquidity costs (opportunity cost of locked BTC), on-chain fees (Bitcoin network fees for round transactions), Lightning routing fees (for off-Ark payments), and development/operational costs. ([Second Docs: Ark Fees](https://docs.second.tech/ark-protocol/fees/))

**Assessment:** Fee management is a demand-side lever. It does not create new capital; it manages the timing and volume of capital demand. Necessary but not sufficient. An ASP in a liquidity crunch can raise fees to reduce demand, but at the cost of pushing users to competitors. This is a survival mechanism, not a growth strategy.

---

## 10. Lines of Credit

**Proposed by:** reardencode (in the Stacker News AMA, responding to questions about ASP liquidity management).

The specific quote: "ASPs would proactively manage liquidity -- they have visibility into the flow of funds from expiring pool transactions, and would likely pursue lines of bitcoin credit to bridge times of low expiration flow." ([Stacker News: Ark AMA](https://stacker.news/items/192040))

This is the closest any public discussion comes to proposing external capital sourcing for ASPs. The implication is that ASPs would borrow BTC from external lenders (institutions, wealthy Bitcoiners, other ASPs) to cover temporary liquidity gaps, repaying from the BTC reclaimed when VTXOs expire.

**No further specification found.** No discussion of:
- Who would provide these lines of credit
- What collateral the ASP would post
- What rates or terms would apply
- Whether this would be bilateral or through a market
- How the credit facility would be structured on-chain vs. off-chain

**Assessment:** This is the seed of the repo idea, articulated informally. The concept of "lines of bitcoin credit" to bridge liquidity gaps is exactly what a repo market would formalize. But as stated, it is a one-sentence mention in an AMA, not a proposal.

---

## 11. What the Community Sees as the Biggest Challenges

### Capital requirements

The community consistently identifies capital requirements as the primary barrier to ASP operation. From the Stacker News AMA: "One must own a large chunk of BTC to run an ASP infra." The Ark Labs blog simulation shows liquidity requirements of 8x-25x the traded volume depending on money velocity. ([Stacker News: Ark AMA](https://stacker.news/items/192040); [Ark Labs: Liquidity Requirements](https://blog.arklabs.xyz/liquidity-requirements/))

### Minimum viable capital

No specific number has been published. The simulation framework suggests the minimum depends on target capacity and user behavior. A rough estimate from the simulation: to support 1 BTC in active Ark volume with moderate money velocity, an ASP needs approximately 10-15 BTC in available liquidity. For a commercially viable ASP serving thousands of users, the requirement likely runs to hundreds of BTC.

### Profitability and fee structure

ASP profitability is not publicly modeled in detail. The fee structure must cover:
- Opportunity cost on locked BTC (1-4% APR based on market alternatives)
- On-chain transaction fees for round transactions
- Lightning routing fees for off-Ark payments
- Operational costs (server infrastructure, development)

If the opportunity cost alone is 2.6% APR (Amboss Magma median) on, say, 100 BTC of locked liquidity, the ASP needs ~2.6 BTC/year in fee revenue just to cover the cost of capital. At current BTC prices (~$85K), that is ~$221K/year before operational costs.

### The centralization concern

High capital requirements create centralization pressure. If running an ASP requires hundreds of BTC, only well-capitalized institutions can participate. This is the same dynamic Lightning faces with large hub nodes. The federation model is proposed partly to address this -- allowing smaller operators to pool capital -- but federation introduces its own governance and trust complexities.

---

## 12. Explicit Repo or Lending Proposals

**Extensive search conducted across:**
- Ark protocol GitHub (github.com/ark-protocol) -- no repo/lending issues found
- Ark Labs GitHub (github.com/ArkLabsHQ) -- no repo/lending issues found
- Ark Labs blog (blog.arklabs.xyz) -- no repo/lending posts found
- Second blog (blog.second.tech) -- yield survey references opportunity cost but no repo proposal
- Delving Bitcoin -- channel factory discussion only; no repo/lending
- Stacker News AMA -- "lines of credit" mention (see Section 10), but no structured proposal
- Bitcoin Optech -- Ark topic coverage; no repo/lending
- Twitter/X from Ark developers -- no repo/lending proposals found in search results

**Finding: No one in the Ark community has publicly proposed a repo market, a structured lending facility, or a capital market for ASP liquidity.** The closest statement is reardencode's one-sentence mention of "lines of bitcoin credit." The community has focused on protocol-level solutions (revocation, delta reduction) and operational solutions (fee management, inter-ASP routing) rather than financial-market solutions.

This is a significant gap.

---

## 13. Conclusion: Gap Map

### What has been proposed

| Proposal | Status | Impact | Addresses Root Cause? |
|----------|--------|--------|-----------------------|
| V2 revocation | Designed, in implementation | High -- reduces lockup by 30-40% (estimated) | Partially -- helps average case, not worst case |
| Liveness delta reduction | Available as policy lever | Medium -- halving delta halves lockup | No -- just speeds up recovery |
| ASP federation | Mentioned, not specified | Potentially high | No -- pools capital but does not reduce total requirement |
| Inter-ASP routing | Conceptual | Low-medium -- distributes existing capital | No -- reallocation, not creation |
| Lightning bridge | Built (Fulmine) | Medium -- enables cross-network balancing | No -- reallocation, not creation |
| Ark as channel factory | Discussed on Delving Bitcoin | Medium for LSP-ASPs | Partially -- improves capital efficiency for dual-role operators |
| Fee-based demand management | Available as policy lever | Low -- demand management only | No |
| Lines of credit | One-sentence mention in AMA | Potentially high | Yes -- external capital addresses root cause |
| Stablecoin integration (Tether) | Infrastructure being built | Unknown but promising | Potentially -- opens cross-currency funding |

### What has NOT been proposed (but should be)

1. **A structured repo or lending market for ASP liquidity.** The ASP has a predictable, collateralizable funding need (it knows when VTXOs will expire and how much BTC it will reclaim). This is a textbook repo use case: short-term borrowing against collateral with a known maturity date. No one has proposed building this.

2. **A formal capital provider / LP role.** Lightning has liquidity providers (Magma, Pool). Ark has no equivalent formalized role for external capital providers who deposit BTC for ASP use and earn a return. The closest is the vague notion of ASP federation, but that is about operation, not investment.

3. **Yield products for BTC holders.** An ASP repo market would create a new yield opportunity for BTC holders: lend BTC to ASPs for 2-4 week terms at fixed rates. This is a product that does not exist anywhere in Bitcoin today and would compete favorably with Lightning liquidity leasing (similar rates, simpler mechanics, no channel management).

4. **On-chain collateral tracking for ASP borrowing.** Bitcoin's UTXO model enables precise tracking of which VTXOs are expiring when. This information could underpin a collateral management system where the ASP's expected future BTC inflows are used to secure current borrowing. No one has proposed this.

5. **Cross-ASP lending facility.** ASPs with excess liquidity could lend to ASPs with deficits, earning a return on idle capital. This is different from inter-ASP payment routing (which moves payments) -- this would move capital between ASPs through a lending mechanism. No proposal found.

6. **Risk-rated ASP credit.** A system where ASPs build credit history based on their repayment track record, round execution reliability, and capital adequacy, and receive better lending rates accordingly. This exists informally in Lightning (Amboss reputation) but has not been proposed for Ark.

### The fundamental observation

The Ark community has focused almost entirely on protocol-level solutions (revocation, delta reduction) and operational workarounds (fee management, routing). These reduce the liquidity problem but do not solve it. Nobody has proposed the obvious financial-market solution: let ASPs borrow the BTC they need, against the collateral they have (expiring VTXOs), at rates set by a market.

This gap exists because the Ark community is primarily composed of protocol engineers, not capital-markets practitioners. The tools to solve this problem come from traditional finance (repo markets, term lending, collateral management) rather than from Bitcoin protocol design. Bridging this gap -- bringing capital-markets thinking to Bitcoin L2 infrastructure -- is the opportunity.

---

*End of survey.*

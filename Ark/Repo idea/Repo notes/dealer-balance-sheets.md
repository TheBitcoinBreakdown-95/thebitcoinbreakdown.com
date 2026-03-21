# Dealer Balance Sheets in Repo Markets -- and Whether Bitcoin Can Work Without Them

*Research note for the Ark ASP liquidity project. Written for someone who understands Bitcoin protocol design but needs to understand the tradfi plumbing that makes repo markets function.*

---

## Part 1: How Dealer Balance Sheets Work in TradFi Repo

### What Dealers Actually Do

The repo market has two sides that cannot find each other efficiently:

**Cash-rich entities** -- money market funds, pension funds, insurance companies, corporate treasuries, sovereign wealth funds. These institutions hold massive pools of cash (hundreds of billions each) that must be deployed safely overnight or for short terms. They cannot leave cash idle. They cannot take credit risk. They need a safe, liquid, short-term instrument that pays a return.

**Cash-poor entities** -- hedge funds, leveraged investors, proprietary trading desks, other dealers. These participants hold securities (typically Treasuries, agency MBS, corporate bonds) and need short-term cash to fund those positions. A hedge fund running a $10B relative-value strategy might own $10B in bonds but need to borrow $9.5B every night to finance them.

Dealers -- JP Morgan, Goldman Sachs, Citadel Securities, Bank of America, Barclays -- sit between these two groups. The dealer borrows cash from the money market fund (the MMF does a reverse repo with the dealer -- the MMF buys securities from the dealer with an agreement to sell them back). The dealer then lends that cash to the hedge fund (the dealer does a reverse repo with the hedge fund -- the dealer buys securities from the hedge fund with an agreement to sell them back). The dealer earns the spread between the rate it pays the MMF and the rate it charges the hedge fund.

This sounds like simple intermediation. It is not. The critical function is what happens on the dealer's balance sheet between the two sides.

### The Balance Sheet Is the Product

Each repo transaction creates a matched pair on the dealer's books:

- **Asset side**: reverse repo receivable (the cash lent to the hedge fund, collateralized by their securities)
- **Liability side**: repo payable (the cash borrowed from the MMF, secured by the dealer's own securities or the hedge fund's securities, depending on structure)

The dealer does not simply pass cash through. It absorbs three types of mismatch:

**1. Maturity transformation.** The MMF wants to lend overnight. It wants liquidity -- the ability to pull its cash tomorrow morning. The hedge fund wants to borrow for a week, or a month, or rolling 30-day terms. It needs funding certainty -- the assurance that its positions will not be liquidated because financing disappeared. The dealer bridges this gap. It borrows overnight from the MMF, knowing the MMF might not roll tomorrow, and lends term to the hedge fund. The dealer's balance sheet absorbs the maturity mismatch. If the MMF does not roll, the dealer must find replacement funding from another MMF, or from the Fed's standing repo facility, or from its own cash reserves. This is the same maturity transformation that banks perform with deposits and loans, but compressed into days instead of years.

**2. Counterparty risk absorption.** The MMF does not evaluate the hedge fund. The MMF evaluates the dealer. Fidelity's money market fund lends to Goldman Sachs, not to Citadel's quantitative strategies fund. If the hedge fund defaults, Goldman absorbs the loss -- it keeps the hedge fund's collateral and liquidates it, taking the hit if the collateral has declined in value. The MMF's exposure is to Goldman, a G-SIB with a fortress balance sheet. This risk transformation is essential. MMFs are regulated under Rule 2a-7, which restricts them to high-quality, short-duration instruments. They could never lend directly to hedge funds. The dealer's credit standing is what makes the flow possible.

**3. Collateral transformation.** The hedge fund might hold corporate bonds, structured products, or lower-rated securities. The MMF will only accept Treasuries or agency MBS. The dealer accepts the hedge fund's lower-quality collateral on one side and posts its own high-quality collateral to the MMF on the other. The dealer's inventory of high-quality liquid assets (HQLA) is what enables this transformation. It is, in effect, renting its balance sheet quality to the hedge fund.

Without dealers performing these three functions, the cash-rich side and the cash-poor side would need to find each other directly, agree on terms, evaluate each other's credit, and manage the collateral. At the scale of the U.S. repo market -- roughly $4.5 trillion in daily outstanding volume -- bilateral negotiation between thousands of counterparties is operationally impossible.

### Why Regulatory Constraints Matter

Post-2008 regulation fundamentally changed the economics of dealer balance sheets. The constraints are cumulative and interact in ways that reduce repo capacity:

**Basel III Leverage Ratio.** Total exposure (including on- and off-balance-sheet items) divided by Tier 1 capital must exceed 3% globally. In the U.S., G-SIBs face a 5% supplementary leverage ratio (SLR), and their insured depository subsidiaries face 6%. Critically, the leverage ratio does not risk-weight assets. A Treasury reverse repo -- which carries virtually zero credit risk -- consumes the same leverage ratio capacity as a corporate loan. This means dealers cannot expand repo intermediation without either raising more equity capital or shrinking other business lines. Every dollar of repo on the balance sheet costs leverage ratio capacity, regardless of how safe the trade is.

**Liquidity Coverage Ratio (LCR).** Banks must hold enough HQLA to cover 30 days of net cash outflows under a stress scenario. Repo maturity mismatches -- borrowing overnight and lending term -- create potential outflows. If the dealer borrows overnight from an MMF and lends for 30 days to a hedge fund, the LCR model assumes the overnight borrowing might not roll, creating an outflow the dealer must cover with HQLA reserves. This penalizes exactly the maturity transformation that is the dealer's core repo function.

**Net Stable Funding Ratio (NSFR).** Penalizes reliance on short-term wholesale funding, which is precisely what repo is. Assets funded by repo require a higher proportion of stable funding (equity and long-term debt) as a counterbalance. NSFR does not kill repo, but it increases its cost by requiring the dealer to maintain a funding mix that is more expensive than pure repo funding.

**G-SIB Surcharge.** The largest globally systemic banks face additional capital charges based on a scoring methodology that includes size, interconnectedness, substitutability, complexity, and cross-jurisdictional activity. Repo activity contributes to several of these scores. A bank growing its repo book may push itself into a higher G-SIB surcharge bucket, triggering a step-function increase in capital requirements that makes the marginal repo trade uneconomic.

**Quarter-end and year-end window dressing.** The leverage ratio is calculated on a period-end basis (though there are moves toward averaging). Dealers shrink their balance sheets -- reducing repo intermediation -- in the days before reporting dates to optimize their reported ratios. This creates predictable, recurring volatility in repo rates: rates spike as dealers withdraw capacity, then normalize as they re-enter after the reporting snapshot. The September 2019 repo market seizure, when overnight repo rates spiked to 10% (from the usual ~2%), was partly caused by this dynamic coinciding with Treasury settlement dates and corporate tax payments.

### The Pozsar Framework: Institutional Cash Pools vs. Dealer Capacity

Zoltan Pozsar, while at the New York Fed and later at Credit Suisse, mapped the plumbing of the shadow banking system with a precision no one else has matched. His central insight for repo markets:

**Institutional cash pools have grown exponentially.** Corporate treasuries, asset managers, securities lenders, pension funds, and sovereign wealth funds collectively hold pools of short-term cash that have grown from roughly $100 billion in 1990 to over $6 trillion by 2013 to substantially larger today. These pools exist because of regulatory requirements (pension funds must hold liquid reserves), corporate cash hoarding (Apple, Google, Berkshire), and the sheer scale of global asset management (BlackRock alone manages over $10 trillion).

**Dealer balance sheets have not grown proportionally.** Post-2008 regulation -- the leverage ratio in particular -- constrains how much repo intermediation dealers can provide. The numerator (capital) has grown, but the denominator (permitted exposure) is capped by regulation. Dealer balance sheet capacity for repo has been roughly flat to declining in real terms since 2010.

**The gap is structural.** Pozsar's "money dealer" framework shows that the dealer balance sheet is a finite resource. When institutional cash pools exceed dealer intermediation capacity, one of several things happens:

1. Cash pools accept lower returns (they lend at lower rates because dealer capacity is scarce and they compete for access)
2. Cash pools move into less safe instruments (reaching for yield because safe short-term rates are depressed)
3. The sovereign steps in as dealer of last resort

Option 3 is what actually happened. The Federal Reserve's Overnight Reverse Repurchase Facility (ON RRP) was introduced in 2013 and scaled massively during 2021-2023, absorbing over $2.5 trillion at peak. The ON RRP allows money market funds to repo directly with the Fed, bypassing dealer balance sheets entirely. The Fed is acting as a dealer that faces no leverage ratio constraint, no LCR, no G-SIB surcharge. It is balance sheet capacity of last resort.

This is the punchline: the world's largest financial market cannot function without either unconstrained dealer balance sheets (pre-2008) or a sovereign backstop (post-2008). The intermediation function is that essential.

### What Happens When Dealer Capacity Runs Out

The repo market has provided multiple demonstrations:

**September 2019.** Overnight repo rates spiked from ~2% to 10% intraday on September 17. The proximate causes were a Treasury settlement ($54B in new issuance) and a corporate tax deadline that drained reserves. But the underlying cause was that dealer balance sheets were fully utilized -- they had no spare capacity to intermediate the additional flow. The Fed had to intervene with emergency repo operations for the first time since the 2008 crisis.

**March 2020.** COVID-driven panic selling overwhelmed dealer capacity across Treasury, repo, and commercial paper markets simultaneously. Dealers could not absorb the selling because their balance sheets were already close to regulatory limits. The Fed launched massive QE and expanded repo operations to restore functioning.

**The pattern:** in a system where intermediation depends on finite balance sheets, stress events are not about solvency -- they are about capacity. The assets are fine (Treasuries do not default). The problem is that no one has the balance sheet space to intermediate them.

---

## Part 2: Does a Bitcoin Repo Market Need Dealers?

The question is whether the dealer's three core functions -- maturity transformation, counterparty risk absorption, and collateral transformation -- are necessary in a BTC-for-BTC system designed to provide ASP liquidity.

### Functions That May Not Be Needed

**1. Maturity transformation -- likely unnecessary.**

In a BTC-for-BTC Ark repo, the term is defined by the VTXO expiry cycle. An LP lending BTC to an ASP knows the term upfront: 14 days, 28 days, or whatever the round's VTXO locktime is. There is no overnight-to-term transformation because the use case does not require it. The ASP does not need overnight money that rolls -- it needs term funding that matches the VTXO lifecycle.

This is a fundamental structural difference from tradfi repo. In tradfi, the MMF wants overnight because it needs daily liquidity for redemptions. In a BTC lending market, the LP is not a money market fund with daily redemption pressure. The LP is a long-term bitcoin holder seeking yield on an asset that otherwise sits idle. The LP can commit to a fixed term without liquidity mismatch.

The absence of maturity transformation eliminates the largest single reason dealers exist. No one needs to stand between a short-dated lender and a long-dated borrower, because both sides can agree on the same term.

**2. Counterparty risk absorption -- replaced by protocol.**

In tradfi, the dealer absorbs counterparty risk because the cash lender cannot evaluate or monitor the cash borrower. The MMF does not know which hedge funds Goldman is lending to.

In a BTC-for-BTC system with on-chain escrow, this intermediation is unnecessary. The collateral -- BTC -- is locked in a script (multisig, HTLC, or covenant) that neither party controls unilaterally. If the borrower (ASP) defaults, the lender's recourse is enforced by the Bitcoin protocol itself, not by the dealer's willingness and ability to make them whole. The lender does not need to evaluate the borrower's credit standing -- the lender evaluates the escrow script.

This is not perfectly trustless. The lender still faces protocol risk (a bug in the escrow script), oracle risk (if any external conditions are referenced), and liquidity risk (the escrow might lock BTC for longer than expected during a dispute). But these are qualitatively different from credit risk. They are auditable, deterministic, and do not require a creditworthy intermediary.

**3. Collateral transformation -- structurally eliminated.**

In tradfi, the dealer transforms collateral quality: it accepts corporate bonds from the hedge fund and posts Treasuries to the MMF. In a BTC-for-BTC system, the collateral and the loan are the same asset. There is no quality spectrum to transform. BTC is BTC.

This eliminates the third major dealer function. There is no need for an entity with a high-quality inventory to intermediate between different asset classes.

### Functions That Are Still Needed

**1. Matching and market making.**

Someone or something must connect ASPs that need BTC with LPs that have idle BTC. This is a coordination problem. In tradfi, the dealer solves it by being always available -- you call Goldman and they quote you a rate. In a BTC system, this could be a protocol: an order book, an auction mechanism, or a matchmaking service.

The key question is not whether matching is needed (it is) but whether matching requires a balance sheet. It does not. An order book is stateless. A batch auction is stateless. The matching function can be disaggregated from the risk-bearing function.

**2. Liquidity provision and immediacy.**

Dealers provide immediacy. When an ASP needs BTC at 3am UTC to fund a round, the dealer is there. In a peer-to-peer system, the LP may not be online. The ASP may need to borrow at a time when no LP is actively offering.

This is a real constraint. The tradfi solution is the dealer's always-on balance sheet. The Bitcoin-native solutions are:

- **LP pools**: multiple LPs deposit BTC into a pool, and the ASP draws from the pool when needed. This creates a standing facility without requiring any single LP to be online. The pool functions like a credit line.
- **Scheduled auctions**: borrowing and lending match at fixed intervals (hourly, daily). The ASP plans its funding needs around the auction schedule. This sacrifices immediacy for predictability.
- **Bonded market makers**: a protocol participant commits capital (bonded) to always be available, earning a premium for the commitment. This is a dealer in miniature, but the role is protocol-defined and the capital is on-chain, not hidden in a balance sheet.

Each sacrifices something. Pools have utilization risk (what if the pool is fully lent?). Auctions have timing risk (what if you need BTC between auctions?). Bonded market makers reintroduce a form of dealer with its attendant concentration risk.

**3. Information aggregation and price discovery.**

Dealers in tradfi see all the flow. JP Morgan's repo desk knows what every major MMF and hedge fund is doing, in real time. This information advantage lets dealers price risk accurately and provide tight spreads.

Paradoxically, a transparent Bitcoin system might be better at this. If lending and borrowing activity is on-chain or on a public order book, all participants see the same information. There is no information asymmetry to exploit and none to aggregate. The price discovery mechanism is the market itself, not a dealer's private view of it.

The caveat: in early markets with few participants, the "market itself" may be too thin for efficient price discovery. A dozen ASPs and a dozen LPs do not generate the information density that thousands of tradfi counterparties do. In that phase, a dominant market maker (even an informal one) may be necessary to anchor prices.

### The Circular Risk Problem

This is the most important structural issue, and it is specific to Ark.

In the primary use case, the entity borrowing BTC is the ASP. The ASP controls the Ark protocol -- it coordinates rounds, creates VTXO trees, and co-signs cooperative spends. If the ASP borrows BTC from an LP, and the LP's collateral (or the loan's enforcement mechanism) depends on the ASP's cooperation...the lender is trusting the borrower to enforce the loan terms.

This is not a hypothetical concern. In current Ark protocol design:

- The cooperative spending path for VTXOs requires the ASP's co-signature.
- If the ASP is the borrower and goes offline or refuses to cooperate, the lender's recourse requires on-chain enforcement, which means waiting for timelocks to expire.
- The ASP could, in theory, create new VTXOs that prioritize its own interests over lenders' claims.

**Breaking the circularity requires one thing: the collateral must be on-chain BTC, held in a script that the ASP cannot unilaterally control.** The escrow script must be a 2-of-2 multisig (LP + ASP), or a script with a timelock that allows the LP to claim after expiry, or both. The critical requirement is that the ASP's cooperation is not needed for the LP to recover funds in a default scenario. This means the collateral cannot be VTXOs (which require ASP cooperation) -- it must be base-layer BTC locked in a script that is independent of the Ark protocol.

This constraint is consistent with the findings in `constraints.md`: VTXOs cannot directly serve as repo collateral in the current protocol design.

---

## Part 3: A Bitcoin-Native Alternative to Dealer Balance Sheets

The claim is that the dealer's functions can be decomposed and replaced by protocol-native mechanisms in a BTC-for-BTC system. Here is each function mapped to its Bitcoin-native alternative, with an honest assessment of what is gained and lost.

| Dealer Function | TradFi Implementation | Bitcoin-Native Alternative | Gained | Lost |
|----------------|----------------------|---------------------------|--------|------|
| **Matching** | Dealer desk (voice, electronic) | Order book, batch auction, or matchmaking protocol | Transparency; no information asymmetry; no dealer markup | Immediacy; the dealer can match any time, an auction runs on a schedule |
| **Maturity transformation** | Dealer balance sheet absorbs overnight-to-term mismatch | Fixed-term contracts aligned to VTXO expiry; no transformation needed | Eliminates rollover risk; no dependence on short-term funding markets | Flexibility; tradfi borrowers can get custom tenors, BTC borrowers get fixed terms |
| **Counterparty risk absorption** | Dealer stands between both sides; absorbs default losses | On-chain escrow (multisig, timelock, HTLC) enforces collateral claims | No credit risk to evaluate; enforcement is deterministic; no dealer solvency risk | Dispute resolution speed; on-chain enforcement can take hours/days vs. instant dealer action |
| **Collateral transformation** | Dealer accepts low-quality collateral, posts high-quality | Not needed -- same-asset system (BTC for BTC) | No collateral quality disputes; no haircut complexity | Nothing meaningful is lost in a same-asset system |
| **Collateral management** | Triparty agent (BNY) handles selection, valuation, margining | Script/multisig with on-chain verification | Removes custodial dependency on a single agent; auditable by anyone | Operational simplicity; BNY handles everything, on-chain requires LP monitoring |
| **Price discovery** | Dealer spread (opaque, information-advantaged) | Auction mechanism or transparent order book | All participants see the same information; no dealer information rent | Anchoring in thin markets; early markets may have volatile or unreliable price signals |
| **Liquidity provision** | Always-on dealer balance sheet | LP pool, scheduled auction, or bonded market maker | No single point of failure; no concentration in a few dealers | Guaranteed immediacy; no one is contractually obligated to always provide liquidity |

### The Honest Assessment

The Bitcoin-native approach eliminates three of the dealer's four core functions entirely (maturity transformation, counterparty risk, collateral transformation) and replaces the fourth (matching/liquidity provision) with protocol mechanisms that trade immediacy for transparency and decentralization.

What is gained is substantial:

- **No regulatory bottleneck.** Dealer balance sheets are finite and regulation-constrained. A protocol-based system has no equivalent of the leverage ratio. Capacity scales with participant count, not with any institution's balance sheet.
- **No Pozsar gap.** The structural mismatch between institutional cash pools and dealer capacity does not arise. There is no fixed intermediation capacity that fails to grow with demand.
- **No quarter-end volatility.** No reporting dates, no window dressing, no capacity withdrawal at predictable intervals.
- **No single-entity risk.** In tradfi repo, the failure of a major dealer (Lehman, Bear Stearns) freezes the entire market. In a protocol-based system, individual LP departure reduces capacity but does not break the mechanism.

What is lost is also substantial:

- **Immediacy.** A dealer-less system cannot guarantee that liquidity is available at any given moment. The ASP may need to plan its funding around auction schedules or pool availability rather than calling a desk and getting a quote in seconds.
- **Elasticity.** Dealer balance sheets can temporarily expand to absorb stress (the dealer takes a loss on leverage ratio to keep the market functioning). A protocol-based system has no entity with the incentive or ability to provide emergency capacity.
- **Implicit backstop.** In extremis, the Fed can lend directly to dealers through the discount window or standing repo facility. There is no equivalent sovereign backstop for a Bitcoin lending protocol. If the protocol seizes, there is no lender of last resort.
- **Relationship management.** Dealers manage long-term relationships with both sides. They extend capacity to valued clients during stress, call in favors, and exercise judgment that a protocol cannot. In a nascent market, these relationships may be more important than protocol efficiency.

---

## Devil's Advocate: The Case for Dealers Even in BTC-for-BTC

The analysis above may be too optimistic about eliminating dealers. Consider:

**Nascent market dynamics.** The entire Ark ecosystem as of March 2026 consists of a handful of ASPs, most in beta or pre-production. The total addressable market for ASP liquidity is measured in tens or hundreds of millions of dollars at best. At this scale, a peer-to-peer protocol is solving a problem that does not yet exist at sufficient scale to justify the protocol's complexity. A single well-capitalized entity (an exchange, a fund, a consortium) lending BTC to ASPs under bilateral agreements is simpler, faster to deploy, and adequate for the current market size.

**The cold start problem.** A lending protocol needs both borrowers and lenders. ASPs are the borrowers, but who are the lenders? Long-term holders who want yield on idle BTC. These holders already have options: they can lend on centralized platforms, provide Lightning liquidity, or simply hold. A new protocol must offer rates that compete with these alternatives while also being unfamiliar, unproven, and likely less liquid. The cold start problem -- needing liquidity to attract liquidity -- is exactly the problem dealers solve by committing their own capital as the first LP.

**Information asymmetry persists.** The analysis assumed that on-chain transparency eliminates information asymmetry. This is only partially true. On-chain data shows collateral positions and escrow states, but it does not show the borrower's off-chain obligations, other lending relationships, operational health, or likelihood of meeting VTXO expiry obligations. An ASP might be borrowing from multiple LPs against the same effective economic position, creating correlated default risk that no on-chain view reveals. A dealer who sees all the flow -- or a credit rating agency equivalent -- might still be needed to aggregate this information.

**Timing mismatches are real.** An ASP needs to fund a round in the next 60 minutes. No LP is currently offering a matching term at an acceptable rate. In tradfi, the dealer bridges this gap by lending from its own book and finding an offsetting trade later. In a dealer-less system, the ASP either pays a punitive rate, delays the round, or fails to serve its users. The cost of this friction falls on Ark's end users, who experience delayed or failed transactions.

**The likely path: centralized first, decentralize later.** Early-stage Bitcoin repo probably looks like this: ASPs borrow from a known set of LPs (exchanges, funds, early supporters) under bilateral or semi-structured agreements, with on-chain escrow for collateral. This is, functionally, a dealer model where the "dealer" is the ASP itself or a small consortium. The decentralized protocol -- order books, auctions, LP pools -- is the end state, not the starting state. Attempting to build the decentralized version before there is sufficient demand is premature optimization.

The honest answer may be that the dealer function is not eliminated -- it is compressed. In tradfi, the dealer is a massive institution with a $2 trillion balance sheet. In BTC repo, the "dealer" might be a protocol-defined role with bonded capital, transparent pricing, and on-chain enforcement. The function persists; the implementation changes. Whether that change is enough to avoid the capacity constraints and systemic risks of tradfi repo is the open question.

---

## Sources

### Dealer Balance Sheets and Repo Mechanics
- Pozsar, Z. (2014). "Shadow Banking: The Money View." Office of Financial Research Working Paper 14-04.
- Pozsar, Z. (2011). "Institutional Cash Pools and the Triffin Dilemma of the U.S. Banking System." IMF Working Paper WP/11/190.
- Copeland, A., Martin, A., & Walker, M. (2014). "Repo Runs: Evidence from the Tri-Party Repo Market." Journal of Finance, 69(6).
- Baklanova, V., Copeland, A., & McCaughrin, R. (2015). "Reference Guide to U.S. Repo and Securities Lending Markets." Federal Reserve Bank of New York Staff Report 740.
- Duffie, D. (2020). "Still the World's Safe Haven? Redesigning the U.S. Treasury Market After the COVID-19 Crisis." Hutchins Center Working Paper 62.
- TBAC (Treasury Borrowing Advisory Committee). Various quarterly reports on dealer capacity and Treasury market structure.
- BIS (2017). "Repo market functioning." CGFS Papers No. 59.

### Regulatory Framework
- Basel Committee on Banking Supervision (2014). "Basel III leverage ratio framework and disclosure requirements."
- Federal Reserve (2014). "Enhanced Supplementary Leverage Ratio Standards." Final Rule.
- Tarullo, D. (2019). "Financial Regulation: Still Unsettled a Decade After the Crisis." Journal of Economic Perspectives, 33(1).

### Market Events
- Anbil, S., Anderson, A., & Senyuz, Z. (2020). "What Happened in Money Markets in September 2019?" FEDS Notes.
- Duffie, D. (2020). "Prone to Fail: The Pre-pandemic Financial System." Remarks for the Federal Reserve Bank of New York.
- He, Z., Nagel, S., & Song, Z. (2022). "Treasury Inconvenience Yields during the COVID-19 Crisis." Journal of Financial Economics, 143(1).

### Fed Facilities
- Federal Reserve Bank of New York. "Overnight Reverse Repurchase Agreement Facility." Operational details and daily data.
- Logan, L. (2022). "The Federal Reserve's Market Functioning Purchases." Remarks at Brookings.

### Ark Protocol
- Ark Protocol documentation: https://ark-protocol.org/
- Ark Labs blog: "Understanding Ark Liquidity Requirements." https://blog.arklabs.xyz/liquidity-requirements/
- Second documentation: https://docs.second.tech/
- Lightning Pool (batch auction precedent): https://lightning.engineering/pool/

### Bitcoin Lending and DeFi Precedents
- Lightning Pool by Lightning Labs -- batch auction mechanism for channel liquidity.
- Bisq -- decentralized exchange as precedent for peer-to-peer BTC trading without intermediaries.
- DLC (Discreet Log Contracts) -- oracle-based conditional payments as precedent for on-chain escrow mechanisms.

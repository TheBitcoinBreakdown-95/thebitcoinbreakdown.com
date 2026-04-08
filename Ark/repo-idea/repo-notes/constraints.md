# Constraints Analysis: Ark Protocol Repo Market

Go/no-go gate document. Every constraint is assessed for severity and workaround feasibility. If the aggregate picture says "this won't work," this document says so.

---

## Section 1: Protocol Constraints

### 1. Can VTXOs Be Used as Collateral?

**The constraint:** A VTXO's spending script is fixed: `(user + ASP) cooperative OR (user alone after timeout)`. There is no third spending path. A lender cannot be added to this script without protocol-level changes.

**Why it matters for repo:** In traditional repo, the cash lender takes legal title to the collateral. If the borrower defaults, the lender can liquidate the collateral immediately -- that right is what makes repo work. In an Ark repo, the lender would need a credible claim on the VTXO. But the VTXO script only recognizes two parties: the user and the ASP. A third party (lender) has no on-chain claim. The lender cannot unilaterally seize, spend, or exit the VTXO.

**Pre-signed transaction chains cannot help.** A user could pre-sign a transaction spending their VTXO to the lender, but this requires ASP cooperation (the cooperative path is 2-of-2 MuSig2). The ASP would need to co-sign a transaction that transfers the VTXO to the lender. This is possible operationally but introduces two problems: (a) the ASP must be a willing participant in every collateral transfer, and (b) the pre-signed transaction is only valid if the ASP does not refuse to cooperate. There is no enforcement mechanism if the ASP goes offline or refuses.

**Workaround paths:**

1. **Protocol-level change to VTXO scripts.** Add a third spending condition: `(lender alone after repo_timeout)`. This would require modifications to Ark's leaf script template, changes to how covenant trees are constructed, and buy-in from the Ark protocol community and both major implementations (Ark Labs/Arkade and Second/Bark). Feasibility: technically possible but socially and politically difficult. No one has proposed it. Timeline: 1-2 years minimum if started today.

2. **ASP acts as escrow.** The ASP holds the VTXO and agrees to transfer it to the lender on default. This works operationally but reintroduces custodial trust. The lender must trust the ASP to honor the escrow agreement. If the ASP is also the borrower (the central use case -- ASPs borrowing to fund operations), this creates a fatal circular dependency: the borrower is also the escrow agent for its own collateral.

3. **External escrow layer.** A separate smart contract or multisig arrangement holds collateral outside Ark. The borrower exits VTXOs to an on-chain escrow (multisig between borrower and lender, or a script with timeout conditions). This works but defeats much of Ark's purpose -- you are back to on-chain transactions with their costs and delays. The escrow layer adds complexity, on-chain fees for entry/exit, and a 10+ hour unilateral exit delay if using Ark's native exit path.

**Assessment: VTXOs CANNOT directly serve as repo collateral in the current protocol.** The fixed script is the fundamental blocker. Workarounds exist but each introduces significant tradeoffs.

---

### 2. Can VTXOs Move Without ASP Involvement?

**The constraint:** No. The cooperative spending path requires the ASP's co-signature (2-of-2 MuSig2). The only alternative is unilateral exit, which requires broadcasting the entire pre-signed transaction chain on-chain -- multiple transactions, each separated by a ~10-hour CSV delay, each requiring an on-chain fee.

**Why it matters for repo:** Collateral must be transferable. In traditional repo, the lender takes possession of the collateral at trade execution and returns it at maturity. Both legs require the collateral to move. If every collateral movement requires ASP cooperation, then:

- The ASP is a required counterparty to every repo transaction.
- If the ASP goes offline, collateral cannot be transferred to the lender (cooperative path fails) and the lender's only recourse is waiting for the borrower to execute a costly, slow unilateral exit.
- The ASP has veto power over collateral movements. It can refuse to co-sign.

**The circular risk:** The primary use case for this repo market is ASPs borrowing BTC to fund their own operations. If the ASP is both the borrower and the required co-signer for collateral movement, the ASP can refuse to release collateral on default. The lender has no recourse except waiting for the VTXO's absolute timelock to expire (up to 28 days) and hoping the borrower initiates unilateral exit -- which the borrower has no incentive to do if they have defaulted.

**Assessment:** ASP involvement in every VTXO movement creates unacceptable counterparty risk for any repo where the ASP is the borrower. This constraint is less severe when the ASP is not the borrower (e.g., a user borrowing against VTXOs from an external lender), but that is not the primary use case.

---

### 3. What Can Ark Script Enforce?

**Current capabilities:**
- 2-of-2 MuSig2 cooperative spend (user + ASP)
- User-only spend after relative timelock (CSV ~60 blocks / ~10 hours per tree level)
- ASP sweep after absolute timelock expiry (~28 days)
- Revocation branch spend by ASP using aggregated revocation secrets (V2)
- Connector-based atomicity for round participation (forfeit is valid only if round confirms)

**Cannot enforce:**
- Repurchase commitments. There is no script-level mechanism to obligate a party to execute a future transaction. Repo's defining feature -- "I sell you this asset today and commit to buy it back at price X on date Y" -- cannot be encoded in Ark's current script templates.
- Conditional transfers. "Transfer this VTXO to party B if condition C is met" is not expressible. OOR payments are immediate and unconditional.
- Multi-party claims. "This VTXO can be spent by A, B, or C under different conditions" requires more complex scripts than Ark supports.
- Margin calls or partial liquidation. There is no mechanism for a third party to claim a fraction of a VTXO's value.

**Comparison to traditional repo enforcement:** Traditional repo enforcement relies on (a) the legal fiction of a sale (collateral title transfers to the lender), (b) the Bankruptcy Code's Section 559 safe harbor (lender can liquidate immediately on default), and (c) a clearing agent (BNY Mellon, FICC) that manages collateral custody and settlement. None of these have Ark equivalents. The legal fiction requires title transfer (not possible with fixed VTXO scripts). The safe harbor is statutory (no Bitcoin equivalent). The clearing agent is a trusted third party (the ASP is the closest analogue but has the circular-risk problem).

**Assessment:** Ark's scripting capabilities are insufficient for repo enforcement. The protocol was designed for payments, not for financial contracts with conditional execution.

---

### 4. VTXO Expiry as Hard Upper Bound on Repo Tenor

**The constraint:** VTXOs expire in ~28 days (configurable per ASP, could be as short as 14 days). After expiry, the ASP sweeps the on-chain UTXO to reclaim liquidity. An expired VTXO is worthless to the holder.

**Why it matters for repo:** Any repo collateralized by VTXOs must mature before the VTXOs expire. A 28-day VTXO can back a repo of at most ~25 days (leaving a safety margin for settlement). A 14-day VTXO can back at most ~11-12 days.

**The stale collateral problem:** As a VTXO ages, its remaining lifetime shrinks. A VTXO created 20 days ago has only 8 days of remaining life. It can only collateralize a very short-term repo (5-6 days at most). A lender evaluating VTXO collateral must consider not just the amount but the remaining lifetime. Older VTXOs are weaker collateral because:
- Shorter maximum repo tenor
- Higher rollover risk (the repo must be refinanced sooner)
- The borrower must refresh the VTXO before expiry, which requires ASP cooperation and a new round

**Repo rollover and VTXO refresh interaction:** If a repo matures and the borrower wants to roll it (enter a new repo for another term), the underlying VTXO collateral may also need refreshing. Refreshing creates a new VTXO in a new round -- the old collateral ceases to exist and new collateral must be pledged. This means every repo rollover potentially requires a collateral substitution, adding operational complexity.

**Assessment:** The 28-day expiry imposes a hard ceiling on repo tenor and creates a degrading-collateral dynamic that has no equivalent in traditional repo (Treasuries do not expire). This is a significant but not fatal constraint -- overnight and 1-2 week repos are viable within this window. Longer-term funding requires rolling repos, which is standard practice in traditional markets (70-80% of Treasury repo is overnight).

---

### 5. V2 Revocation: Does It Enable Conditional Claims?

**How V2 revocation works:** Each VTXO holder has a per-VTXO revocation secret. When a user spends a VTXO, they reveal the secret to the ASP. Once enough secrets in a shared UTXO tree are revealed, the ASP aggregates them (`sec1 + sec2 + ... + secN`) to unlock the revocation branch, reclaiming the corresponding capital immediately rather than waiting for expiry.

**Could a lender hold revocation secrets as collateral?** This is the most interesting V2 angle for repo. If the borrower reveals their revocation secret to the lender instead of (or in addition to) the ASP, the lender holds a piece of the information needed to reclaim the underlying BTC. However:

- The revocation branch pays to the **ASP**, not to a third party. Even if the lender holds the secret, the funds flow to the ASP when the revocation branch is exercised. The lender does not receive the BTC directly.
- Revocation requires aggregation of multiple secrets from multiple VTXO holders in the same tree. A single user's revocation secret is necessary but not sufficient. The lender cannot unilaterally trigger revocation.
- If the ASP is the borrower and the lender holds the borrower's revocation secret, the lender could theoretically withhold the secret to prevent the ASP from reclaiming that portion of locked capital. This is a weak form of leverage -- the lender cannot seize collateral, but can deny the borrower early capital recovery. The practical impact is limited because the ASP still recovers the capital at expiry.

**Assessment:** V2 revocation does not enable conditional claims by third parties. The revocation branch is ASP-specific by design. Revocation secrets provide a marginal information asymmetry that could be leveraged in a bilateral agreement, but they do not constitute a claim on the underlying BTC.

---

### 6. Can Repo Settlement Happen Over Lightning or OOR?

**OOR (Out-of-Round) payments:** Instant, off-chain transfers between Ark users on the same ASP. The receiver must trust that the sender and ASP do not collude to double-spend until the next round refresh.

**Lightning integration:** Ark supports HTLC-based interop with Lightning. Users can pay Lightning invoices from Ark VTXOs and receive Lightning payments into Ark.

**For the cash leg of repo (disbursement and repayment):**
- OOR payments are viable for same-ASP transactions. The borrower receives BTC instantly. However, the trust assumption (sender+ASP collusion risk until refresh) is problematic when the ASP is the borrower -- the lender would need to trust the ASP not to double-spend, which is exactly the trust the repo is supposed to avoid.
- Lightning payments work for cross-system settlement. The lender sends BTC via Lightning, the borrower receives into Ark. Repayment flows the other direction. This adds the ASP's Lightning node liquidity as a dependency and introduces routing fees, but is operationally sound.

**For the collateral leg of repo (VTXO transfer to lender):**
- OOR payments cannot serve as collateral transfer because they are unconditional. Once transferred, the lender holds the VTXO outright -- there is no mechanism for automatic return at maturity.
- There is no conditional or time-locked OOR payment. You cannot say "this VTXO transfers to the lender now, but reverts to the borrower at maturity unless the lender claims it."

**Assessment:** Lightning and OOR are viable for the cash leg of repo but not for the collateral leg. The collateral transfer problem remains unsolved within Ark's current capabilities.

---

### 7. Atomicity: Can Repo + VTXO Transfer Be Made Trustless?

**The requirement:** A true repo requires atomicity -- the cash leg and the collateral leg must settle simultaneously. The borrower should not be able to receive cash without surrendering collateral, and vice versa.

**Current Ark capabilities:** Ark's connector mechanism provides atomicity for round participation (forfeit is valid only if the round confirms). This is a specific form of atomicity designed for the refresh use case, not for arbitrary conditional transfers.

**HTLCs:** Ark supports HTLCs for Lightning integration. HTLCs provide hash-time-locked conditional payments -- "pay X if you reveal preimage H within T blocks." This is a form of conditional atomicity. Could HTLC-like mechanics be adapted for repo?

- In theory, the cash leg could be an HTLC: "lender pays borrower X BTC, conditional on the borrower revealing a preimage that also triggers the collateral transfer." But the collateral transfer (VTXO to lender) cannot be conditioned on a hash preimage in the current protocol. There is no HTLC-like mechanism for VTXO ownership transfer.
- Cross-system atomicity (cash on Lightning, collateral on Ark) would require a bridge protocol. Submarine swaps achieve this for Lightning-to-on-chain, but no equivalent exists for Lightning-to-Ark-VTXO.

**Assessment:** Trustless atomic repo settlement is not possible with current Ark protocol capabilities. Any repo structure would require at least one party to move first, creating counterparty risk during the settlement window. HTLCs provide a partial path but cannot currently condition VTXO ownership transfers.

---

## Section 2: Structural Constraints (Five Pillars at Ark Scale)

**Critical reframe: BTC-for-BTC changes everything.** The analysis below was originally written assuming dollar-denominated repo (lend dollars, receive BTC collateral). If the system is purely BTC-for-BTC -- lend BTC, receive BTC collateral -- three of the five pillars largely dissolve:

- **Haircuts** exist to protect against collateral losing value *relative to the loan denomination*. In same-asset repo, there is no FX risk. Haircuts drop from 10-20% to ~1-3% (covering only execution/liquidity risk).
- **Mark-to-market and margin calls** are irrelevant when collateral and loan are the same asset.
- **Fire sale cascades** require a price spiral between collateral and loan denomination. In BTC-for-BTC, the collateral IS the loan -- no spiral possible (assuming no rehypothecation).
- **Elastic supply** is only needed when creating credit denominated in one asset backed by another. BTC-for-BTC just moves existing BTC from lender to borrower for a term -- no credit creation.
- **Dealer intermediation** is partially eliminated because three of the dealer's core functions (maturity transformation, counterparty risk absorption, collateral transformation) don't apply in a same-asset, fixed-term, escrow-backed system. See `dealer-balance-sheets.md` for the full analysis.

The assessments below evaluate each pillar twice: once in the dollar-denominated framing (original analysis) and once in the BTC-for-BTC framing (revised).

### 1. Collateral Quality Gap

**The systemic-scale problem:** Bitcoin gets 10-20%+ haircuts in traditional repo markets, compared to 0-2% for U.S. Treasuries. BTC's daily volatility of 3-5% and tail risk of 20%+ moves in a week make it inherently lower-quality collateral. The haircut spiral (Gorton and Metrick) would be more vicious with BTC: a 30% price drop forces massive additional collateral posting, which forces liquidations, which drives the price down further.

**At Ark scale ($10M-$1B):**

The math that matters: is borrowing with a high haircut cheaper than the alternative (locking up your own capital)?

Consider a medium ASP with $26M locked under V2 (50% spend rate). The ASP has $13M of its own capital and needs $13M externally.

- **Option A: Self-fund.** The ASP needs $26M total. Opportunity cost at 5% = $1.3M/year. Fee revenue at 0.3% on $10M/week = $1.56M/year. Net margin: $260K.
- **Option B: Borrow via repo at 80% LTV (20% haircut).** The ASP posts $16.25M in BTC collateral to borrow $13M. The $16.25M collateral is BTC the ASP expects to reclaim from expiring VTXOs. Borrowing cost at 6% = $780K/year. But the ASP only needs $13M of its own capital instead of $26M. Return on own capital: ($1.56M - $780K) / $13M = 6.0%. This is double the self-funded return.
- **Option C: Borrow at 70% LTV (30% haircut).** Post $18.57M collateral for $13M. Same borrowing cost. Same return improvement. The haircut increases the collateral requirement but does not change the cash borrowed.

The haircut is painful but the leverage effect improves capital returns. The critical question is whether the ASP has $16-19M in BTC it can post as collateral. This BTC would need to come from somewhere other than the VTXOs it is trying to fund (those VTXOs are the reason it needs to borrow in the first place). The ASP could post:
- BTC in its on-chain reserves (but if it had excess BTC, it would not need to borrow)
- BTC expected from near-term VTXO expirations (forward claim on future BTC -- hard to collateralize)
- BTC from a separate pool (Lightning channel balances, treasury)

**Verdict (dollar-denominated):** The haircut is painful but not fatal. The leverage benefit outweighs the haircut cost for an ASP that can source collateral. The real constraint is the collateral source -- the ASP's primary asset (locked VTXOs) cannot easily serve as repo collateral (see Section 1). At Ark's operating scale, a 20-30% haircut on BTC is manageable if the ASP has diversified BTC holdings across Ark, Lightning, and on-chain reserves.

**Verdict (BTC-for-BTC):** Haircuts drop to ~1-3%, covering only execution risk (on-chain fee spikes, mempool congestion during collateral liquidation). No FX risk between collateral and loan. This is comparable to zero-haircut bilateral Treasury repo where counterparties trust each other. The economics improve dramatically: at 2% haircut, the ASP posts $13.27M to borrow $13M, vs $16.25M at 20% haircut. **Not a constraint in the BTC-for-BTC framing.**

---

### 2. No Clearing Infrastructure

**The systemic-scale problem:** Traditional repo relies on BNY Mellon (triparty), FICC (central clearing), and Fedwire (settlement). These institutions process over $4 trillion daily in cleared repo. They handle collateral selection, daily mark-to-market, margin management, netting, and default management. Nothing equivalent exists for Bitcoin.

**At Ark scale ($10M-$1B):**

The question is whether a smart contract or multisig can substitute for institutional clearing at this scale.

- **Term Finance operates without institutional clearing.** It uses smart contracts for collateral management, sealed-bid auctions for price discovery, and automated liquidation for default management. TVL ~$50M. This is proof that contract-based clearing works at the low end of institutional scale.
- **Solstice/Cor Prime executed true repo on-chain** using Membrane Labs for settlement infrastructure. Bilateral, institutional, but functional without BNY Mellon.
- **A multisig between borrower and lender** (2-of-3 with an arbiter, or 2-of-2 with timelock) can handle bilateral settlement for individual repos. This does not scale to a market with many participants, but at Ark's early scale (3-10 ASPs), bilateral arrangements may suffice.

**The ASP as clearing agent:** If the ASP also serves as the clearing agent for its own repos, we have circular risk again. The ASP manages the collateral it posted. A separate entity (another ASP, a federation member, or a dedicated clearing service) would need to serve this role. At early scale, the lender itself can serve as clearing agent for bilateral repos.

**Verdict (dollar-denominated):** Manageable at Ark's operating scale. Smart contracts (for automated collateral management and liquidation) and bilateral arrangements (for early-stage markets) can substitute for institutional clearing. This becomes a scaling constraint above $1B but is not a blocker at the $10M-$100M level.

**Verdict (BTC-for-BTC):** Even simpler. A clearing agent's core functions (daily mark-to-market, margin management, collateral optimization) are unnecessary when collateral and loan are the same asset. The remaining function -- custody and settlement -- is handled by on-chain escrow (timelocked multisig or HTLC). A script replaces an institution. **Effectively eliminated as a constraint in the BTC-for-BTC framing.**

---

### 3. No Central Bank Backstop

**The systemic-scale problem:** When the Treasury repo market froze in March 2020, the Fed injected $1.5 trillion in repo in two days and ultimately purchased $1.6 trillion in Treasuries. When the UK gilt repo market spiraled in September 2022, the Bank of England committed GBP 65 billion in gilt purchases. Bitcoin has no lender of last resort. The protocol cannot create emergency liquidity. A Bitcoin repo market that freezes stays frozen.

**At Ark scale ($10M-$1B):**

Blast radius analysis. If one ASP defaults on a $5M repo:
- The lender loses $5M (minus whatever collateral they can recover).
- If the lender is a BTC fund or institution, $5M is a loss but not existential for any entity large enough to be lending at that scale.
- Other ASPs are not directly affected unless they share a lender (contagion through the lender side).
- Ark users of the defaulting ASP can still unilaterally exit (their VTXOs are unaffected by the ASP's repo obligations, since the repo collateral is separate from user VTXOs -- or should be, by design).
- No systemic risk to Bitcoin or the broader financial system.

**Protocol-level liquidation substitute:** If collateral is held in an on-chain escrow (the workaround from Section 1, constraint 1), the lender can liquidate by broadcasting the escrow transaction and selling the BTC on the open market. This is slower than the Fed's facilities (on-chain settlement vs. intraday) but functional. The key is that BTC collateral is always liquid -- unlike structured products in 2008, BTC can always be sold at some price.

**Verdict (dollar-denominated):** Real risk but contained blast radius at this scale. The absence of a backstop means individual repo failures are fully absorbed by the counterparties, not socialized. This is actually a feature in a small market -- it enforces discipline. It becomes a systemic concern only if Ark repo grows to a scale where multiple ASP defaults could cascade (unlikely before 2030+).

**Verdict (BTC-for-BTC):** The backstop concern is further reduced. Traditional repo runs happen because collateral loses value relative to the loan (MBS in 2008, gilts in 2022), triggering haircut spirals and fire sales. In same-asset repo, this dynamic cannot occur -- the collateral cannot devalue against the loan denomination. If rehypothecation is prohibited (each BTC escrowed against exactly one loan), there is no cascade mechanism. A lender who refuses to roll simply claims their escrowed BTC. No run, no spiral, no fire sale. **Largely eliminated as a constraint in the BTC-for-BTC framing, assuming no rehypothecation.**

---

### 4. Inelastic Supply

**The systemic-scale problem:** BTC supply is capped at 21 million. Traditional repo collateral (Treasuries) is issued at scale -- $25 trillion outstanding, with regular new issuance. When the market needs more collateral, the Treasury can issue more. BTC cannot expand supply in response to demand.

**At Ark scale ($10M-$1B):**

A medium ASP needs ~$13M in external BTC funding. At $85K/BTC, that is ~153 BTC. Total BTC market cap exceeds $1.7 trillion. Circulating supply is ~19.8 million BTC. Even the most constrained measure -- BTC on exchanges (~2.5 million BTC) -- dwarfs a single ASP's needs by four orders of magnitude.

Even at the stablecoin-scaled scenario ($1-13B+), the BTC supply is not a binding constraint. The entire repo market would consume at most a few percent of available BTC float.

**Verdict (both framings):** Not a binding constraint at any foreseeable Ark scale. BTC supply inelasticity is a macroeconomic concern for a hypothetical future where BTC repo reaches Treasury repo scale ($12 trillion). That is decades away, if ever. In the BTC-for-BTC framing, the elastic currency argument is even weaker: the system isn't creating credit, just moving existing BTC from idle holders to active ASPs for a fixed term. No new BTC needs to be created.

---

### 5. No Dealer Intermediation

**The systemic-scale problem:** In traditional repo, primary dealers sit between cash lenders (money market funds, pension funds) and cash borrowers (hedge funds, banks). Dealers absorb flow imbalances, warehouse risk, and provide continuous two-way markets. There are no Bitcoin repo dealers.

**At Ark scale ($10M-$1B):**

**Can the ASP serve as its own dealer?** If the ASP is the borrower and also the dealer (matching itself with lenders), the circular risk is clear: the ASP sets the terms for its own borrowing. This is analogous to a bank setting its own deposit rates -- functional but creates moral hazard. The ASP has an incentive to offer low rates to lenders and take on excessive leverage.

**Could a separate entity serve the dealer function?** Possible candidates:
- **Lightning liquidity providers** (Amboss Magma operators) already intermediate BTC capital. They could expand to ASP repo.
- **BTC lending platforms** (Ledn, etc.) already match BTC lenders and borrowers. Adding ASP repo as a product is a natural extension.
- **Other ASPs** with excess capital could lend to ASPs with deficits (cross-ASP lending market).
- **A dedicated repo protocol** (like Term Finance but for BTC/Ark) could automate the dealer function through auctions.

**Verdict (dollar-denominated):** The ASP-as-dealer circularity is the real concern here. A viable repo market requires at least one intermediary that is not also a borrower. At early scale, this could be as simple as a single institutional lender (a BTC treasury company or fund) that provides capital to multiple ASPs. The dealer function does not need to be decentralized or automated on day one -- a bilateral relationship between an ASP and a capital provider is sufficient to start.

**Verdict (BTC-for-BTC):** The dealer function is substantially decomposed. Five of seven traditional dealer functions (maturity transformation, counterparty risk absorption, collateral transformation, collateral management, price setting via spread) are either unnecessary or handled by scripts in a same-asset, fixed-term, escrow-backed system. What remains: matching (connecting ASPs with LPs) and liquidity provision (ensuring BTC is available when needed). These can be handled by a protocol (batch auction, order book) rather than an institutional dealer. The circularity concern remains for the matching function -- if only one ASP exists, it is matching with itself. But with 3+ ASPs and independent LPs, the protocol can serve as a neutral matching layer. See `dealer-balance-sheets.md` for the full decomposition. **Reduced from "real concern" to "cold start problem" in the BTC-for-BTC framing.**

---

## Section 3: Go/No-Go Assessment

### What Is Possible Today (Without Protocol Changes)

1. **Off-chain bilateral lending agreements.** An ASP borrows BTC from a capital provider under a standard loan agreement. Collateral is posted on-chain (not as VTXOs, but as regular BTC in a multisig escrow). The loan term is 2-4 weeks, matching VTXO expiry cycles. Repayment comes from reclaimed expired VTXOs. This is not repo in the technical sense -- it is collateralized lending. But it solves the ASP's immediate funding problem.

2. **Lightning-based cash settlement.** Loan disbursement and repayment can flow over Lightning, reducing on-chain costs. The ASP receives BTC via Lightning, uses it for round funding, and repays via Lightning when VTXOs expire.

3. **ASP federation for capital pooling.** Multiple entities contribute BTC to a shared ASP operation, governed by multisig. Not a market -- more like a consortium. But it addresses the capital access problem for smaller operators.

4. **Dynamic fee management.** ASPs adjust fees based on liquidity pressure. Raises the cost of using Ark during liquidity crunches, reducing demand. Survival mechanism, not a growth strategy.

### What Requires Protocol Changes

1. **VTXOs as direct repo collateral.** Requires adding a third spending condition to VTXO leaf scripts (e.g., `lender after repo_timeout`). This is a fundamental protocol change.

2. **Conditional VTXO transfers.** Requires time-locked or hash-locked OOR payments. Would enable trustless collateral legs for repo.

3. **Atomic repo settlement within Ark.** Requires extending Ark's connector mechanism to support arbitrary conditional transactions beyond round participation.

4. **Multi-party VTXO claims.** Requires escrow or shared-ownership VTXO scripts for collateral management.

### The Minimum Viable Path

The minimum viable path does not run through Ark at all for the collateral leg. It runs alongside Ark:

1. **The ASP borrows BTC through a bilateral, off-chain agreement** with a capital provider (institutional lender, BTC treasury company, or dedicated LP).
2. **Collateral is posted on-chain** in a standard 2-of-2 multisig (or 2-of-3 with an arbiter) between the ASP and the lender. This is not a VTXO -- it is regular BTC that the ASP controls outside of Ark.
3. **The loan term matches VTXO expiry** (~14-28 days). The ASP repays from BTC reclaimed when VTXOs expire.
4. **Cash settlement happens over Lightning** or on-chain, depending on amount and urgency.
5. **Interest rate is negotiated bilaterally** or set by a simple auction (Term Finance-style sealed-bid, but off-chain).

This is structurally a collateralized term loan, not a repo. It lacks repo's defining features (title transfer, rehypothecation rights, bankruptcy safe harbor). But it solves the ASP's funding problem today, without protocol changes, and can evolve toward true repo as Ark's scripting capabilities mature.

### Recommendation: Proceed -- Two-Phase Approach

**Phase 1 (buildable today): BTC-for-BTC collateralized term lending alongside Ark.**

The protocol constraints prevent Ark-native repo (VTXOs can't serve as collateral, no atomic settlement, ASP-as-co-signer circularity). But the BTC-for-BTC reframe eliminates most structural constraints:
- Haircuts drop to ~1-3% (execution risk only, no FX risk)
- No clearing agent needed (script handles custody, no mark-to-market required)
- No backstop needed (no fire sale cascade in same-asset system without rehypothecation)
- No dealer needed (matching + liquidity provision handled by protocol/auction)

The minimum viable product:
- Bilateral BTC-for-BTC lending (on-chain BTC escrow, not VTXO collateral)
- Fixed-term, fixed-rate (matching VTXO expiry cycles, 14-28 days)
- Cash settlement via Lightning
- Batch auction for price discovery (Term Finance / Lightning Pool model)
- No rehypothecation (eliminates cascade risk entirely)
- 1-3% haircut covering on-chain execution risk

**Phase 2 (requires protocol evolution): Ark-native repo with VTXO collateral.**

If Ark adopts richer VTXO scripts (via CTV, OP_CAT, or TXHASH), conditional transfers become possible. At that point, the term lending market can upgrade to true repo with VTXO collateral, atomic settlement, and trustless enforcement. This would allow:
- VTXOs as direct collateral (third-party spending conditions in leaf scripts)
- Atomic repo settlement within Ark rounds
- Repo contracts embedded in the Ark protocol itself

**The gap in the Ark community is real:** nobody has proposed a financial-market solution to the ASP liquidity problem. The BTC-for-BTC framing makes this far more viable than previously assessed -- three of five structural constraints dissolve when the system doesn't touch fiat. The remaining constraints (protocol-level VTXO limitations, cold start for matching) are solvable with the two-phase approach.

---

## Sources

All claims in this document are grounded in the prior research files:

- **Ark protocol mechanics:** `ark-v2-mechanics.md`, `bark-implementation.md`
- **Traditional repo:** `traditional-repo.md` (Pozsar, Gorton/Metrick, Singh frameworks)
- **ASP liquidity quantification:** `problem-spec.md` (capital multipliers, V2 scenarios, revenue analysis)
- **DeFi precedents:** `defi-survey.md` (Term Finance, Solstice, Lightning Pool)
- **Existing proposals:** `existing-proposals.md` (V2 revocation, delta reduction, federation, lines of credit)

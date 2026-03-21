# Unit Economics of ASP Working Capital Financing

---

## 1. The ASP's Revenue Model

### How an ASP Earns Money

An ASP collects fees on three activities:

**1. Per-round participation fees (refreshes and in-Ark transfers).** Every time a user's VTXO moves into a new round -- whether from a payment, a refresh, or an onboarding -- the ASP charges a fee. Second's published fee schedule is the only concrete reference: 0% for VTXOs near expiry (incentivizing timely refresh), scaling up to 0.5% for operations on VTXOs with 14+ days remaining. The blended average depends on user behavior, but for modeling purposes, 0.3% is the central estimate used throughout this research series. ([Second fee schedule](https://second.tech/docs/learn/fees))

**2. Out-of-Round (OOR) payment fees.** OOR payments are instant, off-chain transfers between users on the same ASP. These do not require a new round, so the ASP's cost to facilitate them is lower (no on-chain transaction). Fee structure for OOR is not publicly documented by either implementation. It is reasonable to assume OOR fees are lower than round fees -- perhaps 0.1-0.2% -- since the ASP's capital cost per OOR payment is lower (the capital was already committed in a prior round; the OOR just reassigns the claim).

**3. Lightning gateway fees.** When an ASP bridges Ark-to-Lightning payments, it acts as a routing node. It earns standard Lightning routing fees on the Lightning leg. Block's aggressive routing strategy yields up to 9.7% annualized on 184 BTC, but this is an outlier driven by captive Cash App flow. The network median is 0.006% per routed payment (Voltage LINER data), and mid-size operators report 1.5-2% annualized on deployed channel capital. ([Atlas21](https://atlas21.com/lightning-routing-yields-10-annually-blocks-announcement/); [Voltage](https://voltage.cloud/blog/where-does-lightning-network-yield-come-from))

### Fee Revenue Is Proportional to Throughput

Fee revenue scales with transaction volume (throughput), not with locked capital and not with user count directly. An ASP processing $10M/week at 0.3% earns $30K/week regardless of whether that volume comes from 1,000 users making $10K transactions or 100,000 users making $100 transactions. Capital lockup scales with throughput too, but at a different rate (the 4x multiplier under V1, ~2x under V2 at 50% spend rate).

This creates a fixed ratio between revenue and capital:

```
Annual fee revenue = Weekly throughput * Fee rate * 52
Locked capital     = Weekly throughput * Lockup multiplier

ROI = (Throughput * Fee rate * 52) / (Throughput * Lockup multiplier)
    = (Fee rate * 52) / Lockup multiplier
```

The throughput cancels. ROI on locked capital is determined entirely by the fee rate and the lockup multiplier. At 0.3% fee and 2.0x multiplier (V2, 50% spend, 28-day expiry):

```
ROI = (0.003 * 52) / 2.0 = 0.156 / 2.0 = 7.8%
```

At the more conservative 4.0x multiplier (V1):

```
ROI = (0.003 * 52) / 4.0 = 3.9%
```

Note: The problem-spec.md used a simpler calculation (fee revenue / locked capital) that produced 3.0% for V1 and 6.0% for V2. The difference arises from whether the change multiplier (1.3x) is applied to both numerator and denominator or only the denominator. The change multiplier increases capital committed but does not increase fee-generating throughput by the same factor -- change outputs are internal to the ASP, not fee-generating transactions. Correcting for this:

```
V1 ROI = (0.003 * 52) / (4.0 * 1.3) = 0.156 / 5.2 = 3.0%
V2 ROI (50% spend) = (0.003 * 52) / (2.0 * 1.3) = 0.156 / 2.6 = 6.0%
```

This confirms the problem-spec figures. The 1.3x change multiplier is a capital drag: it inflates the denominator without inflating the numerator.

### Realistic Fee Levels: Competitive Comparison

| Payment method | Typical fee | Notes |
|---|---|---|
| On-chain Bitcoin | $1-50+ per tx | Varies with mempool; fixed cost per tx regardless of amount |
| Lightning routing | 0.006% median, up to 0.1% aggressive | Near-zero for standard payments |
| Ark (Second schedule) | 0-0.5%, blended ~0.3% | Tiered by VTXO age |
| Credit card (merchant) | 2-3% | The fee ceiling for merchant payments |
| Stablecoin transfer (Ethereum/Tron) | $1-10 per tx | Fixed cost model |

Ark's 0.3% blended fee is significantly more expensive than Lightning for pure payments. Ark's value proposition is not cheaper payments -- it is simpler onboarding, better privacy, and batch settlement efficiency at scale. For the fee model to sustain, Ark must attract users who value these properties enough to pay 10-50x more than Lightning routing costs.

The viable fee range is **0.2-0.5%** for round operations and **0.1-0.2%** for OOR payments. Below 0.2%, the ASP cannot cover capital costs. Above 0.5%, users migrate to Lightning or on-chain alternatives.

---

## 2. The ASP's Cost Structure

### 2.1 Capital Lockup Cost (Opportunity Cost)

This is the dominant cost. If the ASP has $26M locked (V2, 50% spend, 28-day expiry, medium ASP), that BTC could earn yield elsewhere.

**Competing yield benchmarks for idle BTC (March 2026):**

| Alternative | Annual yield | Risk profile | Source |
|---|---|---|---|
| Lightning routing (network median) | 1.2-1.7% | Operational (uptime, channel mgmt, force-close) | [Voltage LINER data](https://voltage.cloud/blog/where-does-lightning-network-yield-come-from) |
| Lightning routing (aggressive, Block-style) | 5-10% | Captive flow dependency, fee sensitivity | [Atlas21](https://atlas21.com/lightning-routing-yields-10-annually-blocks-announcement/) |
| Amboss Magma liquidity leasing (median) | 2.6% | Counterparty, channel closure | [Second yield survey](https://blog.second.tech/survey-of-bitcoin-yield/) |
| CeFi lending -- Ledn (< 0.5 BTC tier) | 5.25% | Counterparty (platform solvency) | [Ledn](https://www.ledn.io/post/bitcoin-loan-rates) |
| CeFi lending -- Ledn (> 0.5 BTC tier) | 2% | Counterparty (platform solvency) | [Ledn](https://www.ledn.io/post/bitcoin-loan-rates) |
| DeFi lending (Aave/Compound, wBTC) | 1-4% variable | Smart contract, bridge, depegging | [DeFiRate](https://defirate.com/lend/) |
| Babylon BTC staking | Not yet yielding real returns | Protocol, slashing | [Babylon Labs](https://babylonlabs.io/) |
| Holding BTC (appreciation only) | 0% yield | Price volatility | N/A |

**Selecting the opportunity cost:** The relevant benchmark is not the highest available yield but the *risk-adjusted yield accessible at the ASP's scale*. An ASP with 260 BTC ($26M) cannot earn 5.25% on Ledn -- that rate applies to balances under 0.5 BTC. At institutional scale, the realistic alternatives are:

- Ledn at the institutional tier: ~2% APY
- Lightning routing (median): ~1.5% annualized
- Magma leasing: ~2.6% APR

The best realistic alternative for institutional BTC holders is approximately **2-3% annualized**. Using 3% as the opportunity cost:

```
Opportunity cost = $26M * 3% = $780K/year
```

If we use a more aggressive 5% (assuming the ASP could achieve Block-style Lightning returns or access smaller-balance CeFi tiers through splitting):

```
Opportunity cost = $26M * 5% = $1.3M/year
```

### 2.2 On-Chain Transaction Costs

Each Ark round requires at least one on-chain commitment transaction. The cost depends on Bitcoin mempool fee rates and the transaction size (number of inputs/outputs in the covenant tree).

Assumptions:
- Round frequency: 1 per hour = 24/day = 8,736/year
- Average on-chain fee per round transaction: varies wildly

| Mempool fee rate (sat/vB) | Est. round tx cost | Annual cost (8,736 rounds) |
|---|---|---|
| 5 (low) | ~$5 | $43,680 |
| 20 (moderate) | ~$20 | $174,720 |
| 50 (elevated) | ~$50 | $436,800 |
| 100+ (spike) | ~$100+ | $873,600+ |

At moderate fee rates, on-chain costs are ~$175K/year -- roughly 11% of the $1.56M annual fee revenue for the medium ASP. During fee spikes, this rises dramatically. The ASP can mitigate by reducing round frequency during high-fee periods (batching more transactions per round), but this degrades user experience.

**Assumption for modeling: $200K/year** (moderate fees with occasional spikes, some round frequency adjustment).

### 2.3 Infrastructure Costs

Server, bandwidth, monitoring, software maintenance, security:

| Component | Monthly estimate | Annual |
|---|---|---|
| Dedicated server (high-availability) | $500-2,000 | $6K-24K |
| Bandwidth (serving rounds, OOR relay) | $200-500 | $2.4K-6K |
| Monitoring and alerting | $100-300 | $1.2K-3.6K |
| Security audit (amortized) | $500-2,000 | $6K-24K |
| Development/maintenance labor | $5,000-20,000 | $60K-240K |

**Assumption for modeling: $100K/year** for a lean operation, $300K/year for a professionally staffed one. Using $150K as the base case.

### 2.4 Lightning Channel Costs (If Dual-Stack)

If the ASP also operates Lightning nodes for gateway service:
- Channel opening/closing fees: $50-500 per channel depending on fee rates
- Rebalancing costs: typically 0.1-0.5% of rebalanced volume
- Additional capital locked in channels

These costs are partially offset by Lightning routing revenue. For modeling, we treat the Lightning operation as roughly break-even or slightly positive, contributing to the ASP's revenue through gateway fees rather than adding to costs. Net Lightning contribution: **+$0 to +$50K/year** (conservative).

### 2.5 Cost Summary

| Cost component | Annual (medium ASP) |
|---|---|
| Opportunity cost on $26M locked (at 3%) | $780K |
| On-chain transaction costs | $200K |
| Infrastructure | $150K |
| Lightning (net) | $0 |
| **Total operating costs** | **$1.13M** |

Against $1.56M in fee revenue, this leaves a **net margin of $430K**, or **1.7% return on $26M locked capital**.

If opportunity cost is 5% instead of 3%:

```
Total costs = $1.3M + $200K + $150K = $1.65M
Net margin = $1.56M - $1.65M = -$90K (loss)
```

The ASP is unprofitable if the opportunity cost of its own capital exceeds ~4.6%.

---

## 3. Unit Economics: Does External Financing Make Sense?

### Base Parameters

| Parameter | Value |
|---|---|
| Weekly throughput | $10M |
| Blended fee rate | 0.3% |
| Annual fee revenue | $1.56M |
| Locked capital (V2, 50% spend, 28-day) | $26M |
| On-chain + infrastructure costs | $350K/year |
| Opportunity cost rate for own BTC | 3% |

### Scenario A: Self-Funded ASP

The ASP commits $26M of its own BTC.

```
Revenue:           $1.56M
Operating costs:   $350K
Opportunity cost:  $26M * 3% = $780K
Total costs:       $1.13M
Net profit:        $430K
ROI on own capital: $430K / $26M = 1.7%
Gross ROI:         $1.56M / $26M = 6.0%
```

The 1.7% net ROI is worse than passive Magma leasing (2.6%) and barely above the Ledn institutional rate (2%). The ASP is destroying value relative to simpler alternatives unless its operator either (a) has a strategic reason beyond pure yield (protocol development, ecosystem control, stablecoin issuance), or (b) can push the blended fee rate above 0.3%.

**Break-even fee rate (self-funded):**

```
Break-even: Revenue = Costs
Throughput * fee * 52 = $350K + $26M * 3%
$520M * fee = $1.13M
fee = 0.217%
```

At 0.22%, the ASP breaks even. Below that, it loses money. At 0.3%, the margin is thin. At 0.5%, the math improves:

```
Revenue at 0.5%: $520M * 0.005 = $2.6M
Net profit: $2.6M - $1.13M = $1.47M
ROI: $1.47M / $26M = 5.65%
```

At 0.5% fees, the ASP earns a respectable return. The question is whether users will pay 0.5% when Lightning is available at 0.01%.

### Scenario B: Partially Externally Funded ASP

The ASP has $13M own BTC, borrows $13M.

**What rate would the ASP pay to borrow?** The lender's alternative yield benchmarks (Section 5 below) suggest 3-5% is the minimum to attract capital. Use 5% as the borrowing rate.

```
Revenue:                $1.56M
Operating costs:        $350K
Opportunity cost:       $13M * 3% = $390K
Borrowing cost:         $13M * 5% = $650K
Total costs:            $1.39M
Net profit:             $170K
ROI on own capital:     $170K / $13M = 1.3%
```

The leverage effect is *negative* at these rates. The ASP's gross yield on deployed capital (6.0%) minus the borrowing rate (5.0%) leaves only 1.0% spread on the borrowed portion. After operating costs, the ROI on own capital (1.3%) is lower than the self-funded scenario (1.7%) because operating costs are spread across less own capital.

**When does leverage help?** Only when the borrowing rate is below the ASP's gross yield minus operating costs allocated to the borrowed portion:

```
Gross yield on capital:     6.0%
Operating costs per $ deployed: $350K / $26M = 1.35%
Net yield before capital cost:  6.0% - 1.35% = 4.65%
```

Borrowing makes sense only if the rate is below **4.65%**. At 5%, borrowing destroys value. At 4%, it creates marginal value:

```
Borrowing at 4%:
Borrowing cost:         $13M * 4% = $520K
Total costs:            $350K + $390K + $520K = $1.26M
Net profit:             $300K
ROI on own capital:     $300K / $13M = 2.3%
```

Better than self-funded (1.7%) but still barely competitive with passive alternatives.

**At 0.5% fee rate:**

```
Revenue:                $2.6M
Operating costs:        $350K
Opportunity cost:       $13M * 3% = $390K
Borrowing cost (at 4%): $13M * 4% = $520K
Total costs:            $1.26M
Net profit:             $1.34M
ROI on own capital:     $1.34M / $13M = 10.3%
```

Now leverage works powerfully. The 0.5% fee rate creates enough spread for borrowing to amplify returns.

### Scenario C: Minimally Capitalized ASP

The ASP has $5M own BTC, borrows $21M at 4%.

```
At 0.3% fee:
Revenue:                $1.56M
Operating costs:        $350K
Opportunity cost:       $5M * 3% = $150K
Borrowing cost:         $21M * 4% = $840K
Total costs:            $1.34M
Net profit:             $220K
ROI on own capital:     $220K / $5M = 4.4%
```

```
At 0.5% fee:
Revenue:                $2.6M
Operating costs:        $350K
Opportunity cost:       $5M * 3% = $150K
Borrowing cost:         $21M * 4% = $840K
Total costs:            $1.34M
Net profit:             $1.26M
ROI on own capital:     $1.26M / $5M = 25.2%
```

High leverage amplifies both directions. At 0.3%, the minimally capitalized ASP earns 4.4% on its own capital -- better than the self-funded scenario because the borrowed capital has a positive (but slim) spread. At 0.5%, it earns 25.2% -- venture-grade returns.

**Where does it break?** The break-even borrowing rate for Scenario C at 0.3% fees:

```
Revenue - OpCosts - OppCost = max borrowing cost
$1.56M - $350K - $150K = $1.06M
$1.06M / $21M = 5.05%
```

At any borrowing rate above 5.05%, the minimally capitalized ASP is unprofitable at 0.3% fees.

### Summary Table

| Scenario | Own capital | Borrowed | Borrow rate | Fee rate | Net profit | ROI on own capital |
|---|---|---|---|---|---|---|
| A (self-funded) | $26M | $0 | -- | 0.3% | $430K | 1.7% |
| A (self-funded) | $26M | $0 | -- | 0.5% | $1.47M | 5.7% |
| B (50/50) | $13M | $13M | 4% | 0.3% | $300K | 2.3% |
| B (50/50) | $13M | $13M | 4% | 0.5% | $1.34M | 10.3% |
| C (minimal) | $5M | $21M | 4% | 0.3% | $220K | 4.4% |
| C (minimal) | $5M | $21M | 4% | 0.5% | $1.26M | 25.2% |
| C (minimal) | $5M | $21M | 5% | 0.3% | $10K | 0.2% |

---

## 4. What Rate Can the ASP Afford to Pay Lenders?

Working backward from the economics:

```
Max borrowing rate = (Fee revenue - Operating costs - Min profit on own capital) / Borrowed amount
```

For Scenario B ($13M own, $13M borrowed, 0.3% fee, requiring 3% min return on own capital):

```
Available for borrowing = $1.56M - $350K - ($13M * 3%) - ($13M * 3%)
                        = $1.56M - $350K - $390K - $390K
                        = $430K
Max rate = $430K / $13M = 3.3%
```

For Scenario C ($5M own, $21M borrowed, 0.3% fee, requiring 3% min return on own capital):

```
Available for borrowing = $1.56M - $350K - ($5M * 3%) - ($5M * 3%)
                        = $1.56M - $350K - $150K - $150K
                        = $910K
Max rate = $910K / $21M = 4.3%
```

At 0.5% fee rate, Scenario B:

```
Available = $2.6M - $350K - $390K - $390K = $1.47M
Max rate = $1.47M / $13M = 11.3%
```

### The Spread Question

| ASP can afford to pay | Lenders demand (min) | Spread |
|---|---|---|
| 3.3% (at 0.3% fee, Scenario B) | 3-5% (Section 5) | **Negative to zero** |
| 4.3% (at 0.3% fee, Scenario C) | 3-5% | **Negative to marginal** |
| 11.3% (at 0.5% fee, Scenario B) | 3-5% | **+6 to +8%** |

**At 0.3% fees, there is no positive spread.** The ASP cannot afford to pay what lenders demand. The financing market does not clear.

**At 0.5% fees, the spread is wide.** The ASP can afford to pay well above market rates, and lenders earn attractive returns. The financing market clears easily.

The critical threshold is approximately **0.35-0.40% blended fee rate** -- the point where the ASP generates enough surplus to pay lenders a competitive return while retaining an acceptable profit margin.

---

## 5. The Lender's Perspective

### Competing Yields for Idle BTC

| Deployment option | Annual yield | Risk | Term/Liquidity | Complexity |
|---|---|---|---|---|
| Lightning routing (median) | 1.2-1.7% | Operational | Indefinite lock, exit via channel close | High (node mgmt, rebalancing) |
| Lightning routing (aggressive) | 5-10% | Captive flow dependency | Indefinite | High |
| Amboss Magma leasing | 2.6% median | Counterparty, channel closure | Fixed (weeks to months) | Medium |
| CeFi lending -- Ledn (institutional) | 2% | Platform solvency | Withdrawal terms vary | Low |
| CeFi lending -- Ledn (retail, < 0.5 BTC) | 5.25% | Platform solvency | Withdrawal terms vary | Low |
| DeFi lending (Aave wBTC) | 1-4% variable | Smart contract, bridge | Open-ended, instant exit | Medium |
| Babylon BTC staking | TBD (not yet yielding) | Protocol, slashing | Locked (unbonding period) | Medium |
| Holding BTC | 0% | Price volatility only | Instant liquidity | None |

Sources: [Ledn](https://www.ledn.io/post/bitcoin-loan-rates); [Voltage](https://voltage.cloud/blog/where-does-lightning-network-yield-come-from); [Atlas21](https://atlas21.com/lightning-routing-yields-10-annually-blocks-announcement/); [DeFiRate](https://defirate.com/lend/); [Second yield survey](https://blog.second.tech/survey-of-bitcoin-yield/)

### What the ASP Offers Lenders

| Feature | ASP lending | Lightning leasing | CeFi lending |
|---|---|---|---|
| Yield | 3-5% (at feasible fee rates) | 1.5-2.6% median | 2-5.25% |
| Term | Fixed, 14-28 days | Fixed (weeks-months) | Variable or fixed |
| Collateral | On-chain BTC escrow (multisig) | Channel commitment | Platform custody |
| Denomination | BTC-for-BTC | BTC-for-BTC | BTC |
| FX risk | None | None | None |
| Counterparty risk | ASP default | Node goes offline | Platform insolvency |
| Liquidity | Locked for term | Locked until channel close | Varies |
| Complexity | Low (deposit into escrow) | Medium (channel management) | Low |

### Is ASP Lending Competitive?

Against Lightning leasing (the closest analogue): ASP lending offers higher yield (3-5% vs 1.5-2.6% median) with known term (14-28 days vs indefinite lock), known collateral (on-chain escrow vs channel commitment), and lower operational complexity (no node management). The ASP product is strictly better for a lender who does not want to run Lightning infrastructure.

Against CeFi lending: ASP lending offers comparable yield (3-5% vs 2-5.25%) with on-chain collateral rather than platform custody. The lender does not face platform insolvency risk (the Celsius/BlockFi scenario) because collateral is in a multisig, not in the platform's possession. The tradeoff is shorter term (14-28 days vs flexible) and smaller market (3-5 ASPs vs broad CeFi lending market).

Against holding: Any positive yield beats 0%. The question is whether the risk premium is adequate. A lender earning 4% on a 14-day term with on-chain collateral faces: (a) ASP operational failure (cannot repay from expired VTXOs if the ASP's Ark operation fails), (b) on-chain execution risk during collateral liquidation, (c) rollover risk if the lender wants to continue but terms change. These risks are moderate and well-defined.

**Verdict:** ASP lending is competitive with Lightning leasing and CeFi lending at rates of 3-5%. It occupies a niche between "easy but low yield" (CeFi) and "high effort, variable yield" (Lightning routing). The fixed term and on-chain collateral are differentiators. The market is small but the product is viable.

---

## 6. The Productive Capacity Question

### What Justifies External Financing?

The ASP provides a real service: cheap, private, scalable Bitcoin (and potentially stablecoin) payments. Users pay fees for this service. The fees are the ASP's revenue. The locked BTC is working capital -- the cost of providing the service.

This is standard business finance. A trucking company borrows to buy trucks. A factory borrows to buy equipment. An ASP borrows to fund covenant trees. In each case, external financing is justified when:

```
Return on marginal capital > Cost of marginal capital
```

For the ASP:
- Return on marginal capital: gross yield = 6.0% (at 0.3% fee, V2, 50% spend)
- Cost of marginal capital: borrowing rate = 4-5%
- Spread: 1-2%

The spread is positive but thin. After allocating operating costs, the net spread on borrowed capital is approximately:

```
Net spread = 6.0% - 1.35% (opex allocation) - 4.0% (borrow rate) = 0.65%
```

At 0.65% net spread on $13M borrowed, the ASP earns $84.5K/year from the borrowed capital. This is marginal but positive.

### Challenges to the Productive Capacity Thesis

**Fee compression.** If multiple ASPs compete, fees will compress toward marginal cost. The 0.3% blended rate assumes limited competition. With 10+ ASPs, fees could fall to 0.15-0.20%, at which point the ASP cannot afford external capital at any rate.

**Throughput volatility.** The model assumes steady $10M/week. Real throughput will be lumpy -- high during BTC price moves, low during quiet periods. The ASP's capital is locked for 14-28 days regardless of whether throughput drops next week. If throughput halves for a month, fee revenue halves but capital costs remain fixed. This is operating leverage that cuts both ways.

**BTC price crash impact.** Fees and costs are both BTC-denominated, so a BTC price crash does not directly affect the BTC-denominated P&L. The ASP earns 0.003 BTC per 1 BTC throughput regardless of USD price. However: (a) the ASP's infrastructure costs (servers, labor) are USD-denominated, so a BTC crash increases the BTC-equivalent cost of operations; (b) user behavior may shift unpredictably; (c) lending rates may spike during volatility (lenders demand risk premium), compressing margins.

**Is the ASP "productive" in the economic sense?** Compare:
- A Lightning routing node moves BTC between channels and earns fees. Productive.
- An Ark ASP moves BTC between covenant trees and earns fees. Productive.
- Both provide real services (payment routing, scalable transactions) that users pay for voluntarily.
- Neither creates new BTC. Both earn BTC yield from providing infrastructure services.

The ASP is as productive as a Lightning node. The difference is scale: the ASP's capital requirements are 10-100x larger per unit of throughput, and the yield per unit of capital is comparable. The ASP needs more capital to serve the same volume, which is precisely why external financing becomes relevant.

---

## 7. Alternative Framing: Accounts Receivable Factoring

### The Analogy

The ASP's locked VTXOs function like accounts receivable:

| Factoring concept | Ark equivalent |
|---|---|
| Invoice | VTXO tree expiring in X days, returning BTC to the ASP |
| Invoice amount | BTC locked in the covenant tree |
| Payment date | VTXO expiry date (deterministic, protocol-enforced) |
| Debtor | The Ark protocol itself (not a counterparty -- a script) |
| Factor | A lender who provides BTC now in exchange for the future BTC return |
| Discount rate | The interest rate on the loan |
| Credit risk | ASP operational failure (the "debtor" is a script that always pays on time) |

### Comparison to Traditional Factoring

| Feature | Traditional factoring | ASP "VTXO factoring" |
|---|---|---|
| Typical discount rate | 1-5% of invoice value for 30-60 day terms | 0.3-0.7% for 14-28 day terms (annualized: 4-9%) |
| Payment predictability | Variable (debtor may pay late or not at all) | Deterministic (protocol-enforced expiry) |
| Recourse | Factor may have recourse to seller if debtor defaults | No debtor default possible; only ASP operational risk |
| Volume | Ongoing, growing with business revenue | Ongoing, growing with ASP throughput |
| Documentation | Invoices, purchase orders, shipping docs | On-chain covenant tree commitments, publicly verifiable |

The ASP's "receivables" are more predictable than traditional factoring targets. In traditional factoring, the factor takes credit risk on the debtor (will the customer pay?). In ASP factoring, the "debtor" is a Bitcoin script with a deterministic expiry -- it *always* pays on time. The only risk is ASP operational failure (the ASP goes offline and cannot sweep expired trees). This risk is distinct from and lower than debtor credit risk.

### Factoring Discount Rate Comparison

Traditional factoring: 1-5% of invoice face value for 30-60 day terms. On a $100K invoice with 30-day terms, the factor charges $1K-5K (1-5%). Annualized: 12-60%.

ASP "factoring" at 4% annualized borrowing rate on a 28-day "invoice":

```
28-day cost = 4% * (28/365) = 0.307% of principal
```

This is at the low end of traditional factoring rates (1-5%), which makes sense given the ASP's "receivables" are lower risk (deterministic payment date, no debtor credit risk).

### Does the Factoring Frame Fit Better Than Repo?

The factoring frame describes what is actually happening more accurately than repo:
- **Repo** implies a sale-and-repurchase of an asset. The ASP is not selling VTXOs -- it cannot (the scripts do not allow third-party claims).
- **Factoring** implies advancing cash against known future receivables. The ASP is receiving BTC now against BTC it will reclaim in 14-28 days. This is exactly factoring.

The factoring frame also suggests a simpler structure than repo. Factoring does not require title transfer, collateral management, or clearing infrastructure. The factor assesses the quality of the receivables (are the covenant trees valid? will they expire on schedule?) and advances funds against them. The ASP repays from the expired trees.

The risk model is simpler too. The factor's risk is: (1) the ASP fails to operate and cannot sweep expired trees (operational risk), and (2) the ASP misrepresents its receivables (fraud risk). Both are assessable through on-chain verification -- the factor can independently verify covenant tree commitments on the Bitcoin blockchain.

---

## 8. The "Do Nothing" Economics

### At What Scale Does Self-Funding Become Untenable?

The self-funded ASP needs $26M locked for $10M/week throughput. Scale this:

| Weekly throughput | Locked capital (V2, 50% spend) | BTC required (at $100K) | Who can self-fund? |
|---|---|---|---|
| $1M | $2.6M | 26 BTC | Mid-size Bitcoin companies, funds |
| $10M | $26M | 260 BTC | Large exchanges, treasury companies |
| $100M | $260M | 2,600 BTC | Tether, Block Inc., major exchanges |
| $1B | $2.6B | 26,000 BTC | Nobody (exceeds all but the largest BTC holders) |

Self-funding becomes untenable between $100M and $1B weekly throughput. At $100M/week, only a handful of entities globally have sufficient BTC. At $1B/week (the stablecoin scenario), self-funding is impossible for any single entity.

### Natural Cap on ASP Size

Without external financing, there is a natural cap on ASP size determined by the operator's BTC holdings. A company with 500 BTC can support ~$19M/week in throughput. A company with 5,000 BTC can support ~$192M/week. Beyond that, it needs external capital.

This creates a market structure of **many mid-size ASPs** rather than few large ones -- each constrained by its own capital. This has implications:

**Positive for decentralization.** More ASPs means more competition, more geographic diversity, less systemic risk from a single ASP failure. Users can choose between ASPs based on fees, reliability, and jurisdiction.

**Negative for efficiency.** Fragmented liquidity across many small ASPs is less efficient than concentrated liquidity in few large ones. Users on different ASPs cannot transact directly (they must bridge via Lightning or on-chain). Cross-ASP coordination adds overhead.

**Negative for stablecoin throughput.** If Ark's killer app is stablecoin transfers, the throughput needs to be concentrated enough to support high-volume settlement. Many small ASPs each handling $5M/week in stablecoins is less useful than one ASP handling $500M/week with deep liquidity.

### Is the "Do Nothing" Outcome Actually Good?

For BTC-only payments, many mid-size self-funded ASPs is arguably the ideal outcome. It mirrors the Lightning Network's decentralized node structure (notwithstanding the 0.97 Gini coefficient in practice). The capital constraint acts as a natural scaling limit that prevents monopoly.

For stablecoin settlement, the "do nothing" outcome is inadequate. The stablecoin use case requires throughput levels that exceed self-funding capacity. External financing is the bridge between "BTC payments layer" and "stablecoin settlement layer."

---

## 9. Devil's Advocate: Maybe External Financing Is Not Needed

### Argument 1: Large Entities Self-Fund

If ASPs are run by Tether ($8B+ BTC reserves), exchanges (Binance reportedly holds ~500K+ BTC), or public treasury companies (MicroStrategy holds ~500K+ BTC), the capital requirement is trivial. Tether locking 5,000 BTC in an ASP is 0.06% of its BTC holdings. No financing market needed.

**Counter:** This centralizes Ark around a handful of mega-entities. The protocol becomes permissioned in practice. If only Tether can afford to run an ASP at scale, Ark's non-custodial value proposition is hollow -- users are trusting Tether's ASP, which is one step removed from trusting Tether directly.

### Argument 2: V2 + Short Expiry Reduces the Gap to Manageable Levels

V2 revocation (50% recovery) + 14-day expiry (50% reduction) = 75% total reduction. The medium ASP needs $13M instead of $52M. With a 70% spend rate and 14-day expiry: $9M. Many Bitcoin-native businesses can self-fund $9M.

**Counter:** The 70% spend rate is optimistic for a general-purpose ASP. It requires a payments-dominated user base. Savings-heavy users (HODLers who park BTC in Ark for privacy) spend slowly. A realistic mixed ASP hits 40-50% spend, not 70%. And the 14-day expiry has real UX costs, even with delegation.

### Argument 3: The Market Is Too Small to Justify Infrastructure

Total external funding need at early scale: $7-33M. Building a lending market costs $1-5M in development, audit, and legal work. Annual operational cost: $200K-500K. The market generates maybe $500K-$1M/year in total interest revenue. The infrastructure cost may exceed the value generated for years.

**Counter:** The stablecoin scenario changes the math by 10-100x. And financial infrastructure compounds: a lending market built for ASPs can expand to serve Lightning operators, Bitcoin L2s, and other BTC-denominated capital needs. The addressable market is larger than Ark alone.

### Argument 4: The Strongest Case Is the Stablecoin Scaling Scenario

On this, there is no counterargument. If Ark becomes a significant stablecoin settlement layer, throughput grows 10-100x. Capital requirements outpace even the largest self-funded operators. External financing transitions from "nice to have" to "necessary infrastructure."

The honest assessment: external financing is optional for BTC-only Ark at current projected scale. It becomes necessary when stablecoin throughput materializes. The question is whether to build the infrastructure now (before the need is acute) or wait (and risk being unprepared when demand spikes).

---

## Sources

### Ark Protocol
- [Second fee schedule](https://second.tech/docs/learn/fees) -- 0-0.5% tiered by VTXO age
- [Ark Labs: Liquidity Requirements](https://blog.arklabs.xyz/liquidity-requirements/) -- Simulation-based capital analysis
- [Ark Labs: Adios Expiry](https://blog.arklabs.xyz/adios-expiry-rethinking-liveness-and-liquidity-in-arkade/) -- Delegation model
- [Second: Ark Liquidity Research](https://blog.second.tech/ark-liquidity-research-01/) -- Sat-days comparison, LSP vs Ark
- [Burak: Introducing Ark V2](https://brqgoo.medium.com/introducing-ark-v2-2e7ab378e87b) -- Revocation mechanism

### Lightning Network and BTC Yield
- [Atlas21: Block Lightning Routing Yields](https://atlas21.com/lightning-routing-yields-10-annually-blocks-announcement/) -- 9.7% on 184 BTC
- [Voltage: LINER Yield](https://voltage.cloud/blog/where-does-lightning-network-yield-come-from) -- 1.16-1.65% network average
- [Second: Bitcoin Yield Survey](https://blog.second.tech/survey-of-bitcoin-yield/) -- Magma median 2.6%, Lightning Pool 2.53%

### BTC Lending
- [Ledn: Rates](https://www.ledn.io/post/bitcoin-loan-rates) -- 2-5.25% APY tiered by balance
- [DeFiRate](https://defirate.com/lend/) -- DeFi lending rates 1-4%
- [APX Lending](https://apxlending.com/blog/best-crypto-loan-rates) -- Institutional borrowing rates 4-10%

### Prior Research in This Series
- `problem-spec.md` -- Capital lockup model, V2 scenarios, revenue baseline
- `constraints.md` -- Protocol constraints, BTC-for-BTC reframe, go/no-go assessment
- `framing-analysis.md` -- Four problem frames, residual gap calculation
- `defi-survey.md` -- DeFi lending landscape, factoring parallels, rehypothecation risk

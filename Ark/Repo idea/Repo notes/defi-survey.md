# DeFi Lending and Liquidity: A Survey for Bitcoin-Native Repo Design

*Research compiled March 2026. All claims cited to sources.*

---

## Table of Contents

1. [DeFi Lending Protocols (Not Repo)](#1-defi-lending-protocols-not-repo)
2. [Protocols Closer to Repo](#2-protocols-closer-to-repo)
3. [Bitcoin-Native Liquidity Markets](#3-bitcoin-native-liquidity-markets)
4. [Rehypothecation Cascades](#4-rehypothecation-cascades-the-risk)
5. [What DeFi Has Solved vs What Remains Unsolved](#5-what-defi-has-solved-vs-what-remains-unsolved)
6. [Devil's Advocate: Is DeFi Lending Good Enough?](#6-devils-advocate-is-defi-lending-good-enough)

---

## 1. DeFi Lending Protocols (Not Repo)

These are the dominant DeFi lending models. None of them are repo. The distinction matters: a repurchase agreement involves selling an asset with a contractual obligation to repurchase it at a fixed price on a fixed date. DeFi lending involves depositing collateral into a pool and borrowing against it, with no repurchase commitment, no fixed term, and no collateral reuse by the lender. The economic function is superficially similar (short-term funding against collateral) but the mechanics, risk profiles, and capital efficiency are fundamentally different.

### 1.1 Aave and Compound: Pool-Based Lending

**How they work:** Lenders deposit assets into a shared liquidity pool. Borrowers post collateral and draw from the pool. Interest rates are algorithmically determined by the pool's utilization rate -- the percentage of deposited assets currently borrowed. Aave v3 uses a two-slope interest rate model: below an optimal utilization point, rates rise gently; above it, they rise steeply to discourage over-borrowing and attract new supply. Compound uses a similar "jump rate" model. When a borrower's collateralization ratio drops below a threshold (the "health factor" falls below 1), liquidators can repay up to 50% of the debt and seize collateral at a discount. ([Aave v3 Documentation](https://aave.com/docs/aave-v3/overview); [Cube Exchange: Interest Rate Models](https://www.cube.exchange/what-is/interest-rate-model); [Coin Bureau: Aave Review](https://coinbureau.com/review/aave-lend))

**Why this is not repo:**

- **No repurchase commitment.** A borrower on Aave has no obligation to return funds at a specific time. They can hold the position indefinitely as long as collateral holds. In repo, the seller commits to repurchase the asset at a fixed date and price.
- **No fixed term.** Aave/Compound lending is open-ended. Repo is inherently term-structured -- overnight, one week, one month. The term is what creates the yield curve.
- **No collateral reuse.** When you deposit ETH as collateral on Aave, it sits in the pool earning interest. The protocol does not lend your collateral to a third party (though it does lend pool assets to borrowers). In repo, the cash lender takes legal title to the collateral and can rehypothecate it.
- **Variable rates, not agreed rates.** Aave rates change every block based on utilization. Repo rates are agreed bilaterally at trade execution and fixed for the term.
- **Liquidation, not margin calls.** Aave uses automated liquidation. Repo uses margin calls with cure periods -- the borrower gets a chance to post additional collateral before the position is closed.

**Scale:** Aave remains the largest DeFi lending protocol, with billions in TVL across multiple chains. Compound pioneered the model but has been overtaken in scale.

### 1.2 Morpho Blue: Isolated Markets

**How it works:** Morpho Blue enables the creation of isolated lending markets, each defined by five immutable parameters: loan asset, collateral asset, liquidation loan-to-value (LLTV), oracle address, and interest rate model (IRM). Unlike Aave's shared pools, each Morpho market is a standalone contract. Risk is isolated: a failure in one market does not affect others. Parameters are set at creation and cannot be changed -- the market persists as long as Ethereum exists. ([Morpho Blue Documentation](https://docs.morpho.org/learn/concepts/market/); [MixBytes: How It's Made](https://mixbytes.io/blog/modern-defi-lending-protocols-how-its-made-morpho-blue))

Morpho V2 (launched June 2025) introduced intent-based lending with fixed-rate, fixed-term loans. Lenders and borrowers submit offers at specific prices, and the protocol matches them. This moves Morpho significantly closer to bilateral lending. ([CoinDesk: Morpho V2](https://www.coindesk.com/business/2025/06/12/crypto-lending-platform-morpho-v2-brings-defi-closer-to-traditional-finance))

**Why it is closer but still not repo:** Morpho's isolated markets address one of the key differences -- risk isolation rather than pool risk. And Morpho V2's fixed-rate, fixed-term matching starts to resemble bilateral term lending. But there is still no repurchase obligation. The borrower receives a loan against collateral; they do not sell an asset with a commitment to buy it back. There is no legal title transfer of collateral, and the collateral cannot be reused by the lender.

**Scale:** $2.4B TVL on Ethereum in May 2025, growing to $9B in deposits by July and $6.7B TVL by August 2025. ([Morpho Blog](https://morpho.org/blog/morpho-blue-and-how-it-enables-our-vision-for-defi-lending/))

### 1.3 MakerDAO (Sky): Collateralized Debt Positions

**How it works:** Users lock collateral (ETH, wBTC, real-world assets) into Vaults and mint DAI, a dollar-pegged stablecoin. The collateralization ratio ranges from 101% to 175% depending on the asset. A stability fee (analogous to an interest rate) accrues on the minted DAI. If collateral value drops below the liquidation ratio, the position is automatically liquidated. ([MakerDAO Whitepaper](https://makerdao.com/whitepaper/White%20Paper%20-The%20Maker%20Protocol_%20MakerDAO%E2%80%99s%20Multi-Collateral%20Dai%20(MCD)%20System-FINAL-%20021720.pdf); [Gemini: MakerDAO](https://www.gemini.com/cryptopedia/makerdao-dai-decentralized-autonomous-organization))

**The shadow banking parallel:** MakerDAO is closer to shadow banking than to repo. In shadow banking, entities create money-like claims (commercial paper, money market fund shares) backed by longer-duration or riskier assets. Maker does the same: it creates DAI (a money-like claim) backed by volatile crypto collateral. The transformation is from illiquid/volatile collateral into a liquid stablecoin -- collateral transformation, not a repurchase agreement.

The comparison to traditional shadow banking is instructive:
- **Money market funds** create liquid, redeemable shares backed by less-liquid commercial paper. Maker creates liquid, redeemable DAI backed by less-liquid ETH.
- **Structured investment vehicles (SIVs)** issued short-term commercial paper backed by long-term mortgage securities. Maker issues DAI (short-term liability -- redeemable on demand) against long-duration crypto positions.
- **The run risk is the same.** In 2008, the shadow banking system collapsed when money market funds "broke the buck" and investors demanded redemptions that exceeded liquid reserves. Maker faces the same risk: if a rapid collateral decline triggers mass liquidations, DAI's peg depends on whether the system can process liquidations faster than collateral falls.

This is not repo. It is collateral transformation -- turning one type of asset into a more liquid form. Repo involves a temporary exchange that reverses at maturity. Maker involves the creation of a new asset against collateral, with no scheduled reversal.

---

## 2. Protocols Closer to Repo

### 2.1 Term Finance: The Closest DeFi Analogue to Term Repo

**How it works:** Term Finance is a noncustodial fixed-rate liquidity protocol explicitly modeled on tri-party repo arrangements. It runs weekly auctions where borrowers submit sealed bids (maximum rates they will pay) and lenders submit sealed offers (minimum rates they will accept). A smart contract calculates a single clearing rate that balances supply and demand. All participants in the batch trade at this uniform clearing price. ([Term Finance](https://www.term.finance/); [CoinDesk: Term Finance Launch](https://www.coindesk.com/business/2023/08/01/defi-platform-term-finance-brings-fixed-rate-lending-to-ethereum); [GitHub: term-finance-contracts](https://github.com/term-finance/term-finance-contracts))

**Repo-like features:**
- **Fixed rate:** The clearing rate is fixed for the term of the loan. No utilization-based variability.
- **Fixed term:** Loans have a maturity date. They are not open-ended.
- **Non-redeemable before maturity:** Unlike Aave, you cannot exit early. This is a defining feature of repo.
- **Auction-based price discovery:** Repo rates in traditional finance are determined by auction (e.g., the Fed's reverse repo facility) or bilateral negotiation. Term Finance uses a sealed-bid uniform-price auction -- the closest on-chain analogue.
- **Repo tokens:** Lenders receive Term Repo Tokens that represent their claim. These are analogous to repo receipts in traditional finance.

**What is still missing vs. true repo:**
- **No legal title transfer.** In a repo, the cash lender takes legal title to the collateral. This is what enables rehypothecation. Term Finance uses smart contract custody -- the collateral is locked, not transferred.
- **No collateral reuse.** The collateral sits in a smart contract until maturity. The lender cannot reuse it. This limits capital velocity compared to traditional repo.
- **Smart contracts as clearing agent.** Term Finance's smart contracts automate the functions of a tri-party clearing agent (collateral management, settlement). This is structurally better than most DeFi but still lacks the flexibility of a human clearing agent who can handle exceptions.

**Scale:** TermMax (a related protocol from Term Labs) reached $49.18M TVL with 1,800 daily active users across Ethereum, Arbitrum, and BNB Chain as of mid-2025. The original Term Finance protocol's long-term vision is to create a DeFi-native benchmark yield curve by offering repo tokens maturing every week, going out to one year. ([MEXC: Term Finance](https://www.mexc.com/learn/article/17827791522877); [WuBlockchain: Term Finance](https://wublockchain.medium.com/term-finance-on-chain-lending-protocol-with-fixed-interest-rates-fixed-terms-and-32a641e7bdcf))

### 2.2 Ethena: Basis Trade as Implicit Repo

**How it works:** Ethena creates USDe, a synthetic dollar backed by a delta-neutral basis trade. For each dollar of USDe minted, Ethena holds a long position in spot crypto (BTC, ETH, staked ETH) and an equal short position in perpetual futures. The peg is maintained by the delta-neutral hedge. Yield comes from three sources: (1) the funding rate on perpetual futures (shorts collect from longs when funding is positive), (2) staking rewards on staked ETH collateral, and (3) yields on stable reserve assets. ([Ethena Documentation](https://docs.ethena.fi/solution-overview/usde-overview); [Coin Metrics: Ethena Mechanics](https://coinmetrics.substack.com/p/state-of-the-network-issue-335); [Nansen: Ethena Guide](https://www.nansen.ai/post/what-is-ethena))

**Why this is repo-adjacent:** The perpetual futures funding rate is economically equivalent to an implied repo rate. In traditional finance, the "basis" between spot and futures prices reflects the cost of carry -- which is the repo rate. Ethena monetizes this basis. When funding rates are positive (longs paying shorts), Ethena collects yield that functions identically to earning the repo rate on a collateralized position.

The parallel is precise:
- **Traditional repo:** Sell a bond, receive cash, commit to repurchase. Earn the spread between the bond yield and the repo rate.
- **Ethena:** Hold spot crypto, short the perpetual future. Earn the funding rate (the basis spread). No physical repurchase, but the economic exposure is the same -- you are lending your long position to the market in exchange for yield.

BTC funding rates averaged ~11% annualized in 2024 and ~5% in 2025. ETH funding rates averaged ~12.6% in 2024. USDe has grown to the 3rd largest stablecoin by market cap, exceeding $10.5B. ([Multicoin Capital: Ethena](https://multicoin.capital/2025/11/13/ethena-synthetic-dollars-challenge-stablecoins-duopoly/))

**The risk:** Funding rates can flip negative during market stress. During the October 2025 flash crash (~$20B in liquidations), funding rates inverted, meaning Ethena had to pay rather than collect. The protocol maintains a reserve fund ($50M+) to absorb negative-funding periods, but sustained inversion threatens the peg. This is analogous to a repo rate spike during a liquidity crisis -- the cost of funding your position can exceed the carry, making the trade unprofitable.

### 2.3 Maple Finance and Clearpool: Institutional Term Lending

**Maple Finance** offers institutionally underwritten credit products -- fixed-rate, overcollateralized loans to creditworthy borrowers like market makers, trading firms, and crypto-native funds. Loans are short-duration and underwritten by pool delegates (institutional credit assessors). Maple is essentially DeFi's answer to private credit. ([Maple Finance](https://maple.finance/); [Modular Capital: Maple](https://www.modularcapital.xyz/writing/maple); [21Shares: Maple](https://www.21shares.com/en-eu/research/how-maple-finance-is-defis-answer-to-private-credit))

**Clearpool** (now also behind the Ozean blockchain) provides single-borrower liquidity pools where institutional borrowers set their own terms. Lenders choose which borrowers to fund based on creditworthiness.

**Comparison to repo:**
- **Fixed rate and fixed term:** Both Maple and Clearpool offer this. Closer to repo than Aave/Compound.
- **Institutional counterparties:** Like repo, these are wholesale markets, not retail.
- **No collateral reuse:** Still uses locked collateral, not title transfer.
- **Credit risk is explicit:** Pool delegates assess borrower creditworthiness. In repo, counterparty credit risk exists but is mitigated by collateral title transfer.
- **Maple's history:** Maple suffered significant defaults in the 2022 crypto credit crisis (Orthogonal Trading, Auros), losing ~$54M. This exposed the gap between fixed-term institutional lending and true repo -- in repo, the lender holds collateral and can sell it immediately on default. In Maple's case, defaulted loans had to go through recovery processes.

### 2.4 Solstice: The First On-Chain Stablecoin Repo

In December 2025, Solstice and Cor Prime executed the first institutional stablecoin-for-stablecoin repurchase agreement on a public blockchain. Solstice supplied its USX stablecoin as collateral while Cor Prime delivered USDC as the cash leg. Both legs transferred directly between institutional wallets across Solana and Ethereum. Membrane Labs provided post-trade infrastructure for settlement, servicing, and lifecycle management, including cross-chain asset movement and a predefined unwind at maturity. ([The Block: Solstice Repo](https://www.theblock.co/press-releases/383619/solstice-and-cor-prime-execute-first-institutional-stablecoin-for-stablecoin-repo-on-a-public-blockchain); [Chainwire: Solstice](https://chainwire.org/2025/12/23/solstice-and-cor-prime-execute-first-institutional-stablecoin-for-stablecoin-repo-on-a-public-blockchain/))

This is the closest thing to true on-chain repo that currently exists. It follows the economic and operational logic of traditional repo -- a bilateral agreement with predefined unwind at maturity, executed under a Global Master Repurchase Agreement (GMRA) with a Digital Asset Annex. The distinction from DeFi lending is explicit: unlike automated lending pools, this involves ownership transfer and scheduled reversal.

**Limitations:** This is institutional infrastructure, not a permissionless protocol. It operates between known counterparties under traditional legal agreements (GMRA). It is not yet a market that arbitrary participants can access programmatically.

### 2.5 Traditional Finance on Blockchain: JP Morgan Onyx

JP Morgan's Onyx platform executes blockchain-based repo transactions involving tokenized US Treasury bonds, settling fully on-chain. This is traditional repo with blockchain settlement rails -- not a new DeFi primitive, but evidence that major institutions see blockchain as a viable settlement layer for repo. ([Kaleido: Repo Tokenization](https://www.kaleido.io/blockchain-blog/repo-tokenization))

Also notable: SBI, UBS, and DBS executed the world's first cross-border repo involving a natively-issued digital bond on a public blockchain. ([Halborn: Cross-Border Repo](https://www.halborn.com/case-studies/post/case-study-securing-the-first-cross-border-digital-bond-repo))

---

## 3. Bitcoin-Native Liquidity Markets

These are the closest precedents for a Bitcoin-native repo market, because they involve BTC-denominated liquidity priced at fixed rates for fixed terms.

### 3.1 Lightning Pool (Lightning Labs)

**How it works:** Lightning Pool is a non-custodial, batched, uniform clearing-price auction for Lightning Channel Leases (LCLs). An LCL packages inbound channel liquidity (the ability to receive funds) as a fixed-income asset with a maturity date expressed in blocks. Nodes needing inbound liquidity bid for it; nodes with excess liquidity offer it. The protocol calculates a uniform clearing price -- all participants in a batch clear at the same rate. ([Lightning Labs: Pool](https://lightning.engineering/pool/); [Lightning Labs: Pool Deep Dive](https://lightning.engineering/posts/2020-11-02-pool-deep-dive/); [GitHub: lightninglabs/pool](https://github.com/lightninglabs/pool))

**Structural similarity to repo:** This is remarkably close to a repo market:
- **Fixed term:** Channel leases have a maturity date in blocks. The liquidity provider commits capital for a specific duration.
- **Fixed rate:** The clearing price determines the cost of liquidity for the term. This is economically equivalent to a repo rate.
- **Auction-based price discovery:** Like a repo auction, prices are set by sealed-bid uniform clearing.
- **Capital deployment for yield:** Liquidity providers lock BTC in channels for a term and earn a return. This is the economic function of lending in the repo market.

**What is different from repo:** There is no repurchase in the traditional sense. The liquidity provider opens a channel (deploys capital) and the channel persists until maturity or close. There is no asset sale with repurchase obligation. The "collateral" is implicit -- the channel itself is the asset, secured by the Bitcoin script's timelock.

**Current status:** Pool is in beta. The last GitHub release appears to be v0.6.0. Lightning Pool's volumes appear low relative to the overall Lightning Network, and Second's research found only two recent orders at 2.53% for 14-day periods -- annualizing to ~66.2%, but the low volume makes this unreliable as a price signal. ([Second Blog: Bitcoin Yield Survey](https://blog.second.tech/survey-of-bitcoin-yield/))

### 3.2 Amboss Magma

**How it works:** Amboss Magma is a peer-to-peer marketplace for Lightning channel liquidity. Nodes needing inbound capacity purchase channels by paying a Lightning invoice. Sellers open channels to buyers within a short timeframe, enforced by HODL invoices (a smart-contract-like mechanism where payment is only released once the channel is confirmed). Magma v2 uses AI-powered matching to pair buyers with high-performing nodes at optimal prices. ([Amboss Magma Documentation](https://docs.amboss.tech/magma); [Amboss: Magma v2 Announcement](https://amboss.tech/blog/bitcoin-lightning-liquidity-marketplace-magma); [Second Blog: Amboss Magma](https://blog.second.tech/diving-deeper-into-lightning-liquidity-amboss-magma-2/))

**Pricing:** Rates use PPM (parts per million), where 10,000 PPM = 1%. The median rate on open offers is approximately 2.6% APR. Channels under 1 BTC capacity show the highest APRs (often exceeding 4%), though these don't translate to higher absolute yields for providers since miner fees eat into returns on small channels. ([Second Blog: Bitcoin Yield Survey](https://blog.second.tech/survey-of-bitcoin-yield/))

**How it differs from Lightning Pool:**
- **P2P vs. auction:** Magma is a marketplace with posted offers; Pool is a batch auction. Magma gives more control over counterparty selection; Pool gives better price discovery.
- **Reputation system:** Magma has a built-in reputation system (Reliability, Speed, Track Record). Pool relies on the auction mechanism.
- **Fee structure:** Amboss charges 0-1% depending on subscription tier.
- **Scale:** Magma appears to be more actively used than Pool, handling "a large share of completed public bitcoin liquidity lease orders." ([Second Blog: Amboss Magma](https://blog.second.tech/diving-deeper-into-lightning-liquidity-amboss-magma-2/))

**Relevance for ASP repo:** Magma's liquidity leasing rates (1-4% APR) represent the prevailing opportunity cost of deploying BTC capital. Second's research explicitly identifies Lightning liquidity leasing as "the closest analogue to liquidity on the Ark protocol," making these rates the most relevant benchmark for pricing ASP repo. ([Second Blog: Bitcoin Yield Survey](https://blog.second.tech/survey-of-bitcoin-yield/))

### 3.3 Liquid Network (Blockstream)

Liquid is a federated Bitcoin sidechain with confidential transactions and the ability to issue arbitrary assets. L-BTC is pegged 1:1 to BTC, held by the Liquid Federation. The network has basic lending infrastructure: Hodl Hodl's Lend platform allows L-BTC and Liquid USDT lending/borrowing, and SideSwap provides atomic swap functionality. ([Blockstream: Liquid](https://blockstream.com/liquid/); [Liquid Network](https://liquid.net/))

**Repo-like experiments:** No public discussion of repo-specific experiments on Liquid was found. The network has the technical capabilities (confidential transactions, asset issuance, scripting) that could support repo, but no one has built it.

### 3.4 Stacks

Stacks is the leading Bitcoin L2 for smart contracts, with the Nakamoto upgrade (October 2024) delivering fast finality and sBTC (December 2024) enabling native BTC in smart contracts. DeFi TVL grew 97.6% to $150.4M in Q1 2025. Zest Protocol is the primary lending protocol on Stacks, offering BTC-backed lending. ([Stacks](https://www.stacks.co/); [Stacks: April 2025 Town Hall](https://stacks.org/april-2025-town-hall))

**Repo-like protocols:** No repo-specific protocols were found on Stacks. The ecosystem has basic lending (Zest) but nothing approaching fixed-term, fixed-rate repo mechanics.

### 3.5 Babylon: Bitcoin Staking Protocol

Babylon enables non-custodial BTC staking to secure proof-of-stake networks. BTC remains in a user-controlled script on the Bitcoin mainchain. The protocol uses cryptographic signatures rather than bridges or wrappers. In August 2025, Babylon published the Trustless Bitcoin Vaults whitepaper, and by late 2025, it secured more than $10B in native BTC. A collaboration with Aave (announced December 2025) will enable native BTC as collateral on Aave V4 without wrapping, expected around April 2026. ([Babylon Labs](https://babylonlabs.io/); [Babylon: 2025 Roadmap](https://babylonlabs.io/blog/the-road-to-btcfi-babylons-2025-roadmap); [CoinDesk: Babylon Trustless Vaults](https://www.coindesk.com/tech/2025/08/06/babylon-introduces-trustless-bitcoin-vaults-for-btc-staking-protocol); [CoinDesk: Babylon x Aave](https://www.coindesk.com/business/2025/12/02/babylon-s-trustless-vaults-to-add-native-bitcoin-backed-lending-through-aave))

**Relevance for ASP repo:** Babylon's Trustless Vaults demonstrate that BTC can be used as verifiable on-chain collateral without bridges, wrappers, or custody transfer. The cryptographic techniques (witness encryption, garbled circuits) could inform how BTC collateral is handled in a repo context. The Babylon x Aave integration is particularly notable -- if native BTC can be used as collateral on Aave, the infrastructure for Bitcoin-collateralized lending is being built, even if repo-specific mechanics remain absent.

---

## 4. Rehypothecation Cascades: The Risk

Any repo design must contend with the rehypothecation problem. In traditional repo, collateral reuse is a feature -- it increases capital velocity. But it also creates systemic risk when chains of reuse break. DeFi has already demonstrated that these cascades are worse on-chain than in traditional finance.

### 4.1 Stream Finance Collapse (November 2025)

On November 4, 2025, Stream Finance announced a $93M loss and froze withdrawals. Its stablecoin, xUSD, crashed 77%. The cascade: $284.96M in loans across multiple protocols were secured by Stream's synthetic assets (xUSD, xBTC, xETH). These assets were used as collateral on Morpho, Euler, Compound, and others. When Stream collapsed, that collateral became worthless, triggering liquidations and bad debt across at least seven blockchain ecosystems. ([DL News: Stream Finance](https://www.dlnews.com/articles/defi/how-the-stream-finance-debacle-affected-the-rest-of-defi/); [BlockEden: Stream Finance Contagion](https://blockeden.xyz/blog/2025/11/08/m-defi-contagion/); [Bitget: DeFi Rehypothecation Turmoil](https://www.bitget.com/news/detail/12560605047139); [Decrypt: Stream Finance](https://decrypt.co/347285/stream-finance-stablecoin-plunges-77-protocol-fund-manager-loses-93-million))

The entities holding Stream exposure included Elixir ($68M), TelosC ($123.6M), and MEV Capital ($25.4M). Elixir's deUSD stablecoin had lent 68M USDC to Stream, representing 65% of its backing. The contagion triggered approximately $1B in net DeFi outflows.

**Root cause:** Gross negligence rather than a protocol design flaw. Over $90M in user funds were entrusted to an individual with "no formal relationship" to the project, without fund segregation, multi-signature controls, on-chain verification, or formal contracts.

### 4.2 Jupiter Lend Rehypothecation Controversy (2025-2026)

Jupiter Lend (on Solana) employs rehypothecation -- collateral from one vault is redeployed elsewhere in the system. A Jupiter executive admitted that official claims of "zero risk of contagion" between vaults were "not 100% correct." Critics identified the real risk: supplying SOL and borrowing USDC means your SOL gets lent to leveraged loopers, and you absorb all the risk of those loops blowing up. "No isolation and full cross contamination." ([The Block: Jupiter Lend](https://www.theblock.co/post/381602/jupiter-exec-acknowledges-zero-contagion-claim-was-not-100-correct-after-backlash-over-vault-design); [AInvest: Jupiter Lend Risks](https://www.ainvest.com/news/jupiter-lend-rehypothecation-risks-implications-defi-safety-2512/); [OneSafe: Jupiter Lend Crisis](https://www.onesafe.io/blog/jupiter-lend-crisis-defi-lending-pitfalls))

Jupiter Lend offers 90% LTV ratios (vs. ~75% elsewhere), enabled by a liquidation engine that processes all eligible positions in one transaction. The higher leverage combined with rehypothecation creates precisely the kind of fragility that makes cascades catastrophic.

### 4.3 Why DeFi Rehypothecation Is Worse Than Traditional Repo Rehypothecation

In traditional finance, rehypothecation is constrained:
- **Regulation T (US):** Limits rehypothecation to 140% of a client's net liability to the prime broker. A broker holding $100 of your collateral can only reuse $140 worth. ([ICMA: Rehypothecation FAQ](https://www.icmagroup.org/market-practice-and-regulatory-policy/repo-and-collateral-markets/icma-ercc-publications/frequently-asked-questions-on-repo/10-what-is-rehypothecation-of-collateral/))
- **Clearing agents:** Tri-party repo uses clearing agents (Bank of New York Mellon, JP Morgan) who track collateral location, enforce concentration limits, and manage substitutions.
- **Finite depth:** Regulatory limits and clearing infrastructure cap the depth of rehypothecation chains. Manby (2010) estimated a maximum multiplier of ~3x in practice.

In DeFi, none of these constraints exist:
- **No concentration limits.** One collateral asset can back unlimited layers of lending. Some protocols achieve 500% capital "efficiency" -- one dollar backing five dollars in loans. ([Midlands in Business: Rehypothecation Risk](https://midlandsinbusiness.com/rehypothecation-risk-in-defi-how-hidden-leverage-puts-your-crypto-at-risk))
- **No clearing agent.** No entity tracks where collateral sits across protocols. Collateral can flow from Aave to Morpho to Euler without any single entity knowing the full chain.
- **Unlimited depth.** Vault A's collateral backs loans in Vault B, which backs Vault C, which backs Vault D. There is no technical limit.
- **Atomic liquidation.** A 15-20% market move can trigger cascading liquidations across the entire chain simultaneously. Traditional repo has cure periods and human intervention.

As former SEC Chair Gary Gensler noted, DeFi rehypothecation presents "systemic risk comparable to pre-2008 money market funds." ([Chaos Labs: DeFi's Black Box](https://chaoslabs.xyz/posts/defi-s-black-box-how-risk-and-yield-are-repackaged))

### 4.4 Lessons for Bitcoin-Native Repo Design

1. **Hard-cap reuse depth.** If a Bitcoin-native repo system allows collateral reuse, it must enforce a maximum chain depth -- e.g., collateral can be reused at most once (like the UK's CASS rules) or twice.
2. **On-chain collateral tracking.** Every reuse must be visible and auditable. Bitcoin's UTXO model actually helps here -- you can track the provenance of collateral more precisely than in account-based systems.
3. **No composable collateral tokens.** The Stream Finance cascade happened because synthetic tokens (xUSD, xBTC) were accepted as collateral across multiple protocols. A Bitcoin-native repo system should not issue collateral tokens that can be fed into other lending protocols.
4. **Concentration limits.** No single counterparty should be able to repo more than X% of total system collateral. This is standard in traditional repo clearing and absent in DeFi.
5. **BTC as base collateral only.** Bitcoin's advantage is that BTC is a simple, non-synthetic asset. A repo system that only accepts BTC (not wrapped/synthetic derivatives) avoids the collateral-quality cascades that killed Stream Finance.

---

## 5. What DeFi Has Solved vs What Remains Unsolved

### Solved

- **Automated collateral management.** Smart contracts handle margin, liquidation, and settlement better than most humans, and they do it 24/7.
- **Permissionless access to lending.** Anyone can be a lender or borrower on Aave, Morpho, etc. Traditional repo is an interbank/institutional market.
- **Variable-rate lending at scale.** Utilization-based rate models work. Billions of dollars flow through them daily.
- **Isolated risk markets.** Morpho Blue proved that isolated lending markets can work on-chain, reducing contagion relative to shared pools.

### Partially solved

- **Fixed-rate, fixed-term lending.** Term Finance and Morpho V2 are making progress, but scale remains limited compared to variable-rate pools.
- **Auction-based price discovery.** Term Finance demonstrates that repo-style auctions work on-chain, but participation is thin.
- **On-chain repo mechanics.** Solstice demonstrated the first true on-chain repo, but it is bilateral, institutional, and not yet a permissionless market.

### Unsolved

- **Collateral reuse with safety.** DeFi has not solved the rehypothecation problem. Either collateral is locked (no reuse, capital-inefficient) or it is reused without limits (capital-efficient, systemically dangerous).
- **True repurchase commitment.** No DeFi protocol enforces a repurchase obligation. Borrowers can extend indefinitely (Aave) or default without consequence (bad debt absorbed by the pool). In repo, the repurchase is the contract.
- **Bitcoin-native repo.** No protocol offers repo for BTC without wrapping it into another ecosystem. Lightning Pool and Magma come closest for Lightning liquidity, but they are channel-specific, not general-purpose BTC repo.
- **Yield curve construction.** Traditional repo markets produce yield curves (overnight, 1-week, 1-month, 3-month). No DeFi protocol has generated a reliable on-chain yield curve, though Term Finance's vision of weekly maturing repo tokens aims at this.
- **Cross-chain settlement for repo.** Solstice's cross-chain repo (Solana/Ethereum) is a start, but it required a third-party infrastructure provider (Membrane Labs). A Bitcoin-native repo would need to settle on Bitcoin's base layer.

### The gap a Bitcoin-native repo market would fill

ASPs and other Bitcoin L2 operators need short-term BTC funding at predictable rates for predictable terms. This is exactly what the repo market does in traditional finance. The current options are:
- **DeFi lending pools:** Wrong mechanics (variable rate, no term, no repurchase).
- **Lightning liquidity markets:** Right concept (fixed term, fixed rate) but specific to channel liquidity, not general BTC lending.
- **Institutional on-chain repo (Solstice):** Right mechanics but wrong asset (stablecoins) and wrong access model (permissioned, bilateral).
- **Nothing:** There is no permissionless, Bitcoin-native, fixed-term, fixed-rate repo market. This is the gap.

---

## 6. Devil's Advocate: Is DeFi Lending Good Enough?

The ASP does not technically need "repo." It needs short-term BTC funding. The question is whether Aave-style lending on a Bitcoin L2 would suffice, and what would be lost or gained compared to true repo mechanics.

### The case for DeFi lending being sufficient

**Simplicity.** Building an Aave-style lending pool on Stacks or Ark itself is dramatically simpler than building a full repo market. The smart contracts are well-understood, battle-tested across multiple L1s, and require no novel financial plumbing.

**Variable rates might be fine.** The ASP's funding need is predictable in aggregate but variable in timing. A utilization-based rate model would automatically increase rates when ASP demand for funding is high (which is when liquidity is scarce) and decrease them when demand is low. This is responsive in a way that fixed-term repo is not.

**No term mismatch.** With Aave-style lending, the ASP borrows when it needs to and repays when VTXOs expire. There is no term to manage, no rollover risk, no maturity mismatch. The ASP's ~28-day liquidity gap maps naturally to an open-ended borrowing position.

**Liquidation as discipline.** If the ASP's collateral (the expiring VTXOs it will reclaim) declines in value relative to its borrowing, liquidation forces the ASP to manage risk. This is a feature, not a bug.

### What would be lost compared to true repo

**Rate certainty.** The ASP cannot predict its funding cost. In a market stress event, utilization could spike and rates could go from 3% to 30% in a single block. With repo, the rate is locked at trade execution. An ASP managing thin margins cannot absorb unpredictable funding costs.

**No collateral reuse.** In a lending pool, the ASP's collateral sits locked. In repo, the lender can reuse the collateral, which increases overall capital velocity in the system. For a Bitcoin L2 where capital efficiency is the core problem, this matters.

**No term structure.** Without fixed terms, there is no yield curve. Without a yield curve, there is no price signal for the time-value of BTC. The ASP cannot distinguish between overnight funding (cheap) and 28-day funding (expensive). Everything is priced at the same variable rate.

**No bilateral relationship.** Pool-based lending is anonymous. Repo is typically bilateral or tri-party, enabling relationship-based pricing, credit assessment, and bespoke terms. An ASP that demonstrates reliable repayment history should get better rates over time. Pool lending does not reward this.

**Liquidation is catastrophic, not corrective.** If an ASP gets liquidated, it loses control of the BTC backing its users' VTXOs. This is not the same as a trading position being liquidated. It is a system failure that affects every user of the ASP. Repo's margin-call-with-cure-period model is better suited to systemically important infrastructure.

### Verdict

DeFi lending could serve as a minimum-viable stopgap. An Aave-style pool on Stacks or another Bitcoin L2 would give ASPs access to short-term funding today, without waiting for novel repo infrastructure. But it would not solve the deeper problems: rate certainty, capital efficiency through collateral reuse, term structure pricing, and safe handling of systemically important collateral. For a mature ASP ecosystem with significant BTC under management, the lending pool model is insufficient. The question is whether the market gets large enough to justify building the harder thing.

---

*End of survey.*

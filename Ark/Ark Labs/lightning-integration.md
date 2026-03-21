# Ark-Lightning Integration

Research notes on how Ark interacts with the Lightning Network, with implications for a repo-like liquidity market.

---

## 1. VTXOs Paying Lightning Invoices

### 1.1 Mechanism

The ASP acts as a Lightning gateway. When an Ark user wants to pay a BOLT11 invoice:

1. The user submits the BOLT11 invoice to the ASP.
2. The ASP creates an HTLC (Hash Time-Locked Contract) on the Lightning Network, forwarding the payment to the invoice's destination.
3. Simultaneously, the user forfeits a VTXO (or portion of a VTXO) to the ASP as payment.
4. The swap is atomic: if the Lightning payment fails, the VTXO forfeit is rolled back. If the Lightning payment succeeds (preimage revealed), the ASP keeps the forfeited VTXO value.

From the user's perspective, they spend a VTXO and a Lightning invoice gets paid. The mechanics are transparent.

### 1.2 What the User Sees

From the barkgui implementation, Lightning send is exposed as:
- Input: a BOLT11 invoice string.
- Output: payment status (success/failure) with the payment hash.
- The wallet handles VTXO selection, ASP communication, and forfeit signing automatically.

The bark CLI exposes this as `bark send <bolt11_invoice>` -- the same command used for Ark payments, with the wallet auto-detecting the payment type.

### 1.3 BOLT12 and Lightning Address Support

The barkgui implementation also exposes:
- **Lightning Address payments**: Input a Lightning address + amount + optional comment.
- **BOLT12 offer payments**: Input a BOLT12 offer string + amount.

These suggest the ASP gateway supports modern Lightning payment protocols beyond basic BOLT11.

---

## 2. The ASP as Lightning Gateway

### 2.1 Architecture

The ASP is simultaneously:
- An Ark operator (manages rounds, VTXOs, connector trees).
- A Lightning node (maintains channels, routes payments).
- A swap service (converts between Ark VTXOs and Lightning HTLCs).

This is a deliberate design choice. Because every ASP is also an LSP (Lightning Service Provider), Ark users get Lightning access without managing their own channels.

### 2.2 Trust Model for Lightning Payments

**Outgoing Lightning payments** (user pays invoice via ASP):
- Atomic via HTLCs. The ASP cannot steal funds -- either the payment succeeds (preimage revealed, ASP earns the fee) or it fails (VTXO returned to user).
- No additional trust beyond what Lightning itself requires.
- Steven Roose (Second) describes this as having "no counterparty risk."

**Incoming Lightning payments** (user receives via ASP):
- The ASP generates a BOLT11 invoice on behalf of the user.
- When payment arrives, the ASP creates a new VTXO for the user.
- The HTLC atomicity ensures the user gets their VTXO if and only if the Lightning payment succeeds.
- However, this is an OOR-style VTXO (spend VTXO), so the user trusts the ASP not to double-spend until they refresh in the next round.

From the barkgui implementation, incoming Lightning involves:
1. Creating an invoice (`ln_create_amount` -> `ln_created_invoice`).
2. Checking pending receives (`pending_lightning_receives`).
3. Claiming received payments (`ln_claim`).

### 2.3 Fee Structure

The ASP charges fees for Lightning operations. From the barkgui's `ParsedArkInfo` struct:

- `ln_receive_base_fee_sat`: Fixed base fee for receiving Lightning payments.
- `ln_receive_ppm`: Parts-per-million fee on the received amount.

Outgoing Lightning payment fees are not explicitly broken out in the barkgui code -- they may be embedded in the Lightning invoice's routing fees or charged as a VTXO service fee.

---

## 3. HTLCs/PTLCs for Atomic Swaps

### 3.1 HTLC-Based Swaps

The current implementation uses HTLCs (Hash Time-Locked Contracts) for Ark-Lightning atomic swaps:

1. A payment hash H is derived from a secret preimage R.
2. The Lightning payment is conditional on revealing R.
3. The Ark VTXO forfeit is conditional on the same R being revealed.
4. Either both succeed (R is revealed, Lightning payment settles, VTXO is forfeited) or both fail.

This is the same atomic swap primitive used throughout the Lightning Network.

### 3.2 PTLC Future

PTLCs (Point Time-Locked Contracts) are referenced in the Ark protocol spec as a future improvement:

- PTLCs use Schnorr signature adaptor techniques instead of hash preimages.
- They provide better privacy (no common hash linking sender and receiver across the route).
- They enable more complex conditional payments.
- Bitcoin's Taproot upgrade (active since November 2021) provides the Schnorr signature infrastructure needed for PTLCs.

Neither Arkade nor bark currently implement PTLCs for Ark-Lightning swaps. This is a protocol-level future enhancement, not an implementation gap.

### 3.3 Implications for Repo Contracts

HTLC/PTLC atomic swaps could be the mechanism for repo settlement:

- **Repo open**: Borrower atomically forfeits collateral VTXO while receiving loan VTXO (or Lightning payment for the loan amount).
- **Repo close**: Borrower atomically returns loan + interest while receiving collateral VTXO back.
- HTLCs ensure neither party can cheat -- the swap is all-or-nothing.

The challenge: standard HTLCs are time-bounded. A repo with a 7-day term would need the HTLC timelock to span 7 days, which is pushing the limits of Lightning's typical HTLC timeout windows. This may require custom Ark-level constructions rather than standard Lightning HTLCs.

---

## 4. Multi-ASP Payments via Multi-Part Lightning

### 4.1 The Problem

In the current design, each Ark instance is a single ASP. Users of different ASPs cannot transact directly via Ark OOR payments -- they are on separate "islands."

### 4.2 Lightning as the Bridge

Lightning serves as the inter-ASP settlement rail:

1. User A (on ASP-1) wants to pay User B (on ASP-2).
2. User A pays a Lightning invoice via ASP-1's Lightning gateway.
3. The payment routes through the Lightning Network to ASP-2.
4. ASP-2 creates a VTXO for User B.
5. The payment is atomic end-to-end via HTLC chains.

### 4.3 Multi-Part Payments (MPP)

For large payments that exceed any single channel's capacity, Lightning's multi-part payment (MPP) feature allows splitting across multiple routes. Multiple ASPs could potentially serve as independent routing hops, though this is speculative and not explicitly implemented.

The Ark protocol spec mentions multi-ASP payments via multi-part Lightning, but current implementations focus on single-ASP operations.

### 4.4 Practical Status

This is more theoretical than operational. Current Ark deployments are single-ASP. Cross-ASP payments via Lightning work in principle (both ASPs just need to be Lightning nodes) but there are no published examples of multi-ASP routing in production.

---

## 5. Liquidity Implications

### 5.1 Double Liquidity Burden

The ASP must maintain two separate liquidity pools:

1. **Ark liquidity**: Capital locked in VTXO trees. The ASP fronts the entire payment volume for the duration of each VTXO's lifetime (~30 days). If the ASP expects $10M in monthly volume, it needs at least $10M in Ark liquidity.

2. **Lightning liquidity**: Channel capacity for routing payments. The ASP needs both inbound and outbound capacity on its Lightning channels. This is separate from Ark liquidity.

The total capital requirement is roughly: `Ark_volume * VTXO_lifetime + Lightning_channel_capacity`.

### 5.2 V2 Revocation Helps

Ark V2's revocation mechanism reduces the Ark liquidity burden by allowing the ASP to reclaim capital before VTXO expiry (as users spend and reveal revocation secrets). This shortens the effective lockup period from ~30 days to the average time between VTXO creation and spend.

### 5.3 Fulmine's Role

Fulmine (Ark Labs' wallet daemon) is specifically designed to help operators manage this dual liquidity:
- Optimizes Lightning channel rebalancing by routing through Arkade settlement.
- Enables swap providers to convert between Ark and Lightning liquidity positions.
- Reduces the need for on-chain transactions when rebalancing.

### 5.4 Comparison to Lightning-Only

| Dimension | Lightning Only | Ark + Lightning |
|-----------|---------------|-----------------|
| User onboarding | Channel open (on-chain tx + inbound liquidity) | Boarding or OOR receive (simpler) |
| Liquidity type | Channel capacity (bilateral) | Ark pool (unilateral) + channel capacity |
| Rebalancing | On-chain or submarine swaps | Ark rounds or Fulmine swaps |
| Total capital needed | Channel capacity | Ark pool + channel capacity (higher) |
| User experience | Complex (channels, routing) | Simpler (single balance, ASP handles routing) |

---

## 6. Lightning as Inter-ASP Settlement Rail

### 6.1 Feasibility

Lightning is the natural candidate for inter-ASP settlement because:
- Both ASPs already run Lightning nodes (required for gateway functionality).
- Lightning HTLCs provide atomic settlement.
- No new protocol is needed -- standard Lightning routing works.
- Payment amounts can be split across multiple channels via MPP.

### 6.2 Limitations

- **Latency**: Lightning payments are fast (~seconds) but not instant at the protocol level. For high-frequency inter-ASP settlement, this may be a bottleneck.
- **Routing failures**: Large Lightning payments can fail due to insufficient channel capacity along routes. This is a known Lightning scalability challenge.
- **Fee accumulation**: Each Lightning hop adds fees. Inter-ASP payments via Lightning may be more expensive than intra-ASP payments.
- **Privacy**: Lightning routing exposes payment amounts and timing to intermediate nodes. Inter-ASP settlement patterns could reveal business intelligence about Ark usage.

### 6.3 Alternative: On-Chain Settlement

ASPs could settle directly on-chain (UTXO transfers) rather than via Lightning. This is slower but more reliable for large amounts. In practice, a hybrid approach is likely: Lightning for small/frequent settlements, on-chain for large/infrequent ones.

### 6.4 Implications for Multi-ASP Repo Markets

A repo market spanning multiple ASPs would require reliable inter-ASP settlement. If ASP-1 holds the collateral and ASP-2 holds the loan, closing the repo requires an atomic cross-ASP swap. Options:

1. **Lightning HTLC chain**: Atomic but subject to Lightning routing limitations.
2. **On-chain atomic swap**: Reliable but slow and expensive.
3. **Both parties on the same ASP**: Simplest but centralizes the market.

For a practical first implementation, a single-ASP repo market is far more feasible than a multi-ASP one.

---

## Devil's Advocate: Lightning Integration Risks

### ASP as Single Point of Failure for Lightning

If the ASP's Lightning node goes down, all Ark users lose Lightning access. There is no fallback -- unlike a standalone Lightning wallet that can connect to any LSP.

### Fee Opacity

The ASP can charge whatever it wants for Lightning gateway services. Users have no way to route around the ASP or choose a cheaper gateway. The ASP is a monopoly provider of Lightning access for its users.

### Incoming Lightning Trust Gap

Receiving Lightning payments results in spend VTXOs (OOR-style) that require trust in the ASP until the next round. For a repo market, this means Lightning-received loan proceeds are not fully trustless until refreshed.

### Capital Efficiency Paradox

The Ark protocol was partly designed to solve Lightning's inbound liquidity problem. But the ASP needs even more capital than a Lightning node alone -- it needs both Ark pool liquidity and Lightning channel liquidity. This raises the question: does Ark actually improve capital efficiency, or does it shift the burden from many small users to one large operator?

The answer depends on utilization rates. If the ASP's Ark and Lightning liquidity is highly utilized (high turnover, many users), the per-user capital cost drops. If utilization is low, the ASP bears a disproportionate capital burden.

---

## Sources

- [Second - Intro to Ark Protocol](https://second.tech/docs/learn/intro)
- [Second - First Ark Mainnet Transactions](https://blog.second.tech/demoing-the-first-ark-transactions-on-bitcoin-mainnet/)
- [Ark Protocol - Main Site](https://ark-protocol.org/)
- [Bitcoin Optech - Ark Protocol](https://bitcoinops.org/en/topics/ark/)
- [CoinDesk - Solving Lightning's Inbound Liquidity Problem](https://www.coindesk.com/tech/2023/06/02/solving-lightnings-inbound-liquidity-problem-is-focus-of-new-layer-2-bitcoin-protocol)
- [Bitcoin Magazine - Bitcoin Layer 2: Ark](https://bitcoinmagazine.com/technical/bitcoin-layer-2-ark)
- [Bitcoin Magazine - Assessing Lightning's Last-Mile Solutions](https://bitcoinmagazine.com/technical/assessing-the-lightning-networks-last-mile-solutions)
- [GitHub - ArkLabsHQ/fulmine](https://github.com/ArkLabsHQ/fulmine)
- [Ark Labs - Fulmine](https://arklabs.xyz/fulmine)
- [Ark Labs - Arkade Goes Live](https://blog.arklabs.xyz/press-start-arkade-goes-live/)
- [Neha Narula - Another Explanation of How Ark Works](https://nehanarula.org/2025/05/20/ark.html)
- barkgui source: `TBB/JC Bitcoin/barkgui/src/main.rs` (lines 163-204, 278-364, 596-608)

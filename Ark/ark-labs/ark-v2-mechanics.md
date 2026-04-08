# Ark V2 Protocol Mechanics

Research notes for evaluating Ark as infrastructure for a repo-like liquidity market.

---

## 1. VTXO Lifecycle

A VTXO (Virtual Transaction Output) is a series of pre-signed Bitcoin transactions held off-chain by a user that provide the ability to create an on-chain UTXO at a later time, if required. VTXOs are to Ark what UTXOs are to Bitcoin L1 -- the fundamental unit of value.

### 1.1 Creation (Boarding)

BTC enters the Ark system through **boarding UTXOs**:

1. The user creates a funding transaction with one UTXO that can be spent either (a) cooperatively by the user + ASP together, or (b) unilaterally by the user alone after a timelock.
2. The user broadcasts this transaction on-chain and waits for confirmations.
3. Once confirmed, the user contacts the ASP, who includes the boarding UTXO in the next round's commitment transaction.
4. The user now holds a **board VTXO** -- the simplest tree structure (root -> leaf, 2 transactions total).

Board VTXOs are fully trustless. The ASP cannot prevent the user from exiting. Default lifetime is ~30 days (configurable by server policy).

Alternative onboarding: new users can skip boarding entirely and receive VTXOs directly from existing Ark participants via OOR payments. This is the most common entry point for new users.

### 1.2 Ownership

Each VTXO leaf encodes a bifurcated spending policy:

- **Cooperative path**: 2-of-2 MuSig2 between the user's pubkey (A) and the ASP's pubkey (S). Used for normal operations.
- **Timelocked recovery path**: User can spend alone after a relative timelock (CSV, ~60 blocks / ~10 hours for leaves). Used for emergency exits.

Intermediate tree nodes (root and branches) use n-of-n MuSig2 for the cooperative path and CLTV absolute timelocks for server recovery after expiry.

### 1.3 Transfer (OOR Spend)

Payments between Ark users happen **out-of-round (OOR)**, also called "arkoor":

1. Sender co-signs a new leaf transaction with the ASP, creating a **spend VTXO** for the receiver.
2. The spend VTXO extends the sender's existing transaction tree by appending a new leaf.
3. Settlement is near-instantaneous -- no round wait required.
4. Change from the transaction returns to the sender as a separate spend VTXO.

Trust assumption: the receiver must trust that the sender and ASP do not collude to double-spend the leaf. This trust requirement is eliminated once the receiver refreshes into the next round.

Spend VTXOs inherit the remaining lifetime of their source VTXO -- spending does not reset the expiration clock.

### 1.4 Refresh (In-Round Swap)

Refreshing converts an expiring (or trust-dependent) VTXO into a fresh, fully trustless VTXO:

1. The user registers for the next ASP-coordinated round.
2. The user signs a **forfeit transaction** that transfers their old VTXO to the ASP.
3. The ASP constructs a new shared UTXO tree containing a fresh VTXO for the user.
4. Atomicity is guaranteed via **connector outputs** -- the forfeit transaction is only valid if the round's commitment transaction confirms on-chain. The user cannot lose their old VTXO without receiving the new one.
5. The user receives pre-signed branch and leaf transactions for their new position in the tree.

Refresh resets the ~30-day expiry clock and eliminates any trust dependency from prior OOR payments.

### 1.5 Expiry

If a user fails to refresh before the VTXO's absolute timelock expires:

- The VTXO becomes spendable by either the user or the ASP.
- In practice, the ASP sweeps expired round trees to reclaim liquidity.
- The user's funds are effectively lost if they do not act before expiry.

This is the critical liveness requirement: users must come online at least once within each ~30-day VTXO lifetime to refresh.

### 1.6 Exit

#### Cooperative Exit (Offboarding)

The user participates in a round, forfeiting their VTXO and receiving a standard on-chain UTXO in the round transaction's outputs. This is the cheapest exit path -- the user pays only their share of the round's on-chain fee.

#### Unilateral Exit (Emergency)

When the ASP is unresponsive or uncooperative:

1. The user broadcasts their pre-signed transaction chain: root -> branch(es) -> leaf.
2. Each branch transaction has a relative timelock (CSV) of ~60 blocks (~10 hours) that must elapse before the next transaction in the chain can be broadcast.
3. After broadcasting the final leaf, the user waits the leaf's CSV period, then claims their bitcoin.

Cost scales with tree depth. Ark uses quad trees (4-way splits at each branch level), so exit transaction count scales logarithmically:

| Users in tree | Branch layers | Total exit txs |
|---------------|---------------|----------------|
| 4             | 1             | 2              |
| 16            | 2             | 3              |
| 64            | 3             | 4              |
| 256           | 4             | 5              |
| 1,024         | 5             | 6              |

Each exit transaction requires its own on-chain fee. In a high-fee environment, unilateral exit becomes uneconomical for small VTXOs -- a VTXO worth less than the cumulative exit fees is effectively non-redeemable on L1.

Additionally, spend VTXO chains (from OOR payments) add one transaction per hop to the exit path, further increasing costs. A VTXO that has been transferred OOR multiple times without refresh will have an increasingly expensive exit path.

---

## 2. Round Mechanics

### 2.1 ASP Coordination

The ASP (Ark Service Provider) is a server that coordinates rounds, provides liquidity, and serves as a Lightning gateway. It is not a custodian -- users retain unilateral exit rights at all times.

### 2.2 Round Timing

Rounds are periodic and configurable per ASP. Expected interval: ~1 hour (configurable from 15 minutes to several hours). Each ASP sets its own schedule.

### 2.3 Round Process

1. **Registration**: Users with VTXOs to refresh or payments to settle register with the ASP before the round cutoff.
2. **Tree Construction**: The ASP constructs two covenant trees:
   - **Output tree**: Contains all new VTXOs created during the round.
   - **Connector tree**: Contains connector outputs (one per input VTXO), used to ensure atomicity.
3. **Collaborative Signing**: In the covenant-less (clArk) variant, all participants must sign the complete VTXO tree. Each user generates an ephemeral key, signs, then deletes the key. This produces a pseudo-covenant -- secure as long as at least one participant in the group deletes their key.
4. **Forfeit Signing**: Each user who is forfeiting an old VTXO signs a forfeit transaction that spends their old VTXO to the ASP. The forfeit includes a connector output from the connector tree as an input, making it valid only if the round confirms.
5. **Commitment Transaction**: The ASP broadcasts the root of the output tree on-chain. This single on-chain transaction anchors all the round's VTXOs.
6. **Distribution**: Each user stores their branch and leaf transactions offline as their "VTXO package" -- proof of ownership and exit capability.

### 2.4 Atomicity via Connectors

The connector mechanism is the key safety feature of rounds. Each forfeit transaction includes a connector output as an input. Since the connector output only exists if the round's commitment transaction confirms, the forfeit transaction is invalid without the round confirming. This means:

- Users cannot lose their old VTXOs without receiving new ones.
- The ASP cannot steal funds by accepting forfeits without broadcasting the round.
- The entire process is atomic at the Bitcoin protocol level.

---

## 3. Covenant Trees (Shared UTXOs)

### 3.1 Structure

A single on-chain UTXO is logically split among many users through a **transaction tree**:

- **Root transaction**: The only on-chain transaction. Creates the shared UTXO.
- **Branch transactions**: Off-chain. Each splits value among child nodes (4-way in quad trees).
- **Leaf transactions**: Off-chain. Each pays to an individual user's VTXO script.

The tree is a binary/quad structure where each internal node is a pre-signed transaction spending from its parent.

### 3.2 Ownership Proof

Users prove ownership by holding the complete set of pre-signed transactions from the root to their leaf. This chain of transactions constitutes their VTXO package. To exit, they broadcast this chain sequentially.

### 3.3 Scaling Properties

The tree structure optimizes for individual exit cost at the expense of aggregate exit cost:

- If one user exits: they broadcast log4(N) transactions (efficient).
- If all users exit: the total on-chain footprint is N leaf transactions + all intermediate branches (expensive, but each user only pays for their own path).

The V-PACK standard provides "stateless VTXO verification" -- a portable proof format that allows independent auditability and sovereign recovery across Ark implementations.

---

## 4. V2 Revocation Branches

### 4.1 The V1 Problem: Capital Lockup

In Ark V1, the ASP's liquidity is locked for the full VTXO lifetime (~4 weeks). Even after all users in a round have spent their VTXOs, the ASP cannot reclaim the on-chain UTXO until the absolute timelock expires. This creates a massive capital inefficiency -- the ASP needs enough liquidity to cover all active rounds simultaneously.

### 4.2 V2 Solution: Revocation

Ark V2 introduces a revocation mechanism inspired by Lightning Network's penalty scheme:

- Each VTXO owner holds an individual **revocation secret**.
- When a user spends a VTXO (via OOR payment or refresh), they reveal their revocation secret to the ASP.
- When a sufficient number of VTXO owners in a tree have revealed their secrets, the ASP can aggregate them: `aggregate_secret = sec1 + sec2 + sec3 + ... + secN`.
- With a valid signature from this aggregate secret, the ASP can access the corresponding leaf in the **revocation branch**, reclaiming liquidity immediately.

### 4.3 TapTree Structure

Each shared UTXO's script is organized as a Taproot tree with two upper branches:

- **Left upper TapBranch**: Contains the **sweep branch** (unchanged from V1 -- ASP reclaims after full expiry) and the **unroll branch** (users can exit by unrolling the tree).
  - Key change in V2: the unroll branch can no longer be triggered at any time. It is only available **after 2 weeks from tree creation**. This gives the ASP a window to use the revocation branch first.
- **Right upper TapBranch**: The **revocation branch**, containing various combinations of revocation possibilities corresponding to different subsets of users who have revealed their secrets.

### 4.4 Implications for Capital Efficiency

In practice, the ASP's capital lockup period shrinks from the full VTXO lifetime (~4 weeks) to the time it takes for enough users to spend their VTXOs and reveal their secrets. In an active system with high turnover, the ASP may reclaim liquidity within hours or days rather than weeks.

The 2-week delay on the unroll branch is designed to prevent users from racing the ASP's revocation claim. If a user tries to exit after revealing their revocation secret, the ASP can use the revocation branch (available immediately) before the user can use the unroll branch (available only after 2 weeks).

### 4.5 Comparison to Lightning Penalties

| Property | Lightning Penalty | Ark V2 Revocation |
|----------|------------------|-------------------|
| Secret type | Per-channel revocation key | Per-VTXO revocation secret |
| Aggregation | No | Yes (secrets are summed) |
| Punishment | Counterparty loses all channel funds | ASP reclaims specific tree portion |
| Scope | Bilateral (2 parties) | Multilateral (many users + ASP) |
| Trigger | Broadcasting old state | Sufficient secret aggregation |

---

## 5. Onboarding

### 5.1 Boarding Process

1. User generates a boarding address (encodes the cooperative and timelock spending conditions).
2. User sends BTC to this address on-chain.
3. User waits for block confirmations (typically 1-6 depending on ASP policy).
4. ASP recognizes the boarding UTXO and includes it in the next round.
5. User receives a board VTXO -- a simple 2-transaction tree (root -> leaf).

### 5.2 Costs

- On-chain transaction fee for the funding transaction.
- ASP boarding fee: base fee + parts-per-million (PPM) on the boarded amount.
- From the barkgui implementation, the ASP exposes `board_base_fee_sat` and `board_ppm` parameters.

### 5.3 Alternative: Receive OOR

New users can bypass boarding entirely by receiving an OOR payment from an existing Ark user. This is faster (no on-chain confirmation wait) but introduces the temporary OOR trust assumption until refresh.

---

## 6. Offboarding

### 6.1 Cooperative Exit (via Round)

The preferred method. User participates in a round, forfeiting their VTXO and specifying an on-chain destination address. The round's commitment transaction includes an output paying to that address. Cost: shared round fee only.

From the barkgui implementation, this is exposed as the "offboard" action on individual VTXOs, with a destination address field.

### 6.2 Unilateral Exit

When the ASP is uncooperative:

1. User broadcasts their pre-signed transaction chain from root to leaf.
2. Each transaction requires a ~60-block CSV delay (~10 hours) before the next can be broadcast.
3. Total time: (tree_depth + 1) * ~10 hours.
4. Total cost: (tree_depth + 1) on-chain transaction fees.

For a tree with 256 users (4 branch layers): 5 transactions, ~50 hours, 5x on-chain fees.

For spend VTXOs with OOR chains: add 1 transaction + 10 hours per OOR hop.

### 6.3 When Unilateral Exit Becomes Uneconomical

A VTXO is effectively non-redeemable on L1 when:

```
vtxo_amount < sum_of_exit_fees(tree_depth + oor_chain_length)
```

At 10 sat/vbyte, a typical exit transaction costs ~2,000-3,000 sats. For a 5-transaction exit path, that is 10,000-15,000 sats minimum. VTXOs under this threshold have a weaker security model -- they rely entirely on ASP cooperation for exit.

In a fee spike (e.g., 100 sat/vbyte), this threshold rises 10x, potentially making VTXOs under 100,000-150,000 sats non-redeemable unilaterally.

---

## 7. Out-of-Round (OOR) Payments

### 7.1 Mechanics

1. Sender initiates a payment to a receiver's Ark address.
2. The ASP co-signs a new leaf transaction extending the sender's VTXO tree.
3. The receiver gets a **spend VTXO** -- an extension of the sender's tree.
4. Settlement is near-instantaneous (no round wait, no on-chain confirmation).

### 7.2 Trust Assumption

The receiver must trust that the sender and ASP do not collude to double-spend. The sender could theoretically sign a conflicting transaction with the ASP that spends the same VTXO to a different destination.

This is sometimes described as a "statechain model" for spend VTXOs.

### 7.3 Eliminating Trust via Refresh

Once the receiver participates in the next round and refreshes their spend VTXO into a fresh refresh VTXO, the trust assumption is eliminated. The forfeit/connector atomicity mechanism ensures the refresh is trustless.

Practical implication: for low-value payments (coffee), the OOR trust assumption may be acceptable. For high-value payments, the receiver should wait for the next round to refresh before considering the payment final.

### 7.4 Limits and Constraints

- Spend VTXOs inherit the remaining lifetime of their source VTXO. A VTXO near expiry cannot be meaningfully transferred OOR.
- Each OOR hop adds one transaction to the unilateral exit path, increasing exit cost.
- The ASP may impose maximum VTXO amounts (`max_vtxo_amount_sat` in the barkgui implementation).
- OOR payments are limited to other users of the same ASP (cross-ASP OOR requires Lightning bridging).

---

## Devil's Advocate: Critical Weaknesses

### Liveness Requirement

The ~30-day refresh requirement is a hard constraint. Users who go offline for a month lose their funds. This is fundamentally different from Bitcoin L1 (hold forever) or even Lightning (channels persist indefinitely with watchtowers). For a repo market, this means all collateral positions must be actively managed or delegated.

### ASP Centralization

Each Ark instance is a single ASP. There is no peer-to-peer network of ASPs. The ASP is a single point of failure for liveness (though not for safety -- users can always exit unilaterally). A repo market built on Ark would be dependent on the ASP's uptime and willingness to process rounds.

### Exit Cost Risk

Unilateral exit costs are unpredictable because they depend on future fee markets. A VTXO that is economically viable to exit today may become trapped in a fee spike. For a repo market, this means collateral that appears fully backed may be only partially redeemable in adversarial conditions.

### OOR Double-Spend Window

Between OOR payment and the next round refresh, the receiver is exposed to sender+ASP collusion. In a repo context, if the ASP is also the counterparty (or colluding with the counterparty), OOR-based collateral transfers are not safe until refreshed.

### Interactivity Burden

In the covenant-less variant (the only one deployable today), all round participants must be online simultaneously to sign the tree. This creates coordination overhead that scales with the number of participants. Future covenant support (CTV, TXHASH) would eliminate this requirement.

---

## Sources

- [Ark Protocol - VTXOs](https://ark-protocol.org/intro/vtxos/index.html)
- [Ark Protocol - Covenant-less Ark (clArk)](https://ark-protocol.org/intro/clark/index.html)
- [Ark Protocol - Connectors](https://ark-protocol.org/intro/connectors/index.html)
- [Ark Protocol - Main Site](https://ark-protocol.org/)
- [Bitcoin Optech - Ark Protocol](https://bitcoinops.org/en/topics/ark/)
- [Introducing Ark V2 - Burak (Medium)](https://brqgoo.medium.com/introducing-ark-v2-2e7ab378e87b)
- [Ark Labs Documentation](https://docs.arkadeos.com/)
- [Second - Intro to Ark Protocol](https://second.tech/docs/learn/intro)
- [Second - Ark VTXOs](https://second.tech/docs/learn/vtxo)
- [Neha Narula - Another Explanation of How Ark Works](https://nehanarula.org/2025/05/20/ark.html)
- [Ark: A UTXO-based Transaction Batching Protocol (PDF)](https://docs.arklabs.xyz/ark.pdf)
- [Second - First Ark Mainnet Transactions](https://blog.second.tech/demoing-the-first-ark-transactions-on-bitcoin-mainnet/)
- [Ark Protocol to Scale Bitcoin by Sharing UTXOs (teemupleb)](https://typefully.com/teemupleb/ark-protocol-to-scale-bitcoin-by-sharing-utxos-3CJcisv)

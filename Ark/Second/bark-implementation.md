# Bark Implementation (Second)

Research notes on Second's Ark implementation -- the bark wallet and ASP.

---

## 1. Bark Architecture

### 1.1 Overview

Bark is a Rust implementation of the Ark protocol on Bitcoin, built by Second. It consists of:

- **bark-wallet** (crate: `bark-wallet`): The core wallet library providing the full Ark wallet API.
- **bark CLI**: Command-line wallet for end users and developers.
- **bark ASP (aspd)**: Ark Service Provider server implementation.
- **bark-wallet library**: Reusable Rust library that other applications can embed (e.g., barkgui).

Repository: Originally on GitLab (`gitlab.com/ark-bitcoin/bark`), mirrored to Codeberg (`codeberg.org/ark-bitcoin/bark`) and GitHub.

### 1.2 Core Dependencies

From the barkgui source and bark-wallet crate:

- **BDK (Bitcoin Development Kit)**: HD wallet for on-chain operations. Wrapped in `Arc<TokioMutex>` for shared async access.
- **SQLite**: Persistent storage for wallet state, VTXOs, and transaction history via `SqliteClient`.
- **tokio**: Async runtime for all wallet operations.
- **MuSig2**: For cooperative multi-signature operations in VTXO trees.
- **bitcoin crate**: Bitcoin primitives (transactions, scripts, keys).
- **bip39**: Mnemonic seed phrase generation and recovery (12/24 words).

### 1.3 Data Model

From the barkgui source code, the core data types reveal bark's internal model:

**Wallet** (`bark::Wallet`): The primary interface. Provides:
- `balance()` -> `Balance` (spendable, pending, etc.)
- `sync()` -> Synchronize with ASP and blockchain
- `new_address()` -> Generate Ark receiving address
- `ark_info()` -> Query ASP configuration (round interval, expiry delta, fees, nonces)
- `vtxos()` -> List all VTXOs with metadata
- `pending_boards()` -> List boarding UTXOs awaiting confirmation
- `pending_lightning_receives()` -> List unclaimed Lightning invoices
- `history()` -> Full movement history

**WalletVtxo**: Wraps a VTXO with wallet-specific state:
- `id()` -> VTXO identifier string
- `amount()` -> Bitcoin amount
- `expiry_height()` -> Block height when VTXO expires
- `policy_type()` -> Script policy type
- `user_pubkey()` / `server_pubkey()` -> Key pair involved
- `exit_delta()` -> Relative timelock (CSV blocks) for unilateral exit
- `exit_depth()` -> Number of transactions in the exit path
- `chain_anchor()` -> On-chain transaction this VTXO is anchored to
- `is_standard()` -> Whether the VTXO follows standard script templates
- `has_all_witnesses()` -> Whether all pre-signed witnesses are available for exit
- `state.kind()` -> VTXO state (active, spent, expired, etc.)

**Config**: ASP connection configuration:
- `server_address` -> ASP gRPC/HTTP endpoint
- `esplora_address` -> Esplora block explorer for chain data
- `network` -> Bitcoin network (Mainnet, Signet, Testnet)

**ArkInfo** (from ASP): Server-side parameters:
- `round_interval` -> Time between rounds
- `nb_round_nonces` -> Number of nonces pre-generated for rounds
- `vtxo_expiry_delta` -> VTXO lifetime in blocks
- `max_vtxo_amount` -> Maximum single VTXO size (optional cap)
- `fees.refresh` -> Base fee + PPM table by expiry proximity
- `fees.board` -> Boarding base fee + PPM
- `fees.lightning_receive` -> Lightning receive base fee + PPM

### 1.4 Wallet Operations (from barkgui API surface)

The barkgui implementation reveals the complete set of wallet operations bark exposes:

| Operation | bark API | Description |
|-----------|----------|-------------|
| Create wallet | `Wallet::create_with_onchain()` | New wallet from mnemonic |
| Open wallet | `Wallet::open_with_onchain()` | Load existing wallet |
| Sync | `wallet.sync()` | Sync with ASP + chain |
| Balance | `wallet.balance()` | Ark balance (spendable, pending) |
| Ark address | `wallet.new_address()` | New receiving address |
| On-chain address | Via BDK `OnchainWallet` | Standard Bitcoin address |
| Send OOR | `wallet.send_ark(dest, amount)` | Out-of-round Ark payment |
| Send on-chain | `wallet.offboard(dest, amount)` | Cooperative exit to address |
| Board | `wallet.board(amount)` | On-chain BTC -> Ark VTXO |
| List VTXOs | `wallet.vtxos()` | All VTXOs with full metadata |
| Refresh VTXO | `wallet.refresh_vtxos([id])` | Refresh specific VTXOs in next round |
| Offboard VTXO | `wallet.offboard_vtxos([id], dest)` | Exit specific VTXO cooperatively |
| Start exit | `wallet.start_exit([id])` | Begin unilateral exit for VTXO(s) |
| Progress exit | Via exit management | Advance exit transactions on-chain |
| Claim exit | Via exit management | Claim completed exit to destination |
| Lightning send | `wallet.send_lightning(invoice)` | Pay BOLT11 invoice |
| Lightning receive | `wallet.create_invoice(amount)` | Generate BOLT11 invoice |
| Lightning claim | `wallet.claim_lightning()` | Claim pending Lightning receives |
| Lightning address | `wallet.pay_lightning_address(addr, amt)` | Pay via Lightning address |
| BOLT12 offer | `wallet.pay_bolt12_offer(offer, amt)` | Pay BOLT12 offer |
| History | `wallet.history()` | Full movement history |
| Maintenance | Sync + register boards + progress exits + refresh | One-click full wallet upkeep |
| Drop VTXO | `wallet.drop_vtxo(id)` | Remove VTXO from wallet (advanced) |
| Peek address | Index-based address derivation | Debug/dev tool |
| Send many | Batch on-chain send | Multiple destinations in one tx |
| Drain | Sweep all on-chain funds to address | Empty BDK wallet |
| Offboard all | Exit all VTXOs cooperatively | Bulk cooperative exit |
| Exit all | Unilateral exit for entire wallet | Emergency full exit |

### 1.5 Movement History Model

The `Movement` type tracks all wallet activity:

- `id` -> Sequential identifier
- `status` -> Current state (pending, completed, failed)
- `subsystem_name` / `subsystem_kind` -> Which subsystem handled it (Ark, Lightning, on-chain)
- `intended_balance_sat` / `effective_balance_sat` -> Expected vs actual balance change
- `offchain_fee_sat` -> Ark/Lightning fees paid
- `sent_to` / `received_on` -> Addresses involved
- `input_vtxos` / `output_vtxos` / `exited_vtxos` -> VTXO flows
- `created_at` / `updated_at` / `completed_at` -> Timestamps

---

## 2. Second's Design Philosophy

### 2.1 Pure Bitcoin Focus

Second focuses exclusively on Bitcoin -- no stablecoins, no asset issuance, no programmable finance beyond payments. Their tagline: "Scalable Bitcoin Payments With Ark & Lightning."

This contrasts sharply with Ark Labs' Arkade, which positions itself as "an operating system for bitcoin" with assets, lending, and trading capabilities.

### 2.2 Open Protocol, Not Platform

Second treats Ark as an open protocol specification, not a proprietary platform. Their documentation focuses on the protocol itself rather than SDK marketing. The code is hosted on GitLab/Codeberg (not GitHub) -- a deliberate choice signaling independence from Microsoft/GitHub's ecosystem.

### 2.3 CLI-First, GUI-Second

The primary interface is the bark CLI -- a terminal-only experience. The barkgui (the source we analyzed) is a community/third-party tool built on top of bark-wallet, not an official Second product. This CLI-first approach prioritizes developer tooling and scriptability over end-user polish.

### 2.4 Signet-Only (Currently)

As of this research, bark only supports **signet** (a Bitcoin testnet). It is explicitly experimental: "contains known bugs and vulnerabilities that can result in loss of funds and must not be used in production."

Second demonstrated the first Ark mainnet transactions in September 2024 (block 862149), but the mainnet support in bark is not considered production-ready.

---

## 3. Steven Roose (Ex-Blockstream)

### 3.1 Background

Steven Roose is the CEO of Second. He was previously at Blockstream, where he worked on Bitcoin protocol development, Liquid Network, and related infrastructure. His Blockstream experience informs bark's design in several ways:

- **Protocol correctness over features**: The bark codebase prioritizes getting the core Ark protocol right rather than shipping features quickly.
- **Rust-first**: Blockstream's Liquid uses Rust extensively (rust-bitcoin, rust-elements). Bark inherits this toolchain preference.
- **Skepticism of premature productization**: The "known bugs" warning and signet-only status reflect a Blockstream-style caution about shipping before the protocol is hardened.

### 3.2 Design Decisions

- **Single binary**: bark bundles wallet and ASP functionality in one codebase.
- **BDK integration**: Uses the Bitcoin Development Kit for on-chain wallet management, leveraging the broader Rust Bitcoin ecosystem.
- **MuSig2 native**: Bark implements MuSig2 for cooperative VTXO operations, aligned with Taproot's Schnorr signature capabilities.
- **Esplora backend**: Uses Esplora (block explorer API) for chain data rather than running a full node, simplifying deployment at the cost of some trust in the Esplora provider.

---

## 4. Barkgui Analysis

### 4.1 What barkgui Reveals

The barkgui source (`TBB/JC Bitcoin/barkgui/src/main.rs`, ~6000 lines) is a comprehensive egui desktop application that wraps the full bark-wallet API. Key observations:

**Full Protocol Coverage**: Every Ark operation is exposed -- boarding, OOR payments, Lightning (BOLT11, BOLT12, Lightning address), unilateral exits, cooperative exits, VTXO refresh, and more. This suggests the bark-wallet library has complete protocol coverage.

**VTXO Metadata Richness**: Each VTXO exposes exit_depth, exit_delta, chain_anchor, policy_type, and has_all_witnesses. This granularity is important for a repo market -- it means collateral VTXOs can be assessed for exit feasibility and cost.

**Fee Visibility**: The ASP's fee structure is fully exposed (boarding fees, refresh fees with PPM tables by expiry proximity, Lightning receive fees). This transparency enables economic modeling.

**Visualizations**: The barkgui includes a VTXO timeline visualization (horizontal bars from current tip to expiry height) and a liquidity lock gauge. These suggest the community sees VTXO lifecycle management as a first-class UX concern.

**Signet Default**: The wallet connects to `ark.signet.2nd.dev` by default, confirming the signet-only status.

### 4.2 API Surface Summary

The barkgui exercises these bark-wallet operations:

1. **Wallet lifecycle**: Create, open, sync, get config, get ark info
2. **Balance**: Ark balance (spendable/pending), on-chain balance (confirmed/pending/immature)
3. **Addresses**: Ark address, on-chain address, peek address (by index)
4. **Payments**: Ark OOR send, on-chain offboard, Lightning BOLT11 send, Lightning address send, BOLT12 offer send
5. **Receiving**: Lightning invoice creation, Lightning claim, board registration
6. **VTXO management**: List all VTXOs, refresh specific VTXOs, offboard specific VTXOs, start exit for specific VTXOs, drop VTXO
7. **Exit management**: List exits, progress exits, claim exits, exit entire wallet
8. **On-chain wallet**: Direct BDK sends, drain, send-many (batch)
9. **Maintenance**: Combined sync + register boards + progress exits + refresh VTXOs
10. **History**: Full movement log with subsystem tracking

### 4.3 What the Implementation Reveals About Ark's Practical Capabilities

**Positive signals:**
- The protocol is complete enough to build a full-featured wallet GUI.
- VTXO metadata is rich enough for programmatic collateral management.
- Lightning integration is bidirectional and supports modern protocols (BOLT12, Lightning addresses).
- Exit management is explicit and user-controlled, not hidden behind abstractions.

**Limitations revealed:**
- `has_all_witnesses` field suggests that some VTXOs may be missing pre-signed witnesses, which would prevent unilateral exit. This could be a data availability problem in practice.
- `exit_depth` being a separate field (not derivable from the VTXO's position in the tree) suggests that OOR chains can create arbitrarily deep exit paths, confirming the cost escalation concern.
- The "maintenance" operation (sync + register boards + progress exits + refresh) being a single button suggests these operations are expected to be done together and frequently -- the protocol requires active management.
- No multi-ASP support visible. The wallet connects to a single ASP and all operations go through it.

---

## 5. Practical Capabilities and Limitations for a Repo Market

### 5.1 What Bark Can Do Today

- **Hold collateral as VTXOs**: VTXOs with rich metadata (amount, expiry, exit cost) can represent collateral positions.
- **Transfer collateral atomically**: OOR payments enable instant collateral transfers between parties.
- **Settle via Lightning**: Loan disbursement and interest payments can flow through Lightning.
- **Programmatic control**: The bark-wallet library can be embedded in custom Rust applications (like barkgui does).
- **Monitor collateral health**: VTXO expiry tracking, exit depth, and fee estimation are available.

### 5.2 What Bark Cannot Do Today

- **No conditional VTXOs**: There is no way to create a VTXO with custom spending conditions (e.g., "spendable by borrower OR by lender after timeout"). VTXOs follow the standard Ark script template.
- **No multi-party VTXOs**: A VTXO belongs to one user. There is no escrow or multi-sig VTXO primitive.
- **No time-locked transfers**: Ark OOR payments are immediate and unconditional. There is no built-in mechanism for deferred or conditional transfers (needed for repo maturity).
- **No mainnet production**: Bark is signet-only and explicitly experimental.
- **No asset support**: Bark is pure BTC. No stablecoin-denominated VTXOs.

### 5.3 What Would Need to Be Built

A repo market on bark would require:

1. **Custom VTXO scripts**: Modify the leaf scripts to support conditional spending (time-locked, multi-party). This is a protocol-level change, not an application-level one.
2. **Escrow mechanism**: Either the ASP or a separate service would hold collateral VTXOs with rules about when they can be released.
3. **Interest calculation**: Off-chain logic for computing and settling interest payments.
4. **Maturity management**: Automatic refresh of collateral VTXOs before they expire, ensuring the repo can be closed at any time.
5. **Liquidation logic**: If the borrower defaults, the lender (or ASP) needs a mechanism to claim the collateral.
6. **Mainnet readiness**: Bark would need to reach production quality.

---

## Devil's Advocate: Bark as a Repo Foundation

### The Good

Bark's Rust implementation is well-structured, the API is comprehensive, and the VTXO metadata model is rich enough for collateral management. The bark-wallet library is designed to be embedded, which is exactly what a repo daemon would need. The team (Steven Roose, ex-Blockstream) has deep Bitcoin protocol expertise.

### The Bad

Bark is signet-only, explicitly buggy, and not production-ready. The pure-Bitcoin focus means no stablecoin support -- a repo market in BTC-only is volatile and limited in appeal. The single-developer-company risk is real: Second is a small team, and bark's development pace depends on their capacity.

### The Ugly

The fundamental problem is that Ark's VTXO script templates are fixed. A VTXO is `(user + ASP) OR (user after timeout)`. There is no room for a third party (lender) in this script. Building repo functionality requires either:

1. **Protocol-level changes** to Ark's VTXO scripts (hard, requires ASP support).
2. **Application-level workarounds** where the ASP acts as escrow (reintroduces custody/trust).
3. **A separate escrow layer** on top of Ark (adds complexity, may negate Ark's simplicity benefits).

None of these are easy, and all would need buy-in from the Ark protocol community.

---

## Sources

- [bark-wallet crate (crates.io)](https://crates.io/crates/bark-wallet)
- [bark-wallet documentation (docs.rs)](https://docs.rs/bark-wallet/latest/bark/)
- [bark GitLab repository](https://gitlab.com/ark-bitcoin/bark)
- [bark Codeberg mirror](https://codeberg.org/ark-bitcoin/bark)
- [Second - Official Site](https://second.tech/)
- [Second - First Ark Mainnet Transactions](https://blog.second.tech/demoing-the-first-ark-transactions-on-bitcoin-mainnet/)
- [Second - Ark Protocol Introduction](https://second.tech/docs/learn/intro)
- [Second - Ark VTXOs](https://second.tech/docs/learn/vtxo)
- [Blockspace Media - Steven Roose Interview](https://blockspace.media/podcast/ark-bitcoin-l2s-and-scaling-bitcoin-w-steven-roose/)
- [awesome-ark-protocol (GitHub)](https://github.com/aljazceru/awesome-ark-protocol)
- barkgui source: `TBB/JC Bitcoin/barkgui/src/main.rs`
- barkgui README: `TBB/JC Bitcoin/barkgui/README.md`

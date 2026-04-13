# docs.second.tech -- Scraped Content

**URL:** https://docs.second.tech/ark-protocol/intro
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\ARK – Layer 2.md
**Scraped:** 2026-04-12

---

Skip to main content

[Second Docs home page](/docs)

[Docs](/docs)[API reference](/docs/api-reference/overview)[Learn](/docs/learn/intro)[Changelog](/docs/changelog)[Forum](https://community.second.tech)[Chat](https://chat.second.tech)

Search...

Navigation

Learn

Intro to the Ark protocol

Search...

⌘K


##### Learn

  * [Introduction](/docs/learn/intro)
  * [VTXOs](/docs/learn/vtxo)
  * [Lifetime](/docs/learn/lifetime)
  * [Rounds](/docs/learn/rounds)
  * [Forfeits](/docs/learn/forfeits)
  * [Boarding](/docs/learn/board)
  * [Ark payments](/docs/learn/payments)
  * [On-chain payments](/docs/learn/payments-on-chain)
  * [Lightning payments](/docs/learn/payments-lightning)
  * [Offboarding](/docs/learn/offboard)
  * [Emergency exits](/docs/learn/exit)
  * [Liquidity](/docs/learn/liquidity)
  * [Fees](/docs/learn/fees)
  * [Glossary](/docs/learn/glossary)


On this page

  * Client-server
  * VTXO-based scaling
  * Round-based
  * Transaction trees
  * VTXO lifetime
  * Liquidity
  * Boarding
  * Offboarding
  * Emergency exits
  * Ark payments
  * Lightning payments
  * Beyond the basics


Learn

# Intro to the Ark protocol

Copy page

Copy page

The Ark protocol is a second layer on the bitcoin network. It offers: simple onboarding, low and predictable fees, instant payments, Lightning interoperability, and full control over your bitcoin. The Ark protocol works on bitcoin today and doesn’t require any new opcodes or changes in consensus rules.

## 

​

Client-server

The protocol centers around an _Ark server_. Users connect to the server to transact with one another directly over Ark. Ark users can also transact with the broader Lightning Network via the server’s _Lightning gateway_.

## 

​

VTXO-based scaling

Ark introduces a new scaling model based on [virtual UTXOs (VTXOs)](vtxo). A VTXO is a series of off-chain, pre-signed transactions that a user can broadcast at any time to retrieve their bitcoin on-chain in an emergency. Under normal operating conditions, these off-chain transactions will never be broadcast on-chain, and users will instead _off-board_ from the Ark protocol cooperatively with the Ark server. Although VTXOs are structurally more complex under the hood, they are based on the UTXO model and for the most part function in the same manner—anything you can do with a UTXO, you can do with a VTXO.

## 

​

Round-based

The Ark server [initiates and coordinates rounds](rounds) on a periodic basis. We’re expecting the optimal round interval to be in the region of an hour, but it’s configurable by each Ark server. In each round, users can _refresh_ their VTXOs—forfeit old VTXOs for new ones. Not all users of an Ark participate in every round. Only the users participating in the refresh have their VTXOs included in the round transaction.

## 

​

Transaction trees

During a round, the Ark server and users together [construct a transaction tree](vtxo#transaction-trees). Each _leaf_ of the tree (also known as an _exit transaction_) is controlled by a single user and corresponds to a single VTXO. The _root_ of the tree is broadcast on-chain and is known as a _round transaction_. Once the round transaction is confirmed, each user has verifiable assurance that they can unilaterally retrieve their bitcoin on-chain.

## 

​

VTXO lifetime

VTXOs must be refreshed on an ongoing basis because [VTXOs have a limited lifetime](lifetime). This is required by the protocol to enable the Ark server to claim all forfeited bitcoin in an expired round using a single on-chain transaction (_“sweeping”_), instead of many small transactions. Each VTXO includes a built-in expiration that’s set at creation. Users (or rather, their wallets) must spend or refresh their VTXOs before they expire, otherwise the VTXO technically becomes spendable by either the user _or_ the Ark server. VTXO lifetime is expected to be in the region of 30 days, though ultimately it’ll be determined by each Ark server’s configuration.

## 

​

Liquidity

Unlike Lightning, [Ark users don’t need to manage liquidity](liquidity)—the Ark server takes care of this for them. The Ark server must maintain liquidity for several operations, with refreshes being the most common. During a refresh, a user forfeits an old VTXO for a new one. The bitcoin in the forfeited VTXO will not be available to the Ark server until it expires, while the new VTXO requires immediate on-chain bitcoin for inclusion in the round transaction’s tree. This creates a temporary capital requirement for the Ark server, which will translate into user fees. [Ark’s fee structure](fees) (not yet defined) will need to reflect that refreshing newer VTXOs costs more, while refreshing VTXOs closer to the end of their lifetime costs less. Other liquidity-demanding operations include offboarding and Lightning payments. Transfers between Ark users don’t require liquidity—they are handled _out-of-round_.

## 

​

Boarding

To get bitcoin onto an Ark, a user co-signs a funding transaction with the Ark server and broadcasts it. The user does not need to wait for a round, but does need to wait for one or more on-chain block confirmations to complete the boarding. Importantly, new users do not need to go through the boarding process. They can start receiving VTXOs immediately (from someone else that has) upon setting up a wallet.

## 

​

Offboarding

Ark is an optimistic protocol. Under normal operations, users will withdraw bitcoin from Ark [using offboarding, not emergency exits](exit), which should be reserved for exceptional circumstances. To offboard, a user cooperates with the Ark server to [forfeit their VTXO(s)](forfeits) and receive an output to an on-chain bitcoin address of their choice. Like most processes on Ark, the offboard is atomic, so neither the Ark server nor the user are exposed to counterparty risk.

## 

​

Emergency exits

The availability of emergency exit is the key feature of the Ark protocol that puts users in total control of their off-chain bitcoin. However, emergency exits are expected to be reserved for emergency situations—e.g., the Ark server becomes unresponsive. To perform an emergency exit, a user broadcasts the pre-signed transactions that make up their VTXO in sequence, from root to branch to leaf. Each of these transactions breaks up the round transaction into successively smaller chunks until the user’s bitcoin is released to their own on-chain address. Since users’ VTXOs share branches in the transaction tree, each user’s emergency exit reduces the number of transactions required for subsequent users to complete their own emergency exits.

## 

​

Ark payments

Payments between Ark users happen at any time between rounds. The receiver obtains a new [spend VTXO](vtxo#spend-vtxos) that extends directly from the sender’s leaf in the transaction tree.

Because Ark payments bypass rounds entirely, they have zero liquidity costs and near-instantaneous settlement. However, there is a temporary trust trade-off: the receiver assumes that the sender and Ark server don’t collude to double-spend. As long as either the sender or server is honest, the payment is secure. And the receiver can [refresh](rounds) the VTXO in any subsequent round to restore the standard Ark trust model.

## 

​

Lightning payments

Ark users can send and receive [Lightning payments](payments-lightning) via the Ark server’s Lightning gateway. Users spend VTXOs to pay Lightning invoices and receive incoming Lightning payments as new VTXOs—no channels, inbound liquidity, or routing management required. Both directions use HTLCs to ensure payments are atomic.

## 

​

Beyond the basics

Now you’re up to speed with the fundamentals, it’s time to dive deeper! Whether you’re a developer looking to integrate with Ark or simply exploring the protocol’s design, we hope the following sections provide you the technical depth needed to fully understand Ark’s approach to bitcoin scaling.

Was this page helpful?

YesNo

[Ark VTXOsNext](/docs/learn/vtxo)

⌘I

Assistant

Responses are generated using AI and may contain mistakes.

[Contact support](mailto:hello@second.tech)

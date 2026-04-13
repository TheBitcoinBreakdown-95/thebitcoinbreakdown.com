# bitcoinops.org -- Scraped Content

**URL:** https://bitcoinops.org/en/newsletters/2023/09/27
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** Lightning ⚡️\httpsgithub.comJohnLaw2ln-scaling-covenantsblobmainscalingcovenants_v1.3.pdf.md
**Scraped:** 2026-04-12

---

[ ](/)

[en](/en/newsletters/2023/09/27/) | [ja](/ja/newsletters/2023/09/27/) | [es](/translations/ "No Spanish translation currently available") | [cs](/cs/newsletters/2023/09/27/) | [hi](/translations/ "No Hindi translation currently available") | [zh](/zh/newsletters/2023/09/27/) | [de](/translations/ "No German translation currently available") | [fr](/fr/newsletters/2023/09/27/) | [pt](/translations/ "No Portuguese translation currently available")

/ [home](/) / [newsletters](/en/newsletters/) / 

# Bitcoin Optech Newsletter #270

Sep 27, 2023 

This week’s newsletter describes a proposal to use covenants to significantly improve LN’s scalability. Also included are our regular sections summarizing popular questions and answers on the Bitcoin Stack Exchange, announcing new releases and release candidates, and describing notable changes to popular Bitcoin infrastructure software.

## News

  * ● **Using covenants to improve LN scalability:** John Law [posted](https://gnusha.org/url/https://lists.linuxfoundation.org/pipermail/lightning-dev/2023-September/004092.html) to the Bitcoin-Dev and Lightning-Dev mailing lists the summary of a [paper](https://github.com/JohnLaw2/ln-scaling-covenants) he’s written about creating very large [channel factories](/en/topics/channel-factories/) using [covenants](/en/topics/covenants/) and managing the resultant channels using adaptations of several previous protocols he’s described (see Newsletters [#221](/en/newsletters/2022/10/12/#ln-with-long-timeouts-proposal), [#230](/en/newsletters/2022/12/14/#factory-optimized-ln-protocol-proposal), and [#244](/en/newsletters/2023/03/29/#preventing-stranded-capital-with-multiparty-channels-and-channel-factories)).

He begins by describing a scalability problem with signature-based protocols that require participation from a large number of users, such as [coinjoins](/en/topics/coinjoin/) or previous factory designs: if 1,000 users agree to participate in the protocol but one of them becomes unavailable during signing, the other 999 signatures are useless. If, during the next attempt, another individual user becomes unavailable, the other 998 signatures collected in the second attempt are useless. He proposes covenants like [OP_CHECKTEMPLATEVERIFY](/en/topics/op_checktemplateverify/) and [SIGHASH_ANYPREVOUT](/en/topics/sighash_anyprevout/) as a solution to this problem: they are known to allow a single small transaction to restrict its funds to only being spent in one or more subsequent pre-defined child transactions. The subsequent transactions can also be limited by a covenant.

Law uses this mechanism to create a _timeout tree_ where a _funding transaction_ pays to a tree of pre-defined child transactions that are ultimately spent offchain into a large number of separate payment channels. A mechanism similar to the one used by Ark (see [Newsletter #253](/en/newsletters/2023/05/31/#proposal-for-a-managed-joinpool-protocol)) allows each of the payment channels to optionally be put onchain, but it also allows the factory funder to reclaim any channel funds that have not been put onchain after an expiry. This can be extremely efficient: an offchain timeout tree funding millions of channels can be created using a single small onchain transaction. After the expiry, the funds can be reclaimed by the factory funder in another small onchain transaction, with individual users withdrawing their funds over LN to their other channels prior to the factory expiration date.

The model above is compatible with the currently used LN-Penalty channel construction as well as the proposed [LN-Symmetry](/en/topics/eltoo/) mechanism. However, the remainder of Law’s paper looks at a modification of his proposed Fully Factory Optimized Watchtower Free (FFO-WF) protocol that provides several advantages for the covenant-based factory design. In addition to the advantages described in previous newsletters, such as only requiring _casual users_ to go online for a few minutes every few months and allowing _dedicated users_ to use their capital across channels more efficiently, a new advantage of the updated construction allows the factory funder to move funds for casual users from one factory (based on a particular onchain transaction) to another factory (anchored in a different onchain transaction) without requiring interaction from the user. That means casual user Alice who knows she needs to come online before the 6-month expiry of a factory may come online at month 5 to discover that her funds have already been rolled over to a new factory with another several months until expiry. Alice doesn’t need to do anything; she retains complete trustless control of her funds. This reduces the chance that Alice might come online very close to expiry, discover that the factory funder is temporarily unavailable, and be forced to put her part of the timeout tree onchain—incurring transaction fees and reducing overall network scalability.

Anthony Towns [replied](https://gnusha.org/url/https://lists.linuxfoundation.org/pipermail/lightning-dev/2023-September/004095.html) with a concern about what he called the “thundering herd” problem (called “forced expiration spam” in the [original LN paper](https://lightning.network/lightning-network-paper.pdf)) where the deliberate or accidental failure of a large dedicated user requires many other users to put many time-sensitive transactions onchain all at the same time. For example, a factory with a million users may require time-sensitive confirmation of up to a million transactions plus non-sensitive confirmation of up to two million more transactions for those users to put those funds back into new channels. It currently takes the network about a week to confirm three million transactions, so users of a million-user factory might want a factory to roll over their funds a few weeks before expiration—or perhaps several months early if they’re worried about several million-user factories having problems simultaneously.

A version of the original LN paper suggested that this problem could be addressed using an [idea](https://www.reddit.com/r/Bitcoin/comments/37fxqd/it_looks_like_blockstream_is_working_on_the/crmr5p2/) by Gregory Maxwell that would delay expiry when “blocks are full” (e.g., feerates are above the normal amount). In Law’s [reply](https://gnusha.org/url/https://lists.linuxfoundation.org/pipermail/lightning-dev/2023-September/004102.html) to Towns, he noted that he’s working on a specific design for a solution of that type which he will publish when he’s finished thinking through it. [__](/en/podcast/2023/09/28/#using-covenants-to-improve-ln-scalability)


## Selected Q&A from Bitcoin Stack Exchange

_[Bitcoin Stack Exchange](https://bitcoin.stackexchange.com/) is one of the first places Optech contributors look for answers to their questions—or when we have a few spare moments to help curious or confused users. In this monthly feature, we highlight some of the top-voted questions and answers posted since our last update._

  * ● [How did peer discovery work in Bitcoin v0.1?](https://bitcoin.stackexchange.com/a/119507) Pieter Wuille describes the evolution of the peer discovery mechanisms in Bitcoin Core from the IRC-based peer finding in the 0.1 release through hardcoded IP addresses to the DNS peer seeding currently used. [__](/en/podcast/2023/09/28/#how-did-peer-discovery-work-in-bitcoin-v0-1)

  * ● [Would a series of reorgs cause Bitcoin to break because of the 2-hour block time difference restriction?](https://bitcoin.stackexchange.com/a/119677) User fiatjaf asks whether a series of block chain reorgs, potentially the result of [fee sniping](/en/topics/fee-sniping/), could cause issues with Bitcoin’s block timestamp restrictions. Antoine Poinsot and Pieter Wuille describe the two block timestamp restrictions (must be greater than the [Median Time Past (MTP)](/en/newsletters/2021/04/28/#what-are-the-different-contexts-where-mtp-is-used-in-bitcoin) and no more than two hours in the future according to the node’s local time) and conclude that neither restriction’s conditions are exacerbated by a reorg. [__](/en/podcast/2023/09/28/#would-a-series-of-reorgs-cause-bitcoin-to-break-because-of-the-2-hour-block-time-difference-restriction)

  * ● [Is there a way to download blocks from scratch without downloading block headers first?](https://bitcoin.stackexchange.com/a/119503) Pieter Wuille confirms that it is possible to download blocks without headers but points out the downside is that the node would not know if it is on the best chain until after downloading and processing all of the blocks. He contrasts that approach with [headers-first sync](https://github.com/bitcoin/bitcoin/pull/4468) and outlines the P2P messages exchanged for each approach. [__](/en/podcast/2023/09/28/#is-there-a-way-to-download-blocks-from-scratch-without-downloading-block-headers-first)

  * ● [Where in the bitcoin source code is the 21 million hard cap stated?](https://bitcoin.stackexchange.com/a/119475) Pieter Wuille explains Bitcoin Core’s `GetBlockSubsidy` function that defines the subsidy emission schedule. He also links to a previous Stack Exchange discussion about Bitcoin’s [20999999.9769 BTC limit](https://bitcoin.stackexchange.com/a/38998) and points to the `MAX_MONEY` constant that is used as a sanity check in consensus validation code. [__](/en/podcast/2023/09/28/#where-in-the-bitcoin-source-code-is-the-21-million-hard-cap-stated)

  * ● [Are blocks containing non-standard transactions relayed through the network or not as in the case of non-standard transactions?](https://bitcoin.stackexchange.com/a/119693) User fiatjaf responds that while transactions that are non-standard according to [policy](/en/blog/waiting-for-confirmation/) are not relayed on the P2P network by default, blocks containing non-standard transactions are still relayed, assuming the block adheres to consensus rules. [__](/en/podcast/2023/09/28/#are-blocks-containing-non-standard-transactions-relayed-through-the-network-or-not-as-in-the-case-of-non-standard-transactions)

  * ● [When does Bitcoin Core allow you to “Abandon transaction”?](https://bitcoin.stackexchange.com/a/119771) Murch details the three required conditions to be able to [abandon](https://bitcoincore.org/en/doc/0.20.0/rpc/wallet/abandontransaction/) a transaction in Bitcoin Core: [__](/en/podcast/2023/09/28/#when-does-bitcoin-core-allow-you-to-abandon-transaction)

    * the transaction has not been previously abandoned
    * neither the transaction nor a conflicting transaction are confirmed
    * the transaction is not in the node’s mempool


## Releases and release candidates

_New releases and release candidates for popular Bitcoin infrastructure projects. Please consider upgrading to new releases or helping to test release candidates._

  * ● [LND v0.17.0-beta.rc5](https://github.com/lightningnetwork/lnd/releases/tag/v0.17.0-beta.rc5) is a release candidate for the next major version of this popular LN node implementation. A major new experimental feature planned for this release, which could likely benefit from testing, is support for “simple taproot channels”. [__](/en/podcast/2023/09/28/#lnd-v0-17-0-beta-rc5)


## Notable code and documentation changes

_Notable changes this week in[Bitcoin Core](https://github.com/bitcoin/bitcoin), [Core Lightning](https://github.com/ElementsProject/lightning), [Eclair](https://github.com/ACINQ/eclair), [LDK](https://github.com/lightningdevkit/rust-lightning), [LND](https://github.com/lightningnetwork/lnd/), [libsecp256k1](https://github.com/bitcoin-core/secp256k1), [Hardware Wallet Interface (HWI)](https://github.com/bitcoin-core/HWI), [Rust Bitcoin](https://github.com/rust-bitcoin/rust-bitcoin), [BTCPay Server](https://github.com/btcpayserver/btcpayserver/), [BDK](https://github.com/bitcoindevkit/bdk), [Bitcoin Improvement Proposals (BIPs)](https://github.com/bitcoin/bips/), [Lightning BOLTs](https://github.com/lightning/bolts), and [Bitcoin Inquisition](https://github.com/bitcoin-inquisition/bitcoin)._

  * ● [Bitcoin Core #28492](https://github.com/bitcoin/bitcoin/issues/28492) updates the `descriptorprocesspsbt` RPC to include the complete serialized transaction if the processing of the [PSBT](/en/topics/psbt/) results in a broadcastable transaction. See [last week’s newsletter](/en/newsletters/2023/09/20/#bitcoin-core-28414) for a similar merged PR. [__](/en/podcast/2023/09/28/#bitcoin-core-28492)

  * ● [Bitcoin Core GUI #119](https://github.com/bitcoin-core/gui/issues/119) updates the transaction list in the GUI to no longer provide a special category for “payment to yourself”. Now transactions that have both inputs and outputs that affect the wallet are displayed on separate lines for spending and receiving. This may improve clarity for [coinjoins](/en/topics/coinjoin/) and [payjoins](/en/topics/payjoin/), although Bitcoin Core does not currently support either of those types of transactions by itself. [__](/en/podcast/2023/09/28/#bitcoin-core-gui-119)

  * ● [Bitcoin Core GUI #738](https://github.com/bitcoin-core/gui/issues/738) adds a menu option to allow migrating a legacy wallet based on keys and implied output script types stored in BerkeleyDB (BDB) to a modern wallet that uses [descriptors](/en/topics/output-script-descriptors/) stored in SQLite. [__](/en/podcast/2023/09/28/#bitcoin-core-gui-738)

  * ● [Bitcoin Core #28246](https://github.com/bitcoin/bitcoin/issues/28246) updates how the Bitcoin Core wallet internally determines what output script (scriptPubKey) a transaction should pay. Previously, transactions just paid whatever output script the user specified, but if support for [silent payments](/en/topics/silent-payments/) is added to Bitcoin Core, the output script will need to be derived based on data from the inputs selected for the transaction. This update makes that much simpler. [__](/en/podcast/2023/09/28/#bitcoin-core-28246)

  * ● [Core Lightning #6311](https://github.com/ElementsProject/lightning/issues/6311) removes the `--developer` build option that produced binaries with additional options over the standard CLN binaries. Now experimental and non-default features can be accessed by starting `lightningd` with the `--developer` runtime configuration option. An `--enable-debug` build option will still produce a slightly different binary with some modifications beneficial for testing. [__](/en/podcast/2023/09/28/#core-lightning-6311)

  * ● [Core Lightning #6617](https://github.com/ElementsProject/lightning/issues/6617) updates the `showrunes` RPC to provide a new results field, `last_used`, that displays the last time the _rune_ (authentication token) was used. [__](/en/podcast/2023/09/28/#core-lightning-6617)

  * ● [Core Lightning #6686](https://github.com/ElementsProject/lightning/issues/6686) adds configurable Content-Security-Policy (CSP) and Cross-Origin-Resource-Sharing (CORS) headers for the REST interface to CLN’s API. [__](/en/podcast/2023/09/28/#core-lightning-6686)

  * ● [Eclair #2613](https://github.com/ACINQ/eclair/issues/2613) allows Eclair to manage all of its own private keys and to use Bitcoin Core with only a watch-only wallet (a wallet with public keys but no private keys). This can be especially useful if Eclair is being run in a more secure environment than Bitcoin Core. For details, see the [documentation](https://github.com/ACINQ/eclair/blob/d3ac58863fbb76f4a44a779a52a6893b43566b29/docs/ManagingBitcoinCoreKeys.md) added in this PR. [__](/en/podcast/2023/09/28/#eclair-2613)

  * ● [LND #7994](https://github.com/lightningnetwork/lnd/issues/7994) adds support to the remote signer RPC interface for opening taproot channels, which requires specifying a public key and the [MuSig2](/en/topics/musig/) two-part nonce. [__](/en/podcast/2023/09/28/#lnd-7994)

  * ● [LDK #2547](https://github.com/lightningdevkit/rust-lightning/issues/2547) updates the probabilistic pathfinding code to assume that it’s more likely remote channels have most of their liquidity pushed to one side of a channel. For example, in a 1.00 BTC remote channel between Alice and Bob, the least likely state for the channel is for Alice and Bob to each have 0.50 BTC. It’s more likely that one of them has 0.90 BTC—and even more likely than one of them has 0.99 BTC. [__](/en/podcast/2023/09/28/#ldk-2547)

  * ● [LDK #2534](https://github.com/lightningdevkit/rust-lightning/issues/2534) adds `ChannelManager::send_preflight_probes` method for [probing](/en/topics/payment-probes/) payment paths before attempting to send a payment. A probe is generated by a sender like a regular LN payment but the value of its [HTLC](/en/topics/htlc/) preimage is set to an unusable value (e.g. a value only known to the sender); when it reaches its destination, the receiver doesn’t know the preimage and so rejects it, sending back an error. If that error is received, the prober knows that the payment path had enough liquidity to support the payment when it was sent and so an actual payment sent along the same path for the same amount will likely succeed. If a different error is received, such as an error indicating one of the hops along the path couldn’t forward the payment, a new path can be probed before the actual payment is sent.

Pre-payment (“preflight”) probing can be useful with small amounts of money to find hops that are having issues that might cause delays. If a few hundred sats (or less) get stuck for a few hours, it’s not a big deal for most spenders—but if the full amount of a payment representing a significant portion of a node’s capital gets stuck, it can be very annoying. It can also be possible to probe several paths simultaneously and use the results to choose the best path a few moments later when sending a payment. [__](/en/podcast/2023/09/28/#ldk-2534)


Subscribe to our newsletter

# bitcoinops.org -- Scraped Content

**URL:** https://bitcoinops.org/en/newsletters/2025/09/26
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\OP Return Arguments & Knots.md
**Scraped:** 2026-04-12

---

[ ](/)

[en](/en/newsletters/2025/09/26/) | [ja](/ja/newsletters/2025/09/26/) | [es](/translations/ "No Spanish translation currently available") | [cs](/translations/ "No Czech translation currently available") | [hi](/translations/ "No Hindi translation currently available") | [zh](/zh/newsletters/2025/09/26/) | [de](/de/newsletters/2025/09/26/) | [fr](/fr/newsletters/2025/09/26/) | [pt](/translations/ "No Portuguese translation currently available")

/ [home](/) / [newsletters](/en/newsletters/) / 

# Bitcoin Optech Newsletter #373

Sep 26, 2025 

This week’s newsletter summarizes a vulnerability affecting old versions of Eclair and summarizes research into full node feerate settings. Also included are our regular sections summarizing popular questions and answers on the Bitcoin Stack Exchange, announcing new releases and release candidates, and describing notable changes to popular Bitcoin infrastructure software.

## News

  * ● **Eclair vulnerability:** Matt Morehouse [posted](https://delvingbitcoin.org/t/disclosure-eclair-preimage-extraction-exploit/2010) to Delving Bitcoin to announce the [responsible disclosure](/en/topics/responsible-disclosures/) of a vulnerability affecting older versions of Eclair. All Eclair users are recommended to upgrade to version 0.12 or greater. The vulnerability allowed an attacker to broadcast an old commitment transaction to steal all current funds from a channel. In addition to fixing the vulnerability, Eclair developers added a comprehensive testing suite designed to catch similar problems. [__](/en/podcast/2025/09/30/#eclair-vulnerability)

  * ● **Research into feerate settings:** Daniela Brozzoni [posted](https://delvingbitcoin.org/t/measuring-minrelaytxfee-across-the-bitcoin-network/1989) to Delving Bitcoin the results of a scan of almost 30,000 full nodes that were accepting incoming connections. Each node was queried for its [BIP133](https://github.com/bitcoin/bips/blob/master/bip-0133.mediawiki) fee filter, which indicates the lowest feerate at which it will currently accept relayed unconfirmed transactions. When node mempools aren’t full, this is the node’s [default minimum transaction relay feerate](/en/topics/default-minimum-transaction-relay-feerates/). Her results indicate most nodes used the default of 1 sat/vbyte (s/v), which has long been the default in Bitcoin Core. About 4% of nodes used 0.1 s/v, the default for the upcoming 30.0 version of Bitcoin Core, and about 8% of nodes didn’t respond to the query—indicating that they might be spy nodes.

A small percentage of the nodes used a feefilter value of 9,170,997 (10,000 s/v), which developer 0xB10C [noted](https://delvingbitcoin.org/t/measuring-minrelaytxfee-across-the-bitcoin-network/1989/3) is the value Bitcoin Core sets, through rounding, when the node is more than 100 blocks behind the tip of the chain and is focused on receiving block data rather than transactions that might be confirmed in later blocks. [__](/en/podcast/2025/09/30/#research-into-feerate-settings)


## Selected Q&A from Bitcoin Stack Exchange

_[Bitcoin Stack Exchange](https://bitcoin.stackexchange.com/) is one of the first places Optech contributors look for answers to their questions—or when we have a few spare moments to help curious or confused users. In this monthly feature, we highlight some of the top-voted questions and answers posted since our last update._

  * ● [Implications of OP_RETURN changes in upcoming Bitcoin Core version 30.0?](https://bitcoin.stackexchange.com/a/127895) Pieter Wuille describes his perspectives on the effectiveness and drawbacks of using [mempool and relay policy](/en/blog/waiting-for-confirmation/) to affect the contents of mined blocks. [__](/en/podcast/2025/09/30/#implications-of-op-return-changes-in-upcoming-bitcoin-core-version-30-0)

  * ● [If OP_RETURN relay limits are ineffective, why remove the safeguard instead of keeping it as a default discouragement?](https://bitcoin.stackexchange.com/a/127904) Antoine Poinsot explains the malincentive created by the current OP_RETURN default limit value in Bitcoin Core and the rationale for removing it. [__](/en/podcast/2025/09/30/#if-op-return-relay-limits-are-ineffective-why-remove-the-safeguard-instead-of-keeping-it-as-a-default-discouragement)

  * ● [What are the worst-case stress scenarios from uncapped OP_RETURNs in Bitcoin Core v30?](https://bitcoin.stackexchange.com/a/127914) Vojtěch Strnad and Pieter Wuille respond to a list of extreme scenarios that might occur with the OP_RETURN limit policy default setting changing. [__](/en/podcast/2025/09/30/#what-are-the-worst-case-stress-scenarios-from-uncapped-op-returns-in-bitcoin-core-v30)

  * ● [If OP_RETURN needed more room, why was the 80-byte cap removed instead of being raised to 160?](https://bitcoin.stackexchange.com/a/127915) Ava Chow and Antoine Poinsot outline considerations against a 160-byte default OP_RETURN value including an aversion to continually setting the cap, existing large miners already bypassing the cap, and risks of not anticipating future on-chain activity. [__](/en/podcast/2025/09/30/#if-op-return-needed-more-room-why-was-the-80-byte-cap-removed-instead-of-being-raised-to-160)

  * ● [If arbitrary data is inevitable, does removing OP_RETURN limits shift demand toward more harmful storage methods (like UTXO-inflating addresses)?](https://bitcoin.stackexchange.com/a/127916) Ava Chow points out that dropping the OP_RETURN limit provides incentives to use a less harmful alternative for output data storage in certain situations. [__](/en/podcast/2025/09/30/#if-arbitrary-data-is-inevitable-does-removing-op-return-limits-shift-demand-toward-more-harmful-storage-methods-like-utxo-inflating-addresses)

  * ● [If OP_RETURN uncapping doesn’t increase the UTXO set, how does it still contribute to blockchain bloat and centralization pressure?](https://bitcoin.stackexchange.com/a/127912) Ava Chow explains how increased use of OP_RETURN outputs affects the resource utilization of Bitcoin nodes. [__](/en/podcast/2025/09/30/#if-op-return-uncapping-doesn-t-increase-the-utxo-set-how-does-it-still-contribute-to-blockchain-bloat-and-centralization-pressure)

  * ● [How does uncapping OP_RETURN impact long-term fee-market quality and security budget?](https://bitcoin.stackexchange.com/a/127906) Ava Chow answers a series of questions about hypothetical OP_RETURN usage and its impact on future Bitcoin mining revenues. [__](/en/podcast/2025/09/30/#how-does-uncapping-op-return-impact-long-term-fee-market-quality-and-security-budget)

  * ● [Assurance blockchain will not suffer from illegal content with 100KB OP_RETURN?](https://bitcoin.stackexchange.com/a/127958) User jb55 provides several examples of potential encoding schemes for data concluding “So no, in general you can’t really stop these kinds of things in a censorship resistant, decentralized network.” [__](/en/podcast/2025/09/30/#assurance-blockchain-will-not-suffer-from-illegal-content-with-100kb-op-return)

  * ● [What analysis shows OP_RETURN uncapping won’t harm block propagation or orphan risk?](https://bitcoin.stackexchange.com/a/127905) Ava Chow points out that while there is no dataset specifically isolating large OP_RETURNs, previous analyses of [compact blocks](/en/topics/compact-block-relay/) and stale blocks indicate there is no reason to expect them to behave differently. [__](/en/podcast/2025/09/30/#what-analysis-shows-op-return-uncapping-won-t-harm-block-propagation-or-orphan-risk)

  * ● [Where does Bitcoin Core keep the XOR obfuscation keys for both block data files and level DB indexes?](https://bitcoin.stackexchange.com/a/127927) Vojtěch Strnad notes the chainstate key is stored in LevelDB under the “\000obfuscate_key” key and the block and undo data key is stored in the blocks/xor.dat file. [__](/en/podcast/2025/09/30/#where-does-bitcoin-core-keep-the-xor-obfuscation-keys-for-both-block-data-files-and-level-db-indexes)

  * ● [How robust is 1p1c transaction relay in bitcoin core 28.0?](https://bitcoin.stackexchange.com/a/127873) Glozow clarifies that the non-robustness referred to in the original opportunistic [one parent one child (1P1C) relay](/en/bitcoin-core-28-wallet-integration-guide/#one-parent-one-child-1p1c-relay) pull request means “not guaranteed to work, particularly in the presence of adversaries or when volume is really high so we miss things.” [__](/en/podcast/2025/09/30/#how-robust-is-1p1c-transaction-relay-in-bitcoin-core-28-0)

  * ● [How can I allow getblocktemplate to include sub 1 sat/vbyte transactions?](https://bitcoin.stackexchange.com/a/127881) User inersha discovers the settings required to not only relay sub 1 sat/vbyte transactions but also have them included in a candidate block template. [__](/en/podcast/2025/09/30/#how-can-i-allow-getblocktemplate-to-include-sub-1-sat-vbyte-transactions)


## Releases and release candidates

_New releases and release candidates for popular Bitcoin infrastructure projects. Please consider upgrading to new releases or helping to test release candidates._

  * ● [Bitcoin Core 30.0rc1](https://bitcoincore.org/bin/bitcoin-core-30.0/) is a release candidate for the next major version of this full verification node software. Please see the [version 30 release candidate testing guide](https://github.com/bitcoin-core/bitcoin-devwiki/wiki/30.0-Release-Candidate-Testing-Guide/). [__](/en/podcast/2025/09/30/#bitcoin-core-30-0rc1)


## Notable code and documentation changes

_Notable recent changes in[Bitcoin Core](https://github.com/bitcoin/bitcoin), [Core Lightning](https://github.com/ElementsProject/lightning), [Eclair](https://github.com/ACINQ/eclair), [LDK](https://github.com/lightningdevkit/rust-lightning), [LND](https://github.com/lightningnetwork/lnd/), [libsecp256k1](https://github.com/bitcoin-core/secp256k1), [Hardware Wallet Interface (HWI)](https://github.com/bitcoin-core/HWI), [Rust Bitcoin](https://github.com/rust-bitcoin/rust-bitcoin), [BTCPay Server](https://github.com/btcpayserver/btcpayserver/), [BDK](https://github.com/bitcoindevkit/bdk), [Bitcoin Improvement Proposals (BIPs)](https://github.com/bitcoin/bips/), [Lightning BOLTs](https://github.com/lightning/bolts), [Lightning BLIPs](https://github.com/lightning/blips), [Bitcoin Inquisition](https://github.com/bitcoin-inquisition/bitcoin), and [BINANAs](https://github.com/bitcoin-inquisition/binana)._

  * ● [Bitcoin Core #33333](https://github.com/bitcoin/bitcoin/issues/33333) emits a startup warning message if a node’s `dbcache` setting exceeds a cap derived from the node’s system RAM, to prevent out-of-memory errors or heavy swapping. For systems with less than 2GB of RAM, the `dbcache` warning threshold is 450MB; otherwise, the threshold is 75% of the total RAM. The `dbcache` 16GB limit was removed in September 2024 (see Newsletter [#321](/en/newsletters/2024/09/20/#bitcoin-core-28358)). [__](/en/podcast/2025/09/30/#bitcoin-core-33333)

  * ● [Bitcoin Core #28592](https://github.com/bitcoin/bitcoin/issues/28592) increases the per-peer transaction relay rate from 7 to 14 for inbound peers due to an increased presence of smaller transactions on the network. The rate for outbound peers is 2.5 times higher, increasing to 35 transactions per second. The transaction relay rate limits the number of transactions a node sends to its peers. [__](/en/podcast/2025/09/30/#bitcoin-core-28592)

  * ● [Eclair #3171](https://github.com/ACINQ/eclair/issues/3171) removes `PaymentWeightRatios`, a pathfinding method that assumed uniformity in channel balances, and replaces it with a newly introduced probabilistic approach based on past payment attempt history (see Newsletter [#371](/en/newsletters/2025/09/12/#eclair-2308)). [__](/en/podcast/2025/09/30/#eclair-3171)

  * ● [Eclair #3175](https://github.com/ACINQ/eclair/issues/3175) starts rejecting unpayable [BOLT12](https://github.com/lightning/bolts/blob/master/12-offer-encoding.md) [offers](/en/topics/offers/) where the fields `offer_chains`, `offer_paths`, `invoice_paths`, and `invoice_blindedpay` are present but empty. [__](/en/podcast/2025/09/30/#eclair-3175)

  * ● [LDK #4064](https://github.com/lightningdevkit/rust-lightning/issues/4064) updates its signature verification logic to ensure that if the `n` field (payee’s pubkey) is present, the signature is verified against it. Otherwise, the payee’s pubkey is extracted from the [BOLT11](https://github.com/lightningnetwork/lightning-rfc/blob/master/11-payment-encoding.md) invoice with either a high-S or low-S signature. This PR aligns signature checks with the proposed [BOLTs #1284](https://github.com/lightning/bolts/issues/1284) and with other implementations such as Eclair (See Newsletter [#371](/en/newsletters/2025/09/12/#eclair-3163)). [__](/en/podcast/2025/09/30/#ldk-4064)

  * ● [LDK #4067](https://github.com/lightningdevkit/rust-lightning/issues/4067) adds support for spending [P2A ephemeral anchor](/en/topics/ephemeral-anchors/) outputs from [zero-fee commitment](/en/topics/v3-commitments/) transactions, ensuring that channel peers can claim their funds back on-chain. See Newsletter [#371](/en/newsletters/2025/09/12/#ldk-4053) for LDK’s implementation of zero-fee commitment channels. [__](/en/podcast/2025/09/30/#ldk-4067)

  * ● [LDK #4046](https://github.com/lightningdevkit/rust-lightning/issues/4046) enables an often-offline sender to send [async payments](/en/topics/async-payments/) to an often-offline recipient. The sender sets a flag in the `update_add_htlc` message to indicate that the [HTLC](/en/topics/htlc/) should be held by the LSP until the recipient comes back online and sends a `release_held_htlc` [onion message](/en/topics/onion-messages/) to claim the payment. [__](/en/podcast/2025/09/30/#ldk-4046)

  * ● [LDK #4083](https://github.com/lightningdevkit/rust-lightning/issues/4083) deprecates the `pay_for_offer_from_human_readable_name` endpoint to remove duplicate [BIP353](https://github.com/bitcoin/bips/blob/master/bip-0353.mediawiki) HRN payment APIs. Wallets are encouraged to use the `bitcoin-payment-instructions` crate to parse and resolve payment instructions before calling `pay_for_offer_from_hrn` to pay an [offer](/en/topics/offers/) from a [BIP353](https://github.com/bitcoin/bips/blob/master/bip-0353.mediawiki) HRN (e.g. satoshi@nakamoto.com). [__](/en/podcast/2025/09/30/#ldk-4083)

  * ● [LND #10189](https://github.com/lightningnetwork/lnd/issues/10189) updates its `sweeper` system (see Newsletter [#346](/en/newsletters/2025/03/21/#discussion-of-lnd-s-dynamic-feerate-adjustment-system)) to properly recognize the `ErrMinRelayFeeNotMet` error code and retry failed transactions by [fee bumping](/en/topics/replace-by-fee/) until the broadcast is successful. Previously, the error would be mismatched, and the transaction wouldn’t be retried. This PR also improves weight estimation by accounting for a possible extra change output, which is relevant in [taproot](/en/topics/taproot/) overlay channels used to enhance LND’s [Taproot Assets](/en/topics/client-side-validation/). [__](/en/podcast/2025/09/30/#lnd-10189)

  * ● [BIPs #1963](https://github.com/bitcoin/bips/issues/1963) updates the status of the BIPs that specify [compact block filters](/en/topics/compact-block-filters/), [BIP157](https://github.com/bitcoin/bips/blob/master/bip-0157.mediawiki) and [BIP158](https://github.com/bitcoin/bips/blob/master/bip-0158.mediawiki), from `Draft` to `Final` as they’ve been deployed in Bitcoin Core and other software since

    1. [__](/en/podcast/2025/09/30/#bips-1963)


Subscribe to our newsletter

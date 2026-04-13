# blog.bitmex.com -- Scraped Content

**URL:** https://blog.bitmex.com/bitcoin-cash-abcs-rolling-10-block-checkpoints
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\Golden rules.md
**Scraped:** 2026-04-12

---

[](/)

English

[简体中文](/zh-hans/blog/bitcoin-cash-abcs-rolling-10-block-checkpoints)[繁體中文](/zh-hant/blog/bitcoin-cash-abcs-rolling-10-block-checkpoints)[Русский](/ru/blog/bitcoin-cash-abcs-rolling-10-block-checkpoints)[Español](/es/blog/bitcoin-cash-abcs-rolling-10-block-checkpoints)[Tiếng Việt](/vn/blog/bitcoin-cash-abcs-rolling-10-block-checkpoints)

[Blog](/blog)/[Research](/blog?tab=Research&subcategory=research)/Bitcoin Cash ABC's rolling 10 block checkpoints

# Bitcoin Cash ABC's rolling 10 block checkpoints

21 November 2018

**Abstract:** We evaluate Bitcoin Cash ABC’s new rolling 10 block checkpoint system. The new system does defend against "deep" hostile reorgs; however, it increases the risk of consensus chain splits and provides new opportunities for a would-be attacking miner. Another tradeoff is that the change increases the damage hostile miners can do to the network, but it reduces the potential reward for such behaviour. It is not clear at this point if this change is a net benefit, although it is a fundamental change to the system and it may therefore be better to spend more time assessing the dynamics involved before the network adopts this technology.

**Overview** Bitcoin Cash ABC added a new rolling checkpoint system in software version [ABC 0.18.5](https://github.com/Bitcoin-ABC/bitcoin-abc/releases/tag/v0.18.5), which was released on 21st November 2018. Essentially, the new mechanism finalizes a block once it has received 10 confirmations, which prevents large blockchain reorgs. Therefore even if an alternative chain has more proof of work, if it conflicts with a checkpoint, the node will not switch over to the most work chain.This feature may have been added as a defence against potential attackers including from supporters of the rival Bitcoin Cash SV chain, who have indicated they may wish to attack Bitcoin Cash ABC.

**Security Analysis of the New Checkpointing Mechanism**

The new rolling checkpoint mechanism includes a trade-off:

  * The risk of a deep reorg is**reduced**.

  * The risk of a consensus chainsplit is**increased**.


Network Risk Analysis of the New Checkpoint System

| **Latency issues**| **Attack scenario**  
---|---|---  
**Reorg risk**| **No change** It it unlikely that latency problems will cause nodes to be out of sync with each other by 10 blocks, therefore, this is largely a non-issue, in our view. The new checkpointing system is therefore not likely to cause problems here. Although with a block size of up to 32MB, there could be some latency issues in a small number of circumstances and it is possible nodes could be out of sync by 10 blocks.The checkpoint doesn't seem to solve any issues to do with latency. If latency issues cause a 10 block reorg, the user may want to follow the most work chain. Therefore we do not think there is any benefit here.| **Risk reduced** The risk of a deep hostile reorg is now reduced or limited to 10 blocks.  
**Consensus split**| **New small risk introduced** In the unlikely scenario that poor network connectivity causes nodes to be out of sync with each other by 10 blocks or more, the conflicting checkpoints could cause a consensus split resulting in two or more coins.| **New risk introduced** Although the reorg risk is now reduced, the hostile miner now has a new attack vector. The attacker can attempt to mine a 10 block long (or longer) chain in secret and then publish the chain at a time designed to cause conflicting checkpoints on the network, causing a chain split.  
  
**Attacking Miner: An Alternative Option to a Reorg**

As indicated above, if a hostile miner is producing a shadow chain, once this diverges from the “honest” chain by more than 10 blocks, it is essentially useless as it cannot reorg the honest chain, even if it has more work. Therefore the attacker might as well give up and stop extending the shadow chain.However, this also means that as soon as the 10th block since the split has been produced on the “honest chain,” the attacker might as well publish the shadow chain at this point, depending on the attacker’s objectives. (i.e. release the shadow chain as soon as the attacker receives the block in red indicated in the below diagram.) This could then cause a consensus chain split, with some nodes having received the red block first and some receiving the shadow chain first, resulting in conflicting checkpoints.

**(Source: BitMEX Research)**

This attack may cause a consensus chain split, which could be just as damaging to the network as continuing on to do a hostile reorg. It is also cheaper than continuing on to do a deep reorg, since the hostile miner can stop earlier. Therefore it is not clear to us why this new checkpointing defence is a material improvement. Although the risks in this section are unlikely to materialise (and could require the attacker to have a majority of the hashrate), they seem at least as likely to occur as the problem the new checkpointing system is trying to mitigate against.

**Advantages of the Checkpointing System**

  * Although the new checkpointing mechanism may have a limited impact on security within a 10 block window, when looking back more deeply from the current chain tip, security may be increased over longer timeframes. This may be very useful to some exchanges or merchants who can now wait for more than 10 blocks before crediting a user account and achieve a higher level of assurance. However, a key focus of Bitcoin Cash is to increase transaction speeds, so this benefit may not be desirable for the Bitcoin Cash community.

  * Although a new attack vector is opened up by this mechanism, providing a new way for hostile miners to instigate a consensus split as we explained above, the incentive to do this is less clear than for a “normal” deep reorg attack. A normal reorg attack can be used to initiate a double spend against an exchange, whereby the attacker could profit. While it is possible to also attempt a double spend attack using this new chain split-related attack vector, the outcome is less clear, as it is not obvious which side (if any) will be the winner or which chain an individual exchange may follow. Therefore, although this attack is potentially more devastating on the network, the incentives for it are less obvious. We view this as a significant positive.


**Other issues**

**Centralisation and More Developer Power**

Another common criticism of checkpoints is that it gives developers more power and increases centralisation since developers normally manually insert the checkpoints when they release new versions of the software (like Bitcoin used to have). However in our view, this does not apply in this case as the checkpoints are automatically generated by the node software and not manually generated by the development team. Therefore this a non-issue.

**Long Range Attack and the Initial Sync**

As Eric Wall [explained](https://twitter.com/ercwl/status/1065056459937976320) on Twitter, the new checkpoint mechanism opens up the ability to sybil attack nodes not on the latest chaintip. For example, nodes still in the initial sync or nodes related to users who temporarily shut down their nodes for several days. An attacker needs to launch his own relay nodes and generate a new 10 block long chain at any point in the past.This lower work chain can then be broadcast to nodes (including the specific targeting of nodes not at the current tip), potentially causing these nodes to conduct the checkpoint prematurely, on an alternative chain. Not only does this leave these nodes on a different chain, but this chain is under the control of the attacker. This seems to be a significant flaw of the checkpointing system.Satoshi’s “original vision” appears to imply that the ability of nodes to be switched off and then verify what happened when it was gone is potentially important:

> Nodes can leave and rejoin the network at will, accepting the proof-of-work chain as proof of what happened while they were gone.
> 
> (Source: [Bitcoin Whitepaper)](https://bitcoin.org/bitcoin.pdf)

To some extent this Bitcoin Cash ABC upgrade abandons that philosophy, and requires nodes to be online 24x7.

**Conclusion**

The new Bitcoin Cash ABC checkpointing system is a fundamental change to the core network and consensus dynamics, resulting in a number of trade-offs. These changes may not have been adequately explored before the upgrade. Although we do not think it is likely such a change will result in an immediate crisis, it's not likely to prevent one either.Overall Summary of the Checkpointing System’s ImpactPositives:

  * Reduces the incentive for a miner to attack the chain

  * Provides more assurances for merchants and exchanges for transactions with over 10 confirmations


Negatives:

  * Increases the ability of a miner to instigate a devastating attack on the network

  * Introduces new attack vectors on nodes which are still syncing to the main chain


## SHARE POST

[](https://twitter.com/intent/tweet?text=Bitcoin%20Cash%20ABC's%20rolling%2010%20block%20checkpoints&url=https%3A%2F%2Fwww.bitmex.com%2Fblog%2Fbitcoin-cash-abcs-rolling-10-block-checkpoints)[](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.bitmex.com%2Fblog%2Fbitcoin-cash-abcs-rolling-10-block-checkpoints)[](https://reddit.com/submit?url=https%3A%2F%2Fwww.bitmex.com%2Fblog%2Fbitcoin-cash-abcs-rolling-10-block-checkpoints&title=Bitcoin%20Cash%20ABC's%20rolling%2010%20block%20checkpoints)[](https://t.me/share/url?url=https%3A%2F%2Fwww.bitmex.com%2Fblog%2Fbitcoin-cash-abcs-rolling-10-block-checkpoints&text=Bitcoin%20Cash%20ABC's%20rolling%2010%20block%20checkpoints)

## WRITTEN BY

BitMEX Research

## TAGS

bitcointradingbitmexeducationanalysis

Trade

  * [Derivatives](/app/trade/XBTUSD)
  * [Spot](/app/trade/XBT_USDT)
  * [Buy Crypto ](/app/buyCrypto)
  * [Convert](/app/cryptoConverter)
  * [Mobile ](/mobile)
  * [XBTUSD](/app/trade/XBTUSD)
  * [ETHUSD](/app/trade/ETHUSD)
  * [BNBUSD](/app/trade/BNBUSD)
  * [BMEXUSDT](/app/trade/BMEXUSDT)


About

  * [Why BitMEX ](/why-bitmex)
  * [Security and Custody ](/security-and-custody)
  * [Compliance ](/compliance)
  * [BMEX Token](/BMEX)
  * [Careers](/careers)
  * [Blog](https://blog.bitmex.com/)
  * [Legal](/legal)


Boost

  * [Promotions](/current-promotions)
  * [Partner ](/partners)
  * [Affiliates ](/affiliates)
  * [Bug Bounty ](https://hackerone.com/bitmex)
  * [TradingView](/tradingview)


References

  * [API](/our-api)
  * [Fees](/app/fees)
  * [Futures Guide](/app/futuresGuide)
  * [Perpetuals Guide](/app/perpetualContractsGuide)
  * [Trading on BitMEX](/trading-on-bitmex)


Support

  * [Contact Support](/contact)
  * [FAQ](/faq)
  * [Knowledge Base](https://support.bitmex.com/hc/en-gb)
  * [PGP Communication ](/technical-contact)
  * [Platform Status](https://status.bitmex.com/)
  * [Announcements ](https://blog.bitmex.com/site_announcement/)


FOLLOW US

  * [](https://twitter.com/bitmex)
  * [](https://www.linkedin.com/company/bitmex)
  * [](https://www.twitch.tv/bitmex_official)
  * [](https://discord.com/invite/X2jcEX4Csf )
  * [](https://www.instagram.com/bitmex_dotcom/)
  * [](https://www.reddit.com/r/BitMEX/)
  * [](https://www.youtube.com/channel/UCQ9eXM9P9-f93eeRImPcpUA)
  * [](https://t.me/BitMEX_Announcements)
  * [](https://www.bitmex.com/communities)
  * [](https://www.tradingview.com/broker/BitMEX/)


[](/)

  * [Terms of Service](/terms)
  * [Privacy Policy](/privacy-notice)
  * [Risk Disclosure](/risk-disclosure)
  * [US Person Definition](/us-person-definition)

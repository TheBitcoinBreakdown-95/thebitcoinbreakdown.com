# lists.linuxfoundation.org -- Scraped Content

**URL:** https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2017-April/013985.html
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\Golden rules.md
**Scraped:** 2026-04-12

---

[**public inbox for bitcoindev@googlegroups.com**](../?t=20170405102817)
     [help](../_/text/help/) / [color](../_/text/color/) / [mirror](../_/text/mirror/) / [Atom feed](../new.atom)
    
    From: Johnson Lau <jl2012@xbt•hk>
    To: bitcoin-dev <bitcoin-dev@lists•linuxfoundation.org>
    Subject: [bitcoin-dev] A different approach to define and understand softforks and hardforks
    Date: Wed, 5 Apr 2017 18:28:07 +0800	[thread overview]
    Message-ID: <CB65A263-FFD5-4F9A-B14E-31F44EEC05B9@xbt.hk> ([raw](raw))
    
    [[-- Attachment #1: Type: text/plain, Size: 6290 bytes --]](1-a.txt)
    
    Softforks and hardforks are usually defined in terms of block validity (BIP99): making valid blocks invalid is a softfork, making invalid blocks valid is a hardfork, and SFs are usually considered as less disruptive as it is considered to be “opt-in”. However, as shown below this technical definition could be very misleading. Here I’m trying to redefine the terminology in terms of software upgrade necessity and difficulty.
    
    Softforks are defined as consensus rule changes that non-upgraded software will be able to function exactly as usual, as if the rule changes have never happened
    
    Hardforks are defined as consensus rule changes that non-upgraded software will cease to function or be severely handicapped
    
    SFs and HFs under this definitions is a continuum, which I call it “hardfork-ness”. A pure softfork has no hardfork-ness.
    
    *Mining node
    
    Under this definitions, for miners, any trivial consensus rule changes is somewhat a hardfork, as miners can’t reliably use non-upgraded software to create blocks. However, there is still 3 levels of “hardfork-ness”, for example:
    
    1. Those with lower hardfork-ness would be the SFs that miners do not need to upgrade their software at all. Instead, the minimum requirement is to setup a boarder node with latest rules to make sure they won’t mine on top of an invalid block. Examples include CSV and Segwit
    
    2. Some SFs have higher hardfork-ness, for example BIP65 and BIP66. The minimum actions needed include setting up a boarder node and change the block version. BIP34 has even higher hardfork-ness as more actions are needed to follow the new consensus.
    
    3. Anything else, ranging from simple HFs like BIP102 to complete HFs like spoonnet, or soft-hardfork like forcenet, have the highest hardfork-ness. In these cases, boarder nodes are completely useless. Miners have to upgrade their servers in order to stay with the consensus.
    
    *Non-mining full node
    
    Similarly, in terms of non-mining full node, as the main function is to fully-validate all applicable rules on the network, any consensus change is a hardfork for this particular function. However, a technical SF would have much lower hardfork-ness than a HF, as a border node is everything needed in a SF. Just consider a company has some difficult-to-upgrade software that depends on Bitcoin Core 0.8. Using a 0.13.1+ boarder node will make sure they will always follow the latest rules. In case of a HF, they have no choice but to upgrade the backend system.
    
    So we may use the costs of running a boarder node to further define the hardfork-ness of SFs, and it comes to the additional resources needed:
    
    1. Things like BIP34, 65, 66, and CSV involves trivial resources use so they have lowest hardfork-ness.
    
    2. Segwit is higher because of increased block size.
    
    3. Extension block has very high hardfork-ness as people may not have enough resources to run a boarder node.
    
    * Fully validating wallets
    
    In terms of the wallet function in full node, without considering the issues of validation, the hardfork-ness could be ranked as below:
    
    1. BIP34, 65, 66, CSV, segwit all have no hardfork-ness for wallets. Non-upgraded wallets will work exactly in the same way as before. Users won’t notice any change at all. (In some cases they may not see a new tx until it has 1 confirmation, but this is a mild issue and 0-conf is unsafe anyway)
    
    2. Extension block, as presented in my January post ( <https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2017-January/013490.html> <<https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2017-January/013490.html>> ), has higher hardfork-ness, as users of legacy wallets may find it difficult to receive payments from upgraded wallet. However, once they got paid, the user experience is same as before
    
    3. Another extension block proposal ( <https://github.com/tothemoon-org/extension-blocks> <<https://github.com/tothemoon-org/extension-blocks>> ) has very high hardfork-ness for wallets, as legacy wallets will frequently and suddenly find that incoming and outgoing txs becoming invalid, and need to sign the invalidated txs again, even no one is trying to double spend.
    
    4. Hardfork rule changes have highest hardfork-ness for full node wallets
    
    I’ll explain the issues with extension block in a separate post in details
    
    * Real SPV wallet
    
    The SPV wallets as proposed by Satoshi should have the ability to fully validate the rules when needed, so they could be somehow seen as fully validating wallets. So far, real SPV wallet is just vapourware.
    
    * Fake SPV wallet, aka light wallet
    
    All the so-called SPV wallets we have today are fake SPV according to whitepaper definition. Since they validate nothing, the hardfork-ness profile is very different:
    
    1. BIP34, 65, 66, CSV, segwit has no hardfork-ness for light wallets. Block size HF proposals (BIP10x) and Bitcoin Unlimited also have no hardfork-ness (superficially, but not philosophically). Along the same line, even an inflation hardfork has no hardfork-ness for light wallets.
    
    2. Extension block has the same kind of hardfork-ness issue as I mentioned.
    
    3. HFs that deliberately breaks light wallets, such as spoonnet, is a complete hardfork.
    
    While some people try to leverage weakness of light wallets, the inability to validate any important rules like block size, double spending, and inflation is a serious vulnerability.
    
    ===========
    
    Before I finish, I’d also like to analyse some other interesting cases.
    
    1. Soft-hardfork: which requires miners to mine empty blocks with 0 reward, and put the tx merkle tree in the legacy coinbase (e.g. <https://github.com/luke-jr/bips/blob/bip-mmhf/bip-mmhf.mediawiki> <<https://github.com/luke-jr/bips/blob/bip-mmhf/bip-mmhf.mediawiki>> ). This allows most hardfork-ing changes including block size and inflation. In terms of block validity this is a softfork. But with the definition I presented, soft-hardforks are clearly hardforks for every practical purposes.
    
    2. On-chain KYC, blacklist, account freezing: technically softforks, but all are very disruptive hardforks in terms of user experience.
    
    3. Lightning network and side chains are not consensus rule changes, and they could provide new features without any hardfork-ness.
    
    
    
    [[-- Attachment #2: Type: text/html, Size: 8339 bytes --]](2-a.bin)
    

* * *
    
    [next](../BLUPR15MB0051872C3E1FB74DF3FCA989B10A0@BLUPR15MB0051.namprd15.prod.outlook.com/)             reply	other threads:[[~2017-04-05 10:28 UTC](../?t=20170405102817)|[newest](../)]
    
    **Thread overview:** 3+ messages / expand[[flat](T/#u)|[nested](t/#u)]  [mbox.gz](t.mbox.gz)  [Atom feed](t.atom)  top
    **2017-04-05 10:28Johnson Lau [this message]**
    2017-04-05 10:41 ` [greg misiorek](../BLUPR15MB0051872C3E1FB74DF3FCA989B10A0@BLUPR15MB0051.namprd15.prod.outlook.com/)
    2017-04-07 10:14 ` [Matt Corallo](../A6D5BF88-F5C0-41FC-BD41-CA5493FD5180@mattcorallo.com/)
    

* * *
    
    **Reply instructions:**
    
    You may reply publicly to this message via plain-text email
    using any one of the following methods:
    
    * Save the following mbox file, import it into your mail client,
      and reply-to-all from there: [mbox](raw)
    
      Avoid top-posting and favor interleaved quoting:
      <https://en.wikipedia.org/wiki/Posting_style#Interleaved_style>
    
    * Reply using the **--to** , **--cc** , and **--in-reply-to**
      switches of git-send-email(1):
    
      git send-email \
        --in-reply-to=CB65A263-FFD5-4F9A-B14E-31F44EEC05B9@xbt.hk \
        --to=jl2012@xbt$(echo .)hk \
        --cc=bitcoin-dev@lists$(echo .)linuxfoundation.org \
        /path/to/YOUR_REPLY
    
      <https://kernel.org/pub/software/scm/git/docs/git-send-email.html>
    

Be sure your reply has a **Subject:** header at the top and a blank line before the message body. 

* * *
    
    This is a public inbox, see [mirroring instructions](../_/text/mirror/)
    for how to clone and mirror all data and code used for this inbox

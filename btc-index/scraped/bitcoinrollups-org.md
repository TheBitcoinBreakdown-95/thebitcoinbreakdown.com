# bitcoinrollups.org -- Scraped Content

**URL:** https://bitcoinrollups.org/
**Category:** wayback-waf
**Scrape status:** DONE
**Source notes:** 
**Scraped:** 2026-04-13

---

*Archived version from 2026-03-12 via Wayback Machine*

__Menu __Close

[validity rollups on bitcoin](https://bitcoinrollups.org/)

# Validity Rollups on Bitcoin

By John Light

Contact the author: <https://lightco.in/contact>

Hosted on [GitHub](https://github.com/john-light/validity-rollups/blob/main/validity_rollups_on_bitcoin.md)

##  Table of contents 

  * Acknowledgements
  * Preface
  * Section 0. The history and prehistory of validity rollups
  * Section 1. An introduction to validity rollups
  * Section 2. The validity rollup user experience
  * Section 3. Enabling new functionality
  * Section 4. Scaling improvements
  * Section 5. Building validity rollups on bitcoin
  * Section 6. The costs and risks of validity rollups
  * Conclusion
  * Appendix A. Comparing validity rollups to other protocols
  * Appendix B. Comparing alternative cryptocurrency privacy techniques
  * Appendix C. Increasing throughput with offchain data availability
  * Appendix D. A closer look at validity sidechains
  * Appendix E. Enabling additional throughput increases with validity proofs
  * Appendix F. Mitigating harm from compromised cryptographic proof protocols and toxic waste
  * License
  * References


##  Acknowledgements 

↩

This report is the product of the author’s participation in the Human Rights Foundation’s [ZK-Rollup Research Fellowship](https://hrf.org/zkrollups). Financial support for the ZK-Rollup Research Fellowship was provided by Starkware and CMS Holdings. The author thanks these organizations for their support.

The author also thanks the following individuals for answering questions, providing insights and ideas, and/or giving feedback that contributed to the production of this report: Alex Gladstein, Eric Wall, Olaoluwa Osuntokun, Dario Sneidermanis, Jameson Lopp, Pete Eyre, Jeremy Rubin, Ruben Somsen, Patrick Dugan, Eli Ben-Sasson, Matt Corallo, Francis Corvino, Louis Guthmann, Vitalik Buterin, Trey Del Bonis, Alberto Garoffolo, Sebastián Gustavo Reca. (Name order has been [randomized](https://www.random.org/lists/).)

Please note that inclusion in this acknowledgements section should not be interpreted as an endorsement of the contents of this report. Any claims, conclusions, opinions, errors, _et cetera_ belong to the author alone, unless explicitly stated otherwise.

##  Preface 

↩

Ever since Satoshi Nakamoto first publicly announced bitcoin, its supporters, critics, and skeptics alike have questioned how the protocol would scale as usage increases over time. This question is more important than ever today, as blocks are increasingly full or close to full of transactions. So-called "Layer 2" (L2) protocols such as the Lightning Network have been deployed to take some transaction volume "offchain" but even Lightning needs to use _some_ bitcoin block space. It’s clear that as bitcoin is adopted by more and more of the world’s population (human and machine alike!) more block space will be needed. Another thread of inquiry concerns whether bitcoin’s limited scripting capabilities help or hinder its value as electronic cash. Researchers and inventors have shown that the electronic cash transactions first made possible by bitcoin could be given new form by improving transaction privacy, supporting new types of smart contracts, and even creating entirely new blockchain-based assets.

One of the results of the decade-plus research into scaling and expanding the capabilities of blockchains such as bitcoin is the invention of the validity rollup. Given the observed benefits that validity rollups have for the blockchains that have already implemented them, attention now turns to the question of whether they would be beneficial for bitcoin and existing bitcoin L2 protocols such as Lightning, too. We explore this question by examining validity rollups from several angles, including their history, how they work on a technical level, how they could be built on bitcoin, and what the benefits, costs, and risks of building them on bitcoin might be. We conclude that validity rollups have the potential to improve the scalability, privacy, and programmability of bitcoin without sacrificing bitcoin’s core values or functionality as a peer-to-peer electronic cash system. Given the "trustless" nature of validity rollups as cryptographically-secured extensions of their parent chain, and given bitcoin’s status as the most secure settlement layer, one could even say these protocols are a _perfect match_ for one another.

##  Section 0. The history and prehistory of validity rollups 

↩

###  Section 0.1 Early applications of cryptographic proofs in cryptocurrencies 

> This is a very interesting topic. If a solution was found, a much better, easier, more convenient implementation of Bitcoin would be possible. 
> 
> Originally, a coin can be just a chain of signatures. With a timestamp service, the old ones could be dropped eventually before there’s too much backtrace fan-out, or coins could be kept individually or in denominations. It’s the need to check for the absence of double-spends that requires global knowledge of all transactions. 
> 
> The challenge is, how do you prove that no other spends exist? It seems a node must know about all transactions to be able to verify that. If it only knows the hash of the in/outpoints, it can’t check the signatures to see if an outpoint has been spent before…
> 
> **It ’s hard to think of how to apply zero-knowledge-proofs in this case.**
> 
> We’re trying to prove the absence of something, which seems to require knowing about all and checking that the something isn’t included.
> 
> — Satoshi Nakamoto 1

It has been over a decade since bitcoin creator Satoshi Nakamoto first considered how zero knowledge (zk) proof technology could be used to improve upon the electronic cash protocol he invented. Originally described by Goldwasser, Micali, and Rackoff in their 1985 paper "The Knowledge Complexity Of Interactive Proof Systems", zk proofs are a type of cryptographic proof defined as "those proofs that contain no additional knowledge other than the correctness of the proposition in question".2 Over 35 years after that seminal paper, and a decade after Nakamoto first discussed using zk proofs in bitcoin, cryptographic proof protocols are now a core component of bleeding-edge blockchain scaling and privacy protocols.

The first concrete proposal for using zk proofs in a bitcoin context came from Greg Maxwell, who wrote about "zero knowledge contingent payments" in the Bitcoin Wiki in 2011. Maxwell later worked with Sean Bowe, Pieter Wuille, and Madars Virza to implement the protocol in 2016.34 In May 2013, Miers et al published the Zerocoin paper, showing how zk proofs could be integrated directly into the bitcoin protocol to hide the addresses involved in a bitcoin transaction.5 That same month, Eli Ben-Sasson gave a presentation at the Bitcoin 2013 conference in San Jose, California describing how, in addition to improving privacy, universal (Turing-complete) cryptographic proofs could be used for scaling bitcoin as well.6 These early proposals foreshadowed and inspired later implementations of cryptographic proofs that have been used to improve the privacy and scalability of blockchains for real users in "mainnet" production environments.

The first cryptocurrency to deploy zk proof technology to mainnet was Firo (fka Zcoin, fka Moneta), an implementation of the Zerocoin protocol that launched in September 2016.7 This was followed shortly after by the launch of Zcash, the first cryptocurrency to implement zk-SNARK proofs using the Zerocash protocol, in October 2016.8 The production implementation of zk proofs in Zcoin and Zcash for privacy, and the potential shown in Ben-Sasson et al’s work for improving blockchain scalability with cryptographic proofs, led to increased investment and research into improving the technology. This increased investment in turn resulted in significant improvements in the capabilities and performance of cryptographic proofs.9

###  Section 0.2 The road to validity rollups 

At the same time that general research into the applicability of cryptographic proof technology to cryptocurrencies was happening, a parallel track of research was ongoing specifically to improve the scalability of cryptocurrencies. This track of scaling research would eventually converge with the cryptographic proof research.

The fundamental problem scaling researchers needed to solve was that in order to remain free from the dangers of centralization (censorship, double-spending, corruption, etc) it had to be easy for almost any cryptocurrency user to run a "full node" on the network and contribute to ensuring that the rules of the cryptocurrency consensus protocol are followed by block producers, and, if desired or required, become a block producer themselves.1011 To keep it easy for almost any user to run a full node, the computational effort of verifying the blockchain had to be limited. This put decentralization at odds with scale. As the popularity of cryptocurrencies, especially bitcoin, grew over the years, this tension became increasingly important to resolve. While a wide variety of approaches were proposed and implemented over the years, cryptocurrency developers and researchers mostly focused on four main techniques attempting to resolve the tension between decentralization and scale: onchain optimization, network optimization, sharding, and offchain transaction execution.

Onchain optimization techniques reduce the amount of resources that are required to process and store transactions that must be executed by full nodes. This can be achieved by decreasing the size in bytes or gas that transactions take up inside each block, and/or by decreasing the computational resources required to verify transactions, for example by optimizing the library used for signature verification. Such optimizations have led to significant improvements in transaction verification and initial block download times in Bitcoin Core.12 For a blockchain that supports more expressive smart contract languages, "gas optimization" techniques can likewise lead to significant cost savings and throughput increases.13

Network optimization scaling techniques have two main goals: one is to reduce block propagation latency, and the other is to reduce the bandwidth cost of participating as a full node on the bitcoin network.14 Reducing block propagation latency has the benefit of improving the certainty of confirmations by reducing the number of orphaned blocks, as well as making mining more "fair" by removing the advantage of faster bandwidth speeds. This helps with scalability because if bigger blocks can be relayed faster then they have less of a negative effect on miner centralization. An example of this technique is FIBRE, a protocol developed by Matt Corallo that can bring block propagation time down to a few milliseconds slower than the speed of light.15 Reducing the cost of participating as a full node in the network has the benefit of making it cheaper and easier to run a full node, improving the decentralization of the network. This helps with scalability by making it possible to increase transaction capacity without blowing up bandwidth costs. An example of this technique is BIP-152, also known as "compact block relay", which was also developed by Matt Corallo based on earlier work by Greg Maxwell.16 BIP-152 reduces the amount of data that needs to be sent when propagating blocks through the bitcoin peer-to-peer network, resulting in reduced bandwidth costs for full nodes.

Sharding is a technique where a cryptocurrency’s block processing and storage is split into two or more groups of nodes. Security is shared between shards so that no shard is easier to attack than any other shard. The effect of sharding is that full nodes can be confident that all of the cryptocurrency’s consensus rules are being followed while only needing to store and execute a fraction of all of the transactions occurring on the network. The more shards there are, the more throughput can be supported without increasing the computational burden on any given full node. Vitalik Buterin first proposed sharding as a means of scaling the Ethereum protocol in a blog post published in October 2014.17 The first implementation of a sharded blockchain was Zilliqa, which went live in January 2019.18 Ethereum developers are still planning to implement sharding, although the specifics of how it will work have changed over time.19

Offchain transaction execution protocols are designed to take resource load off the "base layer" full node network. When an onchain cryptocurrency transaction is broadcast to the network, full nodes must "execute" the transaction to ensure that it is valid according to the protocol’s consensus rules. Exactly how a transaction is executed depends on the specifics of the protocol; for example, some protocols require full nodes to execute scripts to determine the validity of transactions, and some protocols only require full nodes to check the validity of a signature.20 If all protocol rules are followed, the transaction can be confirmed, and gets relayed to other peers to verify. If any protocol rules are broken, the transaction is dropped.

Offchain transaction execution protocols move transaction execution to a separate, "higher layer" network. Full nodes on the "base layer" then only have to execute the first (deposit) and last (withdrawal or final settlement) transactions in a series of transactions that were executed offchain on the next layer up. The first offchain execution protocol was a version of bitcoin payment channels, first described by Satoshi Nakamoto in a private email to Mike Hearn in 2011, and later implemented by Mike Hearn and Matt Corallo in bitcoinj in June 2013.2122 Today the most popular offchain transaction execution protocol built for bitcoin is the Lightning Network, a decentralized protocol that routes offchain payments through a network of bidirectional payment channels.23

In 2017, the popularity of token sales and breedable kittens on Ethereum led to block space congestion that caused gas prices to spike and transaction confirmations to be delayed.24 Just when Ethereum was having its first taste of "mainstream" adoption, the limits of its design prevented usage of the blockchain from increasing any further. Scalability became a priority, and application and protocol developers began searching for solutions.25 Short-term solutions that traded off security for throughput, such as sidechains, were quickly implemented.2627 The developer community was not content to settle for sidechains and continued to search for the holy grail: a scaling solution that would enable more usage without either giving up self-custody or harming full node decentralization. While the community expected that Ethereum’s eventual sharding upgrade would significantly improve scalability, there was both an urgency to the problem that demanded a more near-term solution and an understanding that even greater scaling gains could be had by combining sharding with other scaling solutions.28

One proposed solution that was explored in depth was state channels, a generalization of the payment channel protocols that were first implemented on bitcoin.2930 State channels had several limitations that made them unsuitable as a general scaling solution for all of the different kinds of applications that were being built on Ethereum: they were difficult to build for multiparty applications where many users are coming and going at different times, they required expensive capital lockups, and they required users to be online to receive updates and file disputes.

Another proposed solution that got a lot of attention was Plasma. First described in a whitepaper published by Vitalik Buterin and Joseph Poon in August 2017, Plasma was a technique for moving transaction execution offchain while still rooting security in the Ethereum "Layer 1" (L1) blockchain.31 The main improvement over state channels was that, like a sidechain, and unlike state channels, users would not have to lock up lots of liquidity and manage channel balances. However, like state channels, Plasma had a few problems that held it back from being considered the holy grail scaling solution.

Early versions of Plasma had a "mass exit problem" that could lead to L1 congestion and delay withdrawals by weeks in the case of Plasma operator misbehavior.32 The mass exit problem was a consequence of another problem, the data availability problem.33 The problem is that in order to be able to unilaterally exit from an L2 protocol, users need to be able to prove that they currently own the assets they are trying to exit with. However, if any piece of data making up the current state of the L2 protocol is missing, even a single bit of data, for example because a block producer has committed the latest block’s state root but has not published the block itself, then users do not have all of the data they need to produce the necessary cryptographic proof to exit, and their funds become frozen until the data is made available.

Plasma solved the data availability problem by enabling users to exit with their last known balance if nodes detect that data for the most recent state committed to L1 is unavailable. The cost of this solution was the users had to put some of the plasma chain data on L1 to exit, and if many users have to exit at once, this would require lots of data and transactions on L1, creating the mass exit problem. Later versions of Plasma made mass exits less of a problem, but still required users to be online and verify the plasma chain and withdrawals to monitor for misbehavior.34 Perhaps the most important problem Plasma had was that it was difficult to add support for Turing-complete smart contracts like those supported on Ethereum L1.3536 This made Plasma unattractive to developers who wanted the flexibility of the Ethereum Virtual Machine (EVM).

In 2019 Ethereum developers began thinking about how to solve both the data availability problem and the EVM compatibility problem in ways that also solved the other problems that Plasma and state channels had, such as the online/interactivity requirement. This led developers to revisit older proposals that required users to post a minimal amount of data on L1 for each L2 transaction.37 This category of protocols that put minimal data onchain while keeping transaction execution offchain came to be known as a "rollup" (which got its name from the first implementation of a validity rollup by Barry Whitehat).38

Rollups are categorized into two main variants based on the way state transitions were determined to be valid: optimistic rollups, which use fault proofs to enforce correct state transitions, and validity rollups, which use validity proofs to enforce correct state transitions. (Validity rollups are also often called "zk-rollups", but this can be a misnomer since not all validity rollups use zk proofs.)39 Due to their reliance on cryptographic validity proofs, which automatically prevent invalid state transitions and withdrawals, validity rollups are considered "trustless" i.e. no additional trust assumptions on top of the normal L1 trust assumptions. In contrast, if someone attempts to make an invalid withdrawal from an optimistic rollup, then to block the invalid withdrawal, at least one honest party must be online, notice the invalid withdrawal attempt, construct and submit a fault proof transaction, and be able to get the fault proof transaction confirmed within a challenge period defined by the optimistic rollup protocol. Effectively, optimistic rollup users trust the block producers not to steal from optimistic rollup smart contracts, while validity rollup users do not have trust block producers not to steal because they can’t. See "Majority-vulnerable contracts" in Section 6.4.

With solutions to the most important shortcomings of previous scalability proposals in

[... truncated at 20,000 characters ...]

# bitcoinfoundation.org -- Scraped Content

**URL:** https://bitcoinfoundation.org/bitcoin/core-development-update-5
**Category:** wayback-404
**Scrape status:** DONE
**Source notes:** 
**Scraped:** 2026-04-13

---

*Archived version from 2015-09-24 via Wayback Machine*

# [Core Development Update #5](https://bitcoinfoundation.org/bitcoin/core-development-update-5/)

by Bitcoin Foundation

  * Posted on October 24, 2013

  *   * [Leave a comment](https://bitcoinfoundation.org/bitcoin/core-development-update-5/#respond)

  * [Bitcoin](https://bitcoinfoundation.org/category/bitcoin/)


[vc_row full_width=”” parallax=”” parallax_image=””][vc_column width=”1/1″][vc_column_text]

Since my [last update](https://bitcoinfoundation.org/blog/?p=204 "Core Development Update #4") at the end of June, the core development team produced two minor bug-fix releases while working towards a major 0.9 release. We’ve reviewed and closed over 300 pull requests, which range from correcting the spelling of a word in a comment to major new features like the [payment protocol](https://en.bitcoin.it/wiki/BIP_0070). I’ll highlight some changes that are already in the 0.9 source tree, and then write briefly about some changes that we hope will be ready soon.

## Provably Prune-able Outputs

There have been huge debates in the past about embedding data in the blockchain; some people feel that the blockchain should be a public resource available to use for whatever people like, as long as they pay sufficient transaction fees to make it worthwhile for miners to store their transactions. Others feel that the blockchain should only contain the data necessary to validate bitcoin transactions, and any other data should be stored separately.

And while the debates raged, clever people found lots of creative ways of embedding data into the block chain.

So, with some reluctance, I recently merged [pull request #2738](https://github.com/bitcoin/bitcoin/pull/2738) : “Relay OP_RETURN data TxOut as standard transaction type.”

The idea is to give people a way to do what they clearly want to do (associate extra data with a transaction that is secured by the blockchain), but do it in a responsible way that strikes a balance between “you can put whatever you want into the blockchain” and “you will have to be tricky and inefficient to get your data in the blockchain.”

Pull request #2738 lets developers associate up to 80 bytes of arbitrary data with their transactions by adding an extra “immediately prune-able” zero-valued output.

Why 80 bytes? Because we imagine that most uses will be to hash some larger data (perhaps a contract of some sort) and then embed the hash plus maybe a little bit of metadata into the output. But it is not large enough to do something silly like embed images or tweets.

Why allow any bytes at all? Because we can’t stop people from adding one or more ordinary-looking-but-unspendable outputs to their transactions to embed arbitrary data in the blockchain.

What do I mean by “immediately prune-able?” The form of the up-to-80-byte transaction output (“OP_RETURN ”) is such that it can never be used as an input for another transaction– so it can theoretically be forgotten by everybody except for machines that want to keep a full record of every single transaction (“archive nodes”). That is a big improvement over the various hacks people are using today to associate data with their transactions, and will be more important in the future when we implement code that saves disk space by keeping only unspent transaction outputs and not every old block.

The core code has no easy way of creating these new transaction outputs– you have to create them yourself using the raw transactions API. And there are no plans to display the data in Bitcoin-Qt, so you don’t have to worry about somebody sending you a few millibits and attaching a short-but-annoying message to the transaction.

## Autotools

Less controversial (I hope!) but more disruptive to core development: we’ve switched from using hand-coded, platform-specific Makefiles and qmake to automatically generated with autotools Makefiles. Kudos to Cory Fields who did all the hard work to get everything working on Linux, Windows/mingw, and OSX and then was patient and persistent enough to keep it working until everybody was comfortable making the switch. Using the standard “./autogen.sh; ./configure; make” to build Bitcoin-Qt and bitcoind makes it easier for experienced open source developers to contribute to the project.

## The Payment Protocol

I’m going to be lazy and point you to [the fantastic payment protocol FAQ](https://bitcointalk.org/index.php?topic=300809.msg3225143#msg3225143 "Payment Protocol FAQ")written by Mike Hearn and posted to the bitcointalk forums. Writing something like that was on my mental TODO list, and I’m very happy Mike went and did it instead!

# Work in progress

These are all on the “hopefully going to make it into the 0.9 release” list:

## No-wallet mode and bitcoin-cli

bitcoind is increasingly being used as an “edge router” — used as a firewall between the full Bitcoin peer-to-peer network and some custom wallet or mining software, to filter out any invalid blocks or transactions that might tickle bugs in the custom software’s implementation of the Bitcoin protocol.

The 0.9 release should contain Jeff Garzik’s [“-disablewallet” mode](https://github.com/bitcoin/bitcoin/pull/2901), which lets bitcoind run entirely without a wallet, making startup faster and using less run-time memory.

We are (slowly) moving from a monolithic code base that does everything (wallet, RPC, network, blockchain storage/validation) towards more modular internals with fewer dependencies between the different pieces. Another change you should see in the 0.9 release is moving away from the bitcoind executable functioning both as a server and as a RPC client– Wladimir J. van der Laan split the RPC client functionality (“tell the running bitcoin daemon to do THIS”) into a separate executable, ‘bitcoin-cli’. The RPC client code will eventually be removed from bitcoind, but will be kept for backwards compatibility for a release or two.

## Headers-First, parallel download chain sync

Pieter Wuille has been busy working on further optimizing downloading the block chain… which will enable future work that makes downloading the entire chain optional. Once it has been thoroughly tested, we hope to merge “[headers-first sync](https://github.com/bitcoin/bitcoin/pull/2964)” for the 0.9 release.

The idea of headers-first sync is to download the blockchain in two stages:

  1. Download just block headers from your peers. This is very quick, because each block header is just 80 bytes.
  2. Once you’ve got one or more chains of block headers, pick the one with the most proof-of-work and then fetch just the full blocks for that chain.


Getting the headers first makes it possible to implement parallel download of blocks from multiple peers, which increases performance. And it has security and privacy benefits, too–an attacker can’t make you waste space or time storing or serving an ‘orphan’ blockchain fragment that doesn’t connect to the real blockchain.

## Smarter transaction fees

Today, transaction fees are hard-coded into the Bitcoin-Qt/bitcoind wallet software, and the rules surrounding those fees are a collection of heuristics that evolved over the last four years. In short, the current fee-handling code is a complicated mess that will stop working as soon as transaction volume doubles a couple of more times.

In theory, it should be simple: transaction fees should to be set by a give-and-take between the people creating transactions (who want to pay as little as possible) and the people validating and storing the transactions (miners, who would like to be rewarded with higher fees).

And the code that miners are using today to select transactions is simple: they fill their blocks with the highest fee-per-kilobyte transaction (and highest priority transactions, if they choose to set aside some space in their blocks for free transactions).

I’ve [been working on](https://github.com/gavinandresen/bitcoin-git/commits/smartfee) teaching the wallet code to estimate how low a fee (or priority) a transaction needs, at the moment it is sent, to be accepted by miners and included in the next block or three. The estimates are based on watching transactions as they are broadcast on the network and keeping track of which of those transactions are accepted into blocks.

The danger with estimating transaction fees is miners have an incentive to try to game the estimate to make transaction fees higher. For example, if the estimate was based on the average transaction fee for all transactions in the last N blocks, miners could add very-high-fee pay-to-self transactions to the blocks that they mine to drive up the average. However, by only considering fees for transactions that have been broadcast on the network that threat is eliminated– miners could broadcast very-high-fee pay-to-self transactions, but would end up paying those high transaction fees to other miners. The transaction estimation code also uses median transaction fees, not averages, to make it much harder for a minority of transactions to influence transaction fees.

If most of the miners got together and agreed to all broadcast lots of high transaction fee transactions they could succeed in driving up the average transaction fee… but that isn’t going to happen because it would be easy for miners to “free ride” by breaking the agreement and just collecting the higher transaction fees for themselves.

All of the above will work well for fully-validating software like Bitcoin-Qt/bitcoind. More thinking is needed to figure out how lightweight simplified payment verification software (like Multibit) can better estimate transaction fees, because today they can’t calculate how much transaction fee each transaction is paying.

# So: 0.9 will be released…

… when it is ready.

Our bottleneck is still code review and testing, so if you know C++ jump in,[read and comment on some pull requests](https://github.com/bitcoin/bitcoin/pulls), write some unit tests, and help shake out as many bugs as possible before the release.

If you don’t know C++ but are comfortable running bleeding-edge code from the command line, downloading binaries created by the pull-tester, running them on the -testnet, and reporting any bugs (or reporting “works for me on Ubuntalicious 11.11 64-bit” in the pull request) is very helpful.

Other ways you can help: write a [test plan](https://github.com/bitcoin/QA/blob/master/TestPlanCreation.md) for a pull request that you’d like to see pulled. If you’re really motivated to help get something into Bitcoin-Qt/bitcoind, offer some Bitcoin bounties to the first person (or people) to run through a test plan and report success or failure; I’ve had [good success](https://github.com/gavinandresen/QA/blob/master/PaymentRequestTest.md)recruiting people from the #bitcoin IRC channel to do testing of major features by giving out modest (e.g. 0.11 BTC) bounties.

[/vc_column_text][/vc_column][/vc_row]

* * *

### About the Author

  


##### Bitcoin Foundation

__[All posts by Bitcoin Foundation](https://bitcoinfoundation.org/author/ahosanwordpressdev/)

* * *

[Click here to cancel reply.](/bitcoin/core-development-update-5/#respond)

### Leave a Reply [Cancel reply](/bitcoin/core-development-update-5/#respond)

Your email address will not be published. Required fields are marked *

Name *

Email *

Website

Comment

#### Recent Posts

  * [Update to members and community, Please read:](https://bitcoinfoundation.org/uncategorized/devcoredraperuniversity/)
  * [Bitcoin Foundation Board Meeting Minutes 8.25.15](https://bitcoinfoundation.org/uncategorized/bitcoin-foundation-board-meeting-minutes-8-25-15/)
  * [Bitcoin Foundation Board Meeting Minutes 7.21.15](https://bitcoinfoundation.org/uncategorized/bitcoin-foundation-board-meeting-minutes-7-21-15/)
  * [DevCore Website and More](https://bitcoinfoundation.org/uncategorized/devcore-website-and-more/)
  * [Update to the Board – Week Two](https://bitcoinfoundation.org/bitcoin/update-to-the-board-week-two/)


##### Bitcoin Foundation

  * [Download Bitcoin Core](https://bitcoinfoundation.org/download-bitcoin-core/)
  * [Core Development](https://bitcoinfoundation.org/core-development/)
  * [Developer Resources](https://bitcoinfoundation.org/developer-resources/)


  * [Bylaws](https://bitcoinfoundation.org/bylaws/)
  * [Governance & Elections](https://bitcoinfoundation.org/governance-elections/)
  * [IRS 990 Forms](https://bitcoinfoundation.org/irs-990-forms/)


  * [Partners](https://bitcoinfoundation.org/partners/)
  * [Blog](https://bitcoinfoundation.org/blog/)
  * [Contact](https://bitcoinfoundation.org/contact/)


Copyright (c) 2015 Bitcoin Foundation

  *   *

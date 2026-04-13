# bitmex.com -- Scraped Content

**URL:** https://bitmex.com/blog/dapps-or-only-bitcoin-transactions-the-2014-debate
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\OP Return Arguments & Knots.md
**Scraped:** 2026-04-12

---

[](/)

English

[简体中文](/zh-hans/blog/dapps-or-only-bitcoin-transactions-the-2014-debate)[繁體中文](/zh-hant/blog/dapps-or-only-bitcoin-transactions-the-2014-debate)[Русский](/ru/blog/dapps-or-only-bitcoin-transactions-the-2014-debate)[Español](/es/blog/dapps-or-only-bitcoin-transactions-the-2014-debate)[Tiếng Việt](/vn/blog/dapps-or-only-bitcoin-transactions-the-2014-debate)

[Blog](/blog)/[Research](/blog?tab=Research&subcategory=research)/The OP_Return Wars of 2014 - Dapps Vs Bitcoin Transactions

# The OP_Return Wars of 2014 - Dapps Vs Bitcoin Transactions

11 July 2022

**Abstract:** In this piece we explore why Dapps are typically built on Ethereum rather than Bitcoin, which takes us all the way back to March 2014. We examine a debate about whether and how a Dapp protocol called Counterparty should use Bitcoin’s blockchain. This was sometimes called "The OP_Return Wars". We explain the history of OP_Return usage and sidechains in Bitcoin. We conclude by arguing, whether one likes it or not, that it was the culture in the Bitcoin development community in 2014 and the negative view of using Bitcoin transaction data for alternative use cases, which played a major role in pushing developers of these Dapps onto alternative systems like Ethereum, along with other factors.

**Overview**

We have often been asked the question: Why are Dapps such as distributed exchanges typically on Ethereum rather than Bitcoin? After all, it is certainly possible to build Dapps, such as distributed exchanges, naming systems or alternative tokens on top of Bitcoin. There are of course several reasons for this, such as: i. Ethereum's more flexible native scripting language making it easier to build Dapps, ii. Ethereum's faster blocktime, making Dapps more user friendly, or iii. Bitcoin choosing a more conservative blocksize constraint than Ethereum, resulting in potentially higher fees on Bitcoin. All of the above did have an impact, however their impact is often overstated in our view. The most significant factor is culture. Some Bitcoiners and Bitcoin developers simply did not want this type of activity on the Bitcoin blockchain and they successfully discouraged it. This seems to have primarily occurred in around March 2014 and what happened in that period is the subject of this piece. At the same time, promoters of other chains, such as Ethereum may have exploited and [exaggerated](https://twitter.com/notgrubles/status/1187470076833697794) this apparent stance from the Bitcoin developers, to help their new chains gain traction.

**The Counterparty Protocol**

As we mentioned in our September 2020 [report](https://blog.bitmex.com/battle-of-the-dexes/), towards the start of 2014, Counterparty launched. Counterparty is a protocol layer on top of Bitcoin that enables features such as new token creation and the trading of these tokens on a distributed exchange. The system works by using parts of Bitcoin transaction data and using this in the Counterparty protocol, as a function, such as creating a token, sending a token or a market bid on a token on a distributed exchange.

More concisely, at the start Counterparty used the Bitcoin opcode OP_CHECKMULTISIG to include Counterparty related data into the Bitcoin blockchain. This opcode was supposed to be used to verify the signature for a pay to script hash (P2SH) multi signature transaction. An example of a Counterparty transaction from July 2014 can be seen [here](https://www.blockstream.info/tx/52e498fc0ab6430a9e8902299a63b01a3414fca019c9d5bfdce3318d44033977?expand). The transaction sends Bitcoin back to the address it came from and also has three additional outputs, where the output scripts are data related to the Counterparty protocol. In this case it was the creation of a new token called [TICKET](https://www.xchain.io/tx/3720). Using OP_CHECKMULTISIG can be thought of as a hack, because this was not the intended use of the opcode. Counterparty now uses Bitcoin’s OP_Return opcode to store data, which is more inline with what developers intended, to some extent. For example please see [this](https://www.blockstream.info/tx/393ec1dfd7d51ac46faadf022e339bc463db6e59b8705b2aa3d2aa179db23475?expand) more recent Counterparty transaction, which uses OP_Return.

In early 2014 there was considerable experimentation, developer activity, innovation and excitement around Counterparty, which had the lead over a rival platform called Mastercoin.

**What is OP_Return?**

OP_Return is a transaction output in Bitcoin that is provably unspendable. The function can be used to burn Bitcoin or store arbitrary data in the Bitcoin blockchain. Since the data is not part of the UTXO set, storing data this way is said to help scale Bitcoin, as nodes that engage in pruning do not need to store OP_Return data.

In May 2013 somebody took advantage of this feature in the following [transaction](https://www.blockstream.info/tx/d29c9c0e8e4d2a9790922af73f0b8d51f0bd4bb19940d9cf910ead8fbe85bc9b?expand). The OP_Return output in this transaction contains the lyrics to the 1987 song “Never Gonna Give You Up" by Rick Astley, the song related to the Rickrolling meme.

Prior to 2014, transactions containing an OP_Return were non-standard at not relayed by ordinary Bitcoin nodes. However, if a miner included those transactions they were considered as valid. In March 2014, Bitcoin Core 0.9.0 was released with the OP_Return feature included as a standard transaction type, therefore the transactions would be relayed by default. The release notes at the time said the following:

> This change is not an endorsement of storing data in the blockchain. The OP_RETURN change creates a provably-prunable output, to avoid data storage schemes – some of which were already deployed – that were storing arbitrary data such as images as forever-unspendable TX outputs, bloating bitcoin’s UTXO database. Storing arbitrary data in the blockchain is still a bad idea; it is less costly and far more efficient to store non-currency data elsewhere.

Source: <https://bitcoin.org/en/release/v0.9.0#opreturn-and-data-in-the-block-chain>

Bitcoin Core 0.9.0 would only relay transactions with an OP_Return of 40 bytes or less, if the data was larger than this, it was still a valid transaction, but not relayed. The limit was originally intended to be 80 bytes, however after much [discussion](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2014-February/004421.html), the developers [settled](https://github.com/bitcoin/bitcoin/pull/3737) on 40 bytes. To be clear, the OP_Return relay limit in a released version of Bitcoin Core never declined. In February 2015, Bitcoin Core 0.11.0 finally increased the relay limit to [80 bytes](https://github.com/bitcoin/bitcoin/blob/v0.11.0/src/script/standard.h#L28). In January 2016, in Bitcoin Core 0.12.0, the limit was increased again to [83 bytes](https://github.com/bitcoin/bitcoin/blob/v0.12.0/src/script/standard.h#L30), the limit we have today. Although, this 3 byte increase was merely a change in how the counting worked, to include the opcodes themselves, so it is not a "real" increase. This means that if one wants a transaction with an OP_Return output of over 80 bytes today, one has to mine it themselves or send it directly to a miner.

There is no real consensus limit on the size of OP_Return. There is however a ScriptPubKey limit of 10,000 bytes, but it may be possible to get around this.

**The OP_Return Wars**

On 20 March 2014, one of Bitcoin’s main contributors at the time, Jeff Garzik, started posting on the Counterparty thread on the Bitcointalk forum. Jeff was criticising the use of blockchain space by Counterparty.

> To date, I've not seen a blockchain data dumping scheme that could not be securely replaced with a simple hash. You don't need to store data in the blockchain. That is purely intellectual laziness. Timestamping hash(data) is just as secure, while more efficient. Furthermore, a secondary chain can be provably pegged to bitcoin:

Source: <https://bitcointalk.org/index.php?topic=395761.msg5796379#msg5796379>

Jeff went on to say:

> CheckMultiSig is quite clearly intended for ECDSA public keys, not arbitrary data. It should be no surprise that using an operation for something other than its intended purpose has negative, perhaps unintended or unknown consequences. Counterparty transactions are not "according to the bitcoin protocol", they slip through because it never expected that the feature be used in that way.

Source: <https://bitcointalk.org/index.php?topic=395761.msg5827189#msg5827189>

One may think it's odd that Jeff had this view, given that in 2017 he appeared to be “ [large blocker](https://blog.bitmex.com/the-blocksize-war/) ” and that this view about the conservative use of blockspace does not appear to reconcile with the large block view. However, this apparent contradiction did not appear at all in 2014. Jeff’s view at the time was shared to some extent by many of the active developers at the time, including the ones which later became large blockers. As far as we can tell there was no simple mapping at all between one’s view on the blocksize limit and this issue. Jeff was a highly respected developer at the time and this post was a considerable concern for the Counterparty developers and users.

A Counterparty developer, with the pseudonym “BitcoinTangibleTrust” responded to Jeff as follows:

> You're absolutely right. You don't need to store data in the blockchain. Timestamping hash(data) is just as secure, while more efficient. A secondary chain can be provably pegged to bitcoin. However, Counterparty IS storing data in the blockchain using 256 bytes in each one-of-three multi-sig transactions, as per PhantomPhreak's [the Counterparty co-founder and lead developer] note below. Additionally, all these multisig transactions are processed by the miners.

The developer continued by criticising the Bitcoin developers plan to limit OP_Return to just 40 bytes rather than 80:

> If OP_RETURN was meant to stop/curtail the multisig behaviour (Unspent Outputs) and hereby reduce blockchain bloat, then I fear by reducing the size of OP_RETURN from 80 to 40 bytes, you've inadvertently made multisig MORE ATTRACTIVE to all the metaprotocols and you've made OP_RETURN less attractive.

The lead Counterparty developer and co-founder, who went by “PhantomPhreak” chimed in:

> The idea is that we store the data in a second blockchain, and put hashes of that timestamped data in Bitcoin, which hashes would also be less than 40 bytes. The reason we did not do something like that is not a matter of "intellectual laziness", but rather of implementation complexity. Counterparty is not a project in computer science; it is designed to be as simple as possible, for the benefits in development speed. Even if we have to store our data in multi-sig outputs rather than the too-small OP_RETURN outputs. Worse is definitely better in this space.

The next day Jeff responded:

> It is called a free ride. Given that the overwhelming majority -- >90% -- application for the bitcoin blockchain is currency use, using full nodes as dumb data storage terminals is simply abusing an all-volunteer network resource. The network replicates transaction data, so why not come along for a free ride? Rather than engage the existing community, mastercoin and counterparty simply flipped an "on" switch and started using bitcoin P2P nodes as unwanted data stores. An unspent transaction output was never meant to be used as arbitrary data storage. The fact that it can be abused as such does not make it right, or remotely efficient, or the best solution. The UTXO (unspent transaction output) database is the entire network's fast access database. Every single node needs that database to be as small as possible, for best processing of network transactions. Encoding arbitrary data into unspent outputs is network-wide abuse, plain and simple. The entire network bears the cost.

Source: <https://bitcointalk.org/index.php?topic=395761.msg5815887#msg5815887>

Due to Jeff’s high standing within the community, most people in the Counterparty community seemed keen to engage and resolve the issue. For instance BitcoinTangibleTrust responded by saying:

> Thanks for sharing your thoughts Jeff. So, will you help us start engaging with the existing bitcoin core-dev community? It's in Counterparty's interests to act as a responsible partner as we need the bitcoin blockchain if we are to survive. Will you let us know how we can start working together on these questions?

Source: <https://bitcointalk.org/index.php?topic=395761.msg5816031#msg5816031>

Another Counterparty developer brought up another point:

> Is there a way for the bitcoin protocol to prevent the way XCP is using it, without breaking anything else?

If there is no way for Bitcoin developers to block the Counterparty related transactions, perhaps this opposition didn't matter and Counterparty could continue using Bitcoin without permission. Bitcoin developer and at the time mining pool operator Luke-Jr then entered the debate:

> The miners are supposed to filter out abuses.

Source: <https://bitcointalk.org/index.php?topic=395761.msg5816503#msg5816503>

Luke-Jr then suggested these kinds of systems could be built using merge mined sidechain type constructions, which may avoid the blockchain bloat.

> The problem isn't new layers, it's forcing things on people against their will. New layers can be done on an opt-in basis, without polluting the blockchain and forcing non-participants to store the data.

Luke was also asked why the Bitcoin developers reduced the intended OP_Return relay size down to 40 bytes compared to an 80 byte limit, which was originally proposed. Luke responded with the following three points:

  * Too many people were getting the impression that OP_RETURN was a feature, meant to be used. It was never intended as such, only a way to "leave the windows unlocked so we don't need to replace the glass when someone breaks in". That is, to reduce the damage caused by people abusing Bitcoin.

  * 40 bytes is more than sufficient for all legitimate needs for tying data to a transaction: you get 32 bytes for a hash, plus 8 bytes for some kind of unique identifier (which really isn't necessary either!).

  * The original 80 byte proposal was intended to be for 512-bit hashes, but this was determined to be unnecessary.


Luke-Jr continued as follows:

> Hopefully as mining returns to being decentralised, we will see less toleration of abusive/spam transactions whether the OP_RETURN variant or otherwise. Now, if someone has a valid, necessary use case for actually storing hashes with transactions, obviously that's a case miners should seriously consider mining.

Source: <https://bitcointalk.org/index.php?topic=395761.msg5817170#msg5817170>

Luke’s mining pool at the time also started filtering out Counterparty related transactions. At this point fear and uncertainty started to build in the Counterparty community. They needed OP_Return to be 80 bytes, or they would be forced to keep using the OP_CHECKMULTISIG opcode. It did not seem likely that it would go up to 80 bytes given Luke’s comments. In addition to this, some feared the developers could even reduce the limit even further, potentially booting Counterparty off the network. The Bitcoin developers did not seem especially friendly to Counterparty and therefore some may have felt that it was likely to be difficult to continue to use the Bitcoin protocol.

On 25th March 2014, Vitalik Buterin, the main founder of Ethereum chimed in, he argued that the debate should be more around fees and if you pay enough fees then your transaction should be legitimately included. Today, Ethereum’s fee algorithm is highly complex, with different fee buckets and rates for many different blockchain uses, which essentially solves the OP_Return problem. One can argue that SegWit on Bitcoin also mitigates the problem to some extent.

> _It 's the protocol's fault the OPRETURN battle is such an issue. In an ideal world, the concept of 'abuse' would not even exist; fees would be mandatory, and carefully structured to closely match the actual cost that a given transaction imposes on the network," he says. "If you can pay the fees for what you're doing then you should be able to do it, no questions asked."_

_Source:_ [_https://www.coindesk.com/markets/2014/03/25/developers-battle-over-bitcoin-block-chain/_](https://www.coindesk.com/markets/2014/03/25/developers-battle-over-bitcoin-block-chain/)

On 27th March 2014 Counterparty [changed](https://bitcointalk.org/index.php?topic=395761.msg5927090#msg5927090) the way it made transactions to get around Luke-Jr’s mining filter. However, the following day Luke commented that:

> Great news! Filter added to block this crap in less than 5 minutes, and 1 line of code.

Source: <https://bitcointalk.org/index.php?topic=395761.msg5955613#msg5955613>

Luke-Jr also likened Counterparty to a form of abuse:

> It's abuse because you're forcing others to download/store your data against their free choice. Every full node must download the full blockchain (prunable or not!). Every full node has consented to download and store financial transactions. NOT every full node has consented to store anything else. You need 100% consensus for this, not merely some subset (ie, not miners; not developers) or even a majority. Furthermore, everyone is free to store data that isn't in the blockchain. There is nothing to be gained by putting it in the blockchain except that you force it on those who don't want it. Explain how this is anything but abuse…

Source: <https://bitcointalk.org/index.php?topic=395761.msg5826443#msg5826443>

**Anger at Bitcoin developers**

As one might expect, the concern from Bitcoin developers was eventually met with frustration and anger from some Counterparty developers and users. We have include some of their comments below. Firstly from a user called “porqupine” commenting on Luke-Jr’s mining pool blocking Counterparty transactions:

> Great instead of developers responsibly engaged towards finding a solution - you're promoting cat and mouse. You realize you're also saying fuck it to net-neutrality? And trying to take into private hands what kind of transactions people should and shouldn't make on the Blockchain. What's next sanctions of certain individuals you don't like? Sanctions for transactions broadcast from Nodes in countries whose governments foreign policy you don't approve of?

Source: <https://bitcointalk.org/index.php?topic=395761.msg5955738#msg5955738>

On 21 March 2014 porqupine went on to say:

> Wait a minute when was it decided that:_Every node has consented to store X type data and not Y type data._ Maybe I also did not consent to store transactions for Laundered money, illicit drugs and weapons, human slavery - etc. You're basically negating protocol neutrality and deciding what the Protocol _Should_ and _Should_ Not be used to store, and _More_ than that you aren't speaking in first person but using the pronoun _Us_ given the impression that you are speaking for all miners or protocol users as a whole.

Source: <https://bitcointalk.org/index.php?topic=395761.msg5826584#msg5826584>

Others expressed concern about why Jeff and Luke had a right to block certain use cases over anyone else.

> I can't believe this attitude. I didn't know bitcoin had owners. I thought I and about a million others were owners :-)

PhantomPhreak, a Counterparty co-founder said:

> First of all, Counterparty transactions are financial transactions. Second, every full node has consented to download and store theBitcoin blockchain, no less. That is, transactions that accord to the Bitcoin protocol, which Counterparty transactions obviously do. Satoshi imbedded a political message in the Genesis Block, for Christ's sake... You have a much narrower view of the possible use cases for Bitcoin than do others.

Source: 

[... truncated at 20,000 characters ...]

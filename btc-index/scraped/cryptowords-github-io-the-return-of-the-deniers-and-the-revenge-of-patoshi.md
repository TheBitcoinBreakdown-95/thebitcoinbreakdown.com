# cryptowords.github.io -- Scraped Content

**URL:** https://cryptowords.github.io/the-return-of-the-deniers-and-the-revenge-of-patoshi
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\Patoshi Pattern.md
**Scraped:** 2026-04-12

---

### WORDS

Do Your Own Research. Read Words.

Follow

  * [__Subscribe](https://mailchi.mp/59e9fda5b387/words)
  * [__Twitter](https://twitter.com/_bitcoinwords)
  * [__Support](https://bitcoinwords.github.io/support/)
  * [ __Email](mailto:bitcoinwords@gmail.com)


# The Return of the Deniers and the Revenge of Patoshi 

__20 minute read

**Crypto Words has moved!** The project has migrated to a new domain. All future development will be at [**WORDS**](https://bitcoinwords.github.io/). | [**Go to WORDS**](https://bitcoinwords.github.io/)  
---|---  
  
# [The Return of the Deniers and the Revenge of Patoshi](https://bitslog.com/2019/04/16/the-return-of-the-deniers-and-the-revenge-of-patoshi/)

### By [Sergio Demian Lerner](https://twitter.com/SDLerner)

### Posted April 16, 2019

**Synopsis** : _In this article I will discuss what we know about the early Bitcoin blocks. Also I will present a new strong argument that a single miner mined 22k blocks. Finally I’ll introduce[satoshiblocks.info](http://satoshiblocks.info/), new website that shows a cool visualization of early blocks._

* * *

The last time I wrote about Satoshi I thought it would be the last. But here I am, again. Let me bring some context. It all began in a discussion in 2013, in [bitcointalk](https://bitcointalk.org/index.php?topic=175996.0) forum, where a plausible reasoning led me to believe that Satoshi would have mined one million bitcoins during 2009-2010. As you know, [plausive reasoning](https://en.wikipedia.org/wiki/Plausible_reasoning) doesn’t let you prove anything mathematically, however it gives incredibly good results when applied correctly to solving real real-world problems, where information is imperfect or missing. The original argument about Satoshi coins can be simply stated like this: _**Supposition** : Anyone who took the time and effort to create Bitcoin would not risk letting the network to halt due to lack of miners. He would run at least a miner himself._ During 2009 the mining activity was so low that it was kept active on the minimum accepted difficulty, and blocks were created at a lower rate than one every 10 minutes. It’s plausible that even if Satoshi wanted to turn off his miner after a while, he may have finally decided to let it run until seeing more activity.

## The Patoshi Pattern

In [March 2013](https://bitslog.com/2013/04/17/the-well-deserved-fortune-of-satoshi-nakamoto/) I was able to turn the plausible reasoning into a probabilistically falsifiable argument, which means it it’s highly improbable to be false. By reading the original Satoshi client v0.1 source code, I discovered three privacy-related flaws that, together, enable anyone to correlate the blocks mined during the first years and uncover a common origin. Also, it allows anyone to compute the approximate mining hash rate of each of the early miners. If one of these flaws had been absent, it would not have been possible to recognize a very special miner track and the tracks of the remaining miners. But first, a little technical background. The ExtraNonce field, located in the coinbase transaction, increments every time the nonce fields overflows, meaning the search space is exhausted. As the nonce field is 32 bits in length, and the Bitcoin initial difficulty was tuned to require scanning 32 bits on average, the nonce would sometimes, but not always, overflow. Now let’s present the three flaws present in the original Bitcoin code:

  1. The ExtraNonce works as a “free running counter”, without resetting to zero between blocks mined.
  2. The rate a certain miner increments the ExtraNonce is much faster than its actual hashrate would indicate, based on the original Bitcoin source code. We’ll call this miner **Patoshi**.
  3. Every few seconds during mining, the best block is checked. If the best block changes, the ExtraNonce is additionally incremented. Normally every external block received will increment the ExtraNonce, except for the exceptional miner Patoshi, which doesn’t seem to follow this rule.


Together these flaws enable the visualization of the **Patoshi Pattern**. Blocks in the Patoshi pattern will be elements of the Patoshi set (or P set).

The Patoshi Pattern (blue) and the Remaining Miners Patterns (green)

The first flaw is that the ExtraNonce field was handled in a non-privacy preserving way. By not being reset each time a new block is mined, it works as a free-run counter or timestamp.

The second is that for a reason that was only uncovered a year later, the rate this timestamp is incremented by Patoshi was higher than the number of blocks solved would suggest, so even if his mining equipment was not so much faster, it looked so. This flaw alone let you very easily separate Patoshi from the rest of the miners. We lack information about how Patoshi mining software operated: for instance, it’s seems that the Patoshi miner didn’t followed the rule in flaw 3, but it can be the case that it checked the change in the best block less frequently and this invalidates any attempt to measure if flaw 3 was present or not in his software.

The third flaw enables anyone to follow the tracks of the remaining miners. If this flaw had not been present, most blocks of the remaining miners would be indistinguishable from “noise”, having ExtraNonce values that are too close to zero, because the ExtraNonce would hardly ever increment. The nonce values of the remaining miners almost never overflow. In fact, because of this, in the blocks of the remaining miners the ExtraNonce counter behaves more like a global block counter, and therefore the ExtraNonce patterns of different miners appear with similar slope. If two blocks A and B are mined by the same miner, then the ExtraNonce delta between them would almost equal to the number of blocks mined between A and B. The moment in which the miner starts mining from a zero ExtraNonce value establishes a unique point the in the line created by every non-Patoshi miner.

_When Patoshi stops mining, the remaining miners increment the ExtraNonce at a lower rate due to privacy flaw 3._

An exceptional case is when several blocks are mined in a very short time: or if the mining process is paused and resumed after a few minutes, then the ExtraNonce will be incremented only once for many blocks in a row. However, this doesn’t seem to happen often. Last, it seems that the Patoshi miner doesn’t follow this rule: there are many cases where the distance between his blocks is lower than the number of blocks in-between. While the absence of this flaw is yet another way of distinguishing Patoshi blocks from the rest, we’ll focus on other more interesting distinguishers.

Together, the 3 privacy flaws enable the ExtraNonce in early blocks “links to” the last block mined by the same miner, for all miners. This link is based on a coarse timestamping, it’s imperfect, but it can be shown, by simple statistical analysis, that is highly precise for linking blocks. There is a perfect match between the observed behavior of non-Patoshi blocks and the Satoshi client v0.1 source code. Many people hold this historical [source code](http://satoshiblocks.info/0.1.zip). It’s published in [several](https://github.com/blaesus/bitcoin-0.0.1) places in the Internet. If you doubt the authenticity of such source code, you can convince yourself easily that there are some rules governing the ExtraNonce pattern: the probability that the pattern was created by chance is astonishingly low.

_Bitcoin Client 0.1 Mining Loop_

As soon as you look as the ExtraNonce/Time patterns you realize that the Patoshi chain of linked blocks is outstanding: about 22k blocks in total, high slope, dense chain. Both the naked eye and slope-tracking algorithms pinpoints this pattern immediately. The slopes break at some points, where extranonces restart from zero. The slope (the apparent mining rate) of blocks in this pattern is very different from any other chain of blocks and is quite stable except for three fast changes in two years. While there is a small probability that some blocks are incorrectly tagged by the algorithm, most of the blocks can be tagged without dispute. I estimate the tagging error is 0.1%.

The probability that the Patoshi pattern is formed by multiple miners with the same hardware (slope), each starting exactly when the previous one stopped is also astonishingly low (assuming miners can start mining at any random time). Also take into consideration that the pattern slope does not represent its underlying hashrate. Therefore, the Patoshi pattern is “one thing”, not the concatenations of many separate things.

_Patoshi Pauses Mining for 10 days, his longest pause._

## There is Only One Patoshi

Some people accepted the existence of the Patoshi pattern, but at the same time refused the argument that a single entity mined the whole P set. Let’s review their arguments:

* * *

**Main argument against single Patoshi:** _The pattern is not created by a single miner but by many miners somehow synchronized._

* * *

There are four strong reasons to reject this argument:

  1. 99.9% of all Patoshi blocks are unspent. While only 10% of all non-Patoshi blocks are unspent. This means that the “synchronized” miners decided to spend only 0.1% of their bitcoins, while the remaining miners decided to spent 90% of them (or alternatively each spent 90% of their bitcoins, or each block has a 0.9 probability of being spent). Assuming no correlation between blocks, the probability that only 0.1% of Patoshi blocks being spent is close to 2^-76000. But we can assume high correlation: a miner either sells all his coins or no coin at all. The number of other miners went from 0 to about 25 by March 2010. But the number of synchronized miners in Patoshi pattern would have stayed almost intact, because the hashrate of the Patoshi pattern mostly decreases over time. If we assume the synchronized miners were 6, then the chance they didn’t sell their coins by chance is one in a million.
  2. Each Patoshi block “links” to a block in the P set, but not to any of the remaining blocks. Somehow the information if a previous block was part or P or not needs to have been communicated along the block. How was this communicated? Early blocks are all look similar. There is no pool signature, as there is today. For what reason would miners do this selective linking? What would they gain? Occam Razor would reject the existence of such system.
  3. There are some time intervals where the Patoshi pattern interrupts abruptly (i.e. 07-18-2009 for a full day) and then continues from the point it has interrupted. How did all these separate miners coordinate the interruption, while other continued mining without problems? It may be the case that they were running the same version of the client, which failed. But there is no evidence of a special version of the software being distributed.


* * *

**Second argument against single Patoshi:** _There was a kind of heterogeneous mining pool formed since Genesis, and many independent users joined the pool._

* * *

Strong rejections to this argument:

  1. Mining pools were invented several years later
  2. How was the existence of this mining pool secretly communicated before the Genesis block was even created? The Patoshi pattern starts right at Genesis.
  3. Mining pools were created to reduce reward variance due to the low individual probability of solving a block, but during 2009 single miners could easily solve blocks frequently. Why to pool resources? There is no reason.
  4. There weren’t enough miners to incentivize pooling, as the Patoshi hashrate corresponds to one to six miners (depending on the assumed efficiency of the involved PCs).
  5. It would have required specific software (that was never made public) to manage the pool and more software to use it.
  6. All these being done in secrecy would imply some kind of conspiration, which seems ridiculous.


There is no technical reason, no software developed, no operational expertise at that time, no monetary gain, and no benefit at all for the creation of a mining pool when Bitcoin was launched. Therefore, we can assume there was no mining pool at Genesis time.

Based on the assumption that the pattern comes from a single entity you can directly conclude that this party was using a special mining software and/or hardware: fast as one or more state-of-the-art servers in 2009, and with slightly different rules governing how to mine.

## Nonce Restriction in all Patoshi Blocks

Even if most people were convinced the Patoshi pattern was real, some people still weren’t. But [by the end of 2013](https://bitslog.com/2013/09/03/new-mystery-about-satoshi/) things got more interesting: I found proof, beyond any doubt, that the pattern was real, using a completely different method. I discovered that all Patoshi blocks were marked by a reduction of the range of nonces used in published blocks, to a specific range R. We can define R by restricting the least significant byte of the nonce field. This byte normally increments from 0 to 255, but in the Patoshi blocks is reduced to the range [0..9] U [19.. 58].

_An Histogram of the LSB Byte of the Nonce Value in the Block Header_

The fact that Patoshi nonces are in this range does not imply the miner of the Patoshi pattern only scanned nonces within this range. It could be the case that the network rejected the solved blocks having nonces out of this range, or the same Patoshi mining software did. This is not the case, as there is a direct relationship between the number of nonces scanned and the average time Patoshi took to solve a block. And the relation suggests the nonce space was reduced to R to create blocks at the rate Patoshi blocks were created. The nonces space scanned is about 1/5th of the full range, and the ExtraNonce increments about 5 times faster.

If you collect the set of blocks whose nonce is in range R, you’ll find it contains 27.68k blocks. I call this set M. The blocks that are in M have the nonce in the R range. The set M is far bigger than one would expect from normal mining. The chances M contains 27.68k blocks assuming uniform nonces is negligible (less than 2^-36000). From the 50k blocks analyzed you would expect that only 10K blocks belong to M, not 28k. But we’ll see this perfectly matches the anomaly of the Patoshi set.

If Q blocks had been marked by restricting the nonce range when scanning, and the remaining elements of M had nonces in R just by chance, then we could compute Q from the following equation (isolating Q): Q + (50-Q)/5 ~= 27.6. The solution is Q=~22k, exactly the size of the Patoshi set. It also indicates there are no other blocks were scanned within the restricted range R except those from Patoshi.

If you re-analyze the common arguments against single-miner for the Patoshi pattern considering this new discovery, the original arguments can’t resist any probabilistic justification. Chances get far lower of what people consider just impossible.

Regarding why the nonce was restricted to the range R, I didn’t know, and I still don’t. These are some of the possible arguments I came up with:

  1. **The restricted range was part of a “trapdoor” to mine blocks with higher probability of obtaining a hash digest below the target.** There is a plausible strong reason this to be false: mining faster by restricting the nonce range implies partially breaking SHA256 pre-image resistance. No scientific paper has ever mentioned such a devastating attack, neither for SHA256 nor for standardized hashing functions using the same Merkle–Damgård construction. Any party with the capability to find SHA256 partial pre-images would probably be able to break most commercial communications, from TLS to VPNs, and earn billions. But there is another reason which is mathematical: if you re-mine all Patoshi blocks, trying to find other solutions to the same block templates, will find that the amount of solutions in the R range compared to the amount of solutions out of that range matches the relation of relative range sizes. [It was no “better” to mine within that range](https://bitslog.com/2014/04/03/chain-archeology/). The Patoshi set was simply marked to identify something. What? We don’t know.
  2. **The restricted range is user to indicate ownership.** If Patoshi were two people, maybe they agreed to give 80% of the block rewards to one of them, and 20% to the other. Then the final owner was marked by specific LSB of the nonce, before scanning the rest of the nonce. This can be proven false, as it would imply Patoshi miners had to increase the extra nonce 256 times more often, which doesn’t happen during the first years. Maybe the restricted range is used to indicate probabilistic ownership: the range R is split into sub-ranges, and it’s fully scanned. The party who gets the bitcoins is the one whose sub-range is randomly picked in the solved block.
  3. **Sub-ranges of R were used to identify different mining hardware cores, where each core would scan a reduced nonce space**. This means that Patoshi created the first private homogeneous mining pool. By homogeneous I mean that either all mining machines were setup by a single entity, or a small group of people agreed to use the same type of hardware to fairly distribute earnings. This hypothesis has not been falsified.


At this point I’ve said just a little more from my previous research articles. And from 2014 to early 2019 I didn’t have anything else to say (or to research) about early blocks. Several following studies repeated my research and arrived at similar conclusions. OrganOfConti’s [famous blog post](http://organofcorti.blogspot.com/2014/08/167-satoshis-hashrate.html) contains even more data about Satoshi, describing how he reduced his hashrate [in four steps](http://organofcorti.blogspot.com/2014/08/168-little-more-on-satoshis-blocks_15.html). The last known study, by BitMex Research, comes to the conclusion that Satoshi probably mined [700k coins during 2009-2010](https://blog.bitmex.com/satoshis-1-million-bitcoin/). Sadly, they miss the LSB argument entirely (which is the strongest of all known).

But there are people, like nullc, that every now and then [go public](https://www.reddit.com/r/Bitcoin/comments/b0bj3w/how_do_people_know_satoshis_account_has_1000000/) challenging all this research with old arguments. In a nutshell, I would say that nullc argues a Null Hypothesis: nothing is real. Which is silly because the research was validated by many independent academics.

* * *

**Null hypothesis:** _(in a statistical test) the hypothesis that there is no significant difference between specified populations, any observed difference being due to sampling or experimental error._

* * *

The reasons why nullc argues this continuously escape my imagination. It’s completely unscientific. The data is there in the blockchain. It doesn’t need rocket science to collect and analyze it. All you need is to grab a Bitcoin blockchain parser. When some weeks ago I read [the comments](https://www.reddit.com/r/Bitcoin/comments/b0bj3w/how_do_people_know_satoshis_account_has_1000000/eie9597/) on reddit I felt compelled to refute him again, because … well, because I can. So here I am. Nullc argues that the Patoshi pattern is just the result of some kind of sampling trick. A human interpretation, like shapes in the clouds. He states:

> ” _The million coins being discussed are all unspent coins from the first year, there is fairly strong evidence that they were not mined by a single party (because their nonce incrementing was consistent with multiple parties). If you refer to the lines on the left side of the graph on the page the involved coins there are more like 200k._ ”. Nullc, 2019. Of course, he doesn’t give any “strong argument” and the “nonce incrementing” is perfectly consistent with multiple parties plus a single party mining most of the blocks. The argument is just silly.

I hav

[... truncated at 20,000 characters ...]

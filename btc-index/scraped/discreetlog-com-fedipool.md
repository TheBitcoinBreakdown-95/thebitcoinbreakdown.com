# discreetlog.com -- Scraped Content

**URL:** https://discreetlog.com/fedipool
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\Fedi Mints.md
**Scraped:** 2026-04-12

---

[ ](https://www.discreetlog.com)

Sign in Subscribe

By [ODELL](/author/odell/) — Feb 6, 2023

# Fedipool: Fedimint Could Mitigate Bitcoin Mining Pool Concerns

Current Fedimint development is focused on easy to use consumer wallets that could replace usage of major custodial wallet providers such as Binance and Wallet of Satoshi, but what if the same tech was used to replace major custodial mining pools such as Foundry and AntPool.

_I was fortunate to spend some time with a contributor to the open source project[Fedimint](https://fedimint.org/?ref=discreetlog.com), below is an overview of a concept we discussed._

**The problem:**

  * The overwhelming majority of bitcoin mining relies on mining pools.
  * Individual miners prefer to use pools because they reduce overhead and enable them to be paid much more often than if they mined without one.
  * Mining pool operators benefit from network effects. The more hash rate that is pointed at their pools, the more frequent and predictable the payments to miners, resulting in more miners joining.
  * Mining pool operators custody bitcoin for their users and choose which transactions are included in the blocks they mine.
  * Pool operators can censor transactions, seize funds, and track users. Governments may compel them to act against their users through regulatory pressure.
  * Currently independent miners have two main ways to mitigate these risks: withdraw bitcoin to their own wallets frequently and switch to a competing pool if their current operator acts maliciously.
  * While these techniques reduce risk, pool operators remain vulnerable regulatory targets, and we should expect governments and other malicious entities to target them more going forward.


**Fedimint as a potential solution:**

  * Fedimint is an emerging open source protocol that combines bitcoin, lightning, chaumian ecash, and federated custodians (called Guardians) to create community wallets that are easy to use, have strong privacy, reduced custodial risk, cheap and fast payments within the community, and interoperability with all bitcoin wallets.
  * Current Fedimint development is focused on easy to use consumer wallets that could replace usage of major custodial wallet providers such as Binance and Wallet of Satoshi, but what if the same tech was used to replace major custodial mining pools such as Foundry and AntPool.


**How a Fedipool might look:**

A group of independent miners choose to create a Fedimint together. Their combined hash rate results in reduced payout variance: they are paid more frequently and predictably than if they mined alone. Rather than a single pool operator constructing blocks and choosing which transactions to include, each Guardian can construct their own blocks, reducing censorship risk. Additional miners can join the pool in the future to take advantage of the above, but rather than be a Guardian, they choose which Guardian they want to construct their blocks.

**Due to the properties of Fedimint:**

  * Rewards cannot be seized as long as at least two of the Guardians act honestly.
  * Miners receive the privacy benefit of chaumian ecash.
  * Miners can withdraw mining rewards using bitcoin or lightning at their leisure.
  * Regulatory risk is significantly reduced since Guardians can be easily located in different jurisdictions throughout the world.


There is currently growing and active development of the Fedimint open source project and these benefits can be achieved without any changes to the Bitcoin protocol. This is incredibly important since the Bitcoin protocol is extremely difficult to change by design.

* * *

_**If you found this post helpful support my work with[bitcoin](https://geyser.fund/project/citadel?ref=discreetlog.com).**_

[ Previous Bitcoin is Not a Ponzi Scheme ](/bitcoin-is-not-a-ponzi/) [ Next Bitcoin Transaction Fees and UTXO Management ](/utxos/)

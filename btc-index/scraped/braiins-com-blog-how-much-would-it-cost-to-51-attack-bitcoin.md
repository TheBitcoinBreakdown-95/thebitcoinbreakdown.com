# braiins.com -- Scraped Content

**URL:** https://braiins.com/blog/how-much-would-it-cost-to-51-attack-bitcoin
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\51% Attack.md
**Scraped:** 2026-04-12

---

By clicking **“Accept”** , you agree to the storing of cookies on your device to enhance site navigation, analyze site usage, and assist in our marketing efforts. View our [Privacy Policy](/legal/privacy-policy) for more information.

DenyAccept

[](/)

Resources

[Marketplace](/marketplace)[Store](https://store.braiins.com)

Company

USD/TH/Day

1.53%

USD

1.53%

En

[Contact Sales](/contact-sales)

No items found.

# How Much Would it Cost to 51% Attack Bitcoin?

Fundamentals

Published

11.1.2021

A thorough explanation of 51% attacks, the possible ways to attempt them, and how feasible each method is today. Bonus: how we can mitigate the risk with Stratum V2.

Table of Contents

Text Link

When it comes to mining centralization, the big concern that people have is a “51% attack” — where a single actor or group controls a majority of Bitcoin’s mining power and can effectively decide which transactions (if any) get confirmed in the blockchain. 

Besides just disrupting or censoring the confirmation of new transactions, a 51% attack can also be used for a _double spend_. This means that the attacker mines a different version of the blockchain in secret so that they can spend some coins on the public chain and then later mute the transaction by publishing their version of the blockchain in which they retain ownership of the coins. Another name for this is a blockchain reorganization because it replaces the most recent blocks in the chain. 

So far, there have been no successful 51% attacks on Bitcoin in its history, but we have seen successful attacks on other coins like [Ethereum Classic](https://blog.coinbase.com/ethereum-classic-etc-is-currently-being-51-attacked-33be13ce32de). **If successful, such an attack would likely cause significant harm to Bitcoin’s reputation.**

## Measuring 1-Hour Cost of a 51% Attack

 _Source: Crypto51.app_

There’s a cool website called [Crypto51](https://www.crypto51.app/) which measures the cost to 51% attack Bitcoin and other major proof of work cryptocurrencies. If you go to the About page, it describes how the _1h Attack Cost_ is calculated using the current market price (aka _spot price_) for hashrate from NiceHash (NH), a hashrate exchange that allows people to buy hashpower from miners and control what it’s used for. For non-miners, the significance of this may not be clear, so let’s explain it.

Supposing that a certain blockchain has a total network hashrate of 100 TH/s, then the cost of a 1-hour 51% attack is the cost of controlling more than 50 TH/s of the hashrate. **If a majority of the hashrate is available on a hashrate exchange, then the 1-hour attack cost is simply the cost of purchasing that hashrate from the market for 1 hour.**

On Crypto51, the portion of a given cryptocurrency’s hashrate that’s available for purchase is represented by the _NiceHash-able_ metric on the right side of the image above. A NH-able value below 100% means that less than 51% of the coin’s hashrate can be bought.

**For Bitcoin, the NH-able value is under 1%** , and other hashrate exchanges do not add much to the value. In other words, the 1h Attack Cost is calculated based on the _spot_ _price_ for SHA-256 hashrate, but the volume of SHA-256 hashrate available on the market is not nearly large enough to make it a viable way to actually attack Bitcoin.

Since the value on Crypto51 isn’t realistic for Bitcoin, let’s dive into more detail about the **different methods that could be used to 51% attack Bitcoin, how feasible they are, and what can be done to mitigate them.** By the end, you’ll better understand the security provided by Bitcoin’s proof of work system.

## Bitcoin Cloud Mining and Hashrate Exchanges

For most people, it will never be profitable to mine Bitcoin. This is because competitive electricity prices are typically only found in locations with energy production (e.g. hydroelectric dams, natural gas wells, etc.), not on an urban energy grid.

However, for people who want to speculate on [mining profitability](https://insights.braiins.com/profitability-calculator), cloud mining offers a way to do so. Cloud mining contracts enable people to “mine” cryptocurrencies without owning the physical hardware themselves. In other words, buyers purchase a specific amount of hashrate for a specific time period and price, then earn the mining rewards produced by that hashrate. Meanwhile, the miners still operate the mining equipment, but they get paid via the cloud mining contracts or hashrate market rather than the mining rewards.

Hypothetical example of cloud mining contracts

In order to make a clear distinction, from now on we will refer to hashrate sold on an exchange or via cloud mining contracts as **_synthetic hashrate_** , and hashrate used to mine directly as **_physical hashrate_**. 

So, what does this have to do with Bitcoin’s security?

**Well, if a malicious actor wanted to attack a cryptocurrency network, it would be far simpler to purchase synthetic hashrate than to produce physical hashrate.** However, there’s not nearly enough hashpower on hashrate exchanges to consider them as an attack vector against Bitcoin.

That being the case, let’s talk about the other possible attack methods.

## The Cost of a 51% Attack with Physical Hashrate

With hashrate exchanges not being viable for accessing 51% of network hashrate, there are only two realistic attack vectors left: 

  * Amassing enough ASICs (mining hardware) and power capacity to attack the network with physical hashrate
  * Controlling mining pools who have a combined majority of the synthetic hashrate


Let’s start by analyzing the first case. **_How much would it cost to 51% attack Bitcoin with physical hashrate?_**

With the current total network hashrate of 150 EH/s, we’ll calculate a rough estimate of the costs necessary to set up 150 EH/s worth of ASICs (assuming the miners with the existing 150 EH/s remain honest and don’t contribute to the attack). In the most favorable case where all hashrate is produced by an equivalent machine to the highest efficiency ASIC on the market today, the Antminer S19 Pro, then the specifications per ASIC would be _110 TH/s_ and _3250 W_ consumption.

150,000,000 TH/s / 110 TH/s = approximately **1.364M ASICs needed to amass 150 EH/s.**

With a per-unit consumption of 3250 W, that would put the**electricity capacity needed to power all those ASICs at ~4.4 GW of power**. That limits the possible candidates to pull off such a huge endeavor to powerful nation states who would work in coordination with large energy producers. 

And how much would those 1.364M ASICs cost the taxpayers of such a nation state? Well, at a conservative unit price of $4000 each including power supply units, the **cost of hardware would exceed $5.46 billion**. Factoring in all the R&D costs to catch up to existing hardware manufacturers (who are already [sold out](https://www.coindesk.com/secondary-markets-asic-bitcoin-mining-manufacturing-delays) until May 2021), plus all the other data center equipment needed, the true cost would likely be far higher.

In the grand scheme, this may still be a small sum to the likes of the USA or China. However, it doesn’t account for significant obstacles such as the limited capacity of chip manufacturers like Samsung and TSMC to actually produce these high quality hashing chips. (Not to mention the lunacy of a government using that semiconductor manufacturing capacity to build ASICs and attack Bitcoin rather than any number of other [valuable applications](https://www2.deloitte.com/content/dam/Deloitte/cn/Documents/technology-media-telecommunications/deloitte-cn-tmt-semiconductors-the-next-wave-en-190422.pdf).) 

> In TSMC's 2018 annual report, the company produced 10,436 products for 481 customers. They have limited manufacturing space at their facilities and have to account for massive customers outside of the bitcoin mining space, including Sony, Qualcom, Broadcom, and, famously, Apple.
> 
> — Amanda Fabiano (@_amanda_fab) [December 13, 2020](https://twitter.com/_amanda_fab/status/1338190445717770240?ref_src=twsrc%5Etfw)

‍**Ultimately, attempting to destroy trust in Bitcoin through a mining attack with physical hashrate just doesn’t make sense anymore, and it hasn’t for years.** Nation states who view Bitcoin as a threat are far more likely to over-regulate or (try to) ban its use than to spend billions of taxpayer dollars on mining hardware and power.

Still, that doesn’t mean that 51% attacks are completely impossible. Let’s now turn our attention back to synthetic hashrate. This time, instead of talking about hashrate exchanges and cloud mining, we’ll discuss mining pools.

## Synthetic Hashrate and China Mining Centralization 

Bitcoin mining pool centralization has been a near-constant source of FUD (fear, uncertainty, and doubt) for years. However, it's usually misrepresented. **Mining pool operators have long-term stakes in the Bitcoin network and just as little incentive to attempt an attack as miners themselves.**

You can read an explanation of why hashrate concentration is not a huge cause for concern in this [Coindesk article](https://www.coindesk.com/no-concentration-among-miners-isnt-going-to-break-bitcoin). 

A more interesting case to think about is if the Chinese Communist Party (CCP) were to try taking over several mining pool operations. Currently, ~97% of Bitcoin’s total network hashrate goes through Chinese pools.

Bitcoin hashrate distribution chart; source: coin.dance

It’s extremely unlikely that the CCP will attempt any attack. Nonetheless, we’ll consider the possibility for a simple reason: attacking with physical hashrate would cost at least $5 billion, whereas attacking with synthetic hashrate by taking over several pools would be essentially FREE. 

However, there’s a problem with this attack too: **miners can switch pools in a matter of seconds.** If the CCP were to attempt taking over the 4+ largest pools, they would have to hope that no miners switch to other pools so that they can sustain the attack for more than a few pointless minutes.

The less concentrated hashrate is in a few mining pools, the more difficult it would be to attempt a pool attack. However, mining pools are necessary for most miners today to stabilize their revenue, and concentration in a few pools is unavoidable.

**Therefore, one good way to increase the difficulty of a mining pool attack is to make it impossible to do covertly.** In other words, the attack causes more damage the longer it is sustained, so it can be mitigated by ensuring that some miners would detect it within minutes and switch pools. 

## Blockchain Reorganizations

Every block in the blockchain references the block before it with a value in the block header called the _prevhash_. With Stratum V2, miners will be able to construct blocks themselves with data from their own nodes (a process called _Job Negotiation_), so if they are honest they’ll always reference the prevhash of the most recent block in the chain. 

By taking block construction out of the pools’ hands, Stratum V2 can help miners ensure that they won’t contribute to secretly mining a “shadow” chain that gets broadcasted later in a blockchain reorganization attack. Similarly, they can ensure that their hashrate is not used to mine a different SHA-256 chain, such as Bitcoin Cash or Bitcoin SV.

The chain with the largest block height is considered valid, so mining a longer chain in secret and then broadcasting it later can overwrite all the blocks that were mined publicly in the meantime.

‍**If a pool rejects valid block templates proposed by their miners, those miners could automatically switch to another pool.** That is the potential benefit of [Stratum V2 Job Negotiation](https://braiins.com/blog/stratum-v2-bitcoin-decentralization) from a decentralization standpoint. 

## The Cost to 51% Attack Bitcoin Depends on the Type of Attack

To summarize everything above, there are essentially two ways to attempt a 51% attack:

  * **Physical hashrate** : purchase or manufacture ASICs and run them, costing ~$5.5 billion as a conservative estimate at the time of writing. Alternatively, simultaneously take control of enough individual mining farms to pull off the attack, an extremely difficult coordination problem likely involving 100+ operations.
  * **Synthetic hashrate** : simultaneously take over 3-5 mining pool operations and mine empty blocks or do a deep reorg attack in an attempt to break user trust in Bitcoin. Still difficult to coordinate, but essentially free if the attacker doesn’t have a long-term stake in Bitcoin.


Since the synthetic hashrate attack vector is practically free while the physical hashrate attack vector is far more complex and costly, it makes sense to focus on increasing the difficulty of attacking with synthetic hashrate. Stratum V2 can do just that.  


on social media

[](https://x.com/Braiins)[](https://t.me/braiins)[](https://www.linkedin.com/company/braiins/)[](https://www.youtube.com/channel/UClUiH7v_yj0SNpda99s9_tQ)[](https://www.instagram.com/braiins_mining/)

### Categories

[Fundamentals](/category/fundamentals)

[Mining Use Cases](/category/mining-use-cases)

[Mining Software](/category/mining-software)

[Mining Hardware](/category/mining-hardware)

[Braiins News](/category/braiins-news)

[Economics](/category/economics)

[The Grid](/category/the-grid)

[Pleb mining](/category/pleb-mining)

### Be the first to know! 

  * Checkbox

**Mining News** (Industry news, trends, and analysis)

  * Checkbox

**Product Updates** (New features, releases, and announcements)


Read [Privacy Policy](/legal/privacy-policy).

You’re subscribed. See you in your inbox.

Oops! Something went wrong while submitting the form.

Buy bitcoin  
hashrate

[Try now](https://hashpower.braiins.com)

Share article

## More from

## Fundamentals

[Bitcoin Mining Handbook: Essential Resource for Miners](/blog/bitcoin-mining-handbook-your-essential-resource-for-optimizing-mining-operations)

[Bitcoin Mining Glossary: Key Terms and Concepts for Every Miner](/blog/bitcoin-mining-glossary-essential-terms-and-concepts-for-every-miner)

[So You Think Bitcoin Mining is Wasteful?](/blog/bitcoin-mining-vs-gaming)

[How to Mine Bitcoin [Beginner’s Guide]](/blog/how-to-mine-bitcoin-beginners-guide)

## Most Recent Articles

[](/blog/hashrate-heated-house-bitcoin)

Mining Use Cases

### [Hashrate Heated House: The Complete Guide to Heating Your Home with Bitcoin Mining](/blog/hashrate-heated-house-bitcoin)

19.3.2026

[](/blog/firmware-optimization-gda-40mw-case-study)

Mining Use Cases

### [40% Higher Hashrate on Identical Hardware: Firmware Optimization at 40MW Scale with GDA](/blog/firmware-optimization-gda-40mw-case-study)

3.3.2026

[](/blog/mastering-uptime-in-modern-bitcoin-mining-with-braiins-manager)

Mining Software

### [Beyond 100%: Mastering Uptime in Modern Bitcoin Mining](/blog/mastering-uptime-in-modern-bitcoin-mining-with-braiins-manager)

16.2.2026

# Subscribe to the Braiins newsletter

Stay ahead with our weekly and monthly summaries on bitcoin, mining, and energy, plus exclusive Braiins product updates.

Read by 10,000+ bitcoiners around the world.  


  * Checkbox

**Mining News** (Industry news, trends, and analysis)

  * Checkbox

**Product Updates** (New features, releases, and announcements)


Read [Privacy Policy](/legal/privacy-policy).

You’re subscribed. See you in your inbox.

Oops! Something went wrong while submitting the form.

We apologize but our blog is available only in [English](https://braiins.com/blog), [Spanish](https://es.braiins.com/blog) and [Russian](https://ru.braiins.com/blog).

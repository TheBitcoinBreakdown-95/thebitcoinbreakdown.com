# alpenlabs.io -- Scraped Content

**URL:** https://alpenlabs.io/blog/proof-of-work
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\ZK Rollups.md
**Scraped:** 2026-04-12

---

[](/)

[Docs](https://docs.alpenlabs.io/)[Careers](https://jobs.ashbyhq.com/alpenlabs)[Get in touch](https://tally.so/r/mRj50P)[Start building](https://docs.alpenlabs.io/welcome/get-started)

#### Research

# Proof of Work

Published on 

June 6, 2024

We started Alpen Labs in June 2022. Our founders have personal backgrounds in Nepal, a country where 25% of the GDP comes from remittances. This background primed us to see early on the powerful potential for bitcoin to disintermediate middle-men and lower the cost of global payments.

When we first started Alpen Labs, we knew we wanted to build something on bitcoin that would democratize global access to payments and finance. We started by exploring the Lightning Network, an exciting and relatively new protocol built on bitcoin that enabled fast and low-cost payments. After a deeper dive, we realized that Lightning itself would face numerous challenges and tradeoffs as usage grew, particularly around privacy, centralization, and UX. We explored alternative ways to safely expand the utility of bitcoin that could help Lightning and other L2 protocols scale. Later in 2022, we concluded that zk-SNARKS will be a core part of scaling bitcoin globally. 

The [rapid evolution](https://www.alpenlabs.io/blog/current-state-of-snarks) of this cryptographic primitive finally made it a practical tool to expand the accessibility and utility of bitcoin. Further, it was consistent with bitcoin's design philosophy that blockchains should primarily _verify_ computation, not _execute_ complex computation. We found that zk-SNARKs were the best tools to build secure bridges, off-chain protocols, and services that improve the privacy, scalability, and programmability of bitcoin. Later, we discovered that more people in the bitcoin community had arrived at similar conclusions, even as early as 2013 with Greg Maxwell’s ideas on [CoinWitness](https://bitcointalk.org/index.php?topic=277389.0) when zk-SNARKs were much less practical.

In early 2022, Trey Del Bonis, who now works as a protocol engineer at Alpen Labs, [published a relatively detailed sketch](https://tr3y.io/articles/crypto/bitcoin-zk-rollups.html) of how a zk rollup built on bitcoin would work. Trey's design used the Liquid script extension suite along with a hypothetical "OP_ZKPVERIFY" opcode to enable building a Layer 2 validity rollup on bitcoin. Toward the end of his article, Trey mentioned that "rollups could work super well for Lightning", which got our attention. We peer-reviewed Trey’s design and began exploring ways to simplify the design further with Taproot and new innovations around scaling in other blockchains.

Near the end of 2022, bitcoin rollups received a big boost in attention thanks to the publication of [Validity Rollups on Bitcoin](https://bitcoinrollups.org/), a research report by John Light, who now works on product at Alpen Labs. This research report was commissioned earlier in the year by the Human Rights Foundation, StarkWare, and CMS Holdings as part of the ZK Rollup Research Fellowship. The goal of the fellowship was to answer key questions about the viability of zk rollups on bitcoin, including investigating and analyzing the features and use cases of zk rollups, how they could be built on bitcoin, and if they could be built on bitcoin, what risk/reward tradeoffs were associated with them. Our team went deep into the report, and found that we shared many of the report's conclusions.

We had started working on our own rollup design in Fall of 2022. We took liberties to imagine what the ideal zk rollup on bitcoin would look like, and worked backward from there to figure out what additional new building blocks would be needed to make it possible. This work culminated in [ZK Rollup on Bitcoin](https://github.com/alpenlabs/Technical-Whitepaper/blob/main/whitepaper_v085.pdf), a whitepaper detailing the design we came up with. Simanta Gautam, one of our co-founders, presented a summary of this design in a [talk](https://www.youtube.com/watch?v=Nldg_tjeX_A) at BTC++ in April 2023. We are excited to release the full whitepaper today to the public as free and open source research.

> The “ZK Rollup on Bitcoin” whitepaper represents a snapshot of our views at a formative time in the history of Alpen Labs. Today, our work on the zk rollup design described in the whitepaper, which requires a bitcoin soft fork, is on pause in favor of a rollup design that is possible to build on bitcoin today, based on our recently published [SNARKnado](https://www.alpenlabs.io/blog/snarknado-practical-round-efficient-snark-verifier-on-bitcoin) research. But the long-term vision of trustless zk rollups on bitcoin is still very much of interest to us, and we look forward to contributing where we can to help make this vision a reality.

‍** _Read the "ZK Rollup on Bitcoin" whitepaper _**[**_here_**](https://github.com/alpenlabs/Technical-Whitepaper/blob/main/whitepaper_v085.pdf)** _._**

## Read Next

#### [ResearchShrinking Glock: Duty-Free BitsMarch 9, 2026](/blog/duty-free-bits-bitcoin)

#### [ResearchSize Matters: The Architecture of BTC Credit MarketsMarch 2, 2026](/blog/btc-credit-markets)

#### [NewsletterInside Alpen's 2025January 5, 2026](/blog/inside-alpens-2025)

[](/)

##### Navigation

[Blog](/blog)

[Docs](http://docs.alpenlabs.io/)

[Careers](https://jobs.ashbyhq.com/alpenlabs)

##### Info

[Audits](https://docs.alpenlabs.io/community/security)

[Terms of Service](https://alpenlabs.notion.site/terms-of-service)

[Privacy Policy](https://alpenlabs.notion.site/privacy-policy)

[Media Kit](https://alpenlabs.notion.site/media-kit)

##### Community

[X](https://x.com/AlpenLabs)

[Discord](https://discord.gg/alpen)

[Telegram](https://t.me/AlpenOfficial)

© 2025 Alpen Labs. All rights reserved.

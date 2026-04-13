# stablesats.com -- Scraped Content

**URL:** https://stablesats.com
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\Stablesats.md
**Scraped:** 2026-04-12

---

Stablesats [ GitHub ](https://github.com/GaloyMoney/dealer) [ Chat ](https://chat.galoy.io/) [ Visit galoy.io ](https://galoy.io/) Stablesats Transact USD over Lightning without stablecoins or fiat integration Why Stablesats User Experience How it works Brief history of synthetic USD Comparing the alternatives Further reading FAQ Why Stablesats One problem that persists for people in a Bitcoin economy is the short-term volatility of the bitcoin exchange rate. When the bitcoin price drops, it can lessen the purchasing power of sats and make it harder to pay for dollar-priced goods and services. This creates friction and uncertainty, causing merchants and consumers to frequently consider selling bitcoin for dollars to ensure they can meet their financial obligations.   
  
This problem led Galoy to create a feature called Stablesats, a USD account that people can use to hold “dollar equivalent” balances in their Lightning wallet, thus protect themselves from fluctuations in the bitcoin exchange rate.  User experience - sending USD over Lightning See how users send and receive to the USD Account and convert sats to (synthetic) USD.  Users of [Blink Wallet](https://blink.sv) now have a BTC account and a USD account. Both accounts can be used to send and receive bitcoin, and users can instantly transfer value between these accounts. Value held in the USD account will not fluctuate with the price of Bitcoin.  How it works The current Stablesats implementation uses the bitcoin derivatives market, specifically an instrument called perpetual inverse swap to create synthetic USD.  
  
The video below outlines the basic mechanics of this strategy.  
  
More details, definitions and alternative strategies are shared in the [dealer repo on GitHub.](https://github.com/GaloyMoney/dealer)   
In the future, adding more exchanges, hedging strategies and currencies can drive resiliency and optionality for Bitcoin banks and their users. Ultimately, we can unlock the ability for every Lightning user to choose their own units of account without ever leaving the network.  
  
There are also other interesting avenues to explore such as matching the duration of the liabilities just like insurance companies do (short-term with short-term instrument strategies, long-term with long-term).  Brief history of synthetic USD Methods for creating synthetic USD have been discussed and implemented for many years:   
  

      * In 2015, Arthur Hayes outlined [how to create, store, and spend synthetic USD.](https://blog.bitmex.com/in-depth-creating-synthetic-usd/)
      * In 2021, the [Standard Sats](https://standardsats.github.io/) project introduced the idea of “eurobitcoins” during a hackathon. 
      * In early 2022 Kollider published a [Twitter thread ](https://twitter.com/kollider_trade/status/1496507594214723590) recapping ideas and projects under the “synthetic stablecoins on Lightning.” 
  
The time for synthetic fiat currencies has arrived. Bitcoin banks using Stablesats can deliver a meaningful solution to millions of Lightning Network users seeking volatility protection.  Comparing the alternatives Stablesats offers a third option for Bitcoin banks wishing to solve the volatility problem for their users. The chart below compares some of the tradeoffs between the two typical options – stablecoins and fiat banking integration - and points to a future fourth option based on Discreet Log Contracts (DLCs).  | Where is the Trust | Banking access required | Fees  
---|---|---|---  
Dollar | Bank | Yes, for the user | High  
Stablecoins | Issuer | Yes, for the issuer | Low  
Derivatives (Stablesats) | Exchange | None | Lowest  
DLCFD | Oracle | None | TBD  
Further reading
      * View the [dealer repo](https://github.com/GaloyMoney/dealer) and the [stablesats-rs repo](https://github.com/GaloyMoney/stablesats-rs) on GitHub 
      * Watch [Nicolas Burtey’s presentation](https://youtu.be/OhSSEFwSPDM) from the BOLT.FUN Legends of Lightning tournament 
      * Hear Nicolas on [Stephan Livera Pod 346](https://stephanlivera.com/episode/346/)
      * Watch [Arvin’s API workshop](https://www.youtube.com/watch?v=bp5Dc6Wvnbw) at BOLT.FUN 
      * Hear Kemal's [interview on Bitcoin Dad Pod](https://podcasts.apple.com/us/podcast/interview-kemal-from-galoy/id1611611893?i=1000571338730)
Stablesats FAQ Can I try Stablesats now? Yes, v1 of the dealer is open source and available at at [github.com/GaloyMoney/dealer](https://github.com/GaloyMoney/dealer). So you could clone the repo, and create your own synthetic USD.   
  
Currently the dealer has some coupling with the Galoy stack, so experimenting with the dealer installation requires our whole stack.   
  
We’re working on rewriting our dealer in Rust, such that it could be run independently, even potentially with non-custodial wallet and single account.   
  
If you are a user of Blink Wallet, you can reach out to support to get access to the feature.  Is Stablesats currently compatible with the traditional banking system? No, today Stablesats only relies on the bitcoin payment network to work.  How does this compare with projects like Synonym, Taro or RGB that are enabling tokens on Bitcoin?  The Stablesats project is focused on creating stable value in USD. There is no token involved other than sats, and only Bitcoin payment rails are being used.  Are there regulatory requirements for Stablesats? Since Stablestats uses derivatives products, it may require regulatory approval in some countries.  Are there risks? Every fiat product has some risk. For instance if you hold fiat in a bank account and the bank goes under, you are at risk of losing funds. Similarly, when you stabilize sats, some of the magical powers wear off.   
  
Risks to consider for Stablesats include the following: 
      * Counterparty risk with the exchange. If the exchange goes under, the collateral may be unrecoverable. 
      * Derivatives exchanges have auto-deleveraging for perpetual contracts. The position could be closed despite being in profit. This will lead to an under-hedging situation. 
      * Funding goes negative for an extended period of time. Historically there has been on average more longs than shorts on derivatives exchanges. In this environment, funding is revenue-generating for short positions. This might not stay true in the future. 
      * To learn more from Galoy view the [GitHub repo](https://github.com/GaloyMoney/dealer), or read other relevant resources: [Luna Bros, Inc.](https://blog.bitmex.com/luna-brothers-inc/) (Bitcoin-Backed Stablecoins section) and thoughts from [Kollider](https://twitter.com/kollider_trade/status/1496507594214723590). 
How is Stablesats different from the algorithmic stablecoin projects, some of which have recently blown up?  Algorithmic stablecoins are typically not fully collateralized, which makes them vulnerable to a run on the bank.   
  
The derivatives contracts placed to create Stablesats are fully collateralized with BTC – for every dollar liability, there is an equivalent dollar worth of value in bitcoin.  Why should I be excited about Stablesats when there are stablecoins like Tether and USDC on many different blockchains?  With Stablesats, users don't have to worry about which blockchain or stablecoins their counterparty uses. Stablesats offers a way to hold and transact dollars that is fully interoperable with anyone using bitcoin and Lightning.  Is it possible to use “physical” USD from a bank account to send and receive payments over Lightning?  Not with stablesats, but we are working on this functionality independently. If this is of interest, reach out to us so we can better understand your requirements.  Want to ask a question? Join us in the Stablesats channel at [chat.galoy.io](https://chat.galoy.io) Stablesats © 2022 Galoy, Inc. [ GitHub ](https://github.com/GaloyMoney/dealer) [ Chat ](https://chat.galoy.io/) [ Visit galoy.io ](https://galoy.io/)

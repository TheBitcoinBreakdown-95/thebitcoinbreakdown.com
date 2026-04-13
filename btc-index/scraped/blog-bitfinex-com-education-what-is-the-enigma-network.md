# blog.bitfinex.com -- Scraped Content

**URL:** https://blog.bitfinex.com/education/what-is-the-enigma-network
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\Enigma network.md
**Scraped:** 2026-04-12

---

Skip to content

[ ](https://blog.bitfinex.com/)

Scan to download  
the Bitfinex app 

[ More Info ](https://www.bitfinex.com/mobile)

[ Log in ](https://www.bitfinex.com/login/) [ Sign up ](https://www.bitfinex.com/sign-up/)

English

[ 繁體中文 ](https://blog.bitfinex.com/?lang=zh-hant) [ Tiếng Việt ](https://blog.bitfinex.com/?lang=vi) [ Português ](https://blog.bitfinex.com/?lang=pt-pt) [ Español ](https://blog.bitfinex.com/?lang=es)

[ Log in ](https://www.bitfinex.com/login/) [ Sign up ](https://www.bitfinex.com/sign-up/)

繁體中文  Tiếng Việt  Português  Español  English 

[ ](https://blog.bitfinex.com/) [ All ](https://blog.bitfinex.com/) [ Bitfinex Alpha ](https://blog.bitfinex.com/category/bitfinex-alpha/) [ Products ](https://blog.bitfinex.com/category/products/) [ Announcements ](https://blog.bitfinex.com/category/announcements/) [ Education ](https://blog.bitfinex.com/category/education/) [ Bitfinex Securities ](https://blog.bitfinex.com/category/bitfinex-securities/)

# What is the Enigma Network?

15 September, 2023 

Share

Share on Facebook Share on X Share on LinkedIn

**Since its introduction, Bitcoin has promised to revolutionise the way our money functions by introducing programmability. However, delving into its technical underpinnings can be daunting, particularly for those new to crypto. Today we’ll take a stab at demystifying the Enigma Network, a groundbreaking solution to Bitcoin ’s scalability issues.**

## The Enigma Network: A Settlement Layer For Bitcoin

At its core, the [Enigma Network](https://app.sigle.io/polydeuces.id.stx/bo-iHio5_4iTlvWwXwZ9l) functions as a “Settlement Layer” between Bitcoin’s base blockchain and its secondary layers. It bridges Bitcoin’s main chain (L1) and second layer solutions such as the Lightning Network or [RGB](https://blog.bitfinex.com/education/how-can-rgb-improve-bitcoin/) (L2). Enigma’s primary function is to batch transactions, allowing for simultaneous executions on both L1 and L2. This layer offloads significant data, easing the strain on both primary and secondary chains. The only catch is that it would all work using [Check Template Verify](https://thebitcoinmanual.com/articles/check-template-verify/) (CTV), which would need to be implemented in Bitcoin under a future soft fork.

In the conventional Bitcoin transaction setup, one sends a transaction to be mined within a block. With the Enigma Network’s approach, multiple actions can be executed in parallel, where multiple transactions are represented by a single anchor transaction. Consider you need to conduct three transactions. You’d compute a SHA256 hash of all these transactions and embed this hash within an anchor transaction that uses CTV at its core. 

This anchor acts as an on-chain reference and certification for the three transactions, but the specifics of each transaction aren’t maintained on-chain. This ensures transactions are confirmed without cluttering the main blockchain. CTV, specifically through [BIP-119](https://www.coindesk.com/layer2/2022/05/20/bip-119-unpacking-ctv-and-how-it-would-change-bitcoin/), introduces the concept of pre-committing transactions. This means, instead of only being able to transact with already confirmed UTXOs, users can now sign and commit transaction intentions ahead of time. 

Think of this as packaging multiple transactions which are nested within a single hash – an anchor – thereby reducing on-chain space and increasing efficiency. With CTV, transaction aggregation is possible, which means multiple transactions can be represented and verified with a single anchor, drastically reducing the load on Bitcoin’s blockchain. We covered CTV recently, in our article about [Bitcoin soft forks](https://blog.bitfinex.com/education/what-soft-forks-are-currently-being-debated-in-bitcoin/) currently being debated by the community.

## What Kind of Advantages Could Anchor Transactions Provide?

One of the major advantages would be Non-Interactive Channels or Lightning channels that don’t need to be mutually established. They can remain dormant (or “cold”) until you decide to reveal them. This flexibility allows users to re-establish channels without the need for fresh transactions, a feature beneficial for privacy and efficiency.

Another advantage would be improved trust-minimization. In the traditional Bitcoin ecosystem, a certain degree of trust is required, especially in scenarios where private keys might be potentially exposed. However, with anchor transactions, the risk is mitigated as only hashed references are used. The aim is to enhance security and remove trust barriers. For instance, certain tasks like statechain-based private key swaps, creating vaults, or handling inheritance could now be conducted without the need to delete private keys, ensuring safety, and preventing loss of funds.

Another huge benefit which Enigma Network could deliver, is a massively reduced on-chain footprint. Since each anchor represents multiple transactions, on-chain activity is significantly reduced. This not only conserves space but also alleviates transaction costs. Users have the liberty to create as many transaction intents as needed without bogging down the network.

The entire Bitcoin community benefits from this system. Every transaction and UTXO on the blockchain becomes a communal asset. Instead of individual ownership, each transaction serves as an anchor for economic activity embedded within the hashes. Utilising these techniques can dramatically reduce on-chain transactions, as the real activity is essentially ‘hidden’ inside the anchor transaction hashes.

The integration of CTV in the Enigma Network for anchor transactions has the potential to redefine the transaction landscape of Bitcoin. It offers a more streamlined, efficient, and inclusive transaction mechanism, making Bitcoin more scalable and user-friendly. By leveraging the power of CTV, the Enigma Network will pave the way for a more evolved Bitcoin ecosystem.

## Enigma Network’s Advanced UTXO Variants

The Enigma Network introduces a fresh, deterministic approach to on-chain transactions, characterised by automatic UTXO pooling and asynchronous payments. As collaboration within the network amplifies, so do its scalability and privacy features. This modern framework encourages users to transition from thinking about individual transactions to envisioning broader tasks.

Here’s a brief rundown of the novel UTXO variants proposed within the Enigma Network:

  * ATXO (Anchor UTXO) – ATXOs represent the primary UTXOs that are committed to the blockchain. They act as anchors, holding the references for off-chain transactions.
  * LTXO (Lightning UTXO) –  LTXOs denote Bitcoins stored in Lightning channels, which facilitate faster, off-chain transactions.
  * STXO (Settlement UTXO) – STXOs embody regular transactional tasks, like channel operations or standard payments. Rather than being directly committed to the blockchain, STXOs are held by ATXOs. They are unique in that they can only serve as inputs for generating a Partially Signed Bitcoin Transaction (PSBT) targeted at an ATXO. It’s vital to note that mishandling or losing STXOs could result in fund losses.
  * VTXO (Virtual UTXO) – VTXOs are ephemeral UTXOs with privacy features resembling e-cash. They offer enhanced transactional privacy and are exchanged between users without the necessity of the Mempool, ensuring a non-interactive, private transactional experience.


An essential characteristic of the Enigma Network is its emphasis on collaborative payments. Instead of isolated transactions, users can collaborate with channel partners for combined payments, potentially levying a minor fee for amalgamating transactions.

Moreover, while only ATXOs are directly committed on-chain, STXOs and VTXOs can be freely traded amongst users without the Mempool’s involvement. Should users decide to revert their LTXOs, STXOs, or VTXOs to standard UTXOs, these would be reflected as being ejected from the associated ATXO pool. Subsequent transactions with an ATXO would reincorporate them into the network.

In essence, the Enigma Network offers a layered, efficient transactional ecosystem, enhancing both scalability and privacy through its innovative UTXO variants.

## The Potentially Positive Impact on Scalability

Transactions need only interface with the main chain when visibility or [inscription](https://unchained.com/blog/bitcoin-inscriptions-ordinals/) is mandatory. This reduces the data storage burden on L1. Meanwhile, L2 (Lightning) channel opening and closing transactions can be omitted once they’re redundant, bypassing their need to ever be integrated into the blockchain. This streamlines Bitcoin’s main chain, and reduces the demand for precious blockspace.

Enigma’s introduction of ‘Payment Pools’ is a game-changer. Users can pool their funds, sharing transaction fee costs. These pools can amalgamate for cooperative endeavours and detach afterward. This novel feature reshapes Bitcoin transaction processing, minimising costs for all pool members.

In the Enigma Network, payment pools serve as a collaborative mechanism where multiple individuals jointly manage a single ATXO. Each participant in the pool maintains a stake in this shared UTXO. The real novelty emerges when two individuals, each belonging to separate payment pools, transact: their respective pools can temporarily merge into one unified ATXO. This consolidation isn’t permanent; subsequent transactions can lead to the pools diverging again, reflecting the intermittent nature of collaboration. 

The inherent flexibility of these dynamic merges and separations introduces both complexity and versatility to transactions. Furthermore, within a payment pool, participants have the advantage of sharing transaction costs, ensuring that no single member incurs a hefty fee. This shared cost structure keeps the pool economically competitive. Intriguingly, the internal transactions and modifications within these pools remain obscured, preserving privacy by making the internal UTXO redistributions undetectable externally. 

When a payment pool is established, it can comprise numerous inputs but will result in a singular ATXO output. If only internal adjustments take place during on-chain updates, the resulting transaction will exhibit the original and the updated ATXO, devoid of any ejections. However, should there be a breakdown in collaboration or the introduction of new members, the anchor transaction will manifest additional inputs and ejected ATXOs.

Enigma also pioneers ‘Transaction Aggregation’ and Decentralised Mining Pools (dpools). Decentralised Mining Pools, or dpools, represent a groundbreaking shift in the mining landscape by offering a decentralised approach to mining operations. Unlike traditional mining pools, where a centralised entity oversees the operations, dpools are inherently democratic. 

They function without a central authority governing the funds, and all operations are transacted directly through the blocks, removing dependencies on communication channels like DNS. This design ensures that once a dpool’s template is set with its inaugural mined block, it remains resistant to external dominance or control. One notable perk of dpools is the equitable distribution of collected fees across several blocks, ensuring a consistent reward for miners irrespective of individual block fee variations.

Within the dpool framework, innovative features emerge, including “Compaction.” This mechanism enables streamlined on-chain transactions by consolidating multiple payments to a single recipient into one transaction. For instance, if both Alice and Carol intend to pay Bob, their transactions can be compacted, merging their UTXOs into a singular UTXO directed at Bob. 

The magic intensifies when participants like Alice, Bob, and Carol are members of individual payment pools. Through the dpool’s functionality, their separate pools can converge into a unified entity, allowing for efficient transaction consolidation directly on the foundational layer of the network. This not only optimises space but also maximises the number of transactions accommodated per block.

With the surging popularity of protocols like [Ordinals, Stamps, and BRC-20 tokens](https://blog.bitfinex.com/education/what-does-the-bitcoin-defi-ecosystem-look-like/), transaction fees recently skyrocketed by 500% and remained high for several months. This surge strains the system and upsets economic equilibrium. Enigma’s solution is UTXO pooling. Users can split transaction costs within a pool, considerably lowering individual fees. Miners enjoy heightened overall fees from these aggregated transactions, while inscribers can schedule their data processing during less busy times, promoting consistent operations. Inscribers, acting as fallback buyers for block space, can adjust their systems to only transact when fees are most economical.

The Enigma Network emerges as a game-changing innovation, holding the potential to redefine the contours of Bitcoin’s scalability and improve the Lightning Network’s efficiency. At its core, Enigma introduces a novel approach to transactions, focusing on multi-threaded actions, anchor transactions, and the strategic use of different UTXO variants. This design allows for significant reductions in direct on-chain activity, thereby alleviating the congestion on the Bitcoin blockchain. 

The seamless integration between Enigma’s anchor transactions and the Lightning Network (or another potential layer two) blurs the lines between Bitcoin’s primary layer and secondary scaling solutions. By doing so, Enigma paves the way for a more holistic ecosystem where atomic actions can span across both layers, maximising efficiency and scalability.

## Trading Starts Here

Master your financial future.  
Use the best tools to succeed 

[ Log in ](https://www.bitfinex.com/login) [ Sign up ](https://www.bitfinex.com/sign-up)

We use [_cookies_](https://www.bitfinex.com/legal/cookies_policy) to ensure that we give you the best experience on our website. If you continue to use this site we will assume that you are happy with it.Ok

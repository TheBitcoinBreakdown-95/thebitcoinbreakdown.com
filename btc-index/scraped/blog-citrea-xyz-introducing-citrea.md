# blog.citrea.xyz -- Scraped Content

**URL:** https://blog.citrea.xyz/introducing-citrea
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\Citrea.md, BTC\ZK Rollups.md
**Scraped:** 2026-04-12

---

[ ](https://www.blog.citrea.xyz)

Sign in Subscribe

[Announcements](/tag/announcements/) Featured

# Introducing Citrea: Bitcoin’s First ZK Rollup

  * [ ](/author/citrea-team/)


#### [Citrea Team](/author/citrea-team/)

06 Feb 2024 • 6 min read

Citrea: Bitcoin's First ZK Rollup

Today we introduce Citrea, the first rollup that enhances the capabilities of Bitcoin blockspace with zero knowledge technology.

The Bitcoin scalability landscape has long been dependent on solutions that move security and demand off-chain, off-Bitcoin. Citrea is set to change this reality by scaling Bitcoin in its entirety with zero-knowledge proofs, ensuring on-chain verifiability and data availability within the Bitcoin network. This approach makes Citrea the first scaling solution to enable more complex applications without compromising Bitcoin security and changing its consensus rules.

## The Problem with Creating New Blockspace

Bitcoin has the most secure, decentralized, and censorship-resistant blockspace. Scaling proposals that create new blockspaces cannot inherit any of these properties of Bitcoin. These proposals or implementations merely offer alternative blockspaces; they do not scale the Bitcoin blockchain. Constructing sidechains with an alternative blockspace competes with Bitcoin in the long term and risks users' funds through insecure bridges and network constructions.

### Bitcoin Blockspace is in High Demand

People are demanding Bitcoin for all their on-chain needs because of its security, decentralization, and censorship resistance. Over the past few months, we have observed exponential interest in Bitcoin blockspace, reflected in the fee rates. Whether it is a payment or inscription transaction, people want to get included in the blockspace and are willing to pay for it. Ensuring sustainable participation in the Bitcoin network is vital for its long-term health and security budget, but there is a trade-off: the inevitable exclusion of some transactions due to the high fees and necessary block size limit. It's imperative that Bitcoin scales to include many more complex transactions without changing its core principles. 

This increasing interest highlights a significant problem with existing scalability proposals: their failure to address the growing demand for inclusion in the Bitcoin blockspace.

### Existing Scalability Proposals Don't Scale Bitcoin

Bitcoin has long faced the challenge of handling more transactions and enabling a wider array of applications without compromising its security or core principles. This multifaceted issue has proven difficult to address in its entirety. Some attempts have targeted scaling Bitcoin’s payment throughput, such as Lightning, while others have focused on scaling the functionality of the BTC asset, like sidechains. While the first scaling proposal fell short in bringing programmability to Bitcoin, the latter missed a critical point: the active and effective utilization of the Bitcoin blockchain itself.

In the current landscape, the inherent demand for Bitcoin blockchain is being redirected to separate consensus protocols, to sidechains. This approach results in a trade-off — sacrificing Bitcoin’s security and misaligning with its incentives in exchange for lower fees and more use cases for BTC. Consequently, Bitcoin, dominated by sidechains, suffers from scaling solutions that fail to serve its long-term health and incentives in any meaningful way. These solutions, though well-intentioned, do not operate on the Bitcoin blockchain, do not contribute to Bitcoin security, and ultimately, do not scale the Bitcoin blockchain as needed.

Once again, a demand for Bitcoin moved to a sidechain is not a demand for Bitcoin anymore. 

### Scale the Bitcoin Blockspace

Truly scaling Bitcoin requires establishing a symbiotic relationship between Bitcoin and the scaling solution. The scaling solution must actively and efficiently utilize Bitcoin blockspace to scale the demand and increase its expressivity and throughput without changing its protocol. **Scaling Bitcoin blockspace is the only way to transact with Bitcoin security.** Any other alternative cannot inherit full Bitcoin security.

**The most secure and incentive-aligned way to scale Bitcoin blocks is to shard the execution with on-chain verifiability and data.** The only way to achieve easy verifiability by Bitcoin is through leveraging zero knowledge or fraud proofs. As fraud proofs require vast amounts of data to be written on Bitcoin, ZK proofs are the most efficient way to verify the validity of execution inside Bitcoin within the block size limit.

ZK Rollups create an execution shard and batch multiple transactions on the shard while verifying them on-chain with a succinct mathematical proof as well as minimal essential data to reconstruct the state. This method enables ZK Rollups to utilize underlying blockspace verifiably in the most efficient manner, scaling the L1 with its full security.

## Enter Citrea: Bitcoin Security at Scale 

Citrea is the first rollup on Bitcoin that enables greater expressivity and increases the utility of Bitcoin blockspace without ever leaving Bitcoin. Citrea keeps the demand for Bitcoin within its network and ensures that Bitcoin Network serves as a data availability and settlement layer for Citrea transactions. Citrea requires no consensus changes to Bitcoin.

Citrea represents a significant milestone for Bitcoin: **it is the only execution layer on Bitcoin that settles on Bitcoin, the first ZK proof verification, and the first universal L2 verification inside Bitcoin.** Citrea’s mission is to advance Bitcoin into its next phase, foundation for the world's financial infrastructure, where developers can build everything on Bitcoin.

Citrea batches thousands of transactions, processes them in zkVM, and produces a succinct validity proof asserting the correctness of the execution as well as the output data. For the first time in Bitcoin history, Citrea validity proofs are inscribed and natively verified within the Bitcoin blockchain. Citrea comes with a native ZK proof verifier smart contract on Bitcoin L1, built in BitVM.**Unlike monolithic sidechains, Citrea creates a modular world for Bitcoin with its execution shard that keeps the settlement and data availability on-chain, on-Bitcoin.**

Citrea: A Modular Touch to Bitcoin

Citrea creates consistent fee revenue for miners through data availability, trustlessly scales BTC beyond Bitcoin with validity proofs, and allows developers to build anything on its EVM equivalent execution shard.

### Scaling Bitcoin Security

Citrea is the only execution layer on Bitcoin that actually settles on Bitcoin. Every transaction occurring on Citrea is fully secured by zero-knowledge proofs and verified by Bitcoin. The execution environment of Citrea is trustless with respect to Bitcoin and is accessible to all participants of the Bitcoin Network.

As a result, Citrea ensures that it satisfies Bitcoin equivalent data availability, censorship resistance, and re-org resistance guarantees.

  1. **Bitcoin as App Bedrock:** Citrea's mission is to build a programmable liquidity layer on top of the most secure and decentralized blockchain, Bitcoin. We believe Bitcoin blockspace must be used to settle all kinds of financial activities efficiently such as trustlessly buying BTC, leveraging BTC, or lending BTC. Most existing meta protocols attempting to provide these features are trusted and inefficient. Citrea is the most efficient and secure platform to build applications on Bitcoin.
  2. **Bitcoin Settlement and Trust-Minimized Two-Way Peg:** For the first time in Bitcoin history, a universal L2 is settled on Bitcoin, enabling the first ever universal trust-minimized two-way peg. Prior to Citrea, Layer 2 solutions relied on the honest majority assumption of a multi-signature, such as open or closed federations. With Citrea, the validity proofs are verified in Bitcoin using BitVM paradigm, as long as one network participant is honest. BitVM is based on fraud proofs, meaning that ZK proofs of Citrea are being optimistically verified on the Bitcoin network. In the future, a ZK proof verifier opcode will enable a fully trustless two-way peg mechanism.
  3. **EVM Equivalence:** Building Citrea with full EVM equivalence enables all the EVM developers to build on Bitcoin, effortlessly. Citrea ships a Type 2 zkEVM, fully equivalent to EVM, built using RISC Zero. Citrea is not limited to a single VM by design, and can adopt new VMs such as WASM VM in the future thanks to its modular architecture.


## What’s Next?

### Internal Devnet is Enabled

We are running Citrea Devnet with a synthetic native BTC internally for critical infrastructure integrations and tests. Trust-minimized two-way peg with BitVM is under heavy development.

**We welcome infrastructure partnerships.** If you are an infrastructure provider interested in partnering with Citrea, please get in touch with us at: [_info@citrea.xyz_](mailto:info@citrea.xyz)

### Revealing The First Trust-Minimized Two-Way Peg

**Keep an eye out for the reveal of Citrea's trust-minimized peg design.** We will announce our bridge design and open-source our codebase in the coming weeks!

### Public Testnet

**We are making rapid progress.** We’ve been working hard on building a robust testnet for the first rollup on Bitcoin. We’re excited to share more in the coming months. Keep an eye on our [_socials_](https://twitter.com/citrea_xyz?ref=blog.citrea.xyz) and [_blogs_](http://blog.citrea.xyz/?ref=blog.citrea.xyz).

### Build with Citrea

**Our developer contact form opens today.** Citrea has been incubated by [_Chainway Labs_](https://twitter.com/chainway_xyz?ref=blog.citrea.xyz) for over a year, and is well-funded. If you’re interested in building with us or deploying on Citrea, please get in [_touch_](https://citrea.typeform.com/buildwithus?ref=blog.citrea.xyz). Check out our [_documentation_](https://docs.citrea.xyz/?ref=blog.citrea.xyz) to explore Citrea’s technology.

## Making Bitcoin the Foundation for World’s Finance

Citrea’s vision is to build scalable infrastructure that advances Bitcoin into its next phase, the foundation for the world’s finance. To achieve this vision, we believe that Bitcoin blockspace must be enhanced to include more transactions and offer more expressivity and features  without changing its consensus rules.

Bitcoin, with its security, decentralization, and censorship resistance, is perfectly positioned to serve as the foundation for the world’s finance. Recognizing this potential, Citrea builds on these strengths and makes Bitcoin a base layer for a dynamic ecosystem of DeFi, gaming, NFTs, and more. Citrea will only get bigger and more advanced with its modular world anchored on Bitcoin.

We are incredibly bullish on our vision and committed to working towards it. 

On Bitcoin, For Bitcoin.

## Get Ready

Join the community and follow us on Twitter to be an early adopter. You don’t want to miss any updates from Citrea!

  * Join [_Discord_](https://discord.gg/citrea?ref=blog.citrea.xyz)
  * Follow [_Twitter | X_](https://twitter.com/citrea_xyz?ref=blog.citrea.xyz)


## Acknowledgments

We would love to thank Cem Ozer, who initially pushed us towards committing to building the first rollup on Bitcoin. Since then, Citrea has evolved to a larger vision with the invention of BitVM by Robin Linus.

We thank Ekram Ahmed and CJ Huntzinger for providing their invaluable expertise through the branding and marketing process. We thank Emre Tekisalp for helping us to find our way along our journey.

## Sign up for more like this.

Enter your email Subscribe

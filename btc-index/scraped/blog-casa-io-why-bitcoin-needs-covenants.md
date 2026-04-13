# blog.casa.io -- Scraped Content

**URL:** https://blog.casa.io/why-bitcoin-needs-covenants
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\CovenantsTimeout treesCTV.md
**Scraped:** 2026-04-12

---

[](https://blog.casa.io)

Casa Blog - Bitcoin Security Made Easy

[Bitcoin](/tag/bitcoin/) [covenants](/tag/covenants/) [Technical](/tag/technical/)

# Why bitcoin needs covenants

by [Jameson Lopp](/author/jameson-lopp/) 3 years ago 9 min read

Bitcoin script is used to define the conditions that must be met in order to spend a given UTXO. When you create a bitcoin address to receive funds, that address is effectively a (transformed) hash of the bitcoin script that defines what is required in order to unlock the deposited funds and spend them. 

At time of writing, bitcoin script can ONLY define the conditions that must be met for the inputs (funds being spent) in a bitcoin transaction. There is NOT a way to constrain any of the attributes for the outputs of a bitcoin transaction (where the spent funds are being deposited.)

> A bitcoin covenant is a mechanism to enforce conditions on future bitcoin transactions.

Why should we care about having the ability to constrain output conditions? Bitcoin has worked fine for 14 years without that functionality, right? Well, it's not for lack of trying!

### A lengthy history of covenant proposals

The discussion of covenants has been ongoing for over 9.5 years as of time of writing!

In general chronological order, the covenants discussions I've found (and there are probably others I've missed):

  * CoinCovenants ([Bitcointalk post](https://bitcointalk.org/index.php?topic=278122.0))
  * CHECKOUTPUTVERIFY ([whitepaper](https://fc16.ifca.ai/bitcoin/papers/MES16.pdf))
  * OP_CHECKSIGFROMSTACK ([blog post](https://blog.blockstream.com/en-covenants-in-elements-alpha/))
  * SIGHASH_ANYPREVOUT ([BIP-118](https://github.com/bitcoin/bips/blob/master/bip-0118.mediawiki))
  * Oleg Andreev's Vaults ([blog post](https://blog.oleganza.com/post/163955782228/how-segwit-makes-security-better))
  * Bryan Bishop's Pre-signed Vaults ([mailing list post](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2019-August/017229.html))
  * OP_TAPLEAFUPDATEVERIFY ([mailing list post](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2021-September/019419.html))
  * OP_CAT ([blog post](https://medium.com/blockstream/cat-and-schnorr-tricks-i-faf1b59bd298))
  * OP_CHECKOUTPUTSHASHVERIFY ([draft BIP](https://github.com/JeremyRubin/bips/blob/op-checkoutputshashverify/bip-coshv.mediawiki))
  * Efficient Bitcoin Vaults ([draft BIP](https://github.com/fresheneesz/bip-efficient-bitcoin-vaults))
  * OP_CHECKTEMPLATEVERIFY ([BIP-119](https://github.com/bitcoin/bips/blob/master/bip-0119.mediawiki))
  * OP_TXHASH ([mailing list post](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2022-January/019813.html))
  * OP_EVICT ([mailing list post](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2022-February/019937.html))
  * OP_TX ([mailing list post](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2022-May/020450.html))
  * OP_CAT2 ([mailing list post](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2022-May/020427.html))
  * OP_VAULT ([whitepaper](https://jameso.be/vaults.pdf))


### Types of covenants

Each covenant proposal has different properties, but tends to fall in one of two categories for different attributes of how it operates.

  * **Generalized** \- these tend to be a lot more flexible and offer more functionality, but also often come with more complexity and trade-offs. Examples include OP_CHECKTEMPLATEVERIFY, OP_CHECKSIGFROMSTACK, OP_CAT.
  * **Restrictive** \- these covenants targeted only adding a specific set of functionality and tend to be easier to reason about. Examples include Brian Bishop's Pre-signed Vaults, OP_VAULT.


Some covenant proposals are essentially single use while others can propagate their restrictions forward in perpetuity.

  * **Non-recursive** \- these covenants can only apply their rules for one "round" of the bitcoin value flowing through whatever logic tree you architect. Examples include OP_CHECKTEMPLATEVERIFY.
  * **Recursive** \- these can replicate themselves (and thus their restrictions) into the future UTXOs to which funds are sent, without limitation. Examples include OP_VAULT.


At a more detailed implementation level, covenant proposals tend to add the functionality to the protocol in one of two ways.

  * **Opcode based** \- these covenants require a soft fork to add a new operation (or multiple operations) to bitcoin's scripting language. Examples include OP_CHECKTEMPLATEVERIFY and OP_VAULT.
  * **Signature based** \- instead of storing spending constraints inside the bitcoin script, the future (presigned) transactions can have their attributes verified by constructing them while executing script and then comparing hash values with OP_CHECKSIG. Examples include OP_CHECKSIGFROMSTACK and SIGHASH_ANYPREVOUT.


### Covenant Use Cases

  * [Batched Lightning Channels](https://utxos.org/uses/batch-channels/)
  * [Blockchain congestion control](https://utxos.org/uses/scaling/)
  * [Coin Pools](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2020-June/017964.html)
  * [Decentralized options](https://utxos.org/uses/options/)
  * [Discreet Log Contract improvements](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2023-January/021339.html) ([2](https://bitcoinops.org/en/newsletters/2022/02/02/#improving-dlc-efficiency-by-changing-script))
  * [Drivechain 2-way Pegs](https://utxos.org/uses/drivechains/)
  * [Non Interactive Lightning Channels](https://utxos.org/uses/non-interactive-channels/)
  * Scripts of unbounded length
  * [Soft Fork bets](https://utxos.org/uses/taproot-bet/)
  * [Spacechains](https://gist.github.com/RubenSomsen/c9f0a92493e06b0e29acced61ca9f49a#spacechains)
  * [Statechains](https://gist.github.com/RubenSomsen/c9f0a92493e06b0e29acced61ca9f49a#statechains)
  * Transaction-level MAST
  * [Trustless Mining Pools](https://utxos.org/uses/miningpools/)
  * Turing complete contracts
  * [Vaults](https://github.com/ariard/bitcoin-contracting-primitives-wg/blob/main/use-cases/vaults.md)


### Covenant Complexities

> Great security requires usability; complexity is the enemy of security.
> 
> — Casa (@CasaHODL) [April 21, 2020](https://twitter.com/CasaHODL/status/1252638980782374916?ref_src=twsrc%5Etfw)

Signature based covenant proposals require architecting and signing all of the possible future transactions ahead of time, which locks you into specific private keys and fee rates.

Some proposals even require you to generate short-lived (ephemeral) private keys that you use for setting up all of the pre-signed transactions, and then the onus is on you to securely delete those private keys so that they can't be used by an attacker to redirect funds elsewhere.

Covenants that require setting up pre-signed transactions also mean that you have to repeat this process for every new deposit (because it creates a new UTXO that you want to subject to the spending conditions of your covenant.) Meaning that the ongoing maintenance cost is onerous and that to move the funds through the covenant paths you have to broadcast a separate transaction for every UXTO you want to spend. It's easy to see how this complexity can blow up to outrageous proportions. Here's one example of a specific vault's logical flow, constructed with pre-signed transactions:

[Full size image source](https://diyhpl.us/~bryan/irc/graphviz-transaction-tree.png)

As you can imagine, pre-committing to all of these potential flows of funds at some arbitrary length of time before they are used (potentially many years) leads to all kinds of difficult questions about the security and availability of the keys where funds _might_ end up.

Some covenant constructions involve absolute timelocks to enforce delays to slow down attackers and give you "escape hatches" to get out of scenarios in which your keys have been compromised. This can introduce an additional complexity of needing to update your covenant (and all of its pre-signed transactions) when the timelock expires. Covenants that only use relative timelocks don't have this problem. It's worth noting that this is not merely a theoretical issue, as the bitcoin script used to secure the BTC for the Liquid sidechain peg uses similar timelock logic and this resulted in a security issue that had to be patched.

[Patching the Liquid Timelock IssueBy Adam BackBlockstream Engineering BlogBlockstream](https://medium.com/blockstream/patching-the-liquid-timelock-issue-b4b2f5f9a973)

[Evil covenants](https://github.com/ariard/bitcoin-contracting-primitives-wg/blob/main/constraints/evil-covenant.md) are a scary scenario, but I think it's safe to classify them as FUD. The claim is that recursive covenants could be used to implement a “taint” on existing UTXOs, such as requiring a 3rd-party signature for their use, which would spread throughout the coin supply and be impossible to remove. The reason I consider this to be FUD is that a similar system could be implemented today, by use of 2-of-2 multisignature scripts in which one party refuses to sign transactions that don’t preserve the 2-of-2 “covenant” restriction. Such schemes would be impossible to force people to adopt on this voluntary network. **Caveat** : it [was pointed out](https://twitter.com/LaurentMT/status/1617925707157630976) that some times of covenants could be used to hide restrictions from recipients; as such I'd advocate that covenants should require users to commit to their conditions to prevent "rug pulls."

### Vaults

There are clearly a LOT of use cases that could potentially be unlocked with the right kind of covenant implementation. Personally, having spent 8 years working on high security multi-signature wallets, I'm most interested in vaults. I believe their value they offer is quite straightforward and is applicable to **every single self-custody bitcoin user,** regardless of what type of wallet they are running.

> A bitcoin vault is a specific type of covenant transaction that enforces a timelock on the transfer of control of funds to a hot wallet, but enables an immediate transfer of funds into a recovery wallet.

https://jameso.be/vaults.pdf

If it wasn't clear from the decade-long history of 15+ proposals, covenants are a particularly thorny problem with a **ton of trade-offs**. In particular, the need to precompute and presign large transaction graphs has always felt like a non-starter to me in terms of usability, especially for users who operate distributed multi-key architectures.

OP_VAULT is the latest of many vaulting proposals; it uniquely allows for:

  1. Batching operations
  2. Partial unvaultings
  3. Dynamic withdrawal targets
  4. Recursive deposits


OP_VAULT aims to be more flexible for end users by allowing them to create a vault without requiring them to commit to specific future transactions, giving them fee flexibility when they go to spend, enabling them to batch easily, and allowing partial spends from their vaults. I won't go into further details, but will simply say that this particular proposal feels like it has taken the KISS (Keep It Simple, Stupid) principle to heart. When engineering security solutions we prefer simplicity because complexity is the enemy of security.

This Satoshi quote was originally referencing multisignature escrow transaction capability, but I dare say it's far more applicable to vaults. The ability for an individual to retrieve stolen funds, without the need for trusted third parties or compromising any of the inviolable principles of the protocol, would be a huge value add.

### Vaults Enable Key Compromise Policies

What do you do when a key is compromised?

Previously, with simple single signature setups, a key compromise was catastrophic. You only learned of the compromise _after your funds were lost_.

With multi-key setups, it's slightly better. But it requires more onerous **proactive maintenance** to regularly check on the status of your keys. There is still no global way (on the blockchain) to know that a compromise has occurred until it's too late.

Note that the CryptoCurrency Security Standard states that a [Key Compromise Policy is required](https://cryptoconsortium.org/cryptocurrency-security-standard-documentation/details/#elementor-toc__heading-anchor-7) in order to pass even the lowest level of certification. To date, Key Compromise Policies have only made sense for organizations / institutional custodians to enact, but the amazing thing about vaults is that they make it sensible and attainable even for individuals who are protecting more than $1,000 to enact! You can learn more about Key Compromise Policies in this CCSS livestream:

### Game Theory FTW

With the right tools, we can be _reactive_ rather than only _proactive_ with regard to recovering from key compromises. If you're moderately technical, the following diagram may be familiar:

Lightning Network channel construction

The above shows the set of pre-signed transactions that are used to construct lightning channels and update them. Lightning employs Hashed Timelock Contracts (HTLCs) to create a set of game theory that makes it difficult for one party to cheat the other.

Vaults allow for the creation of a new set of game theory. Similar to how you can run watchtowers to look out for a Lightning channel counterparty trying to cheat you, you would be able to run a watchtower to make sure no one has compromised your bitcoin vault. If you find that a compromise has occurred, sweeping the funds to safety is simple enough that you can automate it!

Bitcoin vaults are far superior to timelocks, which are a feature we get requested at Casa somewhat regularly. I've written about some of the reasons why timelocks are not user-friendly. There are good reasons why you don't find timelocks as a feature in many wallets.

[Bitcoin multisig time locking challenges | CasaQ: How do you prevent $5 wrench attacks? A: Make funds impossible to move.Casa BlogJameson Lopp](https://blog.casa.io/bitcoin-multisig-time-locking-challenges/)

Additionally: a compromised timelocked bitcoin wallet creates a race-to-the-bottom scenario once the timelock expires. Think about it: both you and the attacker have the private keys to your funds. So you essentially are racing to bribe the miners to confirm the withdrawal transaction that sends the money to yourself rather than the other key holder.

Such is the downside to only having proactive security tools in your toolbelt; even if you manage to construct a setup that is difficult to compromise, a successful compromise will likely lead to catastrophic or near-catastrophic loss.

To be clear, covenants and vaults are not a silver bullet. Anything that can be secured can be compromised. As such, it's incredibly important that the security characteristics of a vault's recovery wallet are quite difficult to compromise, otherwise an attacker could compromise the recovery wallet first, take their time compromising the vault, and then simply sweep funds to the recovery wallet and then immediately sweep them to a separate address.

It is my sincere belief that every bitcoin self-custody user and every wallet developer should be salivating over the prospect of user-friendly vault functionality. The ability to "claw back" funds that have been lost due to a compromised security architecture means that bitcoiners can sleep more peacefully at night, knowing that they can be fallible, make mistakes, and not have to suffer from catastrophic loss due to a single oversight.

### Further reading

[BitcoinCovenants.com](https://bitcoincovenants.com/)

Bitcoin Optech coverage of [covenants](https://bitcoinops.org/en/topics/covenants/) and [vaults](https://bitcoinops.org/en/topics/vaults/)

[Bitcoin Contracting Primitives Working Group](https://github.com/ariard/bitcoin-contracting-primitives-wg)

[MATT Covenants](https://merkle.fun/)

[TFTC Podcast Episode on OP_VAULT](https://tftc.io/tftc-podcast/388-op_vault-and-bitcoin-governance-james-obeirne/)

[UTXOs.org](https://utxos.org/)

* * *

### Stay updated on privacy and security news

Our Security Briefing newsletter provides free updates and analysis on recent developments in bitcoin, digital privacy, and crypto security. Sign up below.

Read more posts by this author

[](/author/jameson-lopp/)

#### [Jameson Lopp](/author/jameson-lopp/)

Jameson Lopp is co-founder and Chief Security Officer of Casa. He is passionate about creating tools to empower individuals; he has been building bitcoin wallets since 2015.

[](https://twitter.com/intent/tweet?text=Why%20bitcoin%20needs%20covenants&url=https://blog.casa.io/why-bitcoin-needs-covenants/) [](https://www.facebook.com/sharer/sharer.php?u=https://blog.casa.io/why-bitcoin-needs-covenants/) [](javascript:) The link has been copied!

# blog.mutinywallet.com -- Scraped Content

**URL:** https://blog.mutinywallet.com/note-duel-superposition
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\DLC.md
**Scraped:** 2026-04-12

---

[ ](https://blog.mutinywallet.com)

[DLC](/tag/dlc/)

# Announcing Superposition and Note Duel, our first two DLC experiments

Superposition and Note-Duel, two new experiments we've built with DLCs.

  * [ ](/author/benthecarman/)


#### [benthecarman](/author/benthecarman/)

Jan 26, 2024 • 5 min read

For the past three years, I've been a co-host of Austin BitDevs. Most months we discuss something cool in bitcoin or cryptography that relates to DLCs. And each time my task is the same: "Ben, can you explain DLCs for us?"

Today I'll leave the [low-level DLC explanation](https://suredbits.com/discreet-log-contracts-part-1-what-is-a-discreet-log-contract/?ref=blog.mutinywallet.com) to others. Instead, I'd like to introduce you to Superposition and Note-Duel, two new experiments we've built _with_ DLCs.

### Superposition

[Superposition](https://superposition.events/?ref=blog.mutinywallet.com) is a DLC oracle app where you can create and attest to events. The events you create, and your signed attestations, are all published to nostr, where it's easy to discover and use these attestations.

For instance, I can create a Superposition called "Will Mempools clear in 2024?" with two possible outcomes:

  1. Yes
  2. No  


I'll set a due date of December 24th, 2024, and click "Create". That will publish this Superposition to nostr, where other apps can make smart contracts based on the outcome. Because the events are public, and connected to a nostr profile, anyone can discover the events I publish and check my reputation as an oracle before basing a contract on those events.

On December 24 I'll return to Superposition and "observe" the outcome, which will publish a new event to nostr with my signature. Now, smart contracts based on this Superposition can use my oracle DLC signature to resolve.

Because Superposition is nostr-based, all your signatures are based on your nostr private key. If you want to stake your reputation you can sign with your nostr nsec, or if you just want to play around, Superposition can generate a new nsec for you.

### Note Duel

Alright, so what are these smart contracts that can make use of these Superposition oracles? Our first demo app is [Note Duel](https://noteduel.com/?ref=blog.mutinywallet.com).

Note Duel lets you wager a nostr "note" on the outcome of a Superposition.

To create a new duel you pick an existing Superposition, enter your opponent's nostr pubkey, choose your favored outcome, and write in a "winning note" and a "losing note". The winning note will be automatically published as a note from the winner's profile, and the losing note will be published as a note from the loser's profile.

The world's first Note Duel was against me and Paul, and oracle'd by Tony. I won:

All of this is cryptographically enforced using the magic of DLCs: my winning note and Paul's losing note only became valid with the oracle's signature. Before the oracle resolves the notes were only partially signed by the participants. Without the oracle signature, they're useless, although it's possible to verify that a signature will be made valid by the oracle signature.

For now, this is just for fun social betting but we could see in the future similar things being done to enforce things of greater importance like oracle-based fact-checking, more advanced smart contract uses, or inputs into something like a [DVM](https://www.data-vending-machines.org/intro/?ref=blog.mutinywallet.com).

### The "DLC network"

When doing a DLC, there are two main discoverability problems: finding an oracle and finding a counterparty. There is no "DLC network" where oracles can announce themselves and there is no central order book for creating contracts. The way other smart contracting systems (shitcoins) solve this is just by doing everything on-chain and making the system extremely inefficient and expensive.

That's why the emergence of nostr is such an interesting pairing with DLCs: a global broadcast system validated using schnorr signatures.

I've been talking about this [for a while now](https://twitter.com/benthecarman/status/1555631329911263232?ref=blog.mutinywallet.com), and it's exciting to get Superposition and Note Duel out the door so people can start realizing this vision and building a DLC ecosystem on nostr.

### What's next

Our goal is to eventually build DLC functionality into Mutiny. For the last few months I have been working on various [refactors](https://github.com/p2pderivatives/rust-dlc/pulls?q=is%3Apr+author%3Abenthecarman&ref=blog.mutinywallet.com) to rust-dlc to make it possible. Of course, we're not going to just be betting with notes forever, the plan is to build self-sovereign, private, and intuitive DLCs for actual money.

Initially, we'll start with on-chain DLCs, because the tech is most mature for those. On-chain DLCs have very good privacy properties: the outside world can't tell if the transaction is even a DLC much less what you're betting on, and you even have great privacy from the oracle.

### It gets better with Fedimint

On-chain DLCs are the best way to do high-value bets, but most people just want to do low-stakes prop bets with their friends.

So the next evolution will be to use Fedimint for DLCs to enable smaller, and even _more_ private bets. With on-chain bets, you are inherently revealing your UTXOs to your counterparty, and they can follow them before and after the contract. With Fedimints everything is done with ecash, so you get all of the privacy benefits of ecash: no tracking of the funds before or after the contract.

Fedimints can also greatly improve the programmability for DLCs via the Fedimint module system. For instance, you can simplify the UX of DLC creation by allowing parties to create a bet on an arbitrary event without a pre-existing oracle. It can be built in such a way that the federation is only needed in uncooperative cases, the members of the contract can always cooperatively close the contract themselves. [LLFourn](https://twitter.com/LLFOURN?ref=blog.mutinywallet.com) gave a great [presentation](https://www.youtube.com/watch?v=hCjbStBKCEQ&ref=blog.mutinywallet.com) two years ago about this and different ways we can enhance DLCs, I highly recommend watching it if you're interested in the topic.

### Learn more

I've proposed [a spec for Discreet Log Contracts over Nostr](https://github.com/nostr-protocol/nips/pull/919/files?ref=blog.mutinywallet.com) on the NIPs repo if you want to dig into the specifics of how this works. Note Duel and Superposition frontends are both powered by open-source NPM packages built with Rust and compiled to WASM: [@benthecarman/note-duel](https://www.npmjs.com/package/@benthecarman/note-duel?ref=blog.mutinywallet.com) and [@benthecarman/kormir-wasm](https://www.npmjs.com/package/@benthecarman/kormir-wasm?ref=blog.mutinywallet.com).

We have more planned for DLCs in the future and this is only the beginning. We want to thank [OpenSats](https://opensats.org/?ref=blog.mutinywallet.com) for funding this work in trying to bridge the unison of nostr and DLCs and hope to see the ecosystem flourish even more.

---
title: "So...What is Bitcoin Exactly?"
description: "Strip away the buzzwords and look under the hood. Bitcoin is pure information, sound money, proof of work, a new kind of time, and the internet of money — all at once."
chapter: 6
order: 1
draft: false
---

We've covered what bitcoin does, why it matters, what problems it solves, where it came from, and what properties it has. Now let's go deeper. What is bitcoin, exactly? What's actually happening under the hood?

## Pure Information

Bitcoin is <span class="glitch-hover" data-text="pure information">pure information</span>. There's never been a money like this, so it's hard to explain. Nothing like this has ever existed.

Before bitcoin, information could be freely copied on the internet — which is why you needed a centralized source of truth for anything of value. You couldn't have a scarce token in the informational realm. The genius of bitcoin was finding a way to create scarcity in a world of infinite copies.

Bitcoin has the highest value density of any asset ever created. You could have a billion dollars worth of bitcoin in your head, retaining your wealth even if stripped naked. A private key is just a number. It can be memorized, written on paper, encoded into an image, transmitted over radio, beamed via satellite, or whispered in a phone call.

Due to its lack of physicality, there is no limit to what shape bitcoin might take: text, QR codes, images, sound, emojis. Whether we're talking about storage or transmission, bitcoin can shapeshift into anything it needs to be. This is part of what makes it so resilient to censorship. How can you censor something if you can't tell what you're looking at?

Since the internet's inception, there's been a relentless trend toward dematerialization. Blockbuster became Netflix. Kodak became Instagram. Tower Records became Spotify. When the digital version of an analog entity emerges, it inevitably renders the analog obsolete. The digital version trends toward being virtually cost-free and gains the advantage of moving around the globe at the speed of light.

Now apply that to money. Bitcoin is at the forefront of dematerializing everything we've known as money — including the <span class="count-up" data-target="160">0</span> fiat currencies and even gold itself.

## Sound Money

Sound money is as necessary to a free society as a constitution. Ludwig von Mises argued in 1912 that sound money was a crucial part of classical liberal theory — not just an economic instrument but a safeguard of civil liberties:

<blockquote data-compile data-final="It is impossible to grasp the meaning of the idea of sound money if one does not realize that it was devised as an instrument for the protection of civil liberties against despotic inroads on the part of governments. Ideologically it belongs in the same class with political constitutions and bills of rights.">
<p>It is impossible to grasp the meaning of the idea of sound money if one does not realize that it was devised as an instrument for the protection of civil liberties against despotic inroads on the part of governments. Ideologically it belongs in the same class with political constitutions and bills of rights.</p>
<p class="bq-attr">— Ludwig von Mises, The Theory of Money and Credit</p>
</blockquote>

Bitcoin's architecture embodies the Austrian economic doctrine of sound money. It's a money that's harder than anything that came before. It can be transported around the world at the speed of light, permissionlessly available to all of humanity — even those who live on a dollar a day. It's not captured by elites in any way. It's completely neutral, open-source software, built by an anonymous programmer who left the project as a gift to humanity.

You can't have real capitalism without <span class="glitch-hover" data-text="sound money">sound money</span>. If sound money is a systemic risk to your financial system, then the system is garbage.

Gold served this role for most of human history, but it fails in divisibility, portability, and verifiability. Silver was used alongside gold in a bimetallic standard for most of history, but bimetallism wasn't perfect either — still not portable over telecommunications infrastructure and doomed to fail. Bitcoin solves every shortcoming of the classical sound money tradition while adding properties that no physical commodity could ever possess.

## Proof of Work

A failure to understand proof of work is a failure to understand bitcoin.

<span class="glitch" data-text="Proof of work">Proof of work</span> is the mechanism that makes it all possible — the engine that powers the trust machine. Here's how it works:

The Bitcoin network is programmed to create a new block on average every ten minutes. Mining nodes compete to create new blocks by running specialized hardware to solve a cryptographic puzzle. There's no way to cheat — the way the cryptography works, the only way to find the solution is to guess. The solution is so improbable that finding it is proof that you put in the work.

Think of it as a global math contest. The winner of each roughly ten-minute round gets a treasure chest of brand new bitcoin. To keep the contest fair, the difficulty of the next puzzle adjusts based on how quickly the last ones were solved. This is the difficulty adjustment — the mechanism that keeps blocks arriving every ten minutes regardless of how many miners are on the network.

When China banned crypto mining in 2021 and approximately half the global network went offline, Bitcoin's payment network briefly slowed down but kept working with 100% uptime. The difficulty adjustment kicked in and brought the network back up to speed. Imagine if Amazon or Microsoft had to move half their server capacity internationally with one week's notice — they'd experience issues for months. Bitcoin didn't skip a beat.

But proof of work is much more than a contest. It serves as a bridge between the physical world and cyberspace. As Gigi wrote: "Bitcoin's proof-of-work serves as a bridge between the world of atoms and the realm of information. This bridge can be built in one way and one way only: by coming up with information that is so unique, so preposterously unlikely, that certain things had to happen in the real world for this information to appear."

Energy is the link. Without it, cyberspace is a place without limits — anything can be copied, forged, faked. Proof of work imposes the laws of physics onto the digital realm. It creates real-world cost, making the ledger immutable without needing to trust a central authority. The energy used to mine bitcoin isn't "wasted" — it's there to defend bitcoin from edits, to make the historical record unbreakable.

This is why proof of work is multi-purpose: duration, costly signal, public data integrity, conflict resolution, probabilistic irreversibility, currency issuance, network security, and consensus — all solved by difficulty-adjusted proof of work.

## A New Kind of Time

Bitcoin is a clock.

This sounds strange, but it's one of the most profound aspects of what Satoshi built. Previous attempts at digital cash all failed because they needed a centralized party to keep the time — to establish the order of transactions and prevent double-spending.

Bitcoin solves this by reinventing time itself. It says no to seconds and yes to blocks.

As Satoshi wrote in the whitepaper: "We propose a solution to the double-spending problem using a peer-to-peer distributed <span class="glitch-hover" data-text="timestamp server">timestamp server</span> to generate computational proof of the chronological order of transactions."

Every ten minutes, a new block ticks. This creates an unbreakable chain of time — a canonical ordering of events that no one can dispute or reverse. The longest chain, with the most work put into it, is the correct order of transactions. There's no room for disagreement. Conflicts in the order of time are solved through mining, not through force.

Bitcoin is a decentralized clock that ticks for eternity. And that clock is what makes everything else possible — scarcity, ownership, transfer, settlement. Without a trustless way to establish time, none of it works.

## Cryptographically Secured

Under the hood of how bitcoin works, at the heart of it all, is cryptography:

- **Cryptographic timestamps** ensure the ordering of transactions
- **Hashing and mining** produce the proof of work that secures the network
- **Public and private keys** (using elliptic curve cryptography) enable ownership and transfer
- **Merkle trees** efficiently organize transaction data within each block

The private key space is 10^77 — a number so incomprehensibly large that randomly guessing someone's key would take longer than the heat death of the universe. The system uses double-hashing for additional security, and the same SHA-256 cryptographic standard that protects internet infrastructure and nuclear codes.

This is what "crypto" actually means. Not speculative tokens. Not NFTs. It means <span class="glitch-hover" data-text="cryptographically secured">cryptographically secured</span> — protected by mathematics that no computer on Earth, or any computer that will ever exist, can break.

## The Internet of Money

Now zoom out and see the full picture.

The internet is programmable information — unrestricted, global, instantly transferable information. Bitcoin is programmable money — unrestricted, global, and instantly transferable money.

The internet is decentralized informational infrastructure. Bitcoin is decentralized monetary infrastructure. The internet is an information protocol that can be built upon. Bitcoin is a money protocol that can be built upon.

<blockquote data-compile data-final="Bitcoin is digital public infrastructure for money, much like the internet is digital public infrastructure for information. It is owned by no one, and accessible to everyone. It is a public good that acts as infrastructure for civilization to utilize if they so please.">
<p>Bitcoin is digital public infrastructure for money, much like the internet is digital public infrastructure for information. It is owned by no one, and accessible to everyone. It is a public good that acts as infrastructure for civilization to utilize if they so please.</p>
<p class="bq-attr">— Jack Mallers</p>
</blockquote>

Bitcoin is less like an app — like AOL or Myspace — and more like TCP/IP, the base layer protocol of the internet. In the early days of the internet there was competition among protocols, but TCP/IP won out. Not because of complex utility at the base layer, but because it was an agreed-upon, simple, rules-based system. Bitcoin follows the same playbook.

The internet is a dumb network, and that's its most valuable feature. Almost all the intelligence lives on the edge — all the services, all the applications are created on edge devices. Bitcoin works the same way. The base layer offers one service: securely time-stamped scripted transactions. Everything else — Lightning Network, sidechains, smart contracts, custody solutions, payment infrastructure — is built on the edge, without permission.

<span class="glitch" data-text="Bitcoin is the internet of money">Bitcoin is the internet of money</span>. Currency is only the first application.

A monetary system doesn't only need money. It needs transfer services, storage, accounting systems, exchanges, options contracts, trading platforms, insurance, crowdfunding, payment infrastructure, liquidity services. Bitcoin is the money, but it's also the platform where all of these functionalities can be built.

The industries that will integrate into the internet of money are boundless. Social media, creator economies, augmented reality, the metaverse, esports, ecommerce — all connected to a global and frictionless monetary system. And because bitcoin is open and permissionless, it isn't limited to humans. AI, robots, self-driving cars, smart homes, and the unimagined future of the internet of things can all leverage this public money infrastructure.

This is the key insight: Bitcoin will not necessarily be the "money" used for every transaction. It's aiming for something much greater. Bitcoin will become the foundational protocol that the future digital economy and all global monies will be built upon.

We're talking about a new global financial and monetary system, remade on top of bitcoin. Based on rules, not rulers. The <span class="glitch-hover" data-text="separation of money and state">separation of money and state</span>.

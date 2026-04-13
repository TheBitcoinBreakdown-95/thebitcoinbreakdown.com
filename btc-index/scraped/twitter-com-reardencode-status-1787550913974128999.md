# twitter.com -- Scraped Content

**URL:** https://twitter.com/reardencode/status/1787550913974128999
**Category:** tweet
**Scrape status:** DONE
**Source notes:** BTC\The Great Script Restoration (GSR).md
**Scraped:** 2026-04-12

---

**@reardencode** (Rearden Vibes 🛩 fork/acc)

CTV, APO, LNHANCE, TXHASH, CCV, VAULT, etc. have failed to gain consensus because they are variously framed by both what they do enable and what they deliberately avoid enabling (e.g. CTV and LNHANCE avoid enabling Drivechains, but do enable coinpools and lightning symmetry respectively). This has resulted in in-fighting with everyone wanting to enable their thing, but still trying to avoid enabling some other thing.

As part of the discussion in ATX, I asked the group what specifically we want to avoid enabling. Within that group, at least, there were only two answers: we want to avoid enabling turing complete scripts (to ensure that we can statically analyze all scripts), and we want to avoid enabling anything that can increase validation costs for nodes.

With that change in framing, there was further discussion about not only what is enabled but how, which was part of Rusty's presentation: If we enable hashrate escrows via BIP300, we're kinda boxing ourselves into that way of doing pegs because it's in the protocol. If we enable hashrate escrows as part of a broader improvement in script, we are also enabling much better ways of doing pegs that are more use friendly. The how matters, not only the what.

Now we can talk about how we want to enable things, and this is where the Great Script Restoration comes in. How we improve bitcoin is by engineering the best version of script that we can. What this enables is any developer to validate their contracts on bitcoin as long as they don't unfairly burden nodes (i.e. their validation cost per byte doesn't exceed that of checksig).

----

So, what are the pros and cons?
Pros:
* Much more useful script, able to express user intents more clearly and with less trust (e.g. a user can directly encode spend size limits or vault-delays in their UTXO).
* Enabling 2nd layer protocols such as Ark, CatVM, Lightning Symmetry and more.
* Avoiding the horse trading and pork barrelling of different smaller proposals
* More efficient taproot contracts when no internal public key is needed
* (probably) Simplified off chain signature aggregation thanks to x+parity keys
Cons:
* More work due to the larger scope
* (probably) New address type will split the taproot anonymity set
* Enables some types of protocols which have historically concerned some people (e.g. hashrate escrows)

You can kinda see why this idea has many feeling very enthusiastic. Rather than fighting over whether this or that protocol is best for Ark or BitVM or Lightning, the Great Script Restoration makes them all great, and many more that we haven't even thought of yet.  All we have to do is accept those 3 fairly small (IMO) downsides (and the last one many of the other proposals had any way).

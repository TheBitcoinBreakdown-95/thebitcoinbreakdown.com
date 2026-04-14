# burakkeceli.medium.com -- Scraped Content

**URL:** https://burakkeceli.medium.com/introducing-ark-6f87ae45e272
**Category:** medium-apify
**Scrape status:** DONE
**Source notes:**
**Scraped:** 2026-04-14
**Title:** Introducing Ark. I’m excited to publicly introduce Ark… | by Brock | Medium
**Chars:** 6,134

---

Introducing Ark. I’m excited to publicly introduce Ark… | by Brock
I’m excited to publicly introduce Ark: a second-layer protocol for making cheap, anonymous, off-chain Bitcoin payments.
Press enter or click to view image in full size
Ark allows recipients to receive payments without acquiring inbound liquidity while preserving their receiver privacy. The protocol is as private as WabiSabi, as convenient as on-chain, and as cheap as Lightning. Before getting into the details, let’s talk a bit about my story.
As someone who initially started on the big-blockers side of camp, you can imagine I’ve been a big critic of Lightning myself. I have always had severe objections to Lightning, centered around inbound liquidity, async receiving, and the on-chain footprint.
Over time, the more I dig deeper into Lightning, the more I realize some of my objections are kind of addressable in the long term. For example, PTLCs solve the async receiving & proof of payment at the same time, and the shared UTXO model partially addresses the footprint issue.
However, unfortunately, I couldn’t find a “cure” for the inbound liquidity issue. Inbound liquidity always felt like a bug to me. It always felt like it simply should not exist. The entirety of it just doesn’t feel right.
Imagine doing a simple market survey before designing LN: “Hey, would you use a payment system that requires you to run a server 24h that works only if you acquire liquidity in the first place?”. Do you realize what kind of UX assumption this is?
The ideal end-user experience has to just be frictionless. If something works 95% of the time, it’s not considered to be working. Users should be able to simply push a magic button to receive sats and another button to send sats, just like how on-chain funds flow.
Anyhow, over time I came up with interesting solutions to address some of my UX concerns, which eventually led me to work on a new LN wallet:
https://twitter.com/brqgoo/status/1614040022797221888
At some point, I realized what I’m working on no longer looks like Llightning; it felt more like a distinct layer-two of its own. A layer two protocol that can pay lightning invoices and can get paid from Lightning; however, internally, at its core, is a different kind of design.
Long story short, my lightning wallet idea has evolved into a new layer two protocol. I’ve been trying to communicate this with my inner circle, collecting private feedback, and iterating on my design.
After months-long refactoring and iteration, I realized I now have the optimal design, and it felt mature enough to share with the entire community what I was working on.
Then, I made Ark public for the first time at @TheBitcoinConf https://bitcointv.com/w/pVk3bPfKZ7YqDzsNZjz9tf (Starts at 4:09:20)
Get Brock’s stories in your inbox
Join Medium for free to get updates from this writer.
Remember me for faster sign in
… and posed to the bitcoin-dev mailing list shortly after: https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2023-May/021694.html
Now back to Ark, I named it Ark because it resonated with Noah’s Ark to save plebs from chainalaysis companies and custodians. Self-custodial Lightning doesn’t work for obvious reasons, and chainalaysis companies significantly threaten user privacy.
Ark enables anonymous, scalable, off-chain payments through an untrusted intermediary called the Ark Service Provider (ASP). ASPs are always-on servers that provide liquidity to the network, similar to how Lightning service providers work.
There have been, unfortunately, some misconceptions about double-spending and the trustless nature of the protocol.
Ark is a trustless, distinct layer two protocol with unilateral exit capability. ASPs cannot steal users’ funds nor link senders & receivers. Users retain self-custody and can exit their funds to the base layer if something goes wrong on the second layer.
Ark has a utxo set that lives off the chain. These utxos are referred to as virtual utxos or vtxos in short. Existing virtual utxos are destroyed, and new virtual utxos are created on an ongoing basis, similar to how on-chain funds flow.
Ark payments settle every 5 seconds and are final in every block. Users need to wait for on-chain confirmations to consider a payment ‘final’. However, this doesn’t prevent them from paying invoices with their zero-conf coins. Ark has immediate availability with delayed finality.
Ark ensures “absolute atomicity” by using ATLCs instead of HTLCs. Users can receive payments and forward them without waiting for confirmations. A mempool-level double-spend breaks the atomicity. ASPs cannot redeem senders’ vTXOs if they double-spend recipients’ vTXOs.
Ark provides an order of magnitude greater level of privacy than Lightning. Every payment on the protocol takes place in a coinjoin round. This obfuscates the trace from the sender to the receiver. The anonymity set is everyone who involves in a payment.
Lightning payments, on the other hand, are linked through a hashlock identifier along the route. Hubs in the middle can collude to extract payment info and break the link between the sender and receiver.
Lightning also doesn’t scale in terms of on-chain footprint. Lightning is a layer two that heavily relies on the base layer to operate. Recent fee-market incidents, making key lightning infra unreliable, proved this to some extent.
Numbers tell us it would take >100 years to onboard the whole population into Lightning in a non-custodial way, assuming it takes four channels per person and an average channel opening consumes a few hundred vBytes.
You may say, okay, channels can be batched under a coinpool or a factory, but still, you have to “touch” the chain very often to close channels. Bitcoin backspace cannot handle channel closings at a scale of ~150,000 people dying daily, considering closings are TLUV-style.
Ark kind of checks all the boxes; maybe I’m just biased. It preserves receiver privacy, has no entry barrier to onboarding, and is convenient to use. Ark may in theory onboard the whole population to Bitcoin in a self-custodial way.
Feel free to check out arkpill.me for more info.

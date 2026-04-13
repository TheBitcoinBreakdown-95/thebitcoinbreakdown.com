# blog.mutinywallet.com -- Scraped Content

**URL:** https://blog.mutinywallet.com/blinded-authentication
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\Mutiny Wallet.md
**Scraped:** 2026-04-12

---

[ ](https://blog.mutinywallet.com)

[Privacy](/tag/privacy/)

# Blinded Authentication Tokens in Mutiny

Mutiny's unique privacy-preserving approach to solving lightning addresses with fedimint and blind authentication tokens.

  * [ ](/author/tony/)


#### [Tony Giorgio](/author/tony/)

May 16, 2024 • 7 min read

Mutiny has recently added Lightning Addresses to our wallet, and we wanted to spend a little time explaining the challenges, why it took so long, how we're solving them, some of the advanced privacy tech we built out for this, and some other features to come. This post will be more of a technical explainer. I encourage you to check out the [announcement post](https://blog.mutinywallet.com/federated-lightning-addresses-for-mutiny-users/) to learn more about the feature.

## Existing Lightning Addresses

[Lightning Addresses](https://blog.mutinywallet.com/federated-lightning-addresses-for-mutiny-users/) work by using an LNURL server that maps a unique username to various commands on the LNURL server. The most common one is for getting an invoice for that unique username. These are commonly used in two ways:

**Custodians** : Gets an invoice that, once paid, credits the user some bitcoin in a DB.

**Self-hosted** : The invoice is retrieved by the user's always online self-hosted node, and they receive a lightning payment directly to it.

## Problems

None of these solutions work well with non-custodial mobile lightning wallets. For LNURL to work, there has to be a server that runs all the time. Mobile phones cannot be servers, so a third party must run the server for it to work. However, the third-party LNURL server needs to be able to generate and retrieve an invoice for the mobile wallet at any time. If the mobile user does not have the app opened, they can't create an invoice on demand.

Two popular non-custodial lightning wallets have implemented their solution based on hodl invoices to work around those limitations. Blixt and Zeus users create preimages on the client side and submit the hashes of those preimages to the LNURL server. The LNURL server will create invoices locked to these preimage hashes, but without the preimage, the LNURL server cannot redeem the invoices. They require the user to come online before the lightning payment times out to create an invoice for the same payment hash, and once the LNURL server sends a payment to the user, the user will redeem the payment, revealing the preimage that the LNURL server needs to redeem the payment routed to them in the first place.

They differ slightly in implementation details but behave similarly from my perspective. As long as the LNURL server creates the invoices correctly, they cannot steal the funds from the user. However, long-standing hodl invoices cause problems for the lightning network. They can result in channel closes and locked-up liquidity for all nodes involved in the payment routing. They also require the wallet developer to route and hold all these payments, making it a more significant burden for liquidity requirements.

Since Mutiny users might not be online for extended periods, we've found an increase in closed channels as more and more users attempted to pay these hodl invoices that were redeemed while the Mutiny user was offline. If the user does not return online in time, the LSP closes the channel to redeem the funds on the chain. Hodl-invoice-related channel closes have really sucked as a user experience, so we didn't want to go down this path for our Lightning Address solution. We also are not an LSP, don't run a routing node, and don't process lightning payments, so this solution was not for us.

We needed a better way to solve this that did not strain the network or our users.

## Our solution: Federated Lightning Addresses

We've been integrating Fedimint into our wallet stack for the past ~6 months. We can do some cool things with ecash that could solve this problem with a similar trust model.

Instead of creating a hodl invoice, we can use a regular invoice from a user's configured federation. A lightning gateway for that federation will be running 24/7 to settle the payment instantly and in an atomic way. Our LNURL Address server, called [Blinded-Hermes](https://github.com/MutinyWallet/blinded-hermes?ref=blog.mutinywallet.com), will create an ecash contract that spends to a pubkey-locked ecash note. We use the user's registered pubkey for this. Once the lightning gateway processes the payment, the federation will complete the contract and provide the user with the new ecash.

Under a setup like this, neither the lightning node gateway nor the Hermes server can redeem any ecash locked to the user's pubkey. It also happens instantly without a hodl invoice locking up funds across the network. It still requires the Hermes server to set up the contract correctly, but otherwise, it is not involved in the lightning flow of funds. It doesn't require us to have a node or any liquidity. Users can use whatever federation they want and change federations anytime, further decentralizing the whole process.

## Blinded Registration

Sound cool? We're still going.

One important thing to us and our users is their financial privacy. At Mutiny, we do not process payments, lightning channels, on-chain transactions, etc.

Because of this, we know very little about our users and prefer to keep it this way. We do not want to create a honeypot that could hurt our users. However, one problem this introduces is that we now have to keep track of usernames, public keys, and which federation the username is using. For now, we have kept this feature for paying users only. So, how can we keep track of this without leaking any other information about the wallet user?

We use a blinded authentication scheme to handle this. It's very similar to how ecash works. Each paying user can check with the blind auth server to see what services it can register for. For our federated address service, each paying user can register for precisely one username throughout their lifetime. When the wallet starts up and sees that it can register, it does so instantly. It creates a secret and has the server blind-sign it. In the backend, the blind auth server will mark that it has once issued a registration token to the user, though it doesn't know the blind secret.

Consider the carbon copy envelope analogy when thinking about Blind Signatures. This explainer from [fedimint.org](https://fedimint.org/docs/CommonTerms/Blind%20Signatures?ref=blog.mutinywallet.com) summarizes it well.

Once the user has this blind token, they store it in their local database and end-to-end encrypt it to our server in case they use Mutiny on multiple devices or need to restore their wallet on a new device. We need to ensure they have this token. If they lose it, they will not have the ability to get a new one, though we do use deterministic client-side nonces that could be resigned if things go wrong. We have already built a resilient multi-device e2ee backup solution to store critical lightning and ecash data, so this was no additional effort.

When the user registers for a lightning address, the wallet checks to see if it has a blinded registration token. If so, it uses that to register their username, a new pubkey just for this service, and the federation the user has configured. No other information is needed. By simply having this token, we know they paid for Mutiny+ and have the right to register for an address. All without knowing anything else about them. Once the token is unblinded and revealed to us, we mark the unblinded message as spent in our database, ensuring that someone cannot use the same token to register another username again.

Another cool thing about this setup is that we separated the service that verifies spent tokens and the service that issues these blinded signatures. The blind auth service doesn't care if or when the address service does a registration. The address service doesn't need the private key for the blind signing. In theory, it doesn't even need to be the same actor. With this kind of tech, we could offer a blinded payment protocol for other third parties if we wanted to. Our blind auth service is designed in a way that only needs to know what service is available to what users, what plans are available, and that it has issued a blinded signature to the user.

## Other Use Cases

For now, the blind auth service supports the Blinded Hermes service we described above, but we want to use it for other things in the future.

We could build a privacy-preserving paid support ticket system with this. Anything that might mean there's more metadata the user creates, the more critical it is for us to protect that. Our support process needs to be improved, mainly around filing GitHub issues. This is very public, revealing, and cumbersome since it is outside the app.

With something like a blinded support system, we could restrict it to paying users only without knowing which user it is and without associating multiple support requests to the same user. All we care about is whether or not the user paid for support tickets at some point and the one-off pubkey they have so we can communicate securely with them. We could allow two monthly support tickets for any subscribed Mutiny+ user, possibly doing one-off paid support tickets for non-subscribers.

## Shoutout

I wanted to thank several people who helped make something like this possible.

Firstly, [OpenSats](https://opensats.org/?ref=blog.mutinywallet.com). Last year, we applied for a grant to build several new features into our open-source wallet. This federated lightning address feature has taken a while, but we're happy to say it's been a great success—better late than never or rushed too soon.

Secondly, Kody from the Fedi team built the first version of [Hermes](https://github.com/Kodylow/hermes/commits/master/?ref=blog.mutinywallet.com). We modeled ours after his and used a blinded authentication scheme instead of an invoice-based one.

Next, [Calle](https://primal.net/calle?ref=blog.mutinywallet.com) and multiple cashu teams have been experimenting similarly with pubkey-locked ecash. This led our CTO, Ben Carman, to implement this into Fedimint directly. Massive shoutout to the Fedimint team for working with us and reviewing this.

Lastly, conversations with [Gzuuus](https://primal.net/p/npub1gzuushllat7pet0ccv9yuhygvc8ldeyhrgxuwg744dn5khnpk3gs3ea5ds?ref=blog.mutinywallet.com) at [Sovereign Engineering](https://sovereignengineering.io/?ref=blog.mutinywallet.com) while he was working on similar concepts were super valuable as I was building out most of this work in Madiera.

## Conclusion

Both federated lightning addresses and our blinded authentication scheme have been a great success since we launched it last month. We're excited about what's possible with this kind of tech. We'd love to know what you think, or if there's any other application or use case, you'd be interested in with this.

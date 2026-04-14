# foundation.xyz -- Scraped Content

**URL:** https://foundation.xyz/2023/02/making-sense-of-stealth-addresses
**Category:** wayback-waf
**Scrape status:** DONE
**Source notes:** 
**Scraped:** 2026-04-13

---

*Archived version from 2025-12-14 via Wayback Machine*

Skip to main content

# Blog

## Making sense of stealth addresses

In our [previous blog post](https://foundationdevices.com/2023/01/what-we-protect/) we briefly touched on how important it is to protect the privacy of the recipient in a transaction. Today we’re going to take a closer look at a specific way to preserve privacy – “reusable payment codes”, otherwise known as “stealth addresses.” While the concept of the reusable payment code is not a new one – a form of them was officially proposed as a Bitcoin Improvement Proposal (“BIP”) in 2015 by Peter Todd – they’ve become a popular topic again after two recent proposals on new ways to implement them.

Today we’ll walk through why we need reusable payment codes, how the current approaches differ, and how you can start using them today.

### **Why do we need reusable payment codes?**

If you’ve ever had to receive Bitcoin multiple times from the same person before, you’ll know that there is a seemingly simple choice to make – do you generate a new address for them each time (and communicate it somehow), or do you tell them to re-use the same address? If you choose to generate a new address each time, you have to actively communicate somehow, send them the address, and hope they copy and paste it correctly each time. If you instead choose for them to reuse a single address, you harm the privacy of both participants in order to simplify repeat payments.

For a real-world example, consider the case of wanting to accept donations as a political dissident. If you choose to post a single static Bitcoin address, you put every donor (and yourself) at risk of trivial surveillance in order to simplify the process for you and your donors. If you choose to generate a new address for each donor, you have to run extra infrastructure like [BTCPay Server](https://btcpayserver.org/) or [SatSale](https://github.com/SatSale/SatSale), increasing the difficulty exponentially and requiring some technical know-how. We’ve even seen a recent example of this in donations raised by Russian opposition leader Alexey Navalny, easily visible to [anyone with a blockchain explorer](https://mempool.space/address/3QzYvaRFY6bakFBW4YBRrzmwzTnfZcaA6E) and actively surveilled by the Russian pro-Putin government.

The dilemma in both of these simple cases is exactly what reusable payment codes seek to solve, allowing you to provide a single static string of characters (a “code”) that can be reused as many times as necessary – even by multiple senders – without sacrificing privacy or requiring online communication with the recipient. To better understand how this type of tool presents a solution, we need to dig into each of the current proposals, including the only current live implementation of reusable payment codes, [PayNyms](https://samouraiwallet.com/paynym) (or [BIP 47](https://bips.dev/47/)).

### Where did the idea of reusable payment codes come from?

The original idea for reusable payment codes (originally called “stealth addresses”) is over a decade old at this point, originally being proposed [in 2011 on the Bitcoin Talk forums](https://bitcointalk.org/index.php?topic=5965.0) and then unofficially given a BIP number (63) in 2015 after [a proposal by Peter Todd in early 2014](https://www.mail-archive.com/bitcoin-development@lists.sourceforge.net/msg03613.html). This proposal never gained traction and was abandoned by the author when a change to Bitcoin’s OP_RETURN field broke his approach.

This original proposal shares many similarities to PayNyms, Silent Payments, and Private Payments, using a set of keys combined into one long payment code to allow senders to generate unique addresses for the recipient and leveraging the OP_RETURN. This approach is simple and relatively easy to implement, but relied on a large OP_RETURN field (something that was reduced shortly after it was proposed) and made every payment utilizing stealth addresses stand out on-chain. Even with its drawbacks, this was a major step forward and would form the foundation for future proposals.

### Reusable payment codes become a reality

The next proposal to build on the work of Peter Todd was [presented in BIP 47](https://bips.dev/47/) and ultimately became what we know today as “[PayNyms](https://samouraiwallet.com/paynym).” BIP 47 iterated on the stealth address proposal by utilizing a single notification transaction to signal to the recipient to watch for payments to a specific public key (and thus set of addresses) instead of including payment code signaling in every payment. While there are multiple versions of BIP 47, as the only one in use is version 1 we will focus on that in this post. For simplicity’s sake, for the rest of this post let’s have “Alice” represent the sender in a transaction, and “Bob” represent the recipient who is using a reusable payment code.

#### How it works

When Alice goes to send funds to Bob, her wallet uses the reusable payment code she got from Bob to generate a unique shared secret by combining (1) a private key from an output she owns, (2) the public key in Bob’s reusable payment code, and (3) a 64-byte blinding factor so that only Bob can interpret the shared secret. Alice’s wallet then converts this payment code to binary and inserts it into this notification transaction’s OP_RETURN field in order to let Bob know where to expect future payments from her. 

Both Alice and Bob have to be extremely careful not to link this notification transaction (or the inputs or outputs) with other transactions, as that could provide an on-chain link between their wallets and undo privacy gained from using BIP 47 reusable payment codes. Thankfully, current implementations in Samourai and Sparrow Wallet hide this “toxic” output associated with the notification transaction by default to protect both sender and recipient.

When Bob wants to check for received funds, he monitors his notification address, and when a transaction is received to it he (1) validates that it includes a BIP 47 payment code, (2) decrypts it with his private key, and then (3) stores the information on the set of addresses Alice can send to and watches them like any normal Bitcoin wallet. Even though this notification code is publicly visible on the blockchain, it is encrypted in such a way that only Bob can deduce the addresses it is used to generate, and thus all of Alice’s future payments are known only to Bob. Alice can now send as many payments as she would like to a unique address every time, and Bob can easily watch for new payments with both “light” wallets and “full” wallets.

[](https://mempool.space/tx/a562500b6edca8e100f40e8013361a8f7222d8d9535e215f83281b0dbd1e5b09#flow=&vout=0) [A example BIP 47 notification transaction](https://mempool.space/tx/a562500b6edca8e100f40e8013361a8f7222d8d9535e215f83281b0dbd1e5b09#flow=&vout=0), note the OP_RETURN output

#### Advantages and trade-offs

BIP 47 holds the unique status of being the only form of reusable payment code to actually be implemented and widely used thanks to the efforts of the [Samourai Wallet](https://samouraiwallet.com/) team, who have implemented BIP 47 as [“PayNyms.”](https://samouraiwallet.com/paynym) PayNyms are leveraged in Samourai Wallet, [Sparrow Wallet](https://www.sparrowwallet.com/), and [Stack Wallet](https://stackwallet.com/), allowing any user to easily share a reusable payment code or [register their PayNym with Samourai Wallet’s servers](https://paynym.is/) to get a short version of their reusable payment code like “+shrillsurf491.” This short form of their reusable payment code can then be looked up by any PayNym user on Samourai’s servers and resolved to the full payment code, allowing them to then send payments in a privacy-preserving way.

> **While BIP 47 does have the major drawback of requiring a notification transaction for funds to be easily recovered, this is outweighed by the ability for light wallets to utilize reusable payment codes and the simplicity of implementation, making it very easy for wallet developers to add support for BIP 47 reusable payment codes to their wallets.**

While BIP 47 does have the major drawback of requiring a notification transaction for funds to be easily recovered, this is outweighed by the ability for light wallets to utilize reusable payment codes and the simplicity of implementation, making it very easy for wallet developers to add support for BIP 47 reusable payment codes to their wallets. This has led to rapid growth and adoption of BIP 47 and PayNyms in a way that no other proposal has seen so far.

### **Doing away with the notification transaction via Silent Payments**

Some Bitcoin developers consider the trade-offs inherent in BIP 47 too harmful, and have sought ways to implement reusable payment codes without needing an on-chain notification transaction, but no other proposals gained interest until 2022. However, in March of 2022 Ruben Somsen proposed “[Silent Payments](https://gist.github.com/RubenSomsen/c43b79517e7cb701ebf77eec6dbb46b8),” a new approach to reusable payment codes that removes the need for a notification transaction entirely by leveraging the outputs in a transaction to signal to the recipient when funds are intended for them. Silent Payments makes use of advances in Bitcoin scanning to remove the need for a notification transaction, thereby improving scaling and privacy associated with reusable payment codes (with a key trade-off we’ll address later).

#### How it works

When Alice goes to send funds to Bob, she takes three keys and creates a unique one-time address that only Bob controls the keys to. These three keys are the (1) public key of the output(s) Alice wants to send to Bob, (2) Bob’s public key in his reusable payment code, and (3) a shared secret (generated using the same cryptography as stealth addresses and BIP 47, “[ECDH](https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman)“) that only Alice and Bob know. These three keys combine into a unique one-time address that Bob can then validate and spend from, allowing Alice to generate practically infinite addresses without any communication with Bob. This payment appears exactly like any other payment using the same script type (i.e. Taproot), thereby preventing an outside observer from even knowing Silent Payments were used at all, much less link payments to a Silent Payment address together.

When Bob wants to check for received funds, he takes (1) the private key from his payment code and (2) the aggregated key across the inputs of every transaction on-chain and checks to see if the combination matches an output in a transaction. If it matches, that output is owned by his private key and he can spend it at will, and if it doesn’t match he simply ignores that transaction and continues scanning. This process of checking every input in transactions is relatively costly and requires a full node, but does preserve privacy and remove the need for problematic notification transactions entirely. 

[](https://mempool.space/signet/tx/296d4a6e4383886d3ccca9c103c6216fd1cdebb2915b890bf6c04304c04aae8b) [An example testnet SIlent Payment transaction](https://mempool.space/signet/tx/296d4a6e4383886d3ccca9c103c6216fd1cdebb2915b890bf6c04304c04aae8b), note that it looks like any other standard Taproot transaction

#### Advantages and trade-offs

> [This] brings us to the significant trade-off of Silent Payments: because this scanning is relatively costly and can only be performed with a full Bitcoin node, Silent Payments necessarily do not work on light wallets, limiting their usage in practice.

Because with Silent Payments Bob must scan all transactions on the blockchain from the point that he generated the payment code, it brings us to the significant tradeoff of Silent Payments: because this scanning is relatively costly and can only be performed with a full Bitcoin node, Silent Payments necessarily do not work on light wallets, limiting their usage in practice.

While Silent Payments present a unique and useful set of trade-offs in comparison to BIP 47, they have not yet been implemented in any wallet and thus cannot be used by the average person. Silent Payments are particularly useful when you only want to send a single payment or donation to a given reusable payment code, as they do not require a separate notification transaction and so are cheaper and more efficient than the alternatives available today. It will be interesting to see if Silent Payments catch on, but for now you can follow the [conversation on the topic on Github](https://gist.github.com/RubenSomsen/c43b79517e7cb701ebf77eec6dbb46b8) for future developments.

#### BIP 47 with a twist: Private Payments

Last but not least, the newest kid on the block is [BIP 351](https://bips.dev/351/), or “Private Payments.” Private Payments strikes a middle ground in trade-offs between BIP 47 and Silent Payments, minimizing the potential impact and issues of a notification transaction (while still requiring one) and reducing the scanning requirements to only scanning OP_RETURNs (while still requiring a full node). Private Payments was proposed in July of 2022 by Alfred Hodler and Clark Moody, and is the latest approach to reusable payment codes.

#### How it works

When Alice goes to send funds to Bob, she takes (1) Bob’s public key encoded in his payment code and combines it with (2) a shared secret she generates to create a unique one-time address to use for a notification transaction. She then generates a unique notification code to include in the OP_RETURN of the notification transaction, creating a transaction that does not re-use a notification address (unlike BIP 47), but does stand out on-chain (unlike Silent Payments). Once she has sent this notification transaction, she can then generate a new, unique address for each subsequent payment to Bob without any links on-chain, and no direct link between any of her UTXOs and Bob’s notification address.

When Bob wants to check for received funds, he checks the OP_RETURN on every transaction since he generated his payment code for those with OP_RETURNs including a notification code that matches his private key. When he finds one that matches, he can then add all derived addresses to a watch list and monitor them for transactions just like a normal Bitcoin wallet. As this only requires checking the OP_RETURN field in each transaction instead of performing validation of every input and output, it’s necessarily much lighter on requirements than that of Silent Payments. While this still precludes the simple usage of light wallets (similar to Silent Payments), it would be easier to off-load the validation of OP_RETURNs to an external (trusted) service.

#### Advantages and trade-offs

As Private Payments requires both a notification transaction and a full node for proper scanning, it strikes something of a balance between the two other proposals without fully gaining the benefits of BIP 47’s notification transactions and the ability to use light wallets, or the scaling and privacy improvements from the omission of a notification transaction in Silent Payments. It could still pose an interesting approach for light wallets that are willing to trust an external OP_RETURN validation service, however, and gives us a great example of the continuing innovation and exploration around how we can best approach reusable payment codes.

### Using reusable payment codes today

If you’ve read through this and are wondering how you can actually use this fascinating technology today, I’ve got great news for you – BIP 47, or PayNyms, are extremely easy to use today with both Samourai Wallet and Sparrow Wallet. Both have well-implemented native support for reusable payment codes, making it extremely easy to create one (all hot wallets have one by default) and to send to a reusable payment code. For the relevant documentation on using PayNyms in both wallets, you can jump in below:

  * [PayNyms in Samourai Wallet](https://docs.samourai.io/wallet/usage#paynym-1)
  * [Paying to a PayNym in Sparrow Wallet](https://www.sparrowwallet.com/docs/spending-privately.html#paying-to-paynym)


If you’re not currently using one of these wallets, using reusable payment codes is unfortunately often not supported as it does require a bit of work for wallet developers to implement. There is, however, [ongoing work by an independent developer to implement BIP 47 PayNyms in Blue Wallet](https://abhishandy.notion.site/Implementing-BIP47-in-BlueWallet-1453f97a4c644062b0d76d1e2f1ed874), and we at Foundation are eager to implement PayNyms into [Envoy](https://foundationdevices.com/envoy/) in the future. Outside of using Samourai Wallet. Sparrow Wallet, or Stack Wallet, you can help along the growth of reusable payment codes by talking about the need on social media, following the relevant conversations and BIPs, and donating to developers and projects working on innovation and implementations along the way.

[ ← Passport version 2.0.6 is now live! ](https://foundation.xyz/2023/02/passport-version-2-0-6-is-now-live/ "Passport version 2.0.6 is now live!")

[ Privacy on Nostr → ](https://foundation.xyz/2023/03/privacy-on-nostr/ "Privacy on Nostr")

Discount Applied Successfully!

Your savings have been added to the cart.

Close

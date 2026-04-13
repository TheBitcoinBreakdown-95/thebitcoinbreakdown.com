# bitstack-app.com -- Scraped Content

**URL:** https://bitstack-app.com/en/learn-bitcoin/timestamp-overflow-will-bitcoin-stop-in-2106
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\Bitcoin's Y2K - Hard fork needed.md
**Scraped:** 2026-04-12

---

[Home](/en)[Round-Ups](/en/roundups)[Card](/en/card)[Business](/en/business)[Security](/en/security)[Learn Bitcoin](/en/learn-bitcoin)[About](/en/about)[Bitcoin price](/en/bitcoin-price)

[](/en)

Get started

Get started

[](https://www.bitstack-app.com/download)

[Learn Bitcoin](/en/learn-bitcoin)

Categories

[Home](/en/learn-bitcoin)[How Bitcoin works](/en/comprendre-bitcoin-categorie/le-fonctionnement-de-bitcoin)

# Timestamp overflow: Will Bitcoin stop in 2106?

Disponible en podcast

Share article:

If you are interested in computer science, you may have already heard of the famous bug of the year 2038, which will affect all computer systems using the Unix timestamp stored as a 32-bit signed integer. On Bitcoin, this bug will not concern us. However, Bitcoin time stamps also have a maximum value that cannot be exceeded. This threshold will be reached on February 7, 2016.

So will the year 2106 spell the death knell for Bitcoin? In this article, we take stock of this relatively unknown event with you.

## **What is the timestamp on Bitcoin?**

On the Bitcoin protocol, a blockchain is used to avoid double spending. Each transaction is placed in a block with a time frame. In other words, we put an hour and a day on each block in order to be able to put them in chronological order. This time frame is what we call a “timestamp.”

Thanks to this mechanism, when a node receives a new Bitcoin transaction waiting for confirmation, it can verify that, in the past, those same Bitcoins were not already spent. In this way, we avoid double spending on the system, without making it rely on a central authority.

The timestamp is in the header of each block. It is a 32-bit integer that is based on UNIX time. To determine this time frame, we count the number of seconds that have passed since January 1, 1970, and that gives us a whole number. For example, when I am writing this article, 1,693,498,694 seconds have passed since 1970. All I need to do is convert this integer to binary to get my timestamp. In this case, this would give us: _01100101110001100100100101011111110_. This is how you timestamp blocks on Bitcoin.

## **What is wrong with the year 2106 on Bitcoin?**

The timestamp on Bitcoin is done on unsigned 32-bit integers. This means that you can put 32 zeros or one in a row to represent time, but not one more. So there is a limit on the interpretation of time within Bitcoin. The maximum value that can be used is as follows: _1111111111111111111111111111111111_. In decimal value, this gives us 4,294,967,295 seconds, and this time corresponds to the date February 7, 2106.

After this date is exceeded, the timestamp will overflow and it will reset to zero. Computer systems using this format will interpret the current date as January 1, 1970, when in reality it will be 2106.

To better understand this phenomenon, let's draw an analogy. Some old car odometers are limited to 6 digits. As a result, the maximum value that can be displayed is 999,999 km. Once this limit is reached, the counter goes back to zero and starts counting again from the beginning. However, the kilometers already covered by the car have taken place. Therefore, there is a difference between the interpreted value and the real value, because of the number of digits that can be displayed. For the timestamp on Bitcoin, it's exactly the same principle.

If nothing is changed in the Bitcoin protocol, this discrepancy between the interpretation of the timestamp and the reality will mean that no new blocks can be published. Indeed, there are two restrictions on the timestamp of a block in order for it to be accepted by the nodes: 

  * It must be greater than the median time of the previous 11 blocks;
  * and it should be less than the median of the node timestamps plus 2 hours.


Once the 32-bit timestamp reaches its maximum value on February 7, 2106, you can still publish a maximum of 6 blocks (this is due to the fact that the low limit is a median). Then, the blockchain should stop and no more transactions could be confirmed.

Fortunately, there are many solutions to be able to bypass this date and thus prevent possible repercussions on Bitcoin.

📌 The difference between signed and unsigned 32-bit integers is in the number of bits available. The unsigned make full use of 32 bits (that's what we have on Bitcoin), while the signed reserve one bit for the sign, leaving 31 bits to represent a positive number (this is what is used on systems affected by the 2038 bug).

[**➤ Learn more about building a block on Bitcoin.**](/en/learn-bitcoin/how-to-restore-a-bitcoin-wallet)

## **How do you solve the 2106 problem?**

**Don 't worry, we have more than 80 years left to solve this small problem!** To do this, several solutions exist. The one that comes most naturally would be to change the size of the integer used to write down the timestamp on Bitcoin. We could thus use 64-bit integers, which would allow us to push the time limit to several hundred billion years in the future.

Another solution would be to keep a 32-bit timestamp, but interpreted as a 64-bit integer. Only the last 32 bits of the integer would be noted in the block header, but at each overflow, the nodes would add 2^32 to the noted value to get the real value. Overflows could be detected by nodes as soon as the 32-bit timestamp drops sharply compared to previous blocks.

However, these two solutions are hard forks. The Bitcoin community will have to agree in the next 80 years to foresee this change, before the fateful date of February 7, 2016 arrives.

[**➤ Discover the difference between a hard fork and a soft fork.**](/en/learn-bitcoin/quelle-est-la-difference-entre-un-hard-fork-et-un-soft-fork)

## **Conclusion**

In Bitcoin block headers, the timestamp is an unsigned 32-bit integer. It allows you to associate a time marker with the block. In this way, we can determine the chronological order of transactions, and thus avoid the double spending of bitcoin coins.

This timestamp will reach its maximum value on February 7, 2106 and will cause the Bitcoin blockchain to stop if nothing is done. Fortunately, this bug is not only very remote, but also very easy to fix. Full node operators will have to update the protocol via a hard fork before this deadline. The objective will be either to change the interpretation of the integer timestamp, or to extend its size to 64 bits, thus allowing Bitcoin to function for a few hundred billion more years.

**Resources:**

  * [**https://bitcoin.stackexchange.com/questions/106783/will-a-hard-fork-be-required-to-change-timestamp-fields**](https://bitcoin.stackexchange.com/questions/106783/will-a-hard-fork-be-required-to-change-timestamp-fields)
  * [**https://en.bitcoin.it/wiki/Block_timestamp**](https://en.bitcoin.it/wiki/Block_timestamp)


‍

Podcast available

# Table of contents

...

Share article

[Loïc MorelBitcoin specialist](/en/auteur/loic-morel)

[Bitcoin](/en/comprendre-bitcoin-tags/bitcoin)

[Blockchain](/en/comprendre-bitcoin-tags/blockchain)

[Consensus](/en/comprendre-bitcoin-tags/consensus)

[Protocol](/en/comprendre-bitcoin-tags/protocole)

[Fork](/en/comprendre-bitcoin-tags/fork)

[Bloc](/en/comprendre-bitcoin-tags/bloc)

[Timestamp](/en/comprendre-bitcoin-tags/horodatage)

Published on25/10/2023et mis à jour le18/9/2025

Bitstack provides its clients with articles and/or educational content on its website and application. All information is provided for informational purposes only, even if it is based on reputable and reliable sources. The articles or educational content are intended solely as general information for the reader. If you choose to invest in digital assets (Bitcoin), you must be aware of and understand the designated service and accept the associated risks.

# You may also like these articles

[](/en/learn-bitcoin/coinbase-transaction)[How Bitcoin works](/en/comprendre-bitcoin-categorie/le-fonctionnement-de-bitcoin)[Everything you need to know about the Coinbase transaction](/en/learn-bitcoin/coinbase-transaction)

[](/en/learn-bitcoin/what-is-a-bitcoin-mempool)[How Bitcoin works](/en/comprendre-bitcoin-categorie/le-fonctionnement-de-bitcoin)[What is a Mempool on Bitcoin?](/en/learn-bitcoin/what-is-a-bitcoin-mempool)

[](/en)

The #1 Bitcoin savings app.  


Product

[Roundups](/en/roundups)[Card](/en/card)[What is Bitcoin](/en/bitcoin)[Security](/en/security)[Pricing](/en/pricing)

Bitstack

[About](/en/about)[Learn Bitcoin](/en/learn-bitcoin)[Business](/en/business)[Media & Press](/en/media-press)[News](/en/news)[Careers](/en/careers)

Help

[FAQ](https://help.bitstack-app.com/en/)[Community](https://t.me/bitstack)[Contact us](/en/contact)

Language

© 2026 Bitstack

[Terms and conditions](/en/terms-and-conditions)[Privacy](/en/privacy-policy)[Legal agreements](/en/regulatory-documents-hub)

[](https://x.com/bitstack?lang=en)[](https://www.instagram.com/bitstack_app/)[](https://www.tiktok.com/@bitstack)[](https://www.linkedin.com/company/bitstack-app/mycompany/)[](https://www.youtube.com/@bitstack-app)[](https://t.me/bitstack)[](https://discord.com/invite/nWmbXJ44qu)

Bitstack Digital Assets SAS, a company registered with the Aix-en-Provence Trade and Companies Register under number 899 125 090 and operating under the trade name Bitstack, is licensed as an agent of Xpollens — an electronic money institution authorized by the ACPR (CIB 16528 – RCS Paris no. 501586341, 110 Avenue de France, 75013 Paris) — with the Autorité de Contrôle Prudentiel et de Résolution (ACPR) under number 747088, and is also licensed as a Crypto-Assets Service Provider (CASP) with the French Financial Markets Authority (AMF) under number A2025-003 for the following activities: exchange of crypto-assets for funds, exchange of crypto-assets for other crypto-assets, execution of orders for crypto-assets on behalf of clients, providing custody and administration of crypto-assets on behalf of clients, and providing transfer services for crypto-assets on behalf of clients, with its registered office located at 100 impasse des Houillères, 13590 Meyreuil, France.  
  
Investing in digital assets carries a risk of partial or total loss of the invested capital.  
Past performance is not indicative of future results.

[](https://apps.apple.com/be/app/bitstack-%C3%A9pargner-en-bitcoin/id1608783388)[](https://play.google.com/store/apps/details?id=com.bitstack.app)

Scan the QR code to download the app

Open the camera app to scan the QR code and tap the link that pops up.

DOWNLOAD BITSTACK

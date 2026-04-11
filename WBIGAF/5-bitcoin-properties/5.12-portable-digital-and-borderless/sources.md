# 5.12 Portable Digital and Borderless -- Scraped Source Content

## Metadata
- **Purpose:** Full extracted text from each scraped link, keyed by link # from `links.md`
- **Status:** 2 DONE, 0 PARTIAL, 2 FAILED, 0 SKIPPED
- **Last updated:** April 11, 2026

---

## Extracted Content
### Link #1 -- r/Bitcoin Newcomers FAQ -- borderless property

**Source:** www.reddit.com
**URL:** https://www.reddit.com/r/Bitcoin/comments/11sswss/bitcoin_newcomers_faq_please_read/
**Type:** Reddit
**Scrape status:** FAILED (HTTP 403 (Cloudflare/JS-protected))

---

*No content extracted. Reason: HTTP 403 (Cloudflare/JS-protected)*


---

### Link #2 -- "21 Ways, Ch. 0-03: Quick and Dirty" by Gigi -- mathematics quote

**Source:** 21-ways.com
**URL:** https://21-ways.com/ch0-03-quick-and-dirty/
**Type:** Blog
**Scrape status:** DONE

---

Chapter Zero - A Quick And Dirty Explanation - 21 Ways To Look At Bitcoin - 21-ways.com [ ](https://21-ways.com/)

## Chapter Zero

###  A Quick And Dirty Explanation

Your browser doesn't support HTML5 audio. Here is a [link to the audio](https://21-ways.com/assets/audio/zero.ogg) instead.

Read by [Guy Swann](https://twitter.com/TheGuySwann).

* * *

  * [](https://21-ways.com/ch0-02-introduction/ "Previous")
  * [ToC](https://21-ways.com/toc "Table of Contents")
  * [](https://21-ways.com/ch0-04-building-blocks/ "Next")


> Explanations are clear but since no one to whom a thing is explained can connect the explanations with what is really clear, therefore clear explanations are not clear.
> 
> [Gertrude Stein](https://en.wikiquote.org/wiki/Gertrude_Stein)

> Paradoxes explain everything. Since they do, they cannot be explained.
> 
> [Gene Wolfe](https://en.wikiquote.org/wiki/Gene_Wolfe)

Above all, Bitcoin is paradoxical. It is simple yet complicated, ever-changing yet unchangeable. A novel machine without any novel parts; a technological innovation that isn't really about technology. You can't touch it, yet it is hard money. You can't see it, yet it will show you a vision of the future. You can't possess it, yet thousands of people seem to be possessed by it.

All that makes Bitcoin notoriously difficult to understand - and even harder to explain. As John Oliver so succinctly quipped, "it's everything you don't understand about money combined with everything you don't understand about computers." While this is true, and while one doesn't have to necessarily understand bitcoin to use it, it helps to have a deep understanding of money and the technology that powers Bitcoin to truly appreciate the gravity of the situation. Unfortunately, even a basic understanding of Bitcoin requires some expertise in networks, markets, cryptography, game theory, mathematics, physics, computer science, and human behavior. If it were easy to understand and convey, hyperbitcoinization1 would be in the past, and we would be on a bitcoin standard2 already. As Satoshi remarked almost one year after his initial publication: "Writing a description for this thing for general audiences is bloody hard. There's nothing to relate it to."

While many people have tried to do exactly that - describe Bitcoin for general audiences - I'm not sure that such a thing is even possible. There truly is nothing to relate it to, so all metaphors, historical equivalencies, and explanatory shortcuts will miss the point in one way or another. It seems to me that the proverbial sat3 will drop for everyone  _individually_ , and without talking to you personally, I can't know what your hangups are. Maybe you think that Bitcoin has no intrinsic value, or that it can be shut down by governments, or that it will be hacked, or that it will be superseded by another technology, or that using it is unethical because of its energy consumption or illicit use. All these concerns are more or less valid at first, but, believe it or not, they fade away as your understanding of money in general—and Bitcoin in particular—increases. Alas, this understanding doesn't come easy. It seems that very few people are curious enough to put in the necessary work, which, in turn, means that most people will have to learn the hard way: they will have to deal with bitcoin out of necessity.

That being said, it is definitely possible to understand Bitcoin and the implications that its continued existence will bring about. If this weren't the case, there would be no bitcoiners, no bitcoin developers, and no individuals investing in Bitcoin's future. Everyone who was once bitten by the bitcoin bug has their own "a-ha!" moment to share, and my hope is that exploring this phenomenon from a vast array of perspectives will increase your chance of having such a moment.

Before we explore these different viewpoints in-depth, a quick and dirty explanation is in order. I will try to explain how Bitcoin works, what you can do with it, why it is important, who is behind it, what "bitcoin" is, and what its fundamental building blocks are.

### How It Works

In essence, Bitcoin is a large spreadsheet that documents who owns how much of Bitcoin's internal units:  _sats_ , short for  _satoshis_. This spreadsheet contains a record of all transactions that ever happened, in the form of "Alice sent 21 sats to Bob." To keep everyone honest, everyone gets a copy of this spreadsheet. Everyone can add entries at the bottom of it, as long as certain rules are followed. To do so, people are taking part in a kind of game, not too different from a lottery or sports competition. The odds are set up so that roughly every ten minutes, someone will win this competition, allowing them to add a batch of entries at the bottom. The spreadsheet has certain internal rules that prevent the modification of past entries. If you change these rules in a backward-incompatible way, other people will refuse to play with you, effectively kicking you from the network. It is these rules that make sure that all the accounting is done correctly, e.g., that the person who wants to send money actually has the money and that the money is sent to only one other person. In addition, these rules make sure that no money is created out of thin air, which in turn ensures that no more than 2.1 quadrillion sats (= 21 million bitcoin) will ever exist.

No single entity can change the rules because everyone on the network has to opt-in to changes voluntarily. All participants play according to their own rules. Thus, nobody is in charge of the rules. Everyone is free to participate. All you need is a computational device and an internet connection.

That's pretty much it.

If you know a thing or two about Bitcoin already, you will realize that what I called the spreadsheet is Bitcoin's (distributed) ledger, what I called batches of entries are Bitcoin's blocks, what I called a lottery is better known as mining, and what I called rules are, well, Bitcoin's consensus rules.

Granted, everything is a tiny bit more complicated than I make it out to be - it is a quick and dirty explanation, after all. However, I think that the mental framework of a large spreadsheet that everyone has a copy of is helpful. While this explanation of Bitcoin is undoubtedly imperfect, I strongly believe that the technical details of how Bitcoin works will become less relevant over time, just like the intricate details of how the internet works are irrelevant for most people today. Yes, you will have to learn some technical details to truly understand why Bitcoin is resistant to seizure and censorship, just like you have to learn some technical details to understand why the internet can't be easily shut down. However, you don't need to have a complete understanding of all the parts that make your car or your smartphone work to enjoy the benefits of using it. The same is true for Bitcoin. As with most things, the basic idea of what you can do with it is more important than how it works in detail.

### What You Can Do With It

Bitcoin is money, first and foremost. It behaves like cash, meaning that you can use it  _without asking anyone for permission_. This is true whether you want to receive it, spend it, or save it. The only thing you need to open a "Bitcoin account" is mathematics, and the only thing you need to send or receive payments is a communications channel.

As of today, this means that all you need is a smartphone and an internet connection. In principle, however, you can use any source of random information to create a Bitcoin wallet, and any communications channel to send and receive transactions. A pair of dice and a ham radio will work just as well as a smartphone and the internet, as Bitcoin enthusiasts have demonstrated in the past.4

Unfortunately, permissionless transactions and inflation-resistant savings aren't very attractive to most people. Until one is forced to understand the importance of these basic use cases, it is easy to dismiss Bitcoin as a speculative asset or mania. However, once your bank account gets frozen because you bought or sold the wrong thing, or your account gets closed because you dealt with the wrong person, or your savings get obliterated because of hyperinflation, or you are forced to flee your country and want to have your wealth intact, the question of "what can I do with bitcoin" becomes obsolete. 

As time progresses, more and more people will be forced to understand the importance of Bitcoin simply due to the trajectory of the prevailing systems. The natural end-state of fiat money is hyperinflation, and the natural end-state of centralized control is authoritarian censorship. Bitcoin is the antidote to both of these ills.

### Why It Is Important

Bitcoin radically changes our collective assumptions about what money is and who should be in control of it. The world is going digital, and it becomes more apparent every day that uncensorable and natively digital money is essential for a free society. In addition to that, Bitcoin is important because it offers an alternative to the debt-based money that the world is so addicted to. Bitcoin is independent of governments and corporations, and as its short history has shown, it is extremely resistant to subversion. This independence, combined with the unchanging nature of Bitcoin's monetary properties, makes bitcoin a valuable asset to be held by companies, individuals, and countries alike. With each passing day of Bitcoin's operation, trust in the system will increase, which will make its adoption and value increase. The earlier you will be able to understand this process, the better your position in a bitcoinized world will be.

It is worth pointing out that Bitcoin's mere survival is enough to put it on the world stage. Its incentive structure has put in motion a series of events that is best described as the ongoing  _bitcoinization_ of our world. Whether this process will be a gradual, multi-decade one, or a violent, single-digit year one is yet to be seen. I believe it will be the latter. I believe that Bitcoin's incentives are strong enough and its operation antifragile enough for it to absorb other monies and stores of value quicker than most expect. While the hyperinflations of the 21st century will happen independently of Bitcoin's existence, the economic reality that Bitcoin forces upon the rest of the world must not be underestimated. It is serendipitous that the ongoing digitization of our world coincides with the beyond-irresponsible money printing of central banks. This serendipity, combined with the exponentially increasing pace of change in our global society, is the perfect setting for what is aptly named  _hyperbitcoinization:_ a rapid, bitcoin-induced demonetization of currencies and other stores of value such as gold and real estate.

### Who Is Behind It

The short answer is: we don't know, and it doesn't matter. It doesn't matter because Bitcoin is open and mathematical in nature. Everyone can inspect it and verify that it operates as expected. Just like we do not need to know who Pythagoras was in order to understand and use the Pythagorean theorem, we do not need to know who Satoshi Nakamoto was to use and understand Bitcoin. Similarly, asking the same question in regards to fire, the wheel, the internet, and electricity might not lead to satisfying answers. All these phenomena had inventors/discoverers, but these people don't have any influence over their creation/discovery anymore.

Bitcoin was released into the wild, and soon after, [Satoshi disappeared](https://21lessons.com/5/). His gift to the world was leaving behind free and open-source software that spawns a global, public, permissionless peer-to-peer network, which in turn spawns uncensorable and natively digital money.

Bitcoin's history, where it came from, and what came before it will be the focal point of the first chapter. Bitcoin is an idea, and this idea didn't come out of nowhere. The quest for digital money is almost as old as the internet itself. It was just a matter of time until someone had the right idea and built a system that would actually work.

### What It Is

 _What is Bitcoin?_ That's the 2.1 quadrillion sats question. It is what humanity is trying to figure out - and what this book is all about. I believe that the answer to this question depends on your point of view and how you are willing to perceive it. To paraphrase Morpheus5: "Unfortunately, no one can be told what Bitcoin is. You have to see it for yourself."

It is not readily apparent what people mean when they speak of Bitcoin. Some are talking about the network, some are talking about the asset, some are talking about the industry or community around it.

I had an epiphany a couple of years ago when trying to make sense of the elusive and circular nature of Bitcoin. At least one other person6 had a similar insight: Bitcoin is not only different things to different people, but it is many things at once, and we lack precise words to talk about it meaningfully. To make matters worse, all the things that we call Bitcoin are interconnected in a circular loop. Every part influences the whole.

In short, here is what "Bitcoin" is:

  1. Bitcoin is an idea. 
  2. Bitcoin is software implementing this idea.
  3. Bitcoin is a protocol birthed by the software it represents.
  4. Bitcoin is a computer network comprised of nodes running the software.
  5. Bitcoin is an absolutely scarce asset emerging from the operation of the network.
  6. Bitcoin is a social movement comprised of individuals that are holding the asset and participating in the operation of the network.
  7. Bitcoin is a toxic, freedom-loving cult of unwavering believers; an intolerant minority from all backgrounds that will do everything in their power to defend the idea.


What follows is my attempt to break this loop apart, hoping that it helps to shine some light on this strange phenomenon. To do that, an explanation of some key concepts is in order.

  1. [Hyperbitcoinization](https://21-ways.com/terminology#hyperbitcoinization) is the final phase of the transitionary period in which humanity upgrades its monetary operating system from fiat money to bitcoin. ↩

  2. The [Bitcoin Standard](https://amzn.to/2TLl5RP) is a book written by Saifedean Ammous, describing how bitcoin could be the base of a global sound monetary standard, similarly to how the world used to be on a gold standard in the past. ↩

  3. In pre-bitcoin times, we would call this a penny. ↩

  4. This is also why [outlawing Bitcoin](https://dergigi.com/law) is a fool's errand. ↩

  5. The son of Hypnos and the god of dreams. ↩

  6. This person goes by the name of [Deep Void](https://twitter.com/deepvoid1981) and voiced his insight in [a tweet](https://archive.is/1KLeC). I explored this line of thinking in my [Circularity thread](https://archive.is/bzVcQ) and in various [discussions](https://dergigi.com/media). ↩


  * [](https://21-ways.com/ch0-02-introduction/ "Previous")
  *   * [ Chapter 0.1 ](https://21-ways.com/ch0-04-building-blocks/ "Bitcoin's Building Blocks")


* * *

### Translations

  * [ 🎧 German audio ](https://www.bitcoinaudible.de/bitcoin-kurz-gigi/) by [Rob](https://www.bitcoinaudible.de/)
  * [🔗](https://archive.ph/9t1Dk) [ Russian translation ](https://www.21ideas.org/books-21-ways-chapter-0/) by [Tony](https://twitter.com/TonyCrusoe)
  * [ 🎧 Russian audio ](https://www.youtube.com/watch?v=UI4CGxlshWY&list=PL4Iznl-WZTbCOufK6PLVLO05BO-gUg2dV&index=3) by [Tony](https://twitter.com/TonyCrusoe)


Want to help? [Add a translation](https://dergigi.com/translations)!

[All translations »](https://dergigi.com/translations)

* * *

  * [ Introduction ](https://21-ways.com/ch0-02-introduction/)
  * [Table of Contents](https://21-ways.com/toc)
  * [ Chapter 0.1 ](https://21-ways.com/ch0-04-building-blocks/ "Bitcoin's Building Blocks")


* * *

### [🧡](https://dergigi.com/support "Value4Value")

Found this valuable? 

[ Give Value Back ](https://ts.dergigi.com/api/v1/invoices?storeId=E3XrQsYCkAn5wdxsvjypSRSr1hKKSuCBK1egHamoPGuJ&orderId=21W-ch0-03&checkoutDesc=Value+for+Value%3A+Give+as+much+as+it+is+worth+to+you.&currency=USD)

Can't [support me](https://dergigi.com/support) directly?  
Consider sharing it, [translating it](https://dergigi.com/translations), or remixing it in another way.


---

### Link #3 -- "The Bullish Case for Bitcoin" -- portability section

**Source:** vijayboyapati.medium.com
**URL:** https://vijayboyapati.medium.com/the-bullish-case-for-bitcoin-6ecc8bdecc1
**Type:** Blog
**Scrape status:** FAILED (HTTP 403 (Cloudflare/JS-protected))

---

*No content extracted. Reason: HTTP 403 (Cloudflare/JS-protected)*


---

### Link #4 -- ACLU -- "Edward Snowden Explains Blockchain to His Lawyer" -- free money quote

**Source:** www.aclu.org
**URL:** https://www.aclu.org/blog/privacy-technology/internet-privacy/edward-snowden-explains-blockchain-his-lawyer-and-rest-us
**Type:** Article
**Scrape status:** DONE

---

Skip navigation

[ Back to News & Commentary ](/news/)

#  Edward Snowden Explains Blockchain to His Lawyer — and the Rest of Us 

[ Ben Wizner](https://www.aclu.org/bios/ben-wizner),  
Deputy Legal Director and Director, Center for Democracy,  
ACLU

**Share This Page**

November 20, 2018

_[This piece originally appreared in_ _[McSweeney’s new issue](https://store.mcsweeneys.net/products/mcsweeney-s-issue-54-the-end-of-trust), The End of Trust_ _, a collection featuring over 30 writers investigating surveillance, technology, and privacy, with special advisors the Electronic Frontier Foundation.]_

_Over the last five years, Edward Snowden and I have carried on an almost daily conversation, most of it unrelated to his legal troubles. Sometimes we meet in person in Moscow over vodka (me) and milkshakes (him). But our friendship has mostly taken place on secure messaging platforms, a channel that was comfortable and intuitive for him but took some getting used to for me. I learned to type with two thumbs as we discussed politics, law, and literature; family, friends, and foster dogs. Our sensibilities are similar but our worldviews quite different: I sometimes accuse him of technological solutionism; he accuses me of timid incrementalism._

_Through it all, I’ve found him to be the clearest, most patient, and least condescending explainer of technology I’ve ever met. I’ve often thought that I wished more people — or perhaps different people — could eavesdrop on our conversations. What follows is a very lightly edited transcript of one of our chats. In it, Ed attempts to explain “blockchain” to me, despite my best efforts to cling to my own ignorance._

**Ben Wizner:** The Electronic Frontier Foundation recently joked that “the amount of energy required to download tweets, articles, and instant messages which describe what ‘the blockchain’ is and how ‘decentralized’ currencies are ‘the future’ will soon eclipse the total amount of power used by the country of Denmark.” It’s true that there are a lot of “blockchain explainers” out there. And yet I’m ashamed to admit I still don’t really get it.

**Edward Snowden:** Are you asking for another math lesson? I’ve been waiting for this day. You remember what a cryptographic hash function is, right?

**BW:** This is where I’m supposed to make a joke about drugs. But no, I do not now nor will I ever remember that.

**ES:** Challenge accepted. Let’s start simpler: what do you know about these mythical blockchains?

**BW:** That I could have been rich if I’d listened to you about this four years ago? But really, I’ve heard a lot and understood little. “Decentralized.” “Ledgers.” What the hell is a blockchain?

**ES:** It’s basically just a new kind of database. Imagine updates are always added to the end of it instead of messing with the old, preexisting entries — just as you could add new links to an old chain to make it longer — and you’re on the right track. Start with that concept, and we’ll fill in the details as we go.

**BW:** Okay, but why? What is the question for which blockchain is the answer?

**ES:** In a word: trust. Imagine an old database where any entry can be changed just by typing over it and clicking save. Now imagine that entry holds your bank balance. If somebody can just arbitrarily change your balance to zero, that kind of sucks, right? Unless you’ve got student loans.

The point is that any time a system lets somebody change the history with a keystroke, you have no choice but to trust a huge number of people to be both perfectly good and competent, and humanity doesn’t have a great track record of that. Blockchains are an effort to create a history that can’t be manipulated.

**BW:** A history of what?

**ES:** Transactions. In its oldest and best-known conception, we’re talking about Bitcoin, a new form of money. But in the last few months, we’ve seen efforts to put together all kind of records in these histories. Anything that needs to be memorialized and immutable. Health-care records, for example, but also deeds and contracts.

When you think about it at its most basic technological level, a blockchain is just a fancy way of time-stamping things in a manner that you can prove to posterity hasn’t been tampered with after the fact. The very first bitcoin ever created, the “Genesis Block,” famously has one of those “general attestations” attached to it, which you can still view today.

It was a cypherpunk take on the old practice of taking a selfie with the day’s newspaper, to prove this new bitcoin blockchain hadn’t secretly been created months or years earlier (which would have let the creator give himself an unfair advantage in a kind of lottery we’ll discuss later).

**BW:** Blockchains are a history of transactions. That’s such a letdown. Because I’ve heard some extravagant claims like: blockchain is an answer to censorship. Blockchain is an answer to online platform monopolies.

**ES:** Some of that is hype cycle. Look, the reality is blockchains can theoretically be applied in many ways, but it’s important to understand that mechanically, we’re discussing a very, very simple concept, and therefore the applications are all variations on a single theme: verifiable accounting. Hot.

So, databases, remember? The concept is to bundle up little packets of data, and that can be anything. Transaction records, if we’re talking about money, but just as easily blog posts, cat pictures, download links, or even moves in the world’s most over-engineered game of chess. Then, we stamp these records in a complicated way that I’m happy to explain despite protest, but if you’re afraid of math, you can think of this as the high-tech version of a public notary. Finally, we distribute these freshly notarized records to members of the network, who verify them and update their independent copies of this new history. The purpose of this last step is basically to ensure no one person or small group can fudge the numbers, because too many people have copies of the original.

It’s this decentralization that some hope can provide a new lever to unseat today’s status quo of censorship and entrenched monopolies. Imagine that instead of today’s world, where publicly important data is often held exclusively at GenericCorp LLC, which can and does play God with it at the public’s expense, it’s in a thousand places with a hundred jurisdictions. There is no takedown mechanism or other “let’s be evil” button, and creating one requires a global consensus of, generally, at least 51 percent of the network in support of changing the rules.

mechanically, we’re discussing a very, very simple concept, and therefore the applications are all variations on a single theme: verifiable accounting. Hot.

**BW:** So even if Peter Thiel won his case and got a court order that some article about his vampire diet had to be removed, there would be no way to enforce it. Yes? That is, if _Blockchain Magazine_ republished it.

**ES:** Right — so long as _Blockchain Magazine_ is publishing to a decentralized, public blockchain, they could have a judgment ordering them to set their office on fire and it wouldn’t make a difference to the network.

**BW:** So… how does it work?

**ES:** Oh man, I was waiting for this. You’re asking for the fun stuff. Are you ready for some abstract math?

**BW:** As ready as I’ll ever be.

**ES:** Let’s pretend you’re allergic to finance, and start with the example of an imaginary blockchain of blog posts instead of going to the normal Bitcoin examples. The interesting mathematical property of blockchains, as mentioned earlier, is their general immutability a very short time past the point of initial publication.

For simplicity’s sake, think of each new article published as representing a “block” extending this blockchain. Each time you push out a new article, you are adding another link to the chain itself. Even if it’s a correction or update to an old article, it goes on the end of the chain, erasing nothing. If your chief concerns were manipulation or censorship, this means once it’s up, it’s up. It is practically impossible to remove an earlier block from the chain without also destroying every block that was created after that point and convincing everyone else in the network to agree that your alternate version of the history is the correct one.

Let’s take a second and get into the reasons for why that’s hard. So, blockchains are record-keeping backed by fancy math. Great. But what does that mean? What actually stops you from adding a new block somewhere other than the end of the chain? Or changing one of the links that’s already there?

We need to be able to crystallize the things we’re trying to account for: typically a record, a timestamp, and some sort of proof of authenticity.

So on the technical level, a blockchain works by taking the data of the new block — the next link in the chain — stamping it with the mathematic equivalent of a photograph of the block immediately preceding it and a timestamp (to establish chronological order of publication), then “hashing it all together” in a way that proves the block qualifies for addition to the chain.

**BW:** “Hashing” is a real verb?

**ES:** A cryptographic hash function is basically just a math problem that transforms any data you throw at it in a predictable way. Any time you feed a hash function a particular cat picture, you will always, always get the same number as the result. We call that result the “hash” of that picture, and feeding the cat picture into that math problem “hashing” the picture. The key concept to understand is that if you give the very same hash function a slightly different cat picture, or the same cat picture with even the tiniest modification, you will get a WILDLY different number (“hash”) as the result.

**BW:** And you can throw any kind of data into a hash function? You can hash a blog post or a financial transaction or _Moby-Dick_?

**ES:** Right. So we hash these different blocks, which, if you recall, are just glorified database updates regarding financial transactions, web links, medical records, or whatever. Each new block added to the chain is identified and validated by its hash, which was produced from data that intentionally includes the hash of the block before it. This unbroken chain leads all the way back to the very first block, which is what gives it the name.

I’m sparing you some technical nuance here, but the important concepts to understand are that blocks in the chain are meant to be verifiable, strictly ordered by chronology, and immutable. Each new block created, which in the case of Bitcoin happens every ten minutes, effectively testifies about the precise contents of all the ones that came before it, making older blocks harder and harder to change without breaking the chain completely.

So by the time our Peter Thiel catches wind of the story and decides to kill it, the chain has already built a thousand links of confirmable, published history.

Money is, of course, the best and most famous example of where blockchains have been proven to make sense.

**BW:** And this is going to… save the internet? Can you explain why some people think blockchain is a way to get around or replace huge tech platform monopolies? Like how could it weaken Amazon? Or Google?

**ES:** I think the answer there is “wishful thinking.” At least for the foreseeable future. We can’t talk Amazon without getting into currency, but I believe blockchains have a much better chance of disrupting trade than they do publication, due to their relative inefficiency.

Think about our first example of your bank balance in an old database. That kind of setup is fast, cheap, and easy, but makes you vulnerable to the failures or abuses of what engineers call a “trusted authority.” Blockchains do away with the need for trusted authorities at the expense of efficiency. Right now, the old authorities like Visa and MasterCard can process tens of thousands of transactions a second, while Bitcoin can only handle about seven. But methods of compensating for that efficiency disadvantage are being worked on, and we’ll see transaction rates for blockchains improve in the next few years to a point where they’re no longer a core concern.

**BW:** I’ve been avoiding this, because I can’t separate cryptocurrency from the image of a bunch of tech bros living in a palace in Puerto Rico as society crumbles. But it’s time for you to explain how Bitcoin works.

**ES:** Well, I hate to be the bearer of bad news, but Zuckerberg is already rich.

Money is, of course, the best and most famous example of where blockchains have been proven to make sense.

**BW:** With money, what is the problem that blockchain solves?

**ES:** The same one it solves everywhere else: trust. Without getting too abstract: what _is_ money today? A little cotton paper at best, right? But most of the time, it’s just that entry in a database. Some bank says you’ve got three hundred rupees today, and you really hope they say the same or better tomorrow.

Now think about access to that reliable bank balance — that magical number floating in the database — as something that can’t be taken for granted, but is instead transient. You’re one of the world’s unbanked people. Maybe you don’t meet the requirements to have an account. Maybe banks are unreliable where you live, or, as happened in Cyprus not too long ago, they decided to seize people’s savings to bail themselves out. Or maybe the money itself is unsound, as in Venezuela or Zimbabwe, and your balance from yesterday that could’ve bought a house isn’t worth a cup of coffee today. Monetary systems fail.

**BW:** Hang on a minute. Why is a “bitcoin” worth anything? What generates value? What backs the currency? When I own a bitcoin, what do I really own?

**ES:** Good question. What makes a little piece of green paper worth anything? If you’re not cynical enough to say “men with guns,” which are the reason legal tender is treated different from Monopoly money, you’re talking about scarcity and shared belief in the usefulness of the currency as a store of value or a means of exchange.

Let’s step outside of paper currencies, which have no fundamental value, to a more difficult case: why is gold worth so much more than its limited but real practical uses in industry? Because people generally agree it’s worth more than its practical value. That’s really it. The social belief that it’s expensive to dig out of the ground and put on a shelf, along with the expectation that others are also likely to value it, transforms a boring metal into the world’s oldest store of value.

Blockchain-based cryptocurrencies like Bitcoin have very limited fundamental value: at most, it’s a token that lets you save data into the blocks of their respective blockchains, forcing everybody participating in that blockchain to keep a copy of it for you. But the scarcity of at least some cryptocurrencies is very real: as of today, no more than twenty-one million bitcoins will ever be created, and seventeen million have already been claimed. Competition to “mine” the remaining few involves hundreds of millions of dollars’ worth of equipment and electricity, which economists like to claim are what really “backs” Bitcoin.

Yet the hard truth is that the only thing that gives cryptocurrencies value is the belief of a large population in their usefulness as a means of exchange. That belief is how cryptocurrencies move enormous amounts of money across the world electronically, without the involvement of banks, every single day. One day capital-B Bitcoin will be gone, but as long as there are people out there who want to be able to move money without banks, cryptocurrencies are likely to be valued.

**BW:** But what about you? What do you like about it?

**ES:** I like Bitcoin transactions in that they are impartial. They can’t really be stopped or reversed, without the explicit, voluntary participation by the people involved. Let’s say Bank of America doesn’t want to process a payment for someone like me. In the old financial system, they’ve got an enormous amount of clout, as do their peers, and can make that happen. If a teenager in Venezuela wants to get paid in a hard currency for a web development gig they did for someone in Paris, something prohibited by local currency controls, cryptocurrencies can make it possible. Bitcoin may not yet really be private money, but it is the first “free” money.

Bitcoin has competitors as well. One project, called Monero, tries to make transactions harder to track by playing a little shell game each time anybody spends money. A newer one by academics, called Zcash, uses novel math to enable truly private transactions. If we don’t have private transactions by default within five years, it’ll be because of law, not technology.

As with all new technologies, there will be disruption and there will be abuse. The question is whether, on balance, the impact is positive or negative. 

**BW:** So if Trump tried to cut off your livelihood by blocking banks from wiring your speaking fees, you could still get paid.

**ES:** And all he could do is tweet about it.

**BW:** The downside, I suppose, is that sometimes the ability of governments to track and block transactions is a social good. Taxes. Sanctions. Terrorist finance.

We want you to make a living. We also want sanctions against corrupt oligarchs to work.

**ES:** If you worry the rich can’t dodge their taxes without Bitcoin, I’m afraid I have some bad news. Kidding aside, this is a good point, but I think most would agree we’re far from the low-water mark of governmental power in the world today. And remember, people will generally have to convert their magic internet money into another currency in order to spend it on high-ticket items, so the government’s days of real worry are far away.

**BW:** Explore that for me. Wouldn’t the need to convert Bitcoin to cash also affect your Venezuelan teen?

**ES:** The difference is scale. When a Venezuelan teen wants to trade a month’s wages in cryptocurrency for her local currency, she doesn’t need an ID check and a bank for that. That’s a level of cash people barter with every day, particularly in developing economies. But when a corrupt oligarch wants to commission a four hundred million-dollar pleasure yacht, well, yacht builders don’t have that kind of liquidity, and the existence of invisible internet money doesn’t mean cops won’t ask how you paid for it.

The off-ramp for one is a hard requirement, but the other can opt for a footpath.

Similarly, it’s easier for governments to work collectively against “real” criminals — think bin Laden — than it is for them to crack down on dissidents like Ai Weiwei. The French would work hand in hand with the Chinese to track the activity of bin Laden’s Bitcoin wallet, but the same is hopefully not true of Ai Weiwei.

**BW:** So basically you’re saying that this won’t really help powerful bad actors all that much.

**ES:** It could actually hurt them, insofar as relying on blockchains will require them to commit evidence of their bad deeds onto computers, which, as we’ve learned in the last decade, government investigators are remarkably skilled at penetrating.

**BW:** How would you describe the downsides, if any?

**ES:** As with all new technologies, there will be disruption and there will be abuse. The question is whether, on balance, the impact is positive or negative. The biggest downside is inequality of opportunity: these are new technologies that are not that easy to use and still harder to understand. They presume access to a level of technology, infrastructure, and education that is not universally available. Think about the disruptive effect globalization has had on national economies all over the world. The winners have won by miles, not inches, with the losers harmed by the same degree. The first-mover advantage for institutional blockchain mastery wi

[... truncated at 20,000 characters ...]


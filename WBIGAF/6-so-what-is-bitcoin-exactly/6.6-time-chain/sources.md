# 6.6 Time Chain -- Scraped Source Content

## Metadata
- **Purpose:** Full extracted text from each scraped link, keyed by link # from `links.md`
- **Status:** 1 DONE, 0 PARTIAL, 0 FAILED, 0 SKIPPED
- **Last updated:** April 11, 2026

---

## Extracted Content
### Link #1 -- Dergigi: "Bitcoin Is Time" -- canonical ordering problem, centralized time-keeping, Bitcoin re-inventing time through blocks

**Source:** dergigi.com
**URL:** https://dergigi.com/2021/01/14/bitcoin-is-time/
**Type:** Article
**Scrape status:** DONE

---

Bitcoin Is Time | dergigi.com [ ](https://dergigi.com/)

## Bitcoin Is Time

[666053](https://www.blockstream.info/block-height/666053 "14 Jan 2021") 10 conversations  27 translations  [21-ways.com/2](https://21-ways.com/2 "This article is part of 21 Ways") [📖](https://read.withboris.com/a/naddr1qq8ky6t5vdhkjm3dd9ej6arfd4jsygrwg6zz9hahfftnsup23q3mnv5pdz46hpj4l2ktdpfu6rhpthhwjvpsgqqqw4rsdan6ej "Read with Boris") 🧡 

Your browser doesn't support HTML5 audio. Here is a [link to the audio](https://dergigi.com/assets/audio/bitcoin-is-time.ogg) instead.

Read by [Guy Swann](https://twitter.com/TheGuySwann).

* * *

> One luminary clock against the sky   
>  Proclaimed the time was neither wrong nor right.
> 
> Robert Frost, _Acquainted with the Night_ (1928)

> Time is still the great mystery to us. It is no more than a concept; we don’t know if it even exists…
> 
> Clifford D. Simak, _Shake­speare’s Planet_ (1976)

Time is money, or so the saying goes. It follows that money is also time: a repre­sen­ta­tion of the collec­tive economic energy stored by humanity. However, the link between time and money is more intri­cate than it might seem at first. If money requires no time to create, it doesn’t work as money very well, or not for long. More profoundly, as we shall see, keeping track of things in the infor­ma­tional realm always implies keeping track of time.

As soon as money goes digital, we have to agree on a  _defin­i­tion of time_ , and herein lies the whole problem. You might think telling the time is as easy as glancing at whatever clock is nearby, and you would be right when it comes to everyday tasks. But when it comes to synchro­nizing the state of a global, adver­sarial, distrib­uted network, telling the time becomes an almost intractable problem. How do you tell the time if clocks can’t be trusted? How do you create the concept of a singular time if your system spans the galaxy? How do you measure time in a timeless realm? And what is time anyway? 

To answer these questions, we will have to take a closer look at the concept of time itself and how Bitcoin makes up its own time: block time — more commonly known as _block height_. We will explore why the problem of timekeeping is intimately related to keeping records, why there is no absolute time in a decen­tral­ized system, and how Bitcoin uses causality and unpre­dictability to build its own sense of now. 

Timekeeping devices have trans­formed civiliza­tions more than once. As Lewis Mumford pointed out in 1934: “The clock, not the steam-engine, is the key-machine of the modern indus­trial age.” Today, it is again a timekeeping device that is trans­forming our civiliza­tion: a clock, not computers, is the true key-machine of the modern infor­ma­tional age. And this clock is Bitcoin.

## Keeping Track of Things

> Let the child learn to count things, thus getting the notion of number. These things are, for the purpose of counting, consid­ered alike, and they may be single objects or groups.
> 
> David Eugene Smith, _The Teaching of Elemen­tary Mathe­matics_ (1900)

Very broadly speaking, there are two ways to keep track of things: physical tokens and ledgers. You can either use real-world artifacts directly, e.g., give someone a sea shell, a coin, or some other tangible _thing_ , or you can repli­cate the state of the world by writing down what happened on a piece of paper. 

Imagine you are a shepherd and want to make sure that your whole flock returned home. You can put a collar on each sheep, and as soon as a sheep returns home, you simply remove the collar and hang it up in your shed. If you have one hanger for every collar, you will know that every sheep returned safely as soon as all hangers are filled. Of course, you can also count them and keep a list. However, you will have to make sure to create a new list every time you start counting, and you will also have to make sure not to count a single sheep twice (or not at all).

Money is essen­tially a tool to keep track of who owes what to whom. Broadly speaking, every­thing we have used as money up to now falls into two categories: _physical_ artifacts and _infor­ma­tional_ lists. Or, to use more common parlance: tokens and ledgers.

It is impor­tant to realize the inherent differ­ence of these categories, so let me point it out explic­itly: The first method — a physical token —  _directly_ repre­sents the state of things. The second one — a ledger —  _indirectly_ reflects the state of things. Each comes with advan­tages and disad­van­tages. For example, tokens are physical and distrib­uted; ledgers are infor­ma­tional and central­ized. Tokens are inher­ently trust­less; ledgers are not.

In the digital realm — no matter how intensely marketing gurus try to convince you of the opposite — we can only use ledgers. It is an _infor­ma­tional_ realm, not a physical one. Even if you call a certain kind of infor­ma­tion a “token,” it is still a malleable piece of infor­ma­tion, written down on a hard drive or some other medium that can hold infor­ma­tion, effec­tively rendering it an infor­ma­tional record.

The ledger-like nature of all digital infor­ma­tion is the root cause of the double-spend problem. Infor­ma­tion never repre­sents the state of the world _directly_. Further, the movement of infor­ma­tion implies copying. Infor­ma­tion exists in one place, and to “move” it, you have to copy it to another place and erase it at its origin. This problem doesn’t exist in the physical realm. In the physical realm, we can actually move things from A to B. The infor­ma­tional realm doesn’t have this property. If you want to “move” infor­ma­tion from list A to list B, you have to copy it from A to B. There is no other way.

Another way to think about it is in terms of unique­ness. Physical tokens are unique compos­ites of atoms whose assembly is not easily replic­able. Pure infor­ma­tion does not have this property. If you can read the infor­ma­tion, you can also copy it perfectly. Practi­cally speaking, it follows that physical tokens are unique, and digital tokens are not. I would even argue that “digital token” is a misnomer. A token might repre­sent secret infor­ma­tion, but it will never repre­sent unique, singular, uncopy­able infor­ma­tion.

This differ­ence in proper­ties shows that there really is no way to “hand over” infor­ma­tion. It is impos­sible to pass on a digital token like you would pass on a physical one since you can never be sure if the original owner destroyed the infor­ma­tion on his end. Digital tokens, like all infor­ma­tion, can only be spread, like an idea.

> … if you have an apple and I have an apple, and we swap apples — we each end up with only one apple. But if you and I have an idea and we swap ideas — we each end up with two ideas.
> 
> Charles F. Brannan (1949)

Physical tokens — what we call physical bearer assets, or “cash” — are free from this dilemma. In the real world, if you hand me a coin, your coin is gone. There is no magical dupli­ca­tion of the coin, and the only way to give it to me is to physi­cally hand it over. The laws of physics do not allow you to double-spend it.

While double-spending does exist in the non-digital realm — George Parker, a con artist who famously “double-spent” the Brooklyn Bridge and other landmarks comes to mind — it requires elabo­rate decep­tion and gullible buyers. Not so in the digital realm. 

In the digital realm, because we are always dealing with _infor­ma­tion,_ double-spending is an _inherent_ problem. As everyone who ever copied a file or used copy-and-paste knows, infor­ma­tion is something that you can copy _perfectly_ , and it is not bound to the medium that hosts it. If you have a digital photo­graph, for example, you can copy it a million times, store some copies on a USB stick, and send it to thousands of different people. Perfect copies are possible because infor­ma­tion allows for flawless error correc­tion, which elimi­nates degra­da­tion. And to top things off, there is virtu­ally no cost to dupli­ca­tion and no way to tell what the original was.

Again: when it comes to infor­ma­tion, copying is all there is. There simply is no way to _move_ digital infor­ma­tion from A to B. Infor­ma­tion is always _copied_ from A to B, and if the copying process was successful, the original copy of A is deleted. This is why the double-spending problem is so tricky. Absent of a central authority, there is no way to move _anything_ from A to B in a trust­less manner. You always have to trust that the original will be deleted. A natural side-effect is that, when it comes to digital infor­ma­tion, it is _impos­sible_ to tell how many copies are in existence and where these copies might be.

Because of this, using digital “tokens” as money can not and will never work. Since tokens derive their relia­bility from being hard to repro­duce as a result of their unique physical construc­tion, this advan­tage disap­pears in the digital realm. In the digital realm, tokens cannot be trusted. As a result of the nature of infor­ma­tion’s intrinsic proper­ties, the only viable format for digital money is not a token but a ledger — which brings us to the problem of time.

## Tokens Are Timeless, Ledgers Are Not

> For the things seen are tempo­rary, but the things unseen are everlasting.
> 
> Paul of Tarsus, _Corinthians_ 4:18b

When it comes to physical tokens, the time of a trans­ac­tion does not matter. You either have the coins in your pocket, or you don’t; you can either spend them, or you can’t. The simple act of posses­sion is the only prereq­ui­site for spending. The laws of nature take care of the rest. In that sense, physical tokens are trust­less and timeless.

When it comes to ledgers, physical posses­sion falls to the wayside. Whoever is in control of the ledger needs to make sure that things are _in order_. What is other­wise given by physical laws, namely that you can’t spend money that you don’t have and you can’t spend money that you have already spent previ­ously, has to be enforced by man-made rules. It is these rules that govern the orderly opera­tion and mainte­nance of a ledger, not physical laws. 

Moving from physical laws to man-made rules is the crux of the matter. Man-made rules can be bent and broken, physical laws not so much. For example, you can’t simply “make up” a physical gold coin. You have to dig it out of the ground. You can, however, absolutely make up a gold coin on paper. To do this, you simply add an entry to the ledger and give yourself a couple of coins. Or, in the case of central banks, simply add a couple trillion with a few computer keystrokes. (Fancy finan­cial people call this “Rehypoth­e­ca­tion,” “Fractional Reserve Banking,” or “Quanti­ta­tive Easing” — but don’t be fooled, it’s all the same: making up money.)

To keep ledgers and those who manip­u­late them honest, regular, indepen­dent audits are required. The ability to account for every single entry in a ledger is not a luxury. Auditors need to be able to go over the books — backward in time — to keep ledgers honest and functioning. Without reliable timestamps, verifying the internal consis­tency of a ledger is impos­sible. A mecha­nism to estab­lish an unambiguous order is essen­tial.

Without an absolute sense of time, there is no way to have a defined order of trans­ac­tion. And without a defined order of trans­ac­tions, the rules of a ledger can not be followed. How else can you make sure how much money you actually have? How else can you make sure that things are _in order_?

The distinc­tion between tokens and ledgers highlights the neces­sity for keeping track of time. In the physical realm, coins are timeless artifacts that can be exchanged without oversight. In the digital realm, coinstamping requires timestamping.

## Centralized Coinstamping

> Time: a great engraver, or eraser.
> 
> Yahia Lababidi (b. 1973)

The common way to solve the double-spending problem — the problem of making sure that a digital transfer only happens once — is to have a central list of trans­ac­tions. Once you have a central list of trans­ac­tions, you have a single ledger that can act as the sole source of truth. Solving the double-spending problem is as easy as going through the list and making sure that every­thing adds up correctly. This is how PayPal, Venmo, Alipay, and all the banks of this world — including central banks — solve the double-spending problem: via central authority.

> The problem of course is the payee can’t verify that one of the owners did not double-spend the coin. A common solution is to intro­duce a trusted central authority, or mint, that checks every trans­ac­tion for double-spending. […] The problem with this solution is that the fate of the entire money system depends on the company running the mint, with every trans­ac­tion having to go through them, just like a bank.
> 
> Satoshi Nakamoto (2009)

It is worth pointing out that Satoshi didn’t manage to make infor­ma­tion non-copyable. Every part of bitcoin — its source code, the ledger, your private key — can be copied. All of it can be dupli­cated and tampered with. However, Satoshi managed to build a system that makes rule-breaking copies completely and utterly useless. The Bitcoin network performs an intri­cate dance to decide which copies are useful and which aren’t, and it is this dance that brings scarcity into the digital realm. And like with every dance, a temporal measuring stick is required to dictate the rhythm.

Even a central­ized ledger can only solve the double-spending problem if it has a consis­tent way to keep track of time. You always need to know who gave how much to whom and, most impor­tantly: _when_. In the realm of infor­ma­tion, there is no coin-stamping without time-stamping.

> It must be stressed that the _impos­si­bility of associ­ating events with points in time_ in distrib­uted systems was the unsolved problem that precluded a decen­tral­ized ledger from ever being possible until Satoshi Nakamoto invented a solution.
> 
> Gregory Trubet­skoy (2018)

## Decentralized Time

> Time brings all things to pass.
> 
> Aeschylus (525 BC – 456 BC)

Time and order have a very intimate relation­ship. As Leslie Lamport pointed out in his 1978 paper _Time, Clocks, and the Ordering of Events in a Distrib­uted System_ : “The concept of time is funda­mental to our way of thinking. It is derived from the more basic concept of the order in which events occur.” Absent a central point of coordi­na­tion, seemingly intuitive notions of “before,” “after,” and “simul­ta­ne­ously” break down. In the words of Lamport: “the concept of ‘happening before’ defines an invariant partial ordering of the events in a distrib­uted multi­process system.”

Phrased differ­ently: Who should be in charge of time if putting someone in charge is not allowed? How can you have a reliable clock if there is no central frame of refer­ence?

You might think that solving this problem is easy because everyone could just use their own clock. This only works if every­one’s clock is accurate, and, more impor­tantly, everyone plays nice. In an adver­sarial system, relying on individual clocks would be a disaster. And, because of relativity, it does not work consis­tently across space.

As a thought exper­i­ment, imagine how you could cheat the system if everyone was in charge of keeping the time for themselves. You could pretend that the trans­ac­tion you’re sending now is actually from yesterday — it just got delayed for some reason — thus, you would still have all the money that you’ve spent today. Because of the asynchro­nous commu­ni­ca­tion that is inherent in every decen­tral­ized system, this scenario is more than a theoret­ical thought exper­i­ment. Messages do indeed get delayed, timestamps are inaccu­rate, and thanks to relativistic effects and the natural speed limit of our universe, it is anything but easy to tell apart the order of things absent of a central authority or observer.

> Who’s there? Knock knock.
> 
> An Asynchro­nous Joke

To better illus­trate the impos­si­bility of the problem, let’s look at a concrete example. Imagine that you and your business partner both have access to your company bank account. You do business all over the world, so your bank account is in Switzer­land, you are in New York, and your business partner is in Sydney. For you, it is January 3^rd^, and you are enjoying a beautiful Sunday evening at your hotel. For her, it’s Monday morning already, so she decides to buy break­fast using the debit card of your shared bank account. The cost is $27. The avail­able balance is $615. The local time is 8:21 am.

At the same time, you are about to pay for your stay with another debit card linked to the same bank account. The cost is $599. The avail­able balance is $615. The local time is 5:21 pm.

So it comes to be that — at exactly the same moment — you both swipe the card. What happens? (Dear physi­cists, please excuse my use of “the same moment” — we will ignore relativistic effects and the fact that there is no absolute time in our universe for now. We will also ignore that the concept of synchro­nous events doesn’t really exist. Bitcoin is compli­cated enough as it is!)

The central ledger at your bank will probably receive one trans­ac­tion before the other one, so one of you will be lucky, the other not so much. If the trans­ac­tions happen to arrive in the same _tick_ — let’s say in the same millisecond — the bank would have to decide who gets to spend the money.

Now, what would happen if there was no bank? Who decides who was the first one to swipe? What if it wasn’t only you two, but hundreds or even thousands of people coordi­nating? What if you didn’t trust those people? What if some of those people are trying to cheat, e.g., by setting their clocks back so that it looks like they spent the money a couple of minutes earlier?

> A time-related tool [is] needed to estab­lish a canon­ical ordering and to enforce a unique history in the absence of any central coordi­nator.
> 
> Giacomo Zucco, [_Discov­ering Bitcoin_](https://bitcoinmagazine.com/articles/discovering-bitcoin-a-brief-overview-from-cavemen-to-the-lightning-network) (2019)

This problem is _precisely_ why all previous attempts of digital cash required a central­ized registry. You always had to trust someone to correctly identify the order of things. A central­ized party was required to keep the time.

Bitcoin solves this problem by re-inventing time itself. It says no to seconds and yes to blocks.

## Keeping the Time, One Block at a Time

> Time’s glory is to calm contending kings,  
>  To unmask false­hood and bring truth to light,  
>  To stamp the seal of time in aged things,  
>  To wake the morn and sentinel the night,  
>  To wrong the wronger till he render right;
> 
> William Shake­speare, _The Rape of Lucrece_ (1594)

All clocks rely on periodic processes, something that we might call a “tick.” The familiar _tick-tock_ of a grand­fa­ther’s clock is, in essence, the same as the molec­ular-atomic buzzing of our modern Quartz and Caesium clocks. Something swings — or oscil­lates — and we simply count these swings until it adds up to a minute or a second.

For large pendulum clocks, these swings are long and easy to see. For smaller and more special­ized clocks, special equip­ment is required. The frequency of a clock — how often it ticks — depends on its use-case.

Most clocks have a fixed frequency. After all, we want to know the time _precisely_. There are, however, clocks that have a variable frequency. A metronome, for example, has a variable frequency that you can set before you make it tick. While a metronome keeps its pace constant once it is set, Bitcoin’s time varies for each tick because its internal mecha­nism is proba­bilistic. The purpose, however, is all the same: keep the music alive, so the dance can continue.

Clock| Tick Frequency  
---|---  
Grandfather’s clock| ~0.5 Hz  


[... truncated at 20,000 characters ...]


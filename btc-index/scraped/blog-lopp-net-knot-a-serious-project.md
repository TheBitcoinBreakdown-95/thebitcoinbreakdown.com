# blog.lopp.net -- Scraped Content

**URL:** https://blog.lopp.net/knot-a-serious-project
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\OP Return Arguments & Knots.md
**Scraped:** 2026-04-12

---

[ Cypherpunk Cogitations ](https://blog.lopp.net)

Sign in

Sep 23, 2025  15 min read  [bitcoin](/tag/bitcoin/)

# It's Knot a Serious Project

A comprehensive compilation of controversial actions and statements by Luke Dashjr. 

[Jameson Lopp](/author/jameson/)

The spam / filters / Knots debate has been simmering for a decade, heated up a few years ago when ordinals became a thing, and has been blazing over OP_RETURN policy changes for the past 6 months. I grow weary of repeating myself as to why this is not a particularly new concern, and the most interesting aspect (to me) is that Luke Dashjr has managed to convince a non-trivial number of people to join the cause that he's been championing for over a decade.

This post is NOT about the spam / filters debate, as those issues have been covered exhaustively by numerous people this year. Rather, this is about Luke Dashjr. Luke is quite a character, to say the least.

[https://x.com/r0ckstardev/status/1967993913597452375](https://x.com/r0ckstardev/status/1967993913597452375?ref=blog.lopp.net)

It is, indeed, a long backstory. And I think that anyone who is considering running Knots should be aware of the lead maintainer's history and reputation. Because, unlike Bitcoin Core, Knots only has a single maintainer.

The following essay is my attempt to comprehensively catalog the long list of concerning actions and statements by Luke Dashjr over the years that have resulted in him becoming far less welcome in the Bitcoin Core organization. I will also pose to you that the characteristics of a person who makes such actions and statements are not what we should desire to be embodied by the leader of an open source project.

### Luke's Security Practices

Luke has had several security failures over the years and to this day fails to implement basic security practices, which leaves many of his peers bewildered.

In late 2022 Luke's server was compromised. No big deal, that could happen to anyone, right?

[https://x.com/LukeDashjr/status/1593396689724854273](https://x.com/LukeDashjr/status/1593396689724854273?ref=blog.lopp.net)

Well, I start to raise my eyebrows when I see that binaries for Bitcoin Knots are still hosted on a server that is KNOWN to have been compromised, yet 3 YEARS later and Luke still has not rebuilt the server to ensure it's clean. This is not ignorance, it's neglectfully lazy.

[https://luke.dashjr.org/programs/bitcoin/files/bitcoin-knots/www/#download](https://luke.dashjr.org/programs/bitcoin/files/bitcoin-knots/www/?ref=blog.lopp.net#download)

Luke's own web site admits that he keeps _personal files_ on what appears to be that same, known compromised, public web server. That's a double whammy. It should be obvious why you should not put private files onto a publicly accessible machine, much less on a machine that has been compromised. Who in their right mind slaps these notices onto their web site instead of actually fixing the underlying issue?

[https://luke.dashjr.org/](https://luke.dashjr.org/?ref=blog.lopp.net)

In January 2023 Luke lost 200+ BTC due to poor security practices. From what we can tell (we have yet to hear a detailed postmortem), he wasn't even using a hardware key manager device to keep the keys permanently offline. My rough understanding is he was keeping his bitcoin wallet file in a PGP encrypted container that was on an internet connected machine, and somehow his PGP private key along with his machine were compromised, resulting in catastrophic loss.

[https://x.com/LukeDashjr/status/1609613748364509184](https://x.com/LukeDashjr/status/1609613748364509184?ref=blog.lopp.net)

This is quite unfortunate, because there also exist ways to keep your PGP key offline, such as by storing it inside of a Yubikey. To this day, Luke maintains that his keys were in "cold storage" which I doubt is accurate by anyone's definition other than Luke's.

If that was not enough, Luke sent the FBI after his fellow Bitcoin Core contributors, claiming that one of them must have accessed his laptop while at an event. From what I've been told by other people who attended Core Dev meetups, Luke would often leave his laptop unattended while at events like this, which would have provided an opportunity for a malicious person to put malware on it. At time of writing, 18 months have passed and yet no one from that group has been charged with committing the crime.

[Atlanta 2022 CoreDev Event Probed by the FBIFBI was looking for more information about Bitcoin developers who attended CoreDev Atlanta event back in October 2022 as a part of investigation into the theft of more than 200 BTC from Bitcoin developer Luke Dashjr.No Bullshit BitcoinEZ](https://www.nobsbitcoin.com/atlanta-2022-coredev-event-probed-by-the-fbi/?ref=blog.lopp.net)

It's my personal opinion that Luke's catastrophic loss was a turning point, after which he became much more vitriolic toward Bitcoin Core and now makes outrageous claims that it's compromised and trying to destroy Bitcoin. I can only imagine what being financially wiped out from such a significant sum could do to someone.

Beyond Luke's personal security practices, there are several concerns with the integrity of Knots' software development lifecycle.

Bitcoin Knots' merge process is opaque. Compare and contrast [Bitcoin Core's merged pull requests](https://github.com/bitcoin/bitcoin/pulls?q=is%3Apr+is%3Aclosed+is%3Amerged&ref=blog.lopp.net) vs [Knots merged pull requests](https://github.com/bitcoinknots/bitcoin/pulls?q=is%3Apr+is%3Aclosed+is%3Amerged&ref=blog.lopp.net). Why is this problematic? If you are actually reviewing the code changes, it's incredibly simple in the Bitcoin Core repository to find the related pull request where the changes were discussed. In Knots, it's a mystery.

Bitcoin Core commits that merge pull requests are all cryptographically signed. Knots commits are not. This is another integrity check and assurance that Knots lacks. Not only is this clear from the github web site, but you can verify yourself in the [Knots repository](https://github.com/bitcoinknots/bitcoin?ref=blog.lopp.net) via **git log --show-signature**.

Another git repository concern is that Luke just pulls the code in manually from pull requests and then commits it himself, causing anyone who wants to audit it to have to manually re-examine the Luke commit compared to the pull request code that others might have reviewed. This is getting really deep in the weeds of software development lifecycle integrity assurance, but the point is that Luke must be changing the commits in some way for them to have a different hash. While that _may only be a changed commit message or fixing merge conflicts_ , the problem is that _nobody knows_. It might be obvious to other _engineers_ that Luke could have changed something, but I doubt it's clear to the average person.

Let's go deeper with a specific example. Here is [Luke's commit ](https://github.com/bitcoinknots/bitcoin/commit/99cdb3fa41fed3e5d226a282b615a36cd47e7779?ref=blog.lopp.net)to apply the code change from Bitcoin Core [pull request #30635](https://github.com/bitcoin/bitcoin/pull/30635/files?ref=blog.lopp.net) which tweaks the parameters for a specific RPC function. We can see by putting the code diffs side by side that they are not the exact same. This is to be expected, because Knots code is not the exact same as Core.

But what are the security implications of this? Mainly, the integrity of what the original code author wrote (Sjors Provoost in this case) is completely lost, as is the work that the upstream Bitcoin Core reviewers put into ensuring that the code change was safe. In order for this fundamentally new code change that Luke is implementing to have similar security properties, it needs to go back through a robust peer review process. This is what we're talking about why we say that Knots is a dangerous "solo dev" project that does not have the necessary level of peer review. I cannnot overstate the ramifications of this weakness in the Knots software development lifecycle.

When you follow standard github practices, you have a strong chain of custody of the code, which helps ensure code integrity. Knots fails in this regard.

### Luke's Controversial Bitcoin History

In January 2012, Gavin Andresen, the lead maintainer of Bitcoin Core at the time, called out Luke as being a "poisonous person."

[https://bitcointalk.org/index.php?topic=62037.0](https://bitcointalk.org/index.php?topic=62037.0&ref=blog.lopp.net)

Gavin linked to an excellent talk on this topic that I suggest anyone involved in open source development watch:

Another long-time contributor considers Luke to be a "net negative" for development.

[https://x.com/hrdng/status/1733965811864523094](https://x.com/hrdng/status/1733965811864523094?ref=blog.lopp.net)

In 2013 Luke stated that Erik Voorhees was a criminal who should be arrested for running SatoshiDice. I think the following exchange is important to absorb because it should help your understand Luke's authoritarian tendencies, such as his belief that disobeying the State is a sin. And the cherry on top is his conclusion that Rosa Parks was sinning by not sitting in the back of the bus.

[https://www.facebook.com/rogerkver/posts/486683521377401](https://www.facebook.com/rogerkver/posts/486683521377401)

In 2014 Luke abused his position of maintainer of the Gentoo Bitcoin Core package to [enable his custom blacklist rules by default](https://bugs.gentoo.org/524512?ref=blog.lopp.net) for Gentoo users and tried to dismiss concerns as trolling.

[https://bugs.gentoo.org/524512](https://bugs.gentoo.org/524512?ref=blog.lopp.net)

He later apologized but folks felt it was halfhearted.

[https://www.reddit.com/r/Bitcoin/comments/2iuf4s/lukejrs_public_apology_for_poor_gentoo_packaging/](https://www.reddit.com/r/Bitcoin/comments/2iuf4s/lukejrs_public_apology_for_poor_gentoo_packaging/?ref=blog.lopp.net)

In 2015 Luke generated controversy by trying to redefine the term "paper wallet."

[https://www.reddit.com/r/Bitcoin/comments/2xcef5/lukejr_decides_to_rename_paper_wallet_to_paper/](https://www.reddit.com/r/Bitcoin/comments/2xcef5/lukejr_decides_to_rename_paper_wallet_to_paper/?ref=blog.lopp.net)

A month later there was more wiki controversy over Luke's pet project, "Tonal Bitcoin." Note the common theme about the difficulty people find when trying to work with Luke.

[https://www.reddit.com/r/Bitcoin/comments/2xiqwg/lets_keep_the_bitcoin_wiki_clean_remove_tonal_junk/](https://www.reddit.com/r/Bitcoin/comments/2xiqwg/lets_keep_the_bitcoin_wiki_clean_remove_tonal_junk/?ref=blog.lopp.net)

By the way, if you're not familiar with Tonal Bitcoin, it's a completely different numbering system that is base sixteen and each unit has a unique sound. Knots supports the Tonal system, presumably because Luke considers it superior to the standard base ten number system used by 99.9999% of humanity.

[https://en.bitcoin.it/wiki/Tonal_Bitcoin](https://en.bitcoin.it/wiki/Tonal_Bitcoin?ref=blog.lopp.net)

In 2021 many developers became frustrated with Luke because they felt that he was stonewalling the merge of Taproot's BIP by bikeshedding the activation parameters.

[https://github.com/bitcoin/bips/pull/1104](https://github.com/bitcoin/bips/pull/1104?ref=blog.lopp.net)

By 2024, Bitcoin developers had become sufficiently frustrated by Luke's poor leadership as BIP editor that they proposed adding more editors.

[https://groups.google.com/g/bitcoindev/c/cuMZ77KEQAA/m/vUd1mh9kAgAJ](https://groups.google.com/g/bitcoindev/c/cuMZ77KEQAA/m/vUd1mh9kAgAJ?ref=blog.lopp.net)

1 year later, this was determined to have been an appropriate change as we can see rapid improvement in progress ever since Luke has stepped aside.

[https://groups.google.com/g/bitcoindev/c/erO5zP3FgS4/m/G5Vjtu9xCAAJ](https://groups.google.com/g/bitcoindev/c/erO5zP3FgS4/m/G5Vjtu9xCAAJ?ref=blog.lopp.net)

There is also controversy around Ocean's Datum protocol which is a competitor to Stratum V2.

[https://x.com/TheBlueMatt/status/1965040061239656775](https://x.com/TheBlueMatt/status/1965040061239656775?ref=blog.lopp.net)

There is also a dispute between Luke and Bitcoin Core regarding ownership of the Transifex translation repository because apparently he was using the same source for Knots which has slightly different needs. 

[https://x.com/LukeDashjr/status/1786143344818565411](https://x.com/LukeDashjr/status/1786143344818565411?ref=blog.lopp.net)

You can dive into the details of this dispute here.

[https://x.com/glozow/status/1921986329933709575](https://x.com/glozow/status/1921986329933709575?ref=blog.lopp.net)

Knots is actually detrimental to both Lightning Network and to the Whirlpool mixing protocol.

[https://x.com/brian_trollz/status/1966947159007506475](https://x.com/brian_trollz/status/1966947159007506475?ref=blog.lopp.net)

The Whirlpool controversy seems to go back several years. When you get into Luke's personal opinions on bitcoin mixing (further down) this particular decision will make more sense.

[https://x.com/Diverter_NoKYC/status/1732337726924448102](https://x.com/Diverter_NoKYC/status/1732337726924448102?ref=blog.lopp.net)

Finally, a side note on Luke's claims about current Bitcoin Core maintainers.

[https://x.com/LukeDashjr/status/1967053162528801118](https://x.com/LukeDashjr/status/1967053162528801118?ref=blog.lopp.net)

Luke was actually "in the room" (IRC meeting) when Gloria becoming a maintainer was discussed and had no objections.

[https://www.erisian.com.au/bitcoin-core-dev/log-2022-06-30.html](https://www.erisian.com.au/bitcoin-core-dev/log-2022-06-30.html?ref=blog.lopp.net)

### Luke's Bitcoin Beliefs

Luke claims Bitcoin Knots has MORE maintainers and contributors than Bitcoin Core, which is not something any sane software engineer would claim.

[https://x.com/LukeDashjr/status/1937937554176979214](https://x.com/LukeDashjr/status/1937937554176979214?ref=blog.lopp.net)

You don't automatically inherit those attributes in a fork. And as I explained earlier, Luke's engineering practices actually break the integrity of the code changes from their original author and original reviewers. Project contributor stats are trivial to check on github; here is Knots' contributors page on github:

[https://github.com/bitcoinknots/bitcoin/graphs/contributors](https://github.com/bitcoinknots/bitcoin/graphs/contributors?ref=blog.lopp.net)

Which you can compare to [Bitcoin Core's contributors page](https://github.com/bitcoin/bitcoin/graphs/contributors?ref=blog.lopp.net)...

[https://github.com/bitcoin/bitcoin/graphs/contributors](https://github.com/bitcoin/bitcoin/graphs/contributors?ref=blog.lopp.net)

By Luke's logic, Bitcoin doesn't work since very few Bitcoiners run nodes. 

[https://x.com/LukeDashjr/status/1779804698687533266](https://x.com/LukeDashjr/status/1779804698687533266?ref=blog.lopp.net)

Luke thinks that using the bitcoin protocol in ways people don't like is a jailable offense.

[https://x.com/lopp/status/1917148830912356831](https://x.com/lopp/status/1917148830912356831?ref=blog.lopp.net)

Luke has accused me personally of threatening to rape Bitcoiners (nodes.) By his logic I am committing literal violence. I have to hand it to Luke - it is incredibly difficult to offend me. But as an ardent supporter of the Non Aggression Principle, I do find being accused of violence to be quite offensive.

[https://x.com/LukeDashjr/status/1917422311415681071](https://x.com/LukeDashjr/status/1917422311415681071?ref=blog.lopp.net)

More evidence of Luke's anti-cypherpunk authoritarian beliefs: "I would do whatever I can to help shutdown Silk Road because people shouldn't be enabled to do illegal trade."

[https://gist.github.com/AgoristRadio/5803075#file-gistfile1-txt-L137](https://gist.github.com/AgoristRadio/5803075?ref=blog.lopp.net#file-gistfile1-txt-L137)

Luke is anti-privacy when it comes to using bitcoin, because the State might not like it. This is relevant to my earlier point about Knots breaking the Whirlpool mixing protocol. He doesn't care because he thinks mixing is wrong and people shouldn't do it.

[https://web.archive.org/web/20131201203803/http://bitcoinstats.com/irc/bitcoin-dev/logs/2012/09/29](https://web.archive.org/web/20131201203803/http://bitcoinstats.com/irc/bitcoin-dev/logs/2012/09/29)

### Luke Logic

Luke has a tendency to not be in consensus with people on a variety of topics even outside of Bitcoin.

For example, he often talks about being a Roman Catholic... but he's not in consensus with what basically everybody considers to be Catholicism. Luke is a part of a tiny fork of Catholicism called [Sedevacantism](https://en.wikipedia.org/wiki/Sedevacantism?ref=blog.lopp.net). To put it in perspective, there are 1.4 billion Roman Catholics globally and about 30,000 Sedevacantists. The Sedevacantist fork of Catholicism amounts to less that 0.01% of Catholics.

[https://x.com/LukeDashjr/bio](https://x.com/LukeDashjr/bio?ref=blog.lopp.net)

What's my point here? It's that Luke clearly has no issue operating well outside of any given group's consensus. I'd say this is highly relevant to how Luke should be expected to act when it comes to Bitcoin consensus issues.

While many OG Bitcoiners are libertarians and anarchists, Luke is actually a monarchist. Yes, you read that right.

[https://x.com/LukeDashjr/status/1893436279032885531](https://x.com/LukeDashjr/status/1893436279032885531?ref=blog.lopp.net)

From his (old) Wikipedia profile we can see that he has some interesting political views.

[https://en.wikipedia.org/w/index.php?title=User:Luke-Jr&oldid=928063633](https://en.wikipedia.org/w/index.php?title=User%3ALuke-Jr&oldid=928063633&ref=blog.lopp.net)

All laws are just, nobody has the right to free speech or to use bitcoin.

[https://web.archive.org/web/20131201200415/http://bitcoinstats.com/irc/bitcoin-dev/logs/2011/12/31](https://web.archive.org/web/20131201200415/http://bitcoinstats.com/irc/bitcoin-dev/logs/2011/12/31)

Luke appears to be a geocentrist. "By the way, the Sun really orbits the Earth, not vice-versa."

[https://forums3.armagetronad.net/viewtopic.php?p=203752&sid=5fa9c3b88a382cb9b5edb5ed2aea8286#p203752](https://forums3.armagetronad.net/viewtopic.php?p=203752&sid=5fa9c3b88a382cb9b5edb5ed2aea8286&ref=blog.lopp.net#p203752)

Apparently slavery is moral if your religious doctrine and State condone it.

[https://www.reddit.com/r/DebateReligion/comments/44jj4y/i_went_to_catholic_schools_from_preschool_to/czqwmje/?context=3](https://www.reddit.com/r/DebateReligion/comments/44jj4y/i_went_to_catholic_schools_from_preschool_to/czqwmje/?context=3&ref=blog.lopp.net)

Men have the right to drag their wife around without interference from the State. 

[https://x.com/LukeDashjr/status/1597728734702108672](https://x.com/LukeDashjr/status/1597728734702108672?ref=blog.lopp.net)

If the intent is to simply prevent conception, even abstinence can be sinful within marriage.

[https://www.reddit.com/r/TrueChristian/comments/45ypf9/question_about_contraceptionbirth_control/](https://www.reddit.com/r/TrueChristian/comments/45ypf9/question_about_contraceptionbirth_control/?ref=blog.lopp.net)

Masturbation, or any sexual pleasure not ordered toward procreation, is always a grave sin.

[https://www.reddit.com/r/Christianity/comments/42guxq/is_having_remote_virtual_sex_a_sin_if_you_arent/czas8qq/?context=3](https://www.reddit.com/r/Christianity/comments/42guxq/is_having_remote_virtual_sex_a_sin_if_you_arent/czas8qq/?context=3&ref=blog.lopp.net)

Freedom of religion is bad.

[https://www.reddit.com/r/DebateACatholic/comments/30qmzg/is_sedevacantism_heretical_or_simply_schismatic/cpv06c8/](https://www.reddit.com/r/DebateACatholic/comments/30qmzg/is_sedevacantism_heretical_or_simply_schismatic/cpv06c8/?ref=blog.lopp.net)

As a general principle, it is moral for the State to execute criminals with due process, including heretics.

[https://www.reddit.com/r/DebateReligion/comments/44jj4y

[... truncated at 20,000 characters ...]

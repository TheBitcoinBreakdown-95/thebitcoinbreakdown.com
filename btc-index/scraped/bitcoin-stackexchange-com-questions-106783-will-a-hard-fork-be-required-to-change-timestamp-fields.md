# bitcoin.stackexchange.com -- Scraped Content

**URL:** https://bitcoin.stackexchange.com/questions/106783/will-a-hard-fork-be-required-to-change-timestamp-fields
**Category:** wayback-waf
**Scrape status:** DONE
**Source notes:** 
**Scraped:** 2026-04-13

---

*Archived version from 2025-12-29 via Wayback Machine*

Skip to main content

#### Stack Exchange Network

Stack Exchange network consists of 183 Q&A communities including [Stack Overflow](https://stackoverflow.com), the largest, most trusted online community for developers to learn, share their knowledge, and build their careers. 

[Visit Stack Exchange](https://stackexchange.com)

Loading…

[ ](https://bitcoin.stackexchange.com)

**Stack Internal**

Knowledge at work

Bring the best of human thought and AI automation together at your work.

[ Explore Stack Internal ](https://stackoverflow.co/internal/?utm_medium=referral&utm_source=bitcoin-community&utm_campaign=side-bar&utm_content=explore-teams-compact-popover)

# [Will a hard fork be required to change timestamp fields?](/questions/106783/will-a-hard-fork-be-required-to-change-timestamp-fields)

[ Ask Question ](/questions/ask)

Asked 4 years, 6 months ago

Modified [4 years, 3 months ago](?lastactivity "2021-09-23 13:18:55Z")

Viewed 777 times 

4 

[](/posts/106783/timeline "Show activity on this post.")

In the protocol there are multiple timestamp fields with varying lengths. For example a 4 byte unix timestamp would overflow in the year 2106. Will a hard fork be needed to deal with this issue in the coming century?

  * [blockchain-fork](/questions/tagged/blockchain-fork "show questions tagged 'blockchain-fork'")
  * [timestamp](/questions/tagged/timestamp "show questions tagged 'timestamp'")


[Share](/q/106783 "Short permalink to this question")

[Improve this question](/posts/106783/edit)

Follow 

asked Jun 3, 2021 at 19:18

[](/users/119698/chiru)

[Chiru](/users/119698/chiru)

30111 silver badge66 bronze badges


Add a comment   | 

##  1 Answer 1

Sorted by:  [ Reset to default ](/questions/106783/will-a-hard-fork-be-required-to-change-timestamp-fields?answertab=scoredesc#tab-top)

Highest score (default)  Date modified (newest first)  Date created (oldest first) 

6 

[](/posts/109797/timeline "Show activity on this post.")

There is a fairly trivial solution, which is technically a hard fork, but doesn't require changing fields.

The idea is that the timestamp is indeed treated as a 64-bit value, but only its lower 32 bits (which are then allowed to overflow) are stored in the block header. When a block's 32-bit timestamp is sufficiently much lower than the previous blocks' 32-bit timestamp, it is assumed to have overflowed, and 2^32 is added to the interpreted 64-bit timestamp.

[Share](/a/109797 "Short permalink to this answer")

[Improve this answer](/posts/109797/edit)

Follow 

answered Sep 23, 2021 at 13:18

[](/users/208/pieter-wuille)

[Pieter Wuille](/users/208/pieter-wuille)

114k1010 gold badges208208 silver badges327327 bronze badges


Add a comment   | 

##  Your Answer 

Draft saved

Draft discarded

### Sign up or [log in](/users/login?ssrc=question_page&returnurl=https%3a%2f%2fbitcoin.stackexchange.com%2fquestions%2f106783%2fwill-a-hard-fork-be-required-to-change-timestamp-fields%23new-answer)

Sign up using Google 

Sign up using Email and Password 

Submit

### Post as a guest

Name

Email

Required, but never shown

Post Your Answer  Discard 

By clicking “Post Your Answer”, you agree to our [terms of service](https://stackoverflow.com/legal/terms-of-service/public) and acknowledge you have read our [privacy policy](https://stackoverflow.com/legal/privacy-policy).

Start asking to get answers

Find the answer to your question by asking.

[Ask question](/questions/ask)

Explore related questions

  * [blockchain-fork](/questions/tagged/blockchain-fork "show questions tagged 'blockchain-fork'")
  * [timestamp](/questions/tagged/timestamp "show questions tagged 'timestamp'")


See similar questions with these tags.

  * The Overflow Blog 
  * [Containers are easy—moving your legacy system off your VM is not](https://stackoverflow.blog/2025/12/26/containers-are-easy-moving-your-legacy-system-off-your-vm-is-not/)

  * [AI vs Gen Z: How AI has changed the career pathway for junior developers](https://stackoverflow.blog/2025/12/26/ai-vs-gen-z/)

  * Featured on Meta 
  * [Native Ads coming soon to Stack Overflow and Stack Exchange](https://meta.stackexchange.com/questions/415259/native-ads-coming-soon-to-stack-overflow-and-stack-exchange)

  * [A proposal for bringing back Community Promotion & Open Source Ads](https://meta.stackexchange.com/questions/416429/a-proposal-for-bringing-back-community-promotion-open-source-ads)


#### Linked

[ 1 ](/questions/116777/does-bitcoin-need-future-consensus-change-upgrades-or-could-a-billion-people-use "Question score \(upvotes - downvotes\)") [Does Bitcoin need future consensus change upgrades or could a billion people use Bitcoin today?](/questions/116777/does-bitcoin-need-future-consensus-change-upgrades-or-could-a-billion-people-use?noredirect=1)

[ 0 ](/questions/113357/softening-the-2106-hard-fork "Question score \(upvotes - downvotes\)") [Softening the 2106 hard fork](/questions/113357/softening-the-2106-hard-fork?noredirect=1)

#### Related

[ 18 ](/questions/36090/has-a-hard-fork-ever-occurred "Question score \(upvotes - downvotes\)") [Has a hard fork ever occurred?](/questions/36090/has-a-hard-fork-ever-occurred)

[ 3 ](/questions/36726/do-new-sighash-types-need-a-hard-fork-or-a-soft-fork "Question score \(upvotes - downvotes\)") [Do new SIGHASH types need a hard fork or a soft fork?](/questions/36726/do-new-sighash-types-need-a-hard-fork-or-a-soft-fork)

[ 7 ](/questions/50665/does-my-bitcoin-multiply-with-every-fork "Question score \(upvotes - downvotes\)") [Does my bitcoin multiply with every fork?](/questions/50665/does-my-bitcoin-multiply-with-every-fork)

[ 11 ](/questions/52210/what-is-the-best-way-to-prevent-replay-attacks-in-the-event-of-a-bitcoin-hard-fo "Question score \(upvotes - downvotes\)") [What is the best way to prevent replay attacks in the event of a bitcoin hard fork?](/questions/52210/what-is-the-best-way-to-prevent-replay-attacks-in-the-event-of-a-bitcoin-hard-fo)

[ 7 ](/questions/52275/at-what-point-does-a-hard-fork-occur "Question score \(upvotes - downvotes\)") [At what point does a hard fork occur?](/questions/52275/at-what-point-does-a-hard-fork-occur)

[ 8 ](/questions/56661/what-happens-to-my-bitcoins-if-a-hard-fork-occurs "Question score \(upvotes - downvotes\)") [What happens to my bitcoins if a hard fork occurs?](/questions/56661/what-happens-to-my-bitcoins-if-a-hard-fork-occurs)

[ 3 ](/questions/57260/what-happens-to-bitcoin-transactions-that-are-unconfirmed-during-the-hard-fork "Question score \(upvotes - downvotes\)") [What happens to bitcoin transactions that are unconfirmed during the hard fork?](/questions/57260/what-happens-to-bitcoin-transactions-that-are-unconfirmed-during-the-hard-fork)

[ 9 ](/questions/79182/january-19th-2038-rip-unix-timestamps "Question score \(upvotes - downvotes\)") [January 19th, 2038: RIP Unix Timestamps](/questions/79182/january-19th-2038-rip-unix-timestamps)

[ 0 ](/questions/113357/softening-the-2106-hard-fork "Question score \(upvotes - downvotes\)") [Softening the 2106 hard fork](/questions/113357/softening-the-2106-hard-fork)

####  [ Hot Network Questions ](https://stackexchange.com/questions?tab=hot)

  * [ Has Swami Vivekananda refuted the Western claim that the Rig Veda is henotheistic? ](https://hinduism.stackexchange.com/questions/69256/has-swami-vivekananda-refuted-the-western-claim-that-the-rig-veda-is-henotheisti)
  * [ K-theoretical interpretation of Witt vectors ](https://mathoverflow.net/questions/506394/k-theoretical-interpretation-of-witt-vectors)
  * [ Position where a player can either force mate or selfmate ](https://puzzling.stackexchange.com/questions/136464/position-where-a-player-can-either-force-mate-or-selfmate)
  * [ How do I prevent 'docker run...' from creating anonymous volumes? ](https://unix.stackexchange.com/questions/803357/how-do-i-prevent-docker-run-from-creating-anonymous-volumes)
  * [ Where are some places that I can stay for a night in Turku? ](https://travel.stackexchange.com/questions/202897/where-are-some-places-that-i-can-stay-for-a-night-in-turku)
  * [ What is the significance of the red thread in Wake Up Dead Man? ](https://movies.stackexchange.com/questions/131185/what-is-the-significance-of-the-red-thread-in-wake-up-dead-man)
  * [ Why doesn't the HDMI port on an HP EliteBook Ultra G1i work as an output port? ](https://superuser.com/questions/1932963/why-doesnt-the-hdmi-port-on-an-hp-elitebook-ultra-g1i-work-as-an-output-port)
  * [ Why is Blessed Virgin Mary anonymous in the latter half of Mtt 2? ](https://hermeneutics.stackexchange.com/questions/113464/why-is-blessed-virgin-mary-anonymous-in-the-latter-half-of-mtt-2)
  * [ What could be the reason for error 500 after adding IP networks to Require Not IP? ](https://webmasters.stackexchange.com/questions/148421/what-could-be-the-reason-for-error-500-after-adding-ip-networks-to-require-not-i)
  * [ What is the benefit of letting an in-progress espagnole sauce rest overnight? ](https://cooking.stackexchange.com/questions/136581/what-is-the-benefit-of-letting-an-in-progress-espagnole-sauce-rest-overnight)
  * [ Solution of definite integral equations ](https://math.stackexchange.com/questions/5116999/solution-of-definite-integral-equations)
  * [ Self Connection in CDG from Terminal 1 to Terminal 2B with less than 3 hours ](https://travel.stackexchange.com/questions/202928/self-connection-in-cdg-from-terminal-1-to-terminal-2b-with-less-than-3-hours)
  * [ Li-ion charger TP4056 protections ](https://electronics.stackexchange.com/questions/763658/li-ion-charger-tp4056-protections)
  * [ GEE script annual Landsat 5/7/8/9 composites ](https://codereview.stackexchange.com/questions/300870/gee-script-annual-landsat-5-7-8-9-composites)
  * [ Is it philosophically coherent to treat memetic propagation as part of cognitive architecture rather than merely cultural transmission? ](https://philosophy.stackexchange.com/questions/134802/is-it-philosophically-coherent-to-treat-memetic-propagation-as-part-of-cognitive)
  * [ What materials should I use in my DIY car seat heater (80 W)? ](https://engineering.stackexchange.com/questions/65153/what-materials-should-i-use-in-my-diy-car-seat-heater-80-w)
  * [ Is the Canonical Decomposition of Functions Canonical? ](https://math.stackexchange.com/questions/5116989/is-the-canonical-decomposition-of-functions-canonical)
  * [ How can I get the Korg Pa5X to play a bass guitar voice when I press a key on the keyboard? ](https://music.stackexchange.com/questions/142921/how-can-i-get-the-korg-pa5x-to-play-a-bass-guitar-voice-when-i-press-a-key-on-th)
  * [ Derivation in the sense of distributions ](https://mathoverflow.net/questions/506404/derivation-in-the-sense-of-distributions)
  * [ MS-DOS 4.0 MZ executable specification ](https://retrocomputing.stackexchange.com/questions/32361/ms-dos-4-0-mz-executable-specification)
  * [ How to quickly break Geo Traveller's Starblade? ](https://gaming.stackexchange.com/questions/417466/how-to-quickly-break-geo-travellers-starblade)
  * [ Why does my internal laptop screen (Lenovo IdeaPad Slim 5i) stay black and only works with an external monitor? ](https://superuser.com/questions/1932914/why-does-my-internal-laptop-screen-lenovo-ideapad-slim-5i-stay-black-and-only)
  * [ When and how was I supposed to do customs when traveling from Frankfurt to Beijing to Zhengzhou? ](https://travel.stackexchange.com/questions/202911/when-and-how-was-i-supposed-to-do-customs-when-traveling-from-frankfurt-to-beiji)
  * [ FunctionDomain of Hold Piecewise function ](https://mathematica.stackexchange.com/questions/318355/functiondomain-of-hold-piecewise-function)

more hot questions 

[ Question feed ](/feeds/question/106783 "Feed of this question and its answers")

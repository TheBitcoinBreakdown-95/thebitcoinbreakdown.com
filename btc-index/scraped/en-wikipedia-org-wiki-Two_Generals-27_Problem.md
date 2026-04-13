# en.wikipedia.org -- Scraped Content

**URL:** https://en.wikipedia.org/wiki/Two_Generals%27_Problem
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\Double Spend problemByzantine Generals problem.md
**Scraped:** 2026-04-12

---

Jump to content

[ ](/wiki/Main_Page)

[ Search ](/wiki/Special:Search "Search Wikipedia \[alt-f\]")

Search


  * [ Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
  * [Create account](/w/index.php?title=Special:CreateAccount&returnto=Two+Generals%27+Problem "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](/w/index.php?title=Special:UserLogin&returnto=Two+Generals%27+Problem "You're encouraged to log in; however, it's not mandatory. \[alt-o\]")


Personal tools

  * [ Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
  * [ Create account](/w/index.php?title=Special:CreateAccount&returnto=Two+Generals%27+Problem "You are encouraged to create an account and log in; however, it is not mandatory")
  * [ Log in](/w/index.php?title=Special:UserLogin&returnto=Two+Generals%27+Problem "You're encouraged to log in; however, it's not mandatory. \[alt-o\]")


# Two Generals' Problem

14 languages

  * [العربية](https://ar.wikipedia.org/wiki/%D9%85%D8%B9%D8%B6%D9%84%D8%A9_%D8%A7%D9%84%D8%AC%D9%86%D8%B1%D8%A7%D9%84%D9%8A%D9%86 "معضلة الجنرالين – Arabic")
  * [Čeština](https://cs.wikipedia.org/wiki/Probl%C3%A9m_dvou_arm%C3%A1d "Problém dvou armád – Czech")
  * [Español](https://es.wikipedia.org/wiki/Problema_de_los_dos_generales "Problema de los dos generales – Spanish")
  * [فارسی](https://fa.wikipedia.org/wiki/%D9%85%D8%B3%D8%A6%D9%84%D9%87_%D8%AF%D9%88_%DA%98%D9%86%D8%B1%D8%A7%D9%84 "مسئله دو ژنرال – Persian")
  * [Suomi](https://fi.wikipedia.org/wiki/Kahden_kenraalin_ongelma "Kahden kenraalin ongelma – Finnish")
  * [Français](https://fr.wikipedia.org/wiki/Probl%C3%A8me_des_deux_g%C3%A9n%C3%A9raux "Problème des deux généraux – French")
  * [עברית](https://he.wikipedia.org/wiki/%D7%91%D7%A2%D7%99%D7%99%D7%AA_%D7%A9%D7%A0%D7%99_%D7%94%D7%A6%D7%91%D7%90%D7%95%D7%AA "בעיית שני הצבאות – Hebrew")
  * [日本語](https://ja.wikipedia.org/wiki/%E4%BA%8C%E4%BA%BA%E3%81%AE%E5%B0%86%E8%BB%8D%E5%95%8F%E9%A1%8C "二人の将軍問題 – Japanese")
  * [한국어](https://ko.wikipedia.org/wiki/%EB%91%90_%EC%9E%A5%EA%B5%B0_%EB%AC%B8%EC%A0%9C "두 장군 문제 – Korean")
  * [Lombard](https://lmo.wikipedia.org/wiki/Problema_di_du_generai "Problema di du generai – Lombard")
  * [Português](https://pt.wikipedia.org/wiki/Problema_dos_dois_generais "Problema dos dois generais – Portuguese")
  * [Русский](https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0_%D0%B4%D0%B2%D1%83%D1%85_%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D0%BB%D0%BE%D0%B2 "Задача двух генералов – Russian")
  * [Українська](https://uk.wikipedia.org/wiki/%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0_%D0%B4%D0%B2%D0%BE%D1%85_%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D0%BB%D1%96%D0%B2 "Задача двох генералів – Ukrainian")
  * [中文](https://zh.wikipedia.org/wiki/%E4%B8%A4%E5%86%9B%E9%97%AE%E9%A2%98 "两军问题 – Chinese")


[Edit links](https://www.wikidata.org/wiki/Special:EntityPage/Q2632674#sitelinks-wikipedia "Edit interlanguage links")

From Wikipedia, the free encyclopedia

Thought experiment

[](/wiki/File:Two_Generals%27_Problem.svg)Positions of the armies. Armies A1 and A2 cannot see one another directly, so need to communicate by messengers, but their messengers may be captured by army B.

In computing, the **Two Generals' Problem** (or **Chinese Generals Problem**[1]) is a [thought experiment](/wiki/Thought_experiment "Thought experiment") meant to illustrate the pitfalls and design challenges of attempting to coordinate an action by communicating over an unreliable link. In the experiment, two generals are only able to communicate with one another by sending a messenger through enemy territory. The experiment asks how they might reach an agreement on the time to launch an attack, while knowing that any messenger they send could be captured. 

The Two Generals' Problem appears often as an introduction to the more general [Byzantine Generals](/wiki/Byzantine_Generals "Byzantine Generals") problem in introductory classes about [computer networking](/wiki/Computer_networking "Computer networking") (particularly with regard to the [Transmission Control Protocol](/wiki/Transmission_Control_Protocol "Transmission Control Protocol"), where it shows that TCP cannot guarantee state consistency between endpoints and why this is the case), though it applies to any type of two-party communication where failures of communication are possible. A key concept in [epistemic logic](/wiki/Epistemic_logic "Epistemic logic"), this problem highlights the importance of [common knowledge](/wiki/Common_knowledge_\(logic\) "Common knowledge \(logic\)"). Some authors also refer to this as the **Two Generals' Paradox** , the **Two Armies Problem** , or the **Coordinated Attack Problem**.[2][3] The Two Generals' Problem was the first computer communication problem to be proven to be unsolvable.[4] An important consequence of this proof is that generalizations such as the Byzantine Generals problem are also unsolvable in the face of arbitrary communication failures, thus providing a base of realistic expectations for any distributed consistency protocols. 

## Definition

[[edit](/w/index.php?title=Two_Generals%27_Problem&action=edit&section=1 "Edit section: Definition")]

Two [armies](/wiki/Army "Army"), each led by a different [general](/wiki/General "General"), are preparing to attack a fortified city. The armies are encamped near the city, each in its own valley. A third valley separates the two hills, and the only way for the two generals to communicate is by sending [messengers](/wiki/Runner_\(war\) "Runner \(war\)") through the valley. Unfortunately, the valley is occupied by the city's defenders and there is a chance that any given messenger sent through the valley will be captured.[5]

While the two generals have agreed that they will attack, they haven't agreed upon a time for an attack. It is required that the two generals have their armies attack the city simultaneously to succeed, lest the lone attacker army die trying. They must thus communicate with each other to decide on a time to attack and to agree to attack at that time, and each general must know that the other general knows that they have agreed to the attack plan. Because [acknowledgement of message receipt](/wiki/Acknowledgement_\(data_networks\) "Acknowledgement \(data networks\)") can be lost as easily as the original message, a potentially infinite series of messages is required to come to [consensus](/wiki/Consensus_\(computer_science\) "Consensus \(computer science\)").[6]

The thought experiment involves considering how they might go about coming to a consensus. In its simplest form, one general is known to be the leader, decides on the time of the attack, and must communicate this time to the other general. The problem is to come up with algorithms that the generals can use, including sending messages and processing received messages, that can allow them to correctly conclude: 

Yes, we will both attack at the agreed-upon time.

Allowing that it is quite simple for the generals to come to an agreement on the time to attack (i.e. one successful message with a successful acknowledgement), the subtlety of the Two Generals' Problem is in the impossibility of designing algorithms for the generals to use to safely agree to the above statement.[_[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")_]

## Illustrating the problem

[[edit](/w/index.php?title=Two_Generals%27_Problem&action=edit&section=2 "Edit section: Illustrating the problem")]

The first general may start by sending a message: "Attack at 0900 on August 4." However, once dispatched, the first general has no idea whether or not the messenger got through. This uncertainty may lead the first general to hesitate to attack due to the risk of being the sole attacker. 

To be sure, the second general may send a confirmation back to the first: "I received your message and will attack at 0900 on August 4." However, the messenger carrying the confirmation could face capture, and the second general may hesitate, knowing that the first might hold back without the confirmation. 

Further confirmations may seem like a solution—let the first general send a second confirmation: "I received your confirmation of the planned attack at 0900 on August 4." However, this new messenger from the first general is liable to be captured, too. Thus, it quickly becomes evident that no matter how many rounds of confirmation are made, there is no way to guarantee the second requirement that each general is sure the other has agreed to the attack plan. Both generals will always be left wondering whether their last messenger got through.[7]

## Proof

[[edit](/w/index.php?title=Two_Generals%27_Problem&action=edit&section=3 "Edit section: Proof")]

[](/wiki/File:Question_book-new.svg)| This section **does not[cite](/wiki/Wikipedia:Citing_sources "Wikipedia:Citing sources") any [sources](/wiki/Wikipedia:Verifiability "Wikipedia:Verifiability")**. Please help [improve this section](/wiki/Special:EditPage/Two_Generals%27_Problem "Special:EditPage/Two Generals' Problem") by [adding citations to reliable sources](/wiki/Help:Referencing_for_beginners "Help:Referencing for beginners"). Unsourced material may be challenged and [removed](/wiki/Wikipedia:Verifiability#Burden_of_evidence "Wikipedia:Verifiability"). _( November 2019)__([Learn how and when to remove this message](/wiki/Help:Maintenance_template_removal "Help:Maintenance template removal"))_  
---|---  
  
Because this protocol is [deterministic](/wiki/Deterministic_system "Deterministic system"), suppose there is a sequence of a fixed number of messages, one or more successfully delivered and one or more not. The assumption is that there should be a _shared certainty for both generals to attack_. Consider the last such message that was successfully delivered. If that last message had not been successfully delivered, then one general at least (presumably the receiver) would decide not to attack. From the viewpoint of the sender of that last message, however, the sequence of messages sent and delivered is exactly the same as it would have been, had that message been delivered. Since the protocol is deterministic, the general sending that last message will still decide to attack. We've now created a situation where the suggested protocol leads one general to attack and the other not to attack—contradicting the assumption that the protocol was a solution to the problem. 

A non-deterministic protocol with a potentially variable message count can be compared to an edge-labeled finite [tree](/wiki/Tree_\(graph_theory\) "Tree \(graph theory\)"), where each node in the tree represents an explored example up to a specified point. A protocol that terminates before sending any messages is represented by a tree containing only a root node. The edges from a node to each child are labeled with the messages sent in order to reach the child state. Leaf nodes represent points at which the protocol terminates. Suppose there exists a non-deterministic protocol _P_ which solves the Two Generals' Problem. Then, by a similar argument to the one used for fixed-length deterministic protocols above, _P'_ must also solve the Two Generals' Problem, where the tree representing _P'_ is obtained from that for _P_ by removing all leaf nodes and the edges leading to them. Since _P_ is finite, it then follows that the protocol that terminates before sending any messages would solve the problem. But clearly, it does not. Therefore, a non-deterministic protocol that solves the problem cannot exist. 

## Engineering approaches

[[edit](/w/index.php?title=Two_Generals%27_Problem&action=edit&section=4 "Edit section: Engineering approaches")]

[](/wiki/File:Question_book-new.svg)| This section **does not[cite](/wiki/Wikipedia:Citing_sources "Wikipedia:Citing sources") any [sources](/wiki/Wikipedia:Verifiability "Wikipedia:Verifiability")**. Please help [improve this section](/wiki/Special:EditPage/Two_Generals%27_Problem "Special:EditPage/Two Generals' Problem") by [adding citations to reliable sources](/wiki/Help:Referencing_for_beginners "Help:Referencing for beginners"). Unsourced material may be challenged and [removed](/wiki/Wikipedia:Verifiability#Burden_of_evidence "Wikipedia:Verifiability"). _( November 2019)__([Learn how and when to remove this message](/wiki/Help:Maintenance_template_removal "Help:Maintenance template removal"))_  
---|---  
  
A pragmatic approach to dealing with the Two Generals' Problem is to use schemes that accept the [uncertainty](/wiki/Uncertainty "Uncertainty") of the [communications](/wiki/Communication "Communication") channel and not attempt to eliminate it, but rather mitigate it to an acceptable degree. For example, the first general could send 100 messengers, anticipating that the probability of all being captured is low. With this approach, the first general will attack no matter what, and the second general will attack if any message is received. Alternatively, the first general could send a stream of messages and the second general could send acknowledgments to each, with each general feeling more comfortable with every message received. As seen in the proof, however, neither can be certain that the attack will be coordinated. There is no algorithm that they can use (e.g. attack if more than four messages are received) that will be certain to prevent one from attacking without the other. Also, the first general can send a marking on each message saying it is message 1, 2, 3 ... of n. This method will allow the second general to know how reliable the channel is and send an appropriate number of messages back to ensure a high probability of at least one message being received. If the channel can be made to be reliable, then one message will suffice and additional messages do not help. The last is as likely to get lost as the first. 

Assuming that the generals must sacrifice lives every time a messenger is sent and intercepted, an algorithm can be designed to minimize the number of messengers required to achieve the maximum amount of confidence the attack is coordinated. To save them from sacrificing hundreds of lives to achieve very high confidence in coordination, the generals could agree to use the absence of messengers as an indication that the general who began the transaction has received at least one confirmation and has promised to attack. Suppose it takes a messenger 1 minute to cross the danger zone, allowing 200 minutes of silence to occur after confirmations have been received will allow us to achieve extremely high confidence while not sacrificing messenger lives. In this case, messengers are used only in the case where a party has not received the attack time. At the end of 200 minutes, each general can reason: "I have not received an additional message for 200 minutes; either 200 messengers failed to cross the danger zone, or it means the other general has confirmed and committed to the attack and has confidence I will too". 

## History

[[edit](/w/index.php?title=Two_Generals%27_Problem&action=edit&section=5 "Edit section: History")]

The Two Generals' Problem and its impossibility proof was first published by E. A. Akkoyunlu, K. Ekanadham, and R. V. Huber in 1975 in "Some Constraints and Trade-offs in the Design of Network Communications",[8] where it is described starting on page 73 in the context of communication between two groups of gangsters. 

This problem was given the name the _Two Generals Paradox_ by [Jim Gray](/wiki/Jim_Gray_\(computer_scientist\) "Jim Gray \(computer scientist\)")[9] in 1978 in "Notes on Data Base Operating Systems"[10] starting on page 465. This reference is widely given as a source for the definition of the problem and the impossibility proof, though both were published previously as mentioned above. 

## References

[[edit](/w/index.php?title=Two_Generals%27_Problem&action=edit&section=6 "Edit section: References")]

  1. **^** Lamport, Leslie; Shostak, Robert; Pease, Marshall (1982-07-05). ["The Byzantine Generals Problem"](https://www.microsoft.com/en-us/research/publication/byzantine-generals-problem/). _ACM Transactions on Programming Languages and Systems_ : 382–401.
  2. **^** Gmytrasiewicz, Piotr J.; Edmund H. Durfee (1992). ["Decision-Theoretic Recursive Modeling and the Coordinated Attack Problem"](http://dl.acm.org/citation.cfm?id=139492.139503). _Artificial Intelligence Planning Systems_. San Francisco: Morgan Kaufmann Publishers. pp. 88–95\. [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1016/B978-0-08-049944-4.50016-1](https://doi.org/10.1016%2FB978-0-08-049944-4.50016-1). [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [9780080499444](/wiki/Special:BookSources/9780080499444 "Special:BookSources/9780080499444"). Retrieved 27 December 2013. `{{[cite book](/wiki/Template:Cite_book "Template:Cite book")}}`: `|journal=` ignored ([help](/wiki/Help:CS1_errors#periodical_ignored "Help:CS1 errors"))
  3. **^** [The coordinated attack and the jealous amazons](http://www.dsi.uniroma1.it/~asd3/dispense/attack+amazons.pdf) Alessandro Panconesi. Retrieved 2011-05-17.
  4. **^** Leslie Lamport. ["Solved Problems, Unsolved Problems and Non-Problems in Concurrency"](https://lamport.azurewebsites.net/pubs/solved-and-unsolved.pdf). 1983\. p. 8.
  5. **^** Ruby, Matt. ["How the Byzantine General's Problem Relates to You in 2024"](https://www.swanbitcoin.com/byzantine-generals-problem/). _Swan Bitcoin_. Retrieved 2024-02-16.
  6. **^** ["The Byzantine Generals Problem (Consensus in the presence of uncertainties)"](https://www.doc.ic.ac.uk/~jnm/DistrAlg/Notes/Byzantine-4up-final.pdf) (PDF). _[Imperial College London](/wiki/Imperial_College_London "Imperial College London")_. Retrieved 16 February 2024.
  7. **^** Lamport, Leslie; Shostak, Robert; Pease, Marshall. ["The Byzantine Generals Problem"](https://lamport.azurewebsites.net/pubs/byz.pdf) (PDF). _[SRI International](/wiki/SRI_International "SRI International")_. Retrieved 16 February 2024.
  8. **^** Akkoyunlu, E. A.; Ekanadham, K.; Huber, R. V. (1975). [_Some constraints and trade-offs in the design of network communications_](https://dl.acm.org/doi/pdf/10.1145/800213.806523). Portal.acm.org. pp. 67–74\. [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1145/800213.806523](https://doi.org/10.1145%2F800213.806523). [S2CID](/wiki/S2CID_\(identifier\) "S2CID \(identifier\)") [788091](https://api.semanticscholar.org/CorpusID:788091). Retrieved 2010-03-19.
  9. **^** ["Jim Gray Summary Home Page"](http://research.microsoft.com/~Gray/JimGrayHomePageSummary.htm). Research.microsoft.com. 2004-05-03. Retrieved 2010-03-19.
  10. **^** R. Bayer, R. M. Graham, and G. Seegmüller (1978). _Operating Systems_. Springer-Verlag. pp. 393–481\. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [0-387-09812-7](/wiki/Special:BookSources/0-387-09812-7 "Special:BookSources/0-387-09812-7").`{{[cite book](/wiki/Template:Cite_book "Template:Cite book")}}`: CS1 maint: multiple names: authors list ([link](/wiki/Category:CS1_maint:_multiple_names:_authors_list "Category:CS1 maint: multiple names: authors list")) Online version: [_Notes on Data Base Operating Systems_](http://portal.acm.org/citation.cfm?coll=GUIDE&dl=GUIDE&id=723863). Portal.acm.org. January 1978. pp. 393–481\. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-3-540-08755-7](/wiki/Special:BookSources/978-3-540-08755-7 "Special:BookSources/978-3-540-08755-7"). Retrieved 2010-03-19.


## See also

[[edit](/w/index.php?title=Two_Generals%27_Problem&action=edit&section=7 "Edit section: See also")]

  * [Consensus algorithm](/wiki/Consensus_algorithm "Consensus algorithm")


Retrieved from "[https://en.wikipedia.org/w/index.php?title=Two_Generals%27_Problem&oldid=1340776655](https://en.wikipedia.org/w/index.p

[... truncated at 20,000 characters ...]

# 6.4 Proof of Work -- Source Inventory

> **Pipeline step:** Step 1 -- Triage COMPLETE
> **Source file:** `Proof of work.md` (read-only, ~1,500 words)
> **Scope:** Explains what Proof of Work is, how it functions technically, why it was invented, and why it is essential to Bitcoin -- covering the double-spend problem, energy expenditure as a feature, the difficulty adjustment, Nakamoto consensus, and the oracle problem.
> **Orphans imported:** None

---

## Part 2: Source Inventory

### What Proof of Work Is

1. Proof of Work is the first workable solution to the double-spend problem at scale. (Author)
2. Proof of Work is a consensus mechanism utilized in Bitcoin. (Author)
3. Mining nodes compete to create new blocks by running specialized hardware to solve the Proof-of-Work algorithm. (Author)
4. In order to mine a block, a miner must guess and check numbers until a solution to the puzzle is found. (Author)
5. Once the miner discovers the solution, a block is formed and broadcast to all other nodes who update their version of the ledger. (Author)
6. New blocks are linked to the ones before them, creating a chain of transactions. (Author)
7. The blockchain with the most work put into it is considered "law" by the miners. (Author)
8. "This 'work' is cryptographic proof that energy was expended looking for solutions, and keeps the system honest." (Author)
9. You would have to out-mine all other miners in order to tamper with the ledger. (Author)
10. Proof of Work acts as an energy forcefield to the network. (Author)

### How Proof of Work Was Invented and How It Functions

11. Proof of Work was invented by Adam Back as a way to prevent email spam. (Author)
12. It creates a real-world cost and imposes physical limits in a limitless cyber universe. (Author)
13. Bitcoin works like a CAPTCHA -- you can't just create new money, you have to solve a puzzle. (Author)
14. Miners use special ASIC computers to guess and check numbers that satisfy the conditions of a block. (Author)
15. There is no way to cheat -- the only way to find the answer is to guess; the solution is so improbable that finding it is proof that work was done. (Author)
16. Energy is the link between the real world and cyberspace -- otherwise cyberspace is a place without limits. (Author)

### The Mining Lottery -- Satoshi's Description

17. "New bitcoins will still continue to be created every ten minutes for the next couple years. In an attempt to hand them out fairly, the original creator of Bitcoin devised an extraordinarily clever scheme: a kind of global math contest." (Dergigi / inalienable-property-rights)
18. The winner of each roughly ten-minute round gets that round's reward: a treasure chest of brand new, never-used bitcoins. (Dergigi / inalienable-property-rights)
19. The difficulty of the next math problem is increased based on how quickly the last few were solved, keeping rounds always roughly ten minutes long no matter how many players enter. (Dergigi / inalienable-property-rights)

### PoW as a Bridge Between Atoms and Information

20. "Bitcoin's proof-of-work serves as a bridge between the world of atoms and the realm of information." (Dergigi / Twitter)
21. "This bridge can be built in one way and one way only: by coming up with information that is so unique, so preposterously unlikely, that certain things had to happen in the real world for this information to appear." (Dergigi / Twitter)

### PoW is Multi-Purpose

22. "Proof-of-work is multi-purpose: Duration, costly signal, public data integrity, conflict resolution, probabilistic irreversibility, cryptanalytic stability... All these and more are solved by difficulty-adjusted PoW." (Dergigi / Twitter)
23. "A failure to understand proof of work is a failure to understand Bitcoin." (Dergigi / dergigi.com)

### Proof of Work 101 -- Technical Detail (Lyn Alden)

24. The Bitcoin network is programmed to create a new block on average every ten minutes since inception in 2009. (Lyn Alden / lynalden.com)
25. A new block is produced by a bitcoin miner contributing processing power (electricity) to solve a cryptographic puzzle left by the previous block, at which point the miner packages thousands of transactions into that block -- that's how transactions get settled. (Lyn Alden / lynalden.com)
26. Processors use random guesses to solve the puzzle; the law of large numbers means more mining equipment equals more blocks found over a sufficient period. (Lyn Alden / lynalden.com)
27. If miners drop off and blocks start taking longer than ten minutes, the network automatically makes the puzzle easier -- this is the difficulty adjustment, occurring every two weeks. (Lyn Alden / lynalden.com)
28. If miners join and blocks speed up, the network makes the puzzle harder. (Lyn Alden / lynalden.com)
29. In the first half of 2021 China banned crypto mining and approximately half the global Bitcoin network went offline; Bitcoin kept working with 100% uptime. (Lyn Alden / lynalden.com)
30. Imagine if Amazon or Microsoft had to move half their server capacity internationally with one week's notice -- they would likely have uptime issues for the rest of the year. Bitcoin did not. (Lyn Alden / lynalden.com)
31. If a miner creates an invalid block, the network discards it. (Lyn Alden / lynalden.com)
32. If two miners produce a valid block at the same time, the winner is decided by which one gets found by the rest of the network first and has another valid block added onto it. (Lyn Alden / lynalden.com)
33. The longest blockchain is the one with the most work put into it and that meets consensus criteria -- that blockchain becomes global consensus. (Lyn Alden / lynalden.com)
34. The more energy Bitcoin's network uses, the more secure its latest transactions are against most types of attacks. (Lyn Alden / lynalden.com)
35. Many small non-Bitcoin blockchains have been victims of 51% attacks -- where a single entity gains control of over 51% of processing power and uses it to re-organize blocks and perform double-spend transactions (essentially theft). (Lyn Alden / lynalden.com)
36. Work is the arbiter of truth in Bitcoin -- there is no central authority that decides what constitutes a valid block; the longest blockchain is verifiable and recognized by all. (Lyn Alden / lynalden.com)

### Energy as a Feature -- Immutability Through Energy

37. "Repeating the entire world's collective hashing effort from the edited block to the latest block is the barrier to editing Bitcoin." (Arman the Parman / armantheparman.com)
38. The energy expended to create hashes with improbable zeros must be repeated to edit Bitcoin. (Arman the Parman / armantheparman.com)
39. This is why energy used to mine Bitcoin is not "wasted" -- it defends Bitcoin from edits and makes the ledger immutable without needing to trust a central authority. (Arman the Parman / armantheparman.com)
40. "Satoshi also realized that the only real-world asset that can be linked to a computer system in a trustless manner is energy, nothing else." (Dergigi / bitcoin-is-an-idea)
41. Every other thing -- gold, paper certificates, real estate, strawberries -- re-introduces a trusted third party because of the inherent disconnect between the digital and the physical world. (Dergigi / bitcoin-is-an-idea)
42. Someone always has to make sure real-world assets and their digital representations remain in sync -- this is the oracle problem. (Dergigi / bitcoin-is-an-idea)
43. Proof-of-Work solves the oracle problem in an ingenious, roundabout way: by using energy and physics as the base truth. (Dergigi / bitcoin-is-an-idea)
44. The oracle problem is a variant of the GIGO principle (Garbage In, Garbage Out) -- you can never be sure data represents reality, except if the reality is rooted in computation itself. (Dergigi / bitcoin-is-an-idea)
45. "The fact that block production requires electricity is a feature, not a bug. It acts as an unforgeable costly signal that is used to build up a trustless arrow of time, as well as a transparent and publicly verifiable shield around the past." (Dergigi / bitcoin-is-digital-scarcity)
46. Electricity in block production is "an anti-cheat mechanism to ensure that the past can't be altered cheaply and to ensure that future issuance can't be farmed efficiently." (Dergigi / bitcoin-is-digital-scarcity)
47. "Bitcoin is a digital item in a digital environment, brought about and kept alive by physical processes." (Dergigi / bitcoin-is-digital-scarcity)
48. "It is the combination of the physical with the digital that gives Bitcoin its power: a digital commodity that can be sent around at the speed of light, inexorably linked to the physical laws of our universe." (Dergigi / bitcoin-is-digital-scarcity)

### Why Proof of Work is Important

49. Satoshi was looking for a way to make a trustless system with a monetary policy that couldn't be co-opted by special interests -- a neutral third party. (Author)
50. PoW secures the network -- you can't double-spend or DDoS the network without competing with honest actors. (Author)
51. PoW issues new currency in a fair way -- it's a provably random lottery that is incorruptible. (Author)
52. PoW records transactions on the blockchain, creating an immutable proof of history of transactions -- providing irreversibility, immutability, and data integrity. (Author)
53. PoW is a network self-perpetuation and preservation mechanism -- lottery winners have an economic interest in keeping the system alive, which builds trust, builds price, and brings more miners online. (Author)
54. PoW establishes Nakamoto consensus -- Bitcoin is an automated justice system and truth arbitrator, enforcing rules in a non-violent way. (Author)
55. Nakamoto consensus provides peaceful conflict resolution -- the longest chain with the most work is the correct order of transactions; there's no room for disagreement and conflicts are solved through mining, not force. (Author)
56. PoW anchors Bitcoin to the real world -- energy is the link from the real world to cyberspace. (Author)
57. Bitcoin = Money + Time + Energy + Information (Dergigi formula, referenced via YouTube)

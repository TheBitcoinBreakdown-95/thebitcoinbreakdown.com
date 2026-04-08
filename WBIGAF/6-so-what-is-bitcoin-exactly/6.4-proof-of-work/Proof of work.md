- Proof of work is the first workable solution to the double spend problem at scale
    
- What is proof of work?
    - Proof of work is a consensus mechanism utalized in bitcoin
    - Mining nodes compete to create new blocks by running specialized hardware to solve the proof-of-work algorithm.
        - In order to mine a block, a miner must guess and check lots of numbers until a solution to the puzzle is found. 
        - Once the miner discovers the solution, a block is formed and the newly mined block is broadcast to all other nodes on the network who then update their version of the ledger. 
        - The new blocks are linked to the ones before them, creating a chain of transactions
        - The blockchain with the most work put into it is considered “law” by the miners
        - This “work” is cryptographic proof that energy was expended looking for solutions, and keeps the system honest
            - As long as the majority of miners on the network are adding blocks to a chain it remains the 
        - It therefore it acts as an energy forcefield to network. 
        - You would have to out mine all other miners in order to tamper with the ledger
    -   
        
    -   
        
    -   
        
    - “New bitcoins will still continue to be created every ten minutes for the next couple years. In an attempt to hand them out fairly, the original creator of Bitcoin devised an extraordinarily clever scheme: a kind of global math contest. The winner of each roughly ten-minute round gets that round’s reward: a little treasure chest of brand new, never-used bitcoins, created from the answer you came up with to that round’s math problem. To keep all the coins in the lottery from being won too quickly, the difficulty of the next math problem is increased based on how quickly the last few were solved. This mechanism is the explanation of how the rounds are always roughly ten minutes long, no matter how many players enter the competition.”
-   
       
\> From \<[https://dergigi.com/2022/04/03/inalienable-property-rights/](https://dergigi.com/2022/04/03/inalienable-property-rights/)\>  

Bitcoin's proof-of-work serves as a bridge between the world of atoms and the realm of information. This bridge can be built in one way and one way only: by coming up with information that is so unique, so preposterously unlikely, that certain things had to happen in the real world for this information to appear. The rules of the game and the nature of physical law allow for no other possibility.
   

[https://twitter.com/dergigi/status/1565633115317469184?s=21&t=lUbh7T7dIyIiY2tOHK4fLQ](https://twitter.com/dergigi/status/1565633115317469184?s=21&t=lUbh7T7dIyIiY2tOHK4fLQ)  
Proof-of-work is multi-purpose.
 
Duration, costly signal, public data integrity, conflict resolution, probabilistic irreversibility, cryptanalytic stability...
 
All these and more are solved by difficulty-adjusted PoW.
   

[https://dergigi.com/threads/pow-is-essential](https://dergigi.com/threads/pow-is-essential)  
A failure to understand proof of work is a failure to understand Bitcoin.
          
https://www.fidelitydigitalassets.com/research-and-insights/understanding-proof-work?ccmedia=owned&amp;ccchannel=social&amp;cccampaign=proof-of-work-blog&amp;cctactics=linkedin&sf270293164=1
 - how proof of work works
    - Proof of work was invented by Adam back, as a way to prevent email spam. 
    - It creates a real world cost, imposes physical limits in a limitless cyber universe
        - Bitcoin works like a captcha, you can't just create new money, you have to solve a puzzle
    - Miners use special ASIC computers to guess and check numbers that satisfy the conditions of a block
    - There is no way to cheat, the way the crytography works the only way to find the number is to guess, the solution is so improbable, that means finding the solution to a block is proof that you put in the work.
    - Energy is the link between the real world and cyberspace, otherwise it’s a place without limits.    
[Bitcoin = Money + Time + Energy + Information by @dergigi](https://www.youtube.com/watch?v=DLsIcIoLSsI&t=13s)

- What money is
 
Repeating the entire world’s collective hashing effort from the edited block to the latest block is the barrier to editing Bitcoin. The energy was expended to create those hashes with all those improbable zeros, and that energy expenditure must be repeated to edit Bitcoin. This is why energy used to mine Bitcoin is not “wasted”; it is there to defend Bitcoin from edits; to make the ledger immutable without needing to trust a central authority.

\> From \<[https://armantheparman.com/mining/](https://armantheparman.com/mining/)\>     

Satoshi also realized that the only real-world asset that can be linked to a computer system in a trustless manner is energy, nothing else. Every other thing—no matter if it’s gold, paper certificates, real estate, or strawberries, re-introduces a trusted third party because of the inherent disconnect between the digital and the physical world. Someone has to make sure that the real-world assets and the digital representation of these assets—in essence, a list of things—remains up-to-date and in sync. This is what is known as the **oracle problem**, and proof-of-work solves it in an ingenious, roundabout way: by using energy, and thus physics, as the base truth. One can also think of the oracle problem as a variant of the GIGO principle: Garbage In, Garbage Out. You have to trust whoever is keeping the records that the records are correct. Phrased differently: you can never be sure that the data at hand represents reality, except if the reality is rooted in computation itself.
 \> From \<[https://dergigi.com/2021/06/13/bitcoin-is-an-idea/](https://dergigi.com/2021/06/13/bitcoin-is-an-idea/)\>        

 the fact that block production requires electricity is a feature, not a bug. It acts as an unforgeable costly signal that is used to build up a trustless arrow of time, as well as a transparent and publicly verifiable shield around the past. It is an anti-cheat mechanism to ensure that the past can’t be altered cheaply and to ensure that future issuance can’t be farmed efficiently.  
…  
Bitcoin is a digital item in a digital environment, brought about and kept alive by physical processes. It is the combination of the physical with the digital that gives Bitcoin its power: a digital commodity that can be sent around at the speed of light, inexorably linked to the physical laws of our universe.
 \> From \<[https://dergigi.com/2022/10/02/bitcoin-is-digital-scarcity/](https://dergigi.com/2022/10/02/bitcoin-is-digital-scarcity/)\>     

Proof-of-Work 101
 
The Bitcoin network is programmed to create a new block on average every ten minutes and add that block to the blockchain, which consists of hundreds of thousands of blocks since inception in 2009.  
A new block is produced by a bitcoin miner (a specialized computer) contributing processing power (and thus electricity) to solve a cryptographic puzzle that the previous block created, at which point the miner can package thousands of bitcoin transactions currently in the queue, into that block. That’s how transactions get settled. The network is programmed to target average block times of ten minutes, meaning on average every ten minutes a block of thousands of transactions is added to the blockchain.  
Processors use random guesses to solve the puzzle left by the prior block, but the law of large numbers is such that the more bitcoin mining equipment you have, the more blocks you find over a sufficiently long period of time.  
If miners drop off the network and new blocks on average start taking longer than ten minutes to produce, the network is automatically programmed to make the puzzle easier by a quantified amount, so that blocks go back to an every-ten-minute average schedule. Likewise, if a lot of miners join the network and blocks get added to the blockchain faster than every ten minutes on average, the network will make the puzzle harder. This is known as the “difficulty adjustment” which occurs automatically every two weeks, and is one of the key programming challenges that Satoshi Nakamoto solved to make the network work properly.  
So, at any given time, there are millions of bitcoin mining machines around the world looking to solve the puzzle and create the next block, and there’s a natural feedback mechanism to ensure that blocks are created on average every ten minutes, regardless of how many or few miners are on the network.  
In the first half of 2021 China (by far the largest country in terms of miner concentration at the time) banned crypto mining, and approximately half the global Bitcoin network went offline and started moving elsewhere. Bitcoin’s payment network briefly slowed down, but otherwise kept working with 100% uptime. The difficulty adjustment then kicked in, and brought the network back up to its target speed. Imagine if Amazon or Microsoft were told with one week’s notice that they had to move half of their server capacity internationally; they would likely experience uptime issues for their services for the rest of the year (at least) as they moved and rebuilt half of their infrastructure. The Bitcoin network instead continued to operate with 100% uptime.  
If a miner creates an invalid block, meaning one that doesn’t conform to the shared rules of the existing node network, the network discards it. If two miners produce a valid block at around the same time, the winner will be decided by which one gets found by the rest of the network first and has another valid block produced and added onto it, becoming the longer (and thus official) blockchain. If those second blocks are also close, then it will come down to who wins the third valid block, or fourth valid block. Eventually a longer chain wins, as a greater share of the network is finding it and building on top of it.  
This process is known as “proof-of-work”. Millions of machines are using electricity to apply processing power to guess the answer to cryptographic puzzles left by the most recent block. This may seem like a waste of energy, but it’s what keeps the system decentralized. Work is the arbiter of truth, in this case. There is no central authority that decides what constitutes a valid block or a valid set of transactions; the longest blockchain is verifiable at any given time, and is recognized as truth by the rest of the network based on code.  
The longest blockchain is the one with the most work put into it, and that also meets the consensus criteria that the node network checks. That blockchain becomes the global consensus.  
The more energy that Bitcoin’s network uses, the more secure that its latest transactions are against most types of attacks. Many of the tiny non-Bitcoin blockchains have been victims of 51% attacks, where a single entity temporarily or permanently gains control of over 51% of the processing power on the network, and uses that majority of processing power to re-organize blocks and perform double-spend transactions (which is essentially theft).
 \> From \<[https://www.lynalden.com/proof-of-stake/](https://www.lynalden.com/proof-of-stake/)\>  
          \> From \<[https://dergigi.com/2022/04/03/inalienable-property-rights/](https://dergigi.com/2022/04/03/inalienable-property-rights/)\>                           
*A failure to understand proof of work is a failure to understand bitcoin
 \> From \<[https://armantheparman.com/mining/](https://armantheparman.com/mining/)\>      \> From \<[https://dergigi.com/2021/06/13/bitcoin-is-an-idea/](https://dergigi.com/2021/06/13/bitcoin-is-an-idea/)\>         \> From \<[https://dergigi.com/2022/10/02/bitcoin-is-digital-scarcity/](https://dergigi.com/2022/10/02/bitcoin-is-digital-scarcity/)\>        
\> From \<[https://www.lynalden.com/proof-of-stake/](https://www.lynalden.com/proof-of-stake/)\>  

- why it’s important
    1. Satoshi was looking for a way to make a trustless system with a monetary policy that couldn’t be coopted by special interests. A neutral third party
    2. secures the network
        1. Can't double spend or ddos the network without competing with honest actors
    3. it issues new currency in a fair way
        1. Provably random lottery, incorruptible
    4. Records transactions on the blockchain creating an immutable proof of history of transactions, 
        1. irreversibility/immutability
        2. data integrity 
    5. Network self-perpetuation & preservation mechanism 
        1. Lottery winners have an economic interest in keeping the system alive, which builds trust and price and more miners come online
    6. Establishing Nakamoto consensus
        1. Bitcoin is an automated justice system and truth arbitrator, enforcing the rules in a non-violent way
        2. Peaceful conflict resolution
            1. The longest chain, with the most work put into it, is the correct order of transactions. There's no room for disagreement. Conflicts in the order of time are solved through mining, and not through force. 
    7. anchoring bitcoin to the real world
        1. energy is a link from the real world to cyberspace
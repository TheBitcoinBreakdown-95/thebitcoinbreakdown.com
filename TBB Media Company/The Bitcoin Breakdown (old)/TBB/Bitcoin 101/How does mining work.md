[Bitcoin Lesson | Mining](https://www.youtube.com/watch?v=MJ0OzrkHvXA)  
Learn me a bitcoin
   

BW: Say more about the environmental harms. Why does making magical internet money use so much energy?
 
ES: Okay, imagine you decide to get into “mining” bitcoins. You know there are a limited number of them up for grabs, but they’re coming from somewhere, right? And it’s true: new bitcoins will still continue to be created every ten minutes for the next couple years. In an attempt to hand them out fairly, the original creator of Bitcoin devised an extraordinarily clever scheme: a kind of global math contest. The winner of each roughly ten-minute round gets that round’s reward: a little treasure chest of brand new, never-used bitcoins, created from the answer you came up with to that round’s math problem. To keep all the coins in the lottery from being won too quickly, the difficulty of the next math problem is increased based on how quickly the last few were solved. This mechanism is the explanation of how the rounds are always roughly ten minutes long, no matter how many players enter the competition.
      

[https://armantheparman.com/mining/](https://armantheparman.com/mining/)
 
the funny way to think about mining is that it's like running your PlayStation 24 hours a day resulted in solved sudokus you could trade for heroine. But basically what you have to know is that it is the process that settles bitcoin transactions and keeps them record forever.
 
When you send a transaction on PayPal, the software just updates it's backend number spreadsheet. In bitcoin when you send a transaction it just updates it's backend number spreadsheet. Basically the same idea. PayPal's spreadsheet is private, not open source or transparent and the company can theoretically go in and update whatever numbers they want. In bitcoin the spreadsheet is public, everyone has a record and no one has the ability to update someone else's numbers.

\> From \<[https://thebitcoinbreakdown.com/wp-admin/post.php?post=163&action=edit](https://thebitcoinbreakdown.com/wp-admin/post.php?post=163&action=edit)\>        

[https://twitter.com/bitcoinnewscom/status/1673118963293724673?s=46&t=KWxEkTiQ4L9C3lu9s4hJJw](https://twitter.com/bitcoinnewscom/status/1673118963293724673?s=46&t=KWxEkTiQ4L9C3lu9s4hJJw)
 
Nakamoto consensus is built on Proof-of-Work, which requires miners to **expend real-world computational resources** to find a valid block. Specifically, miners attempt to find a nonce such that the SHA-256 hash of the block header is below a target difficulty threshold. This process is fundamentally **non-deterministic guessing** — not solving a puzzle — where each guess consumes electricity and time.  
This expensive activity anchors consensus to the real world. The difficulty adjustment ensures that blocks are found roughly every 10 minutes on average, regardless of total hashrate.
 
What makes Nakamoto consensus novel is the **rule that the valid chain with the most accumulated PoW (not simply the most blocks)** is considered canonical by all honest nodes. This rule is **objective and verifiable**: any node, even newly joining the network, can independently validate which chain has the greatest work embedded in it.  
This eliminates the need for voting, trusted third parties, or identity-based coordination. It provides a deterministic tie-breaker in the presence of forks.
    
### **Why Miners Follow the Longest (Heaviest) Chain: Game Theory Meets Thermodynamics**

Yes, incentives are at the heart of miner behavior — but it's not _only_ about profit.

_Economic Incentives:_- Miners earn block subsidies and transaction fees only if their block is included in the chain that others build upon.
- **If a miner mines a block on a shorter chain that is ultimately orphaned, they lose the block reward — which can be significant.**
- Thus, miners have a **strong economic incentive to always mine on the tip of the heaviest valid chain**, because that's the only way their efforts (PoW) will be rewarded.
_Coordination Equilibrium:_- The protocol creates a **coordination game**: the rational strategy is to follow the chain with the most work, because everyone else is doing the same.
- Attempting to deviate (e.g., mining on an old fork or rewriting history) has a cost: unless you control over 50% of total hashrate _and_ sustain it, your fork will be ignored, and your work wasted.
_Thermodynamic Finality:_- Once sufficient PoW accumulates on a chain, it becomes practically immutable. Rewriting history requires exponentially more work the further back you go.
- This is where PoW achieves something that digital signatures and timestamping alone cannot: it creates a **costly signal** of chronological ordering that can’t be forged or undone without immense resource expenditure.       
Nakamoto Consensus relies on the assumption that a **majority of miners (hashrate)** are honest, in the sense that they follow the protocol rules. If that assumption holds, the protocol guarantees that:

- Double-spending is prevented.
- Consensus converges probabilistically (with greater certainty as more blocks are confirmed).
- A global state of transaction finality emerges, purely from local rules and incentives.

It’s a brilliant fusion of economics, cryptography, and thermodynamics. No identity or politics involved. Just raw energy, math, and time.
      

Miners follow the chain with the most accumulated PoW not out of moral duty or blind protocol-following — but because:

- **They are economically incentivized to do so** (maximizing expected profit).
- **The protocol penalizes deviation** (orphaned blocks).
- **The system self-reinforces** (everyone else does the same, creating a Schelling point).
    - (Bitcoin Core (the reference implementation) contains logic that ensures a node always adopts the chain with the greatest cumulative work, not the longest chain, and not the chain with the most transactions.)
- **The rule is unambiguous and universally verifiable**.

In essence, Nakamoto Consensus is a decentralized economic engine that uses thermodynamic expenditure to enforce chronological ordering — with miner incentives acting as the gears that keep it running.
    
[https://99bitcoins.com/education/bitcoin-mining/](https://99bitcoins.com/education/bitcoin-mining/)
   

![Embedded YouTube video](https://www.youtube.com/embed/MJ0OzrkHvXA?feature=oembed&autoplay=true)
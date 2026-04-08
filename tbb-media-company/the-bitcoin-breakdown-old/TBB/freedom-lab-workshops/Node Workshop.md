- Text peter and ask about electrum server
- Notes:
- [https://www.lopp.net/bitcoin-information/full-node.html](https://www.lopp.net/bitcoin-information/full-node.html)
    - Provide all of Lopp's resources
  
Initial Block Download(IBD)  
Initial block download refers to the process where nodes synchronize themselves to the network by downloading blocks that are new to them. This will happen when a node is far behind the tip of the best block chain. In the process of IBD, a node does not accept incoming transactions nor request mempool transactions.
    
- Using your node over Tor
- Integrating a Lightning node
- Building a local explorer with Mempool.space
- Verifying messages, signatures and raw transactions
- Running a watch-only setup for cold storage
- Contributing to Bitcoin Core or translating
 
**🧠** **8. Philosophy to Emphasize**

- You don’t outsource verification
- You reject surveillance finance
- You participate in a network that values _rules without rulers_
   

Node hardware requirements:

- Community posts and resources, and common issues resolved
 
Recommended OS Requirements:

- Quad-Core CPU 2.5Ghz+ (boost)
- 8GB+ RAM
- 2TB+ Storage
 
- 5 Port Switch
    - [https://www.bhphotovideo.com/c/product/1642110-REG](https://www.bhphotovideo.com/c/product/1642110-REG)
- New/Unused USB Stick - 64gb ram minimum - $8
- Ethernet cable -
- Stickers

- HP EliteDesk 800 G3 i5 Mini 65W, 16G-Ram
    - On Amazon for $120-$250
        - $83 - Also refurbished for cheaper on ebay, with pre-installed 2TB
        - [https://www.ebay.com/itm/285910140376?mkcid=16&mkevt=1&mkrid=711-127632-2357-0&ssspo=aY7OL6JIRbO&sssrc=4429486&ssuid=bCx9YmazRPS&stype=1&var=&widget_ver=artemis&media=COPY](https://www.ebay.com/itm/285910140376?mkcid=16&mkevt=1&mkrid=711-127632-2357-0&ssspo=aY7OL6JIRbO&sssrc=4429486&ssuid=bCx9YmazRPS&stype=1&var=&widget_ver=artemis&media=COPY)
    - If your machine doesn't have 2TB it's recommended to buy an SSD that we can install into the node
    - SATA SSD - 2TB - $100
        - [https://www.amazon.com/Silicon-Power-Gen3x4-Solid-SP002TBP34A60M28/dp/B07ZQ97H3W/ref=sr_1_4?crid=3I8ONE4635SAA&dib=eyJ2IjoiMSJ9.54S5lyRrAdsrq4Ji9UhjVgBTBO9KlaXZBXKgZobgu2if1h41asV3MQZCMKjM_KLBdYF84ylwg475us58V937pnBO6QStAOdwkXgm3m9y4WP0OmBQ0u014WTKAHOdddjTtVrOPKlfZvc0dfXpQH2Jh_k3Wls1-j9DEzyPP5dVi5BwCSxufJ4GS-e8_Tt3lOj2CEQAEP4gaySFkZmTMFZWEIPHmSQVxuiT9gd3W6YKmas.Q-XsI6C5t0tAGIa7xJXwYgpDN6LE-Qk9mrpDvag0dWg&dib_tag=se&keywords=SATA%2BNVMe%2B2TB&qid=1756955800&sprefix=sata%2Bnvme%2B2tb%2Caps%2C85&sr=8-4&th=1](https://www.amazon.com/Silicon-Power-Gen3x4-Solid-SP002TBP34A60M28/dp/B07ZQ97H3W/ref=sr_1_4?crid=3I8ONE4635SAA&dib=eyJ2IjoiMSJ9.54S5lyRrAdsrq4Ji9UhjVgBTBO9KlaXZBXKgZobgu2if1h41asV3MQZCMKjM_KLBdYF84ylwg475us58V937pnBO6QStAOdwkXgm3m9y4WP0OmBQ0u014WTKAHOdddjTtVrOPKlfZvc0dfXpQH2Jh_k3Wls1-j9DEzyPP5dVi5BwCSxufJ4GS-e8_Tt3lOj2CEQAEP4gaySFkZmTMFZWEIPHmSQVxuiT9gd3W6YKmas.Q-XsI6C5t0tAGIa7xJXwYgpDN6LE-Qk9mrpDvag0dWg&dib_tag=se&keywords=SATA%2BNVMe%2B2TB&qid=1756955800&sprefix=sata%2Bnvme%2B2tb%2Caps%2C85&sr=8-4&th=1)
        - Video on how to install the NVMe
            - [HP EliteDesk 800 G4 mini PC - how to replace SSD and upgrade memory RAM](https://www.youtube.com/watch?v=5gkaJWC-K90) 
Raspberri Pi build is also about $220 so the mini-computer is much better performance for not much more money
   

**What Is a Bitcoin Node?**

- Downloading and verifying the entire blockchain
- Validating transactions and blocks according to Bitcoin’s consensus rules
- Relaying valid transactions to other peers
- Optionally broadcasting your own transactions

- **Full node:** Verifies all rules from Genesis to present. Trustless.
- **Pruned node:** Like a full node but deletes old block data to save space.
- **Light node (SPV):** Only downloads headers, relies on full nodes. Not trustless.
- **Mining node:** A full node that also constructs blocks and guesses nonces.
- **Archival node:** Stores the full UTXO set and the entire blockchain.
   

**Why Run a Node?**

- Your node, your rules. You verify your own transactions. No trust required.

- No need to query third-party servers like a light wallet. You can look up your own balances and TX history directly.

- Running a node forces you to learn how Bitcoin actually works under the hood.

- By running a node, you enforce the rules. You don't just _follow_ consensus—you _are_ consensus.

- The more nodes, the more decentralized and robust the network becomes.
 - What a BTC node is, a way for you to verify incoming transactions and your current balance
- If you're not running a full node, you are trusting someone else to feed you that information, and that could be dummy data, no way to verify that what they're showing you is actually bitcoin.
    - For example, say you have your hardware wallet, and you plug that in and you go to the website/software, how do you know that the software is actually part of the 21MM bitcoins that we all agree to? The answer is that you don't, you're trusting the software to feed you that information because you're using their node to verify.
    - What if one day, these companies that you're fetching your ballances from, say they believe that BTC has 25 Million coins and not 21 million, so they're showing you a balance that's a number out of 25 million coins, significantly diluted, and so this is why we need to verify our own balances using the node that we downloaded, that we fetched from bitcoin core, and so running a node is the most trust minimized way of verification, and it's incredibly important that it's accessible to the individual level.
    - What that means is, I don't need to run a massive server, don't need to be a company, don't have to invest a significant amount of money, don't have to be a huge entity with a lot of wealth in order to do this.
    - Need to be able to verify your coins at an individual level, not a giant corporation
    - That's how we want to keep bitcoin, so that its always accessible to the individual, using computer parts and hardware that will always be available for the individual
    - The reason that we do that, is that if it's not accessible to the everyday consumer, then what happens is that we end up with centralized servers, and the controllers of these servers have the ability to censor you, they can block payments and you then get into a situation where you're asking for permission to transact on the bitcoin network
- The other thing that you're doing when you're running a full node, is that you're defending your chosen ruleset
    - Bitcoin is a voluntary participation, and when you run the software that you decide is money, you believe that there should only be a max of 21 million coins that are on issue, and you're defending that, and making sure that this is the node that I wish to participate and transact on with other people, and those who are going to pay me should also be part of that 21 million coins and not something else
- Need to make sure we are an economic node
    - i.e the more people running nodes the more decentralized
- Another reason is that it enhances privacy
    - When you plug your hardware wallet into your computer, and you go out and query the blockchain using their bitcoin node, and it gives a result back, is that your internet/IP address has been logged with Ledger's node
    - Quirying is what's known as an ex pub, or a master public key, which is what contains all of your past and future transactions, your IP address is logged with every one of your past and future transactions
- Lastly, you run a full node to help out the network propagate blocks to other peers/nodes that you're connected to
- The two most important things about bitcoin are self-custody and running your own node 
[https://en.bitcoin.it/wiki/Full_node](https://en.bitcoin.it/wiki/Full_node)
 - Running a full node is the only way you can use Bitcoin in a trustless way.
- You will know for sure that all the rules of Bitcoin are being followed, for example that no bitcoins are spent not belonging to the owner, that no coins were spent twice, that no inflation happens outside of the schedule and that all the rules needed to make the system work (e.g. difficulty) are followed.
- Full nodes are currently the most private way to use Bitcoin, with nobody else learning which bitcoin addresses belong to you.
- Full nodes are the most secure way to use Bitcoin, they do not suffer from many attacks that affect lightweight wallets.

Network Services

- Full nodes may provide various services to other network participants
    - Filtering transactions and blocks on behalf of lightweight nodes so that lightweight nodes do not need to download every transaction ever made on the network in order to find their own transactions.
    - Serving historical full blocks to nodes that have been offline for a while.
    - Transmitting new transactions from users to miners.
    - Broadcasting new blocks from miners to other nodes.   

I can single handedly enforce satoshi’s consensus rules  
[GuysTake_012 - Full Nodes or Nothing, The Story of Validation [Part 1]](https://open.spotify.com/episode/3qAzMtj3gErLFAqe7tlIeG?si=4viakdAsSHKZ8IaIluN7xA&dl_branch=1)
 
[Bitcoin Q&A: Why Running a Node is Important](https://www.youtube.com/watch?v=oX0Yrv-6jVs)
      

[https://twitter.com/foundationdvcs/status/1570128564569407488?s=46&t=IxnAfOPkGq68Ne3K-HTuGA](https://twitter.com/foundationdvcs/status/1570128564569407488?s=46&t=IxnAfOPkGq68Ne3K-HTuGA)
    
[https://bitcoinmagazine.com/technical/erlay-preserves-bitcoins-decentralization](https://bitcoinmagazine.com/technical/erlay-preserves-bitcoins-decentralization)  
 A full node is any computer that maintains and stores the entire Bitcoin blockchain; in order to verify and record new transactions as they happen, according to a common set of network consensus rules. In the absence of a central party, it’s these nodes that act as referees of the Bitcoin network by independently validating all transactions and blocks; and filtering out invalid transactions. This is how the Bitcoin network removes trust in any centralized entity and ensures the integrity of its 21 million supply cap.
   
    
**7. Optional Topics for Advanced Attendees**
 
Running a Bitcoin node is **not** about ROI. It's about **independence** and **truth**.
   

[https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/202](https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/202)
 
If you intend to run Bitcoin or store any meaningful amount of data, we recommend the following:
 
Other Requirements:
 
Recommended Computers:
    
A **Bitcoin node** is software that participates in the Bitcoin network by:  
**Types of nodes:**
   

**🔐** **Sovereignty**  
**🛡️** **Privacy**  
**🧠** **Education**  
**🗳️** **Consensus Participation**  
**🧩** **Support for the Network**
                      
**🧱** **What Is a Bitcoin Node?**

- ~~A~~ **Bitcoin node** ~~is a piece of software (most often Bitcoin Core) that:~~
    
    - Downloads and verifies the entire Bitcoin blockchain.
    - Validates all incoming transactions and blocks.
    - Ensures that all Bitcoin rules (like the 21 million cap, no double spends, etc.) are being followed.
    - Participates in the peer-to-peer network by relaying valid transactions and blocks to other nodes.
    
    - **Full node:** Verifies all rules from Genesis to present and stores the full UTXO set and the entire blockchain. Also known as an archival node.
    - **Pruned node:** Like a full node but deletes old block data to save space.
    - **Light node (SPV):** Only downloads headers, relies on full nodes. Not trustless.
    - **Mining node:** A full node that also constructs blocks and guesses nonces.
    -   
        
-   
    
- At its core, a node is **your tool for verifying reality**. It gives you the ability to independently confirm your:
    - Incoming transactions
    - Current balances
    - Chain history
- Without your own node, you’re outsourcing this verification to **someone else’s server** — meaning you’re effectively trusting them to be honest and competent.
    
    - Don't trust verify
    - If you are trusting you're not sovereign
    
    - You verify your own truth.
    - No reliance on anyone else to tell you what Bitcoin is.
- "What is the real bitcoin?"
    - The rules to which you agree and which you enforce 
**Types of nodes:**
   

**Running your own node**
   

**🔍** **Why Is This Important?**  
**🧾** **Trustless Verification of Balances**
 
-   
    
- running a full node ensures that you can't be tricked into accepting invalid bitcoin payments. Running and using your own node gives you the strongest security model Bitcoin has to offer. - If you're not running your own full node, you're trusting someone else (e.g., Ledger, Trezor, Electrum servers) to feed you information.
    - That data _could_ be incorrect, malicious, or manipulated — and you'd have no way to detect it.
- **Example**: You plug your hardware wallet into your computer and open its companion app. The app tells you your balance — but how do you know that data is accurate?
    - You're trusting their node to verify your balance _on your behalf_. You're not actually verifying anything yourself.
- What if these companies decide, maliciously or mistakenly, that Bitcoin now has **25 million coins** instead of 21 million?
    - Their node software would show you balances and transactions _based on a diluted supply_, and you'd have no way to prove otherwise unless you run your own node.
    - Running your own node ensures you're always referencing the **true Bitcoin ledger**, the one governed by the consensus rules you choose.
- I like to think of node runners as the old guard, hidden cloaked figures upholding the consensus rules as bitcoin was intented
   

**🔐** **Sovereignty and Individual Access**

- Running a node is how you participate in Bitcoin at the **individual level**. You don’t need:
    - A data center
    - A corporation
    - A huge budget or technical team
- It’s designed so that anyone with a modest computer, basic hardware, and an internet connection can **defend their monetary truth**.
- If node operation becomes centralized in the hands of a few server operators or companies:
    - They could begin to **censor**, **gatekeep**, or **distort** the network.
    - This destroys Bitcoin’s core property of **permissionlessness**.
- We must preserve the ability for **any individual to verify Bitcoin**, because:
    - It keeps Bitcoin honest.
    - It prevents gatekeeping.
    - It avoids central points of failure.
- Full nodes are the **most secure way** to use Bitcoin. They do not suffer from the weaknesses and vulnerabilities that affect SPV wallets.
    - "Full nodes offer the strongest security model. When you have a copy of the ledger that you have validated yourself, you no longer have to trust a third party to be honest about the state of the ledger. If you’re using a centralized wallet, you’re completely trusting that they are running nodes that enforce the rules of the network. If you’re using an SPV wallet, you’re trusting that the majority of hashpower is validating the rules of the network to which you agree."
      
    
   

**🛡️** **Defending the Ruleset**

- By running a node, you are **defending the ruleset you choose to follow**.
    - That includes the **21 million supply cap**, the **block time**, the **difficulty adjustment**, and more.
- Bitcoin is voluntary. No one can force you to upgrade or change rules — unless you surrender verification to someone else.
- Running a node means:
    - “These are the rules I accept.”
    - “These are the coins I recognize.”
    - “This is the chain I consider valid.”
- You enforce consensus by **refusing to recognize invalid coins** or blocks. You are your own referee.

**"I can single-handedly enforce Satoshi’s consensus rules."**
 
**🧠** **Full Nodes Enable Trustless Bitcoin Usage**

- A full node is the **only way to use Bitcoin in a truly trustless way**.
- With your node, you verify:
    - That no one spends coins they don’t own.
    - That no coins were double-spent.
    - That no coins exist outside of the fixed issuance schedule.
    - That all other Bitcoin protocol rules are being followed — independently, without relying on third parties.
- It’s how Bitcoin removes the need for centralized trust and replaces it with **mathematical verification**.
 
**👤** **Privacy Benefits of Running a Node**

- Full nodes are the **most private way** to use Bitcoin.
- Without your own node:
    - Your wallet connects to someone else’s server.
    - That server sees your **IP address** and your **XPUB** (extended public key).
    - This links your IP to **all past and future transactions**.
- With your own node:
    - No one learns which addresses belong to you.
    - No one learns what addresses you send to or receive from
    - You query your own copy of the blockchain.
    - You maintain **informational privacy** and **network privacy**.
   

**🌍** **Helping the Bitcoin Network**  
When you run a full node, you contribute to the health and decentralization of the network:

- You help relay transactions and blocks to other peers.
- You validate transactions and stop invalid ones from propagating
- You provide services to lightweight (SPV) wallets by servicing data requests such as:
    - Filtering blocks and transactions for them.
    - Broadcasting their transactions to the network.
    - You provide historical block data for them.
    - Helping propagate new blocks from miners.
- You provide historical block data to nodes who've gone offline, or new nodes who want to join the network
-   
    
- Using a node to secure your own bitcoin makes you an **economic node** — one that validates and participates in the network actively.
 
The more economic full nodes exist, the more **decentralized and censorship-resistant** Bitcoin becomes.  
"From a macro perspective, full nodes keep the network honest. The more entities who are actively running nodes to audit their economic interactions, the more robust the network is against attacks. If you’re thinking from a nation-state attack scenario, more nodes = more “doors that have to be kicked down” in order to coerce the node owner into making changes against their will."
 
**⚙️** **Technical Summary: What Your Node Does**  
A full node:

- Stores and syncs the entire Bitcoin blockchain from genesis to present.
- Checks every transaction and block it receives.
    - Makes sure they are valid and don't contain double spends
- Stores and updates the current UTXO (unspent transaction output) set.
- Filters out invalid data (e.g., fake coins, invalid signatures).
- Ensures the 21 million BTC cap is never violated.
- Enforces the difficulty adjustment every 2,016 blocks.
- Relays valid transactions and blocks to peers.

In the absence of any central authority, nodes **are the referees** of the Bitcoin system.
 
**🧭** **Final Takeaways for Workshop Attendees**

- The two most important responsibilities in Bitcoin:
    - **Self-custody of your keys**
    - **Running your own node**
- These two together give you:
    - Sovereignty
    - Privacy
    - Security
    - Independence
    - A vote in Bitcoin's ongoing consensus
- Bitcoin was designed to empower the individual. If you’re not verifying, you’re trusting. And Bitcoin was not built on trust — it was built to **eliminate** it.
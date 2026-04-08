It’s basically just a new kind of database. Imagine updates are always added to the end of it instead of messing with the old, preexisting entries — just as you could add new links to an old chain to make it longer — and you’re on the right track. Start with that concept, and we’ll fill in the details as we go.
 
BW: Okay, but why? What is the question for which blockchain is the answer?
 
ES: In a word: trust. Imagine an old database where any entry can be changed just by typing over it and clicking save. Now imagine that entry holds your bank balance. If somebody can just arbitrarily change your balance to zero, that kind of sucks, right? Unless you’ve got student loans.
 
The point is that any time a system lets somebody change the history with a keystroke, you have no choice but to trust a huge number of people to be both perfectly good and competent, and humanity doesn’t have a great track record of that. Blockchains are an effort to create a history that can’t be manipulated.
 
BW: A history of what?
 
ES: Transactions. In its oldest and best-known conception, we’re talking about Bitcoin, a new form of money. But in the last few months, we’ve seen efforts to put together all kind of records in these histories. Anything that needs to be memorialized and immutable. Health-care records, for example, but also deeds and contracts.
 
When you think about it at its most basic technological level, a blockchain is just a fancy way of time-stamping things in a manner that you can prove to posterity hasn’t been tampered with after the fact. The very first bitcoin ever created, the “Genesis Block,” famously has one of those “general attestations” attached to it, which you can still view today.
 
It was a cypherpunk take on the old practice of taking a selfie with the day’s newspaper, to prove this new bitcoin blockchain hadn’t secretly been created months or years earlier (which would have let the creator give himself an unfair advantage in a kind of lottery we’ll discuss later).
 
- It's high-tech version of a public notary
 \> From \<[https://www.aclu.org/blog/privacy-technology/internet-privacy/edward-snowden-explains-blockchain-his-lawyer-and-rest-us](https://www.aclu.org/blog/privacy-technology/internet-privacy/edward-snowden-explains-blockchain-his-lawyer-and-rest-us)\>      
The interesting mathematical property of blockchains, as mentioned earlier, is their general immutability a very short time past the point of initial publication.
 
For simplicity’s sake, think of each new article published as representing a “block” extending this blockchain. Each time you push out a new article, you are adding another link to the chain itself. Even if it’s a correction or update to an old article, it goes on the end of the chain, erasing nothing. If your chief concerns were manipulation or censorship, this means once it’s up, it’s up. It is practically impossible to remove an earlier block from the chain without also destroying every block that was created after that point and convincing everyone else in the network to agree that your alternate version of the history is the correct one.
 
Let’s take a second and get into the reasons for why that’s hard. So, blockchains are record-keeping backed by fancy math. Great. But what does that mean? What actually stops you from adding a new block somewhere other than the end of the chain? Or changing one of the links that’s already there?
 
We need to be able to crystallize the things we’re trying to account for: typically a record, a timestamp, and some sort of proof of authenticity.
 
So on the technical level, a blockchain works by taking the data of the new block — the next link in the chain — stamping it with the mathematic equivalent of a photograph of the block immediately preceding it and a timestamp (to establish chronological order of publication), then “hashing it all together” in a way that proves the block qualifies for addition to the chain.
 
BW: With money, what is the problem that blockchain solves?
 
ES: The same one it solves everywhere else: trust
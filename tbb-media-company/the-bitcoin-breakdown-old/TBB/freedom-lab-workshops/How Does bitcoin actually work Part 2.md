- Obviously take from first speech and from the youtube video
- Dads advice was to do a quick intro about what bitcoin is and how this topic fits into that
- Really perfect the “what is bitcoin” 5 min pitch and branch off of that
- Mining
    - Hash algos
    - Nonce and difficulty target
    - Blocks
    - Block header
    - Blockchain
    - Difficulty and difficulty adjustment
    - Mempool
    - Proof of work
    - Nakamoto consensus
- Software
    - Protocol
    - Open source
    - Peer to peer network   
- What is bitcoin?
    - Money
- How does money work       
Make something interactive for each piece:
   
- People send a transaction by sending a text or by writing on a piece of paper
- They race to mine by rolling dice and winning candy
- We bundle the transactions and then go again
-   
                           
Building each piece:

- Intro:
    - Why would you need to 'mine' internet money? What is the purpose?
    - There's a limit of 21 million, but how do you distribute them fairly?
        - Satoshi designed a way to give them out via a lottery, instead of just printing them all at once
        - Every 10 minutes miners compete to create a new block, the winner gets some bitcoin
        - This process will continue every 10 minutes until the year 2140 when all the bitcoin are mined
    - Bitcoin is also a payment app, like paypal, but who decides who has which money, and how do you stop people from stealing?
      
    
- Send a transaction
    - What is a transaction? When I take my money and send it from Alice to bob
- Transaction reaches the mempool
    - What is the mempool? Just a waiting room of transactions
- Miners take transactions from mempools and put them into blocks
    - What is a block? Just a collection of transactions
- Miners hash the blocks until a solution is found
    - Hashing algo
    - Nonce
    - Block headder
- Block is added to the blockchain
    - Block before is within the block header
- Nodes choose the chain with the most work
    - Following someone on twitter with the most followers, easy way to see they are the real one
       
Design a game:

- Write transacions on a piece of paper
- They go into a hat
- A miner pics some from the hat and starts rolling dice
- Winning miner gets some candy
- Transactions get written into a notebook
 
[https://www.gemini.com/cryptopedia/what-is-bitcoin-and-how-does-it-work](https://www.gemini.com/cryptopedia/what-is-bitcoin-and-how-does-it-work)
   

[https://armantheparman.com/bitcoin-english/](https://armantheparman.com/bitcoin-english/)
   

[http://learnmeabitcoin.com](http://learnmeabitcoin.com)
 
*less memes  
*More visuals

ES: Okay, imagine you decide to get into “mining” bitcoins. You know there are a limited number of them up for grabs, but they’re coming from somewhere, right? And it’s true: new bitcoins will still continue to be created every ten minutes for the next couple years. In an attempt to hand them out fairly, the original creator of Bitcoin devised an extraordinarily clever scheme: a kind of global math contest. The winner of each roughly ten-minute round gets that round’s reward: a little treasure chest of brand new, never-used bitcoins, created from the answer you came up with to that round’s math problem. To keep all the coins in the lottery from being won too quickly, the difficulty of the next math problem is increased based on how quickly the last few were solved. This mechanism is the explanation of how the rounds are always roughly ten minutes long, no matter how many players enter the competition
# medium.com -- Scraped Content

**URL:** https://medium.com/mycrypto/the-future-of-ethereum-doesnt-have-wallets-232fcee708bf
**Category:** medium-apify
**Scrape status:** DONE
**Source notes:**
**Scraped:** 2026-04-14
**Title:** The Future of Ethereum Doesn’t Have Wallets | by Taylor Monahan | MyCrypto | Medium
**Chars:** 14,497

---

The Future of Ethereum Doesn’t Have Wallets | by Taylor Monahan | MyCrypto
The Future of Ethereum Doesn’t Have Wallets
This is a talk I did for the first time at “Above Blockchain” this past weekend (2/24/18). It was put together in a few hours on Friday night and it puts into words some things I’ve been thinking about lately. The ideas explored here are much more fleshed out than they were initially, but I still feel they are in the “seedling” stage of ideation and implementation. I welcome all comments on what I’ve shared here to help me expand my thinking and force the idea to become more robust. :)
As the title suggests, I’m going to talk a bit about why the future of Ethereum doesn’t have wallets.
Now this may seem a bit odd, seeing as I have spent the last two and a half years building and scaling an ether wallet.
Like most things in this fast-moving space, the tools that are most useful and most needed today are not necessarily the tools that are most useful and needed tomorrow.
Let’s start by talking about what exactly a wallet is…which is actually a bit more complicated than you may think.
The term wallet is confusing, and people bring a lot of assumptions about this word depending on their experiences inside and outside the crypto-space.
Most people start on Coinbase and see Coinbase as a wallet. When those people moved off Coinbase in order to buy tokens or participate in ICOs, we had a terrifically hard time breaking all of their preconceived notions. We spent a lot of time re-training people’s brains to help them comprehend that we don’t hold their funds and we cannot recover their private keys and passwords.
When we integrated with Ledger & TREZOR’s Hardware Wallets and Metamask it only became more confusing for new users entering the space.
In Andreas Antonopoulos & Gavin Wood’s new book, Mastering Ethereum, they capture what a wallet is and the confusion it creates beautifully:
“At a high level, a wallet is an application that serves as the primary user interface…”
“A common misconception about Ethereum is that Ethereum wallets contain ether or tokens. [They are actually stored on the blockchain.] So an Ethereum wallet is actually a keychain.”
I strongly prefer the word keychain as it is more representative of what is happening, and it perhaps has less preconceived notions that we would have to break.
So, while Antonopoulos & Wood describe it as a user interface (which is how we describe it as well), the reality is new users entering this space do not inherently get this.
If we are trying on making the blockchain usable for the masses, we simply can’t have such confusion up front.
So, why are wallets such an integral part of the ecosystem today?
Right now everything is still speculative. The reason you likely interact with the blockchain today is almost certainly speculative and, even if you aren’t a trader, you are still primarily interacting with only the “money” aspect of the blockchain.
You are holding funds. You are sending funds. You’re sending them to and from an exchange. And so forth.
Until 
, Ethereum was almost exclusively used to facilitate ICOs — which is speculating on the viability of tokens.
But, if we think about the future, what is the primary use-case for Ethereum? What should it be used for?
This is one of the first infographics I saw in the very early days of Ethereum and it struck a cord with me. It uses WhatsApp and a decentralized version of WhatsApp to explain the potential of Ethereum. These are the types of things that got me excited before Ethereum launched. It’s the world that the blockchain enables. It’s decentralized WhatsApp. Decentralized Twitter. Decentralized Uber.
So how do we ensure that these dapps are easily usable?
It’s easy to ask ourselves “what role does the wallet play in the decentralized future,” but we should really ask “what role does the wallet play in centralized apps?” Because if we’re going to have any chance at replacing the current apps and centralized services, it must be easy for the end user.
So, what role does the wallet play in a traditional app? Almost none. The payment portions of the app are usually small, tucked away under settings. You spend the least amount of time on any page that has to do with payment.
This is because when I go on Airbnb or Uber, I’m not opening that app with the goal of paying someone for their place or for a ride. My goal is to have a place to stay for my next conference or to get a ride from the bar to my house, and it’s easy forget that when we’re thinking about decentralized apps in this space. So much of the conversation is around money - around these new coins and tokens. The payment/money side of things, especially with the utility tokens, should be the smallest part of it.
Furthermore, when you visit Airbnb or Uber, do you place the order and then go and visit your mobile banking app to make the payment? Hell no.
Pretend that somehow magically a decentralized Airbnb on the blockchain was working today, and you see how absurd the experience would be.
Imagine this scenario:
I want to book a place for a conference I’m attending. I open up my decentralized Airbnb app. I find the place, read the reviews, and decide — yes! This is the place for me.
The dapp then tells me to get this specfic tokens, open my wallet interface, and send my tokens to the specified address…. with the specified data… and the specified gas.
I then have buy some tokens in order to pay.
And, oops, I forgot I must have ETH in my wallet to cover the cost of gas.
And, oops, I fucked up and forgot to include the data parameter with my transaction.
If I made a single mistake at any one of these points, I risk losing my money and ultimately, I wouldn’t have a place to stay for the conference.
If we have any chance at a usable decentralized future, the experience needs to be like Airbnb. I explore places. I find a place. I click a button. I am booked. That’s it.
The interaction must be infinitely more frictionless than that. It must be invisible. It must remove as many obstacles in the user’s path as possible.
So how do we do that? If we admit that a separate wallet interface is not the ideal way for users to interact with the blockchain, then what is the ideal solution?
We cannot expect every dapp to build a wallet interface / keychain into their dapp. This is a waste of time, energy, and opens up a variety of security issues.
We need an access layer that is universal and works seamlessly, with as little overhead on the end user as possible.
MetaMask, an amaaaazing project with a kickass team, has created browser extensions to handle key management and facilitate interaction with dapps.
Mist & Brave have gone the route of creating an entirely new browser.
Get Taylor Monahan’s stories in your inbox
Join Medium for free to get updates from this writer.
Remember me for faster sign in
The winning solution in the long term will likely be something even more invisible and more seamless. I think this is because the future doesn’t necessarily exist in your browser or on your computer.
We have websites and phones and computers and Xbox’s and our doorbells and our cars and even the lock on our front door. And all of these things will probably want to interact with the blockchain at some point and facilitate transactions. Everything needs to be able to utilize this access layer to seamlessly enable payments via the blockchain in a safe and secure way.
What exactly does this look like?
I’m going to be honest: I don’t know. I’ve been thinking about this a lot and there are a lot of possibilities and pros and cons and things that will change in the coming months and years that influence the technical decisions.
However, I do know that if it wins at being invisible, it won’t look like much at all. 😉
This access layer will be transparent and integratable and hide all the confusing concepts like gas and private keys and transactions from the user.
Because at the end of the day, the user doesn’t want to send tokens. The user wants to rent a place for that conference they are attending.
Press enter or click to view image in full size
I will back up for a moment because some of you are arguing with me in your heads right now and saying, “there will never not be wallets, you moron.” Yes. Okay. You win.
There will always be speculators and hodlers and traders and situations where you may need to only manage your funds. Therefore, there will probably always be an interface where you can go and just see how much money you have. It just won’t be the primary way the average user interacts with the blockchain, just like you probably don’t spend much time on your mobile banking app.
A dedicated wallet interface is not going to be such an integral part of day-to-day life tomorrow. The wallet is just going to be one itty-bitty piece of the ecosystem that serves the investors or traders or hodlers or whatever. It won’t serve the people who want to rent a place or get a ride.
So, what are we working on at MyCrypto to help usher in the decentralized future? How do we transition from being a wallet interface to being something that removes friction during the dapp experience? Great question.
Previously, I wasn’t focused on the long-term. In fact, that’s the reason why MEW succeeded so quickly — we were building shit that people needed today. But, it was purely reactionary.
As I think about what MyCrypto is going to focus on, I keep returning to this word “balance.” We want to balance security and ease-of use. We want to balance usability and trustlessness.
And we also want to balance solving the problems users have today with the problems the ecosystem is going to have tomorrow.
In the short term for MyCrypto we have a fully-audited react & typescript codebase that is going to be entering public beta in the coming weeks. This new codebase enables faster, safer development.
We have new infrastructure that reduces our overhead and costs and also sets us up to provide integral features that people really need, like a gas price oracle so the end user doesn’t have to think about it.
On the next version of MyCrypto that will be entering public beta in the next few weeks, the user no longer needs to think about gas at all. We will automatically set their gas price based on network conditions. (Of course the option remains for users to customize their settings, it’s just behind an “Advanced” button.)
These are the little items that need to be built on the backend as much as the frontend that will help us move from “wallet interface” to “invisible access layer”
We have new developer tools that automate builds because as we were building the new codebase, we realized that there were a lot of things missing that we really needed in order to do our jobs more securely and efficiently.
We have tools to verify every build of every website and app is verified by multiple parties before it goes live. This ensures everything we do and everything we publish is secure and cannot be compromised by a single party. More simply: myself nor my single computer no longer has the ability to push something live to our hundreds of thousands of users.
We have a client-side node balancer to help ensure uptime and further increase decentralization.
And we have some awesome typesafe libraries that have make our work with contracts much easier — and safer.
We have been working with the Swarm City team to build out a gas station. This is one of my favorite things in the world.
How many of you have gotten in on an ICO or bought a token or something and then when you went to send it, you couldn’t send it because you didn’t have enough ETH in your account for gas?
This gas station will enable you to send tokens, even if you don’t have ETH in your account. The transaction fee essentially will be paid in the token, rather than the ETH, via a decentralized API / smart contract.
Oh yeah….and we‘re working on new desktop and mobile apps.
Once we have more awesome tools that are cross-platform, we can start abstracting away as much as possible. This means the user doesn’t have to understand gas limit or gas price. They also don’t need to have ETH in their account in order to send tokens. They also don’t need to switch nodes if one is offline or responding slowly. It will all be automatic.
As much as we like to talk about tech & code & fancy features and tooling, the future really revolves around people. The people are what matter.
If you have a product you are building or thinking about building and it’s just in your head, or in a private repo somewhere then you aren’t necessarily building for people. That isn’t going to make the world a better place, or even a different place, and you aren’t going to learn as much as you would if you shared it and collaborated and talked about it with people.
Also, it takes all types of people — not just developers — to build the decentralized future. This movement is global.
We need people of all genders, upbringings, races, sexual orientations, everything. We need people with different experiences. We need different perspectives to solve problems more creatively.
Everyone brings something unique to the table and ensures a more powerful decentralized future. This future is not just for technical geniuses.
So my question for you today is:
What are you doing to help usher in this decentralized future?
What unique skills or experiences do you have that you can contribute to this ecosystem?
The best part about the blockchain is that everyone can contribute. It’s so new and moving so fast that anyone can create the next Facebook or Google today.
I hear “I’m not a developer” or “I’m not a blockchain expert” so often. Fuck that. No one started as a blockchain expert. I was not a blockchain expert. I’m still not an expert. I just soak in as much knowledge as possible. No one went to school for this! All it takes to be part of this world is to want to be part of this world.
Stop telling the people around you, stop telling yourself, and stop telling me all the things you can’t or don’t do and shift your thinking. What can you do? What are your experiences? What makes you unique?
If you are excited by the journey we are on, find me, find my team, find another team. Join the party.
Thank you so much to everyone for supporting us on this journey.
And thank you to Austin and Matt and the Blockchain Beach crew for putting their event on and putting us all in a room together to share awesome ideas.
-Taylor

# blog.lopp.net -- Scraped Content

**URL:** https://blog.lopp.net/lightning-network-liquidity-management-guide
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** Lightning ⚡️\Channel management guide.md, Lightning ⚡️\Liquidity management.md
**Scraped:** 2026-04-12

---

[ Cypherpunk Cogitations ](https://blog.lopp.net)

Sign in

Aug 7, 2021  23 min read  [lightning network](/tag/lightning-network/)

# Lightning Liquidity Management Guide

Lessons learned from running a routing node on the Lightning Network. 

[Jameson Lopp](/author/jameson/)

Ever since people started running Lightning nodes on mainnet in early 2018, some have asked the question: what is a reasonable ROI to expect for placing my capital in a routing node? Nik Bhatia went in depth with his theory of how this may play out:

[The Time Value of Bitcoin and LNRRA Journey from Lightning to Reserve Currency StatusMediumNik Bhatia](https://timevalueofbtc.medium.com/the-time-value-of-bitcoin-and-lnrr-e0c435931bd8?ref=blog.lopp.net)

But as we've learned over the years, there's far more to ROI than simply putting capital into Lightning channels.

> Lightning routing is a multi-faceted competitive system. It’s not just about capital, a brute force deployment of capital will cripple ROI. The system models a distributed predictive cache. Available capital is a factor but so is intelligent capital placement, reliability, speed.
> 
> — Alex Bosworth (@alexbosworth) [May 10, 2018](https://twitter.com/alexbosworth/status/994603452310278144?ref_src=twsrc%5Etfw&ref=blog.lopp.net)

In early 2021 I decided to set forth to try to determine how well I could do running a node with the goal of earning a profit by routing funds.

> If you're asking what is the ROI on a routing node, you're operating from an incorrect premise of how Lightning functions  
>   
> A billion dollars can flow over a $5 channel. Managing to place and maintain that channel where a billion dollars needs to flow is the really difficult part.
> 
> — Alex Bosworth (@alexbosworth) [February 8, 2021](https://twitter.com/alexbosworth/status/1358807809631035395?ref_src=twsrc%5Etfw&ref=blog.lopp.net)

I followed the process described in my earlier post to set up my tor-only node:

[Tor-Only Bitcoin & Lightning GuideA detailed guide to improving your privacy as a Lightning Network user.Cypherpunk CogitationsJameson Lopp](https://blog.lopp.net/tor-only-bitcoin-lightning-guide/)

Getting the software running was the easy part. Next I had to figure out how to place my capital most effectively.

### Your Mileage May Vary

Unfortunately it's not possible to write a guide that simply says "connect to these nodes and start earning fees." You have to think of the Lightning Network as a competitive market for offering efficient flow of capital. Much like with a given trading strategy, if everyone started to use the same strategy, any advantages the strategy had will disappear and it would create opportunities for others to trade against it. If everyone builds the same bridges for capital flows, it would be a race to the bottom to compete over fees and it would be smarter for other operators to "counter trade" that strategy by building bridges elsewhere.

### A Plethora of Variables

You may have noticed that this is an extremely lengthy article. That's because there are many different issues one needs to consider when operating a Lightning Network node with the goal of maximizing routing. This includes:

  * Capital Placement
  * Routing Fees
  * Minimizing on-chain fees
  * Your Total Inbound / Outbound Capacity
  * Maintaining Routing Capacity (Rebalancing / Submarine Swaps)
  * Inbound / Outbound Capacity of Peers
  * Peer Responsiveness / Uptime / Health
  * Your Node's Responsiveness / Load / Network Connectivity


### Deciding What Channels to Open

Alex Bosworth has some detailed guidance [in this document](https://github.com/alexbosworth/run-lnd/blob/master/LIQUIDITY.md?ref=blog.lopp.net).

It's simple to open Lightning channels - the vast majority of nodes on the network will accept almost any value of incoming channel. As such, it's easy to lock up capital with a poorly performing peer who does not route many payments. And if your peer becomes unresponsive, an uncooperative channel close can put your capital in limbo for weeks.

In my initial experimentation I found that some peers were simply unroutable, perhaps because they didn't have enough liquidity going to other peers. It's pretty hard to tell what a peer's status will be without probing different routes through them, which requires opening a channel first. I do expect we will see services coming online to help address this issue and offer more insight regarding the liquidity status of a given node.

Whatever you do, **avoid using lnd's autopilot** ; it just connects to large popular nodes. Similarly, it seems like a lot of folks are just going to Lightning Terminal or 1ML and connecting to the highest ranked nodes. It may be counterintuitive, but this is not a winning strategy if you want your node to route a lot of payments. Rather, you should **seek to create new bridges** by tying together peers that otherwise would have to take many hops to route to each other.

Another issue I've seen is folks using the BOS score to decide what nodes with which to open channels. Alex Bosworth, who wrote that scoring algorithm, has told me that it wasn’t designed as a routing node matching system / quality score.

I used the [node match tool](https://moneni.com/nodematch?ref=blog.lopp.net) to figure out which nodes would increase my connectivity the most. However, I'd once again caution against blindly opening channels to the ones ranked the highest. Before opening a channel with one of the recommended nodes, I check it on [Lightning Terminal](https://terminal.lightning.engineering/?ref=blog.lopp.net) to see if it's stable. Then I check it on [1ML](https://1ml.com/?ref=blog.lopp.net) to see if they are setting sane fee policies.

To get another perspective on how to increase my node's centrality, I used Gridflare's ["improve centrality" script](https://github.com/Gridflare/lndpytools/blob/main/improvecentrality.py?ref=blog.lopp.net) from [lndpytools](https://github.com/Gridflare/lndpytools?ref=blog.lopp.net). This is certainly not as user friendly as other web based tools as it requires getting a full network graph dump from your node, transferring it to your desktop / laptop, and then running the analysis on that json file.

In my experience, most of the "highly connected" nodes with 500+ channels tend to be unstable and thus don't route many payments. I suspect that they are putting too much strain on their hardware. However, others have reported a different experience - YMMV!

If you can afford it, don't create channels of < 10M sats. Keep in mind that the default max payment size is a little over 4M sats. So if you want to be able to maintain channels that can route the max payment size in either direction, you need at least double that - preferably more since it's pretty hard to have both enough inbound liquidity and enough outbound liquidity on both sides of the channel. If you're not trying to be a routing node, this doesn't matter as much. It's possible to be a high volume routing node for smaller payments with smaller channels - you'll likely need to do more rebalancing - but it's still desirable for your channel's capacity to be as high as possible.

If you can't afford 10M sats channels then I'd still suggest a **minimum of 1M sats**. My node has forwarded 400 payments over the past few months and the average amount forwarded was 420,000 sats - about $150. thus you'd need a nearly perfectly balanced 1M sat channel in order to be able to forward a single average payment. Hopefully the dynamics will change as more and more wallets start using multi-path payments.

In lnd you can prevent inbound channels below a certain size by setting this in lnd.conf: 
    
    
    minchansize=1000000
    

Not all nodes will allow you to open a channel with them, and they won't explain why they reject your channel request. For example, I tried to open a channel with a Zap node and got rejected even when I tried the max (default) channel size.

_$ lncli openchannel --node_key 03b428ba4b48b524f1fa929203ddc2f0971c2077c2b89bb5b22fd83ed82ac2f7e1 --local_amt 16000000 --sat_per_vbyte 1  
[lncli] rpc error: code = Unknown desc = received funding error from 03b428ba4b48b524f1fa929203ddc2f0971c2077c2b89bb5b22fd83ed82ac2f7e1: err=channel rejected_

Before opening a channel you should try to determine what the routing policy of the counterparty will be. For example, LNBIG has pretty high fees of 175ppm - what's the point of paying for inbound liquidity to your node if folks will avoid using it due to high fees?

Some nodes have absurdly high routing fees; for example I noticed that both OKEX and OKCoin's nodes have their base fee set to 1M satoshis - $400! I actually spoke to OKCoin's CEO about this and they said it was done by design to discourage routing; I suggested they change their configs to simply reject inbound channel opens.

### Saving On-Chain Channel Open Fees via Batch Opens

If you're starting up a fresh node for which you need to open many channels, and you're comfortable on the command line, consider batching your channel opens with the following method.

__Batch open transaction with balanceofsatoshi and Electrum Desktop. Below is a quick description of the process, but this step involves an onchain transaction and therefore possible loss of funds if_ you make a mistake _._ There is a _detailed tutorial on Jestopher's website:_ _[__http://satbase.org/bos-open/__](http://satbase.org/bos-open/?ref=blog.lopp.net)

  1. In Electrum Desktop, go to Tools > Preferences, under the 'Transactions' tab, activate 'Advance preview'. Then in Tools, open the 'Pay to many' dialog box.
  2. On your node, as a bos user, in the command line interface, enter this command: `bos open <node pubkey 1> --amount <channel size in sats 1> <pubkey 2> --amount <channel size 2> <pubkey 3> --amount <channel size 3> <pubkey 4> --amount <channel size 4> <pubkey 5> --amount <channel size 5> <pubkey 6> --amount <channel size 6>` After pressing enter, a 10 min counter will start, and you will need to do steps 3 to 5 within the 10 mins. Make sure to not use Ctrl+C once the timer has started! If you want to cancel the process and timer, just press Enter in the command line interface.
  3. Do not enter any other command in the CLI, but just copy the output of the 'bos open' command, which will be a list of onchain addresses and amount in bitcoin separated by a comma. This is a format compatible with Electrum 'pay to many' option.
  4. In Electrum, paste this list in the pay-to-many dialog box, save the transaction, click 'Pay', set a fixed fee as low as possible based upon the current conditions of the [mempool](https://mempool.space/?ref=blog.lopp.net). Make sure that RBF is NOT checked. Then click 'Finalize' and 'Sign' it using your hardware wallet (or Electrum wallet if not using a hardware wallet) but **DO NOT broadcast it!** This will be done by balanceofsatoshi.
  5. Once finalized and signed, copy the signed raw transaction and paste it in the command line interface and press 'Enter'. After a few seconds or minutes, bos will display a transaction ID. You can then use your node's own block explorer to check the status of your batch transaction.


### Opening Dual Funded Channels

If you have a friend who will cooperate with you, you can save a bit on rebalancing / looping by initializing a channel that is already balanced. Here are the steps for Alice and Bob, using the bos CLI.
    
    
    (NODE 1: Bob)
    (0) Run: bos open-balanced-channel
    (1) enter remote node public key
    (2) enter full channel size
    (3) enter fee rate
    Open a new terminal window.
    (4) Run: bos fund --fee-rate <fee> <address> <amount in sats>
    Copy the signed_transaction and go back to 1st window and paste
    (5) paste the signed_transaction to bos prompt in 1st window
    
    
    (NODE 2: Alice)
    (0) Run: bos open-balanced-channel (it should see the request from node1 at this point)
    (1) agree with funding rate (y/n)
    Open a new terminal window.
    (2) Run: bos fund --fee-rate <fee> <address> <amount>
    Copy the signed_transaction and go back to 1st window and paste
    (3) paste the signed_transaction to bos prompt in 1st window
    (4) hit enter and this should work.
    
    check via: lncli pendingchannels

### Channel Rebalancing

In some cases I was never able to rebalance a channel due to insufficient liquidity. If you notice a channel can never be rebalanced and it never gets used to route funds, you may want to consider closing it and allocating that capital elsewhere.

You should make sure it makes economic sense before rebalancing channels. Otherwise you will just get caught in a loop of constantly rebalancing channels since they will rarely stay perfectly balanced. Blindly rebalancing in the hunt for maintaining perfect balance is almost assuredly going to end up costing you more in fees than you earn from routing payments. Thankfully 'bos' has a --dryrun option to see what the fee will be.

You can use bos to auto rebalance but in order to ensure that you don't perform uneconomical rebalances is that you'd want to set the max fee rate to your minimum fee rate / 2. You can achieve it by adding this line to /etc/crontab:

*/10 * * * * jameson /path/to/bos rebalance --max-fee-rate 5

Eventually I stumbled across Carsten Otto's [rebalance-lnd tool](https://github.com/C-Otto/rebalance-lnd?ref=blog.lopp.net). I like this tool for rebalancing because it goes an extra step into determining if a given rebalance route makes economic sense. How is economic viability of a rebalance calculated?

Let's say your node has two channels for which to evaluate a rebalance; one to Bitfinex with 10M sats on your side and a 1,000 ppm fee rate. Your node also has a channel to LOOP and charges 5,000 ppm to forward funds. Sadly, your side of the channel is mostly empty.

It might be a good idea to push funds from the Bitfinex channel to the LOOP channel. If you do that for a 4M sat rebalance, this would mean:

  1. After doing a rebalance there will be 6M sats left that can be pushed to Bitfinex. You won't be able to earn the 4M * 1,000 ppm = 4,000 sats for the funds you took out of the channel as part of the rebalance to LOOP. This is the opportunity cost you have paid.
  2. You also have to pay whatever the rebalance transaction costs; this is your direct cost.
  3. If you're lucky, you get to send those 4M sat to LOOP and earn 4M * 5,000 ppm = 20,000 sat. This is your potential future earnings.


The rebalance transaction only makes economic sense if Potential Earnings - Opportunity Cost - Direct Cost > 0.

The frustrating thing I quickly discovered was... rebalancing usually isn't worth it. It seems that < 5% of my attempted rebalances end up completing with this tool.

I set a cronjob to run a random rebalance every 5 minutes by adding this line to /etc/crontab:

*/5 * * * * jameson /path/to/rebalance.py --to -1

My node has a couple dozen channels but at any given time only about 25% of them are in need of rebalancing according to the rebalance-lnd tool, which defaults to trying to keep at least 1M sats on each side of a channel. These defaults are unlikely to be optimal for your own situation. By running a random rebalance attempt every 5 minutes I expect that each channel in need of rebalancing will be attempted twice an hour.

**Warning** : _this can be costly if your channel fee rates are unrealistically high and you lower them in the future_! Make sure you understand the ramifications of automating actions that cost money.

**Pro Tip** : I learned after running rebalances every 5 minutes for a week that it filled up various dashboards with tons of unpaid expired invoices. In order to mitigate this issue, I suggest setting the following two lnd configs:
    
    
    gc-canceled-invoices-on-startup=true
    gc-canceled-invoices-on-the-fly=true
    

### Channel Policy Management

Eventually I came across [charge-lnd](https://github.com/accumulator/charge-lnd?ref=blog.lopp.net) which is a tool to automatically dynamically change routing fees on my channels. It's worth noting that this is far from a perfect tool because unfortunately we can only set outbound fees for channels. This is a limitation of the Lightning protocol rather than the tool; you can read more about the debate over supporting inbound fees [on this github issue](https://github.com/lightningnetwork/lightning-rfc/issues/835?ref=blog.lopp.net).

Initially for the first few months of operation I set all of my channel fee policies to be:
    
    
    base_fee_msat:   5000
    fee_ppm:         2000
    

These fees are an order of magnitude higher than the defaults; I just wanted to see if users on the network would bite. However, my node only sporadically routed funds with these fee levels. Presumably either my fees were too high and/or my node was not positioned well in the network graph.

Later on I set the following config for charge-lnd:
    
    
    [proportional]
    chan.min_ratio = 0
    chan.max_ratio = 1
    strategy = proportional
    base_fee_msat = 1000
    min_fee_ppm = 10
    max_fee_ppm = 2000
    

And set a cronjob to run charge-lnd hourly by adding this line to /etc/crontab:

0 * * * * jameson /path/to/charge-lnd -c /path/to/charge.config

Within 48 hours after enabling this dynamic policy management, I saw my node start routing more payments.

You shouldn't run this script more frequently than once an hour since these updates propagate relatively slowly (1 minute per hop) and if you change fees too often, the remote nodes that decide to route through you would often get `FEE_INSUFFICIENT` errors and probably blacklist your channels or node for hours. It's also desireable to reduce gossip traffic on the network.

After a couple months I still was only seeing sporadic routing so I changed my fee values to:
    
    
    min_fee_ppm = 2
    max_fee_ppm = 200
    

One thing worth noting is that using dynamic channel policy manager somewhat conflicts with the logic used by the rebalance-lnd tool - it assumes that your channel fees will remain the same for the forseeable future when it calculates the opportunity cost you're paying by moving liquidity around. For example, if rebalance -lnd is using the current fee rate of your channel to decide when to rebalance, but charge lnd is changing the fee rates around, rebalance lnd would make a decision that makes sense to it at fee rate A but then charge lnd could come along later and change to fee rate B, invalidating the logic of rebalance lnd for fee rate A. It seems like rebalance-lnd would need to also know the charge lnd config and the historical flow of funds across the channel in order to better predict future fee revenue.

### Buying Inbound Liquidity

Gaining (and maintaining) inbound liquidity is one of the biggest challenges to running a routing node.

As of July 5, 2021 the cost to purchase a max amount of inbound liquidity (16.7M sats / $5,650) for a channel via certain services is:

  * [Bitrefill](https://www.bitrefill.com/buy/lightning-channel/?ref=blog.lopp.net): 199,021 sats / $67
  * [Y'alls](https://yalls.org/about/?ref=blog.lopp.net): 150,000 sats / $50.44
  * [LNBIG](https://lnbig.com/?ref=blog.lopp.net#/open-channel): 24,101 sats / $8.30
  * [Loop](https://github.com/lightninglabs/loop?ref=blog.lopp.net): 26,165 sats / $8.81
  * [Pool](https://github.com/lightninglabs/pool?ref=blog.lopp.net): unknown (auctions are blind)


You can also use these services to open a channel and either have a reciprocated channel opened back to your or have funds returned on-chain:

  * [https://lightningconductor.net/channels](https://lightningconductor.net/channels?ref=blog.lopp.net)
  * [https://ln2me.com/](https://ln2me.com/?ref=blog.lopp.net)


Those methods require trusting the service to return funds. A solution that requires less trust is to use the bos dual-funded channel open functionality referenced earlier, though this

[... truncated at 20,000 characters ...]

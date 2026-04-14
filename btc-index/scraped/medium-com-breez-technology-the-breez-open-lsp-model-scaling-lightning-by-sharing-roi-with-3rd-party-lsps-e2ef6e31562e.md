# medium.com -- Scraped Content

**URL:** https://medium.com/breez-technology/the-breez-open-lsp-model-scaling-lightning-by-sharing-roi-with-3rd-party-lsps-e2ef6e31562e
**Category:** medium-apify
**Scrape status:** DONE
**Source notes:**
**Scraped:** 2026-04-14
**Title:** Scaling Bitcoin with the Breez Open-LSP Model | Breez
**Chars:** 9,028

---

Scaling Bitcoin with the Breez Open-LSP Model
The Breez Open-LSP Model: Scaling Lightning by Sharing ROI with 3rd-Party LSPs
“Fintech” is, obviously, short for “financial technology,” which itself is just a fancy way of saying “money and machines.” Lightning is undoubtedly fintech. It’s a way of using machines to move money.
Breez is developing Lightning as a Service (LaaS) because both of those things — machines and money — can get very arcane very quickly. We love bitcoin, we believe in Lightning, and we’re trying to make it easier for everyone to use, from consumers to entrepreneurs to developers. The two major components of LaaS aim to simplify these two complex issues: machines and money.
The first component, our Lightning SDK, is mostly focused on the machine side, i.e. getting the machines to cooperate with each other and behave themselves around humans. In this post, I’d like to tell you more about how LaaS deals with the money side by means of Lighting Service Providers (LSPs) and how these two components — money and machines, supply and demand — fit together like clockwork.
Press enter or click to view image in full size
(Image: Lucas Santos)
LSP Redux
We really hoped the concept and the term “LSP” would take off when we invented it, and it sure has. The idea is basically that connecting to the Lightning Network is more complicated than many end-users would like, so there is a niche for service providers to do things like opening channels for users, making sure they have sufficient incoming liquidity, routing payments, ensuring network connectivity, and so on.
Just like most people prefer to connect to the internet through an ISP, to whom they delegate a lot of the technical matters for a fee, many Lightning users want the same.
Generally speaking, that’s exactly what’s happened. Many Lightning payment apps have started acting as LSPs for their users, and there are also special-purpose LSPs out there too. It’s not that we have a crystal ball; we’ve just done our homework about how networks scale.
There is a wrinkle, however, in that LSPs need to provide financing in the form of inbound liquidity to their users in addition to the technical infrastructure. There aren’t enough Lightning payment apps to front the capital requirements to scale the network as fast as new users would like to join. The network needs more third-party LSPs to help carry the financial burden of rapid scaling.
A Virtuous Cycle of Supply and Demand
Thanks to our SDK, which enables developers of all kinds of apps to add Lightning payments easily, the demand is primed. The network is not only welcoming hordes of new users; it is now open to entirely new use cases.
Third-party LSPs are now required to take care of supply — making sure there is enough liquidity preloaded onto the network to accommodate all these new users and their payments. But philanthropy or the interest of devoted hobbyists is not enough. Putting money somewhere is always an investment, and those with the capital available to park tens of millions of sats on an LSP node expect a return on their investment. There’s nothing wrong with that. ROI is the incentive to scale the network, so Lightning needs an LSP model that incentivizes investors to provide the liquidity the network needs to scale.
ROI is what turns a financial burden into an opportunity.
Increasing ROI is where the SDK and third-party LSPs fit together like clockwork. Routing fees are and always have been Lightning’s monetization model. For fees to remain low, the LSPs providing the liquidity and routing the payments need volume. By making it easy for new users and apps to adopt Lightning payments, the SDK provides the volume. As more users pay for more things over Lightning, the liquidity that LSPs invest in the network gets reused to forward ever more payments, generating ever higher returns.
Lightning’s financial logic starts to look like this:
As the network’s financial capacity increases, we can onboard more users over the SDK.
More users making more payments provide more ROI.
More ROI attracts more LSPs.
More LSPs increase the network’s financial capacity.
Return to step 1.
The SDK is driving demand. LSPs are providing the supply. Economics baby!
Press enter or click to view image in full size
This logic bears a crucial implication: through LSPs, Lightning can generate yield on bitcoin holdings without transferring custody. Without staking. Nothing is being securitized (as far as I can tell), no one is holding, gambling, or losing anyone else’s money. It’s a means to generate returns on bitcoin today, not just locking it up and hoping that numbers go up. Yield with full sovereignty and full custody: this is the holy grail of crypto, not just bitcoin. (Though we’ll stick with bitcoin, thank you very much.)
Get Roy Sheinfeld’s stories in your inbox
Join Medium for free to get updates from this writer.
Remember me for faster sign in
We’ve actually run some numbers on this. We took APY as a more universal measure of ROI and looked at how it varies in relation to a variable of key importance to LSP operators: the ratio of average monthly throughput to channel size. In effect, this variable measures how often the same sats on a channel are reused to forward payments and generate fees relative to how much money the LSP operators had to invest in the channel.
As you’d expect, the relation is linear and positive: as the throughput/channel size ratio increases, so does the APY. This is perfectly logical because it means that the more the sats in a channel are reused to forward payments and generate fees, the greater the return to the operator. Huuuuuge channels are not necessarily efficient, as they can lower this ratio, but channels need a certain size to forward most payments that come their way.
The curve looks like this, and it’s beautiful:
Press enter or click to view image in full size
The Breez Open-LSP Model
There’s gold in them thar hills! APY without losing sovereignty and custody is exactly what big exchanges and neobanks would like to promise but can’t. So what’s the catch and how can we help you overcome it?
The obstacle to getting started as an LSP is, like so many things related to Lightning, the complexity. Just because someone has a few spare BTC kicking around to start an LSP doesn’t mean they have the technical expertise to open all the necessary channels to the right nodes, keep those channels balanced, find and connect users, and so on. Just as the SDK lowers the barriers for those who know apps but don’t know Lightning, the Breez open-LSP model lowers the barriers for those with BTC investment capital but don’t know Lightning.
Our vision of LaaS includes incoming LSPs as well. The Breez LSP package gives incoming LSP operators a head start on several key tasks:
Our SDK provides them with downstream users to generate the traffic they need for ROI. That takes care of demand, usage, payments: volume.
They get a channel to the Breez node, which is well connected to all the other major nodes on the network. That takes care of connectivity and managing their public channels.
They get software to run their LSP node, with all the same features we use to manage our own LSP. That takes care of actually opening channels to end users.
All the new LSPs need to contribute is their own node that’s always online with sufficient outbound liquidity (i.e. incoming liquidity for their users and outbound liquidity to the Breez node).
Press enter or click to view image in full size
Introducing Our LQwDity Provider
The Breez open-LSP model is a vital and credible component of LaaS. But of course I would say that, so don’t take my word for it. Take LQwD’s. LQwD Fintech Corp is the first third-party LSP to sign up for our program.
LQwD is a publicly traded Lightning company. As much as we love hobbyists running Lightning at home, LQwD is a company of professionals. They know finance, and they know technology. They’re experts at money and machines.
LQwD has honored our work by investing in it, and we’re going to honor their investment by building the best LSP product we can. Just as we will do for yours.
Doing Good by Doing Well
A lot of popular discourse seems to assume that you can either prosper or care about the world around you, but not both. As if helping people requires that we all wear sackcloth and exploitation were the only way to make money.
Our open-LSP model shows that this is a false dichotomy. Bitcoin is good for people. Lightning is the way to make bitcoin the universal mainstream currency it was designed to be. This is how we’re going to bring open financial services to everyone. And we’re scaling Lightning by inviting people to participate and share in the gains.
LaaS, with an open-LSP model, will accelerate the growth of this liberating network. It will do so without taking custody of anyone’s money, and it will share the returns that result. Bitcoin makes the world better, Lightning makes bitcoin better, and LaaS makes Lightning better.

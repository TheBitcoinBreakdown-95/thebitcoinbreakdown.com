# github.com -- Scraped Content

**URL:** https://github.com/bitcoin-cap/bcap
**Category:** github
**Scrape status:** DONE
**Source notes:** BTC\Soft forks and activation methods.md
**Scraped:** 2026-04-12

---

**Repository:** bitcoin-cap/bcap

# Analyzing Bitcoin Consensus: Risks in Protocol Upgrades

Original Authors (V1): Ren Crypto Fish, Steve Lee, Lyn Alden

Thank you to the following people who reviewed drafts of the initial project, providing valuable feedback to improve the quality of the project:

Mat Balez, Jay Beddict, Jeff Booth, Joe Carlasare, Hong Fang, David Harding, Avichal Garg, Gwart, Chaitanya Jain, Shirish Jajodia, Hong Kim, David King, Jameson Lopp, Shehzan Maredia, Sanjay Mavinkurve, Murch, Matt Odell, John Pfeffer, Reardencode, Bradley Rettler, Rijndael, Pierre Rochard, AJ Towns, 0xkrane, jesmros

# Table of contents

- [Introduction](#introduction)
- [What is Bitcoin Consensus](#what-is-bitcoin-consensus)
	- [Technical Aspects of Consensus](#technical-aspects-of-consensus)
	- [How are changes activated](#how-are-changes-activated)
    	- [Soft Forks vs Hard Forks](#soft-forks-vs-hard-forks)
    	- [Historical Activation Mechanisms](#historical-activation-mechanisms)
- [What maintains Bitcoin Consensus](#what-maintains-bitcoin-consensus)
	- [State of Mind](#state-of-mind)
	- [Stakeholders](#stakeholders)
		- [Economic Nodes](#economic-nodes)
		- [Investors](#investors)
		- [Media Influencers](#media-influencers)
		- [Miners](#miners)
		- [Protocol Developers](#protocol-developers)
		- [Users and Application Developers](#users-and-application-developers)
	- [Consensus Game Theory](#consensus-game-theory)
		- [How is Consensus Change attained](#how-is-consensus-change-attained)
		- [Stakeholder powers during a consensus change](#stakeholder-powers-during-a-consensus-change)
	- [How to measure Consensus](#how-to-measure-consensus)
	- [Future Scenarios and Considerations](#future-scenarios-and-considerations)
		- [Consensus changes with alternative clients](#consensus-changes-with-alternative-clients)
		- [What is a chain split](#what-is-a-chain-split)
- [Recommendations](#recommendations)
	- [Proposals Maturing Toward Possible Consensus](#proposals-maturing-toward-possible-consensus)
	- [Key Questions for Stakeholders](#key-questions-for-stakeholders)
	- [Determining Consensus](#determining-consensus)
- [Appendix](#appendix)
  
# Introduction

This paper provides an analysis of bitcoin’s consensus mechanism, focusing on the roles of various stakeholders, their powers, and the incentives that guide their actions. Bitcoin is incredibly difficult to change by design. The default is no change. Any significant change needs to pass that hurdle. We categorize the roles people play in bitcoin's consensus into [six distinct stakeholder groups](#stakeholders), each with their own motivations and influence. We also notice that the relative powers of the stakeholders shift depending on their role in the network’s operation and the stage of the consensus change process. Notably, while [Bitcoin Core maintainers](#protocol-developers) do not have excessive power to change Bitcoin, they possess significant power to veto changes. We also introduce the concept of [State of Mind](#state-of-mind), which affects the degree that stakeholders engage in the process of finding consensus.

Historically, changes to Bitcoin's consensus have typically followed a smooth path. However, it is essential to thoroughly explore and understand potential future scenarios that may be more contentious and could lead to a fragile network. This paper presents [a novel analysis](#consensus-changes-with-alternative-clients) of the challenges and risks associated with adopting alternative clients. Although alternative clients are an important option, their adoption is difficult to achieve. Soft fork consensus changes can be partially deployed without full consensus, creating a fragile network prone to forks with [uncertain outcomes](#upgrade-paths-with-alternative-consensus-clients). During a soft fork, investors also have less power than other stakeholders. We highlight the [risks of bounty claims](#how-might-this-occur-with-a-soft-fork) in contentious consensus change scenarios involving alternative clients, which increase chain split risks.

In the event of a hard fork, we observe that [not all Investors are equal](#what-happens-after-a-chain-split) when it comes to price discovery. Large investor segments may react more slowly, if at all, compared to nimble, self-custodying Investors. Since many Investors do not run nodes themselves, their influence is diminished until a chain split occurs or a futures market develops. Additionally, a stakeholder’s awareness and engagement impact their influence on bitcoin’s consensus; possessing power is ineffective if one is unaware or apathetic.

By examining [past consensus upgrades](#segwit) and [future scenarios](#future-scenarios-and-considerations), taking into account the game theory surrounding stakeholder involvement — we aim to enhance understanding of how bitcoin’s consensus is maintained, how it can be changed, and the risks associated with protocol upgrades. Our goal is to equip stakeholders with the tools and frameworks needed to assess and contribute to the evolution of bitcoin’s consensus effectively. We offer [recommendations](#recommendations) for stakeholders on evaluating proposed changes, including identifying proposals that are maturing toward consensus, asking critical questions about their benefits and potential risks, and determining whether a change has broad support.

# What is Bitcoin Consensus

Bitcoin consensus refers to the set of rules that define the validity of transactions and blocks. These rules are encoded in software run by and enforced by the network’s nodes, ensuring that all participants agree on the blockchain’s transaction history.

## Technical Aspects of Consensus

Important aspects of bitcoin’s technical consensus include:

1. Block Validation: Define what constitutes a valid block, including aspects like block size, block header, transaction structure, and proof-of-work requirements.
2. Transaction Validation: How transactions should be structured and what makes them valid, including rules about inputs and outputs, signatures, and script execution.
3. Chain Selection: Determine which chain is considered the canonical bitcoin blockchain in case of forks, typically based on the valid chain with the most accumulated proof-of-work.

Understanding the technical aspects of consensus is important because any changes to the client software that change these technical aspects of consensus result in either a soft fork or hard fork (described in greater depth below) and the nodes on the network may be required to upgrade and adopt newer versions of the client. For example, new opcodes introduced require a soft fork or hard fork because they affect script execution, making scripts that completed successfully before the fork now terminate in failure (in the case of a soft fork), or vice versa (in the case of a hard fork).

## How are changes activated

### Soft Forks vs Hard Forks

Soft forks and hard forks are two types of protocol changes in blockchain networks like bitcoin. Soft forks are backwards-compatible upgrades where old nodes still see new blocks as valid, though they may miss out on new features. They only tighten or add rules to the existing protocol and can be activated with consensus from the network. Furthermore, for soft forks, only the nodes that want to use the newly proposed rules have to upgrade. Soft forks are generally preferred in bitcoin due to being a more pragmatic coordination solution as the window of time for Economic Nodes to upgrade can be quite lengthy. Examples include segwit and P2SH. However, they can create two classes of nodes, upgraded and non-upgraded nodes. The median time for a bitcoin node to upgrade has historically been ~40 weeks, but that has been trending even longer in recent years.

![bitcoin_core_upgrade_time](img/bitcoin_core_upgrade_time.png) [^1]

Hard forks, on the other hand, are non-backwards-compatible upgrades requiring all nodes to upgrade within an activation window of time with code that activates at the same block height to maintain consensus. They can change or relax existing rules, allowing for more extensive protocol modifications. Hard forks need near-universal consensus to avoid permanent chain splits and are more difficult to coordinate. Hard forks do not necessarily create a separate chain if all existing nodes on the network use the hard fork or if Miners do not continue mining the previous rule set. For example, the addition of OP_NOP in 2010 was done with a hard fork on bitcoin. While they can fix fundamental issues or add significant new features, they carry a higher risk of community divisions and network splits. Notable examples include the Bitcoin Cash hard fork in 2017, where a proposal to increase the block size limit led to disagreements within the Bitcoin community, resulting in a contentious hard fork and the creation of a new coin. This illustrates the risks of chain splits and network fragmentation inherent in hard forks.

### Historical Activation Mechanisms

Activation mechanisms refer to the processes through which upgrades are rolled out on the bitcoin network. As bitcoin has grown, so too have the number of stakeholders and the complexity of coordinating network-wide upgrades. The activation mechanisms themselves have evolved to address these growing challenges, each offering distinct trade-offs in terms of security, flexibility, and consensus-building. Below, we explore the key activation mechanisms that have been used historically.

#### Flag Day

A Flag Day activation is one of the earliest and simplest methods used for upgrading the bitcoin network. It involves setting a specific future date or block height at which the new rules automatically come into effect. This method does not rely on any form of signaling; instead, it mandates that all nodes must be upgraded by a certain point in time.

Advantages:

- Simplicity: Easy to implement and understand, with a clear deadline for all participants.
- Predictability: Ensures a fixed timeline for the upgrade, reducing uncertainty about when the change will occur.

Risks and Considerations:

- Risk of Chain Splits: If a significant portion of the network fails to upgrade by the Flag Day, it can lead to the creation of incompatible chains.
- Lack of Flexibility: There is no built-in mechanism to gauge network readiness or adjust the timeline, which can force through an upgrade even if consensus is not fully achieved.

Early proposals such as BIP16 Pay to Script Hash (P2SH) used a predetermined Flag Day to activate on the network.[^2] P2SH was activated on April 1, 2012 at block 173,805. Following the activation there were reports that some Miners who failed to update from 0.6.0 rc1 were stuck at block 170,060.[^3]

#### IsSuperMajority (BIP34) and Version Bits (BIP9)

BIP34 introduced an upgrade path for versioned transactions and blocks. Miners would increment their version number in the block header to activate the upgrade. Once 75% of the last 1000 blocks had the upgraded version 2 number, invalid version 2 blocks were rejected. Once 95% of the last 1000 blocks were version 2 or greater, all version 1 blocks would be rejected. This mechanism would allow the network to more gradually upgrade. CheckLockTimeVerify (BIP65) and Strict DER Signatures (BIP66) were successfully activated with BIP34. The activations with BIP34 at the time had short grace periods for nodes on the network to upgrade.

BIP9 followed BIP34 and introduced the ability for Miners to signal readiness for multiple upgrades with version bits in the block header. Similar to BIP34, upgrades on the network would only lock in and activate if a certain hashrate threshold is reached before nodes begin enforcing the new rules, often with a long grace period that allows nodes on the network to upgrade. If the threshold was not reached, then the activation would not occur.

The key difference between IsSuperMajority (BIP34) and Version Bits (BIP9) is that ISM would invalidate previous version blocks past the 95% threshold. This essentially guaranteed to fork-off the last 5% of the miners to upgrade. This was fixed with BIP9 by removing the requirement for miner signaling past a certain threshold.

CheckSequenceVerify (BIP68, BIP112, BIP113) was activated successfully with version bits signaling at a 95% threshold with a 2 week grace period after the hashrate threshold was reached for nodes on the network to upgrade.

Segwit (BIP141, BIP143, BIP147) was also activated successfully with version bits signaling with a 95% threshold, but it highlighted some of the risks with miner activated soft forks.

Advantages:

- Flexibility: Can handle multiple upgrades simultaneously.
- Miner coordination: Allows Miners to signal readiness.
- Grace period: Provides time for the network to prepare after the signaling threshold is met.
- Speed: Allows for faster deployments, a principled approach to a flag day would require the flag day to be set much longer in the future to minimize disruption.

Risks and Considerations:

- Potential for miner veto and stalling: If Miners do not signal, the upgrade cannot activate.
- Complexity: More complex to implement and understand than flag day.
- Potential for false signaling: Miners could signal readiness without actually upgrading their software, creating risk of chain reorgs and network disruption.
- Lack of user input: The mechanism does not directly account for the preferences of non-mining full nodes and other network participants.

The experiences with BIP34 and BIP9 activations, particularly the challenges faced during the segwit activation, led to further refinements in activation mechanisms. These lessons influenced the development of subsequent proposals like BIP8 and the concept of User Activated Soft Forks (UASF), which aim to address some of the limitations of purely miner-driven activation processes.

#### User Activated Soft Forks (BIP8) and User Resisted Soft Forks

BIP8 was proposed as an evolution of BIP9, addressing some of its limitations, particularly the potential for miner-driven activation vetoes. Although largely similar to BIP9, BIP8 includes a crucial option to set "lockinontimeout" (LOT) to True, in which case blocks are required to signal in the final period, ensuring the soft fork has locked in by the timeout height.

Advantages:

- Prevents Miner Veto: With LOT=true, Miners cannot indefinitely block an upgrade.
- Flexibility: Can be configured to behave like BIP9 (with LOT=false) or to guarantee activation (with LOT=true).

Risks and Considerations:

- Potential for Chain Splits: If there is significant disagreement, especially with LOT=true, it could lead to a chain split.
- Likely Chain Reorgs: The required signaling approach at the end of the period guarantees that, if the BIP8 specific logic is reached, unupgraded nodes are exposed to chain reorgs, potentially losing funds due to double-spends.
- Complexity: Requires careful coordination and communication to ensure network-wide understanding and readiness.
- Pressure on Miners: LOT=true could be seen as coercive towards Miners, potentially creating tension in the ecosystem.

Although BIP8 has never been implemented as an activation mechanism in Bitcoin Core, versions of User Activated Soft Forks (UASF) have been implemented in an alternative client such as for activation of segwit and taproot. There is substantial debate over the value of BIP8.

The mirror of a User Activated Soft Fork is a User Resisted Soft Fork (URSF). In a UASF, blocks that do not signal for a soft fork are rejected, in a URSF, blocks that do signal for a soft fork are rejected. As the miner signaling threshold approaches, the URSF will reject the last block prior to the signaling threshold being hit and cause a chain split.[^4] The concept of URSF first arose surrounding discussions of BIP-119 (CTV).[^5]

# What maintains Bitcoin Consensus

In bitcoin, each major stakeholder group possesses certain powers and is driven by a set of incentives that shape how they are likely to wield those powers. Entities may belong to multiple stakeholder groups, leading them to exercise various powers and navigate a mix of potentially competing incentives. For instance, a wealthy investor might also be a large influencer, or a business could operate an Economic Node, engage in mining, employ Protocol Developers, and have media influence. Additionally, entities can sometimes act against their typical group incentives for ideological or other reasons, meaning incentive descriptions apply to the average group, but allow for individual variance. When assessing whether groups should be classified together or separately in terms of their impact on consensus, it is important to consider whether their incentives and powers are meaningfully similar. If both aspects align, they can be treated as the same group for consensus purposes; if they differ, they should be regarded as distinct.

## State of Mind

There are different states of minds (SOM) the different stakeholders might be in towards a given proposal for a protocol change that affects the degree that stakeholders engage in the process of finding consensus.

1. SOM1: Passionate advocate for a change
2. SOM2: Supportive of a change
3. SOM3: Apathetic or undecided
4. SOM4: Unaware
5. SOM5: Not supportive, but not to a degree to spend time, money, resources toward fighting it
6. SOM6: Passionately against a change and willing to expend resources and exercise power to fight it

Most of the time, the majority of stakeholders are likely apathetic or unaware of changes unless they are actively contributing to protocol code or building a product that is dependent on a consensus change. It is therefore important in consensus changes for all stakeholders to form an opinion ahead of the actual consensus change, moving away from apathetic and unaware (SOM3, SOM4) to either being supportive or not supportive of a change (SOM1, SOM2, SOM5, SOM6). It is only when stakeholders are engaged that it is possible to reach consensus without whiplash that might result from regret of not participating. If stakeholders remain apathetic or unaware of changes, the risk is that new precedents may be set without their input or their apathy delays the consensus process. Future changes might then build on these precedents, and by the time stakeholders re-engage, they could find that bitcoin has evolved into something very different from what they initially supported.

## Stakeholders

### Economic Nodes

Economic Nodes play a critical role in bitcoin's consensus mechanism. Economic Nodes are full nodes that not only validate and relay transactions, but also receive and send substantial amounts of bitcoin payments. These nodes are distinct from nodes just validating blocks and transactions. These Economic Nodes are typically operated by businesses and institutions that handle significant volumes of bitcoin transactions and often serve as bridges between the bitcoin network and the traditional financial system (providing a venue to swap BTC for fiat currencies or other cryptocurrencies).

Economic Nodes, or nodes that regularly receive bitcoin, have power and influence which is proportional to the frequency and volume of payments received. For example, a high volume exchange has power in that if their nodes reject blocks mined by Miners, it would devalue the chain that Miners are building upon.

They include:

- Cryptocurrency exchanges
- Payment processors
- Custody providers
- Large merchants and service providers who accept Bitcoin as payment
- RPC providers (manage and host nodes for application developers)

Powers:

- Ability to define which fork is bitcoin by choosing which version of the software to run and set ticker symbols.
- Reject blocks they consider invalid, potentially causing chain splits.
- Ability to list or not list markets for spot and derivative markets for forks.
- Ability to sell fork coins on behalf of users without their permission.

Incentives:

- Maximize transaction volume and trading activity.
- Maintain the security and stability of the network.
- Comply with regulatory requirements in their jurisdictions.
- May have equity investments in bitcoin businesses.

### Investors

Although Investors do not tend to play a role in the day to day operations of bitcoin, they impact the price of bitcoin by buying or selling. Investors tend to have a thesis for why they hold bitcoin, thus changes in bitcoin consensus that affect their thesis can positively or negatively affect the price of bitcoin and consequently the incentives to Miners for the amount of hashrate security the network has. However, bitcoin's price also has broader implications beyond mining. It can drive venture capital funding for new businesses, affect funding for open-source developers working on software related to bitcoin, and stimulate overall investment, leading to innovation in products and services. Thus, the price of bitcoin not only influences network security, but also shapes the development and expansion of the entire ecosystem.

They include:

- Large individual holders of bitcoin
- Active and passive institutional fund holders of bitcoin
- Sovereign wealth funds, central banks, and governments

Powers:

- Influence market prices through buying and selling activity.
- Signal preferences for different proposals through futures markets (which could in turn affect choices of Economic Nodes).
- Fund development efforts or advocacy for specific changes.

Incentives:

- Maximize the value of their bitcoin holdings.
- Maintain or improve bitcoin's properties as a store of value.
- Minimize risks of network instability or contentious changes.
- Comply with regulatory requirements in their jurisdictions.

Investor groups differ in their agility and capacity to influence consensus changes, largely due to variations in their legal frameworks and custodial setups. These differences make it important to distinguish between several key investor categories.

| Segment of investor                   | Custody                                     | Control and ownership structure                                | Ability to act quickly |
| ------------------------------------- | ------------------------------------------- | -------------------------------------------------------------- | ---------------------- |
| Self custody, proprietary owner       | Self                                        | Self                                                           | High                   |
| Institutional Investors               | Qualified custodian, often an Economic Node | General partners and limited partners                          | Medium                 |
| Corporation with BTC on balance sheet | Qualified custodian, often an Economic Node | Board of directors and shareholders                            | Low - Medium           |
| Exchange traded funds                 | Qualified custodian, often an Economic Node | ETF Sponsor/Portfolio Manager and Executives of the ETF Issuer | Low - Medium           |

Self custodying proprietary owners of bitcoin can respond the fastest in consensus changes because they control the private keys to bitcoin and do not have to seek approval from anyone. They have the ability to immediately respond to contentious consensus changes by selling hard forks of bitcoin for example.

Institutional Investors often use qualified custodians (who are also often Economic Nodes) to custody bitcoin and are somewhat at the mercy of the Economic Nodes in forks. For instance, Coinbase’s User Agreement says that “Coinbase has no responsibility to support new Digital Asset forks” and “Coinbase has no liability for any losses related to supplemental protocols” including forked protocols.[^6] They are also subject to investor agreement terms which in cases may limit their ability to buy or sell hard forks of bitcoin.

Corporations with bitcoin on their balance sheet also tend to use qualified custodians and if publicly traded are held to high regulatory scrutiny for treasury assets. Publicly traded corporations, especially those listed on major stock exchanges, are subject to stringent regulatory scrutiny regarding how they manage their treasury assets, including bitcoin. They also have a fiduciary duty to act in the best interest of their shareholders. Decisions made in a contentious consensus change likely requires board of director approval.

Exchange traded funds (ETFs) are operated by a sponsor (a financial institution or company responsible for creating, managing, and overseeing the ETF) and hold bitcoin in qualified custodians on behalf of their shareholders. With respect to consensus changes, the prospectus of BlackRock’s Bitcoin ETF (the largest ETF at the time of writing) says it will “use its sole discretion to determine, in good faith, which peer-to-peer network, among a group of incompatible forks of the Bitcoin network.” Furthermore, “the Sponsor may also disagree with Shareholders, the Bitcoin Custodian, other service providers, the Index Administrator, cryptocurrency platforms, or other market participants on what is generally accepted as bitcoin and should therefore be considered “bitcoin” for the Trust’s purposes.” “With respect to a fork, airdrop or similar event, the Sponsor will cause the Trust to irrevocably abandon the Incidental Rights and any IR Virtual Currency associated with such event.”[^7] This suggests that in the case of a contentious consensus change, ETF sponsors have the ability to choose the fork they think is bitcoin and will abandon the incidental rights or coins that might arise from hard forks, but how this actually plays out in practice is unknown territory.

### Media Influencers

Media Influencers play a crucial role in shaping public perception, disseminating information, and facilitating discussions within the bitcoin ecosystem. Their influence can significantly impact the direction of consensus decisions by swaying public opinion and amplifying certain narratives that in turn can affect the decision making process of other stakeholder groups.

They include:

- Media and press organizations
- Thought leaders with large followings on social media platforms
- Organizers of conferences related to bitcoin
- Platform moderators
- Bot farms

Powers:

- Shape narratives around bitcoin and proposed changes.
- Distort the perceived support level of a consensus change (either aggrandizing or minimizing) relative to reality.
- Amplify or critique various stakeholder positions.
- Censor various stakeholder positions on centralized platforms.
- Educate the broader public about bitcoin developments.

Incentives:

- Generate engagement and grow their audience.
- Maintain credibility within the bitcoin community.[^8]
- Act in their sponsors best interest.
- Often have their own ideological or economic stakes in bitcoin's direction; may fall into one of the other Stakeholder categories.

### Miners

Miners are individuals or organizations that use specialized hardware to find a block template and nonce that in combination produce a hash that is less than or equal to the network’s difficulty target. Miners also historically have signaled readiness for consensus upgrades that help other stakeholders determine that it is safer for users to use new upgrades, but does not provide a guarantee because the signaling can be spoofed.

They include:

- Individual Miners
- Large Scale Mining Operations
- Mining Pools
- Chip Manufacturers

Powers:

- Create new blocks, determining which transactions are included.
- Signal readiness for protocol changes through version bits.
- Potentially censor transactions by not including them in blocks.
- Direct hash power to compete for chains in the event of a fork. Each ASIC mining chip can only mine for one side of a fork.[^9]

In the current environment, Miners rarely run bitcoin software to construct block templates and thus do not directly control which consensus rules to follow, only a handful of pools do. However, the switching costs are low for a miner to switch to another pool. So if a pool acts against the interests of a miner, they will lose customers. The Miner’s state of mind (SOM) matters, if the miner is unaware or apathetic (SOM3, SOM4) then they might not even be aware it is in their interest to switch pools. 

The current segmentation of Miners power is detailed below

| Segment of Miner                      | Create new blocks                           | Signal readiness for protocol changes                          | Censor transactions      | Direct hash power to competing chain |
| ------------------------------------- | ------------------------------------------- | -------------------------------------------------------------- | ------------------------ | ------------------------------------ |
| Individual Miners                     | Possible, if solo mining                    | Possible, if solo mining                                       | Possible, if solo mining | Yes                                  |
| Large Scale Miners                    | No                                          | No                                                             | No                       | Yes                                  |
| Mining Pools                          | Yes                                         | Yes                                                            | Yes                      | No                                   |
| Chip Manufacturers                    | No                                          | No                                                             | No                       | No                                   |

In the future, we may see a shift toward Miners running bitcoin software and directly controlling transaction selection and choosing consensus rules with protocols such as Stratum v2, DATUM, and Braidpool.[^10] [^11]

[... truncated ...]

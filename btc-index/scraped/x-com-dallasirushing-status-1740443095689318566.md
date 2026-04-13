# x.com -- Scraped Content

**URL:** https://x.com/dallasirushing/status/1740443095689318566
**Category:** tweet
**Scrape status:** DONE
**Source notes:** BTC\CovenantsTimeout treesCTV.md
**Scraped:** 2026-04-12

---

**@dallasirushing** (Dallas Rushing)

What is #CTV BIP 119 (covenants)?

CTV = CHECKTEMPLATEVERIFY

It enables users to set conditions/rules for how their Bitcoins can be spent in the future.

-------------------------

What problem does this solve?
As Bitcoin grows and transaction fees increase, more users will need to transact on other layers like Lightning to be able to use their BTC as money.

An essential aspect of #Bitcoin is being able to hold your own keys so that only you, can spend your money.

The reality is, self custodial lightning can NOT scale to billions of users in its current form. 

There's not enough block space on-chain for everyone in the world to have a UTXO if they wanted to.

The solution is to enable the ability to share UTXOs, with your ownership being secured by your private key.

-------------------------

What issues exist with lightning and side chains?

Self-Custodial Lightning:
- High L1 fees = high open/close channel fees
- Onboarding requires an on-chain transaction
- Increasing liquidity requires an on-chain transaction

Custodial Lightning Wallets:
- Users can get rugged by custodians
- Custodians can be hacked/targeted
- Legal risks for the custodian
- It's up to the custodian to let you use your money

Liquid/Fedimint issues:
- Funds are controlled by a multi-sig
- Multi-sig members could rug users
- Multi-sig members could be targeted
- Multi-sig members have legal risk

Summary: These options to transact beyond on-chain BTC, are custodial or have massive friction in high-fee environments.

-------------------------

What are the use cases enabled by CTV?

1. Lightning becomes >100x more scalable
- Resize channels off-chain
- Improves lightning liquidity efficiency
- Batched channel openings: open multiple channels in a single transaction. It's like carpooling and everyone still gets to keep their money in their pocket.

Additionally, anyone can leave the channel/UTXO with their money whenever they want and not affect others.

2. Vaults with enhanced security
- Set a max daily spend limit on your wallet and add a recovery address to withdraw your money to, if your private keys get compromised.
- This would limit the loss of what an attacker could take and give you the ability to move your funds to safety.

3. Inheritance vaults
- Imagine you have your life savings in cold storage. You can create rules to say, if I don't interact with this wallet in 12 months, start sending a % each month to my spouse, child or friends wallet.
- The people you want to give your inheritance to, don't have to have your keys or understand your setup to be able inherit your wealth.

4. Makes mining more decentralized
- Removes custodians from miner payouts
- Enable miner payouts to be instant
- This is like setting a multi-destination autopay that activates the moment a block is found to distribute miner rewards.

Potentially, many more use cases can be built with CTV. 

I've yet to hear a compelling argument against #BIP119

This is the most important improvement that we can make for #Bitcoin that would safely add immense value for users.

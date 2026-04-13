# en.bitcoin.it -- Scraped Content

**URL:** https://en.bitcoin.it/wiki/Pay_to_script_hash
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\Full list of Bitcoin address prefixes.md
**Scraped:** 2026-04-12

---

# Pay to script hash

From Bitcoin Wiki

Jump to navigation Jump to search

Pay to Script Hash

**BIP number**| [BIP 16](/wiki/BIP_0016 "BIP 0016")  
---|---  
**Type**|  Miner-activated softfork  
**Purpose**|  Allow the recipient of a transaction to specify the redeem script instead of the sender  
** Deployment  **  
**[CB signature](/wiki/Coinbase "Coinbase")**|  /P2SH/  
**Starttime**|  2012-03-08 00:00:00  
**Timeout**|  2012-03-15 00:00:00  
**Supermajority**|  55%  
**Activated**|  Block #173805  
2012-04-01 00:00:00  
  
**Pay to script hash** (P2SH) transactions were standardised in [BIP 16](/wiki/BIP_0016 "BIP 0016"). They allow transactions to be sent to a script hash ([address](/wiki/Address "Address") starting with 3) instead of a public key hash (addresses starting with 1). To spend bitcoins sent via P2SH, the recipient must provide a [script](/wiki/Script "Script") matching the script hash and data which makes the script evaluate to true. 

Using P2SH, you can send bitcoins to an address that is secured in various unusual ways without knowing anything about the details of how the security is set up. You just send bitcoins to the ~34-character P2SH address. The recipient might need the signatures of several people to spend these bitcoins, or a password might be required, or the requirements could be completely unique. 

## Contents

  * 1 Addresses
  * 2 Example
  * 3 History
  * 4 References


## Addresses

[BIP 13](/wiki/BIP_0013 "BIP 0013") specifies the address format. Bitcoin P2SH addresses always start with `3`. 

## Example

Transaction 40eee3ae1760e3a8532263678cdf64569e6ad06abc133af64f735e52562bccc8 paid to P2SH address 3P14159f73E4gFr7JterCCQh9QjiTjiZrG. You can see the redeem script in transaction 7edb32d4ffd7a385b763c7a8e56b6358bcd729e747290624e18acdbe6209fc45 which spends that output, using `OP_FALSE <sig> { OP_1 <pubkey> OP_1 OP_CHECKMULTISIG }`. 

## History

The first activation window failed and another was set to be active on 1 April 2012, in v0.6.0rc2[1]. Users running v0.6.0rc1 who did not upgrade for the delay, activated early and got stuck on block 170,060[2] when an invalid transaction according to their nodes was mined. Later soft fork activation techniques, such as [BIP 34](/wiki/BIP_0034 "BIP 0034") and [BIP 9](/wiki/BIP_0009 "BIP 0009"), reflect on block history to determine activation (also from miner signaling) in order to prevent this problem. 

After activation problems were then caused by the remaining 45% of miners producing invalid blocks for several months[3]. Later soft fork activation techniques raised the signaling enforcement threshold from 55% to 95% in order to mitigate this problem. 

Testnet activated following its first window, which was two weeks earlier than the first (failed) mainnet window[4]. 

342ftSRCvFHfCeFFBuz4xwbeqnDw6BGUey is a Bitcoin [address](/wiki/Address "Address") notable for being the first [P2SH](/wiki/P2SH "P2SH")-compatible address receiving bitcoins on the production network. Its payment was mined in [block](/wiki/Block "Block") 160720; note that it was spent prior to the enforcement of [BIP 16](/wiki/BIP_0016 "BIP 0016"), so it's not a good example to understand P2SH. 

## References

  1. ↑ [Move BIP16 switchover time to April 1 (gavinandresen)](https://github.com/bitcoin/bitcoin/commit/46aa2a6bdd5ec512dd2e364b298e6e73c3e61354)
  2. ↑ [bitcointalk topic 63165](https://bitcointalk.org/index.php?topic=63165.msg788832#msg788832)
  3. ↑ [A Complete History of Bitcoin’s Consensus Forks](https://blog.bitmex.com/bitcoins-consensus-forks/)
  4. ↑ [Remove -bip16 and -paytoscripthashtime command-line arguments (gavinandresen)](https://github.com/bitcoin/bitcoin/commit/8f188ece3c82c4cf5d52a3363e7643c23169c0ff)


Retrieved from "[https://en.bitcoin.it/w/index.php?title=Pay_to_script_hash&oldid=64705](https://en.bitcoin.it/w/index.php?title=Pay_to_script_hash&oldid=64705)"

[Category](/wiki/Special:Categories "Special:Categories"): 

  * [Miner-activated softforks](/w/index.php?title=Category:Miner-activated_softforks&action=edit&redlink=1 "Category:Miner-activated softforks \(page does not exist\)")


## Navigation menu

### Search

[](/wiki/Main_Page "Visit the main page")

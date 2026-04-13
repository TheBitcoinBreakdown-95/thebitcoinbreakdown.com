# twitter.com -- Scraped Content

**URL:** https://twitter.com/cryptoquick/status/1700455402784043012
**Category:** tweet
**Scrape status:** DONE
**Source notes:** BTC\RGB.md
**Scraped:** 2026-04-12

---

**@cryptoquick** (Hunter Beast 🕯️)

Some additional observations:
- CSV essentially puts what is usually done in blockchain nodes into the wallet itself
- RGB wallets and contracts are cold and noncustodial, and use ordinary wallet keys
- RGB contracts can't hold bitcoin themselves, at least not yet. Think of them more like metadata about a UTXO, like, "This UTXO commits to data for an account. This account has 20 CATO and 10 PUPR coins. This account can also vote on PETDAO and their name is PurrPuppy89". This metadata can change according to specific consensus rules set within the contract that can be proven to be valid as the metadata is moved from one UTXO to another as the owned data is modified.
- RGB contracts have this concept of "global data"; it's not quite global in the blockchain sense, but it's more like, data that can be shared publicly, and it's immutable and defined at the time of contract creation. For RGB20, this would be supply (21,000,000), precision (8), ticker (BTC), description, (Bitcoin), timestamp, (1/3/2009), etc.
- RGB contracts also have the concept of "owned data", and this a reference to how RGB abstracts ownership from accounts. Owned fields are mutable, unlike global fields, and only by their owner. They can mutate any kind of data, not just account balance, and are tied to a specific UTXO single use seal.
- In some ways, this kind of makes a sidechain of a UTXO, capable of storing over 250,000 different contracts, and one UTXO corresponds to one user account.
- A single Bitcoin block would be sufficient to hold every Ethereum contract ever created.

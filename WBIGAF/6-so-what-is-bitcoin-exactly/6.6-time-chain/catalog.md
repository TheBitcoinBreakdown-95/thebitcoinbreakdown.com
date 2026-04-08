# 6.6 Time Chain -- Source Inventory

> **Pipeline step:** Step 1 -- Triage COMPLETE
> **Source file:** `Time chain.md` (read-only, ~180 words)
> **Scope:** Explains how Bitcoin solved the problem of establishing canonical ordering of transactions without a trusted central coordinator -- by re-inventing time itself through blocks rather than seconds, functioning as a decentralized timestamp server.
> **Orphans imported:** None

---

## Part 2: Source Inventory

### The Problem of Time and Ordering Without a Trusted Party

1. Without a central authority (like a bank), determining who transacted first among hundreds or thousands of coordinating and potentially untrusting parties is an unsolved problem. (Dergigi / bitcoin-is-time)
2. Some people trying to cheat could set their clocks back so it looks like they spent money earlier -- time manipulation is a real attack vector. (Dergigi / bitcoin-is-time)
3. "A time-related tool [is] needed to establish a canonical ordering and to enforce a unique history in the absence of any central coordinator." (Giacomo Zucco, *Discovering Bitcoin*, 2019)
4. This problem is precisely why all previous attempts at digital cash required a centralized registry -- you always had to trust someone to correctly identify the order of things. (Dergigi / bitcoin-is-time)
5. A centralized party was required to keep the time. (Dergigi / bitcoin-is-time)

### Bitcoin's Solution: Re-Inventing Time

6. Bitcoin solves this problem by re-inventing time itself -- it says no to seconds and yes to blocks. (Dergigi / bitcoin-is-time)
7. Satoshi Nakamoto (2009): "In this paper, we propose a solution to the double-spending problem using a peer-to-peer distributed timestamp server to generate computational proof of the chronological order of transactions." (Satoshi Nakamoto, Bitcoin Whitepaper, 2009)

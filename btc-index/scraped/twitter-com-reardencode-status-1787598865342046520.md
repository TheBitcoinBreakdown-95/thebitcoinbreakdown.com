# twitter.com -- Scraped Content

**URL:** https://twitter.com/reardencode/status/1787598865342046520
**Category:** tweet
**Scrape status:** DONE
**Source notes:** BTC\The Great Script Restoration (GSR).md
**Scraped:** 2026-04-12

---

**@reardencode** (Rearden Vibes 🛩 fork/acc)

Digging into this in the past several days, I'm starting to go back on the push for a new output type.

Here's the arguments as I understand them:
Pro new output type:
* Remove script-only penalty
* Bring back parity bit
* Potentially quantum security
* New key spend sighash
Anti:
* Split anonymity set
* Deployment cost

Responses to pro:
* OP_INTERNALKEY can mitigate this in many cases
* Code is already written to deal with the lack of parity bit, and is not obviously escalating as off chain protocol complexity increases (thanks @jesseposner)
* If there is a quantum break, the network will have to block all EC signatures, so a script path with a quantum resistant signature could still protect coins from freeze
* For key spends, the existing sighash is generally sufficient

Responses to anti:
* GSR will incentivize many users who haven't jumped to TR, and is easy to adopt for those who have
* One more byte in the same witness version and format should be very low cost

I find some of the response to pro pretty compelling, so perhaps a new tapscript version with OP_INTERNALKEY is the best path for GSR.

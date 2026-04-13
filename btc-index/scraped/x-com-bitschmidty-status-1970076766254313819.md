# x.com -- Scraped Content

**URL:** https://x.com/bitschmidty/status/1970076766254313819==
**Category:** tweet
**Scrape status:** DONE
**Source notes:** BTC\OP Return Arguments & Knots.md
**Scraped:** 2026-04-12

---

**@bitschmidty** (Mike Schmidt)

Earlier today I opened a PR to Bitcoin Core to remove the deprecation for the `datacarrier` and `datacarriersize` options. I realize this is a sensitive topic for Bitcoin Core users, so I am also posting here for both visibility and as a place for feedback that might not otherwise be appropriate on the PR.

The tactical goal is to get the change into the forthcoming Bitcoin Core v30 release. I provided rationale which you can review in the PR:
https://github.com/bitcoin/bitcoin/pull/33453

In it I outline that 1. users clearly want this option 2. the intent of deprecation is unclear, and 3. the potential harm to Bitcoin Core users is not large.

Bigger picture, I think designating these options as deprecated has exacerbated  already contentious discussions. People supportive of keeping and using these options are some of Bitcoin’s most ardent supporters and disenfranchising them by deprecating the option is not good for Bitcoin Core or Bitcoin. I know that people still object to the default OP_RETURN value, but with this change, at least Bitcoin Core users can continue to set the value as they see fit. Bitcoin is sure to have more, and bigger, battles ahead and Id like to move forward together to fight those.

Your guess is as good as mine as to whether this PR will get merged. In full transparency, I did reach out to a few contributors to see whether this PR is even “reasonable to propose” at this point, but I did not seek to get “approvals” during such discussions.

Note that this PR takes an existing commit by @ajtowns from a branch of his.

Ill add the same disclaimer here that I did in the PR, given my role @bitcoinbrink:
“I am the executive director of Brink, an organization that funds some Bitcoin Core developers, some of which may review this PR. I have emailed them separately letting them know that any review feedback here (positive or critical) will not impact their standing, funding, or employment with Brink. Independent review and open discussion are critical for Bitcoin Core, and Ive encouraged them to engage as they would with any other contributor.”

I welcome your feedback.

# blog.second.tech -- Scraped Content

**URL:** https://blog.second.tech/ark-on-bitcoin-is-here
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\ARK – Layer 2.md
**Scraped:** 2026-04-12

---

[ Second Blog ](https://blog.second.tech)

Sep 02, 2024 

3 min read

[Steven Roose](/author/steven-roose/)

# Ark on bitcoin is here

[Steven Roose](/author/steven-roose/)

3 min read

Slightly over a year ago, an idea for a new off-chain payment protocol for bitcoin was proposed: Ark. Originally conceived as a solution for onboarding Lightning users, Ark’s design has evolved significantly since then, and it’s become a full-fledged bitcoin scaling protocol in its own right.

Now, we believe Ark is ready for primetime. That’s why we’ve formed [Second](https://second.tech)—a company dedicated to scaling bitcoin through Ark and other second-layer technologies. 

To demonstrate the progress we made, we ran the first-ever Ark transactions with some friends on bitcoin mainnet yesterday—yes, _real sats_. [Read our dedicated report](https://blog.second.tech/demoing-the-first-ark-transactions-on-bitcoin-mainnet/).

## Beyond Lightning

Since its reveal in 2016, the Lightning Network has made incredible progress, becoming the undisputed standard for making retail payments with bitcoin. 

However, with this success, we’ve also started to see the challenges of Lightning’s limitations. While it works incredibly well for tech-savvy users with high payment volumes, retail users often face friction with onboarding and channel management.

Lightning Service Providers (LSPs) can alleviate some of this, but if users are relying on centralized entities for their payments, it raises the question: do they need the complexities of Lightning, which was originally designed for a fully peer-to-peer network?

## Simpler bitcoin scaling

This is where Ark comes in. Ark embraces a centralized approach, adopting a client-server model for fast, low-cost payments while leveraging smart cryptography to ensure that users remain in full control of their bitcoin. 

It achieves this while offering an easier experience for developers and users alike: simpler integrations and simpler wallet management.

## An extension of Lightning, not a replacement

Ark was initially designed to improve Lightning onboarding, so it’s naturally compatible with Lightning and should be seen more as an extension than a replacement. For instance, Ark users can directly pay Lightning invoices (and soon, receive payments too!), allowing them to participate seamlessly in bitcoin’s wider payment ecosystem while enjoying the benefits of Ark when transacting with other Ark users.

We’re still in the early stages of working out how things will shake out, recognizing that some users may benefit more from Ark, others from Lightning, and many from a combination of both.

## An open Ark

Bitcoin and Lightning thrive because of their development communities’ strong dedication to self-custody and open-source. We intend no different with Ark—our implementations of both the client wallet _and_ the Ark server will be open-source. This transparency is essential for Ark’s success within the bitcoin ecosystem.

## Who are we?

[_Our small team_](https://second.tech/about) consists of a group of former Blockstreamers, all passionate about bitcoin’s censorship-resistance and scaling it to a global user base. Personally, I’ve also been a lead contributor in developing the Ark protocol to its current state.

We’re [on the hunt for talented developers too](https://bitcoinerjobs.com/company/second). If you have experience with Rust, C++, or devops (especially running Lightning infrastructure!) and share our passion for bitcoin, we’d love to hear from you!

## Get involved

If you’re interested in enabling Ark payments in your app with Second, check out [_our new developer docs_](https://docs.second.tech/), and [_visit the repository of our Ark implementation_](https://gitlab.com/ark-bitcoin).

Ark opens up a new frontier for scaling bitcoin and we hope you’ll join us in making it a reality!

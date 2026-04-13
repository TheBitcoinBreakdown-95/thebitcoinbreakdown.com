# lists.linuxfoundation.org -- Scraped Content

**URL:** https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2023-May/021602.html
**Category:** scrapable
**Scrape status:** DONE
**Source notes:** BTC\CIV KIT.md
**Scraped:** 2026-04-12

---

[**public inbox for bitcoindev@googlegroups.com**](../?t=20230501174800)
     [help](../_/text/help/) / [color](../_/text/color/) / [mirror](../_/text/mirror/) / [Atom feed](../new.atom)
    
    From: Antoine Riard <antoine.riard@gmail•com>
    To: Bitcoin Protocol Discussion <bitcoin-dev@lists•linuxfoundation.org>
    Subject: Re: [bitcoin-dev] Civ Kit: A Peer-to-Peer Electronic Market System
    Date: Mon, 1 May 2023 18:47:46 +0100	[thread overview]
    Message-ID: <CALZpt+Ga5nT5yy=DpjiU8ULgnas=5CWJYqrRPu5i2Tyq5tG=UA@mail.gmail.com> ([raw](raw))
    In-Reply-To: <[CALZpt+G_wqAqXkenDwdojT4EhpweYwe2DiCYZRFfCbMLL8DbVA@mail.gmail.com](../CALZpt+G_wqAqXkenDwdojT4EhpweYwe2DiCYZRFfCbMLL8DbVA@mail.gmail.com/)>
    
    [[-- Attachment #1: Type: text/plain, Size: 7294 bytes --]](1-a.txt)
    
    Hi all,
    
    One of the most relevant feedback I received on the paper publication
    was the lack of underscoring front-running resistance as a fundamental
    property wished for a peer-to-peer marketplace.
    
    It is expected the level of front-running resistance aimed by the
    market participants to be heavily functioned by the types of trades
    considered: fiat currencies, real goods, services. For some classes of
    goods, e.g commodities one cannot expect the same level of item
    liquidity due to cycle of production and exogenous factors like
    weather. Some types of trades marketplaces might be exposed to far
    less front-running risks and rather would have to deal with accurate
    risk modelling of the underlying goods. E.g attest there is a
    decentralized identifier or any other linkage proof of the physical
    good existence staying valid for the duration of offer lifetime.
    Offers conditions themselves might be far more verbose and precise
    special Bitcoin Script paths to morph the shipment risks.
    
    On the other hand, the types of trades like fiat currencies or bitcoin
    financial contracts (e.g discreet log contracts or submarine swaps),
    front-running risk by the bulletin board sounds a qualified concern.
    In traditional finance, front-running is defined as "entering into an
    equity trade, options or future contracts with advance knowledge of a
    block transaction that will influence the price of the underlying
    security to capitlize on the trade" [0]. In Bitcoin/Civkit parlance, a
    front-running could be a board on the discovery of a batch of market
    offers increasing liquidity for a fiat-2-btc pair, seizing the
    opportunity by forwarding a HTLC across a Lightning payment path to
    enter into the trade, before publishing the offer on its board.
    
    I think you have at least two security paradigms to mitigate
    front-running happening peer-to-peer marketplace. The first one is to
    duplicate the announcement of the offers to a number of concurrent
    board operated by independent identities and in parallel monitor the
    latency. Latency anomalies should be spotted on by watchtower-like
    infrastructure at the service of makers/takers and in case of repeated
    anomalies a maker should disqualify the misbehaving board from future
    announcements. As all statistical mitigation it is not perfect and
    open the way to some margin of exploitation by the boards, as the
    watchtower monitoring frequency can be guessed. Additionally, this
    latency monitoring paradigm sounds to be valid under the assumption
    that at least one board is "honest" and board might have a holistic
    interest to silently collude. Running or accessing monitoring
    infrastructure comes with a new liveliness requirement or additional
    cost for mobile clients.
    
    Another paradigm can be to run the bulletin boards as a federation e.g
    under Honey Badger BFT as used by Fedimint [1]. The incoming board
    offers become consensus items that must be announced to all the
    federations members onion gateway and which are not announced before a
    consensus proposal has been adopted. The e-cash tokens can be rather
    Bitcoin-paid credentials required by the board federation for
    publication. The federation members earn an income as a group to
    follow the consensus rules and be paid only when there is "consensus"
    publication. The federation could adopt some "DynFed" techniques to
    extend the federation set [2]. One can imagine a federation consisting
    of all the significant market participants, leveling the field for
    all.
    
    Is there another security paradigm direction to mitigate front-running
    and other asymmetries of information ? I can't immediately imagine
    more though I believe it stays an interesting open question.
    
    In fine, the Civkit proposes a flexible framework for peer-to-peer
    marketplace, where propagation latency monitoring and federation set
    and rules can be tweaked as "front-running resistance" parameters,
    adapting to the types of trades and market participants tolerance.
    Configuration of those parameters will at the end be function of
    real-world deployments. Somehow mass front-running on the board is a
    "champagne" issue  I'll be happy to have.
    
    Best,
    Antoine
    
    [0] <https://www.finra.org/investors/insights/getting-speed-high-frequency-trading>
    [1] <https://fedimint.org/docs/CommonTerms/HBBFTConsensus>
    [2] <https://blockstream.com/assets/downloads/pdf/liquid-whitepaper.pdf>
    
    
    Le jeu. 13 avr. 2023 à 15:10, Antoine Riard <antoine.riard@gmail•com> a
    écrit :
    
    > Hi list,
    >
    > We have been working since a while with Nicholas Gregory (Commerce Block),
    > Ray Youssef (the Built With Bitcoin foundation) and few others on a new
    > peer-to-peer market system to enable censorship-resistant and
    > permissionless global trading in all parts of the world. While the design
    > aims in priority to serve on-ramp/off-ramp trading, it can be extended to
    > support any kind of trading: goods, services, bitcoin financial derivatives
    > like discreet log contracts.
    >
    > The design combines the Nostr architecture of simple relays announcing
    > trade orders to their clients with Lightning onion routing infrastructure,
    > therefore granting high-level of confidentiality to the market
    > participants. The market boards are Nostr relays with a Lightning gateway,
    > each operating autonomously and in competition. The market boards can be
    > runned as a federation however there is no "decentralized orderbook" logged
    > into the blockchain. The trades are escrowed under Bitcoin Script
    > contracts, relying on moderations and know your peer oracles for
    > adjudication.
    >
    > The scoring of trades, counterparties and services operators should be
    > enabled by the introduction of a Web-of-Stakes, assembled from previous
    > ideas [0]. From the Bitcoin UTXO set servicing as a trustless source of
    > truth, an economic weight can be assigned to each market entity. This
    > reputation paradigm could be composed with state-of-the-art Web-of-Trust
    > techniques like decentralized identifiers [1].
    >
    > A consistent incentive framework for service operators is proposed by the
    > intermediary of privacy-preserving credentials backed by Bitcoin payments,
    > following the lineaments of IETF's Privacy Pass [2]. Services operators
    > like market boards and oracles are incentivized to thrive for efficiency,
    > akin to routing hops on Lightning and miners on the base layer.
    >
    > The whitepaper goes deep in the architecture of the system [3] (Thanks to
    > the peer reviewers!).
    >
    > We'll gradually release code and modules, extensively building on top of
    > the Lightning Dev Kit [4] and Nostr libraries. All according to the best
    > Bitcoin open-source and decentralized standards established by Bitcoin Core
    > and we're looking forward to collaborating with everyone in the community
    > to standardize libraries and guarantee interoperability between clients
    > with long-term thinking.
    >
    > Feedback is very welcome!
    >
    > Cheers,
    > Nick, Ray and Antoine
    >
    > [0]
    > <https://lists.linuxfoundation.org/pipermail/lightning-dev/2020-November/002884.html>
    > [1] <https://www.w3.org/TR/2022/REC-did-core-20220719/>
    > [2] <https://privacypass.github.io>
    > [3] <https://github.com/civkit/paper/blob/main/civ_kit_paper.pdf>
    > [4] <https://lightningdevkit.org>
    >
    
    [[-- Attachment #2: Type: text/html, Size: 8578 bytes --]](2-a.bin)
    

* * *
    
    [next](../CAFQwNuwDCC08jbhAE2pjqi9JFNerP00JpGo9dfzT4j8KNc_+0A@mail.gmail.com/) [prev parent](../CALZpt+G_wqAqXkenDwdojT4EhpweYwe2DiCYZRFfCbMLL8DbVA@mail.gmail.com/) reply	other threads:[[~2023-05-01 17:48 UTC](../?t=20230501174800)|[newest](../)]
    
    **Thread overview:** 4+ messages / expand[[flat](T/#u)|[nested](t/#u)]  [mbox.gz](t.mbox.gz)  [Atom feed](t.atom)  top
    2023-04-13 14:10 [Antoine Riard](../CALZpt+G_wqAqXkenDwdojT4EhpweYwe2DiCYZRFfCbMLL8DbVA@mail.gmail.com/)
    **2023-05-01 17:47 `Antoine Riard [this message]**
    2023-05-09 15:09   ` [Chris Stewart](../CAFQwNuwDCC08jbhAE2pjqi9JFNerP00JpGo9dfzT4j8KNc_+0A@mail.gmail.com/)
    2023-06-30  3:46     ` [Antoine Riard](../CALZpt+GZgnRTpQZOpHQEo5Txt-DJZ+Zu=frm0OkoX6gzhZP-rg@mail.gmail.com/)
    

* * *
    
    **Reply instructions:**
    
    You may reply publicly to this message via plain-text email
    using any one of the following methods:
    
    * Save the following mbox file, import it into your mail client,
      and reply-to-all from there: [mbox](raw)
    
      Avoid top-posting and favor interleaved quoting:
      <https://en.wikipedia.org/wiki/Posting_style#Interleaved_style>
    
    * Reply using the **--to** , **--cc** , and **--in-reply-to**
      switches of git-send-email(1):
    
      git send-email \
        --in-reply-to='CALZpt+Ga5nT5yy=DpjiU8ULgnas=5CWJYqrRPu5i2Tyq5tG=UA@mail.gmail.com' \
        --to=antoine.riard@gmail$(echo .)com \
        --cc=bitcoin-dev@lists$(echo .)linuxfoundation.org \
        /path/to/YOUR_REPLY
    
      <https://kernel.org/pub/software/scm/git/docs/git-send-email.html>
    

Be sure your reply has a **Subject:** header at the top and a blank line before the message body. 

* * *
    
    This is a public inbox, see [mirroring instructions](../_/text/mirror/)
    for how to clone and mirror all data and code used for this inbox

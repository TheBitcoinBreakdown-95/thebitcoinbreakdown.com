# ArkPool Research -- WORKLOG

## Session 2 -- 2026-03-21

**What was done:**
- Wrote viability assessment (rewrote 3 times as framing improved)
- Fixed repayment model: principal from capital cycle, interest from fee revenue
- All figures BTC-denominated (no dollar amounts)
- High-fee contingency: 200-500 sat/vB sustained, with batching strategies and OOR escape valve
- Reframed lender economics: idle BTC at 0% is the baseline, lender floor ~1-2%
- Built arkpool-spec.html (TBB V4 theme, standalone)
- Updated prior-art-and-resources.md with all links from bitcoinops.org and ark-protocol.org (full site crawl)
- Verified V2 revocation status: NOT implemented in either codebase. Blog post only.
- Pulled actual config values from cloned repos (arkd + bark source code)
- Name check: "ArkPool" semi-taken (old ARK.io delegate pool, unrelated)

**Critical corrections this session:**
- V2 revocation is a blog post, not shipping code. ZK-based VPU not specified.
- Arkade default VTXO expiry: 7 days (config.go:241, `604672` seconds) -- NOT 28 days
- Bark default VTXO expiry: 30 days (captaind.default.toml:14, `4320` blocks) -- NOT 28 days
- The "4x multiplier" and "1.3x change multiplier" are NOT from any published Ark spec. Derived independently.
- Lockup multiplier at 7-day expiry is only ~1.3x -- the capital problem is much smaller than originally framed
- Bark's fee tiers (0-0.8% PPM by VTXO age) explicitly price the lockup cost to users
- Arkade fees: CEL expression programs, zero by default, fully operator-configured

**Key insight:** ArkPool's necessity depends heavily on which expiry setting ASPs choose. At 7-day (Arkade), most operators can self-fund through high throughput. At 30-day (Bark), the wall hits much sooner -- but those ASPs also earn more from lockup-weighted fees.

**Documents (18 total):**
- Session 1: 16 research docs + protocol-spec.md + prior-art-and-resources.md
- Session 2: viability-assessment.md, arkpool-spec.html, updates to protocol-spec.md and prior-art

**To-do:**
- [ ] Write the code (Phase 1 CLI: escrow library, term sheet, proof-of-reserves, CLI wrapper)
- [ ] Formal whitepaper (after code is written)
- [ ] Decide on name (ArkPool vs alternatives: ArkFund, ArkLend, VTXOPool, etc.)
- [ ] Publish: GitHub repo, comment on issue #197, Delving Bitcoin post
- [ ] Review protocol-spec.md in detail (carried from session 1)
- [ ] Sync arkpool-spec.html with latest protocol-spec.md and viability changes

# ArkPool Research -- WORKLOG

## Session 2 -- 2026-03-21

**What was done:**
- Wrote viability assessment (rewrote 3x as framing improved)
- Fixed repayment model: principal from capital cycle, interest from fee revenue
- All figures BTC-denominated
- High-fee contingency: 200-500 sat/vB sustained, batching strategies, OOR escape valve
- Reframed lender economics: idle BTC at 0% is baseline, lender floor ~1-2%
- Built arkpool-spec.html (TBB V4 theme, standalone)
- Updated prior-art-and-resources.md with all links from bitcoinops.org and ark-protocol.org
- Verified V2 revocation: NOT implemented. Blog post only. ZK-based VPU not specified.
- Pulled actual config values from cloned repos (arkd + bark source code)
- Rewrote protocol spec as v0.2: compact intro-problem-cause-solution-impact framework
- Dropped Approach A, went straight to per-round integration (Approach B)
- Committed all research to git (TBB repo, commit cfaae75, 21 files, 7,412 lines)

**Critical corrections:**
- Arkade default VTXO expiry: 7 days (config.go:241). NOT 28 days.
- Bark default VTXO expiry: 30 days (captaind.default.toml:14). NOT 28 days.
- Lockup multiplier at 7-day: ~1.3x. At 30-day: ~5.6x. NOT from any published spec -- derived.
- 1.3x change multiplier is our own estimate. Not sourced.
- V2 revocation not implemented in either codebase. Requires unspecified ZK system.
- Bark refresh fees: 0-0.8% PPM tiered by VTXO age (from code). Arkade fees: zero by default, operator-configured via CEL expressions.
- "ArkPool" name semi-taken (old ARK.io DPoS delegate pool at arkpool.net, unrelated).

**Unresolved design problem (carry to next session):**
The per-round integration (Approach B) exposes LPs to unilateral exit risk. When a user exits on-chain, their portion of the LP's forfeit claim is voided. The LP's principal recovery depends on user behavior.

Three models explored, none fully satisfactory:
1. **Secured loan (old Approach A):** ASP posts collateral escrow. LP is safe. But posting 110% collateral to borrow 100% means net negative capital gain -- only works if ASP has idle reserves separate from operating capital.
2. **Unsecured round participation (Approach B):** LP funds round directly, repaid from forfeits. No collateral. LP bears exit risk. Higher yield compensates but principal is not guaranteed.
3. **Hybrid (A+B):** ASP posts partial collateral + LP enters round. Collapses back into one of the above depending on collateral ratio. Not a real third option.

The core tension: full collateral = LP safe but ASP gains nothing. No collateral = ASP gains capital but LP exposed. Partial collateral = partial exposure. No clean solution found yet.

**Key questions for next session:**
- Is there a tree construction where LP claims are structurally senior to user exit paths?
- Can the LP's portion be isolated in the tree so unilateral exits don't affect it?
- Is the secured loan model (Approach A) actually fine if we frame it as "ASP posts idle reserves, not operating capital"?
- Should we accept that the LP takes actuarial risk and just price it correctly?
- Is there a mechanism where the ASP absorbs exit shortfall from its other expiring trees (the LP waits a few rounds)?

**Documents (18 research + spec + viability + HTML):**
All committed to git. Protocol spec is v0.2 (per-round integration focus).

**To-do:**
- [ ] Resolve the LP principal protection problem (the big one)
- [ ] Update protocol spec with chosen approach
- [ ] Write the code (Phase 1 CLI)
- [ ] Formal whitepaper (after code)
- [ ] Decide on name
- [ ] Publish: GitHub repo, issue #197 comment, Delving Bitcoin post
- [ ] Sync arkpool-spec.html with latest protocol-spec.md

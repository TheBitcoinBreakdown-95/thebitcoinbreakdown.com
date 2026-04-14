# ArkPool Research -- WORKLOG

## Last Session -- 2026-04-07

**What was done:**
- Protocol spec upgraded from v0.2 to v0.3 with four targeted edits:
  - Reframed "For the Ark Ecosystem" impact section: distinguishes throughput ceiling (ArkFloat solves) from bootstrapping problem (it doesn't)
  - Added "Fee Adequacy" subsection to Viability: capital asymmetry vs Lightning, managed-service pricing ceiling, OOR scale economics argument
  - Expanded Cold Start risk: small ASP adverse selection spiral, Lightning Pool precedent mitigation, honest caveat that mitigation may not function (tail risk dominates expected value for early-stage ASPs)
  - Updated prior-art acknowledgment (PR #198 and Discoco-Labs Pool fork identified)
- Thorough prior-art web search confirmed: no project named ArkFloat exists. ben2077/Discoco-Labs PR #198 (closed, unmerged) is the only partial implementation of the core mechanism. Second's 3-part liquidity research series is closest active work but stops at economic analysis.
- Comprehensive problem audit: 55+ issues cataloged across spec and 11 research note files
- Consolidated into 22 numbered problems (P1-P22) across 7 categories
- Designed 8-phase brainstorming pipeline: Operationalize -> Research -> Reframing (human checkpoint) -> Council of Experts -> Skeptic -> Check-in (human checkpoint) -> Verification -> Summary
- Brainstorm plan finalized with locked decisions:
  1. Two-pass approach (A+B on all 22 first, then C-H on survivors)
  2. Compressed pipeline for Tier 5 (timing/context problems)
  3. Flexible pacing at human checkpoints

**Key findings:**
- LP yield structurally thin at current market fee rates (~0.3% blended). Breakeven at ~0.35-0.40%.
- Fee adequacy argument: Ark fees justifiably higher than Lightning routing fees (ASP fronts 100% capital, user gets zero-infra managed service)
- Scale economics improve LP viability: OOR transactions have zero on-chain footprint, margin improves at volume. But benefit accrues to large ASPs, not small ones.
- Small ASP adverse selection spiral is real and unaddressed: need capital most, can afford it least, higher fees to service LP debt make them less competitive.

**Files created/modified:**
- Modified: `repo-idea/protocol-spec.md` (v0.3 edits)
- Created: `repo-idea/repo-notes/problems-brainstorming/brainstorm-plan.md`

## Session History

### 2026-03-21 -- Session 2: Spec v0.2 and viability assessment
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
- Critical corrections: Arkade 7-day expiry (not 28), Bark 30-day (not 28), lockup multipliers derived not sourced
- Unresolved: LP principal protection problem (per-round exit risk)

## To-Do
- [ ] Execute brainstorm Pass 1: Phases A+B on all 22 problems (start with Tier 1: P1, P2, P5, P14)
- [ ] Human triage checkpoint after Pass 1 landscape is complete
- [ ] Execute brainstorm Pass 2: Phases C-H on survivors
- [ ] Update protocol spec to v0.4 with brainstorm results
- [ ] Update prior-art-and-resources.md with PR #198 and Discoco-Labs Pool fork findings
- [ ] Sync arkpool-spec.html with latest protocol-spec.md
- [ ] Resolve LP principal protection problem
- [ ] Write the code (Phase 1 CLI)
- [ ] Formal whitepaper (after code)
- [ ] Decide on name
- [ ] Publish: GitHub repo, issue #197 comment, Delving Bitcoin post

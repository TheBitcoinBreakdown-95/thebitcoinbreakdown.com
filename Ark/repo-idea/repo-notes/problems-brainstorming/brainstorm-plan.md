# ArkFloat Brainstorm Plan

## Context

The ArkFloat protocol spec (v0.3) proposes an LP lending protocol for Ark ASPs. A comprehensive audit surfaced 55+ problems, concerns, and open questions across the spec and 11 research note files. This plan defines a structured brainstorming process to address each one -- moving from problem definition through multi-perspective ideation to verified solutions.

---

## Numbered Problem List (22 problems, 7 categories)

### Economic Viability
- **P1:** Fee adequacy -- can ASPs sustain the ~0.35-0.40% blended rate threshold under competitive pressure?
- **P2:** LP yield structurally thin -- 1-3% best case, negative in stress cases. Is it attractive enough?
- **P3:** Change output capital drag -- capital committed without proportional fee generation (1.3x multiplier)
- **P4:** V2 revocation residual gap -- only solves 30-60% of capital problem; residual may not justify infrastructure

### LP Risk
- **P5:** Unilateral exit risk -- correlated, tail-heavy, not diversifiable within a single ASP
- **P6:** Insurance pool circular dependency -- same stress event depletes insurance and triggers LP losses
- **P7:** LP diversification not protocol-enforced; unsophisticated LPs bear catastrophic risk

### Competitive Dynamics
- **P8:** Small ASP adverse selection spiral -- need capital most, can afford it least
- **P9:** Scale economics favor large ASPs disproportionately (OOR cost collapse at volume)
- **P10:** Institutional self-funding creates permissioned ASP ecosystem if LP market fails

### Protocol Design
- **P11:** hArk forfeit compatibility -- musig sighash changes when recipient changes, may break hArk guarantees
- **P12:** Forfeit verification refactor -- scope uncertain in both Arkade and Bark
- **P13:** Fixed VTXO script template -- no custom spending conditions, no third-party claims possible
- **P14:** ASP as borrower AND co-signer -- circular risk for collateral enforcement

### Market Structure
- **P15:** LP discovery -- no mechanism specified beyond "bilateral, then auction"
- **P16:** Rate discovery -- no market mechanism defined
- **P17:** Proof of reserves format -- LPs can't evaluate ASP health without it
- **P18:** No cross-implementation interop standard (Arkade LP != Bark LP)

### Timing & Readiness
- **P19:** Cold start -- LP base doesn't exist, ASPs are beta, market too small now
- **P20:** Infrastructure cost may exceed economic benefit for 3-5 years
- **P21:** Stablecoin scenario changes throughput 10-100x, shifting timing calculus entirely

### Legal
- **P22:** Legal classification of BTC-for-BTC fixed-term lending is unknown

---

## Brainstorming Pipeline (8 phases per problem)

### Phase A: Operationalize the Problem
**Who:** Claude main thread
**Action:** Read relevant research notes. State the problem precisely -- what's broken, what assumptions it rests on, what "solved" looks like. Identify variables and dependencies on other numbered problems.
**Output:** Problem statement, success criteria, dependency map.

### Phase B: Research
**Who:** /ark-expert subagent + WebSearch + Read on research notes
**Action:** Check source code for existing mechanisms. Check research notes for partial solutions. Web search for prior art on this specific sub-problem.
**Output:** Research brief -- what's known, tried, unexplored.

### Phase C: Reframing / Brainstorming [HUMAN CHECKPOINT]
**Who:** Claude main thread
**Action:** Present the problem through 5 cognitive lenses:
1. **Inversion** -- what would make this worse? What's the opposite of the solution?
2. **First principles** -- strip tradfi framing. What's actually required?
3. **Analogy transfer** -- what other systems (biological, engineering, economic) solved something structurally similar?
4. **Constraint removal** -- if we could change ONE thing, what makes this trivial?
5. **Stakeholder rotation** -- LP / ASP / user / regulator / Satoshi perspectives

**Output:** 3-5 reframed problem statements.
**PAUSE** for human reaction before Phase D.

### Phase D: Council of Experts Ideation
**Who:** Claude main thread + /ark-expert subagent
**Action:** 5 expert perspectives each generate 1-2 concrete solution proposals:
1. **Satoshi** -- minimize trust, script-level enforcement, no intermediaries
2. **Ark-expert** -- what the actual code enables/prevents (source code citations)
3. **TradFi expert** -- how repo/securities lending handles the analogue
4. **Game theorist** -- incentive structures, who defects, mechanism design
5. **Systems engineer** -- simplest mechanism, failure mode analysis

**Output:** Concrete proposals with enough detail to evaluate.

### Phase E: Skeptic Analysis
**Who:** Claude main thread
**Action:** Attack each Phase D proposal:
- What assumptions might not hold?
- Failure mode under adversarial conditions?
- Does it create worse problems than it solves?
- Does it require changes neither implementation will accept?
- Survives a correlated stress event?

**Output:** Each proposal rated VIABLE / PROMISING BUT FLAWED / DEAD ON ARRIVAL with reasons.

### Phase F: Check-In [HUMAN CHECKPOINT]
**Who:** Claude main thread
**Action:** Summarize: problem, surviving proposals (ranked), killed proposals and why.
**PAUSE** for human to select which proposals proceed to verification.

### Phase G: Verification
**Who:** /ark-expert subagent + Claude math
**Action:** For human-approved proposals: verify code feasibility (specific files/functions), check economic arithmetic with numbers from unit-economics.md, confirm no dependency on non-existent features.
**Output:** Confidence-rated feasibility assessment.

### Phase H: Summary
**Who:** Claude main thread
**Action:** Final output: recommended approach, alternatives considered, open items.
**Output:** Appended to brainstorm-output.md.

---

## Execution Order (tiered by leverage)

### Tier 1: Existential / Go-No-Go (first)
| Order | Problem | Why first |
|-------|---------|-----------|
| 1 | P1 | If fees can't clear LP spread, nothing else matters |
| 2 | P2 | Even if fees clear, is yield attractive? |
| 3 | P5 | Core risk. 2 directions already rejected in research. |
| 4 | P14 | Structural circular risk -- may be unfixable |

### Tier 2: Design-Critical
| Order | Problem | Why |
|-------|---------|-----|
| 5 | P11 | Technical blocker for Bark |
| 6 | P12 | Technical blocker for Arkade |
| 7 | P13 | Determines if LP claims can be script-enforced |
| 8 | P6 | If insurance is part of P5 solution, this is the follow-on |

### Tier 3: Economic Model
| Order | Problem | Why |
|-------|---------|-----|
| 9 | P3 | Hidden cost; affects P1/P2 conclusions |
| 10 | P4 | Does V2 change the ArkFloat calculus? |
| 11 | P8 | Who is the actual customer? |
| 12 | P9 | May reveal ArkFloat serves 2-3 ASPs, not 20 |

### Tier 4: Market Infrastructure
| Order | Problem | Why |
|-------|---------|-----|
| 13 | P15 | Market can't function without LP discovery |
| 14 | P16 | Paired with P15 |
| 15 | P17 | LP due diligence requirement |
| 16 | P18 | Needed for multi-ASP diversification |

### Tier 5: Context & Timing (compressed pipeline)
| Order | Problem | Why |
|-------|---------|-----|
| 17 | P19 | When to launch |
| 18 | P20 | Cost/benefit horizon |
| 19 | P21 | Stablecoin scenario planning |
| 20 | P10 | Alternative future analysis |
| 21 | P7 | Design choice, not blocker |
| 22 | P22 | Parallel legal track |

### Batching Opportunities
- **P1 + P2** (same economic model, do back-to-back)
- **P11 + P12** (forfeit changes, one per implementation)
- **P15 + P16** (discovery mechanisms)
- **P8 + P9 + P10** (competitive dynamics trio)

---

## Decisions (Locked)

1. **Two-Pass approach.** Pass 1: Phases A+B on all 22 problems (operationalize + research). Human triages the landscape -- problems may dissolve, merge, or reorder. Pass 2: Phases C-H on survivors only.
2. **Compressed pipeline for Tier 5.** P19-P22 get Phases A, B, D, H only. Skip human checkpoints, skeptic, and verification.
3. **Flexible pacing.** Human decides per-problem whether to pause at checkpoints or blow through.

---

## Output Files

| File | Location | Purpose |
|------|----------|---------|
| `brainstorm-output.md` | `TBB/Ark/repo-idea/repo-notes/problems-brainstorming/` | Running results -- all phase outputs, accumulated per problem |
| `brainstorm-state.md` | `TBB/Ark/repo-idea/repo-notes/problems-brainstorming/` | Lightweight state tracker: current problem, current phase, human decisions, cross-problem insights |

---

## Execution Plan

### Pass 1: Operationalize + Research (Phases A-B on all 22)
- **Batch by tier.** Process in tier order so existential problems surface first.
- **~500-1500 tokens per problem** (lighter phases). All 22 in ~2-3 sessions.
- **Output:** Complete landscape in brainstorm-output.md. Each problem has a crisp statement + research brief.
- **Then:** Human triage checkpoint. Review the full landscape. Mark problems as: PROCEED (full pipeline) / MERGE (combine with another) / DISSOLVE (no longer relevant) / DEFER (not worth solving now).

### Pass 2: Deep Brainstorm (Phases C-H on survivors)
- **Tier 1-4 survivors:** Full 8-phase pipeline with human checkpoints at Phase C and F.
- **Tier 5 (P19-P22):** Compressed pipeline -- Phases A, B, D, H only.
- **~2-3 problems per session** for full pipeline problems.
- **Estimated total:** 7-9 sessions for Pass 2 (depends on how many problems survive triage).

---

## Verification Plan

After each problem completes Phase H:
1. Confirm brainstorm-output.md has the complete Phase A-H record
2. Confirm brainstorm-state.md is updated
3. If the solution affects the protocol spec, note the spec section that needs updating (but don't edit the spec during brainstorming -- batch all spec updates after)

After all 22 problems complete:
1. Review brainstorm-output.md holistically for cross-problem coherence
2. Identify spec sections that need revision
3. Draft spec v0.4 incorporating brainstorm results

---

## Critical Source Files

| File | Content | Used in |
|------|---------|---------|
| `TBB/Ark/repo-idea/protocol-spec.md` | Main spec (v0.3) | All problems |
| `TBB/Ark/repo-idea/repo-notes/unit-economics.md` | Fee/yield arithmetic | P1, P2, P3, P9 |
| `TBB/Ark/repo-idea/repo-notes/lp-exit-risk-analysis.md` | Exit risk analysis, rejected directions | P5, P6, P7 |
| `TBB/Ark/repo-idea/repo-notes/constraints.md` | Protocol constraints (go/no-go gates) | P13, P14 |
| `TBB/Ark/repo-idea/repo-notes/framing-analysis.md` | Four frames, residual gap analysis | P4, P10, P20 |
| `TBB/Ark/repo-idea/repo-notes/existing-proposals.md` | Gap map of all published proposals | P15, P16, P19 |
| `TBB/Ark/repo-idea/repo-notes/defi-survey.md` | DeFi precedents, rehypothecation risk | P6, P7 |
| `TBB/Ark/repo-idea/repo-notes/viability-assessment.md` | Phase 1 escrow design | P14 |
| `TBB/Ark/repo-idea/prior-art-and-resources.md` | All prior art and references | Phase B research |
| `TBB/Ark/ark-labs/arkade-spec.md` | Arkade architecture | P11, P12 |
| `TBB/Ark/Second/bark-implementation.md` | Bark architecture | P11, P12 |

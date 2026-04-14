# Brainstorm State Tracker

## Current Position
- **Pass:** 1 (Operationalize + Research)
- **Last completed:** P14 Phase B (April 7, 2026)
- **Next:** Tier 2 problems (P11, P12, P13, P6) or continue to remaining tiers

## Tier 1 Status (Existential / Go-No-Go)

| Problem | Phase A | Phase B | Status |
|---|---|---|---|
| P1 (Fee adequacy) | Done | Done | Key finding: 0% Ark-to-Ark fees make blended rate a traffic mix question |
| P2 (LP yield) | Done | Done | BTC yield market contracted; 1-3% more competitive than expected |
| P5 (Unilateral exit risk) | Done | Done | Novel framing; Aave Umbrella + tranching identified as templates |
| P14 (Circular co-signer) | Done | Done | Fundamental gap: no sybil detection without trusting ASP |

## Cross-Problem Insights (Tier 1)

1. **P1 and P2 are coupled but pulling in different directions.** P1's 0% Ark-to-Ark fee finding suggests blended fees may be lower than modeled, which hurts LP yield. But P2's finding that the BTC yield market has contracted means even lower yields are relatively competitive. The question is whether the absolute yield clears LP risk appetite, not whether it beats CeFi benchmarks (which have collapsed).

2. **P5's "novel framing" status is both a risk and an opportunity.** No one in the Ark community has analyzed external LP exit risk. This means (a) the problem hasn't been solved, but also (b) it hasn't been dismissed as unsolvable. ArkFloat has first-mover framing advantage.

3. **P14 may not be a blocker for Phase 1.** The standalone escrow model (Phase 1) adequately mitigates circular risk. Per-round integration (Phase 2) carries reducible but not eliminable ASP trust. The honest framing: Phase 1 is trustless, Phase 2 adds trust assumptions that are bounded by economic mechanisms (bonds, watchtowers, co-signing).

4. **The stablecoin scenario keeps appearing as the unlock.** P1 fee adequacy, P2 yield attractiveness, and P5 risk pricing all improve dramatically under stablecoin throughput. Tether's investment in Ark Labs is the leading indicator. ArkFloat may be premature for BTC-only Ark but essential for stablecoin Ark.

5. **First-loss reserve funded from historical revenue** (Aave Umbrella pattern) is the strongest candidate for breaking the P5/P6 circular dependency. This should be a central design element in Pass 2.

## Decisions Log
- (none yet -- awaiting human triage after Pass 1 completes)

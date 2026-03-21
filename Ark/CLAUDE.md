# CLAUDE.md -- ArkPool

> BTC-native liquidity market for Ark Service Providers. Research and protocol design.

**Status:** Protocol spec v0.1 drafted. Risk/viability assessment pending. No code yet.

---

## Project Map

| Folder | Purpose |
|--------|---------|
| `Ark Labs/` | Ark Labs research + cloned repos (ark, arkd) |
| `Second/` | Second research + cloned repo (bark) |
| `Repo idea/` | Protocol spec, prior art tracking |
| `Repo idea/Repo notes/` | Research documents (16 files, ~7,200 lines) |

## Key Documents

### Protocol Spec
- `Repo idea/protocol-spec.md` -- **ArkPool v0.1 draft.** Two-phase architecture: standalone bilateral lending (now) -> per-round integration (future). Timelocked multisig escrow. BTC-for-BTC. Block-height denominated terms.

### Prior Art + Resources
- `Repo idea/prior-art-and-resources.md` -- Tracks existing work, discussion venues (GitHub issue #197), adjacent projects (Lendasat, Lightning Pool, Lygos), and the gap we're filling.

### Research (by topic)
| Topic | Files |
|-------|-------|
| Ark protocol | ark-v2-mechanics.md, arkade-spec.md, lightning-integration.md, bark-implementation.md, comparison.md |
| Traditional repo | traditional-repo.md |
| DeFi + existing proposals | defi-survey.md, existing-proposals.md |
| Problem quantification | problem-spec.md, unit-economics.md |
| Constraints + framing | constraints.md, framing-analysis.md |
| BTC-for-BTC analysis | dealer-balance-sheets.md, interbank-liquidity.md |

## Cloned Repos

| Repo | Local Path |
|------|-----------|
| ark-network/ark | `Ark Labs/ark/` |
| arkade-os/arkd | `Ark Labs/arkd/` |
| ark-bitcoin/bark | `Second/bark/` |

## Key Design Decisions

- "Repo" is the wrong frame -- this is BTC-for-BTC working capital financing (interbank model)
- Unilateral exit is sacrosanct (design principle P1)
- Phase 1 is fully trustless: timelocked 2-of-2 multisig, no oracle, no DLC
- All terms in block heights, not clock time (design principle P7)
- No rehypothecation, no credit creation, no fractional reserves
- Three liquidity sources: inter-ASP, Lightning LPs, HODLers

## Conventions

- Research notes are Markdown, no frontmatter required
- Cite sources inline with links
- Every claim about Ark mechanics must reference a spec, codebase, or official doc
- Devil's advocate sections encouraged in every document
- No emojis

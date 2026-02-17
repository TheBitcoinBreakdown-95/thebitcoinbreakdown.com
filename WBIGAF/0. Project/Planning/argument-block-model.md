# Argument Block Model

> **Purpose:** This document defines how raw source material gets structured into draftable argument architecture. It is the reference for Step 4 (Argument Map) of the sub-chapter pipeline.
>
> **Condensed summary:** See `WBIGAF/WBIGAF.md` Section 4, Step 4.

---

## 1. Why This Model Exists

During Triage (Step 1), every distinct claim, quote, data point, and observation in the source file gets its own numbered line item. This raw inventory is deliberately granular — it catches everything. But granular inventory is not argument architecture. A quote is not an argument. A data point is not an argument. A bullet point in a list is not an argument.

The problem with treating every line item as an "argument":
- A Nat Brunell transcript clip and an Investopedia definition get equal weight
- Sub-points of the same argument get separate numbers (#69-71 are all "Bitcoin fixes this because...")
- Rhetorical devices, author observations, and sourced evidence all sit at the same level
- Duplicates accumulate when the source file revisits the same theme
- When it's time to draft, staring at 199 items provides no structural guidance

The Argument Block model solves this by adding a structured layer between raw inventory and draft prose.

---

## 2. Three Models Considered and Rejected

### Hierarchical (core arguments with nested evidence)
- **Strength:** Clear parent-child relationships
- **Failure mode:** Evidence that supports multiple arguments gets trapped in one branch. Restructuring cascades through the tree. Feels academic, not polemic.

### Thesis-Based (each item = standalone thesis)
- **Strength:** Modular, each piece stands alone
- **Failure mode:** Not everything is a thesis. In a polemic, arguments build cumulatively — pure modularity fights the escalating structure needed. Forces artificial containers around non-thesis material.

### Inventory + Map (flat index with clustering layer on top)
- **Strength:** Preserves raw material, flexible grouping
- **Failure mode:** Clusters show *what's related* but not *what the argument is* or *how to present it*. Creates a gap between map and draft that still needs bridging. Two layers to maintain.

### Why Argument Blocks Win
- Separates capture (inventory) from structure (blocks) — no premature classification during Triage
- Explicitly distinguishes argument types: thesis, logic, quotes, evidence, devices
- Each block maps directly to one section of the draft
- Evidence can appear in multiple blocks via cross-reference
- Source traceability preserved through inventory item references
- Scales across 67 sub-chapters with a consistent format

---

## 3. Argument Block Format

```
## Block [#]: [Title]

**THESIS:** [One sentence — the core claim being made]

**LOGIC CHAIN:**
1. [Premise or step 1]
2. [Step 2 — follows from step 1]
3. [Step 3]
...
n. [Conclusion — restates thesis with force]

**KEY QUOTES:**
- "[Quote]" — Source
- "[Quote]" — Source

**EVIDENCE:** [Data points, examples, historical facts, definitions]

**RHETORICAL MOVES:** [Analogies, metaphors, emotional beats, devices worth preserving]

**SOURCE REFS:** Inventory #X-Y | Links #A, #B | Research #Z
```

### Field Definitions

| Field | What Goes Here | Required? |
|-------|---------------|-----------|
| **Thesis** | The one-sentence claim this block proves/demonstrates. Must be arguable — if nobody could disagree, it's not a thesis. | Yes |
| **Logic Chain** | Numbered steps showing how the argument unfolds. This becomes the paragraph structure during drafting. | Yes |
| **Key Quotes** | Pre-selected quotes from sources or author's notes that belong in this section. A quote can appear in multiple blocks. | If available |
| **Evidence** | Data, facts, definitions, historical examples that support the logic chain. | If available |
| **Rhetorical Moves** | Analogies, metaphors, one-liners, emotional beats worth preserving in the draft. Not arguments themselves — devices for delivering arguments. | If available |
| **Source Refs** | Inventory item numbers, link numbers, and research item numbers that feed this block. Permanent traceability. | Yes |

---

## 4. When Argument Blocks Are Required

**Threshold rule:** If a sub-chapter's source inventory exceeds **30 items** after Steps 1-3 are complete, Argument Blocks are required at Step 4.

**Under 30 items:** The material is simple enough to organize directly during drafting. Skip the formal block structure — just note the key arguments and sequence in the Step 4 presentation to the user.

**Rationale:** Sub-chapters with fewer than 30 items typically have 3-5 obvious arguments that don't need formal architecture. Above 30, the material becomes complex enough that drafting without structure produces incoherent prose.

---

## 5. Polemic Sequencing

This book is a polemic — arguments build cumulatively toward a crescendo. Argument Blocks must be sequenced for **escalating persuasive impact**, not logical taxonomy.

### Sequencing Principles

1. **Escalating severity.** Start with problems the reader already senses (inflation eroding savings, debt growing). Build toward problems they haven't connected yet (weaponization of FX reserves, debt colonialism in the global south). End with the most outrageous revelation.

2. **Concrete → systemic.** Open with things the reader can feel in their daily life. Move to the structural mechanisms that cause those feelings. Close with the systemic picture that ties everything together.

3. **Problem → mechanism → solution.** Within each block: show the pain first, explain how the system creates that pain, then reveal how Bitcoin addresses it. Not every block needs the Bitcoin resolution — save that for the blocks where it hits hardest.

4. **Plant and payoff.** Early blocks can introduce concepts that later blocks weaponize. If Block 3 defines "cost of capital" and Block 8 shows how broken cost of capital enables corporate welfare, the reader connects the dots with increasing anger.

5. **End on the kill shot.** The final block of each sub-chapter should be the most powerful — the argument or quote that the reader carries away. This is where the author's voice hits hardest.

### Sequencing Anti-Patterns
- **Taxonomy ordering** (alphabetical, by source, by theme letter) — kills momentum
- **Strongest argument first** — nowhere to build toward
- **Bitcoin solution in every block** — becomes repetitive; save it for impact
- **Academic balance** (steelman → counterargument → response) in every block — this is a polemic, not a debate transcript. Steelman where it strengthens the argument, not as a formula.

---

## 6. Example: "The Cost of Capital is Broken"

### Raw Inventory (current catalog items #22-32)
```
22. THE COST OF CAPITAL IS BROKEN
23. Cost of capital = minimum return needed (Investopedia)
24. Encompasses equity and debt, weighted = WACC
25. Projects must exceed cost of capital
26. Artificially low interest rates skew the price of money
27. Therefore the prices of everything else are skewed
28. Stock valuations depend on interest rate
29. Low rates → lower P/E denominator → synthetic stock prices
30. "If we can fix the money..." — Nat Brunell quote
31. Bitcoin fixes the cost of capital
32. A capitalist society needs a base layer of savings
```

11 items. But only **one argument** lives here.

### Argument Block

```
## Block 4: The Cost of Capital is Broken

**THESIS:** Central bank interest rate manipulation corrupts the foundational
price signal of capitalism, making all economic calculation unreliable.

**LOGIC CHAIN:**
1. Cost of capital = the minimum return needed to justify an investment
2. It encompasses both equity and debt (WACC)
3. Central banks artificially suppress interest rates
4. Interest rates are the base variable pricing everything else
   (stocks via P/E, bonds, real estate, all capital allocation)
5. Artificial rates → synthetic prices → broken price discovery
6. Society shifts from saving to reckless spending and risk-chasing
7. Bitcoin restores sound money → real interest rates → functioning markets

**KEY QUOTES:**
- "If we can fix the money, we can actually create a free and open
  market, and a free and open cost of capital, and we can actually get
  efficient productivity happening in the world" — Nat Brunell, Fox Business
- "A capitalist society needs a base layer of savings, not be built on
  a house of cards" — author

**EVIDENCE:**
- Investopedia: cost of capital definition + WACC formula
- P/E ratio mechanics under rate suppression

**RHETORICAL MOVES:**
- "House of cards" metaphor (savings vs debt as foundation)

**SOURCE REFS:** Inventory #22-32 | Links #1 (Investopedia), #2 (Brunell)
```

This block gives you everything needed to write one section of the draft: the thesis is your topic sentence, the logic chain is your paragraph structure, the quotes are pre-selected, and source refs enable Chicago citations.

---

## 7. Building Blocks from Inventory — Process

When constructing Argument Blocks at Step 4:

1. **Read the complete inventory** (all items from Steps 1-3)
2. **Identify core theses** — scan for actual arguable claims. Most sub-chapters will have 10-25.
3. **For each thesis, gather supporting material** from the inventory:
   - Which items provide the logical steps?
   - Which items are quotes that support this?
   - Which items are evidence or data?
   - Which items are rhetorical devices?
4. **Build the logic chain** — number the steps from premise to conclusion
5. **Flag orphans** — inventory items that don't fit any block. These may:
   - Need their own block (missed thesis)
   - Belong in a different sub-chapter (cross-chapter duplicate)
   - Be cuttable (not actually an argument, just noise)
6. **Sequence the blocks** for escalating impact (see Section 5)
7. **Present to user** for review at Step 5

### What Goes in catalog.md After Step 4

The catalog file gets restructured into three parts:
- **Part 1: Argument Blocks** — the structured architecture (draft blueprint)
- **Part 1.5: Amendments** — Step 5 additions (new evidence, quotes, user color, structural changes). Append-only — never edit blocks in Part 1 directly. Merged into blocks at draft time.
- **Part 2: Source Inventory** — the original numbered items (permanent reference index)

**Amendment format:**
- `+Block N` — add to existing block (quote, evidence, logic point, rhetorical note)
- `+Block N.1` — new block that drafts after Block N (use N.2, N.3 for multiples)
- `+Block N: cut` / `+Block N: merge into M` — structural changes
- New inventory items continue sequential numbering at end of Part 2

---

## 8. Relationship to Other Pipeline Files

| File | Role | Relationship to Argument Blocks |
|------|------|-------------------------------|
| `catalog.md` | Contains both Argument Blocks (Part 1) and Source Inventory (Part 2) | Blocks are built from inventory items |
| `sources.md` | Full extracted content from scraped links | Blocks reference specific quotes/data from sources |
| `links.md` | Link registry + bibliography | Blocks reference link numbers for citations |
| `research.md` | Deep research additions | New items feed into inventory, then into blocks |
| `draft.md` | Written sub-chapter | Each block ≈ one section of the draft |
| `voice-dna-profile.md` | Author's voice model | Loaded during drafting (Step 6), not during block construction |

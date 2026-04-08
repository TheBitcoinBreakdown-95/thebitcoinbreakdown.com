# WBIGAF -- Architectural Decisions

> Decisions about structure, process, and strategy that affect the whole book. Each entry records what was decided, why, what was considered, and where it applies. Reverse-chronological.

---

## D10: Refutation System -- Prosecutorial Counter-Argument Handling

**Date:** 2026-03-15
**Scope:** All argument blocks (optional field) + pipeline Step 4 (Refutation Analysis gate)
**Status:** Adopted (v2.2 of argument block model)
**Supersedes:** D7 (Opposition Fallacy field -- fallacy naming absorbed into Refutation's Fallacy sub-field)

### Decision

Replace the Opposition Fallacy field with a structured **REFUTATION** field that handles counter-arguments prosecutorially, not academically. Add a **Refutation Analysis** step to the pipeline (Section 3.3 of the block model) that serves as an analytical gate -- determining which blocks (if any) need refutation before blocks are built.

### The Refutation Field (5 sub-fields)

| Sub-field | Purpose |
|-----------|---------|
| **Placement** | Upfront (within the block -- objection too strong to defer), Inline (woven into argument body), or Deferred (handled later or in kill shot) |
| **The Objection** | Strongest version of the counter-argument at full strength. 1-3 sentences. Not a strawman -- the reader's actual doubt. |
| **What's Conceded** | What the objection gets right. Granting partial validity is what makes it prosecutorial rather than dismissive. Can be empty if nothing is valid. |
| **The Demolition** | Why the objection fails. The trapdoor moment -- the author saw it before the reader did. 2-5 sentences. |
| **Fallacy** | Optional. The logical flaw the opposing position relies on, if one exists. Absorbs the former Opposition Fallacy field. |

### The Refutation Analysis (pipeline gate)

Runs once per sub-chapter, early in Step 4. Four questions per thesis:
1. Is this claim counter-mainstream?
2. What is the strongest objection a skeptical reader would raise?
3. Is the objection strong enough to block reader acceptance?
4. If yes, what placement (Upfront/Inline/Deferred)?

Output: a table in the catalog (after metadata, before Chapter Grid) showing which blocks are flagged, what the counter-argument is, and the approach. Most sub-chapters output "0 blocks requiring refutation."

### Why

**The problem:** The book had no formal structural space for the classical *refutatio* -- the section of an oration where opposing arguments are acknowledged and destroyed. Counter-argument handling was dispersed across three optional mechanisms (Concessive block type, Opposition Fallacy one-liner, Warrant field) with no analytical process determining when any of them should be used. The Opposition Fallacy field named a logical flaw but didn't provide the full counter-argument, didn't concede anything, and didn't demolish -- it was a footnote, not a structural element.

**The risk:** Adding a refutation field to every block could trigger the "academic balance" anti-pattern (Polemic Sequencing Anti-Patterns, Section 5): every argument followed by "but the other side says..." kills momentum, dignifies weak objections, and shifts the author's voice from advocate to referee.

**The solution:** A two-part design that separates the analytical decision (does this block need refutation?) from the execution (the Refutation field itself). The Refutation Analysis is the gate. It runs for every sub-chapter but most output zero. The field itself is prosecutorial: the author introduces the objection (controlling framing and timing), concedes what's valid (building credibility), and demolishes it (the trapdoor moment). This is how a closing argument works in a trial -- the prosecutor raises the defense's argument because they're about to destroy it in front of the jury.

**Scope expectation:** Refutation is primarily needed in Ch3.1 (Fiat Capitalism) and Ch3.2 (Inflation/Cantillon) -- sub-chapters making claims that directly contradict mainstream economic consensus. By Ch3.3 (CBDCs) the reader is primed to distrust the system. By Ch5 (Bitcoin properties) the content is descriptive mechanism, not counter-consensus argument. The book's default posture is constructive: "why Bitcoin is amazing," not "why the critics are wrong."

### What Was Considered

1. **Dedicated Refutatio section (classical)** -- A cluster of 3-5 blocks placed after the full positive case and before the kill shot. Rejected as the sole approach: too rigid. Some objections need to be answered immediately (Upfront) while others can wait. The placement flexibility of the field-within-a-block approach handles both.

2. **Woven refutation (inline only)** -- Counter-argument blocks scattered after each block that provokes an objection. Rejected as the sole approach: breaks escalating momentum by repeatedly pausing to argue defensively.

3. **Hybrid (adopted)** -- The Refutation field within individual blocks handles Upfront and Inline cases. Deferred cases point to later blocks or kill shot sections. The Refutation Analysis prevents overuse. This combines the flexibility of woven refutation with the structural discipline of a gated process.

4. **Keep Opposition Fallacy unchanged** -- Rejected: the field only named a logical flaw. It didn't present the objection, concede what's valid, or demolish. A prosecutorial refutation needs all four elements.

### Anti-Pattern Check

The Refutation Analysis includes a built-in guardrail: if >20% of a sub-chapter's blocks are flagged, the analysis pauses and asks whether the sub-chapter is genuinely that counter-consensus or whether the analysis is being too cautious. 2-4 blocks per 20-block sub-chapter is normal for counter-consensus content. 0 is normal for descriptive content. 8+ is a red flag.

### How to Apply

- **Block model:** See argument-block-model.md Sections 3 (field format), 3.2 (Ref column in Chapter Grid), 3.3 (Refutation Analysis), and 7 (process steps 3c and 5b)
- **Existing blocks:** Blocks with Opposition Fallacy fields get migrated -- the fallacy content moves to the Refutation's Fallacy sub-field, and the full Refutation structure is built out only if the block is flagged by the Refutation Analysis. Unflagged blocks drop the field entirely.
- **Chapter Grid:** Optional Ref column with U/I/D/blank markers
- **Distinct from Concessive block type:** Concessive is when the entire block's argument structure is a preemptive rebuttal. The Refutation field is an optional section within any block type.

### Classical Sources

- Cicero's six-part *dispositio*: Exordium, Narratio, Partitio, Confirmatio, **Refutatio**, Peroratio
- Quintilian's *Institutio Oratoria* on the placement and strategy of refutation
- Trial advocacy: prosecutorial framing of defense arguments (introducing the objection to control its destruction)

---

## D1: Kill Shot Block Structure -- Classical Peroration (3-Part)

**Date:** 2026-03-15
**Scope:** All sub-chapter conclusion blocks (the final "Bitcoin resolution" block in each sub-chapter)
**Status:** Adopted

### Decision

The final block of each sub-chapter (the "kill shot") uses a **3-part structure** based on the classical peroration model (Cicero/Quintilian), sized at 2-3x the word count of a standard argument block.

### The 3 Parts

| Part | Name | Classical Origin | Job | Size |
|------|------|-----------------|-----|------|
| A | **The Indictment** | *Recapitulatio* | Compressed callback chain through the chapter's strongest blocks. Prosecutorial summation, not neutral recap. Each callback framed as a charge. | ~30% |
| B | **The Human Cost** | *Amplificatio* + *Indignatio* | Take the most devastating moral/emotional thread and expand it. This is where the chapter's emotional payload detonates. | ~20% |
| C | **The Exit** | *Conquestio* | Full Bitcoin resolution with mechanism. Each Capital Restorer point names the block it resolves. Ends on the mic drop -- the single strongest quote or image. | ~50% |

### Rhetorical Techniques by Part

**Part A -- The Indictment:**
- **Anaphoric Recapitulation** (callback chain): Repeat a structural phrase while cycling through prior arguments. "When X... when Y... when Z... then what you have is not [what they claim]."
- **Escalating Enumeration**: List consequences in ascending severity. The extension beyond the Rule of Three itself becomes the point.
- **Reductio Stack**: Take the opponent's defenses and collapse them one by one.

**Part B -- The Human Cost:**
- **Thesis Inversion** (Hitchens's move): Shift from "what is" to "what could be." Creates a structural hinge between diagnosis and resolution.
- **Tense Shift**: Move from past/present (diagnosis) to future (vision). Gives the conclusion forward momentum.

**Part C -- The Exit:**
- **Thread Resolution Chain**: Each Bitcoin mechanism point explicitly names the block it resolves, so the reader feels every prior argument clicking into place.
- **Mic Drop Options** (choose one per sub-chapter):
  - The prophetic quote (someone who predicted this moment)
  - The concrete image ("the lifeboat is already in the water")
  - The challenge (addressed to the reader)
  - The inevitability frame ("not if, but when")

### Why This Structure

**Problem:** Kill shot blocks in 3.1 and 3.2 resolved only 14% and 12% of prior blocks' threads respectively. They functioned as philosophical rallying cries but dropped the chapter's strongest evidence, data, emotional arguments, and political framing. The reader gets an inspiring close but no integration of the case that was just built.

**Audit results (March 2026):**
- 3.1 Block 21: 3 of 22 threads fully resolved (59% gap rate)
- 3.2 Block 17: 2 of 16 threads fully resolved (69% gap rate)

**What was considered:**
1. **Single expanded block** -- just making Block 21 bigger. Rejected: a 3x block without internal structure becomes a wall of text. The parts need distinct rhetorical jobs.
2. **Three separate numbered blocks** (21a, 21b, 21c) -- Rejected: fragments the closer's identity. The kill shot should feel like one sustained crescendo, not three separate arguments.
3. **Hegelian pivot** (thesis/antithesis/synthesis) -- Considered viable but less suited to polemic. The peroration is designed for persuasion; Hegel is designed for dialectic.
4. **Classical peroration (4-part)** -- The full Ciceronian model has 4 phases. We merged *amplificatio* and *indignatio* into Part B since the book is already a polemic and every block has been building indignation. 3 parts is cleaner.

**Sources informing this decision:**
- Classical rhetoric: Cicero's *De Inventione*, Quintilian's *Institutio Oratoria*
- Polemic models: Paine (*Common Sense*), Hitchens (*God Is Not Great*), Klein (*The Shock Doctrine*), Rothbard (*What Has Government Done to Our Money?*)
- Bitcoin literature: Ammous, Alden, Gladstein chapter-close patterns

### How to Apply

- Kill shot blocks use the standard argument block format but add a **STRUCTURE** field after the thesis:
  ```
  **STRUCTURE:** Kill Shot (3-Part Peroration)
  - Part A: The Indictment [blocks referenced]
  - Part B: The Human Cost [emotional thread]
  - Part C: The Exit [resolution mechanism]
  ```
- The Chapter Grid marks the kill shot with a note: "Kill shot (3-part peroration)"
- The ARGUMENT BODY is organized under Part A / Part B / Part C headers
- CITATIONS are distributed across all three parts, drawing from the full author roster -- not concentrated on 2-3 voices
- At least 90% of citations come from existing inventory/scraped sources; at most 10% from additional research

### Citation Diversity Rule

The kill shot block must cite authors from across the full chapter, not just the philosophical voices. Specifically:
- Part A (Indictment) leans on data sources, economists, institutions
- Part B (Human Cost) leans on narrative voices, affected populations, moral authorities
- Part C (Exit) leans on Bitcoin thinkers, Satoshi, and the author's voice

No single author should dominate the kill shot. If one author has 5+ citations in a single part, redistribute or replace with equivalent sources from the inventory.

---

## D2: Citation Source Ratio for New Block Construction

**Date:** 2026-03-15
**Scope:** All argument block construction (Step 4 and amendments)
**Status:** Adopted

### Decision

When building or expanding argument blocks, citations should come **~90% from existing inventory and scraped sources**, and **~10% from additional research**. The existing source material was curated intentionally. New research fills gaps, not replaces curation.

### Why

The inventory represents the author's reading and note-taking -- the sources they chose matter for voice and perspective. Over-researching dilutes that curation with generic results. Under-researching leaves real gaps (missing diversity, missing data points). 90/10 balances both.

---

## D3: Author Citation Diversity -- Guidelines, Not Caps

**Date:** 2026-03-15
**Scope:** All sub-chapters
**Status:** Adopted

### Decision

Do not impose arbitrary caps on how many times a thought leader can be cited. If a source is foundational to multiple arguments (e.g., Ammous on time preference, Farrington on capital strip-mining), use them as needed. The concern is **concentration without justification** -- when a single commentator provides the main quoted voice for 5+ blocks and equally strong alternatives exist in the inventory.

**Flags to watch for:**
- One author providing 40%+ of a sub-chapter's citations when the inventory has 10+ other authors
- The kill shot block citing only 2-3 authors when the chapter drew from 15+
- A section that reads like a book report on one person's work

**What to do:** Check the inventory for alternative voices making the same point. If they exist, distribute. If the author genuinely owns that argument (nobody else says it), keep them.

---

## D4: Expanded Argument Type System -- 10 Types (7 Constructive + 3 Combative)

**Date:** 2026-03-15
**Scope:** All argument blocks across all sub-chapters
**Status:** Adopted

### Decision

Expanded from 7 to 10 argument types, adding three **combative** types to complement the existing constructive ones. Also added two variant notes to existing types.

### New Types

| # | Type | Job | When to Use |
|---|------|-----|-------------|
| 8 | **Reductio ad Absurdum** | Demolition -- follow opponent's position to absurd endpoint | Attacking fiat apologia, central bank justifications |
| 9 | **Concessive (Preemptive Rebuttal)** | Defense -- anticipate and dismantle strongest objection | Energy FUD, volatility objections, "tulip" comparisons |
| 10 | **A Fortiori ("If This, How Much More")** | Escalation -- weaponize what the audience already accepts | Counterfeiting analogy, taxation vs. inflation |

### Variants Added

| Base Type | Variant | When |
|-----------|---------|------|
| Causal | **Reveal the Hidden** | Mechanism deliberately concealed (Cantillon, CPI manipulation) |
| Analogical | **Historical Parallel** | Comparing to precedent where outcome is known (Rome, Weimar) |

### Why

The original 7 types are all constructive -- they build affirmative cases. A polemic also needs dedicated tools for destroying opposing arguments (Reductio), defending against the strongest counter-attacks (Concessive), and turning the audience's own beliefs into ammunition (A Fortiori). These three fill distinct structural gaps without overlapping the existing types.

### Sources
- Aristotle's *Rhetoric*, Cicero's *De Inventione*
- Purdue OWL (Toulmin, Classical Argument)
- Stanford Encyclopedia of Philosophy (Aristotle's Rhetoric)
- Internet Encyclopedia of Philosophy (Reductio ad Absurdum)

---

## D5: Warrant Field -- Exposing Hidden Assumptions (Toulmin)

**Date:** 2026-03-15
**Scope:** All argument blocks (optional field)
**Status:** Adopted

### Decision

Add an optional `WARRANT:` field after the thesis in argument blocks. The warrant names the hidden assumption connecting evidence to thesis -- the bridge the reader must cross to accept the argument. Only include when the assumption is contestable or non-obvious.

### Why

The block model had thesis (claim) and evidence (data/grounds) but no mechanism for surfacing the unstated assumption that connects them. In Toulmin's argumentation model (*The Uses of Argument*, 1958), the warrant is where arguments actually break -- if the reader rejects the warrant, the evidence becomes irrelevant regardless of quality. For a polemic, identifying where the audience's bridge is weakest is more valuable than piling on more evidence.

**Example:** Block 5 (Cost of Capital) argues that rate manipulation corrupts price signals. The evidence is Fed rate history. But the *warrant* -- "interest rates should be set by market forces, not institutions" -- is where a Keynesian would attack. Making this explicit ensures the draft addresses the exact point of resistance.

### What Was Considered

1. **Full Toulmin model** (warrant + backing + qualifier) -- Rejected: backing (support for the warrant) and qualifier (degree of certainty) add academic weight without proportional value for a polemic. The warrant alone captures 80% of the insight.
2. **Significance field** (separate "so what?" field) -- Considered but determined to overlap with both the Gift (emotional/intellectual impact) and Conclusion (crystallization). The warrant is distinct: it's about the *hidden assumption*, not the *importance*.
3. **No warrant field** -- Rejected: the gap is real. Without it, blocks can be evidence-rich but assumption-blind.

### How to Apply

- Place after the thesis, before argument type
- One line: "The hidden assumption is..."
- Skip for blocks where the assumption is obvious (e.g., "theft is wrong")
- Especially useful for Concessive blocks (reveals what the strongest objection targets) and blocks where the audience might not share the author's premises

### Sources
- Stephen Toulmin, *The Uses of Argument* (1958)
- Purdue OWL, Toulmin Argument model

---

## D6: Gift Field -- Classical Sententia for Block Impact

**Date:** 2026-03-15
**Scope:** All argument blocks (strongly recommended)
**Status:** Adopted

### Decision

Add a `GIFT:` field between the Argument Body and Conclusion & Transition. The Gift is 1-2 sentences -- the line the reader carries away from the block. The sentence they underline. The moment where the argument stops being information and becomes felt. Tagged by function: Throughline, Register Shift, Reframe, Frisson, or Callback.

### Why

The Conclusion & Transition field was doing two jobs: crystallizing the block's impact *and* bridging to the next block. The crystallization moment -- the blow that lands -- was getting diluted by transition logistics. The Gift gives the block's emotional/intellectual payload its own structural home.

This maps to the classical *sententia* -- the memorable maxim Quintilian recommended placing at the climax of each argument section. The author's voice DNA already has a natural delivery mechanism for sententiae: the one-sentence paragraph drop, the build-punch rhythm, the register oscillation from conversational to prophetic. The Gift field makes this an intentional architectural choice during block construction rather than something that happens (or doesn't) during drafting.

### Gift Types

| Type | What It Does | Example |
|------|-------------|---------|
| **Throughline** | A phrase that echoes forward or backward across blocks, weaving the chapter together | "Every fiat currency dies. Every single one." |
| **Register Shift** | The moment the author's voice goes from educator to prophetic | The build-punch payoff where conversational becomes declaratory |
| **Reframe** | One line that permanently changes how the reader sees the concept | "It's not a free market. It's a free-for-all -- for the people closest to the printer." |
| **Frisson** | Visceral, emotional, makes the hair stand up. Often a fragment or short declarative after a long build | The gut-punch moment |
| **Callback** | Picks up a concept from an earlier block and fires it with new force | Weaponizing a term or idea the reader already absorbed |

### What Was Considered

1. **Significance field** (separate "so what?") -- The Gift subsumes significance but goes further: it's not just why it matters, it's the *felt* version of why it matters. Significance without voice is a textbook summary.
2. **Embedding in Conclusion** -- Status quo. Rejected: the crystallization moment deserves its own spotlight, not a subordinate clause before "which brings us to the next block."
3. **Embedding in Rhetorical Moves** -- Rejected: the Gift is not a device for delivering an argument. It *is* the argument's landing. It's structural, not decorative.

### How to Apply

- Place between Argument Body and Conclusion & Transition
- 1-2 sentences maximum
- Tag the type when intent is clear (Throughline, Register Shift, Reframe, Frisson, Callback)
- Draw from the author's voice DNA: one-sentence paragraph drops, signature phrases, register oscillation, build-punch rhythm
- Strongly recommended for all blocks, but not strictly mandatory -- some blocks are pure mechanism and may not need a Gift

---

## D7: Opposition Fallacy Field -- Attacking the Foundation

**Date:** 2026-03-15
**Scope:** All argument blocks that attack a counter-position (optional field)
**Status:** Superseded by D10 (Refutation field absorbs fallacy naming into a broader prosecutorial structure)

### Decision

Add an optional `OPPOSITION FALLACY:` field to argument blocks. It names the formal or informal fallacy the opposing position relies on, with one sentence showing how the fallacy operates in the specific case. Only for blocks that directly attack a counter-position -- purely constructive blocks skip it.

### Why

The block model had tools for building affirmative arguments (10 argument types) and tools for destroying opposing conclusions (Reductio, Concessive), but no mechanism for attacking the opposing argument's *reasoning process*. Naming the fallacy shows the reader that the counter-position isn't just wrong in its conclusion -- it's structurally flawed in how it arrives there. This is more devastating than counter-evidence because it makes the reader distrust the *method* of the opposition, not just the claim.

This technique has roots in Aristotle's treatment of sophistical refutations and is analogous to what trial lawyers call "attacking the foundation" -- showing the opposing case is built on sand.

### Common Fallacies in WBIGAF

| Fallacy | How It Appears |
|---------|---------------|
| **Circular Reasoning** | "We need the Fed because markets fail" (failures caused by the Fed) |
| **Appeal to Authority** | "All serious economists support X" (consensus as proof) |
| **Begging the Question** | Assuming money must be state-controlled (the thing in dispute) |
| **False Dilemma** | "Either central bank control or chaos" |
| **Moving the Goalposts** | "Transitory" to "manageable" to "healthy" |
| **Composition/Division** | "Good for Wall Street = good for the economy" |
| **Appeal to Consequences** | "If people lose faith in the dollar, everything collapses" |
| **Equivocation** | Using "money" to mean both store of value and medium of exchange |

### What Was Considered

1. **Defensive fallacy tracking** (tracking which fallacies the author avoids) -- Rejected: academic, not useful for a polemic writer. The author's arguments are already structured by the type templates.
2. **Full counter-argument section** -- Rejected: the Concessive argument type already handles steelmanning + dismantling. The Opposition Fallacy is a scalpel, not a second argument.
3. **No fallacy field** -- Rejected: the polemic's power is increased by showing the opposition's reasoning is broken, not just its conclusions.

### How to Apply

- Place after Appeal, before Argument Body
- Name the fallacy (or 2 if they compound)
- One sentence showing how it operates in this specific case
- Skip for purely constructive blocks (~50-60% of blocks will skip this)
- Most useful for: Reductio blocks, Concessive blocks, blocks attacking institutional narratives

---

## D8: Expanded Rhetorical Moves -- Analogies, Micro-Narratives, and Devices

**Date:** 2026-03-15
**Scope:** All argument blocks
**Status:** Adopted

### Decision

Rename `RHETORICAL MOVES` to `RHETORICAL MOVES & DEVICES` and expand the field to explicitly include three categories: (1) teaching analogies, (2) micro-narratives, and (3) devices.

### Why

The original field description ("analogies, metaphors, emotional beats, devices worth preserving in the draft -- not arguments themselves") treated everything as decoration. But teaching analogies are the author's *primary teaching tool* (voice DNA: "the golden tablet, the mushroom, the elephant and the blind monks"). They're load-bearing educational infrastructure, not ornament. Similarly, micro-narratives (2-3 sentence scenarios) make abstract economic concepts personal and concrete.

The Analogical argument type covers blocks where the *entire argument* is an analogy. But many Causal or Logical blocks need a supporting analogy to land -- and there was no explicit home for it.

### The Three Categories

| Category | What It Is | Example |
|----------|-----------|---------|
| **Teaching analogies** | "X is like Y because..." -- grounding the abstract in the concrete | "Airplane without an altimeter" for broken price signals |
| **Micro-narratives** | 2-3 sentence stories or scenarios that make the abstract personal | "Imagine you're a small business owner in 2009..." |
| **Devices** | Metaphors, emotional beats, one-liners, structural devices | "House of cards" metaphor |

### What Was Considered

1. **Two separate fields** (Analogies & Stories / Rhetorical Devices) -- Rejected: adds weight to every block. One field with explicit sub-categories is cleaner.
2. **Keep current field, just update description** -- Almost sufficient, but the rename signals that the field's scope has expanded. Future Claude sessions will treat it differently with the new name.

### How to Apply

- Use the three-category structure in the field: label each item as *Teaching analogy:*, *Micro-narrative:*, or *Device:*
- Teaching analogies are not secondary to the argument -- they're how the argument lands for the reader
- Micro-narratives should feel like the author's voice (conversational, second-person, concrete detail)

---

## D9: Stasis Column in Chapter Grid

**Date:** 2026-03-15
**Scope:** Chapter Grid (Section 3.2 of argument block model)
**Status:** Adopted (optional)

### Decision

Add an optional `Stasis` column to the Chapter Grid. Each block gets one word: Fact, Def (Definition), Quality, or Policy.

### Why

Classical stasis theory (Hermagoras, refined by Cicero) identifies four levels of disagreement. The theory holds that you must win Fact before Definition, Definition before Quality, and Quality before Policy. A Chapter Grid that shows a Policy block appearing before Fact is established may have a sequencing gap.

This is a lightweight diagnostic tool, not a rigid rule. The column is optional -- useful for catching sequencing issues at a glance, skippable when it adds no value.

| Stasis | Question | Book Example |
|--------|----------|-------------|
| Fact | Did it happen? | "Inflation destroys savings" -- is this true? |
| Definition | What is it? | "Is this capitalism or fiat capitalism?" |
| Quality | Is it good/bad? | "Is money printing moral?" |
| Policy | What should we do? | "Adopt Bitcoin as the exit" |

### How to Apply

- Add a Stasis column to the Chapter Grid between Appeal and Narrative Purpose
- Use abbreviations: Fact, Def, Quality, Policy
- Check that Fact/Def blocks generally precede Quality/Policy blocks in the sequence
- Do not force -- some blocks legitimately blend stasis levels

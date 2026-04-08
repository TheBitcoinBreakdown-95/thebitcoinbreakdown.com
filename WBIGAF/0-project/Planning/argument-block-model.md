# Argument Block Model (v2)

> **Purpose:** This document defines how raw source material gets structured into draftable argument architecture. It is the reference for Step 4 (Argument Map) of the sub-chapter pipeline.
>
> **Condensed summary:** See `WBIGAF/WBIGAF.md` Section 4, Step 4.
>
> **v2 changes (March 2026):** Flexible argument types (replacing rigid logic chains), conclusion/transition field, flexible citations, inline source text, cross-chapter refs, Bitcoin resolution control, chapter grid summaries. See Section 3 for the full updated format.
>
> **v2.1 changes (March 2026):** Warrant field (hidden assumptions), Gift field (sententia -- the line the reader carries away), expanded Rhetorical Moves to include teaching analogies and micro-narratives, Opposition Fallacy field (naming the logical flaw in the counter-position), Stasis column in Chapter Grid. See Sections 3 and 3.2.
>
> **v2.2 changes (March 2026):** Refutation field replaces Opposition Fallacy -- structured prosecutorial counter-argument handling (objection, concession, demolition, fallacy) with placement control (Upfront/Inline/Deferred). Refutation Analysis step added to pipeline (Section 3.3) as analytical gate determining which blocks need refutation. Ref column added to Chapter Grid. See Sections 3, 3.2, and 3.3.

---

## 1. Why This Model Exists

During Triage (Step 1), every distinct claim, quote, data point, and observation in the source file gets its own numbered line item. This raw inventory is deliberately granular -- it catches everything. But granular inventory is not argument architecture. A quote is not an argument. A data point is not an argument. A bullet point in a list is not an argument.

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
- **Failure mode:** Not everything is a thesis. In a polemic, arguments build cumulatively -- pure modularity fights the escalating structure needed. Forces artificial containers around non-thesis material.

### Inventory + Map (flat index with clustering layer on top)
- **Strength:** Preserves raw material, flexible grouping
- **Failure mode:** Clusters show *what's related* but not *what the argument is* or *how to present it*. Creates a gap between map and draft that still needs bridging. Two layers to maintain.

### Why Argument Blocks Win
- Separates capture (inventory) from structure (blocks) -- no premature classification during Triage
- Explicitly distinguishes argument components: thesis, argument body, citations, evidence, devices
- Each block maps directly to one section of the draft
- Evidence can appear in multiple blocks via cross-reference
- Source traceability preserved through inventory item references
- Scales across 67 sub-chapters with a consistent format

---

## 3. Argument Block Format

```
## Block [#]: [Title]

**THESIS:** [One sentence -- the core claim being made]

**WARRANT:** [Optional. The hidden assumption connecting evidence to thesis --
the bridge the reader must cross. Only include when the assumption is
contestable or non-obvious. If the reader rejects this, no amount of
evidence matters.]

**ARGUMENT TYPE:** [Primary] / [Secondary if applicable]
**APPEAL:** [Logos | Ethos | Pathos | Kairos]

**REFUTATION:** [Optional. Only when Refutation Analysis (Section 3.3) flags
this block. The book's default posture is constructive -- refutation is the
exception, deployed surgically where the counter-argument is strong enough
to block reader acceptance of the thesis.]
- **Placement:** [Upfront | Inline | Deferred]
- **The Objection:** [The strongest version of the counter-argument, stated
  at full strength. 1-3 sentences. Not a strawman -- the reader's actual doubt.]
- **What's Conceded:** [What the objection gets right, if anything. This is
  what makes it prosecutorial -- you are not afraid of the strongest version.
  Can be empty if nothing is valid.]
- **The Demolition:** [Why the objection fails. The trapdoor moment -- the
  author saw it before the reader did. 2-5 sentences.]
- **Fallacy:** [Optional. The formal or informal fallacy the opposing position
  relies on, if one exists (e.g., Circular Reasoning, Appeal to Consequences,
  Begging the Question). Name it and show how it operates in this specific case.]

**ARGUMENT BODY:**
[Structure adapts based on primary argument type -- see Section 3.1]

**GIFT:**
[1-2 sentences. The line the reader carries away from this block -- the
sentence they underline, the one they quote to someone else. The moment
where the argument stops being information and becomes felt.
Optional tag: Throughline | Register Shift | Reframe | Frisson | Callback]

**CONCLUSION & TRANSITION:**
[1-2 sentences crystallizing the block's core point.
1 sentence bridging to the next block's concern.]

**CITATIONS:**
- "[Quote or direct source language]" -- Source (#inventory-number)
- "[How an expert explains this concept]" -- Source (#inventory-number)
[No count limit. Include as many as the block needs -- 1, 5, or 25.]

**EVIDENCE:**
[Data points, examples, historical facts, definitions that support the argument body]

**RHETORICAL MOVES & DEVICES:**
- **Teaching analogies:** "X is like Y because..." -- grounding the abstract in
  the concrete. Distinct from the Analogical argument type (which is when the
  entire block is an analogy). These are supporting analogies within any block type.
- **Micro-narratives:** 2-3 sentence stories or scenarios that make the abstract
  personal ("Imagine you're a small business owner in 2009...")
- **Devices:** Metaphors, emotional beats, one-liners, structural devices worth
  preserving in the draft. Not arguments themselves -- devices for delivering arguments.

**CROSS-CHAPTER REFS:**
[References to blocks in other sub-chapters. Note whether this block plants a
concept or resolves one planted elsewhere. E.g., "See Ch3.2 Block 4 (Cantillon
mechanism)" or "Plants concept used in Ch5.3 Block 12"]

**BITCOIN RESOLUTION:** [Present | Withheld]
[If Present: 1-2 sentences on how Bitcoin addresses this specific problem.
If Withheld: where the resolution is delivered, e.g., "Resolved in Block 21."]

**SOURCE REFS:** Inventory #X-Y | Links #A, #B | Research #Z

**SOURCE TEXT:**
#X. [Full text of inventory item X]
#Y. [Full text of inventory item Y]
...
[Every inventory item referenced in SOURCE REFS, copied verbatim from Part 2.
Prefixed with item number. This is a convenience copy for human reading --
Part 2 remains the source of truth.]
```

### Field Definitions

| Field | What Goes Here | Required? |
|-------|---------------|-----------|
| **Thesis** | The one-sentence claim this block proves/demonstrates. Must be arguable -- if nobody could disagree, it's not a thesis. | Yes |
| **Warrant** | The hidden assumption connecting evidence to thesis -- the bridge the reader must cross to accept the argument. If the reader rejects the warrant, the evidence becomes irrelevant regardless of quality. Only include when the assumption is contestable or non-obvious. Especially useful for Concessive blocks, where the warrant reveals exactly what the strongest objection targets. | If contestable |
| **Argument Type** | Primary argument type from the ten types in Section 3.1. Optional secondary type if the block blends approaches. | Yes |
| **Appeal** | The dominant classical rhetorical appeal: Logos (logic/reason), Ethos (credibility/authority), Pathos (emotion/values), or Kairos (timeliness/urgency). Tracking this across a chapter ensures persuasive variety. | Yes |
| **Refutation** | Structured prosecutorial counter-argument handling. Replaces the former Opposition Fallacy field. Contains five sub-fields: **Placement** (Upfront -- addressed within the block before or during the argument body, for objections so strong the reader is stuck; Inline -- woven into the argument body as natural preemption; Deferred -- handled in a later block or the kill shot), **The Objection** (strongest version of the counter-argument at full strength, not a strawman), **What's Conceded** (what the objection gets right -- granting partial validity is what makes it prosecutorial rather than dismissive), **The Demolition** (why the objection fails -- the trapdoor moment), **Fallacy** (optional -- the logical flaw the opposing position relies on, if one exists). Only for blocks flagged by the Refutation Analysis (Section 3.3). The book's default posture is constructive; most blocks will not have this field. | If flagged by Refutation Analysis |
| **Argument Body** | The core argument structure. Format adapts to the primary argument type (see Section 3.1 for templates). This becomes the paragraph structure during drafting. | Yes |
| **Gift** | 1-2 sentences -- the line the reader carries away from this block. The sentence they underline, the one they quote to someone else. The moment where the argument stops being information and becomes felt. This is the classical *sententia* -- the memorable maxim placed at the climax of an argument section. Can serve as: a **Throughline** anchor (phrase that echoes across blocks), a **Register Shift** (educator voice goes prophetic), a **Reframe** (one line that permanently changes how the reader sees the concept), a **Frisson** line (visceral, emotional, hair-stands-up), or a **Callback** (weaponizes a concept from an earlier block). Tag the type when the intent is clear. The Gift can draw from the author's voice DNA -- one-sentence paragraph drops, build-punch payoffs, signature phrases, register oscillation. | Strongly recommended |
| **Conclusion & Transition** | Summary of the block's point + bridge to the next block. Block 1 has no backward reference. The final block (kill shot) has no forward bridge -- just closing impact. | Yes |
| **Citations** | Direct quotes, paraphrased expert explanations, and source language that belong in this section. No count limit -- include as many as the block needs. A citation can appear in multiple blocks. Include inventory item numbers for traceability. | If available |
| **Evidence** | Data, facts, definitions, historical examples that support the argument body. | If available |
| **Rhetorical Moves & Devices** | Three categories: (1) **Teaching analogies** -- "X is like Y because..." that ground abstract concepts in the concrete; distinct from the Analogical argument type, which is when the entire block is an analogy; (2) **Micro-narratives** -- 2-3 sentence stories or scenarios that make the abstract personal; (3) **Devices** -- metaphors, emotional beats, one-liners, structural devices worth preserving in the draft. All three categories are tools for delivering arguments, not arguments themselves. | If available |
| **Cross-Chapter Refs** | References to related blocks in other sub-chapters. Prevents duplication across 67 sub-chapters and surfaces throughlines (concepts that recur across chapters). | If available |
| **Bitcoin Resolution** | Whether this block delivers the Bitcoin answer (Present) or withholds it to build tension (Withheld). Explicitly choosing is the point -- this controls when the BTC payoff lands for maximum impact. | Yes |
| **Source Refs** | Inventory item numbers, link numbers, and research item numbers that feed this block. Compact reference line for quick scanning. | Yes |
| **Source Text** | Full text of every inventory item referenced in Source Refs, copied verbatim from Part 2 and prefixed with item numbers. Inline (not collapsible). Convenience copy so a human reader can see all evidence without flipping to Part 2. Part 2 remains the source of truth. | Yes |

---

### 3.1 Argument Type Templates

Ten argument types -- seven constructive (build a case) and three combative (destroy, defend, escalate). Each template shows the recommended ARGUMENT BODY structure for that type. These are starting points, not rigid forms -- most blocks will blend types. Pick the primary type that best describes the block's core approach; note a secondary type if another is significantly present.

#### Logical/Deductive
Numbered premises leading to an inevitable conclusion. The classic logic chain.
```
1. [Accepted premise or established fact]
2. [Second premise or established fact]
3. [Logical step following from 1 and 2]
...
n. [Conclusion -- restates thesis with force]
```

#### Causal
Establishes that A causes B by showing the mechanism, not just correlation.
```
1. [Claim: A causes B]
2. [Mechanism: how A leads to B, step by step]
3. [Evidence the mechanism operates: data, historical precedent]
4. [Rule out alternatives: could C be the real cause?]
5. [Implication: what this causation means for the reader]
```

**Variant -- "Reveal the Hidden":** When the mechanism is deliberately concealed from the public (Cantillon effect, financial repression, CPI manipulation), use this adapted structure:
```
1. [Surface observation: what the reader sees/experiences]
2. [The official explanation: what they're told is happening]
3. [The hidden mechanism: what's actually happening underneath]
4. [Who benefits from the concealment -- and who is harmed]
5. [How the reader can now see through the surface]
```
Note "Causal / Reveal" as the argument type when using this variant.

#### Analogical
Makes the unfamiliar concrete by comparing it to something the reader already understands.
```
1. [Introduce the complex or novel concept]
2. [Draw parallel to a familiar concept: "X is like Y because..."]
3. [Map what holds: where the analogy is accurate]
4. [Acknowledge where the analogy breaks down]
5. [Extract insight: what the comparison reveals]
```

**Variant -- "Historical Parallel":** When comparing the current situation to a specific historical precedent where we know the ending (Roman debasement, Weimar hyperinflation, Continental Dollar). Distinct from standard analogy because the mechanism is identical, not just similar -- and the outcome is known:
```
1. [Describe the historical precedent with specifics]
2. [Map the structural parallels: what was the same situation?]
3. [Show the outcome: how did it end?]
4. [Draw the connection to today: "We are here in the pattern"]
5. [The mechanism is identical -- only the scale has changed]
```
Note "Analogical / Historical Parallel" as the argument type when using this variant.

#### Authority/Credibility
Borrows credibility from trusted, independent sources to establish a claim.
```
1. [State the claim]
2. [Who says it: expert, institution, historical figure]
3. [Why they are credible: background, track record, independence]
4. [What they specifically argue or found]
5. [Convergence: multiple independent sources reaching the same conclusion]
```

#### Statistical/Data
Grounds a claim in measurable, verifiable evidence.
```
1. [Baseline: what the number was before / what "normal" looks like]
2. [Change: what the number is now / the trend]
3. [Context: what does this number mean? Historical comparison?]
4. [Interpretation: what this proves or disproves]
5. [Limitations: what the data does not show]
```

#### Narrative/Anecdotal
Personalizes abstract concepts through human stories that make the reader feel the argument.
```
1. [Setup: introduce a person, place, or situation]
2. [Context: time, stakes, what's at risk]
3. [Event: what happened -- the story]
4. [Impact: what the consequences were]
5. [Meaning: what this story teaches, connected back to the thesis]
```

#### Moral/Ethical
Appeals to the reader's values and principles -- what is right, fair, or just.
```
1. [Name the principle or value at stake]
2. [Why it matters: connection to the reader's worldview]
3. [Violation: how the current system or alternative betrays this principle]
4. [Consequence: what happens when this value is abandoned]
5. [Resolution: how the principle can be honored / restored]
```

#### Reductio ad Absurdum
Takes the opponent's position seriously, follows it to its logical endpoint, and shows the endpoint is absurd or monstrous. The dedicated demolition tool -- distinct from Logical/Deductive because it argues *against* a position rather than *for* one.
```
1. [State the opposing position charitably -- their strongest version]
2. [Accept it as true for the sake of argument]
3. [Follow it to its logical consequences, step by step]
4. [Arrive at the absurd, contradictory, or morally repugnant outcome]
5. [Therefore, the original position cannot hold]
```
*Example:* "If inflation is good for the economy, as central bankers claim, then hyperinflation must be even better. Venezuela should be paradise. It is not. The premise fails."

#### Concessive (Preemptive Rebuttal)
Anticipates the strongest objection to your thesis, states it fairly, and dismantles it before the reader can raise it. Strategic, not academic balance -- used sparingly on the blocks where the counter-argument is strongest. Builds enormous credibility: the reader thinks "that's exactly what I was going to say" and then watches you handle it. **Distinct from the REFUTATION field:** Concessive is when the *entire block's argument structure* is a rebuttal. The REFUTATION field is an optional section within *any* block type that handles a counter-argument surgically without changing the block's primary argument type.
```
1. [State your thesis]
2. [Introduce the strongest objection: "The most common counter is..."]
3. [Grant what is valid in the objection -- do not strawman]
4. [Show where the objection breaks down or is insufficient]
5. [Reassert the thesis, now strengthened by having survived challenge]
```
*Example:* "Bitcoin uses too much energy -- this is the most common objection. The energy use is real. But the objection assumes energy use is inherently wasteful without asking what it secures."

#### A Fortiori ("If This, How Much More")
Argues from an accepted lesser case to an even stronger case that the audience must then accept. Weaponizes the audience's own beliefs. Distinct from Logical/Deductive because it doesn't build from premises -- it leverages an existing concession and escalates.
```
1. [Establish the accepted case: "Even X agrees that..." or "Everyone accepts that..."]
2. [Show why the accepted case is actually the weaker version of the problem]
3. [Introduce the stronger case: "If that's true for X, how much more for Y..."]
4. [Show why Y has the same mechanism but at greater magnitude]
5. [Drive the conclusion: the stronger case is undeniable if the weaker one is accepted]
```
*Example:* "If counterfeiting is a crime when an individual does it -- because it dilutes everyone else's purchasing power -- then how much more criminal is it when a central bank does the same thing at a scale of trillions?"

---

### 3.2 Chapter Grid

Every catalog's Part 1 begins with a Chapter Grid -- a summary table of all blocks plus a narrative arc statement explaining why they are ordered this way.

**Format:**

```markdown
### Chapter Grid

**Narrative arc:** [1-2 sentences describing the emotional/intellectual journey
the reader takes across all blocks in this sub-chapter. What do they feel entering?
What do they believe leaving? How does the sequence get them there?]

| # | Title | Type | Appeal | Stasis | Ref | Narrative Purpose |
|---|-------|------|--------|--------|-----|-------------------|
| 1 | [Block title] | [Primary type] | [Logos/Ethos/Pathos/Kairos] | [Fact/Def/Quality/Policy] | [U/I/D/blank] | [Short phrase: what this block does in the arc] |
| 2 | ... | ... | ... | ... | | ... |
```

**Guidelines:**
- The Narrative Purpose column uses short phrases, not full sentences (e.g., "Reframe: the enemy has a name" or "Make it personal -- your money")
- The grid should make persuasive variety visible at a glance -- if 12 of 17 blocks are Logical/Logos, the chapter may be intellectually dense but emotionally flat
- Update the grid when amendments add new blocks (+Block N.1)
- **Stasis column** (optional): The level of dispute the block engages -- Fact (did it happen?), Definition (what is it?), Quality (is it good/bad?), or Policy (what should we do?). Classical stasis theory holds that you must win Fact before Definition, Definition before Quality, and Quality before Policy. If the grid shows a Policy block before Fact is established, the sequencing may have a gap. Use abbreviations: Fact, Def, Quality, Policy
- **Ref column** (optional): Shows which blocks carry refutation and what placement strategy they use. `U` = Upfront (addressed within the block), `I` = Inline (woven into argument body), `D` = Deferred (handled in a later block or kill shot). Blank = no refutation needed. Most sub-chapters will have 0-3 blocks with refutation markers. If the grid shows refutation in more than ~20% of blocks, the sub-chapter may be drifting toward academic balance -- check whether all flagged blocks truly need it.

---

### 3.3 Refutation Analysis

The Refutation Analysis is the **analytical gate** that determines which blocks (if any) need the REFUTATION field. It runs once per sub-chapter, early in Step 4 (after theses are identified but before blocks are fully built). Its purpose is to prevent refutation from leaking into every block by making the decision explicit and surgical.

**When to run:** Every sub-chapter gets a Refutation Analysis. For most sub-chapters (especially Ch4-8, which describe Bitcoin properties rather than argue against consensus), the expected output is: "Sub-chapter posture: Constructive. Blocks requiring refutation: 0." The analysis takes minutes and confirms the decision rather than leaving it implicit.

**Where refutation is most likely needed:** Sub-chapters making claims that directly contradict mainstream consensus -- particularly Ch3.1 (Fiat Capitalism) and Ch3.2 (Inflation/Cantillon). By Ch3.3 (CBDCs) the reader is primed to distrust the system. By Ch5 (Bitcoin properties) the content is descriptive mechanism, not counter-consensus argument. Refutation need drops off sharply after the first two sub-chapters.

#### The Analysis Process

For each thesis identified in Step 4:

1. **Is this claim counter-mainstream?** Would a smart, educated reader who trusts mainstream economics push back? ("Central banks stabilize markets" is mainstream. "The cost of capital is broken" is counter-mainstream.) If no, skip -- no refutation needed.

2. **What is the strongest objection?** State it at full strength, not as a strawman. What would a skeptical but open-minded reader actually think? (Not "only conspiracy theorists believe..." but "the standard economic argument is...")

3. **Is the objection strong enough to block reader acceptance?** Can the reader continue through the sub-chapter without this being addressed, or will they get stuck? If they can continue (the evidence in the block is sufficient on its own), skip refutation.

4. **What placement?** If refutation is needed:
   - **Upfront** -- the counter-argument is so strong or so common that the reader cannot absorb the block's thesis without it being addressed first. The refutation appears within the block, before or during the argument body. Use when the objection is the first thing the reader will think. ("But central banks prevent recessions...")
   - **Inline** -- the argument body naturally preempts the objection as part of its logic. The refutation is woven in rather than called out separately. Use when the demolition is inherent to the argument structure. (A Causal block that shows the mechanism automatically answers "correlation isn't causation.")
   - **Deferred** -- the objection is better answered after more evidence accumulates, or it's handled in the kill shot's Part A. Use when answering now would slow momentum and the reader can tolerate the doubt temporarily.

#### Output Format

The Refutation Analysis appears at the top of the catalog, after metadata and before the Chapter Grid:

```markdown
### Refutation Analysis

**Sub-chapter posture:** [Constructive | Constructive with surgical refutation]
**Blocks requiring refutation:** [N] of [total]

| Block | Counter-Argument | Strength | Approach |
|-------|-----------------|----------|----------|
| [#] [Title] | [1-sentence strongest objection] | [Strong/Medium] | [Upfront/Inline/Deferred + brief rationale] |

**Blocks NOT requiring refutation:** [Brief statement of why -- e.g., "Remaining
blocks present evidence that speaks for itself, or make claims that are not
counter-mainstream enough to provoke reader resistance."]
```

#### Anti-Pattern Check

If the Refutation Analysis flags more than ~20% of a sub-chapter's blocks, pause and ask:
- Is this sub-chapter actually more counter-consensus than expected?
- Or is the analysis being too cautious -- treating mild skepticism as blocking objections?
- Would some of these blocks be better served by a strong Warrant (revealing the hidden assumption) rather than a full Refutation?

The goal is surgical. 2-4 blocks with refutation in a 20-block sub-chapter is normal for a counter-consensus chapter. 0 is normal for a descriptive chapter. 8+ is a red flag.

---

## 4. When Argument Blocks Are Required

**Threshold rule:** If a sub-chapter's source inventory exceeds **30 items** after Steps 1-3 are complete, Argument Blocks are required at Step 4.

**Under 30 items:** The material is simple enough to organize directly during drafting. Skip the formal block structure -- just note the key arguments and sequence in the Step 4 presentation to the user.

**Rationale:** Sub-chapters with fewer than 30 items typically have 3-5 obvious arguments that don't need formal architecture. Above 30, the material becomes complex enough that drafting without structure produces incoherent prose.

---

## 5. Polemic Sequencing

This book is a polemic -- arguments build cumulatively toward a crescendo. Argument Blocks must be sequenced for **escalating persuasive impact**, not logical taxonomy.

### Sequencing Principles

1. **Escalating severity.** Start with problems the reader already senses (inflation eroding savings, debt growing). Build toward problems they haven't connected yet (weaponization of FX reserves, debt colonialism in the global south). End with the most outrageous revelation.

2. **Concrete to systemic.** Open with things the reader can feel in their daily life. Move to the structural mechanisms that cause those feelings. Close with the systemic picture that ties everything together.

3. **Problem to mechanism to solution.** Within each block: show the pain first, explain how the system creates that pain, then reveal how Bitcoin addresses it. Not every block needs the Bitcoin resolution -- the BITCOIN RESOLUTION field makes this choice explicit.

4. **Plant and payoff.** Early blocks can introduce concepts that later blocks weaponize. If Block 3 defines "cost of capital" and Block 8 shows how broken cost of capital enables corporate welfare, the reader connects the dots with increasing anger. Use CROSS-CHAPTER REFS to track these connections across sub-chapters.

5. **End on the kill shot.** The final block of each sub-chapter should be the most powerful -- the argument or quote that the reader carries away. This is where the author's voice hits hardest. Kill shot blocks use a special 3-part structure (see Section 5.1).

6. **Vary persuasive modes.** Use the Chapter Grid to check that the sub-chapter doesn't rely on a single argument type or appeal for too long. A run of five Logical/Logos blocks benefits from a Narrative/Pathos break. The reader needs emotional rhythm, not just intellectual escalation.

### Sequencing Anti-Patterns
- **Taxonomy ordering** (alphabetical, by source, by theme letter) -- kills momentum
- **Strongest argument first** -- nowhere to build toward
- **Bitcoin solution in every block** -- becomes repetitive; save it for impact (use BITCOIN RESOLUTION: Withheld)
- **Academic balance** (steelman, counterargument, response) in every block -- this is a polemic, not a debate transcript. Steelman where it strengthens the argument, not as a formula.
- **Monotone appeal** -- all Logos or all Pathos. Alternate to keep the reader engaged.

### 5.1 Kill Shot Block Structure (Classical Peroration)

The final block of each sub-chapter -- the "kill shot" -- uses a **3-part structure** based on the classical peroration (Cicero/Quintilian). It is sized at **2-3x the word count** of a standard block. If a typical block's argument body has 5-7 points, the kill shot has 15-20 points organized under three labeled parts.

> **Full decision rationale:** See `decisions.md` (D1: Kill Shot Block Structure)

#### Why a Special Structure

Standard argument blocks make one argument. The kill shot has a different job: it must **integrate every thread** the sub-chapter established, resolve them through Bitcoin, and leave the reader with the single most powerful impression. Audits of existing kill shots (3.1 Block 21, 3.2 Block 17) found they resolved only 12-14% of prior blocks' threads -- functioning as philosophical rallying cries while dropping the chapter's strongest evidence, data, and emotional arguments.

#### The 3 Parts

| Part | Name | Classical Origin | Job | Size |
|------|------|-----------------|-----|------|
| A | **The Indictment** | *Recapitulatio* | Compressed callback chain through the chapter's strongest blocks. Prosecutorial summation. Each callback framed as a charge. | ~30% |
| B | **The Human Cost** | *Amplificatio + Indignatio* | Expand the most devastating moral/emotional thread. This is where the chapter's emotional payload detonates. | ~20% |
| C | **The Exit** | *Conquestio* | Full Bitcoin resolution with mechanism. Each point names the block it resolves. Ends on the mic drop. | ~50% |

#### Kill Shot Block Format

The kill shot uses the standard block format with two additions: a **STRUCTURE** field and a **Part A / Part B / Part C** organization in the argument body.

```
### Block [N]: [Title]

**THESIS:** [The sub-chapter's ultimate claim -- stated at maximum force]

**STRUCTURE:** Kill Shot (3-Part Peroration)
- Part A: The Indictment [list blocks being called back]
- Part B: The Human Cost [name the emotional thread]
- Part C: The Exit [name the resolution mechanism]

**ARGUMENT TYPE:** [Primary] / [Secondary]
**APPEAL:** Pathos (kill shots should land emotionally even when arguing logically)

**ARGUMENT BODY:**

**Part A -- The Indictment**
1. [Callback: Block N thread, compressed to one devastating line]
2. [Callback: Block M thread]
3. [Callback: Block P thread]
...
5-7 callbacks total. Use anaphoric recapitulation ("When X... when Y...
when Z...") or escalating enumeration for rhetorical force.

**Part B -- The Human Cost**
1. [The most emotionally devastating thread, expanded]
2. [Its human consequences, made concrete]
3. [Thesis inversion / pivot: "this is what happens when money is broken.
   Now: what happens when money is fixed?"]

**Part C -- The Exit**
1. [Bitcoin resolution point -- resolves Block A's thread]
2. [Bitcoin resolution point -- resolves Block B's thread]
...
Each point explicitly names the prior block's problem it resolves.
End with the mic drop: one quote, image, or declaration.

**CONCLUSION & TRANSITION:**
[No forward bridge -- this is the closer. Final impact only.]

**CITATIONS:**
[Distributed across all three parts. Draw from the full chapter's author
roster, not just 2-3 philosophical voices.
- Part A: data sources, economists, institutions
- Part B: narrative voices, moral authorities, affected populations
- Part C: Bitcoin thinkers, Satoshi, author's voice]

[All other standard fields: EVIDENCE, RHETORICAL MOVES, CROSS-CHAPTER REFS,
BITCOIN RESOLUTION (always Present), SOURCE REFS, SOURCE TEXT]
```

#### Rhetorical Techniques

**Part A -- The Indictment:**
- **Anaphoric Recapitulation**: Repeat a structural phrase while cycling through prior arguments. Creates a drumbeat that forces the reader to hold all threads simultaneously.
- **Escalating Enumeration**: List consequences in ascending severity. Extend beyond the Rule of Three -- the extension itself becomes the point.
- **Reductio Stack**: Take the opponent's defenses and collapse each one in a single line.

**Part B -- The Human Cost:**
- **Thesis Inversion**: Shift from "what is" to "what could be." Creates a structural hinge between diagnosis and resolution.
- **Tense Shift**: Move from past/present (diagnosis) to future (vision).

**Part C -- The Exit:**
- **Thread Resolution Chain**: Each Bitcoin mechanism point names the block it resolves, so the reader feels prior arguments clicking into place.
- **Mic Drop** (choose one per sub-chapter): prophetic quote, concrete image, challenge to the reader, or inevitability frame.

#### Citation Diversity in Kill Shots

The kill shot must draw from the full chapter's author roster:
- No single author should have 5+ citations within one part
- If the chapter cited 15+ unique authors, the kill shot should reference at least 8-10
- Part A leans on external/institutional authority; Part C is where the author's own voice hits hardest
- At least 90% of citations from existing inventory/scraped sources; at most 10% from new research

#### Thread Coverage Check

Before finalizing a kill shot block, audit it against the Chapter Grid:
1. List every block in the sub-chapter
2. Check whether each block's key thread appears (fully or partially) in Part A, B, or C
3. Target: **80%+ thread coverage** (some minor blocks may not need explicit resolution)
4. If a thread is missing, determine whether it belongs in Part A (callback), Part B (emotional weight), or Part C (Bitcoin resolution)

---

## 6. Example: "The Cost of Capital is Broken"

### Raw Inventory (catalog items #22-32)
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

### Argument Block (v2 format)

```
## Block 4: The Cost of Capital is Broken

**THESIS:** Central bank interest rate manipulation corrupts the foundational
price signal of capitalism, making all economic calculation unreliable.

**WARRANT:** Interest rates should be set by market forces (supply and demand
for capital), not by institutions. If one accepts that central planning of
bread prices fails, the same logic applies to the price of money itself.

**ARGUMENT TYPE:** Causal / Logical
**APPEAL:** Logos

**REFUTATION:**
- **Placement:** Upfront
- **The Objection:** Central bank interest rate policy is necessary to prevent
  economic volatility. Without institutional guidance, rates would swing
  wildly, credit markets would seize, and recessions would be deeper and
  more frequent. This is mainstream macroeconomic consensus.
- **What's Conceded:** Unmanaged rates do fluctuate. Economic cycles are real.
  The desire for stability is legitimate.
- **The Demolition:** The instability cited as justification for rate
  manipulation is itself caused by prior rate manipulation. Each intervention
  creates the conditions that "require" the next intervention. The patient is
  addicted to the medicine that made them sick. Without the ability to
  artificially suppress rates, the bubbles that require emergency rate cuts
  would not form in the first place.
- **Fallacy:** Begging the Question / Appeal to Consequences -- the defense
  assumes markets "need" institutional guidance because unmanaged rates would
  cause instability, but this presupposes that the current instability is
  natural rather than iatrogenic (caused by the treatment itself).

**ARGUMENT BODY:**
1. Cost of capital = the minimum return needed to justify an investment
2. It encompasses both equity and debt (WACC)
3. Central banks artificially suppress interest rates
4. Interest rates are the base variable pricing everything else
   (stocks via P/E, bonds, real estate, all capital allocation)
5. Artificial rates → synthetic prices → broken price discovery
6. Society shifts from saving to reckless spending and risk-chasing

**GIFT:**
Every price in the economy is downstream of the cost of capital. Rig that
one number, and you've rigged everything. [Reframe]

**CONCLUSION & TRANSITION:**
When the most fundamental price signal in capitalism is rigged, every decision
built on top of it -- from corporate investment to personal savings -- is
distorted at the root. This broken cost of capital does not just create
inefficiency; it actively punishes savers, which is exactly what the next
block examines.

**CITATIONS:**
- "If we can fix the money, we can actually create a free and open market,
  and a free and open cost of capital, and we can actually get efficient
  productivity happening in the world" -- Nat Brunell, Fox Business (#30)
- "A capitalist society needs a base layer of savings, not be built on a
  house of cards" -- author (#32)
- "The cost of capital is the minimum rate of return a business must earn
  before generating value" -- Investopedia (#23)

**EVIDENCE:**
- Investopedia: cost of capital definition + WACC formula
- P/E ratio mechanics under rate suppression
- Federal Reserve rate history: zero-bound for 7+ years post-2008

**RHETORICAL MOVES & DEVICES:**
- *Teaching analogy:* "Airplane without an altimeter" -- visceral analogy for
  broken price signals. The pilot (investor) has no reliable instruments.
- *Device:* "House of cards" metaphor (savings vs debt as foundation)

**CROSS-CHAPTER REFS:**
- Ch3.2 Block 3 (How the Money Printer Works) -- mechanism that enables rate suppression
- Ch5.3 (Scarcity) -- Bitcoin's fixed supply as counterpoint to artificial rate manipulation

**BITCOIN RESOLUTION:** Present
Bitcoin restores sound money by removing the ability to artificially suppress
interest rates. With a fixed supply and no central issuer, the cost of capital
reflects actual market conditions rather than political convenience.

**SOURCE REFS:** Inventory #22-32 | Links #1 (Investopedia), #2 (Brunell)

**SOURCE TEXT:**
#22. THE COST OF CAPITAL IS BROKEN
#23. Cost of capital = minimum return needed (Investopedia)
#24. Encompasses equity and debt, weighted = WACC
#25. Projects must exceed cost of capital
#26. Artificially low interest rates skew the price of money
#27. Therefore the prices of everything else are skewed
#28. Stock valuations depend on interest rate
#29. Low rates → lower P/E denominator → synthetic stock prices
#30. "If we can fix the money, we can actually create a free and open market,
     and a free and open cost of capital, and we can actually get efficient
     productivity happening in the world" -- Nat Brunell, Fox Business
#31. Bitcoin fixes the cost of capital
#32. A capitalist society needs a base layer of savings
```

This block gives you everything needed to write one section of the draft: the thesis is your topic sentence, the warrant reveals where the audience might resist, the refutation demolishes the strongest counter-argument before the reader can raise it, the argument body is your paragraph structure, the Gift is the line that lands the blow, the citations are pre-selected with flexible count, the conclusion wraps it up and transitions to the next section, and source text lets you reference the raw material without flipping to Part 2.

---

## 7. Building Blocks from Inventory -- Process

When constructing Argument Blocks at Step 4:

1. **Read the complete inventory** (all items from Steps 1-3)
2. **Identify core theses** -- scan for actual arguable claims. Most sub-chapters will have 10-25.
3. **For each thesis, determine the argument type:**
   - Is this primarily a logical deduction? A causal mechanism? A story? An appeal to authority or values?
   - Pick the primary type from the ten templates (Section 3.1). Note a secondary type if the block blends approaches.
   - Note the dominant appeal (Logos, Ethos, Pathos, Kairos).
3b. **Test the warrant** -- ask: "What must the reader already believe for this evidence to prove this thesis?" If the assumption is obvious (e.g., "theft is bad"), skip the warrant. If it's contestable (e.g., "markets should set interest rates, not institutions"), write it down. The warrant reveals exactly where a skeptic will push back.
3c. **Run the Refutation Analysis** (Section 3.3) -- after identifying all theses, scan for counter-mainstream claims that a skeptical reader would push back on. For each, assess whether the objection is strong enough to block acceptance, and determine placement (Upfront/Inline/Deferred). Output the Refutation Analysis table. Most sub-chapters will flag 0-3 blocks. This step gates which blocks get the REFUTATION field -- blocks not flagged here do not get one.
4. **Gather supporting material** from the inventory for each thesis:
   - Which items provide the argument steps?
   - Which items are quotes or expert explanations that belong as citations?
   - Which items are evidence or data?
   - Which items are teaching analogies, micro-narratives, or rhetorical devices?
   - Include all relevant citations -- there is no count limit. If 8 sources explain this concept well, include all 8. If only 1 quote is relevant, include just 1.
5. **Build the argument body** -- structure it according to the primary type template
5b. **Write the Refutation** (flagged blocks only) -- for blocks flagged by step 3c, write the REFUTATION field. State the objection at full strength. Concede what's valid. Demolish it. Name the fallacy if one exists. The tone is prosecutorial, not academic -- the author anticipated the reader's doubt and is about to handle it. For Upfront placement, the refutation should be written to integrate naturally before or within the argument body. For Inline, it should be woven into the argument body steps. For Deferred, note which later block or kill shot section handles the resolution.
6. **Flag orphans** -- inventory items that don't fit any block. These may:
   - Need their own block (missed thesis)
   - Belong in a different sub-chapter (route via cross-chapter refs)
   - Be cuttable (not actually an argument, just noise)
7. **Sequence the blocks** for escalating impact (see Section 5)
8. **Write the Gift** -- for each block, draft the 1-2 sentence line the reader carries away. Ask: "If the reader remembers one sentence from this block, what is it?" The Gift sits between the argument body and the conclusion -- it's the moment of impact. Tag it: Throughline (echoes across blocks), Register Shift (educator goes prophetic), Reframe (permanently changes how the reader sees it), Frisson (visceral, emotional), or Callback (weaponizes an earlier concept). Draw from the author's voice DNA: one-sentence paragraph drops, build-punch payoffs, signature phrases, register oscillation.
8b. **Write conclusions and transitions** -- this step happens after sequencing, since transitions depend on knowing what comes before and after each block. Block 1 gets no backward reference. The final block gets no forward bridge.
8c. **Build the kill shot block** -- the final block uses the 3-part peroration structure (Section 5.1). After sequencing, audit every prior block's thread and assign each to Part A (callback), Part B (emotional weight), or Part C (Bitcoin resolution). Target 80%+ thread coverage.
9. **Populate source text** -- for each block, copy the full text of every referenced inventory item from Part 2 into the SOURCE TEXT field, prefixed with item numbers.
10. **Set Bitcoin Resolution** -- for each block, explicitly choose Present or Withheld. Review the pattern across the full sequence: if Bitcoin appears in every block, it loses impact. If it never appears until the kill shot, tension may build too long without relief. Find the rhythm.
11. **Add cross-chapter refs** -- scan for concepts that appear in other sub-chapters' inventories or blocks. Note connections to prevent duplication and surface throughlines.
12. **Build the Chapter Grid** -- after all blocks are sequenced and finalized, create the summary table (Section 3.2) at the top of Part 1. Review it for persuasive variety: are argument types diverse? Are appeals varied? Does the narrative purpose column tell a coherent escalating story?
13. **Present to user** for review at Step 5

### What Goes in catalog.md After Step 4

The catalog file gets restructured into three parts:
- **Part 1: Argument Blocks** -- opens with the Chapter Grid, then all blocks in sequence. This is the draft blueprint.
- **Part 1.5: Amendments** -- Step 5 additions (new evidence, quotes, user color, structural changes). Append-only -- never edit blocks in Part 1 directly. Merged into blocks at draft time.
- **Part 2: Source Inventory** -- the original numbered items (permanent reference index)

**Amendment format:**
- `+Block N` -- add to existing block (citation, evidence, argument point, rhetorical note)
- `+Block N.1` -- new block that drafts after Block N (use N.2, N.3 for multiples). New blocks get full v2.2 fields (type, appeal, warrant, refutation if flagged, gift, conclusion, etc.). Update the Chapter Grid when adding new blocks.
- `+Block N: cut` / `+Block N: merge into M` -- structural changes
- New inventory items continue sequential numbering at end of Part 2

---

## 7.1 Upgrade Checklist (Applying New Fields to Existing Blocks)

When upgrading a pre-v2.2 block to the full format (adding Warrant, Gift, Refutation, expanded Rhetorical Moves, merging amendments), follow this checklist to prevent content loss:

### Before Editing

1. **Count original argument body points.** Record the number (e.g., "Block 5: 12 points"). This is the baseline.
2. **Count original citations, evidence items, and rhetorical moves.** Record each count.
3. **If merging amendments:** list every content item in the amendment (argument points, quotes, evidence, rhetorical moves). Each one needs a destination.

### During Editing

4. **Add new fields** (Warrant, Refutation, Gift, rename Rhetorical Moves & Devices with 3 categories). Refutation replaces the former Opposition Fallacy field -- if the block had an Opposition Fallacy, migrate its content into the Refutation's Fallacy sub-field and build out the full Refutation structure (Objection, What's Conceded, Demolition) only if the block is flagged by the Refutation Analysis. If the block is NOT flagged, the Opposition Fallacy content can be dropped -- it was a footnote, not a structural element.
5. **If restructuring the argument body** (e.g., kill shot → 3-part peroration): map every original point to its new location. Every point must appear in one of:
   - The new argument body (same section or different part)
   - Citations (if it was a quote that belongs there instead)
   - Rhetorical Moves & Devices (if it was a device, not an argument)
   - GIFT (if promoted to the sententia)
   - Explicitly cut (with reason noted)
6. **If merging amendments:** integrate each amendment item into its target field. Mark the amendment as MERGED in Part 1.5.

### After Editing — Point-Loss Audit

7. **Re-count argument body points.** New count must be >= original count (minus any explicitly cut) + amendment additions.
8. **Trace check:** For every original argument body point, verify it appears somewhere in the upgraded block. Use this format:
   ```
   Original #1 → Part C #1 (kept)
   Original #3 → Citations (relocated: was a quote)
   Original #11 → CUT (reason: redundant with #8)
   ```
9. **Thread resolution check (kill shots only):** verify every prior block's thread is resolved in Part A, B, or C. Target: 80%+ coverage.
10. **Run the trace check on amendments too** — every amendment item must map to a field in the upgraded block.

### Why This Matters

The v2.1 upgrade restructures blocks, especially kill shots. Restructuring creates opportunities for points to fall through cracks — relocated to "citations" in your head but not on the page, or absorbed into a broader point that loses the specific detail. The trace check catches this mechanically.

---

## 8. Relationship to Other Pipeline Files

| File | Role | Relationship to Argument Blocks |
|------|------|-------------------------------|
| `catalog.md` | Contains Chapter Grid, Argument Blocks (Part 1), Amendments (Part 1.5), and Source Inventory (Part 2) | Blocks are built from inventory items; grid summarizes block architecture |
| `sources.md` | Full extracted content from scraped links | Blocks reference specific quotes/data from sources |
| `links.md` | Link registry + bibliography | Blocks reference link numbers for citations |
| `research.md` | Deep research additions | New items feed into inventory, then into blocks |
| `draft.md` | Written sub-chapter | Each block = one section of the draft |
| `voice-dna-profile.md` | Author's voice model | Loaded during drafting (Step 6), not during block construction |

# Voice DNA Extraction Rulebook

How to extract a full Voice DNA Profile from any single author's corpus. This rulebook codifies the process used to build the TBB Voice DNA Profile and makes it repeatable for any new subject.

**Prerequisites:**
- A corpus of 20,000+ words from the target author (blog posts, essays, scripts, transcripts, etc.)
- Ideally from a single platform or consistent context (reduces noise from format-shifting)
- Raw/unedited material (journals, voice memos, rants) is a powerful supplement but not required for the first pass

---

## Phase 1: Condense the Framework

**Input:** The full Voice DNA Forensic Stylometry methodology (or this rulebook).
**Output:** A working extraction framework scoped to the specific corpus.

### Steps

1. **Scope the L1-L7 model to the corpus.** The seven analysis layers are universal, but what you look for at each layer depends on the corpus type. A single-author blog needs different L1 attention (formatting conventions) than a multi-platform creator (platform-specific adaptations).

2. **Define the deliverables.** The standard set is 8:
   - Voice DNA Card (one-page cheat sheet)
   - Voice Constitution (50-80 do/don't rules with evidence)
   - Reference Tables (synonym preferences, transition preferences, frequency targets)
   - Sentence Skeleton Library (30-50 abstract sentence patterns)
   - Mode Router (primary mode + variants with feature deltas)
   - Production Rewrite Prompt (self-contained system prompt for generation)
   - Evaluation Rubric (yes/no checklist for voice match)
   - Iteration Log (tracking adjustments over time)

3. **Prepare batch analysis instructions.** Divide the corpus into 3-5 batches of roughly equal size. Each batch will be analyzed independently to catch patterns that repeat vs. one-offs.

---

## Phase 2: Batch Analysis (The Scraping Pass)

**Input:** The full corpus, divided into batches.
**Output:** One observation file per batch (e.g., `batch-1-observations.md`).

### Steps

1. **Read each batch closely.** For every batch, read every piece in full. Do not skim. The voice lives in the details -- a habitual comma splice, a recurring sentence opener, a word the author reaches for every time they get passionate.

2. **Extract observations under these headings for each batch:**

```
## L1: Orthography & Visual Style
[Spelling conventions, capitalization habits, emphasis techniques, formatting choices]

## L2: Punctuation & Micro-Prosody
[Punctuation as rhythm -- ellipses, dashes, semicolons, exclamation marks, comma patterns]

## L3: Lexicon & Collocations
[Vocabulary level, favorite words, avoided words, profanity, slang, idioms, recurring phrases, register range]

## L4: Syntax & Sentence Geometry
[Sentence length, complexity, active/passive, fragment usage, sentence starters, parallel constructions]

## L5: Cadence & Paragraph Choreography
[Paragraph length, one-sentence paragraphs, rhythm patterns, white space, build-punch patterns]

## L6: Discourse Strategy & Rhetorical Moves
[Opening strategies, closing strategies, argument structure, analogy use, quote integration, counterargument handling]

## L7: Epistemic Posture & Thinking Style
[Confidence level, hedging, authority signals, reader relationship, stance toward knowledge]

## Signature Sentences
[5-10 sentences from this batch that are most characteristic of the author's voice -- quote directly]

## Phrase Bank (additions)
[Recurring phrases and expressions found in this batch]

## Taboo List (additions)
[Things this author clearly avoids -- words, constructions, tones, devices]
```

3. **Cite specific evidence.** Every observation must point to a specific post or passage. "Uses ellipses" is useless. "Uses ellipses 3-5 times per post for dramatic pauses and trailing-off, e.g., 'And then 14 years later...' (orange-not-gold)" is useful.

4. **Flag contamination.** Identify posts that are:
   - AI-generated or heavily AI-edited (weight their patterns lower)
   - Transcriptions of someone else's speech (not the author's voice)
   - Heavily formatted by a platform or editor (HTML effects, templated content)
   - Atypical in purpose (a listicle from an author who normally writes essays)

5. **Note batch-to-batch consistency.** After batch 2+, explicitly note which patterns from earlier batches are confirmed, which are contradicted, and which are new.

### Batch Size Guidelines

| Corpus Size | Recommended Batches | Posts per Batch |
|-------------|-------------------|-----------------|
| 15-25 pieces | 3 batches | 5-8 |
| 25-40 pieces | 4 batches | 6-10 |
| 40-60 pieces | 5 batches | 8-12 |
| 60+ pieces | 5-6 batches | 10-15 |

### What to Prioritize in Each Batch

- **Batch 1:** Choose the author's most representative, longest, and most voice-rich pieces. These anchor the profile.
- **Middle batches:** Mix of typical and atypical pieces. Look for consistency and edge cases.
- **Final batch:** Include anything unusual -- speeches, transcripts, shorter pieces, drafts. These test whether the patterns hold outside the author's comfort zone.

---

## Phase 3: Synthesis (Building the Profile)

**Input:** All batch observation files.
**Output:** The filled Voice DNA Profile.

### Steps

1. **Merge observations across batches.** For each L1-L7 layer, consolidate all batch observations into a single set of patterns. Patterns that appear in 2+ batches are strong candidates for Constitution rules. Patterns in only one batch are either rare features or noise -- investigate before including.

2. **Write the Voice DNA Card.** This is a ~300-word scannable summary covering these 10 fields:
   - Core Tone
   - Formality Level
   - Persona
   - Favorite Devices
   - Signature Phrases
   - Lexicon
   - Grammar/Punctuation
   - Sentence Style
   - Perspective
   - Rhetorical Moves

   The Card should let someone who has never read the author get the gist in 2 minutes. It is the most-referenced section of the profile.

3. **Write the Voice Constitution.** Convert observations into concrete do/don't rules. Target 50-80 rules organized by L1-L7. Each rule must include:
   - **Signal ranking:** HIGH / MEDIUM / LOW (how diagnostic is this feature? HIGH = if this is wrong, the voice is wrong)
   - **Tier:** Core (every piece) / Secondary (most pieces) / Rare (occasional)
   - **Evidence annotation:** cite the specific post(s) or passage(s)
   - **Format:** `L[N]-[NN] [Tier | Signal]: [Rule]. (Evidence: [source])`

4. **Write the Negative Stylometry section.** What the author NEVER does is as diagnostic as what they always do. List 10-15 absence features with signal rankings. Format: `NS-[NN] [Signal]: Never [pattern]. (Evidence: [absent across N posts])`

5. **Build the Reference Tables:**
   - **Synonym Preferences:** Two-column table (Preferred | Avoided) -- the author's word choices when either option would work in context.
   - **Transition Preferences:** Two lists -- Used transitions (conversational) and Avoided transitions (formal/academic).
   - **Frequency Targets:** Per-~1,000-word targets for key features (ellipses, semicolons, fragments, one-sentence paragraphs, And/But/So starters, contractions, hedge words, active voice, rhetorical questions, direct "you" address, profanity, paragraph length). These make the rules quantifiable.

6. **Build the Sentence Skeleton Library.** Extract 30-50 abstract sentence patterns from the actual corpus, organized by function:
   - Openings and Hooks
   - Build-Up and Pivot
   - Analogy and Explanation
   - Parallel Chains
   - Conviction and Thesis
   - Personal and Confessional
   - Reframe and Escalation
   - Forward Momentum and Closers
   - (Add categories as needed for the author's specific patterns)

   **Format:** `S-[NNN]: "[Pattern with blanks]" -- Usage: [when used]. Example: "[real example from corpus]"`

7. **Build the Mode Router.** Identify the author's primary writing mode and any variants. For each mode:
   - Name and percentage of output
   - Activation trigger (what context activates this mode?)
   - Characteristics (5-10 bullet points)
   - Voice markers present/absent
   - What distinguishes it from the primary mode

   Then build the **Mode Feature Deltas table** -- a grid showing how specific features (fragments, one-sentence paragraphs, register, analogies, "you" address, ellipses, confession, humor, run-ons, self-interruption, conviction level, profanity, parallel chains) change across modes.

   Finally, write **Intra-Piece Routing** rules: when to shift between modes within a single piece, with transition cues.

8. **Write the Production Rewrite Prompt.** A self-contained system prompt that someone can paste into any conversation to write in this voice. Must include:
   - **Generation Workflow** (4 stages: Plan, Draft, Voice, Evaluate)
   - **Core Voice Rules** (tone, sentence/paragraph style, punctuation, teaching, rhetorical moves, signature phrases, word choice)
   - **Anti-Caricature Governor** (distribute features naturally; max 2-3 signature moves per paragraph; concentrate features where they have impact; vary the rhythm)
   - **Anti-Polish Directive** (list specific "errors" that are actually voice features and must not be "corrected")
   - **Content Lock / Meaning Lock** (all source facts must survive voice transformation)
   - **Belief Leakage Prevention** (only express viewpoints present in source material or established corpus)
   - **Taboo list** (constructions the author never uses)
   - **AI-Tell Blacklist** (phrases that instantly mark text as AI-generated)
   - **Corporate Buzzword Blacklist** (if relevant to the author's register)
   - **Sentence Patterns to Use** (5-8 of the most characteristic skeleton patterns)

9. **Write the Evaluation Rubric.** 20-25 yes/no items organized into three groups:
   - **Voice & Style** (one-sentence paragraphs, build-punch rhythm, conversational starters, fragments, analogies, punctuation avoidance, active voice, reader address, emotional investment, register oscillation, etc.)
   - **Content Fidelity** (source facts preserved, nothing omitted, no ungrounded claims)
   - **Consistency & Naturalness** (long-form consistency, AI-tell free, signature phrases natural, cadence variety)

   Include scoring guidance: what score = strong match, needs tuning, or significant mismatch.

10. **Create the Iteration Log.** A table template (Date | Change | Reason | Result) with instructions for updating after each generation session.

---

## Phase 4: Validation

**Input:** The completed Voice DNA Profile.
**Output:** A validation test confirming the profile's accuracy.

### Steps

1. **Generate a test passage.** Using only the Production Rewrite Prompt from the profile, write a ~500-word passage on a topic the author has NOT written about. This tests whether the voice transfers to new content, not just parrots existing posts.

2. **Score against the Evaluation Rubric.** Run every rubric item. Document the score.

3. **Blind comparison test (optional but recommended).** Mix the generated passage with 2-3 real passages by the author. Can a reader (or you, with fresh eyes) tell which is generated? If yes, identify which features are over- or under-represented.

4. **Diagnose failures.** For any rubric items that fail:
   - Trace back to the Constitution rule that should have governed it
   - Determine whether the rule is missing, underweighted, or correctly stated but not followed in generation
   - Update the profile accordingly and log the change in the Iteration Log

5. **Test mode shifts (if applicable).** If the profile has multiple modes, generate a passage that requires a mode shift mid-piece. Verify the transition feels natural and the feature deltas are respected.

---

## Phase 5: Raw Material Supplement (Optional but Powerful)

**Input:** Unedited, informal material -- journal entries, voice memos, rants, speeches, social media posts, messages.
**Output:** Expanded profile covering the author's full register range.

This phase is what separates a good profile from a great one. Published writing is the author's *performing* voice. Raw material reveals the *thinking* and *speaking* voice underneath.

### Steps

1. **Collect raw material.** Anything unedited: spoken-to-mic recordings (transcribed), journal entries, text messages (anonymized), social media rants, speech drafts, unfinished pieces. 5,000+ words is ideal.

2. **Analyze as a separate batch** using the same L1-L7 headings. But pay special attention to:
   - **Register floor:** How casual does the author actually get? (internet slang, verbal tics, profanity frequency)
   - **Self-interruption patterns:** How do they course-correct mid-thought?
   - **Genuine vs. strategic vulnerability:** Do they express real doubt, or only performative doubt?
   - **Thinking rhythm:** Are unfiltered thoughts in long run-on streams, short staccato bursts, or something else?
   - **Humor range:** Is the humor darker, weirder, or more absurd when unedited?

3. **Compare published vs. raw.** Build a comparison table: what features are shared, what exists only in published, what exists only in raw. This reveals the author's editing instincts -- what they polish away is as telling as what they keep.

4. **Expand the profile.** Update the Voice DNA Card, add new Constitution rules, add new sentence skeletons, and add new modes to the Mode Router. Update the Mode Feature Deltas table to cover all modes.

5. **Update the Production Rewrite Prompt** to support the expanded register and modes.

---

## Checklist: Is the Profile Complete?

Before calling the profile done, verify:

- [ ] Voice DNA Card covers all 10 fields
- [ ] Voice Constitution has 50+ rules across L1-L7 with signal rankings and evidence
- [ ] Negative Stylometry has 10+ absence rules
- [ ] Reference Tables include synonym preferences, transition preferences, and frequency targets
- [ ] Sentence Skeleton Library has 30+ patterns organized by function
- [ ] Mode Router has at least a primary mode with characteristics and voice markers
- [ ] Mode Feature Deltas table exists (if 2+ modes)
- [ ] Production Rewrite Prompt is self-contained and includes Anti-Caricature, Anti-Polish, Content Lock, and Taboo sections
- [ ] Evaluation Rubric has 20+ items across Voice, Content, and Consistency categories
- [ ] Iteration Log template exists
- [ ] Validation test has been run and scored
- [ ] All rubric failures have been diagnosed and the profile updated

---

## Common Pitfalls

**Caricature:** Concentrating every signature feature into every paragraph. Real voice is unevenly distributed -- some paragraphs are plain, some are loaded. The Anti-Caricature Governor exists for this reason.

**Polish creep:** "Fixing" intentional voice features (fragments, comma splices, casual grammar) because they look like errors. The Anti-Polish Directive protects these.

**Recency bias:** Weighting the last batch more heavily than earlier ones. All batches should contribute equally unless a batch is flagged as contaminated.

**Ignoring absence:** What the author never does is as diagnostic as what they always do. A profile without Negative Stylometry is incomplete.

**Mode collapse:** Treating the author as having one voice when they actually shift between modes. If the corpus shows distinct registers (teaching vs. storytelling vs. ranting), the Mode Router needs to capture all of them.

**Belief injection:** Inserting opinions or worldview elements that aren't in the corpus. The voice carries the author's perspective, but the profile should only encode perspectives that are evidenced in the writing.

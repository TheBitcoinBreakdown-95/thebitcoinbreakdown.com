# Methodology Insights — Complete Section-by-Section Assessment

Source: `Voice DNA Forensic Stylometry and Production System.md` (1,840 lines, ~37,700 words)
Target: Enriching `voice-dna-profile.md` for a single-author, single-platform Bitcoin blog (28 posts, ~37,000 words)

This document captures what every section of the methodology offers and what's applicable to TBB's specific context. Everything here is for review before any changes are made to the profile.

---

## Section 0: Intake & 10-Pass Pipeline (lines 2-28)

**What it covers:** The overall pipeline for Voice DNA extraction — 10 sequential passes from corpus audit through regression testing.

**What's applicable to TBB:**
- The **4-stage generation pipeline** (semantic plan → structural draft → stylistic infusion → polishing) could structure how we apply voice to guide chapters in Phase 9. Instead of "rewrite in voice," we'd: (1) plan what each section should cover, (2) draft the structure/argument flow, (3) apply voice rules, (4) polish for consistency.
- The **blind comparison target** (≤55% identification accuracy between real and generated text) gives us a concrete quality benchmark.
- Pipeline overview confirms our profile's structure is sound — we've covered passes 1-8 (corpus audit through generation system).

**What to skip:** The pipeline assumes multiple genres (email, blog, academic) — we only have one genre. The segmentation with excerpt IDs (EX-YYYYMMDD-PLATFORM-####) is overkill for 28 posts.

**Specific potential improvements to profile:**
- Add a "Generation Pipeline" note to the Production Rewrite Prompt describing the 4-stage approach

---

## Section 1: L1-L7 Voice Model (lines 29-61)

**What it covers:** The 7-layer voice stack from Orthography through Epistemic Posture.

**What's applicable to TBB:** This is the organizational backbone of our entire profile. Already fully integrated — the Voice Constitution is organized by L1-L7.

**What to skip:** Nothing — fully used.

**Specific potential improvements to profile:** None — already integrated.

---

## Section 2: Corpus Engineering (lines 62-84)

**What it covers:** Techniques for cleaning and preparing the corpus: authorship verification, quoted content detection, de-duplication, temporal drift detection, platform stratification, chunking rules, excerpt storage schema.

**What's applicable to TBB:**
- **Temporal drift detection:** We could note whether the author's voice shifted between 2023-2025 posts. Our batch analysis didn't explicitly track this, but Batch 3 notes suggest the voice is fairly stable. Worth a line in the profile acknowledging voice is consistent across the corpus timeframe.
- **Quoted content detection:** Our batch analysis correctly excluded quoted material (from Satoshi, Antonopoulos, etc.). This is already handled.
- **De-duplication awareness:** Some concepts repeat across the "Bitcoin is X" series. This means those formulations are genuinely high-frequency, not artifacts — strengthens their inclusion as signature phrases.
- **Authorship flags:** We correctly identified "unparalleled-old" and "unparalleled-new" as likely AI-generated and weighted them lower. This aligns with the methodology's authorship purity heuristics.

**What to skip:** Excerpt storage schema with IDs, platform stratification (single platform), mode labeling instructions (single genre), chunking rules for extraction vs generation. All designed for multi-genre, multi-platform corpora.

**Specific potential improvements to profile:**
- Add a brief note in the Voice DNA Card or Constitution about corpus scope and temporal stability

---

## Section 3: Feature Library (lines 85-204)

**What it covers:** 600+ features organized into 8 families, each with detailed format: ID, description, measurement, generation guidance, mode interactions, signal ranking, frequency tier, collision warnings, evidence citations.

**Feature Families:**
- Function Words (60 features)
- Lexicon Preferences (52)
- Punctuation & Orthography (20)
- Cadence & Rhythm (~50)
- Formatting (~50)
- Pragmatics (~50)
- Error Signature (~20)
- Topic-Handling (~30)
- Negative Stylometry (20)

**What's applicable to TBB:**
- **Signal Ranking concept (High/Medium/Low):** Each voice feature has a different diagnostic value. For TBB: ellipses (HIGH), no semicolons (HIGH), register oscillation (HIGH), one-sentence paragraphs (HIGH), fragments (MEDIUM), profanity (MEDIUM — present but not frequent), specific analogies (LOW — content-dependent). Our profile doesn't currently rank features by how diagnostic they are.
- **Frequency Tier concept (Core/Secondary/Rare):** Some features should appear in every piece (Core), some regularly (Secondary), some only occasionally (Rare). For TBB: And/But/So starters = Core; profanity = Rare; "For you see" = Rare.
- **Collision Warnings concept:** What happens when two features activate simultaneously? For TBB: if a sentence is both a fragment AND uses profanity AND is in ALL CAPS, that's too many signature features at once — caricature risk.
- **Negative Stylometry (what the author NEVER does):** The concept of tracking absences as diagnostic features. For TBB: never uses semicolons, never uses em dashes as primary punctuation, never uses formal transitions, never sustains academic register for more than ~3 sentences, never opens with dry exposition, never closes with a summary.

**What to skip:** The specific features shown in the methodology are for a generic hypothetical author (British spelling, no profanity, no exclamation marks, Oxford comma always). Our author is very different. The STRUCTURE is useful; the specific feature values are not.

**Specific potential improvements to profile:**
- Add signal rankings (H/M/L) to Voice Constitution rules
- Add frequency tiers (Core/Secondary/Rare) to indicate how often each feature should appear
- Add a dedicated "Negative Stylometry" section to the Constitution — things the author NEVER does, treated as rules with equal weight
- Add collision warnings for feature combinations that risk caricature

---

## Section 4: Rhetorical Moves Library (lines 205-250)

**What it covers:** 200+ rhetorical moves grouped by function: Opening, Evidence/Explanation, Persuasion/Argument, Narrative/Emotive. Each move has: ID, description, trigger condition, placement, phrase realizations, compatible/incompatible moves, mode deltas, failure modes, evidence citations.

**Moves shown:**
- Opening: Anecdotal Hook, Question Hook, Contextual Scene-Setting
- Evidence: Exemplification, Data Evidence
- Persuasion: Concession & Rebuttal, Devil's Advocate
- Narrative: Self-Deprecating Humor, Vivid Scene Description

**What's applicable to TBB:**
- Our profile already captures many of these moves (L6 Discourse Strategy section) but could be more systematic about **trigger conditions** (when does the author deploy each move?) and **failure modes** (what goes wrong if the move is misused?).
- The concept of **compatible/incompatible move pairs** is useful: steelmanning + immediate pivot works together, but steelmanning + extended agreement doesn't (the author never agrees with the opposition for long).
- The **trigger condition** concept could improve Phase 9 — e.g., "deploy personal confession when the argument has been abstract for 3+ paragraphs."

**What to skip:** The specific move IDs and format are overkill for a single-mode author. We don't need M-0001 through M-0200.

**Specific potential improvements to profile:**
- Add trigger conditions to L6 rules (when does each move activate?)
- Add failure modes to L6 rules (how can each move go wrong?)
- Note move compatibility — which moves pair naturally in TBB's writing

---

## Section 5: Mode Discovery & Router (lines 251-359)

**What it covers:** 15 modes for the generic author (Personal Casual through Q&A/Humor), mode router algorithm, conflict resolution, mode-specific feature deltas.

**What's applicable to TBB:**
- The **mode router logic** (check explicit instruction → infer from content → metadata cues → default) could be useful for Phase 9 within a single chapter — deciding when to shift between Passionate Educator and Dramatic Narrator within different sections.
- The concept that **modes have feature deltas** (what changes between modes) is already in our Mode Router section, but could be more explicit about exactly which features shift and by how much.

**What to skip:** 15 distinct modes are irrelevant — our author has 1 primary mode (Passionate Educator, ~90%) with 1 variant (Dramatic Narrator, ~10%). The multi-genre complexity is unnecessary.

**Specific potential improvements to profile:**
- Add explicit feature deltas to the Mode Router: when shifting to Dramatic Narrator, which specific features increase/decrease?
- Add intra-chapter routing guidance for Phase 9 — when to shift modes within a single long piece

---

## Section 6: Voice DNA Representations (lines 360-404)

**What it covers:** 8 complementary approaches to representing voice: Feature Vector, Rule-Based Constitution, Template/Skeleton Grammar, Rhetorical State Machine, Exemplar Library (RAG), Collocation/Synonym Preference Graph, Cadence Blueprint, Error Signature Policy.

**Key finding:** The methodology itself recommends the **Rule-Based Style Constitution as the PRIMARY representation** — explicit, traceable, adjustable. This is exactly what our voice-dna-profile.md uses.

**Secondary representations used:**
- Exemplar Library (real snippets for style guidance) — we partially do this with batch observation files
- Feature Vector (for post-generation evaluation) — our evaluation rubric serves a similar purpose

**What's applicable to TBB:**
- **Collocation/Synonym Preference Graph:** A graph of the author's word preferences (e.g., "use" over "utilize"). Our profile has some of this in L3 but could be more systematic about mapping preferred → avoided word pairs.
- **Cadence Blueprint:** Representing paragraphs as sentence-length sequences (e.g., [Long, Medium, Short, Long]). Our L5 rules describe this qualitatively — could add quantitative examples.
- **Error Signature Policy:** The author's consistent minor errors (its/it's, loose/lose) are already noted in L1-06, but the concept of NOT over-correcting these in generation (Anti-Polish) is important.

**What to skip:** Feature Vector as a computational tool, Rhetorical State Machine as a formal model — both require infrastructure we don't have. The conceptual insights from each are already captured in simpler forms.

**Specific potential improvements to profile:**
- Add a dedicated synonym preference table (preferred word → avoided word)
- Add cadence blueprint examples (sentence-length patterns for typical paragraphs)
- Reinforce the Anti-Polish principle: don't "fix" the author's intentional quirks

---

## Section 7: Sentence Skeletons (lines 405-483)

**What it covers:** 160+ sentence structure templates grouped by function: Openings, Pivots, Definitions, Emphasis, Examples, Logic, Conclusions.

**What's applicable to TBB:**
- The **functional grouping** (Openings, Pivots, Definitions, Emphasis, Examples, Logic, Conclusions) is a better organizational structure than our current 38 skeletons grouped by thematic/narrative role.
- Skeleton types we haven't captured:
  - **Pivot skeletons:** "X, but Y." / "Although X, Y." / "Not only X, but also Y." — our S-034 captures the last one but we're light on pivot structures.
  - **Definition skeletons:** "X is a Y that Z." / "By X, I mean Y." — we have S-012 and S-013 but could add more.
  - **Logic skeletons:** "If X, then Y." — common in TBB but not templated.

**What to skip:** The specific 160 templates are for a generic author. The organizational principle matters more than the specific patterns.

**Specific potential improvements to profile:**
- Reorganize Sentence Skeleton Library by function (Openers, Build-Up/Pivot, Analogy/Explanation, Parallel Chains, Conviction/Thesis, Personal/Confessional, Closers, Reframe/Escalation, Satoshi/Narrative) — our current grouping is close but could be tightened
- Add any missing functional categories (Pivot, Definition, Logic) with TBB-specific examples

---

## Section 8: Transition Bank (lines 484-565)

**What it covers:** 240+ transitions categorized: Contrast, Addition, Example, Causal, Time/Sequence, Conclusion. Each has context rules, placement, and mode-specific usage.

**What's applicable to TBB:**
- Our profile says "no formal transitions" (L6, Taboo list) but this is too blunt. The methodology shows that ALL authors use transitions — the question is WHICH ones.
- TBB author's actual transitions: And, But, So, The thing is, Here's the part, Now here's where it gets interesting, You see, Look, The point is, In other words
- TBB author's avoided transitions: Furthermore, Moreover, In conclusion, Nevertheless, Consequently, Additionally, In summary, To begin with, Firstly/Secondly/Thirdly

**What to skip:** The 240 specific transitions and their context rules are for a generic author. We only need to document TBB's used vs avoided transitions.

**Specific potential improvements to profile:**
- Add a "Transition Preferences" section (or subsection of L6) listing used vs avoided transitions
- Refine the taboo list to be more specific: it's not "no transitions" but "no FORMAL transitions"

---

## Section 9: Phrase Bank + Taboo List (lines 566-748)

**What it covers:** 600 items: ~250 signature phrases, ~100 preferred synonyms, ~150 collocations, ~50 AI cliches, ~50 corporate buzzwords.

**Key items shown:**
- **Preferred synonyms:** use>utilize, help>assist, about>approximately, many>numerous, get>obtain, have>possess, start>commence, enough>sufficient, buy>purchase, ask>inquire, fix>rectify, because>due to the fact that
- **AI Blacklist:** "As an AI," "In this essay I will discuss," "Firstly/Secondly/Thirdly," "It is important to note that," "in today's society," "throughout history," "needless to say," "ever since the dawn of time," "In a world where," "Due to the fact that," "very unique," "Without further ado"
- **Corporate Blacklist:** synergy, leverage (verb), circle back, think outside the box, paradigm shift, low-hanging fruit, give 110%, core competency, turnkey solution, ideation, incentivize

**What's applicable to TBB:**
- **Synonym preferences are HIGHLY applicable.** The TBB author consistently uses simpler words. Our profile doesn't have a formal synonym table.
- **AI Blacklist is HIGHLY applicable.** Our taboo list covers some of these but not all. Many AI-tell phrases are subtle and worth blacklisting explicitly.
- **Corporate buzzword blacklist** overlaps with our existing "no corporate language" rule but adds specific terms.

**What to skip:** The specific signature phrases, collocations, and their 600-item format. Our corpus-derived signature phrases are already in the profile.

**Specific potential improvements to profile:**
- Add a "Synonym Preferences" table to the Constitution or as a subsection: always prefer the simpler word
- Expand the Taboo list with the full AI-tell blacklist
- Add the corporate buzzword blacklist as a separate category in the Taboo section

---

## Section 10: Generation System & Governors (lines 749-831)

**What it covers:** The 4-stage generation pipeline and its governors: Anti-Caricature Governor, Meaning Lock, Mode Consistency Checker, Cadence Governor.

**What's applicable to TBB:**
- **Anti-Caricature Governor:** Prevents overuse of signature features. Critical for Phase 9. If every paragraph has ellipses, fragments, "Go figure," AND profanity, it becomes parody. The governor ensures features are distributed naturally across the piece, not concentrated.
- **Meaning Lock:** Preserves source content's factual claims through the voice application process. Essential for Phase 9 where we're expanding WBIGAF source material — the facts must survive the voice transformation.
- **Cadence Governor:** Ensures rhythm patterns don't become monotonous. If every paragraph follows the exact same long-long-short-drop pattern, it becomes robotic even if individual features are correct.

**What to skip:** Mode Consistency Checker (minimal relevance with 1-2 modes). The computational implementation details.

**Specific potential improvements to profile:**
- Add an "Anti-Caricature" section to the Production Rewrite Prompt with explicit guidance
- Add a "Meaning Lock" directive: never sacrifice source facts for voice
- Add a "Cadence Governor" note: vary the rhythm patterns, don't repeat the same build-punch sequence identically

---

## Section 11: Control Panel — 80+ Style Knobs (lines 832-1001)

**What it covers:** Quantifiable style parameters organized by L1-L7, each with a numeric range, default per mode, failure modes, and interaction notes.

**Key knobs shown:** Spelling Dialect, Comma Frequency, Serial Comma, Dash vs Parenthesis, Exclamation Use, Question Frequency, Ellipsis Usage, Semicolon Use, Formality, Jargon Level, Idiom Use, Contraction Frequency, Hedge Words, Intensifiers, Sentence Length, Active/Passive, Parallelism, Fragments Allowed, Paragraph Length, Rhythm Variability, Emotional Tone, Humor Level, Certainty.

**What's applicable to TBB:**
- The concept of **numeric frequency targets** instead of binary rules. Some voice features aren't on/off — they have a target frequency. Our profile says things like "use ellipses" and "avoid semicolons" but doesn't quantify HOW OFTEN.
- Estimated TBB targets (per 1,000 words):
  - Ellipses: 3-5 occurrences (frequent)
  - Semicolons: ~0 (virtually never)
  - Exclamation marks: 0-2 (rare, only at peaks)
  - One-sentence paragraphs: 3-5 (frequent)
  - Sentence fragments: 2-3 (moderate)
  - Contractions: always in prose (very high)
  - Hedge words: low (confident voice)
  - Active voice: ~95%
  - Questions: 2-4 (moderate — used as pivots, not barrages)
  - Paragraph length: 1-4 sentences typical, never 8+

**What to skip:** The 80+ individual knob specifications are for a generic multi-mode author. We only need the numeric targets for TBB's specific features.

**Specific potential improvements to profile:**
- Add a "Frequency Targets" section or annotate existing Constitution rules with approximate numeric targets
- This makes the rules more actionable: instead of "use ellipses" → "use ellipses 3-5 times per 1,000 words"

---

## Section 12: Evaluation Rubric — 300+ Dimensions (lines 1002-1113)

**What it covers:** Extensive evaluation framework with 300+ scored dimensions (0-5 scale) across 4 categories: Authorship/Voice Fidelity, Content Fidelity, Language Quality, AI Detection.

**Key dimensions:**
- **D-001 Function Word Profile Match** — statistical comparison of function word usage
- **D-002 Vocabulary Uniqueness** — uses words author uses, avoids words they don't
- **D-006 Signature Phrases** — natural integration of author's phrases, not forced
- **D-007 Overall Voice Consistency** — holistic "would you attribute this to the author?"
- **D-050 Factual Accuracy** — source facts preserved
- **D-051 No Omission** — nothing important dropped
- **D-052 No Ungrounded Claims** — no new facts/opinions injected
- **D-053 Tone Preservation** — attitude/stance maintained
- **D-105 Sentence Variety & Rhythm** — mix of long/short, not monotonous
- **D-150 AI Tell Phrases** — absence of AI-typical constructions
- **D-151 Blind Author Identification** — readers think it's the author
- **D-152 Long-form Consistency** — style doesn't drift in pieces >1500 words

**What's applicable to TBB:**
- Our current 15-item rubric is a simple yes/no checklist. The methodology shows that evaluation can be much more granular.
- **Content fidelity dimensions (D-050 through D-054)** are critical for Phase 9 — we'll be rewriting WBIGAF source material, and the facts/structure must survive.
- **Long-form consistency (D-152)** is essential for 4,000-8,000 word guide chapters — voice must not drift.
- **No ungrounded claims (D-052)** prevents the generation from injecting opinions or facts not present in the source material. This is especially important for educational Bitcoin content.
- **The threshold concept:** Content fidelity all ≥4, key style dims average ≥4, no dimension <3. This gives us a concrete quality bar.

**What to skip:** The full 300-dimension rubric with automated heuristics and human rater instructions. We don't have raters or automated scoring. But the dimensional categories are valuable for expanding our rubric.

**Specific potential improvements to profile:**
- Expand the Evaluation Rubric from 15 to ~20-25 items, adding:
  - Content fidelity checks (facts preserved, nothing omitted, nothing added)
  - Long-form consistency check (style doesn't drift)
  - AI-tell phrase check (expanded beyond current "no formal transitions")
  - Signature phrase naturalness (present but not forced)
  - Cadence variety (not monotonous rhythm)

---

## Section 13: Regression Test Suite — 200+ Cases (lines 1114-1306)

**What it covers:** Test cases organized into: Basic Style Conversion, Content Preservation, Edge Cases/Negative Space, Fail-safe/Governance tests. Each test has: input scenario, expected mode, constraints, forbidden patterns, success criteria.

**Key test types:**
- Basic: formal→voice conversion, casual email, persuasive op-ed
- Content preservation: technical explanations (Meaning Lock), enumeration preservation
- Edge cases: slang handling, spelling consistency, long document drift, redundancy removal
- Governance: taboo phrase enforcement, mode router accuracy, adversarial content (quote isolation)
- **Test 199: Indistinguishability Blind Test** — rewrite author's own text; should come out nearly identical

**What's applicable to TBB:**
- **Taboo enforcement testing:** Verify that generation replaces "utilize" → "use," removes "furthermore," etc. We could build simple spot-checks into our evaluation.
- **Long-form drift testing:** For 4,000+ word chapters, check that voice is consistent from opening to closing paragraphs.
- **Content preservation testing:** WBIGAF source facts must survive voice application. Could test by listing key facts from source, then verifying all appear in output.
- **Quoted text isolation:** When guide chapters include Bitcoin quotes (from Satoshi, Antonopoulos, etc.), the voice should NOT be applied to those quotes — they stay as-is.
- **Test 199 concept (Indistinguishability):** Try running an existing blog post through the Production Rewrite Prompt. If the voice profile is accurate, the output should be very similar to the original.

**What to skip:** The full 200-case regression suite and its automation framework. The test categories and concepts are more valuable than the specific cases.

**Specific potential improvements to profile:**
- Add a "Quality Checks for Phase 9" section or note addressing: content preservation, long-form drift, quote isolation
- Consider adding a brief "Smoke Test" procedure: run one existing post through the prompt and compare

---

## Section 14: Failure Mode Catalog — 80+ Entries (lines 1307-1430)

**What it covers:** Cataloged failure modes with detection criteria, root cause, and fix for each.

**Key failure modes:**
- **FM-0001: Caricature** — overusing signature features until the voice becomes parody
- **FM-0002: Stilted Formality** — too stiff for context
- **FM-0010: Content Omission** — dropping facts from source
- **FM-0020: Wrong Mode** — misclassifying context
- **FM-0030: AI Jargon** — AI self-reference leaking through
- **FM-0040: Over-Polish** — "fixing" intentional voice quirks (fragments, run-ons, ellipses, casual grammar)
- **FM-0100: Evaluation Discrepancy** — metrics say pass but humans feel something's off

**What's applicable to TBB:**
- **FM-0001 (Caricature) is the #1 risk for Phase 9.** The profile has many distinctive features — if they're all turned up to maximum in every paragraph, the writing becomes a parody of itself. The fix: distribute features naturally, not every paragraph needs every signature move.
- **FM-0040 (Over-Polish) is the #2 risk.** AI naturally "corrects" fragments into complete sentences, replaces ellipses with proper punctuation, fixes comma splices, removes profanity. These are features of the voice, not errors.
- **FM-0010 (Content Omission)** is critical for guide chapters — source material facts must not be dropped during voice application.
- **FM-0030 (AI Jargon)** — even with the taboo list, subtle AI-tells can creep in: overly balanced phrasing, hedging where the author would be assertive, "exploring" a topic instead of declaring a position.

**What to skip:** The specific detection algorithms and formal root cause analysis format. The concepts are what matter.

**Specific potential improvements to profile:**
- Add an "Anti-Caricature" section to the Production Rewrite Prompt with explicit guidance: distribute features naturally, don't stack more than 2-3 signature moves in any single paragraph
- Add an "Anti-Polish" directive: do NOT correct fragments, ellipses, comma splices, conversational starters, or minor grammar that's part of the voice
- Add a "Content Lock" directive: facts from source material must all survive the voice application

---

## Section 15: Final Artifacts (lines 1431-1489)

**What it covers:** Defines the format for all 7 deliverables (Voice DNA Card, Constitution, Skeletons, Mode Router, Production Prompt, Rubric, Iteration Log).

**What's applicable to TBB:** Already fully integrated — our profile follows this 7-deliverable structure exactly.

**Specific potential improvements to profile:** None — structure already matches.

---

## Section 16: Synthetic Demo (lines 1490-1620)

**What it covers:** A worked example of the full process: reading input → planning rhetorical moves → drafting in voice → evaluating output. The demo is for a generic author.

**What's applicable to TBB:**
- The **"plan moves before writing" process** could improve Phase 9. Instead of just "rewrite this section in the TBB voice," the process would be:
  1. Identify key content points from WBIGAF source
  2. Plan which rhetorical moves to use for each section (hook type, teaching strategy, pivot points, closer)
  3. Draft in voice
  4. Evaluate against rubric

**What to skip:** The specific demo text and its generic-author application.

**Specific potential improvements to profile:**
- Add a "Generation Workflow" note to the Production Rewrite Prompt describing the plan-then-write process

---

## Appendices A-J (lines 1621-1840)

**What they cover:**
- A: Evidence tagging and traceability
- B: Feature interaction stress tests
- C: Negative space modeling (absence features)
- D: Cross-section consistency (long-form drift detection)
- E: Temporal style changes
- F: Error taxonomy and Anti-Polish governor
- G: Red-team critic and confusion threshold
- H: Belief leakage prevention
- I: Version control for style profiles
- J: Meta-quality bars and refusal conditions

**What's applicable to TBB:**
- **B (Feature interaction stress tests):** Confirms anti-caricature need — activating too many features at once creates artificial writing.
- **C (Negative space modeling):** Reinforces that what the author NEVER does is as important as what they do. Absence features should be tracked.
- **D (Cross-section consistency):** Critical for long-form guide chapters. Provides the concept of checking style vectors across sections of a long piece to detect drift.
- **F (Anti-Polish governor):** The AI's natural tendency to "improve" writing by fixing fragments, removing ellipses, completing sentences, and smoothing grammar. For TBB, this would destroy the voice. The governor ensures these intentional features are preserved.
- **H (Belief leakage prevention):** Don't inject opinions, claims, or viewpoints not present in the source material. Critical for Phase 9 where we're expanding existing content — the expansion should be the author's voice, not AI-generated opinions about Bitcoin.

**What to skip:**
- A (Evidence tagging with excerpt IDs — we cite post names, not formal IDs)
- E (Temporal style — our author's voice is stable across the corpus timeframe)
- G (Red-team critic — useful concept but too heavyweight for our scale)
- I (Version control — single version, no formal versioning needed yet)
- J (Meta-quality bars and refusal conditions — production system feature)

**Specific potential improvements to profile:**
- Add belief leakage prevention to Production Rewrite Prompt: only express viewpoints present in the source material or consistent with the author's established positions
- Reinforce anti-polish in the Taboo section with specific examples of what NOT to "correct"

---

## Summary: All Potential Improvements Compiled

### New sections to potentially add to voice-dna-profile.md:
1. **Negative Stylometry section** — dedicated list of things the author NEVER does
2. **Synonym Preferences table** — preferred → avoided word pairs
3. **Transition Preferences** — used vs avoided transitions
4. **Frequency Targets** — numeric targets for key features per ~1,000 words
5. **Anti-Caricature guidance** — distribute features naturally, max 2-3 per paragraph
6. **Anti-Polish directive** — don't correct intentional voice quirks
7. **Content Lock / Meaning Lock directive** — source facts must survive voice application
8. **Belief Leakage prevention** — don't inject opinions not in source
9. **Generation Workflow** — plan moves → draft → apply voice → evaluate

### Expansions to existing sections:
10. **Signal Rankings** on Constitution rules (H/M/L diagnostic value)
11. **Frequency Tiers** on Constitution rules (Core/Secondary/Rare)
12. **Trigger conditions** on L6 rhetorical move rules
13. **Failure modes** on L6 rhetorical move rules
14. **Mode feature deltas** — explicit list of what changes between Passionate Educator and Dramatic Narrator
15. **Expanded AI-tell blacklist** in Taboo section
16. **Corporate buzzword blacklist** in Taboo section
17. **Expanded Evaluation Rubric** from 15 to ~20-25 items (content fidelity, long-form consistency, AI-tell detection, cadence variety)

### Confirmed/validated approaches:
- Rule-Based Constitution as primary representation ✓ (Section 6 recommends this)
- L1-L7 organizational structure ✓
- 7-deliverable output format ✓
- Existing signature phrases and taboo list ✓ (to be expanded)
- 2-mode router (Passionate Educator / Dramatic Narrator) ✓
- Corpus analysis approach (batch processing, weighted evidence) ✓

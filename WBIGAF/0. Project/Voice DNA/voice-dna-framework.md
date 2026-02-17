# Voice DNA Extraction Framework

Condensed from the full methodology for practical use on a single-author, single-platform Bitcoin blog corpus (28 posts, ~37K words).

---

## The L1-L7 Voice Model

Analyze the author's writing across these 7 layers:

### L1: Orthography & Visual Style
How the text looks on the page. Spelling conventions (American/British), capitalization habits, use of bold/italic/ALL CAPS for emphasis, formatting choices.
- **Look for:** Consistent spelling patterns, capitalization rules (especially "Bitcoin" vs "bitcoin"), visual emphasis techniques, any unconventional formatting.

### L2: Punctuation & Micro-Prosody
Punctuation as rhythm and tone. Comma frequency, dash usage (em dash vs hyphen), ellipses, exclamation/question marks, semicolons.
- **Look for:** Characteristic punctuation patterns, how punctuation creates pacing, emotional punctuation (!, ?!, !!), what punctuation is avoided.

### L3: Lexicon & Collocations
Word choice and common word pairings. Vocabulary level (simple vs complex), favorite words, avoided words, profanity, slang, idioms, recurring phrases.
- **Look for:** Words that appear repeatedly across posts, vocabulary register (casual vs formal), profanity usage, pop culture references, analogies, catchphrases, signature phrases.

### L4: Syntax & Sentence Geometry
Sentence structure patterns. Length and complexity, active vs passive voice, sentence-initial words (And, But, So), fragment usage, parallel constructions.
- **Look for:** Average sentence length, use of fragments for punch, sentence starters, complex vs simple sentence preference, list structures.

### L5: Cadence & Paragraph Choreography
Rhythm and flow at the paragraph level. Sentence length variation, paragraph length, one-sentence paragraphs, white space, pacing patterns (long-then-short for emphasis).
- **Look for:** One-sentence paragraph frequency, paragraph length patterns, rhythm of long/short sentences, how the author builds and releases tension.

### L6: Discourse Strategy & Rhetorical Moves
Higher-level argument and narrative tactics. How topics are introduced, use of questions, counterargument handling, analogies, anecdotes, quotes, definitions, challenges.
- **Look for:** Opening strategies (how posts begin), closing strategies (how they end), use of rhetorical questions, quote integration, analogy patterns, how counterarguments are addressed.

### L7: Epistemic Posture & Thinking Style
Stance toward knowledge. Confidence level, hedging vs assertion, how claims are presented, relationship to the reader, authority signaling.
- **Look for:** Modal verbs (must/might/could), hedging language, confidence markers, how the author positions themselves relative to the reader (teacher, peer, fellow learner), skepticism patterns.

---

## Output Format: 7 Deliverables

### 1. Voice DNA Card (~300 words)
One-page cheat sheet covering: core tone, formality level, persona, favorite devices, signature phrases, lexicon preferences, grammar/punctuation habits, sentence style, perspective, rhetorical moves. Scannable quick reference.

### 2. Voice Constitution (50-80 rules)
Concrete do/don't directives organized by L1-L7. Each rule has a brief evidence note citing specific posts. Format: `L[N]-[NN]: [Rule]. (Evidence: [post name])`

### 3. Sentence Skeleton Library (30-50 templates)
Abstract sentence structure patterns extracted from the actual corpus. Format: `S-[NNN]: "[Pattern with blanks]" — Usage: [when used]. Example: "[real example from corpus]"`

### 4. Mode Router (1-2 modes)
For this single-platform author, identify the primary writing mode and any mild variants. Describe when each mode activates and its distinguishing features.

### 5. Production Rewrite Prompt Template
A ready-to-use prompt that incorporates the Voice DNA Card + key Constitution rules + skeleton examples. Should be self-contained — paste it into a conversation to write in this voice.

### 6. Evaluation Rubric (10-15 items)
Quick checklist for evaluating whether generated content sounds like the author. Yes/no items a reader can verify.

### 7. Iteration Log Template
Simple table template: Date | Change | Reason | Result. For tracking adjustments over time.

---

## Batch Analysis Instructions

For each batch of posts, produce structured observations under these headings:

```
## L1: Orthography & Visual Style
[Observations with specific examples from posts in this batch]

## L2: Punctuation & Micro-Prosody
[Observations with specific examples]

## L3: Lexicon & Collocations
[Observations — list favorite words, recurring phrases, vocabulary level]

## L4: Syntax & Sentence Geometry
[Observations — sentence patterns, fragment usage, starters]

## L5: Cadence & Paragraph Choreography
[Observations — paragraph patterns, rhythm, one-liners]

## L6: Discourse Strategy & Rhetorical Moves
[Observations — openings, closings, argument structure, devices used]

## L7: Epistemic Posture & Thinking Style
[Observations — confidence, hedging, reader relationship]

## Signature Sentences
[5-10 sentences that are most characteristic of this author's voice — quote them directly]

## Phrase Bank (additions)
[Recurring phrases and expressions found in this batch]

## Taboo List (additions)
[Things this author clearly avoids — words, constructions, tones]
```

**Important:** Ignore V4 HTML effects (`<span class="glitch">`, `data-compile`, `class="count-up"`, etc.) — these were added programmatically and are not part of the author's voice.

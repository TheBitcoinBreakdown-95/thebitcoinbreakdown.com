**he Bitcoin Breakdown OS v0.1 — tightened into a “teaching-quality machine”** that stays ultra-light (1–3 hrs/week), local-first, and expandable later without a rebuild.
 
**1) North Star Operating Rules (prevents over-engineering)**  
**Rule 1 — One idea per week.**  
If you do nothing else: **record one clean explanation**.  
**Rule 2 — Teaching comes first.**  
AI may help with **transcripts, summaries, titles, diagrams** — but **never replaces your thinking**.  
**Rule 3 — No daily maintenance.**  
Your system must work even if you ignore it for 2 weeks.  
**Rule 4 — “Drafts are disposable, Published is immutable.”**  
Once recorded, it becomes a permanent artifact. No endless revisions.  
**Rule 5 — Timebox everything.**  
If the clock runs out, you ship the _best current version_, not the perfect one.
 
**2) Tool Stack (cheap, local-first, professional enough)**  
**Foundation (Week 1)**

- **Obsidian** (local Markdown vault; not open-source, but local + free tier)
    - If you want fully open-source: **Logseq** is the closest substitute (also local-first).
- **OBS Studio** (recording)
- **Slides**: LibreOffice Impress (open-source) or Google Slides (frictionless)

**Phase-2 Add-ons (only after habit forms)**

- **whisper.cpp** (local transcription) _or_ OpenAI Whisper via a simple UI
- **LosslessCut** (open-source trimming) for “remove the dead air” edits
- **DaVinci Resolve** (if you _later_ want real editing, optional)
 
**3) Obsidian Vault Structure (clean separation: Research → Thinking → Teaching → Publishing)**
 
bitcoin-breakdown/￼├── 00_inbox/ # raw links, questions, sparks￼├── 10_research/ # source notes (quotes, links, evidence)￼├── 20_thinking/ # your synthesis, mental models, arguments￼├── 30_lessons/ # speakable outlines (teaching-ready)￼├── 40_published/ # immutable records + links￼├── 50_assets/ # slide exports, diagrams, thumbnails￼└── 99_meta/ # workflows, templates, rubrics, prompts￼  
**What this solves:** you’ll never confuse “I collected links” with “I understand it,” and you’ll never confuse “I understand it” with “I can teach it.”
 
**4) The Weekly Workflow (1–3 hours, step-by-step)**  
**Step A — Pick ONE teachable question (10 minutes)**  
From **00_inbox**, choose the one that passes this filter:  
**“Could I explain this to a smart friend in 10 minutes without notes?”**

- If _no_ → it’s **Research week** (don’t record yet).
- If _yes-ish_ → proceed.

Create a single lesson note in **30_lessons/** using the template below.
 
**Step B — Build a Speakable Outline (15–25 minutes)**  
**No prose. No scripting.** Just headings + bullets.  
Your “default teaching sequence” (learning-science friendly):

1. **Problem** (why do we care?)
2. **Naive intuition** (what most people assume)
3. **Failure case** (why the naive view breaks)
4. **Correct model** (the one you’re teaching)
5. **Check for understanding** (2–3 quick questions)
6. **Common misconceptions** (pre-bunk)
7. **One-minute recap** (compress it)

This structure forces clarity and makes you a better teacher fast.
 
**Step C — Record (30–60 minutes)**

- One take, minimal pressure.
- Slides or blank whiteboard.
- Teach like you’re tutoring **one attentive person**.

**Teaching quality hack:**  
At the end, do a **60-second “recap from memory”**. That becomes your short summary later.
 
**Step D — Archive (10 minutes)**  
Move the lesson note into **40_published/** and add:

- YouTube link (unlisted is fine)
- 3–5 bullet “truths learned”
- 2 misconceptions students will likely have
- 2 follow-up questions for next week

Done.
 
**5) Obsidian Templates (copy/paste)**  
**A) Inbox item (00_inbox/)**  
**Filename:** YYYY-MM-DD - spark - \<topic\>.md

- Source / link:
- One-line question:
- Why it matters (1 line):
- Confusion point (what I don’t get yet):
- Tags:
 
**B) Research note (10_research/)**  
**Filename:** source - \<name\> - \<topic\>.md

- Claim(s) made:
- Evidence / quote snippets (bullets):
- What I trust / don’t trust:
- How it connects to Bitcoin Breakdown:
- Link:
 
**C) Thinking note (20_thinking/)**  
**Filename:** \<topic\> - synthesis.md

- My current explanation (bullets, not prose)
- The mental model / analogy
- Where people get stuck
- “If this is true, then…” implications
- Open questions
 
**D) Lesson outline (30_lessons/)**  
**Filename:** Lesson - \<topic\> (v0).md  
**Header**

- Title:
- Target audience (new / intermediate):
- Goal (one sentence):
- Prereqs (max 3):
- Runtime target (10–20 min):

**Outline**

1. The problem (1–3 bullets)
2. Naive model (what people think)
3. Why it fails (the trap)
4. Correct model (the core)
5. Walkthrough example (simple)
6. Misconceptions (pre-bunk)
7. Checks for understanding (2–3 questions)
8. 60-second recap (bullet version)

**Slide prompts (optional)**

- Slide 1: problem picture
- Slide 2: naive model diagram
- Slide 3: failure case
- Slide 4: correct model
- Slide 5: example
- Slide 6: recap
 
**E) Published record (40_published/)**  
**Filename:** Published - YYYY-MM-DD - \<topic\>.md

- YouTube link:
- Version notes (what changed vs last time):
- 3–5 takeaways:
- Misconceptions corrected:
- Next lesson candidate(s):
- Assets used (slides link / file):
 
**6) “Rules of Use” (so it stays lightweight forever)**  
**The 4 Do’s**

- Do keep **00_inbox messy**.
- Do keep lessons **bullet-only**.
- Do record even when it’s “not perfect.”
- Do capture misconceptions + checks-for-understanding every time.

**The 4 Don’ts**

- Don’t build automation until you have 4 published lessons.
- Don’t polish visuals before the explanation is crisp.
- Don’t turn outlines into scripts.
- Don’t expand platforms until consistency is effortless.
 
**7) How this improves teaching skill (not just output)**  
Every lesson must include:

- **A failure case** (why naive thinking breaks)
- **2 checks-for-understanding**
- **2 misconceptions**
- **A one-minute recap**

That’s basically a built-in loop for:

- clearer mental models,
- better sequencing,
- retrieval practice,
- and audience error-correction.

If you only add _one_ “teaching science” element, make it **checks-for-understanding**.
 
**8) Later: where n8n fits (without messing up the system)**  
Only after habit + archive exist:  
**n8n “safe” automations (low risk)**

- If a YouTube upload happens → create a **Published note stub** in 40_published/
- If a link is saved (Pocket/RSS/email) → append to 00_inbox/
- If a transcript file appears in a folder → drop summary into the Published note

**AI assists (still teaching-first)**

- Transcript → **3 bullet summary + 5 title options + 5 chapter timestamps**
- Outline → **slide text suggestions**
- Lesson → **diagram prompt for a single visual** (not a whole design project)
 
**9) Your weekly cadence options (pick one and never change it)**  
**Option 1: “One Session Saturday” (best for 1–2 hrs)**

- 10m pick question
- 20m outline
- 40m record
- 10m archive

**Option 2: “Two tiny sessions” (best for consistency)**

- Session 1 (30m): pick + outline
- Session 2 (45–60m): record + archive
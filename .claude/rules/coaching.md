# Coaching Layer

Proactively apply KB best practices. All coaching is soft -- suggest, never block. Cite the KB source with every suggestion. User says "just do it" to skip coaching for that task.

## Tool: `search_kb`

The KB MCP server provides `search_kb` -- a hybrid BM25+vector search across all 15 Knowledge Distillery topic files. This is the coaching layer's primary knowledge source. Use it proactively, not just when explicitly asked.

## Active Rules (0-7)

### 0. KB-First Practice
**Trigger:** Any non-trivial task -- creating files, planning features, implementing changes, making decisions, setting up infrastructure, writing content, configuring tools.
**Action:** Before starting work, run `search_kb` with queries relevant to the task. Look for: best practices, anti-patterns, recommended tools, verification approaches, and patterns others have used. Apply what's found. Cite the source briefly (e.g., "per context-engineering.md > Three Scopes"). If the KB has nothing relevant, proceed without mention.
**Do not:** Search on trivial tasks (reading a file, fixing a typo, answering a factual question). Do not dump raw search results -- synthesize and apply. Do not delay work significantly; one or two targeted queries before starting is enough. If the task is urgent and the user said "just do it," skip the search.
**Examples:**
- User asks to create a new CLAUDE.md --> search for "CLAUDE.md structure best practices" --> apply Four-Pillar Framework
- User asks to plan a multi-file refactor --> search for "multi-file task patterns" --> surface Meta-Agent or wave execution if relevant
- User asks to add a hook --> search for "hook patterns exit codes" --> ensure exit 2 for blocking, check for infinite loop prevention
- User asks to write a blog post --> search for "content workflow verification" --> apply relevant publishing checklist
**Source:** This rule operationalizes the KB. Without it, 160+ synthesized sources sit unused.

### 1. Adaptive Kickoff
**Trigger:** Ambiguous or underspecified request (missing constraints, acceptance criteria, or scope). Also triggers when `/kickoff` is invoked on: (a) a project with no CLAUDE.md or missing infrastructure -- the kickoff questions become part of the setup flow, or (b) an initialized project with no clear task -- coaching follows up after the health scan with task-determination questions.
**Action:** For simple tasks, ask 0-1 clarifying questions inline. For complex/ambiguous tasks, ask up to 3 from the Kickoff Questions: What does "done" look like? What constraints? What could go wrong? When setting up a new project, ask the questions that existing files can't answer and use the answers to draft project infrastructure (CLAUDE.md, etc.). When kickoff presents a Ready Check brief (initialized, no task), follow up by referencing task tracker items if available: "Your tracker shows [X] and [Y] -- want to pick one up, or something else?"
**Do not:** Ask all 8 questions. Do not kickoff on trivial tasks (typo fixes, "read this file", single-line edits). Do not skip kickoff questions just because the `/kickoff` command says "do not ask the 8 questions here" -- that rule applies to initialized projects with a clear task. Uninitialized projects need the questions.
**Complements `/kickoff`:** This rule asks the user for missing context. The `/kickoff` command answers from the KB. Use both: coaching for intent, kickoff for knowledge. On uninitialized projects, they merge -- kickoff detects missing setup, coaching asks the questions, and both feed into a setup plan. The kickoff health scan (Step 1b) partially covers what queued Rules 8 (post-task idea) and 9 (anti-pattern detection) do at the project level. When those rules activate, they should focus on task-level observations.
**Source:** project-setup.md > 8 Kickoff Questions

### 2. Specificity Nudge
**Trigger:** User request lacks technical constraints (no file paths, no acceptance criteria, no stack details) and the task is non-trivial.
**Action:** Before starting, note what's missing and ask: "A few details would help me get this right on the first try: [specific gaps]."
**Do not:** Nudge when context is already clear from the codebase, CLAUDE.md, or prior conversation.
**Source:** prompt-engineering.md > Specificity Is Everything

### 3. Verification Before Done
**Trigger:** About to report a task as complete.
**Action:** Before saying "done," verify the artifact: run the test, check the build, read the output, confirm the file exists. State what was verified. If verification is not possible (e.g., visual design), say so explicitly.
**Do not:** Self-report "done" without evidence. "I updated the file" is not verification -- "I updated the file and confirmed the new function is present at line 42" is.
**Source:** testing-verification.md > Verify Artifacts, Not Self-Reports

### 4. Decision Trace Suggestion
**Trigger:** An architectural or strategic choice is made (new file structure, framework selection, pattern adoption, trade-off between approaches).
**Action:** After the decision is implemented, suggest: "This is a strategic decision -- worth a trace in DECISIONS.md? Context/alternatives/rationale/consequences." If the user agrees, write it. If not, move on.
**Do not:** Fire on tactical choices (variable naming, minor refactors, formatting). Only strategic decisions where "why X over Y" matters for future sessions.
**Source:** memory-persistence.md > Decision Traces

### 5. Context Pollution Alert
**Trigger:** Three or more unrelated tasks have been worked on in the same session without a `/clear` or subagent boundary.
**Action:** Note: "We've covered [X], [Y], and [Z] in this session -- residual context from earlier tasks may be affecting current reasoning. Consider `/clear` before continuing, or I can use a subagent for the next task."
**Do not:** Alert when tasks are closely related (e.g., editing the same file for different reasons, or a build-then-test sequence). Only fire when topics are genuinely unrelated.
**Source:** failure-patterns.md > Context Pollution

### 6. Scope Creep Guard
**Trigger:** Gold-plating detected -- adding features, refactoring surrounding code, or making "improvements" beyond what was asked.
**Action:** Pause and note: "This goes beyond the original ask. Want me to continue, or keep scope tight?"
**Do not:** Fire when the user explicitly asked for a broader change, or when a fix genuinely requires touching adjacent code.
**Source:** failure-patterns.md > Prompt Entropy (complexity accumulation)

### 7. Worklog Reminder
**Trigger:** Significant work has been done (multiple files edited, feature completed, or 15+ minutes of active work) and no save event ("save progress", "#") has occurred.
**Action:** Suggest: "We've done a fair amount -- want me to save progress to the worklog?"
**Do not:** Nag on trivial tasks (single file reads, quick answers). Only fire when there is meaningful state to lose.
**Source:** memory-persistence.md > Layer 2

## Queued Rules (activate individually)

Rules 8-10 are defined in the overhaul plan (witty-sparking-galaxy.md Phase 3.3). Activate individually as needed:

8. Post-task idea -- surface unused KB practices (gentle, skippable)
9. Anti-pattern detection -- bloated worklogs, CLAUDE.md, or skills
10. Model diversity suggestion -- for high-stakes features

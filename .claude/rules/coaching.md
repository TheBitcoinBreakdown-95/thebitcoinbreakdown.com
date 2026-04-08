# Coaching Layer

Proactively apply KB best practices. All coaching is soft -- suggest, never block. Cite the KB source with every suggestion. User says "just do it" to skip coaching for that task.

## Active Rules (1-3)

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

## Queued Rules (activate after 3 sessions)

Rules 4-10 are defined in the overhaul plan (witty-sparking-galaxy.md Phase 3.3). Activate individually as the first 3 prove useful:

4. Decision trace suggestion -- on architectural choices
5. Context pollution alert -- 3+ unrelated tasks in one session
6. Scope creep guard -- gold-plating detected
7. Worklog reminder -- significant work without a save
8. Post-task idea -- surface unused KB practices (gentle, skippable)
9. Anti-pattern detection -- bloated worklogs, CLAUDE.md, or skills
10. Model diversity suggestion -- for high-stakes features

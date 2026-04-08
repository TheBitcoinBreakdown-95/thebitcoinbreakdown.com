---
description: Design or run a Meta-Agent Orchestration system. Analyzes project suitability, guides coordinator setup in planning mode, or dispatches tasks if a tracker already exists.
---

Design or operate a Meta-Agent Orchestration (Coordinator Pattern) system for the current project. Auto-detects mode based on whether a task tracker already exists.

## What This Is

A coordinator agent handles task decomposition, dispatch, and review -- so you stop being the manual dispatcher between parallel workstreams. You describe a goal, the coordinator reads project state, identifies parallelizable work, writes scoped task briefs for executor agents, and reviews their output. You make decisions at gates. Everything between gates runs without you routing it.

Design for 3-4 parallel executors, not more. Accuracy saturates past 4 concurrent agents. See Reference section for principles and research. -- *agent-design.md > The Coordination Tax*

---

## Usage

`/coordinator` -- Auto-detects mode based on project state.

`/coordinator plan` -- Force planning mode (design a new coordinator system).

`/coordinator dispatch` -- Force dispatch mode (read tracker, identify next tasks).

---

## Instructions

### Step 1: Understand the Project

Read the nearest CLAUDE.md. Extract:

- **What is this project?** (app, book, course, content pipeline, tool, etc.)
- **What is the repeatable unit of work?** (feature, chapter, module, endpoint, sub-page, etc.)
- **How many units exist?** (total count and how many are in progress)
- **What is the pipeline per unit?** (the steps each unit goes through from start to done)
- **What steps are independent?** (can two units be at the same step simultaneously?)
- **What steps require human input?** (external research, approval, subjective review)

Also read any existing status/progress tracker (WORKLOG.md, STATUS.md, TODO.md, or equivalent).

### Step 2: Suitability Check

Not every project benefits from a coordinator. Evaluate against these criteria:

**Good fit (need 3+ of these):**

| Signal | Why it matters |
|--------|---------------|
| 3+ repeatable units following the same pipeline | Parallelism has enough surface area to justify coordination overhead |
| 3+ pipeline steps per unit | Enough structure for a state machine, not just a checklist |
| Units are independent at most steps | Work can actually run in parallel without blocking |
| Human coordination is already the bottleneck | You spend more time dispatching than the agents spend working |
| Work spans multiple sessions | State persistence between sessions adds value |
| Strategic and tactical concerns compete for attention | Vision Compression risk is real |

**Bad fit (any one of these is disqualifying):**

| Signal | Why | Source |
|--------|-----|--------|
| Fewer than 3 units of work | Coordination overhead exceeds benefit -- just do them sequentially | agent-design.md > When to Use Which Architecture |
| All steps are sequential with hard dependencies | Nothing can parallelize -- coordinator adds cost without speed | agent-design.md > Agent Teams > When to Use vs Sub-Agents |
| Units require the same files | One-writer rule violations are inevitable | failure-patterns.md > Concurrent File Editing |
| Single-session scope | No state persistence needed -- a todo list is sufficient | workflow-patterns.md > Pattern 3 |
| The work is exploratory/undefined | You can't dispatch what you can't specify | workflow-patterns.md > RPI When NOT to Use |

> **Note:** 3-5 units may benefit from coordination, but the overhead is marginal. Consider whether a simple task list with `/kickoff` for each item would suffice.

**If the project is a bad fit**, say so clearly:

```
This project doesn't need a coordinator system. [Reason from the table above.]

What would work better: [alternative -- e.g., "a simple task list with /kickoff for each item",
"subagents within a single session for the parallel research steps",
"the RPI workflow pattern for this single complex feature"].
```

Then stop. Do not proceed with planning.

**If the project is a good fit**, state what makes it suitable (cite the signals) and proceed to Step 3.

### Step 3: Detect Mode

Look for a file with one of these names: `TRACKER.md`, `DISPATCH.md`, `workstreams.md`, `STATE.md`, `STATE.yaml`. Also check whether the project's CLAUDE.md names a custom tracker file -- if so, look for that file too.

Do not pattern-match arbitrary files for tracker-like fields. Only named tracker files trigger dispatch mode.

- **If found** --> Dispatch Mode (Step D1)
- **If not found** --> Planning Mode (Step P1)
- **If `/coordinator plan` was invoked** --> Planning Mode regardless
- **If `/coordinator dispatch` was invoked** --> Dispatch Mode regardless (error if no tracker)

---

## Planning Mode

Planning mode is interactive. Ask questions, wait for answers, iterate. Do not dump a complete design at once.

### Step P1: Pipeline Discovery

Ask the user these questions **one group at a time**, waiting for answers before proceeding. Adapt based on what you already know from CLAUDE.md and existing files. Skip questions the project files already answer.

**Group 1: The units and their pipeline**

> I need to understand your pipeline before designing the tracker. Looking at [project name]:
>
> 1. **What is one unit of work called?** (e.g., "sub-chapter", "feature", "module", "endpoint")
> 2. **What steps does each unit go through, in order?** (List them. E.g., "research, outline, draft, review, publish")
> 3. **Which steps produce a file or artifact?** (This determines what the tracker tracks.)

If the project already has a documented pipeline, read it and present your understanding instead of asking. Confirm with: "Is this accurate, or has anything changed?"

**Group 2: Parallelism and gates**

> Now I need to know where the parallelism and human gates are:
>
> 4. **Which steps can run for multiple units simultaneously?** (E.g., "drafting two chapters at once is fine, but review must be sequential")
> 5. **Which steps require you specifically?** (External research, subjective approval, taste decisions, running something outside Claude Code)
> 6. **Are there dependencies between units?** (E.g., "chapter 3 must finish before chapter 4 starts" vs. "all chapters are independent")

**Group 3: Current state and conventions**

> Finally, the practical context:
>
> 7. **Where does each unit's working files live?** (Subdirectory per unit? Flat structure? Naming convention?)
> 8. **What is the current state?** (Which units are at which step right now? Point me to the file if it exists.)
> 9. **How many units would you want in parallel at peak?** (The research says 3-4 max. What feels right for your attention span?)

### Step P2: Design the Task Tracker

After receiving answers, propose a tracker format. The tracker must be:

- **Plain markdown** -- no databases, no YAML files, no external tools
- **One section per work unit** with structured fields a coordinator can parse
- **Compact** -- the full tracker should be readable in one screen for the human, parseable in one read for the agent
- **Compatible** with the existing status file (companion, not replacement)

Propose the format using 3-4 real units from the project as examples.

**Base fields (always include):**

| Field | Purpose | Example values |
|-------|---------|---------------|
| `step` | Current pipeline step (name, not number -- names are self-documenting) | `triage`, `draft`, `review` |
| `status` | State within the step | `not_started`, `in_progress`, `complete`, `blocked` |
| `blocked_by` | What's preventing progress (if blocked) | `user: run research prompts`, `depends: 3.2 must finish first` |
| `files` | Key file paths for this unit | `3.3/catalog.md, 3.3/links.md` |

**Then ask: "What project-specific fields do you need?"** Examples by project type:

| Project type | Common extra fields |
|-------------|-------------------|
| Code | `branch`, `pr_url`, `test_status` |
| Content | `word_count`, `voice_check`, `reviewer` |
| Course | `slide_count`, `exercise_done`, `module_dep` |

Present the proposed format and ask: "Does this capture what you need? Anything to add or remove?"

Iterate until the user approves.

### Step P3: Design the Coordinator Prompt

Once the tracker format is agreed, design the coordinator's operating instructions. This is a prompt (or command file) the coordinator agent uses when dispatched. It must specify:

1. **What to read first:** The tracker file, the pipeline definition, and any project-level constraints
2. **How to select tasks:** Priority rules (which units first? which steps first?), parallelism limits (max 3-4 concurrent), blocker detection (skip blocked units)
3. **How to write handoff briefs:** Each executor gets a self-contained task file with:
   - Context: project identity, pipeline position, what came before
   - Goal: what this task should produce
   - Scope: what files to read, what file to write, what NOT to touch
   - Constraints: style rules, word limits, structural requirements
   - Verification: how the executor confirms it's done before reporting back
   - Source: *workflow-patterns.md > Handoff Prompts Between Sessions*
4. **Where to write handoff briefs:** A convention (e.g., `{unit}/TASK.md`) so executors know where to look
5. **What to do after executors finish:** Read outputs, run verification, update the tracker, flag items for human review

Present the coordinator design and ask: "Does this match how you want to work, or should we adjust?"

#### Tracker Update Protocol

The coordinator is the sole writer of the tracker file. Executors never modify it.

When an executor finishes a task, it writes a completion marker in its unit directory (e.g., `{unit}/DONE.md` containing: what was produced, verification result, any blockers encountered). On the next dispatch cycle, the coordinator reads all completion markers, updates the tracker, and deletes or archives the markers.

This enforces the one-writer rule. -- *agent-design.md > Cross-Agent Coordination Patterns, failure-patterns.md > Concurrent File Editing Race Condition*

#### Code Project Isolation

If this is a code project where executors modify source files, each executor needs its own working copy to avoid file conflicts.

Options:
- **Subagents:** Set `isolation: "worktree"` in the task -- Claude Code creates a temporary git worktree automatically. -- *tools-and-integrations.md > isolation: worktree*
- **Separate sessions:** Use `claude -w feature-name` to launch each executor in its own worktree. -- *workflow-patterns.md > Git Worktrees*
- **Manual:** `git worktree add ../executor-1 -b task-branch` per executor.

For content projects (markdown files in separate directories per unit), worktrees are unnecessary -- the one-writer rule is satisfied by giving each executor its own unit directory.

#### Model Selection per Task

Not every executor needs the most capable model. Match model to task complexity:

| Task type | Recommended model | Rationale |
|-----------|------------------|-----------|
| Strategic/creative (architecture, narrative design) | Opus | Needs deep reasoning and synthesis |
| Implementation (coding, drafting, research synthesis) | Sonnet | 80-90% of execution work at lower cost |
| Mechanical (formatting, state file updates, boilerplate) | Haiku | Fast, cheap, sufficient |

Each handoff brief should specify the recommended model. -- *workflow-patterns.md > Model Selection Strategy, agent-design.md > Five Subagents*

### Step P4: Design the Human Gates

For each step the user identified as requiring human input (Group 2, question 5), define:

- **What the coordinator does before the gate:** Prepares everything the human needs (summary, artifacts, specific questions)
- **What the human does:** The specific action (run a prompt externally, review a draft, approve an outline)
- **What the coordinator does after the gate:** How it picks up and continues (read the human's output, update tracker, dispatch next steps)

Present the gate design. Ask: "Are these the right pause points? Too many? Too few?"

### Step P5: Write the Artifacts

Once all designs are approved, offer to create:

1. **The tracker file** (populated with current state from existing status docs)
2. **The coordinator command or prompt** (a reusable file the coordinator agent reads)
3. **A sample handoff brief** (for one real unit, so the user can see the format)

Ask before creating anything: "Ready for me to create these files, or do you want to adjust the designs first?"

---

## Dispatch Mode

Dispatch mode is operational. The coordinator system already exists. Read state, identify work, write briefs.

### Step D1: Read State

Read the task tracker file. Parse all units and their current state. Also read:
- The pipeline definition (to know what each step involves)
- Any project-level constraints from CLAUDE.md
- Recent handoff briefs or executor outputs (to understand what just happened)
- Completion markers (`{unit}/DONE.md`) from executors that finished since last dispatch

### Step D2: Identify Dispatchable Work

Apply these rules in order:

1. **Filter out blocked units.** Anything with `status: blocked` or a `blocked_by` that hasn't been resolved -- skip.
2. **Filter out units at human gates.** If the next action requires the user, flag it but don't dispatch.
3. **From remaining units, select up to N for parallel dispatch** (where N is the project's parallelism limit, default 3).
4. **Priority rules:** Prefer units further along the pipeline (closer to done). Prefer units in the same chapter/module (shared context is cheaper). Prefer units that unblock other units.

### Step D3: Write Handoff Briefs

For each selected unit, write a handoff brief following the format designed in Planning Mode (Step P3). Each brief must be self-contained -- an executor agent should be able to complete the task by reading only the brief and the files it references.

Each brief must also include:
- **Recommended model** for this task (Opus / Sonnet / Haiku)
- **Isolation method** if this is a code project (worktree branch name or directory)

Place briefs at the agreed location (e.g., `{unit}/TASK.md`).

### Step D4: Present the Dispatch Plan

Show the user:

```
## Dispatch: [date]

### Ready to dispatch (N units)
| Unit | Current Step | Model | Task Summary |
|------|-------------|-------|--------------|
| [unit] | [step] | [Sonnet] | [one-line summary of what the executor will do] |

### Blocked (waiting on you)
| Unit | Blocked By |
|------|-----------|
| [unit] | [what's needed] |

### Recently completed (since last dispatch)
| Unit | Completed Step | Output |
|------|---------------|--------|
| [unit] | [step] | [file path to output] |

Handoff briefs written to: [paths]
```

### Step D4b: Executor Launch

For each dispatched task, output a copyable launch block the user can paste into a new session:

```
## Executor: [unit] -- [step]
**Model:** [Sonnet/Opus/Haiku]
**Launch:** `claude -w [branch-name]` (code project) or new terminal (content project)

### Handoff
[Inline the full handoff brief content here -- context, goal, scope, constraints, verification.
The executor should not need to read any other file to begin.]
```

**Platform options:**
- VS Code: Open a new window, start Claude Code, paste the prompt
- Terminal: New tab, `cd` to project or worktree, paste the prompt
- Subagent: Use the Agent tool with `isolation: "worktree"` for code projects

Ask: "Ready to spawn executors, or want to adjust the plan?"

### Step D5: Post-Execution Review

Run `/coordinator dispatch` again after executors report they're done. The coordinator will:

1. Check for completion markers (`{unit}/DONE.md`) written by executors
2. Read each marker for: output summary, verification result, blockers
3. Update the tracker: advance completed units to their next step, record any new blockers
4. Delete processed completion markers
5. If no completion markers exist, fall back to reading executor output files directly
6. Flag anything that needs human review
7. Report results and ask if the user wants to dispatch the next batch

---

## Important Rules

- **Planning mode is interactive.** Ask questions in groups, wait for answers. Never dump the full design unprompted.
- **Dispatch mode is operational.** Read state, compute plan, present it. Minimize back-and-forth.
- **Read-only until Step P5.** Do not create or modify any project files during suitability analysis or design. Only create files when the user explicitly approves.
- **Respect the coordination tax.** Never propose more than 4 concurrent executors. If the user asks for more, cite the research and recommend against it.
- **The tracker is a companion.** Never replace existing status/progress files. The tracker supplements them with machine-readable state.
- **Executors never write the tracker.** The coordinator is the sole tracker writer. Executors write completion markers only.
- **Handoff briefs are self-contained prompts.** An executor should be able to start work by reading the brief alone -- no external file lookups required to understand the task.
- **Handoff briefs are disposable.** They're consumed by executors and can be deleted after the step completes. The tracker is the persistent record.
- **Cite KB sources** when explaining principles or recommending patterns. The user should be able to trace every recommendation to its origin.

---

## Reference

Educational context for the coordinator. Consult during planning mode. Not needed for dispatch.

### The Coordination Tax

Google DeepMind research shows accuracy saturates or degrades past 4 concurrent agents. A 29-agent swarm study found "the pipeline structure is the real value, not the agent count." The practical ceiling is 3-4 parallel executors before coordination overhead cancels the gains. -- *agent-design.md > The Coordination Tax, agent-design.md > Agent Swarm Critique*

### Core Principles

1. **The coordinator never does the work.** It thinks in goals, constraints, dependencies, and status. The moment it starts implementing, its context fills with detail and strategic oversight degrades (Vision Compression). -- *agent-design.md > Meta-Agent Architecture*
2. **One-writer rule.** Never have two agents writing to the same file. Design every shared file with one writer and many readers. -- *agent-design.md > Cross-Agent Coordination Patterns, failure-patterns.md > Concurrent File Editing*
3. **Files are the interface.** Agents communicate through files, not message passing. State files, task briefs, and outputs are plain markdown. -- *workflow-patterns.md > State Files as Shared Memory*
4. **Pass context, not just the query.** Every handoff includes: project identity, task goal, scope, constraints, verification method. -- *workflow-patterns.md > Handoff Prompts Between Sessions*
5. **Quality gates between steps.** When agent 1's output is wrong, agents 2-N build on bad assumptions. Insert verification between pipeline steps. -- *agent-design.md > Agent Swarm Critique*
6. **Human gates for judgment calls.** Identify steps that require taste, domain judgment, or external action, and design them as pause points. -- *workflow-patterns.md > GSD Checkpoint Orchestration*

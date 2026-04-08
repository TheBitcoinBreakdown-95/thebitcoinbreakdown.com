# L7 Coordinator Pattern -- WBIGAF Planning Prompt

> Copy this into a Claude Code session opened in the TBB/WBIGAF/ directory.

---

## Context

I'm progressing through an agent autonomy scale. I'm currently at L5/L6 (agent-first workflow, beginning to run parallel sessions). I want to reach L7: a coordinator agent that dispatches work to executor agents so I stop being the manual dispatcher.

My project is WBIGAF -- a 67 sub-chapter book where each sub-chapter follows a 7-step pipeline (triage, catalog, links, sources, research, draft, review). The pipeline is defined in WBIGAF.md. Current progress is tracked in WBIGAF-Status.md. The work is embarrassingly parallel -- sub-chapters at the same pipeline step can run simultaneously.

## What I want to plan

Design the L7 coordinator layer for this project. This means:

1. **A machine-readable task tracker** that a coordinator agent can parse to determine what's next. My current WBIGAF-Status.md is human-readable prose. I need structured, per-sub-chapter state that includes: current pipeline step, status, blockers (especially "waiting on user" for Step 5 research prompts), file paths, and what the next step requires.

2. **A coordinator command or prompt** (`/wbigaf-dispatch` or similar) that reads the task tracker, identifies parallelizable work, and writes scoped task briefs for executor agents. The coordinator should never do the work itself -- it dispatches and reviews.

3. **Human-in-the-loop gates** baked into the design. Step 5 (research prompts run off-platform by me) is always a human gate. Triage approval and draft review are also human gates. Everything else can run unattended with spot-checks.

4. **File-based handoffs** between coordinator and executors. Each executor should get a task file with full context (what to do, what files to read, what output to produce, what "done" looks like) so it can work without asking questions.

## KB sources to consult

These Knowledge Distillery sections are directly relevant -- use search_kb to pull them:

- workflow-patterns.md > Pattern 3: Meta-Agent Orchestration (state files as shared memory, handoff prompts)
- agent-design.md > Cross-Agent Coordination Patterns (persistent state machine with file-based checkpoints, STATE.yaml pattern, one-writer rule)
- agent-design.md > Meta-Agent Architecture (strategy-only orchestrator, five subagent roles)
- agent-design.md > Coordination Tax (degrades past 4 agents -- design for 3-4 parallel executors max)
- agent-design.md > Mission Control Pattern (six-table schema as reference for task structure)

## Constraints

- Walk me through this step by step. Do not dump a complete plan at once. Start with the task tracker format, get my feedback, then move to the coordinator design, then handoff format.
- Read WBIGAF.md (the pipeline definition) and WBIGAF-Status.md (current progress) before proposing anything.
- The tracker must work as plain markdown -- no databases, no external tools. It lives in this directory alongside the existing files.
- Do not modify any existing files without asking. This is a planning session first.
- Propose formats with examples using real sub-chapters (3.3, 3.4, 3.5 which are at Step 3A; 4.1-4.5 which are at various steps).
- Keep the existing WBIGAF-Status.md as the human-readable overview. The new tracker is a companion file, not a replacement.

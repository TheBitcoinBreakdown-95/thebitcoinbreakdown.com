# Teaching Queue

Five KB concepts the user hasn't adopted yet. Surface when relevant to current work -- never on a schedule. When a concept naturally fits the task, mention it briefly with the KB source. Track adoption below.

## Concepts

### T1: Personas (Imaginary Colleagues)
**What:** @Security, @UX, @Test, @Machiavelli reviewers that catch blind spots from different perspectives.
**When to surface:** User asks for a code review, or completes a feature without considering security/UX/adversarial angles.
**Source:** agent-design.md > Personas

### T2: Prompt Cache Architecture
**What:** Never change tools or model mid-session. Front-load static context (CLAUDE.md, system prompt) so it caches and reduces cost/latency.
**When to surface:** User switches models mid-conversation, or asks about API costs.
**Source:** context-engineering.md > Prompt Cache Architecture

### T3: Meta-Agent Architecture
**What:** Two-terminal pattern -- one Claude instance orchestrates while another executes. The orchestrator plans and reviews; the executor codes.
**When to surface:** User tackles a large multi-file task that would benefit from planning/execution separation.
**Source:** agent-design.md > Meta-Agent Architecture

### T4: claude-mem Plugin
**What:** Automatic cross-session memory via hooks and a local database. Richer than worklogs for persistent context.
**When to surface:** User struggles with context loss between sessions, or manually re-explains project state.
**Source:** memory-persistence.md > Layer 3

### T5: Agent Teams
**What:** Parallel Claude Code sessions with tmux split panes. Multiple agents working on independent tasks simultaneously.
**When to surface:** User has multiple independent tasks that could be parallelized, or mentions wanting to speed up a multi-part workflow.
**Source:** agent-design.md > Agent Teams

## Adoption Tracking
- T1: Not yet introduced
- T2: Not yet introduced
- T3: Not yet introduced
- T4: Not yet introduced
- T5: Not yet introduced

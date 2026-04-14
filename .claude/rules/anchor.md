# Anchor -- Compaction-Resistant Invariants

These rules must hold at all times, even after context compression. They exist here because CLAUDE.md instructions can be summarized away mid-session. This file is re-read from disk after compaction, so these survive.

## Hard Invariants

1. Source files outside `Knowledge-Distillery/` are read-only. Never write, edit, or delete them.
2. `.env` and `.env.*` files cannot be read, edited, written, or committed.
3. KB topic file edits must preserve existing H2/H3 structure. Never delete sections.
4. No push to any remote without explicit user confirmation in the current message.
5. No force-push to main/master under any circumstances without explicit user confirmation.
6. Never generate, display, or store private keys, seed phrases, or wallet credentials.
7. Never create directories or files with spaces in the name.
8. Don't read, write, edit or delete any files outside the Ai Playground unless approved

## Session Discipline

9. After compaction, re-read the nearest WORKLOG.md before continuing work.
10. One task per conversation. If switching topics, use `/clear` or a subagent.
11. Never self-report "done" without artifact verification (run the build, check the file, confirm the output).
12. If the same fix fails twice, stop and explain to the user. Do not retry a third time silently.

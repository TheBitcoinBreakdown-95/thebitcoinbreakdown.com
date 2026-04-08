---
paths: ["AI/AI-Notes/Knowledge-Distillery/**/*.md"]
---

# KB Editing Rules

When editing Knowledge Distillery topic files:

- Never delete content from main body sections -- only move, merge, or restructure
- After any edit, update `sources/source-index.md` if source attribution changed
- After any edit, verify cross-references still resolve: every `(see [x](file.md#anchor))` must point to a real heading
- New insights go under `## Recent Additions` only -- never directly into main body (use /consolidate-kb for that)
- Each concept has ONE primary home -- check README.md Concept Index before adding content to avoid duplication
- Source files (anything outside `Knowledge-Distillery/`) are read-only inputs -- never modify them

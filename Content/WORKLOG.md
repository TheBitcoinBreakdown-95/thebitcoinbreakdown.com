# Content Workspace Worklog

## Active Project
**Your Agent Control Center** -- Workshop deck + companion materials for non-technical audience

## Last Session
**Date:** 2026-03-20

### What Was Done
- Restructured course from 11 lessons (~19K words) to 4 lessons + appendix (~6K words)
- Renamed course to "Your Agent Control Center"
- Format: workshop deck (PPTX) + companion handout for in-person delivery (~30 min + install time)
- Built PPTX generator script (`generate_workshop.py`) using TBB Format template
  - 20 slides, exact TBB dark luxury theme (hex decorations, gold accents, Georgia font)
  - Slide types: title, section break, content, comparison, quote, process flow, transition, close
  - Rerunnable: edit SLIDES list in script, rerun to regenerate
- Created companion handout: `handout-best-practices.md`
- Created SOUL.md rules file (`.claude/rules/SOUL.md`) -- no flattery, constructive skepticism
- Updated output-callouts.md with Critical Engagement section
- Saved AI autonomy scale (L1-L8) to Thinking Space
- Saved PPTX template system to memory for future presentations

### Decisions Made
- Title: "Your Agent Control Center" (folder still named "How to Learn and Do Anything" -- rename pending)
- Format: PPTX from TBB Format template, not Marp
- Written lessons preserved as standalone reference material
- Old lessons 02-11 in `part2-source/` for Part 2 development
- Philosophy: directing, not vibecoding. Permissions stay on for beginners.
- CLAUDE.md auto-generation shortcut included in handout (from article research)

### What's Next
1. Open PPTX in Google Slides or PowerPoint -- visual review needed (can't preview in VS Code)
2. Test installation flow on a clean machine with a non-technical person
3. Rename folder from "How to Learn and Do Anything" to "Your Agent Control Center"
4. Decide delivery venue (JC Bitcoin meetup? FreedomLab? Other?)
5. Part 2 planning: advanced topics from `part2-source/`

### Key Files
| File | Purpose |
|------|---------|
| `OUTLINE.md` | Workshop structure and flow |
| `generate_workshop.py` | PPTX generator script (edit SLIDES list to change content) |
| `Your Agent Control Center - Workshop.pptx` | Generated deck (20 slides) |
| `handout-best-practices.md` | Take-home reference sheet |
| `01-04 + appendix .md files` | Written course (standalone reference) |
| `part2-source/` | Banked content for Part 2 |
| `../TBB Format.pptx` | Template (do not modify) |

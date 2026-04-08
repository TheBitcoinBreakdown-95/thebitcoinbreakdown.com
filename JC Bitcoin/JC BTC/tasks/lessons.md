# Lessons Learned — Cross-Session Log

Per CLAUDE.md Section 10: After ANY correction, log what went wrong and the specific rule that prevents recurrence.

---

## 2026-03-06: Slide style guide built from data, not visual inspection

**What went wrong**: Built the Slide-Style-Guide.md and rebuild_deck.py entirely from API extraction data (font frequencies, color hex codes, element counts) without looking at reference deck thumbnails. The resulting test deck had wrong backgrounds (navy instead of black), wrong text colors (white instead of orange), wrong font sizes (16pt instead of 26pt), and invented elements (divider bars, background zones) that don't exist in the reference decks.

**Rule**: When building or updating any style guide for presentations, ALWAYS capture and visually compare reference thumbnails before writing code. Follow `Presentation/Slide-Ingestion-Checklist.md`. API data alone is insufficient — theme-inherited styles are invisible in raw extraction.

---

## 2026-03-06: Edit tool path format issues

**What went wrong**: The Edit tool repeatedly failed with "File has not been read yet" errors when using backslash Windows paths (`c:\Users\GC\...`), even after reading the file.

**Rule**: Always use forward-slash paths (`c:/Users/GC/...`) for Read/Write/Edit tools. Backslash paths are not reliably recognized as the same file.

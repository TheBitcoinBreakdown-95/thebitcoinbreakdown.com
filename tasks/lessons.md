# Lessons Learned

Persistent log of corrections and patterns. Recurring lessons get promoted to CLAUDE.md rules.

---

## 2026-02-06: Don't over-build before understanding the project
- **What went wrong**: Built a full Astro site (layouts, components, pages, styles) before looking at the existing WordPress site. The existing site has categories, speeches, memes, guides — not a simple blog.
- **Rule**: Always look at the existing site/content FIRST before building anything. Understand what you're replacing.

## 2026-02-06: Explain tools before using them
- **What went wrong**: Created an Astro project without explaining what Astro is, why the folder is named that, or what node_modules/dist/json files are for. User was confused.
- **Rule**: When introducing any tool or framework, explain what it is and what the generated files mean BEFORE creating them. Don't assume the user knows.

## 2026-02-06: Content collection paths are relative to astro project root
- **What went wrong**: Used `../../TBB/posts` in content.config.ts but glob loader resolves relative to the Astro project root, not the file location. Correct path is `../TBB/posts`.
- **Rule**: Astro glob loader `base` paths are relative to the project root (the `astro/` folder), not to `src/`.

## 2026-02-07: Match the reference implementation exactly — don't approximate
- **What went wrong**: When implementing V4 interactive effects (interactions.js), I approximated the reference HTML's JS instead of copying the exact algorithms. This resulted in 66 discrepancies: lightning bolt was random rain instead of targeted click-strike, wrong character sets, wrong speeds, wrong easing functions, swapped label/value colors, wrong breakpoints, missing mouseleave handlers, etc.
- **Rule**: When a reference implementation exists, read it line-by-line and match every value exactly. Don't paraphrase algorithms — use the same math, same constants, same selectors. Only deviate where the Astro framework requires it (e.g., external script file vs inline). After implementing, do a diff audit against the reference before marking complete.

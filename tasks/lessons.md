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

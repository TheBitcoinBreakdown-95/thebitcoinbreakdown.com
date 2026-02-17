# The Bitcoin Breakdown

**Bitcoin education. No hype. No jargon. No paywalls.**

[thebitcoinbreakdown.com](https://thebitcoinbreakdown.com)

---

## What Is This?

The Bitcoin Breakdown is a Bitcoin education site built to answer the questions most people are afraid to ask — and to do it without the noise that plagues most of the internet's Bitcoin content.

The site hosts two main bodies of work:

- **The Compendium** — A 9-chapter, book-length journey through Bitcoin titled *Why Bitcoin Is Good As Fuck*. Covers everything from "What is Bitcoin?" to its future trajectory, distilled from 83 source documents and years of independent research.
- **Blog Posts** — Standalone articles on Bitcoin philosophy, economics, and culture.

This is not a trading site. There are no price predictions, no affiliate links, no courses to sell. Just rigorous, freely accessible education.

---

## Tech Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| Content | [Obsidian](https://obsidian.md) | Write and organize posts in Markdown |
| Framework | [Astro](https://astro.build) v5 | Static site generator (Markdown → HTML) |
| Hosting | [Hostinger](https://hostinger.com) | Production server |
| Version Control | GitHub | This repo |
| Deployment | GitHub Actions | Auto-build and FTP deploy on push |

The site is fully static — no JavaScript frameworks, no client-side rendering, no databases. Astro compiles Markdown files into plain HTML. The only client-side JS handles visual effects (scroll reveals, typing animations, glitch effects).

---

## Project Structure

```
├── TBB/                          # Obsidian vault (all content lives here)
│   ├── posts/                    # Blog posts as Markdown
│   ├── guide/                    # Compendium chapters as Markdown
│   └── pages/                    # Static pages (About, Learn More, etc.)
│
├── WBIGAF/                       # Book project (research & pipeline)
│   ├── 0. Project/               # Voice DNA profile, planning docs
│   └── 1-9. [chapters]/          # Source research per chapter
│
├── astro/                        # Site generator
│   ├── src/styles/global.css     # Design system (all colors, fonts, spacing)
│   ├── src/layouts/              # Page templates
│   ├── src/components/           # Header, Footer, Terminal, Divider
│   ├── src/pages/                # Routes and page templates
│   ├── src/scripts/              # V4 interaction effects (vanilla JS)
│   └── public/                   # Static assets (images, .htaccess)
│
├── tasks/                        # Task tracking and lessons learned
└── CLAUDE.md                     # AI assistant operating manual
```

---

## The Compendium

*Why Bitcoin Is Good As Fuck* is structured as 9 chapters, each with multiple sub-chapters:

| # | Chapter | Status |
|---|---------|--------|
| 1 | What is Bitcoin? | 11 sub-chapters |
| 2 | Why Bitcoin? | 9 sub-chapters |
| 3 | What Problems Does Bitcoin Solve? | In progress |
| 4 | Bitcoin's Past | Coming soon |
| 5 | Bitcoin's Properties | Coming soon |
| 6 | So...What is Bitcoin Exactly? | Coming soon |
| 7 | Bitcoin's Present | Coming soon |
| 8 | Why Bitcoin is Good as Fuck | Coming soon |
| 9 | Bitcoin's Future | Coming soon |

Chapters 1-2 contain the original blog series that started the project. Chapters 3-9 are being written through a multi-step research pipeline that draws from primary sources — Austrian economists, cypherpunks, the Bitcoin whitepaper, and independent researchers.

---

## Design: "Dark Luxury"

The site's visual identity is called **Dark Luxury** (V4) — a deliberate fusion of four aesthetic traditions:

- **Art Deco** — Geometric minimalism, gold as a luxury signal, restrained ornamentation
- **Cypherpunk** — Cryptographic texture, terminal aesthetics, proof-of-work metaphors
- **Greco-Futurism** — Timelessness meets technology, classical authority with forward momentum
- **Dark Luxury** — Pure black foundations, gold accents, serif elegance, generous negative space

### Why These Colors?

Every color in the palette carries intentional symbolism:

| Color | Value | Meaning |
|-------|-------|---------|
| **Gold** | `#FFD700` | Sound money, incorruptibility, permanence. Gold is the one material humanity has universally agreed stores value. Using it as the accent says: *"this content is valuable."* |
| **Pure Black** | `#000000` | Sovereignty, independence, void. No background noise — only signal. The absence of color is a statement of confidence. |
| **Cream** | `#E8E4DC` | Warm but not white. Avoids the clinical sterility of `#FFFFFF`. Implies parchment, age, knowledge passed through time. |

### Why These Fonts?

| Font | Role | Meaning |
|------|------|---------|
| **Cormorant Garamond** | All text | Timelessness and classical authority. Serifs say *"this is a serious publication, not a tweet."* Weight 300 (light) says *"confident enough to whisper."* |
| **JetBrains Mono** | Code & data only | Cryptographic proof, machine precision. Appears only alongside verifiable data — hashes, code, block heights. Its presence says *"this is mathematically true."* |

### Why These Effects?

The cypherpunk aesthetic is expressed through interactions, not decoration. The background is always pure black — restraint makes every effect more powerful.

| Effect | Meaning |
|--------|---------|
| **Lightning bolt** (page transitions) | Energy, proof-of-work, the Bitcoin Lightning Network. A metaphor for the speed of digital money. |
| **Glitch text** | Disruption of the existing order. Bitcoin glitches the financial system. Brief and controlled — revolution, not chaos. |
| **Matrix rain** (page load) | The underlying data layer of reality. Bitcoin is information money. You're meant to glimpse it, not stare at it. |
| **Hash strings** (decorative) | Cryptographic proof. *"Everything here is verifiable."* They're not readable — they're atmospheric. |
| **Terminal console** | Direct access to the protocol. No GUI intermediary. The cypherpunk's native environment. |
| **Crosshair cursor** | Precision, targeting. You're not just browsing — you're locking onto information. |

### Freedom as Design Philosophy

This isn't a decorative motif — it's a structural principle. Freedom is expressed through what the site *refuses* to do:

- **No paywalls.** All content is freely accessible.
- **No email walls.** You never need to "sign up to continue reading."
- **No tracking analytics.** Essential cookies only.
- **No dark patterns.** Accept and Decline have equal prominence.
- **No interstitials.** Content loads and you read it. Nothing interrupts.
- **No ads.** The design itself is a trust signal.

The absence of barriers IS the freedom statement.

### Design Details

- Sharp corners on all cards (no `border-radius`) — luxury aesthetic
- 720px content width for optimal reading measure
- All animations respect `prefers-reduced-motion`
- No CSS frameworks — every line of CSS is custom and purposeful
- Fully responsive from 375px mobile to ultrawide desktop

The complete design system is documented in [`TBB/Website planning/V4/tbb-master-design-guide.md`](TBB/Website%20planning/V4/tbb-master-design-guide.md) (731 lines covering color theory, typography, spacing, components, accessibility, semiotics, and cognitive load rules).

---

## Local Development

```bash
# Install dependencies
cd astro
npm install

# Start dev server
npm run dev
# → http://localhost:4321

# Build for production
npm run build
# → Output in astro/dist/
```

---

## Deployment

Pushing to `main` triggers a GitHub Actions workflow that:

1. Builds the site with Astro
2. Deploys the `dist/` folder to Hostinger via FTP

The site is live at [thebitcoinbreakdown.com](https://thebitcoinbreakdown.com).

---

## Content Conventions

### Blog Post Frontmatter

```yaml
---
title: "Post Title"
description: "SEO description (150-160 chars)"
pubDate: 2026-02-05
author: "The Bitcoin Breakdown"
tags: ["bitcoin"]
image: ""
draft: false
---
```

### Compendium Chapter Frontmatter

```yaml
---
title: "Chapter Title"
description: "Chapter description"
chapter: 1
order: 2
draft: false
---
```

### Bitcoin Terminology

- **Bitcoin** (capital B) = the network, protocol, and system
- **bitcoin** (lowercase b) = the unit of currency (BTC)

---

## License

Content is published freely for educational purposes. The site's design system, code, and structure are open source in this repository.

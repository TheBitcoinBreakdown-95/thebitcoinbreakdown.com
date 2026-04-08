# CLAUDE.md -- Content Workspace

Educational courses, workshops, and project materials. Each folder is a self-contained project with its own outline, research, drafts, and final content.

---

## What This Is

A workspace for building educational content -- Bitcoin courses, AI onboarding guides, workshop materials, and whatever comes next. Projects here evolve at their own pace. Some ship to the FreedomLab website, some to thebitcoinbreakdown.com, some stay as workshop decks. The publishing destination is decided per-project, not upfront.

## Structure

```
Content/
  Project Name/
    OUTLINE.md        -- scope, structure, audience
    research/         -- notes, references, source material
    drafts/           -- WIP content
    *.md              -- final lesson/chapter files (numbered)
```

Not every project needs every folder. A small workshop might just be an outline and 3 files. A full course might have research, multiple drafts, and a presentation layer. Let the project dictate the structure.

## What Claude Does Here

- Write and edit educational content (lessons, guides, workshop materials)
- Help develop outlines and course structures
- Research topics and organize reference material
- Review existing content for voice, clarity, and accuracy
- Suggest improvements based on KB best practices

## Voice and Tone

Derived from existing content (Node SSH course):

- **Direct and confident.** Second person ("you're about to..."), not passive or hedging.
- **Accessible but not dumbed down.** Assume the reader is smart but new to the topic. Define terms on first use.
- **No jargon without explanation.** Technical terms earn their place by being immediately explained.
- **Show, don't lecture.** Concrete examples, real commands, actual output -- not abstract descriptions.
- **Honest about limitations.** Say what something can't do, what could go wrong, and when to ask for help.

Individual projects may adjust tone for their audience. Node SSH speaks to technical hobbyists. "How to Learn and Do Anything" speaks to non-technical newcomers. The principles above apply to both; the vocabulary shifts.

## Bitcoin Terminology

- **Bitcoin** (capital B) = the network, protocol, system
- **bitcoin** (lowercase b) = the unit of currency (BTC)
- No price predictions or financial advice
- No private keys, seed phrases, or real wallet addresses in content

## Current Projects

| Project | Status | Audience |
|---------|--------|----------|
| Node SSH | 7 lessons written, review pending | Bitcoin node runners (technical hobbyists) |
| How to Learn and Do Anything | Outline complete, no lesson content yet | Non-technical newcomers to AI tools |

## What Claude Does NOT Do Here

- Over-engineer project structure before there's content to structure
- Decide publishing format or destination without being asked
- Add frontmatter, metadata, or build tooling unless a publishing target is chosen
- Write content that contradicts the outline without discussing it first

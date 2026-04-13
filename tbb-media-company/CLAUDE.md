# CLAUDE.md -- TBB Media Company

> The Bitcoin Breakdown as a media, education, and consulting business under 2112 Capital Solutions LLC. Podcast, YouTube, newsletter, social, courses, consulting, workshops, and the production system that ties them together.

**Master TODO:** All tasks tracked in [tasks/TODO.md](tasks/TODO.md) (Phase 14). This file covers workflows, tools, and channel specs.
**Synthesis:** [synthesis.md](tbb-media-company/business/synthesis.md) -- full strategic context extracted from legacy archives.
**Teaching Framework:** [teaching-framework.md](tbb-media-company/business/teaching-framework.md) -- pedagogical principles for content design.
**Episode Roadmap:** [episode-roadmap.md](tbb-media-company/podcast/episode-roadmap.md) -- ordered episode plan with production checklists.

---

## Mission & North Star

**Mission:** "I'm the one putting people in lifeboats. The boots on the ground, physically helping people onto the new financial system. It's my life's purpose to help people with bitcoin."

**North Star:** Bitcoin won't win by default. It requires cultural literacy, storytelling, usability, and trust infrastructure.
1. **Out-narrate** -- emotional stories that connect Bitcoin to real human needs
2. **Out-educate** -- simple, visual content for non-technical audiences
3. **Outlast** -- make self-custody normal before CBDCs arrive

**Market gap:** No one is both funny and educational in Bitcoin-only content. TBB fills that gap: accessible, entertaining, principled, deep without being dry.

---

## What This Is

The production and services arm of The Bitcoin Breakdown. Two goals:
1. **Consistent content output with minimal friction.** AI handles scripting, post-production, and distribution. The human handles being on mic, on camera, and in the room.
2. **Direct services for people who need hands-on help.** Consulting, workshops, self-custody sessions, node setup.

### What Claude Does Here
- Draft episode scripts from existing WBIGAF/TBB content library using Voice DNA
- Generate show notes, social posts, newsletter snippets from transcripts
- Manage RSS feed configuration and episode metadata
- Research topics and pull supporting material from the 103K+ word source library
- Help design and iterate on production workflows
- Draft consulting materials, workshop outlines, and course content

### What Claude Does NOT Do Here
- Record, edit audio/video, or upload to platforms (human + tools handle this)
- Make publishing decisions without user confirmation
- Over-engineer automation before the manual workflow is proven
- Add tools or subscriptions without discussing cost

---

## Corporate Structure

**Legal entity:** 2112 Capital Solutions LLC
- Formation: July 18, 2023 (New Jersey)
- Entity ID: 0450997703
- EIN: 93-2439353
- NAICS: 541611 (Management Consulting Services)
- Status: Active / Good Standing
- Registered Agent: Republic Registered Agent LLC (Wayne, NJ)

**Public brand:** The Bitcoin Breakdown (DBA filing pending)
- All public-facing content, consulting, and products operate under TBB
- 2112 remains the legal/financial shell
- Single entity, multiple revenue streams, tracked as profit centers in bookkeeping

**Operational calendar:**
- Annual report: NJ, filed yearly (2025 complete)
- BOI reporting: completed 12/3/24
- Registered agent: Bizee auto-renews (verify credit card)
- Website hosting: Hostinger renewal July 16, 2027
- DBA filing: pending (Hudson County Clerk, ~$50-75)
- Trademark: pending (USPTO Class 41, ~$250-350)

---

## The Production Flow

```
1. PICK (5 min)
   Choose a topic from existing content:
   - WBIGAF source library (103K words, 86 sub-chapters, 66 bibliography sources)
   - TBB blog posts and compendium (31K+ published words)
   - Node SSH course (7 lessons)
   - Ark/ArkFloat research
   - Episode roadmap (podcast/episode-roadmap.md)
   - Or a new topic informed by the above

2. RANT (10-20 min)
   Record a raw, unstructured brain dump on the topic. Talk through your
   thoughts, opinions, arguments, stories -- whatever comes out. Don't worry
   about structure, polish, or being wrong. This is practice and idea
   generation, not the final product. Can be done at a desk, on a walk, or
   wherever the energy is. Transcribe with Whisper and hand the transcript
   to AI.

3. SCRIPT (30-60 min, AI-assisted)
   AI combines the best lines and ideas from the rant with research pulled
   from the WBIGAF/TBB source library. Output is a speakable outline in
   Voice DNA style -- talking points, not prose.
   User reads, marks up, adds riffs, cuts what's wrong.
   Voice DNA location: WBIGAF/0-project/voice-dna/voice-dna-profile.md
   The script should sound like you because it started as you.

4. RECORD (30-45 min)
   Option A: Audio only (podcast) -- read outline, riff naturally
   Option B: Slides + voiceover (YouTube) -- PowerPoint/Excalidraw walkthrough
   Option C: Screen share (how-to) -- live walkthrough with narration
   Tools: OBS + existing mic + phone/Camo Studio
   One take preferred. Re-record only if major issues.

5. POST-PRODUCTION (AI-assisted, 15-20 min human review)
   Transcribe (Whisper or YouTube auto-captions)
   AI generates: show notes, 3-5 social posts, newsletter snippet, blog post draft
   User reviews and approves

6. PUBLISH (15 min)
   Upload to podcast host + YouTube
   Schedule social posts
   Send newsletter (when subscriber base exists)
   Optionally publish as TBB blog post with embedded audio/video
```

**Target per episode: 2-3 hours total.** The rant step adds 10-20 min but produces a better script and doubles as speaking practice. At 5-10 hrs/week = 1-3 episodes. Even 2/month builds momentum.

---

## Content Design Principles

Every episode should move through: **Inspire -> Absorb -> Deliver** (see `business/teaching-framework.md` for full framework).

**Quick reference:**
- Open with a burning question or emotional hook, not content
- Use stories, analogies, and concrete examples -- not definitions
- Dual coding: words + visuals (especially for YouTube)
- Close with a reflective question or call to action
- Design content so the viewer wants to explain it to someone else

**Style & Voice:**
- Oratory/preaching delivery: dense, pre-written, delivered with conviction
- Brain-dumping (speech-to-text) > rigid scripting
- Mix of reading curated content + personal riffs
- Funny, accessible, principled. Not fluffy, not academic.
- Signature opening: "Yo it's GC -- back with another bitcoin breakdown"

---

## Channels

### Podcast (Primary -- launch first)
- **Format:** Pre-scripted oratory. Dense, not fluffy. Written like a speech, delivered with conviction.
- **Length:** 10-20 min per episode
- **Hosting:** Spotify for Podcasters (free, distributes to Apple/Google/etc)
- **RSS:** Managed by hosting platform
- **Episode files:** `podcast/episodes/YYYY-MM-DD-slug/` (script.md, show-notes.md, transcript.md)
- **First episode:** Golden Rules of Bitcoin (script near-complete in archive)

### YouTube (Second channel -- after podcast flow is proven)
- **Format:** Slide-based explainers (voiceover, no face required), how-to walkthroughs, Ark/L2 visual explainers
- **Tools:** OBS screen capture, PowerPoint/Excalidraw for visuals
- **Script files:** `youtube/scripts/YYYY-MM-DD-slug.md`
- **Thumbnails:** `youtube/thumbnails/` (templates + per-video)
- **Monetization:** 1K subscribers + 4K watch hours for YouTube Partner Program

### Newsletter (Launches with first subscribers)
- **Platform:** Beehiiv (free up to 2,500 subscribers)
- **Format:** Episode digest + curated links + TBB content highlights
- **Cadence:** Weekly or bi-weekly (match to episode cadence)
- **Archive:** `newsletter/issues/YYYY-MM-DD-slug.md`

### Social (Ongoing, AI-assisted)
- **Platforms:** X (primary), LinkedIn, TikTok, Reddit, Nostr
- **Content:** Clips from episodes, standalone posts, engagement
- **Scheduling:** Buffer free tier (3 channels)
- **Templates:** `social/templates/` (post formats, clip specs)

---

## Services & Consulting

TBB is education. 2112 is the business. Both serve the same mission. Content is free; hands-on help is paid.

### Current Service Offerings
| Service | Price | Description |
|---------|-------|-------------|
| Free consultation | 30 min | Discovery call, assess needs |
| Self-custody session | $100 | Hardware wallet setup + education |
| Node setup | $500 | Full node configuration |
| Node maintenance | $50/month | Updates, QA, liquidity management |
| Private consulting | $100/hour | General Bitcoin guidance |

### Future Services (as demand appears)
| Service | Price Range | Description |
|---------|-------------|-------------|
| In-person workshops | $TBD | Bitcoin basics, self-custody, AI tools |
| Corporate training | $2-5K/day | Bitcoin for businesses, treasury education |
| Online courses | $50-300 | Structured multi-lesson programs |
| Ark onboarding | $TBD | Community workshops, starter kits |
| College teaching | $TBD | Guest lectures, semester courses |

### Pricing Philosophy
Charge what the time is worth ($100/hr). Don't undercut. Offer a charity track (free webinars, free resource guides) for those who can't pay -- but that's not the base offering.

---

## Tool Stack (All Free at Launch)

| Tool | Purpose | Cost |
|------|---------|------|
| OBS | Recording (audio or screen+audio) | Free |
| Phone + Camo Studio | Camera | Owned |
| Existing mic | Audio | Owned |
| Audacity | Audio trim (dead air, mistakes) | Free |
| Spotify for Podcasters | Podcast hosting + RSS + distribution | Free |
| YouTube | Video hosting | Free |
| Beehiiv | Newsletter (up to 2,500 subs) | Free |
| Buffer | Social scheduling (3 channels) | Free |
| Gumroad | Digital product sales | Free (10% tx fee) |
| Whisper | Transcription (local) | Free |
| Claude | Scripts, show notes, social, repurposing | Existing |
| CapCut | Video editing, filler word removal | Free |
| DaVinci Resolve | Advanced video editing (if needed) | Free |
| Leonardo AI | Image generation for thumbnails/social | Free tier |

---

## Content Library (Source Material)

| Source | Location | Words | Use For |
|--------|----------|-------|---------|
| WBIGAF source files | `WBIGAF/` (Ch1-9) | ~103,000 | Deep topic scripts, argument-driven episodes |
| TBB compendium | `TBB/guide/` | ~31,600 | Polished explainers, adapted for audio |
| TBB blog posts | `TBB/posts/` | ~9 posts | Adapted readings, updated takes |
| Bibliography | `WBIGAF/bibliography.md` | 66 sources | Citation-backed episodes |
| Node SSH course | `Content/node-ssh/` | 7 lessons | Technical walkthrough episodes |
| Ark research | `Ark/` | Multiple docs | L2/Ark explainer series |
| Voice DNA | `WBIGAF/0-project/voice-dna/` | 761 lines | Script generation reference |
| Golden Rules script | `the-bitcoin-breakdown-old/Lessons/Golden Rules Video/` | Near-complete | Episode 1 source |
| Bitcoin 101 outline | `the-bitcoin-breakdown-old/TBB/Bitcoin 101/` | 16 sections | Series outline |
| Hardware wallet guide | `2112 (old)/Hardware wallet Guidebest practices.md` | 10K+ words | Workshop/episode source |
| Teaching framework | `business/teaching-framework.md` | Full framework | Content design reference |
| Personal journey | `the-bitcoin-breakdown-old/TBB/My history with bitcoin.md` | Narrative | About/bio, EP02 source |

---

## Brand

- **Entity:** 2112 Capital Solutions LLC, DBA "The Bitcoin Breakdown" (DBA pending)
- **Visual identity:** V4 "Dark Luxury" -- Gold (#FFD700) + Black (#000000) + Cream (#E8E4DC)
- **Fonts:** Cormorant Garamond (serif) + JetBrains Mono (mono)
- **Tone:** Clear, accessible, passionate. Dense information delivered with conviction. Funny when appropriate. Not fluffy, not academic. See Voice DNA profile for full spec.
- **Logo assets:** `brand/logo/`
- **Design direction:** Art Deco aesthetic, abstract "B" symbol, integration of Breakdown as "reakdown"

---

## Agent Automation (Phase 2 -- after manual workflow is proven)

Once 5-10 episodes are produced manually and friction points are identified:
- Content repurposing agent: transcript --> social posts, newsletter, blog post
- SEO agent: titles, descriptions, tags, keyword optimization
- Research agent: pulls from WBIGAF/TBB library to support script drafting
- Scheduling agent: manages publish calendar across channels
- Tools to evaluate: Paperclip, Hermes explainer skill, Claude API agents, n8n workflows

Do not build automation before the manual workflow exists and has been repeated enough to know what's worth automating.

---

## Legacy Archives

Three folders of planning/strategy material preserved for reference:

| Folder | Contents | Key Files |
|--------|----------|-----------|
| `2025-2035 (old)/` | 74 files. Personal goals, 10-year plan, teaching pedagogy research, AI project ideas, income planning | 5-Year Roadmap, GOAL CONSOLIDATION, How to Teach, Inspiration Example |
| `2112 (old)/` | ~40 files. LLC formation, business services, pricing, hardware wallet guides, Ark missionary vision | Company Info, What I charge, Mission, Services, Hardware wallet guide |
| `the-bitcoin-breakdown-old/` | 164 files. Content strategy, Golden Rules series, Bitcoin 101 curriculum, production workflows, social media | Golden Rules scripts, Bitcoin 101.md, Purpose.md, North Star.md, My style.md |

**Do not delete these folders.** They are primary source material. Key learnings have been extracted into:
- `business/synthesis.md` -- strategic context, corporate details, revenue model, journey, patterns
- `business/teaching-framework.md` -- pedagogical principles for content design
- `podcast/episode-roadmap.md` -- ordered episode plan

---

## Directory Structure

```
tbb-media-company/
  CLAUDE.md                       -- This file
  business/
    blueprint.md                  -- North star business plan
    synthesis.md                  -- Extracted learnings from legacy archives
    teaching-framework.md         -- Pedagogical principles for content design
    competitive-research.md       -- Market landscape (when completed)
  podcast/
    episodes/                     -- Per-episode folders (script, notes, transcript)
    episode-roadmap.md            -- Ordered episode plan with checklists
    podcast-config.md             -- RSS, hosting, format decisions
  youtube/
    scripts/                      -- Video scripts and outlines
    thumbnails/                   -- Thumbnail templates and assets
  newsletter/
    issues/                       -- Newsletter drafts and archives
  social/
    templates/                    -- Post templates, clip specs per platform
  brand/
    logo/                         -- Logo assets and design explorations
  2025-2035 (old)/                -- Legacy: goals, pedagogy, AI projects
  2112 (old)/                     -- Legacy: LLC, services, pricing, guides
  the-bitcoin-breakdown-old/    -- Legacy: content strategy, scripts, curriculum
```

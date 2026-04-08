---
title: Slide Deck Process Guide
type: content
status: draft
created: 2026-03-15
audience: general
tags: [process, presentations, guide]
---

# JC Bitcoin -- Slide Deck Process Guide

Reference for building monthly Socratic Seminar slide decks. This will become a `/build-deck` slash command once validated.

---

## 1. Slide Formatting Rules

### On-Slide Content
- Title + 3-5 short bullet points MAX (or title + single image)
- Text is a teaser, not the lecture -- keep it scannable
- Every content slide should have an image (meme, chart, screenshot, infographic)
- Use the brand style: black background, orange (#ff9900) Calibri text (see Slide-Style-Guide.md)

### Speaker Notes
- This is where the real content lives -- what you actually say
- **Max 200 words per slide** -- if you need more, split into two slides
- Structure: context, key point, transition to next slide
- Include source citations for data claims

### Slide Count
- **Max 2 slides per topic** -- only use a second when you need a second image
- Target 15-18 total slides per deck (keeps presentation under 60 min with discussion)
- If a topic needs more than 2 slides, it should be its own workshop

---

## 2. Standard Slide Order

1. Cover (logo + event title + date)
2. Sponsor
3. Photo/promo (group photo from last meetup)
4. Agenda
5. Guidelines (Chatham House, no financial advice, etc.)
6. Bitcoin Price Update (1-2 slides)
7. Macro Update (2-4 slides depending on month)
8. Podcast of the Month (1 slide)
9. Book of the Month (1 slide)
10. Infographic of the Month (1 slide)
11. History Moment (1 slide)
12. Tech Topic A (1-2 slides)
13. Tech Topic B (1-2 slides, if applicable)
14. Demo (1 slide -- setup, then do it live)
15. Video of the Month (1 slide -- play it)
16. Open Discussion / Q&A (1 slide with topic seeds)
17. Closing (next meetup, links, thank you)

---

## 3. Content Sourcing

### Where to pull from
| Source | What it provides |
|--------|-----------------|
| Thinking Space/AI ACTION PLAN/Script Summary/ | Podcast breakdowns, macro analysis |
| TBB/guide/ and TBB/posts/ | Bitcoin educational content |
| Twitter/X bookmarks | Memes, charts, hot takes |
| Nostr feed | Privacy/freedom content, zap milestones |
| YouTube | Conference talks, explainer clips |
| CoinGecko / TradingView | Price charts, dominance data |
| FRED / Treasury.gov | Macro data (debt, rates, CPI) |

### Podcast of the Month workflow
1. Check Thinking Space for existing breakdowns
2. Pull 3-4 key takeaways from the summary
3. Connect to Bitcoin: what does this mean for BTC holders?
4. Write speaker notes (under 200 words)
5. Image: screenshot of podcast thumbnail or a key chart from the episode

---

## 4. Image Sourcing

### Per-slide image requirements
Every content slide needs one of:
- **Meme** -- Bitcoin Twitter meme relevant to the topic
- **Chart** -- price chart, macro data visualization, on-chain metric
- **Screenshot** -- tweet, Nostr post, news headline, app UI
- **Infographic** -- community-created educational graphic
- **Photo** -- event photo, speaker headshot, product shot

### Where to find images
- Personal meme/screenshot collection (TBD -- user to locate and index)
- Twitter/X: search topic + "bitcoin meme" or screenshot relevant tweets
- Nostr: screenshot notable posts (White Noise, zap milestones, etc.)
- YouTube: screenshot video thumbnails or key frames
- TradingView: export charts with black background to match deck style
- `Edu Meetup Presentations/assets/` -- indexed collection (to be built)

### Image index format
Store images in `assets/` with descriptive names. Maintain an index:
```
assets/
  btc-vs-gold-ytd-2026.png
  luke-gromen-podcast-thumb.png
  white-noise-app-screenshot.png
  index.md  -- lists all assets with tags and descriptions
```

---

## 5. Build Workflow

1. **Two weeks before meetup:** Create outline markdown file (copy template, fill topics)
2. **One week before:** Finalize content, write all speaker notes, create image shopping list
3. **3-4 days before:** Collect all images, save to assets/
4. **2-3 days before:** Build deck via Google Slides API (`/build-slides <deck-id>`)
5. **Day before:** Review on projector or large screen, rehearse transitions
6. **Day of:** Update any last-minute data (price, breaking news)

---

## 6. Quality Checklist

Before finalizing any deck:

- [ ] Total slides between 15-18
- [ ] Every content slide has an image
- [ ] No slide has more than 5 bullet points of on-slide text
- [ ] All speaker notes are under 200 words
- [ ] Max 2 slides per topic
- [ ] Podcast/Book/Infographic/History/Video picks are all selected
- [ ] Data is current (prices, rates, dates)
- [ ] Disclaimer slide present (education only, not financial advice)
- [ ] Demo has been tested and works
- [ ] Brand style matches (black bg, orange text, Calibri font)

---

## 7. Template

See `JC-BTC-3.19.md` as the first deck built with this process. Future decks should follow the same markdown structure.

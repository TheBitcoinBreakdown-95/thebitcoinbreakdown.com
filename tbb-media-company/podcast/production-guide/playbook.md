# TBB Podcast Production Playbook

> Ship first, perfect later. This is the minimum viable pipeline to get episodes live. Revisit and refine after the first 5 are published.

---

## Release Strategy

**Recommended order:**

1. **EP02 - Hello World** (~5 min) -- shortest script, lowest stakes, learn the pipeline
2. **EP01 - Golden Rules** (~18 min) -- the flagship premiere
3. **EP03 - Why Bitcoin?** (~12 min)
4. **EP04 - What is Money?** (~18 min)
5. **EP05 - Bitcoin Will Save the World** (~18 min)

Release one at a time. Each episode teaches you something about the process. Weekly or bi-weekly cadence -- whatever you can sustain.

---

## Phase 0: One-Time Setup

Do all of this before recording anything. Some steps have approval delays.

### Podcast Hosting (Spotify for Podcasters)

1. Create account at **podcasters.spotify.com**
2. Create a new show: "The Bitcoin Breakdown"
3. Upload cover art (3000x3000px ideal, 1400x1400 minimum, JPEG or PNG, under 512KB)
4. Set category: **Education > Self-Improvement**
5. Write show description (see below for draft)
6. Spotify auto-generates your **RSS feed URL** -- copy it

**Show description draft:**
> Bitcoin education for normal people. No jargon, no hype, no financial advice -- just the clearest explanation of why Bitcoin matters and how to use it. Hosted by GC, founder of The Bitcoin Breakdown. New episodes weekly.

Edit to taste. This appears on every podcast platform.

### RSS Distribution (Upload Once, Publish Everywhere)

Your RSS feed is the master file that every podcast app reads from. Submit it once to each platform:

| Platform | How to Submit | Timeline |
|----------|--------------|----------|
| Spotify | Automatic (you're hosting there) | Instant |
| Apple Podcasts | podcastsconnect.apple.com -- paste RSS URL | 24-72 hrs first review, instant after |
| YouTube Music | YouTube Studio > Podcasts > link RSS | 24-48 hrs |
| Podcast Index | podcastindex.org -- submit RSS | Same day |
| Amazon/Audible | Auto-pulled by Spotify for Podcasters | 24-48 hrs |
| iHeartRadio | Auto-pulled by Spotify for Podcasters | 24-48 hrs |

After the one-time submission, every new episode auto-distributes to all platforms. You only ever upload to Spotify for Podcasters.

### Cover Art

- Brand: V4 Dark Luxury (Gold #FFD700 + Black #000000 + Cream #E8E4DC)
- Fonts: Cormorant Garamond (serif), JetBrains Mono (mono)
- Tool: Canva (free) or Leonardo AI for generation + Canva for text
- Requirements: Show name readable at thumbnail size (small on phone screens)
- Can be changed later -- don't let this block you from shipping

### OBS Audio Setup

Settings for podcast-quality solo voice recording:

| Setting | Value |
|---------|-------|
| Audio Bitrate | 192 kbps |
| Sample Rate | 48 kHz |
| Recording Format | .mkv (crash-safe -- remux to .wav after) |
| Channels | Mono (solo voice, saves file size) |

**Add a noise suppression filter:**
1. Settings > Audio > your mic input
2. Right-click mic in Audio Mixer > Filters
3. Add "Noise Suppression" > select RNNoise
4. Done -- one click, significant background noise reduction

### Mic Technique

- 4-6 inches from the mic
- Slightly off-axis (angled, not directly in front) to reduce plosives (P/B pops)
- Consistent distance matters more than perfect distance
- Pop filter helps but is not required for "ship first" phase

### Test Recording

Before recording any real episode:
1. Record 2 minutes of talking in OBS
2. Remux .mkv to .wav (File > Remux Recordings)
3. Open in Audacity
4. Run noise reduction + normalize (see Phase 2)
5. Play back and confirm it sounds acceptable
6. Adjust mic position or OBS levels if needed

---

## Phase 1: Record

### Pre-Recording Checklist

- [ ] Close unnecessary apps (especially notifications)
- [ ] Script open on second monitor or printed
- [ ] Water nearby
- [ ] 10-second test recording -- confirm levels peak around -6 to -12 dB (never red)

### Recording Approach

- **One take.** Don't restart for stumbles.
- If you flub a line, **pause for 2 full seconds**, then re-say it cleanly. The silence gap makes it easy to find and cut in editing.
- Your scripts have tone shifts and rhythm cues in the production notes -- glance at those, don't read them aloud.
- Talk to one person, not an audience. Pretend someone asked you the question at a bar.
- Brain-dumping energy over teleprompter energy. Riff on the outline.

### After Recording

1. OBS: File > Remux Recordings > select .mkv > remux to .wav
2. Save raw file in episode folder: `episodes/ep01-golden-rules/raw-audio.wav`

---

## Phase 2: Edit

**Tool: Audacity (free)**

The goal is a clean listen, not a polished production. 15-30 minutes per episode max.

### Minimal Edit Pass

1. **Import** the .wav file into Audacity
2. **Noise reduction** (do this first):
   - Select 2-3 seconds of room silence (before you start talking)
   - Effect > Noise Reduction > Get Noise Profile
   - Select All (Ctrl+A) > Effect > Noise Reduction > OK (defaults are fine)
3. **Cut dead air:** Scroll through the waveform. Long flat sections = silence. Trim anything over 2 seconds down to ~1 second. Don't remove all pauses -- your scripts call for letting moments breathe.
4. **Cut bad takes:** Find the 2-second gaps before re-takes (visible in the waveform), delete the flubbed version, keep the clean one.
5. **Trim head and tail:** Cut pre-record silence and post-record fumbling.
6. **Normalize** (last step): Effect > Normalize > set to -1.0 dB. Brings volume to podcast standard.
7. **Export:** File > Export as MP3 > 192 kbps, Joint Stereo. Save as `episodes/ep01-golden-rules/ep01-golden-rules.mp3`

### Do NOT Do (Yet)

- EQ tweaking, compression, de-essing, or mixing
- Music, intros, or outros (add after 5 episodes when you know your rhythm)
- Spending more than 30 minutes editing

---

## Phase 3: Publish

### Episode Metadata (Per Episode)

| Field | Example (EP01) |
|-------|----------------|
| MP3 file | `ep01-golden-rules.mp3` |
| Title | The Golden Rules of Bitcoin |
| Episode number | 1 |
| Season | 1 |
| Type | Full (or "Trailer" for EP02 if released first) |
| Explicit | No |
| Description | Show notes (see Phase 4 -- Claude generates these) |

### Upload Flow

1. Go to podcasters.spotify.com > Episodes > New Episode
2. Upload MP3
3. Fill in metadata
4. Set publish date (immediate or scheduled)
5. Publish

All other platforms (Apple, Amazon, YouTube Music, etc.) auto-update from RSS within 1-4 hours.

---

## Phase 4: Post-Production (AI-Assisted)

After recording and editing, Claude generates from the script + transcript:

1. **Show notes** -- episode summary, timestamps, key quotes
2. **3-5 social posts** -- X/Twitter threads, standalone quotes, engagement hooks
3. **Blog post draft** (optional) -- adapted script as a TBB blog post with embedded player
4. **Newsletter snippet** (when subscriber base exists)

### Getting a Transcript

| Method | How | Quality |
|--------|-----|---------|
| Spotify for Podcasters | Auto-generates after upload | Good enough |
| Whisper (local) | `whisper ep01.mp3 --model base --language en` | Better accuracy |
| YouTube | Auto-captions if also uploaded to YouTube | Good enough |

Give Claude the transcript and script, and the post-production materials get generated in ~10 minutes of human review.

---

## Phase 5: Social and Distribution

### Launch Day (EP02 Trailer)

- Post on X: "The Bitcoin Breakdown podcast is live. [link]"
- Share the Spotify link (or the universal player link from Spotify for Podcasters)
- Keep it simple. Audience builds with consistency, not one big splash.

### Per-Episode Ongoing

- 1 post on X when episode drops (Claude drafts these)
- 1-2 quote clips from the episode over the following days
- Pin the latest episode on X profile

### Tools

| Tool | Purpose | Cost |
|------|---------|------|
| Buffer | Schedule posts across up to 3 channels | Free tier |
| Canva | Episode-specific graphics, audiograms | Free tier |

---

## Tool Stack Summary

| Tool | Purpose | Cost |
|------|---------|------|
| OBS | Recording | Free |
| Existing mic | Audio capture | Owned |
| Audacity | Audio editing (trim, noise reduction, normalize) | Free |
| Spotify for Podcasters | Hosting + RSS + distribution | Free |
| Whisper | Transcription (local) | Free |
| Claude | Scripts, show notes, social posts, repurposing | Existing |
| Buffer | Social scheduling | Free |
| Canva | Cover art, episode graphics | Free |
| Leonardo AI | Image generation for thumbnails/social | Free tier |

**Total cost: $0**

---

## Timeline: Getting Episode 1 Live

| Day | Task | Time |
|-----|------|------|
| Day 1 | Set up Spotify for Podcasters, upload cover art, submit RSS to Apple/Podcast Index | 1 hr |
| Day 1-2 | OBS test recording, Audacity test edit | 30 min |
| Day 2-3 | Record EP02 (Hello World, ~5 min script) | 20 min |
| Day 2-3 | Edit EP02 in Audacity | 15 min |
| Day 2-3 | Upload EP02 as trailer, publish | 15 min |
| Day 3-4 | Claude generates show notes + social posts | 10 min review |
| Day 4-7 | Record EP01 (Golden Rules, ~18 min script) | 40 min |
| Day 4-7 | Edit, publish, post | 45 min |

**First episode live within a week of starting.** After that, 1.5-2.5 hours per episode.

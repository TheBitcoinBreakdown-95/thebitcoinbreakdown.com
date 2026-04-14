# Per-Episode Checklist

> Copy this checklist for each episode. Work through it top to bottom.

---

## Episode: ___
**Script location:** `episodes/ep__-slug/script.md`
**Target length:** ___ min

---

### Prep

- [ ] Read through script, mark sections to riff on
- [ ] Add personal notes, cut anything that feels wrong
- [ ] Confirm OBS is set up (48kHz, 192kbps, .mkv, noise suppression on)

### Record

- [ ] Close all unnecessary apps and notifications
- [ ] Script visible on second monitor or printed
- [ ] Water nearby
- [ ] 10-second test -- levels peak -6 to -12 dB
- [ ] Record in one take (pause 2 seconds before re-takes on flubs)
- [ ] Remux .mkv to .wav (OBS > File > Remux Recordings)
- [ ] Save raw audio to episode folder

### Edit (Audacity)

- [ ] Import .wav
- [ ] Noise reduction (select silence > Get Noise Profile > Select All > Apply)
- [ ] Cut dead air (trim gaps over 2 seconds to ~1 second)
- [ ] Cut bad takes (find 2-second gaps, delete flub, keep clean version)
- [ ] Trim head and tail
- [ ] Normalize to -1.0 dB
- [ ] Export as MP3 (192 kbps, Joint Stereo)
- [ ] Save to episode folder as `ep__-slug.mp3`
- [ ] Listen to the full export once -- confirm no artifacts or missed cuts

### Post-Production (Claude)

- [ ] Get transcript (Whisper, Spotify auto, or YouTube auto)
- [ ] Claude generates: show notes, 3-5 social posts, blog draft (optional)
- [ ] Review and approve generated content

### Publish

- [ ] Upload MP3 to Spotify for Podcasters
- [ ] Fill metadata: title, episode number, season, description (show notes)
- [ ] Set publish date
- [ ] Publish

### Distribute

- [ ] Post on X with episode link
- [ ] Schedule 1-2 follow-up posts (quotes, hooks) via Buffer
- [ ] Pin latest episode on X profile
- [ ] Update episode roadmap status (`episode-roadmap.md`)

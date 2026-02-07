# The Bitcoin Breakdown - Implementation Tasks

## Quick Start (Resume)
```bash
cd c:\Users\GC\Documents\TBB\astro
npm run dev
```
Open http://localhost:4321 - See [CLAUDE.md](CLAUDE.md) for full context.

---

## Phase 1: Git & Folder Setup
- [x] Initialize Git repo at `c:\Users\GC\Documents\TBB`
- [x] Create folder structure in vault (`posts/`, `pages/`, `drafts/`, `assets/`, `templates/`)
- [x] Create `.gitignore`
- [ ] Create GitHub repository (public)
- [ ] Push initial commit

## Phase 2: Astro Project
- [x] Initialize Astro project in `astro/` subfolder
- [x] Configure `astro.config.mjs` with site URL
- [x] Create content collection config (`content.config.ts`)
- [x] Build layouts: BaseLayout, BlogPost, Page
- [x] Build pages: index, blog listing, dynamic post pages, RSS, sitemap
- [x] Build components: Header, Footer, Navigation, PostCard, SEO
- [x] Add basic styling
- [ ] Experiment with theme/design (edit `astro/src/styles/global.css`)

## Phase 3: WordPress Migration
- [x] Recover WordPress admin access
- [x] Export content via Tools > Export > All content (saved to TBB/)
- [ ] Run `wordpress-export-to-markdown` tool to convert XML → Markdown
- [ ] Move converted posts to `TBB/posts/`
- [ ] Update frontmatter on all posts
- [ ] Fix image paths
- [ ] Verify all content renders correctly

## Phase 4: GitHub Actions + Hostinger FTP Deploy
- [ ] Get Hostinger FTP credentials from hPanel
- [ ] Add FTP credentials as GitHub repository secrets
- [x] Create GitHub Actions workflow file (`.github/workflows/deploy.yml`)
- [ ] Backup existing WordPress files on Hostinger
- [ ] Test deployment

## Phase 5: Obsidian Workflow
- [ ] Set up Git credentials on Windows
- [x] Create blog post template in `TBB/templates/blog-post.md`
- [ ] Test full workflow: edit → commit/push → auto-deploy

## Phase 6: Go Live
- [ ] Test live site thoroughly
- [ ] Set up redirects from old WordPress URLs
- [ ] Document workflow for reference

---
title: "The Satoshi Agent"
description: "How we built a purpose-built AI research brain for Bitcoin -- 700+ sources, 3,500 chunks, and an agent that actually cites its work."
pubDate: 2026-04-16
author: "The Bitcoin Breakdown"
tags: ["bitcoin", "ai", "education", "open-source"]
image: ""
imageAlt: ""
draft: false
category: "blog"
subtitle: "How We Built Bitcoin's AI Research Brain"
---

Ask any AI about Bitcoin and you'll get an answer. It'll sound confident. It might even be correct. But ask it *where* it learned that, and you'll get silence. Ask it to cross-reference two sources, and it'll hallucinate a connection that doesn't exist. Ask it something that requires genuine depth -- the kind of understanding that comes from reading hundreds of articles, books, tweets, and protocol specs -- and you'll get a Wikipedia-grade summary dressed up in confident prose.

That's the problem. Not that AI can't talk about Bitcoin. It's that AI doesn't *know* Bitcoin. Not the way someone who's spent years reading, arguing, and building in this space knows it.

So we built something that does.

## What Is the Satoshi Agent?

The Satoshi Agent is a purpose-built research system that gives an AI direct access to a curated corpus of Bitcoin knowledge -- over 700 source files, spanning books, blog posts, tweets, academic papers, GitHub repositories, podcast transcripts, and original research notes. Every piece of content is chunked into searchable segments, embedded with semantic vectors, and indexed for both keyword and meaning-based retrieval.

It's not a chatbot. It's not a wrapper around a language model. It's a structured knowledge layer that an AI agent queries when it needs to reason about Bitcoin with depth, nuance, and citations.

When the Satoshi Agent searches for "how does Ark handle liquidity," it doesn't generate an answer from training data. It searches across 3,500+ indexed chunks, finds the relevant passages in protocol specs, blog posts, and research notes, ranks them by both keyword match and semantic similarity, and returns the actual text with source attribution. The AI then synthesizes an answer from real material -- material it can point to.

## Why We Built It

This project lives inside a larger effort called *WBIGAF* -- a book-length exploration of what Bitcoin did to the internet, and what the internet did to Bitcoin. Writing that book means engaging with hundreds of sources: Satoshi's original writings, cypherpunk mailing lists, economic arguments, protocol deep-dives, cultural commentary, and everything in between.

Keeping all of that in your head is impossible. Keeping it in a folder of bookmarks is barely better. What we needed was a system that could hold the entire corpus, understand the relationships between sources, and surface relevant material on demand -- not just when we remembered to look for it, but when a connection existed that we hadn't thought to make.

The Satoshi Agent is that system. It's the research brain behind the book, and increasingly, behind everything we publish.

## The Corpus

The knowledge base draws from eight distinct source types:

- **Book chapters and author notes** -- Original WBIGAF content, including argument catalogs that break complex topics into discrete, debatable claims.
- **Scraped articles** -- 780+ files pulled from the web. Blog posts, essays, research reports, and technical documentation from across the Bitcoin ecosystem.
- **Tweets and threads** -- 130+ captured Twitter conversations, including multi-tweet threads that most scrapers miss entirely.
- **Research notes** -- 360+ personal notes from the Bitcoin Notes vault -- annotations, summaries, and original analysis written during the research process.
- **Compendium articles** -- Published educational content from thebitcoinbreakdown.com, the kind of material that's been refined through multiple drafts and reader feedback.
- **Blog posts** -- Everything we've published, indexed and searchable alongside the source material that informed it.
- **GitHub content** -- READMEs, protocol specifications, pull request discussions, and technical proposals straight from the repositories where Bitcoin development happens.
- **Argument catalogs** -- Structured claim-by-claim breakdowns of Bitcoin debates, with each argument tagged by theme, source, and chapter.

In total: **1,378 files**, **3,548 searchable chunks**, and a **33 MB vector database** that powers semantic retrieval.

## How It Works

The system has four stages: **scrape**, **chunk**, **index**, and **query**. Each one is designed around the reality that Bitcoin knowledge comes in wildly different formats, and a one-size-fits-all approach loses too much.

### Scraping: Getting the Content

Not all sources cooperate. A direct HTTP request works for most articles, but the internet in 2026 is a maze of Cloudflare challenges, paywalls, JavaScript-rendered pages, and dead links. So the scraper uses a tiered approach:

1. **Direct fetch** -- Fast HTTP requests with browser-like headers. Works for most sites.
2. **Browser rendering** -- For JavaScript-heavy pages, a headless browser loads the page, waits for it to settle, and extracts the content. This catches everything that server-side rendering misses.
3. **Wayback Machine recovery** -- For dead links and 404s, we check the Internet Archive for cached versions. This recovered 44 sources that would otherwise be lost.
4. **Apify bypass** -- For sites with aggressive bot protection (looking at you, Medium behind Cloudflare), a dedicated crawler handles the CAPTCHA challenges.

Tweets get special treatment. Most scraping tools treat a tweet as a single post, but many important Bitcoin conversations happen in threads -- and those threads aren't always labeled. The scraper uses a dedicated Twitter API pathway that captures full threads, including unlabeled ones that simple heuristics miss.

### Chunking: Breaking It Down

A 10,000-word article and a three-sentence tweet need different handling. The chunker applies a different strategy based on source type:

- Long-form content gets split at section headers (H2 or H3), preserving the natural structure of the document.
- Author notes, which tend to be shorter and more focused, stay as single chunks.
- Argument catalogs split at each individual claim block, so every argument is independently searchable.
- Scraped articles skip files marked as failed or already covered by other sources, keeping the index clean.

Each chunk carries metadata: which chapter it belongs to, its source type, line numbers in the original file, and a unique identifier that lets you trace any search result back to its exact origin.

### Indexing: Making It Searchable

Every chunk gets two representations:

1. **A text index** for traditional keyword search (BM25 ranking). When you search for "Lightning Network capacity," it finds chunks that contain those exact words.
2. **A vector embedding** for semantic search. When you search for "how do payment channels scale," it finds chunks that discuss the concept even if they never use the word "scale."

The vectors come from a local embedding model running on the same machine -- no data leaves the system, no API calls to external services. The entire index rebuilds from scratch in about an hour, or incrementally in seconds when only a few files change.

### Querying: The Four Tools

The Satoshi Agent exposes four search tools through the Model Context Protocol (MCP), a standard interface that lets AI assistants call external tools:

**Search Corpus** -- The primary tool. Takes a natural language query, expands it with Bitcoin-specific synonyms (so "Satoshi" also matches "Nakamoto" and "creator"), runs both keyword and semantic search in parallel, and merges the results using Reciprocal Rank Fusion. Returns the full text of the top results with source attribution. Filters by source type and chapter.

**Find Related** -- Takes a chunk you've already found and discovers semantically similar content across the entire corpus. This is where unexpected connections surface -- a tweet thread that echoes an argument from a 2014 blog post, or a GitHub PR discussion that resolves a question raised in a research note.

**Get Chunk** -- Direct retrieval when you know exactly what you're looking for. Fetch a specific passage by file path and heading.

**List Sources** -- A bird's-eye view of the entire corpus, organized by chapter and source type. Useful for understanding what's indexed and where the gaps are.

## What Changes

The difference between a general-purpose AI and one backed by the Satoshi Agent isn't subtle. It's the difference between "Bitcoin uses a blockchain" and "Hal Finney's RPOW system preceded Bitcoin's proof-of-work by four years, and Satoshi cited it in early correspondence -- see the 2008 Cryptography Mailing List thread."

Concretely, here's what it enables:

- **Cross-source discovery.** Ask about a concept and get results from a book chapter, a tweet thread, a blog post, and a GitHub PR -- all discussing the same idea from different angles, with no manual cross-referencing.
- **Cited answers.** Every claim traces back to a specific chunk in a specific file. No hallucinated sources, no confident fabrications.
- **Gap detection.** When researching a topic for the book, the agent can tell us not just what sources exist, but where the coverage is thin -- which arguments lack supporting evidence, which chapters need more diverse source material.
- **Living research.** New sources get scraped, chunked, and indexed incrementally. The corpus grows as the research continues, and old queries return richer results over time.

## The Bigger Picture

The Satoshi Agent is one piece of a larger system for producing rigorous Bitcoin education. The corpus feeds the book. The book produces compendium articles for the website. The website surfaces ideas that drive new research. It's a loop -- and the agent sits at the center of it, making sure nothing gets lost between iterations.

We're building this in the open because we think Bitcoin education deserves better tooling. Most of what passes for Bitcoin content online is either too shallow to be useful or too tribal to be trustworthy. The corpus approach forces a different standard: every claim has a source, every argument has a counter-argument, and the AI can only work with what's actually in the knowledge base.

It's not a replacement for reading the sources yourself. It's a way to make sure you don't miss the connection between source 47 and source 683 that changes how you think about the whole picture.

## What's Next

The corpus is indexed and searchable. The next phase is **claim extraction** -- having the AI read through every source and generate structured argument blocks: a claim, its evidence, its counter-arguments, and its source chain. That transforms the corpus from a searchable library into a structured debate map.

After that: deeper integration with the website, so published articles automatically link to their underlying source material. Readers will be able to trace any claim in any article back through the research that supports it.

The Satoshi Agent doesn't know everything about Bitcoin. But it knows where to look, it shows its work, and it gets smarter every time we feed it a new source. That's more than most can say.

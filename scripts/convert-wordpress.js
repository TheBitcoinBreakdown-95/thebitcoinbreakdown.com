/**
 * WordPress XML Export → Markdown Converter
 *
 * Reads the WordPress WXR export and converts posts/pages to Markdown files
 * with proper Astro frontmatter. Uses Turndown for HTML→Markdown conversion.
 *
 * Usage: node scripts/convert-wordpress.js
 */

const fs = require('fs');
const path = require('path');
const TurndownService = require('turndown');

// --- Configuration ---
const XML_PATH = path.join(__dirname, '..', 'TBB', 'thebitcoinbreakdown.WordPress.2026-02-05.xml');
const POSTS_DIR = path.join(__dirname, '..', 'TBB', 'posts');
const PAGES_DIR = path.join(__dirname, '..', 'TBB', 'pages');

// Pages to skip (WordPress boilerplate, empty stubs)
const SKIP_SLUGS = new Set([
  'sample-page',
  'privacy-policy',
  'test-1',
  'test-2',
  'homepage',  // We already have a custom homepage
]);

// Posts that are just navigation stubs (empty content)
const SKIP_EMPTY = true;

// --- Setup Turndown ---
const turndown = new TurndownService({
  headingStyle: 'atx',
  bulletListMarker: '-',
  codeBlockStyle: 'fenced',
  emDelimiter: '*',
  strongDelimiter: '**',
});

// Custom rule: WordPress figure + img → Markdown image
turndown.addRule('wpFigure', {
  filter: function (node) {
    return node.nodeName === 'FIGURE' && node.querySelector('img');
  },
  replacement: function (content, node) {
    const img = node.querySelector('img');
    const caption = node.querySelector('figcaption');
    const src = img.getAttribute('src') || '';
    const alt = img.getAttribute('alt') || '';
    const captionText = caption ? caption.textContent.trim() : '';

    if (captionText) {
      return `\n\n![${alt}](${src})\n*${captionText}*\n\n`;
    }
    return `\n\n![${alt}](${src})\n\n`;
  }
});

// Custom rule: WordPress buttons → plain links
turndown.addRule('wpButton', {
  filter: function (node) {
    return node.nodeName === 'DIV' &&
           node.getAttribute('class') &&
           node.getAttribute('class').includes('wp-block-button');
  },
  replacement: function (content, node) {
    const link = node.querySelector('a');
    if (link) {
      return `[${link.textContent.trim()}](${link.getAttribute('href') || ''})`;
    }
    return content;
  }
});

// --- XML Parsing (regex-based for WXR format) ---
function parseXML(xmlContent) {
  const items = [];
  // Split on <item> tags
  const itemRegex = /<item>([\s\S]*?)<\/item>/g;
  let match;

  while ((match = itemRegex.exec(xmlContent)) !== null) {
    const itemXml = match[1];

    const title = extractCDATA(itemXml, 'title') || '';
    const slug = extractCDATA(itemXml, 'wp:post_name') || '';
    const status = extractCDATA(itemXml, 'wp:status') || '';
    const postType = extractCDATA(itemXml, 'wp:post_type') || '';
    const postDate = extractCDATA(itemXml, 'wp:post_date') || '';
    const content = extractEncodedContent(itemXml) || '';

    // Extract categories
    const categories = [];
    const catRegex = /category domain="category"[^>]*><!\[CDATA\[(.*?)\]\]>/g;
    let catMatch;
    while ((catMatch = catRegex.exec(itemXml)) !== null) {
      categories.push(catMatch[1]);
    }

    items.push({ title, slug, status, postType, postDate, content, categories });
  }

  return items;
}

function extractCDATA(xml, tag) {
  // Handle both <tag><![CDATA[value]]></tag> and <tag>value</tag>
  const cdataRegex = new RegExp(`<${escapeRegex(tag)}><!\\[CDATA\\[([\\s\\S]*?)\\]\\]></${escapeRegex(tag)}>`, 'i');
  const plainRegex = new RegExp(`<${escapeRegex(tag)}>([^<]*)</${escapeRegex(tag)}>`, 'i');

  let match = xml.match(cdataRegex);
  if (match) return match[1];

  match = xml.match(plainRegex);
  if (match) return match[1];

  return null;
}

function extractEncodedContent(xml) {
  const match = xml.match(/<content:encoded><!\[CDATA\[([\s\S]*?)\]\]><\/content:encoded>/);
  return match ? match[1] : '';
}

function escapeRegex(str) {
  return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

// --- Content Processing ---
function stripGutenbergComments(html) {
  // Remove WordPress Gutenberg block comments: <!-- wp:xxx --> and <!-- /wp:xxx -->
  return html.replace(/<!--\s*\/?wp:[^>]*-->/g, '');
}

function htmlToMarkdown(html) {
  if (!html || !html.trim()) return '';

  // Strip Gutenberg comments first
  let cleaned = stripGutenbergComments(html);

  // Remove empty div wrappers left by Gutenberg
  cleaned = cleaned.replace(/<div class="wp-block-buttons[^"]*">\s*<\/div>/g, '');
  cleaned = cleaned.replace(/<div class="wp-block-button[^"]*">\s*<\/div>/g, '');

  // Convert with Turndown
  let markdown = turndown.turndown(cleaned);

  // Clean up excessive blank lines
  markdown = markdown.replace(/\n{4,}/g, '\n\n\n');

  // Clean up any leftover HTML entities
  markdown = markdown.replace(/&#8217;/g, "'");
  markdown = markdown.replace(/&#8216;/g, "'");
  markdown = markdown.replace(/&#8220;/g, '"');
  markdown = markdown.replace(/&#8221;/g, '"');
  markdown = markdown.replace(/&#8211;/g, '–');
  markdown = markdown.replace(/&#8212;/g, '—');
  markdown = markdown.replace(/&amp;/g, '&');
  markdown = markdown.replace(/&#241;/g, 'ñ');
  markdown = markdown.replace(/&nbsp;/g, ' ');

  return markdown.trim();
}

function generateDescription(markdown, title) {
  // Take first paragraph as description, capped at 160 chars
  const lines = markdown.split('\n').filter(l => l.trim() && !l.startsWith('#') && !l.startsWith('!'));
  const firstPara = lines[0] || '';
  // Strip markdown formatting for description
  const plain = firstPara.replace(/\*\*(.*?)\*\*/g, '$1').replace(/\*(.*?)\*/g, '$1').replace(/\[(.*?)\]\(.*?\)/g, '$1').trim();
  if (plain.length > 155) {
    return plain.substring(0, 152) + '...';
  }
  return plain || `${title} - The Bitcoin Breakdown`;
}

function inferTags(title, content, categories) {
  const tags = ['bitcoin'];
  const lowerTitle = title.toLowerCase();
  const lowerContent = content.toLowerCase().substring(0, 2000);

  if (lowerTitle.includes('scarcity') || lowerContent.includes('21 million') || lowerContent.includes('hard cap')) {
    tags.push('scarcity');
  }
  if (lowerTitle.includes('satoshi') || lowerContent.includes('satoshi nakamoto')) {
    tags.push('satoshi');
  }
  if (lowerTitle.includes('money') || lowerContent.includes('store of value') || lowerContent.includes('monetary')) {
    tags.push('money');
  }
  if (lowerTitle.includes('network') || lowerContent.includes('decentralized') || lowerContent.includes('nodes')) {
    tags.push('network');
  }
  if (lowerTitle.includes('trust') || lowerContent.includes('trustless')) {
    tags.push('trust');
  }
  if (lowerTitle.includes('gold') || lowerContent.includes('digital gold')) {
    tags.push('digital-gold');
  }
  if (lowerTitle.includes('time') || lowerContent.includes('timechain')) {
    tags.push('time');
  }
  if (lowerTitle.includes('freedom') || lowerContent.includes('censorship') || lowerContent.includes('human rights')) {
    tags.push('freedom');
  }
  if (lowerTitle.includes('ethical') || lowerContent.includes('ethical')) {
    tags.push('ethics');
  }
  if (lowerTitle.includes('speech') || lowerTitle.includes('[speech]')) {
    tags.push('speech');
  }
  if (lowerTitle.includes('internet of money')) {
    tags.push('technology');
  }
  if (lowerTitle.includes('save the world') || lowerContent.includes('environment') || lowerContent.includes('energy')) {
    tags.push('energy');
  }

  return [...new Set(tags)];
}

// --- File Output ---
function sanitizeTitle(title) {
  // Escape quotes in YAML
  return title.replace(/"/g, '\\"');
}

function buildFrontmatter(item, markdown) {
  const date = item.postDate.split(' ')[0]; // YYYY-MM-DD
  const isDraft = item.status === 'draft' || item.status === 'private';
  const description = generateDescription(markdown, item.title);
  const tags = inferTags(item.title, markdown, item.categories);

  let fm = `---\n`;
  fm += `title: "${sanitizeTitle(item.title)}"\n`;
  fm += `description: "${sanitizeTitle(description)}"\n`;
  fm += `pubDate: ${date}\n`;
  fm += `author: "The Bitcoin Breakdown"\n`;
  fm += `tags: [${tags.map(t => `"${t}"`).join(', ')}]\n`;
  if (isDraft) {
    fm += `draft: true\n`;
  }
  fm += `---\n`;

  return fm;
}

function buildPageFrontmatter(item) {
  let fm = `---\n`;
  fm += `title: "${sanitizeTitle(item.title)}"\n`;
  fm += `---\n`;
  return fm;
}

// --- Main ---
function main() {
  console.log('Reading WordPress export...');
  const xml = fs.readFileSync(XML_PATH, 'utf-8');

  console.log('Parsing items...');
  const items = parseXML(xml);
  console.log(`Found ${items.length} total items`);

  // Filter to posts and pages
  const posts = items.filter(i => i.postType === 'post');
  const pages = items.filter(i => i.postType === 'page');

  console.log(`\nPosts: ${posts.length}`);
  console.log(`Pages: ${pages.length}`);

  // --- Process Posts ---
  let postCount = 0;
  let skippedCount = 0;

  for (const post of posts) {
    // Skip empty content
    if (SKIP_EMPTY && !post.content.trim()) {
      console.log(`  SKIP (empty): "${post.title}" [${post.slug}]`);
      skippedCount++;
      continue;
    }

    // Skip the default WordPress hello world post
    if (post.slug === 'hello-world') {
      console.log(`  SKIP (WP default): "${post.title}"`);
      skippedCount++;
      continue;
    }

    const markdown = htmlToMarkdown(post.content);

    // Skip if markdown is too short (likely just a stub)
    if (markdown.length < 50) {
      console.log(`  SKIP (stub, ${markdown.length} chars): "${post.title}" [${post.slug}]`);
      skippedCount++;
      continue;
    }

    const frontmatter = buildFrontmatter(post, markdown);
    const fullContent = frontmatter + '\n' + markdown + '\n';

    // Organize by year
    const year = post.postDate.substring(0, 4);
    const dir = path.join(POSTS_DIR, year);
    fs.mkdirSync(dir, { recursive: true });

    const filePath = path.join(dir, `${post.slug}.md`);
    fs.writeFileSync(filePath, fullContent, 'utf-8');

    console.log(`  POST: "${post.title}" → ${year}/${post.slug}.md (${post.status})`);
    postCount++;
  }

  // --- Process Pages ---
  let pageCount = 0;

  for (const page of pages) {
    if (SKIP_SLUGS.has(page.slug)) {
      console.log(`  SKIP (boilerplate): "${page.title}" [${page.slug}]`);
      skippedCount++;
      continue;
    }

    if (SKIP_EMPTY && !page.content.trim()) {
      console.log(`  SKIP (empty): "${page.title}" [${page.slug}]`);
      skippedCount++;
      continue;
    }

    const markdown = htmlToMarkdown(page.content);

    if (markdown.length < 20) {
      console.log(`  SKIP (stub, ${markdown.length} chars): "${page.title}" [${page.slug}]`);
      skippedCount++;
      continue;
    }

    const frontmatter = buildPageFrontmatter(page);
    const fullContent = frontmatter + '\n' + markdown + '\n';

    fs.mkdirSync(PAGES_DIR, { recursive: true });

    const filePath = path.join(PAGES_DIR, `${page.slug}.md`);
    fs.writeFileSync(filePath, fullContent, 'utf-8');

    console.log(`  PAGE: "${page.title}" → pages/${page.slug}.md (${page.status})`);
    pageCount++;
  }

  console.log(`\n--- Done ---`);
  console.log(`Converted: ${postCount} posts, ${pageCount} pages`);
  console.log(`Skipped: ${skippedCount}`);
}

main();

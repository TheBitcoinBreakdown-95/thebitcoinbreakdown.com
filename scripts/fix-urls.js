/**
 * Fix image URLs and internal links in all post markdown files.
 *
 * 1. Image URLs: Replace WordPress URLs with local paths
 *    https://thebitcoinbreakdown.com/wp-content/uploads/YYYY/MM/file.ext → /images/YYYY/MM/file.ext
 *    http://thebitcoinbreakdown.com/wp-content/uploads/YYYY/MM/file.ext  → /images/YYYY/MM/file.ext
 *
 * 2. Internal links: Replace old WordPress slugs with new Astro routes
 *    https://thebitcoinbreakdown.com/slug/ → /blog/YYYY/slug/
 */

const fs = require('fs');
const path = require('path');

function globSync(pattern, dir) {
  const results = [];
  function walk(currentDir, relDir) {
    const entries = fs.readdirSync(currentDir, { withFileTypes: true });
    for (const entry of entries) {
      const rel = relDir ? relDir + '/' + entry.name : entry.name;
      if (entry.isDirectory()) {
        walk(path.join(currentDir, entry.name), rel);
      } else if (entry.name.endsWith('.md')) {
        results.push(rel);
      }
    }
  }
  walk(dir, '');
  return results;
}

// Slug → Astro route mapping (based on actual file locations)
const linkMap = {
  'the-trust-machine': '/blog/2022/the-trust-machine/',
  'absolute-scarcity': '/blog/2022/absolute-scarcity/',
  'the-mystery-of-satoshi-nakamoto': '/blog/2022/the-mystery-of-satoshi-nakamoto/',
  'intro': '/blog/2023/intro/',
  'what-is-bitcoin-2': '/blog/2023/what-is-bitcoin-2/',
  'bitcoin-is-digital-gold': '/blog/2023/bitcoin-is-digital-gold/',
  'the-great-excel-spreadsheet-in-the-sky': '/blog/2023/the-great-excel-spreadsheet-in-the-sky/',
  'bitcoin-is-information': '/blog/2023/bitcoin-is-information/',
  'what-is-bitcoin-3': '/blog/2023/what-is-bitcoin-3/',
  'bitcoin-is-a-network': '/blog/2023/bitcoin-is-a-network/',
  'bitcoin-is-time': '/blog/2023/bitcoin-is-time/',
  'bitcoin-is-money': '/blog/2023/bitcoin-is-money/',
  'bitcoin-is-the-internet-of-money': '/blog/2023/bitcoin-is-the-internet-of-money/',
  'bitcoin-will-save-the-world': '/blog/2023/bitcoin-will-save-the-world/',
  'why-was-bitcoin-invented': '/blog/2023/why-was-bitcoin-invented/',
  'why-will-bitcoin-win': '/blog/2023/why-will-bitcoin-win/',
  'why-should-you-care': '/blog/2023/why-should-you-care/',
  'bitcoin-is-ethical-money': '/blog/2023/bitcoin-is-ethical-money/',
  'the-manhattan-project-for-human-freedom': '/blog/2023/the-manhattan-project-for-human-freedom/',
  'they-invented-a-better-money-who-does-that': '/blog/2023/they-invented-a-better-money-who-does-that/',
  'other-peoples-bitcoin-definitions': '/blog/2023/other-peoples-bitcoin-definitions/',
  'orange-not-gold': '/blog/2023/orange-not-gold/',
  'unparalleled-old': '/blog/2023/unparalleled-old/',
  'unparalleled-new': '/blog/2023/unparalleled-new/',
  'memes': '/blog/2023/memes/',
  'about': '/blog/2023/about/',
  'what-is-bitcoin': '/blog/2023/what-is-bitcoin/',
  'the-trust-machine-speech': '/blog/2025/the-trust-machine-speech/',
};

const postsDir = path.join(__dirname, '..', 'TBB', 'posts');
const files = globSync('**/*.md', postsDir);

let totalImageFixes = 0;
let totalLinkFixes = 0;

for (const file of files) {
  const filePath = path.join(postsDir, file);
  let content = fs.readFileSync(filePath, 'utf-8');
  const original = content;

  // 1. Fix image URLs (both http and https)
  const imageFixCount = (content.match(/https?:\/\/thebitcoinbreakdown\.com\/wp-content\/uploads\//g) || []).length;
  content = content.replace(/https?:\/\/thebitcoinbreakdown\.com\/wp-content\/uploads\//g, '/images/');
  totalImageFixes += imageFixCount;

  // 2. Fix internal links
  // Match patterns like (https://thebitcoinbreakdown.com/slug/) in markdown links
  content = content.replace(
    /\(https?:\/\/thebitcoinbreakdown\.com\/([a-z0-9-]+)\/?\)/g,
    (match, slug) => {
      if (linkMap[slug]) {
        totalLinkFixes++;
        return `(${linkMap[slug]})`;
      }
      console.log(`  WARNING: Unknown slug "${slug}" in ${file}`);
      return match;
    }
  );

  if (content !== original) {
    fs.writeFileSync(filePath, content, 'utf-8');
    const imgCount = imageFixCount;
    const linkCount = content !== original ? '(links fixed)' : '';
    console.log(`Updated: ${file} (${imgCount} images${linkCount})`);
  }
}

console.log(`\nTotal: ${totalImageFixes} image URLs fixed, ${totalLinkFixes} internal links fixed across ${files.length} files`);

/**
 * Add category and order frontmatter to all post markdown files.
 */

const fs = require('fs');
const path = require('path');

const postsDir = path.join(__dirname, '..', 'TBB', 'posts');

// Category assignments with reading order
const categories = {
  'what-is-bitcoin': [
    '2023/intro.md',
    '2023/what-is-bitcoin-2.md',
    '2023/bitcoin-is-digital-gold.md',
    '2023/the-great-excel-spreadsheet-in-the-sky.md',
    '2023/bitcoin-is-information.md',
    '2023/what-is-bitcoin-3.md',
    '2023/bitcoin-is-a-network.md',
    '2023/bitcoin-is-time.md',
    '2023/bitcoin-is-money.md',
    '2023/bitcoin-is-the-internet-of-money.md',
    '2023/other-peoples-bitcoin-definitions.md',
  ],
  'why-bitcoin': [
    '2023/why-should-you-care.md',
    '2023/bitcoin-will-save-the-world.md',
    '2023/why-was-bitcoin-invented.md',
    '2023/why-will-bitcoin-win.md',
    '2022/absolute-scarcity.md',
    '2022/the-trust-machine.md',
    '2023/they-invented-a-better-money-who-does-that.md',
    '2023/bitcoin-is-ethical-money.md',
    '2023/the-manhattan-project-for-human-freedom.md',
    '2023/unparalleled-old.md',
    '2023/unparalleled-new.md',
    '2023/orange-not-gold.md',
  ],
  'memes': [
    '2023/memes.md',
  ],
  'speeches': [
    '2025/the-trust-machine-speech.md',
    '2022/the-mystery-of-satoshi-nakamoto.md',
  ],
};

// Posts to mark as draft (remove from blog)
const markDraft = [
  '2023/about.md',       // Becomes the About page
  '2023/what-is-bitcoin.md', // Earlier combined version, already draft
];

// Build reverse lookup: file → { category, order }
const fileCategoryMap = {};
for (const [category, files] of Object.entries(categories)) {
  files.forEach((file, index) => {
    fileCategoryMap[file] = { category, order: index + 1 };
  });
}

// Process all files
function walk(dir, relDir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const rel = relDir ? relDir + '/' + entry.name : entry.name;
    if (entry.isDirectory()) {
      walk(path.join(dir, entry.name), rel);
    } else if (entry.name.endsWith('.md')) {
      processFile(rel);
    }
  }
}

function processFile(relPath) {
  const filePath = path.join(postsDir, relPath);
  let content = fs.readFileSync(filePath, 'utf-8');

  // Parse frontmatter
  const fmMatch = content.match(/^---\n([\s\S]*?)\n---/);
  if (!fmMatch) {
    console.log(`  SKIP (no frontmatter): ${relPath}`);
    return;
  }

  let frontmatter = fmMatch[1];
  let changed = false;

  // Add category and order if mapped
  const mapping = fileCategoryMap[relPath];
  if (mapping) {
    if (!frontmatter.includes('category:')) {
      frontmatter += `\ncategory: "${mapping.category}"`;
      changed = true;
    }
    if (!frontmatter.includes('order:')) {
      frontmatter += `\norder: ${mapping.order}`;
      changed = true;
    }
  }

  // Mark draft for specific files
  if (markDraft.includes(relPath)) {
    if (!frontmatter.includes('draft: true')) {
      frontmatter = frontmatter.replace(/draft:\s*false/, 'draft: true');
      if (!frontmatter.includes('draft:')) {
        frontmatter += '\ndraft: true';
      }
      changed = true;
    }
  }

  if (changed) {
    content = content.replace(/^---\n[\s\S]*?\n---/, `---\n${frontmatter}\n---`);
    fs.writeFileSync(filePath, content, 'utf-8');
    const info = mapping ? `category="${mapping.category}", order=${mapping.order}` : 'draft=true';
    console.log(`Updated: ${relPath} (${info})`);
  }
}

walk(postsDir, '');
console.log('\nDone!');

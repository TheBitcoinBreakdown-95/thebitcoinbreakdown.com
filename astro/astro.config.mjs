// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import remarkCallout from '@r4ai/remark-callout';
import { visit } from 'unist-util-visit';

// Custom rehype plugin: adds loading="lazy" and decoding="async" to all <img> tags
function rehypeLazyImages() {
  return (tree) => {
    visit(tree, 'element', (node) => {
      if (node.tagName === 'img') {
        node.properties = node.properties || {};
        node.properties.loading = 'lazy';
        node.properties.decoding = 'async';
      }
    });
  };
}

// Custom rehype plugin: wraps <img> with non-empty alt text in <figure>/<figcaption>
function rehypeImageCaptions() {
  return (tree) => {
    visit(tree, 'element', (node, index, parent) => {
      if (
        node.tagName === 'img' &&
        node.properties?.alt &&
        node.properties.alt.trim() !== '' &&
        parent?.tagName !== 'figure'
      ) {
        const caption = node.properties.alt;
        const figure = {
          type: 'element',
          tagName: 'figure',
          properties: { className: ['image-figure'] },
          children: [
            node,
            {
              type: 'element',
              tagName: 'figcaption',
              properties: {},
              children: [{ type: 'text', value: caption }]
            }
          ]
        };
        parent.children[index] = figure;
      }
    });
  };
}

// https://astro.build/config
export default defineConfig({
  site: 'https://thebitcoinbreakdown.com',
  integrations: [sitemap()],
  markdown: {
    shikiConfig: {
      theme: 'github-dark',
      wrap: true
    },
    remarkPlugins: [remarkCallout],
    rehypePlugins: [rehypeLazyImages, rehypeImageCaptions]
  }
});

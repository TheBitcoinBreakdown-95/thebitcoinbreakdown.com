import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: '../TBB/posts' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    author: z.string().default('The Bitcoin Breakdown'),
    tags: z.array(z.string()).default([]),
    image: z.string().optional(),
    imageAlt: z.string().optional(),
    draft: z.boolean().default(false),
    category: z.string().optional(),
    order: z.number().optional(),
  })
});

const guide = defineCollection({
  loader: glob({ pattern: '**/*.md', base: '../TBB/guide' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    chapter: z.number(),
    order: z.number().default(1),
    layout: z.enum(['prose', 'blocks']).default('prose'),
    draft: z.boolean().default(false),
  })
});

const ai = defineCollection({
  loader: glob({ pattern: '**/*.md', base: '../TBB/ai' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    author: z.string().default('The Bitcoin Breakdown'),
    tags: z.array(z.string()).default([]),
    image: z.string().optional(),
    imageAlt: z.string().optional(),
    draft: z.boolean().default(false),
    category: z.string().optional(),
    order: z.number().optional(),
  })
});

const pages = defineCollection({
  loader: glob({ pattern: '**/*.md', base: '../TBB/pages' }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
  })
});

export const collections = { posts, pages, guide, ai };

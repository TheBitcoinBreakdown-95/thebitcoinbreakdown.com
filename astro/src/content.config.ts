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
  })
});

const pages = defineCollection({
  loader: glob({ pattern: '**/*.md', base: '../TBB/pages' }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
  })
});

export const collections = { posts, pages };

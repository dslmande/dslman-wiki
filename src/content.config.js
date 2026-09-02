import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const wiki = defineCollection({
  loader: glob({ pattern: '**/index.md', base: './content' }),
  schema: z.object({
    title: z.string(),
    space: z.string().optional(),
    space_key: z.string().optional(),
    type: z.string().optional(),
    created: z.string().optional(),
    updated: z.string().optional(),
    confluence_id: z.string().optional(),
    confluence_url: z.string().optional(),
    attachments: z.number().optional(),
  }),
});

export const collections = { wiki };

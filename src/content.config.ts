import { z } from "astro/zod";
import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";

const blogCollection = defineCollection({
  loader: glob({ pattern: "**/*.{md,mdx}", base: "./src/content/blog" }),
  schema: z.object({
    title: z.string(),
    date: z.date(),
    author: z.string(),
    tags: z.array(z.string()).optional(),
    keywords: z.array(z.string()).optional(),
    draft: z.boolean().optional(),
    image: z.string().optional(),
    description: z.string(),
  }),
});

export const collections = {
  blog: blogCollection,
};

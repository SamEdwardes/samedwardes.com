import { getCollection } from "astro:content";

async function getPosts() {
  const posts = (
    await getCollection("blog", ({ data }) => {
      return data.draft !== true;
    })
  ).sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());

  // return posts;
  return posts.map((post) => ({
    slug: post.slug,
    title: post.data.title,
    description: post.data.description,
    tags: post.data.tags,
    keywords: post.data.keywords,
    date: post.data.date,
  }));
}

export async function GET({}) {
  return new Response(JSON.stringify(await getPosts()), {
    status: 200,
    headers: {
      "Content-Type": "application/json",
    },
  });
}

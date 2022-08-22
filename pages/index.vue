<template>
  <div>
    <div v-for="post in blogPosts">
      <h2 class="mt-4">
        <NuxtLink :to="post._path">
          <BaseLink>
            {{ post.title }}
          </BaseLink>
        </NuxtLink>
      </h2>
      <p>{{post.description }}</p>
    </div>
  </div>
</template>

<script setup>
const { data: blogPosts } = await useAsyncData(`all-blog-posts`, () => {
  return queryContent('/blog/')
  .only(['title', 'description', "_path", "_slug"])
  .sort({ _path: -1 })
  .find()
})

console.log(blogPosts.value)

const { data: navigation } = await useAsyncData('navigation', () => fetchContentNavigation())

console.log(navigation.value)
</script>
<script setup lang="ts">
const people = ["Llama 3", "ChatGPT", "Claude 3.5 Sonnet"]

const selected = ref(people[0])
</script>

<template>
  <header
    class="flex w-full justify-between border-b border-neutral-200 p-2 px-4 dark:border-neutral-800"
  >
    <USelectMenu v-model="selected" :options="people" class="w-44" />
    <div class="space-x-2">
      <UButton
        icon="i-heroicons-information-circle"
        size="sm"
        color="gray"
        square
        variant="soft"
      />
      <UButton
        icon="i-heroicons-pencil-square"
        size="sm"
        color="gray"
        square
        variant="soft"
      />
    </div>
  </header>
</template>

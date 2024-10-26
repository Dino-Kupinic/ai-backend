<script setup lang="ts">
defineProps<{
  isSender: boolean
}>()
</script>

<template>
  <div :class="['flex', isSender ? 'justify-end' : 'justify-start']">
    <div
      v-if="!isSender"
      class="mt-6 flex h-9 w-9 items-center justify-center rounded-full border border-neutral-200 p-1 dark:border-neutral-700"
    >
      <Icon
        name="i-heroicons-sparkles-solid"
        size="24"
        class="bg-gradient-to-r from-purple-400 via-blue-400 via-20% to-pink-400"
      />
    </div>
    <p
      :class="[
        'text my-3 rounded-lg px-4 py-3 font-light',
        isSender
          ? 'mx-9 max-w-sm bg-neutral-100 dark:bg-neutral-800 dark:text-neutral-300'
          : 'ml-6 mr-9',
      ]"
    >
      <slot />
    </p>
  </div>
</template>

<script setup lang="ts">
const input = ref<string>("")
</script>

<template>
  <div class="flex h-full flex-col">
    <ChatHeader />
    <UContainer class="w-full grow overflow-y-auto"> </UContainer>
    <UInput
      v-model="input"
      placeholder="Send a message"
      class="border-t border-neutral-200 p-3 dark:border-neutral-800"
    />
  </div>
</template>

<style scoped></style>

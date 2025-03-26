<script setup lang="ts">
const { sendMessage, input } = useChat()

const send = async () => {
  await sendMessage()
}
</script>

<template>
  <div
    class="mx-auto flex w-xl flex-col rounded-3xl border border-neutral-200 p-3 pt-2 shadow-sm lg:w-2xl xl:w-3xl dark:border-neutral-800 dark:!shadow-none"
  >
    <UTextarea
      v-model="input"
      :ui="{ base: 'resize-none' }"
      class="w-full grow"
      variant="none"
      autoresize
      :rows="1"
      :maxrows="6"
      size="lg"
      placeholder="Send a message"
      @keyup.enter="send"
    />
    <div class="flex items-center">
      <UButton
        color="neutral"
        variant="link"
        size="md"
        icon="i-flowbite-paper-clip-outline"
      />
      <UButton
        color="neutral"
        variant="link"
        size="md"
        icon="i-tabler-microphone-filled"
      />
    </div>
  </div>
</template>

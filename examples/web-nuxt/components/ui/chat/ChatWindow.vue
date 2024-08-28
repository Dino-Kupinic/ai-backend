<script setup lang="ts">
const input = ref<string>("")
</script>

<template>
  <div class="flex h-full flex-col">
    <ChatHeader />
    <div class="w-full grow overflow-y-auto sm:px-32">
      <ChatMessage :is-sender="true">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
        commodo consequat.
      </ChatMessage>
      <ChatMessage :is-sender="false">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
        commodo consequat.
      </ChatMessage>
    </div>
    <div class="flex items-end p-4 sm:px-32">
      <UButton
        color="gray"
        variant="link"
        size="md"
        icon="i-flowbite-paper-clip-outline"
      />
      <UTextarea
        v-model="input"
        class="grow"
        autoresize
        :rows="1"
        :maxrows="8"
        size="md"
        placeholder="Send a message"
      />
      <UButton
        color="gray"
        variant="link"
        size="md"
        icon="i-tabler-microphone-filled"
      />
    </div>
  </div>
</template>

<style scoped></style>

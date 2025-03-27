<script setup lang="ts">
const { data, text, isLoading, thinking } = useChat()
</script>

<template>
  <div class="flex h-full flex-col">
    <ChatHeader />
    <div
      v-if="data"
      class="mx-auto w-xl grow overflow-y-auto lg:w-2xl xl:w-3xl"
    >
      <ChatMessage :is-sender="true">
        {{ text }}
      </ChatMessage>
      <ChatMessage :is-sender="false">
        <p v-if="isLoading">...</p>
        <template v-else>
          <MDC :value="data" class="max-w-lg font-sans text-base text-wrap" />
        </template>
      </ChatMessage>
    </div>
    <div v-else-if="thinking" class="grow">Thinking...</div>
    <div
      v-else
      class="flex w-full grow items-center justify-center overflow-y-auto sm:px-16 lg:px-32 2xl:px-[500px]"
    >
      <p>Hello, Dino Kupinic</p>
    </div>
    <ChatInput />
    <p class="py-1 text-center text-sm text-neutral-500">
      The AI can make mistakes. Verify important information.
    </p>
  </div>
</template>

<script setup lang="ts">
import type { Model } from "~/types/model"

const input = ref<string>("")
const text = ref<string>("")
const model = useState<Model>("model")
const thinking = ref<boolean>(false)

const { data, isLoading, fetchStream } = useStream()

const sendMessage = async () => {
  text.value = input.value
  input.value = ""
  thinking.value = true
  if (text.value.trim() && !isLoading.value) {
    await fetchStream(text.value, model.value)
  }
  thinking.value = false
}
</script>

<template>
  <div class="flex h-full flex-col">
    <ChatHeader />
    <div
      v-if="data"
      class="w-full grow overflow-y-auto sm:px-16 lg:px-32 2xl:px-[500px]"
    >
      <ChatMessage :is-sender="true">
        {{ text }}
      </ChatMessage>
      <ChatMessage :is-sender="false">
        <p v-if="isLoading">...</p>
        <template v-else>
          <pre class="max-w-lg text-wrap font-sans text-base">
            {{ data }}
          </pre>
        </template>
      </ChatMessage>
    </div>
    <div v-else-if="thinking">Thinking...</div>
    <div
      v-else
      class="flex w-full grow items-center justify-center overflow-y-auto sm:px-16 lg:px-32 2xl:px-[500px]"
    >
      <p>Hello, Dino Kupinic</p>
    </div>
    <div class="flex items-end p-4 sm:px-16 lg:px-32 2xl:px-[500px]">
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
        @keyup.enter="sendMessage"
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

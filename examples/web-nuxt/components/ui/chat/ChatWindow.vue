<script setup lang="ts">
import type { Model } from "~/types/model"

const input = ref<string>("")

const config = useRuntimeConfig()
const model = useState<Model>("model")
const data = ref("")
const isLoading = ref(false)

const fetchStream = async () => {
  isLoading.value = true
  data.value = ""

  try {
    const response = await $fetch("/message", {
      method: "POST",
      body: JSON.stringify({
        prompt: input.value,
        model: model.value.name,
      }),
      baseURL: config.public.API_URL,
    })

    if (response instanceof ReadableStream) {
      const reader = response.getReader()
      const decoder = new TextDecoder()

      while (true) {
        const { done, value } = await reader.read()
        if (done) break
        const chunk = decoder.decode(value)
        data.value += chunk
      }
    } else {
      if (typeof response === "string") {
        data.value = response
      } else {
        console.error("Unexpected response type")
      }
    }
  } catch (error) {
    console.error("Error fetching stream:", error)
  } finally {
    isLoading.value = false
  }
}

const sendMessage = () => {
  if (input.value.trim() && !isLoading.value) {
    fetchStream()
  }
}
</script>

<template>
  <div class="flex h-full flex-col">
    <ChatHeader />
    <div class="w-full grow overflow-y-auto sm:px-16 lg:px-32 2xl:px-[500px]">
      <ChatMessage :is-sender="true">
        {{ input }}
      </ChatMessage>
      <ChatMessage :is-sender="false">
        {{ data }}
      </ChatMessage>
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

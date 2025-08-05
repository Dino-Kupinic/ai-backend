<script setup lang="ts">
import type { SelectMenuItem } from "@nuxt/ui"

const config = useRuntimeConfig()

const { data } = await useFetch<{
  text_models: string[]
  image_models: string[]
}>("/model", {
  baseURL: config.public.API_URL,
})

if (!data.value) {
  throw createError({ status: 404, message: "No models found" })
}

const capitalizeFirstLetter = (str: string) =>
  str.charAt(0).toUpperCase() + str.slice(1)

const models = ref([
  ...data.value.text_models.map((model) => ({
    value: model,
    label: capitalizeFirstLetter(model),
    icon: "i-heroicons-chat-bubble-left-right-16-solid",
  })),
  ...data.value.image_models.map((model) => ({
    value: model,
    label: capitalizeFirstLetter(model),
    icon: "i-heroicons-photo-16-solid",
  })),
] satisfies SelectMenuItem[])

const selected = useState("model", () => models.value[0])
</script>

<template>
  <header
    class="flex w-full justify-between border-b border-neutral-200 p-2 px-4 dark:border-neutral-800"
  >
    <USelectMenu
      v-model="selected"
      :icon="selected?.icon"
      :items="models"
      size="sm"
      class="w-44"
    />
    <div class="space-x-2">
      <UButton
        icon="i-heroicons-pencil-square"
        size="sm"
        color="neutral"
        variant="outline"
        label="New Chat"
      />
    </div>
  </header>
</template>

<script setup lang="ts">
import type { Model } from "~/types/model"

const config = useRuntimeConfig()

// Manual type
type ModelResponse = {
  text_models: string[]
  image_models: string[]
}

const { data } = await useFetch<ModelResponse>("/model", {
  baseURL: config.public.API_URL,
})

if (!data.value) {
  throw createError({ status: 404, message: "No models found" })
}

const models = [
  ...data.value.text_models.map((model) => ({
    name: model,
    type: "text",
  })),
  ...data.value.image_models.map((model) => ({
    name: model,
    type: "image",
  })),
]

const selected = useState<Model>("model", () => models[0])
</script>

<template>
  <header
    class="flex w-full justify-between border-b border-neutral-200 p-2 px-4 dark:border-neutral-800"
  >
    <USelectMenu
      v-model="selected"
      :options="models"
      class="w-44"
      option-attribute="name"
    >
      <template #label>
        <Icon
          :name="
            selected.type === 'text'
              ? 'i-heroicons-chat-bubble-left-right-16-solid'
              : 'i-heroicons-photo-16-solid'
          "
        />
        <span class="truncate">{{ selected.name }}</span>
      </template>

      <template #option="{ option: model }">
        <Icon
          :name="
            model.type === 'text'
              ? 'i-heroicons-chat-bubble-left-right-16-solid'
              : 'i-heroicons-photo-16-solid'
          "
        />
        <span class="truncate">{{ model.name }}</span>
      </template>
    </USelectMenu>
    <div class="space-x-2">
      <UButton
        icon="i-heroicons-information-circle"
        size="sm"
        color="gray"
        square
        variant="solid"
      />
      <UButton
        icon="i-heroicons-pencil-square"
        size="sm"
        color="gray"
        square
        variant="solid"
      />
    </div>
  </header>
</template>

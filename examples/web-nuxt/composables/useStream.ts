import type { Model } from "~/types/model"

export function useStream() {
  const config = useRuntimeConfig()
  const data = ref<string>("")
  const isLoading = ref(false)

  const fetchStream = async (input: string, model: Model) => {
    isLoading.value = true
    data.value = ""

    try {
      const response = await $fetch("/message", {
        method: "POST",
        body: JSON.stringify({
          prompt: input,
          model: model.name,
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

  return {
    data,
    isLoading,
    fetchStream,
  }
}

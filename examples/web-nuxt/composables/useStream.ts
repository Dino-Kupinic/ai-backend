export function useStream() {
  const config = useRuntimeConfig()
  const data = ref<string>("")
  const isLoading = ref(false)

  const fetchStream = async (input: string, model: string) => {
    isLoading.value = true
    data.value = ""

    try {
      const response = await $fetch("/message", {
        method: "POST",
        body: JSON.stringify({
          prompt: input,
          model: model,
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
          throw createError({
            status: 500,
            message: "Unexpected response type",
          })
        }
      }
    } catch (error) {
      const err = error as Error
      throw createError({
        status: 500,
        message: err.message,
      })
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

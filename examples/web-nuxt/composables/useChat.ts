export function useChat() {
  const input = ref<string>("")
  const text = ref<string>("")
  const model = useState("model")
  const thinking = ref<boolean>(false)

  const { data, isLoading, fetchStream } = useStream()

  const sendMessage = async () => {
    text.value = input.value
    input.value = ""
    thinking.value = true
    if (text.value.trim() && !isLoading.value) {
      await fetchStream(text.value, model.value.value)
    }
    thinking.value = false
    console.log(data.value)
  }

  return {
    input,
    text,
    model,
    thinking,
    data,
    isLoading,
    sendMessage,
  }
}

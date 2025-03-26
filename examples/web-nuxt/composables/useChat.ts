export function useChat() {
  const input = useState<string>("input")
  const text = useState<string>("text")
  const model = useState<{
    value: string
    label: string
    icon: string
  }>("model")
  const thinking = useState<boolean>("thinking", () => false)

  const { data, isLoading, fetchStream } = useStream()

  async function sendMessage() {
    text.value = input.value
    input.value = ""
    thinking.value = true
    if (text.value.trim() && !isLoading.value) {
      await fetchStream(text.value, model.value.value)
    }
    thinking.value = false
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

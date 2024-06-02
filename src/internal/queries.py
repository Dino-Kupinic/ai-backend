import ollama
from fastapi import HTTPException


def query(msg: str, model: str = "llama3"):
    try:
        messages = [
            {
                "role": "user",
                "content": msg,
            },
        ]
        for chunk in ollama.chat(
            model,
            messages=messages,
            stream=True,
        ):
            yield chunk["message"]["content"]

    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Unexpected error")

import ollama
from fastapi import HTTPException


def query(msg: str):
    try:
        response = ollama.chat(model="llama3", messages=[
            {
                'role': 'user',
                'content': msg,
            },
        ])

        return response['message']['content']
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Unexpected error")

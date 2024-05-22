import ollama
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from routers import message


class Message(BaseModel):
    text: str


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


app = FastAPI(
    title="AI Backend",
    description="ai backend for your app powered by llama3",
    version="0.1.0"
)
app.include_router(message.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

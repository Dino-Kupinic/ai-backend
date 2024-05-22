import ollama
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Message(BaseModel):
    msg: str


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


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/message")
def message(msg: Message):
    response = query(msg.msg)
    return {"data": response}


if __name__ == "__main__":
    test_message = Message(msg="What is the capital of USA?")
    print(query(test_message.msg))

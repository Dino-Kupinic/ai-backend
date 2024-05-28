from fastapi import FastAPI

from src.routers import message

app = FastAPI(
    title="AI Backend",
    description="ai backend for your app powered by llama3",
    version="0.1.0"
)
app.include_router(message.router)

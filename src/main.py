from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers import message, image

app = FastAPI(
    title="AI Backend",
    description="ai backend for your app powered by llama3",
    version="0.1.6",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(message.router)
app.include_router(image.router)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.api.src.routers import message, image, model, health

app = FastAPI(
    title="AI Backend",
    description="ai backend for your app powered by llama3",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(message.router)
app.include_router(image.router)
app.include_router(model.router)

from fastapi import APIRouter

from src.internal.queries import query
from src.types.requests import Message

router = APIRouter(prefix="/message", tags=["message"])


@router.post("/")
async def send_message(message: Message):
    response = query(message.text)
    return {"data": response}

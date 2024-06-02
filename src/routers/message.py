from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from src.internal.queries import query
from src.types.requests import Message

router = APIRouter(prefix="/message", tags=["message"])


@router.post("/")
async def send_message(message: Message):
    return StreamingResponse(query(message.text))

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from apps.api.src.internal.query import TextQuery
from apps.api.src.types.requests import Message
from apps.api.src.internal.models import TextModel

router = APIRouter(prefix="/message", tags=["message"])

text_query = TextQuery()


@router.post("/")
async def send_message(message: Message):
    try:
        if isinstance(message.model, TextModel):
            model = message.model
        elif isinstance(message.model, str):
            model = message.model
        else:
            raise HTTPException(status_code=400, detail="Invalid model type")

        return StreamingResponse(
            text_query.query(prompt=message.prompt, model=model),
            media_type="text/plain",
        )
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

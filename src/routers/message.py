from fastapi import APIRouter

router = APIRouter(prefix="/message", tags=["message"])


@router.post("/", )
async def sendMessage(message: str):
    response = query(message.text)
    return {"data": response}

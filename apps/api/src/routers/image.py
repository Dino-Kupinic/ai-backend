from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from apps.api.src.internal.models import ImageModel
from apps.api.src.internal.query import ImageQuery
from apps.api.src.types.requests import Image

router = APIRouter(prefix="/image", tags=["image"])

image_query = ImageQuery()


@router.post("/")
async def send_message(image: Image):
    try:
        if isinstance(image.model, ImageModel):
            model = image.model
        elif isinstance(image.model, str):
            model = image.model
        else:
            raise HTTPException(status_code=400, detail="Invalid model type")

        return StreamingResponse(
            image_query.query(prompt=image.prompt, model=model, images=image.images),
            media_type="text/plain",
        )
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

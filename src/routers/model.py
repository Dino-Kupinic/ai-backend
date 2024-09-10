from fastapi import APIRouter

from src.internal.models import TextModel, ImageModel

router = APIRouter(prefix="/model", tags=["model"])


@router.get("/")
async def available_models():
    """
    Endpoint to return all available models
    """
    text_models = [model.value for model in TextModel]
    image_models = [model.value for model in ImageModel]

    return {"text_models": text_models, "image_models": image_models}

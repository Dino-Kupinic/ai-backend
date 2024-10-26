from pydantic import BaseModel

from src.internal.models import TextModel, ImageModel


class Message(BaseModel):
    """
    Request body for sending a message to a model
    """

    prompt: str
    model: TextModel


class Image(BaseModel):
    """
    Request body for sending an image to a model
    """

    prompt: str
    model: ImageModel
    images: list[str]

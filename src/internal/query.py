from abc import ABC, abstractmethod
from typing import overload, Any, Union

import ollama
from fastapi import HTTPException

from src.internal.models import TextModel, ImageModel
from src.types.alias import LLMResponse


class Query(ABC):
    """
    Abstract class for querying a model
    """

    @abstractmethod
    def query(self, prompt: str, model: Any, **kwargs) -> LLMResponse:
        """
        Query the model with the given prompt
        :param prompt: The prompt to query the model with
        :param model: The model to query
        :return: A generator of the model's responses
        """
        pass


class TextQuery(Query):
    """
    Query a text model
    """

    @overload
    def query(self, prompt: str, model: TextModel, **kwargs) -> LLMResponse: ...

    @overload
    def query(self, prompt: str, model: str, **kwargs) -> LLMResponse: ...

    def query(self, prompt: str, model: Union[TextModel, str], **kwargs) -> LLMResponse:
        """
        Query the model with the given prompt
        :param prompt: The prompt to query the model with
        :param model: The model to query (TextModel instance or string)
        :return: A generator of the model's responses
        """
        try:
            model_name = model.value if isinstance(model, TextModel) else model
            messages = [{"role": "user", "content": prompt}]
            yield from self._text_llm_call(model_name, messages)
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise HTTPException(
                status_code=500, detail=f"Internal Server Error: {str(e)}"
            )

    @staticmethod
    def _text_llm_call(model: str, messages: list) -> LLMResponse:
        for chunk in ollama.chat(
            model,
            messages=messages,
            stream=True,
        ):
            yield chunk["message"]["content"]


class ImageQuery(Query):
    """
    Query an image model
    """

    @overload
    def query(self, prompt: str, model: ImageModel, **kwargs) -> LLMResponse: ...

    @overload
    def query(self, prompt: str, model: str, **kwargs) -> LLMResponse: ...

    def query(
        self, prompt: str, model: Union[ImageModel, str], **kwargs
    ) -> LLMResponse:
        """
        Query the model with the given prompt and images
        :param prompt: The prompt to query the model with
        :param model: The model to query (ImageModel instance)
        :return: A generator of the model's responses
        """
        try:
            images = kwargs.get("images", [])
            if not images:
                raise ValueError("Images must be provided for an image query.")

            model_name = model.value if isinstance(model, ImageModel) else model
            messages = [{"role": "user", "content": prompt, "images": images}]
            yield from self._image_llm_call(model_name, messages)
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise HTTPException(
                status_code=500, detail=f"Internal Server Error: {str(e)}"
            )

    @staticmethod
    def _image_llm_call(model: str, messages: list) -> LLMResponse:
        for chunk in ollama.chat(
            model,
            messages=messages,
            stream=True,
        ):
            yield chunk["message"]["content"]

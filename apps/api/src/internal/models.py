from enum import Enum


class TextModel(Enum):
    """
    Enum for text models.
    """

    LLAMA3 = "llama3"
    LLAMA3_1 = "llama3.1"
    GEMMA2 = "gemma2"
    GEMMA3 = "gemma3"
    DEEPSEEK_R1 = "deepseek-r1"


class ImageModel(Enum):
    """
    Enum for image models.
    """

    LLAVA = "llava"

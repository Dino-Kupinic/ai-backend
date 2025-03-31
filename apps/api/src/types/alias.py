from typing import TypeAlias, Generator

LLMResponse: TypeAlias = Generator[str, None, None]

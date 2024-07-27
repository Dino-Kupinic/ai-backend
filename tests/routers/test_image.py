import json
from dataclasses import dataclass

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


@dataclass
class ImagePrompt:
    prompt: str
    model: str
    images: list[str]
    answers: list[str]


def read_json_file(file_path: str) -> list[ImagePrompt]:
    with open(file_path, "r") as f:
        data: list[dict] = json.load(f)

    return [ImagePrompt(**item) for item in data]


def test_image_llava():
    file_path = "../assets/test_images_base64.json"
    image_prompts = read_json_file(file_path)

    for prompt in image_prompts:
        response = client.post(
            "/image",
            json={
                "prompt": prompt.prompt,
                "model": prompt.model,
                "images": prompt.images,
            },
        )
        assert response.status_code == 200

        stream = response.text

        assert any(
            answer.lower() in stream.lower() for answer in prompt.answers
        ), f"None of the expected answers {prompt.answers} were found in the response"

        found_answers = [
            answer for answer in prompt.answers if answer.lower() in stream.lower()
        ]
        print(f"Found answers: {found_answers}")

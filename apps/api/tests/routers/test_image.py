import json
from dataclasses import dataclass
import os
import pytest

from fastapi.testclient import TestClient
from apps.api.src.main import app

client = TestClient(app)


@dataclass
class ImagePrompt:
    prompt: str
    model: str
    images: list[str]
    answers: list[str]


def read_json_file(file_path: str) -> list[ImagePrompt]:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "..", "assets", file_path)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, "r") as f:
        data: list[dict] = json.load(f)

    for item in data:
        item["images"] = [
            os.path.join(current_dir, "..", "assets", img_path)
            for img_path in item["images"]
        ]

    return [ImagePrompt(**item) for item in data]


# TODO: Improve and add more test cases


def test_image_llava():
    try:
        image_prompts = read_json_file("test_images.json")
    except FileNotFoundError as e:
        pytest.fail(f"Failed to load test file: {e}")

    # temporary fix for multiple image prompts
    prompt = image_prompts[0]

    response = client.post(
        "/image",
        json={
            "prompt": prompt.prompt,
            "model": prompt.model,
            "images": prompt.images,
        },
    )
    assert response.status_code == 200

    stream = ""
    for chunk in response.iter_text():
        stream += chunk

    included_answers = [answer in stream for answer in prompt.answers]

    assert included_answers != []


def test_image_llava_base64():
    try:
        image_prompts = read_json_file("test_images_base64.json")
    except FileNotFoundError as e:
        pytest.fail(f"Failed to load test file: {e}")

    # temporary fix for multiple image prompts
    prompt = image_prompts[0]

    response = client.post(
        "/image",
        json={
            "prompt": prompt.prompt,
            "model": prompt.model,
            "images": prompt.images,
        },
    )
    assert response.status_code == 200

    stream = ""
    for chunk in response.iter_text():
        stream += chunk

    included_answers = [answer in stream for answer in prompt.answers]

    assert included_answers != []

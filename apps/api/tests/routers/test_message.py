from fastapi.testclient import TestClient
from apps.api.src.main import app

client = TestClient(app)


def test_message_llama3():
    response = client.post(
        "/message", json={"prompt": "What is 1+1?", "model": "llama3"}
    )
    assert response.status_code == 200

    stream = ""
    for chunk in response.iter_text():
        stream += chunk

    assert "2" in stream

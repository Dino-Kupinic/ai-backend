from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_message():
    response = client.post("/message", json={"text": "What is 1+1?"})
    assert response.status_code == 200

    stream = ""
    for chunk in response.iter_text():
        stream += chunk

    assert "2" in stream

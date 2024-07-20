from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

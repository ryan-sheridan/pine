from fastapi.testclient import TestClient
from pine.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_root():
    response = client.get("/api/v1/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

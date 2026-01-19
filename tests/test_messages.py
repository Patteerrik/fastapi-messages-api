from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_protected_without_key_returns_401():
    res = client.get("/protected")
    assert res.status_code == 401


def test_protected_with_key_returns_200():
    res = client.get(
        "/protected",
        headers={"X-API-Key": "dev-secret"},
    )
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

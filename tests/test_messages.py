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


def test_create_message_persists(client) -> None:
    payload = {"text": "Hello test"}

    resp = client.post("/messages", json=payload)
    assert resp.status_code in (200, 201)

    data = resp.json()
    assert data["text"] == "Hello test"

    if "id" in data:
        assert isinstance(data["id"], int)

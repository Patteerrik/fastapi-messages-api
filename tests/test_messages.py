from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_message():
    response = client.post(
        "/messages/",
          json={"text": "Hello Test!"})
    
    assert response.status_code == 201
    data = response.json()
    assert data["text"] == "Hello Test!"
    assert "id" in data
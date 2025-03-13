from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_page():
    response = client.get("/page/linkedin")
    assert response.status_code == 200
    assert "page_id" in response.json()

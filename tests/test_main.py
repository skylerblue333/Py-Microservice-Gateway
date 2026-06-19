from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_route():
    r = client.post("/api/v1/route", json={"path": "users/1", "token": "valid-token"})
    assert r.status_code == 200
    assert r.json()["routed_to"] == "internal-users"
    
    r2 = client.post("/api/v1/route", json={"path": "users/1", "token": "bad"})
    assert r2.status_code == 401


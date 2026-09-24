from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_create_item_valid():
    payload = {
        "title": "Test Product",
        "description": "Sample description for testing",
        "value": 100.0
    }
    response = client.post("/items/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["calculation_results"]["base_value"] == 100.0
    assert data["calculation_results"]["calculated_tax"] == 20.0
    assert data["calculation_results"]["total_cost"] == 120.0

def test_create_item_invalid_value():
    payload = {
        "title": "Invalid Product",
        "value": -10.0  # Некоректне значення (повинно бути більше 0)
    }
    response = client.post("/items/", json=payload)
    assert response.status_code == 422  # Очікувана помилка валідації Pydantic
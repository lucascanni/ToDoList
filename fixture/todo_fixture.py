import pytest

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def create_task():
    # Test creating a task
    response = client.post("/todo", json={
        "name":"Complete project proposal",
        "description":"Write and finalize project proposal document",
        "date":"2024-05-10",
        "priority":"High",
        "status":"In progress"
    })
    return response.json()

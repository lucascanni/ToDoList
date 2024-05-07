import pytest

from fastapi.testclient import TestClient
from fixture.todo_fixture import create_task
from main import app

client = TestClient(app)

@pytest.mark.parametrize("name, description, date, priority, status", [
    ("Complete project proposal", "Write and finalize project proposal document", "2024-05-10", "High", "In progress"),
    ("Complete project proposal", "Write and finalize project proposal document", "2024-05-10", "High", "In progress")
])
def test_bulk_create_task(name, description, date, priority, status):
    # Test creating a task
    response = client.post("/todo", json={
        "name":name,
        "description":description,
        "date":date,
        "priority":priority,
        "status":status
    })
    assert response.status_code == 201
    assert response.json()['name'] == name
    assert response.json()['description'] == description
    assert response.json()['date'] == date
    assert response.json()['priority'] == priority
    assert response.json()['status'] == status

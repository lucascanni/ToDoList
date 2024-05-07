import pytest

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_task():
    # Test creating a task
    response = client.post("/todo", json={
        "name":"Complete project proposal",
        "description":"Write and finalize project proposal document",
        "date":"2024-05-10",
        "priority":"High",
        "status":"In progress"
    })
    assert response.status_code == 201
    assert response.json()['name'] == "Complete project proposal"

def test_get_all_tasks():
    # Test getting all tasks
    response = client.get("/todo")
    assert response.status_code == 200

def test_get_task_by_id():
    # Test creating a task
    response = client.post("/todo", json={
        "name":"Complete project proposal",
        "description":"Write and finalize project proposal document",
        "date":"2024-05-10",
        "priority":"High",
        "status":"In progress"
    })
    assert response.status_code == 201
    assert response.json()['name'] == "Complete project proposal"
    # Test getting a task by id
    response = client.get("/todo/{}".format(response.json()['id']))
    assert response.status_code == 200
    assert response.json()['name'] == "Complete project proposal"

def test_update_task():
    # Test creating a task
    response = client.post("/todo", json={
        "name":"Complete project proposal",
        "description":"Write and finalize project proposal document",
        "date":"2024-05-10",
        "priority":"High",
        "status":"In progress"
    })
    assert response.status_code == 201
    assert response.json()['name'] == "Complete project proposal"
    # Test updating a task
    response = client.patch("/todo/{}".format(response.json()['id']), json={
        "name":"Complete project proposal",
        "description":"Write and finalize project proposal document",
        "date":"2024-05-10",
        "priority":"High",
        "status":"Completed"
    })
    assert response.status_code == 200
    assert response.json()['status'] == "Completed"

def test_delete_task():
    # Test creating a task
    response = client.post("/todo", json={
        "name":"Complete project proposal",
        "description":"Write and finalize project proposal document",
        "date":"2024-05-10",
        "priority":"High",
        "status":"In progress"
    })
    assert response.status_code == 201
    assert response.json()['name'] == "Complete project proposal"
    # Test deleting a task
    response = client.delete("/todo/{}".format(response.json()['id']))
    assert response.status_code == 200
    assert response.json()['name'] == "Complete project proposal"
    # Test getting a task by id
    response = client.get("/todo/{}".format(response.json()['id']))
    assert response.status_code == 404
    assert response.json()['detail'] == "Task not found"



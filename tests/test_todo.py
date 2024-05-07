import pytest

from fastapi.testclient import TestClient
from fixture.todo_fixture import create_task
from main import app


client = TestClient(app)

# tests found

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
    assert response.json()['description'] == "Write and finalize project proposal document" 
    assert response.json()['date'] == "2024-05-10"
    assert response.json()['priority'] == "High"
    assert response.json()['status'] == "In progress"

def test_create_task_fixture(create_task):
    # Test creating a task using fixture
    response = create_task
    assert response['name'] == "Complete project proposal"
    assert response['description'] == "Write and finalize project proposal document" 
    assert response['date'] == "2024-05-10"
    assert response['priority'] == "High"
    assert response['status'] == "In progress"

def test_get_all_tasks():
    # Test getting all tasks
    response = client.get("/todo")
    assert response.status_code == 200

def test_get_task_by_id(create_task):
    # Test creating a task
    response = create_task
    assert response['name'] == "Complete project proposal"
    # Test getting a task by id
    response = client.get("/todo/{}".format(response['id']))
    assert response.status_code == 200
    assert response.json()['name'] == "Complete project proposal"

def test_update_task(create_task):
    # Test creating a task
    response = create_task
    assert response['name'] == "Complete project proposal"
    assert response['status'] == "In progress"
    # Test updating a task
    response = client.patch("/todo/{}".format(response['id']), json={
        "name":"Complete project proposal",
        "description":"Write and finalize project proposal document",
        "date":"2024-05-10",
        "priority":"High",
        "status":"Completed"
    })
    assert response.status_code == 200
    assert response.json()['name'] == "Complete project proposal"
    assert response.json()['status'] == "Completed"

def test_delete_task(create_task):
    # Test creating a task
    response = create_task
    assert response['name'] == "Complete project proposal"
    # Test getting a task by id before deleting
    response = client.get("/todo/{}".format(response['id']))
    assert response.status_code == 200
    assert response.json()['name'] == "Complete project proposal"
    # Test deleting a task
    response = client.delete("/todo/{}".format(response.json()['id']))
    assert response.status_code == 200
    # Test getting a task by id after deleting
    response = client.get("/todo/{}".format(response.json()['id']))
    assert response.status_code == 404
    assert response.json()['detail'] == "Task not found"

# tests not found

def test_get_task_by_id_not_found():
    # Test getting a task by id that does not exist
    response = client.get("/todo/{}".format("123"))
    assert response.status_code == 404
    assert response.json()['detail'] == "Task not found"

def test_update_task_not_found():
    # Test updating a task that does not exist
    response = client.patch("/todo/{}".format("123"), json={
        "name":"Complete project proposal",
        "description":"Write and finalize project proposal document",
        "date":"2024-05-10",
        "priority":"High",
        "status":"Completed"
    })
    assert response.status_code == 404
    assert response.json()['detail'] == "Task not found"    

def test_delete_task_not_found():
    # Test deleting a task that does not exist
    response = client.delete("/todo/{}".format("123"))
    assert response.status_code == 404
    assert response.json()['detail'] == "Task not found"


import pytest

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_task():
    # Test creating a task
    response = client.post("/todo", json={
        "name"="Complete project proposal",
        "description"="Write and finalize project proposal document",
        "date"="2024-05-10",
        "priority"="High",
        "status"="In progress"
    })
    assert response.status_code == 201
    assert response.json()['name'] == "Complete project proposal"

def test_get_all_tasks():
    # Test getting all tasks
    response = client.get('/todo')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_task_by_id():
    # Create a task first to get its id
    response_create = client.post('/todo', json={
        "name"="Review meeting agenda",
        "description"="Review agenda for next team meeting",
        "date"="2024-05-08",
        "priority"="Medium",
        "status"="Pending"
    })
    task_id = response_create.json()['id']

    # Test getting a task by id
    response_get = client.get(f'/todo/{task_id}')
    assert response_get.status_code == 200
    assert response_get.json()['id'] == task_id

# def test_get_all_tasks():
#     # Test getting all tasks
#     response = client.get('/')
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)

# def test_get_task_by_id():
#     # Create a task first to get its id
#     response_create = client.post('/', json={
#         "name"="Review meeting agenda",
#         "description"="Review agenda for next team meeting",
#         "date"="2024-05-08",
#         "priority"="Medium",
#         "status"="Pending"
#     })
#     task_id = response_create.json()['id']

#     # Test getting a task by id
#     response_get = client.get(f'/{task_id}')
#     assert response_get.status_code == 200
#     assert response_get.json()['id'] == task_id

# def test_update_task():
#     # Create a task first to get its id
#     response_create = client.post('/', json={"name": "Task 3", "description": "Description for Task 3"})
#     task_id = response_create.json()['id']

#     # Test updating a task
#     response_update = client.patch(f'/{task_id}', json={"name": "Updated Task 3"})
#     assert response_update.status_code == 200
#     assert response_update.json()['name'] == "Updated Task 3"

# def test_delete_task():
#     # Create a task first to get its id
#     response_create = client.post('/', json={"name": "Task 4", "description": "Description for Task 4"})
#     task_id = response_create.json()['id']

#     # Test deleting a task
#     response_delete = client.delete(f'/{task_id}')
#     assert response_delete.status_code == 200
#     assert response_delete.json()['id'] == task_id
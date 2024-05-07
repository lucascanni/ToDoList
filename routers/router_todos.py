from fastapi import APIRouter, HTTPException, status
from classe.schemas_dto import Task, TaskCreate
import uuid
from typing import List
from database.firebase import db

router = APIRouter(
    prefix='/todo',
    tags=['todo']
)

@router.post('', response_model=Task, status_code=201)
async def create_task(task: TaskCreate):
    generatedId = str(uuid.uuid4())
    newTask = Task(id= generatedId, **task.model_dump())
    db.child("Tasks").child(generatedId).set(newTask.model_dump())
    return newTask

@router.get('', response_model=List[Task])
async def get_all_tasks():
    firebase_tasks = db.child("Tasks").get().val()
    if firebase_tasks is None:
        return []
    resultArray = [value for value in firebase_tasks.values()]
    return resultArray

@router.get('/{id}', response_model=Task)
async def get_task_by_id(id: str):
    data = db.child("Tasks").child(id).get().val()
    if data is None:
        raise HTTPException(status_code=404, detail="Task not found")
    else:
        return data

@router.patch('/{id}', response_model=Task)
async def update_task(id: str, task: TaskCreate):
    updatedTask = Task(id= id, **task.model_dump())
    data = db.child("Tasks").child(id).get().val()
    if data is None:
        raise HTTPException(status_code=404, detail="Task not found")
    else:
        return db.child("Tasks").child(id).update(updatedTask.model_dump())

@router.delete('/{id}', response_model=Task)
async def delete_task(id: str):
    deleteTask = db.child("Tasks").child(id).get().val()
    if deleteTask is None:
        raise HTTPException(status_code=404, detail="Task not found")
    else:
        db.child("Tasks").child(id).remove()
        return deleteTask
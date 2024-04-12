from fastapi import APIRouter, Depends, HTTPException, status
from classe.schemas_dto import Task, TaskCreate
import uuid
from typing import List

router = APIRouter(
    prefix='/todos',
    tags=['todos']
)
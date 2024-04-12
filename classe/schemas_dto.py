from pydantic import BaseModel

# Model Pydantic = Datatype
class Task(BaseModel):
    id: str
    name: str
    description: str
    date: str
    priority: str
    status: str

class TaskCreate(BaseModel):
    name: str
    description: str
    date: str
    priority: str
    status: str
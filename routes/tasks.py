from fastapi import APIRouter
from models import Task

router = APIRouter()

fake_tasks_db = []

@router.post("/")
def create_task(task: Task):
    fake_tasks_db.append(task)
    return {"message": "Task created", "task": task}

@router.get("/")
def get_tasks():
    return fake_tasks_db

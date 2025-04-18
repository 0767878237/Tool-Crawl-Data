from fastapi import APIRouter
from pydantic import BaseModel
from database.db import SessionLocal
from models.models import CrawlTask

router = APIRouter()

class TaskCreate(BaseModel):
    url_filter: str

# API để tạo task
@router.post("/tasks")
def create_task(task: TaskCreate):
    db = SessionLocal()
    new_task = CrawlTask(url_filter=task.url_filter, status="Pending")
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    db.close()
    return {"task_id": new_task.id, "status": new_task.status}

# API để liệt kê các task
@router.get("/tasks")
def list_tasks():
    db = SessionLocal()
    tasks = db.query(CrawlTask).all()
    db.close()
    return tasks

from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from api import tasks
from database.db import SessionLocal
from models.models import CrawlTask

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.include_router(tasks.router)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    db = SessionLocal()
    tasks_list = db.query(CrawlTask).all()
    db.close()
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks_list})

@app.post("/create-task")
async def create_task(request: Request, url_filter: str = Form(...)):
    db = SessionLocal()
    new_task = CrawlTask(url_filter=url_filter, status="Pending")
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    db.close()
    return {"task_id": new_task.id, "status": new_task.status}

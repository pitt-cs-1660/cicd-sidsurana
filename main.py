from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    title: str

tasks = []

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is running!"}

@app.get("/healthz")
def health_check():
    return {"status": "ok"}

@app.get("/api/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.post("/api/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {"message": "Task created", "task": task}

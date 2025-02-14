from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is running!"}

@app.get("/healthz")
def health_check():
    return {"status": "ok"}

tasks = []

@app.post("/api/tasks")
def create_task():
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "title": f"Task {task_id}"})
    return {"message": "Task created", "task_id": task_id}

@app.get("/api/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.put("/api/tasks/{task_id}")
def update_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = f"Task {task_id} (Updated)"
            return {"message": f"Task {task_id} updated"}
    return {"error": "Task not found"}

@app.delete("/api/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return {"message": f"Task {task_id} deleted"}

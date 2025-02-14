from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is running!"}

@app.get("/healthz")
def health_check():
    return {"status": "ok"}

@app.get("/api/tasks")
def get_tasks():
    return {"tasks": []}  # Placeholder for testing

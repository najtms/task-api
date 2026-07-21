from fastapi import FastAPI

app = FastAPI()

tasks = [
    {
        "id": 1,
        "title": "Task 0",
        "done": True
    },
    {
        "id": 2,
        "title": "Task 1",
        "done" : True
    },
    {
        "id": 3,
        "title": "Task 2",
        "done" : False
    }
]


@app.get("/")
async def root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/tasks")
async def get_tasks():
    return tasks

@app.get("/tasks/{id}")
async def get_task_by_id(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
    return {"error": f"Task {id} not found"}
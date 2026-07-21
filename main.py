from fastapi import FastAPI, Request, HTTPException
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

@app.post("/tasks", status_code=201)
async def create_task(req: Request):

    try:
        task = await req.json()
    except:
        raise HTTPException(
            status_code=400,
            detail="Invalid JSON"
        )

    if "title" not in task:
        raise HTTPException(
            status_code=400,
            detail="Title is required"
        )

    if task["title"].strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    new_task = {
        "id": len(tasks) + 1,
        "title": task["title"],
        "done": False
    }

    tasks.append(new_task)

    return new_task
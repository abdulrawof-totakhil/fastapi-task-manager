from fastapi import FastAPI
from routes.auth import router as auth_router
from routes.tasks import router as task_router

app = FastAPI(title="FastAPI Task Manager")

app.include_router(auth_router, prefix="/auth")
app.include_router(task_router, prefix="/tasks")

@app.get("/")
def root():
    return {"message": "Task Manager API"}

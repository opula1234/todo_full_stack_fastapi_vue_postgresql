from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import models, database

app = FastAPI(title="My Fullstack API")

# Enable CORS so your Vue.js frontend can talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Vite default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Automatically create the tables in PostgreSQL on startup
models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def health_check():
    return {"status": "Backend is running on WSL!"}

# CREATE a new task
@app.post("/tasks")
def create_task(title: str, description: str = None, db: Session = Depends(database.get_db)):
    new_task = models.Task(title=title, description=description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# READ all tasks
@app.get("/tasks")
def get_all_tasks(db: Session = Depends(database.get_db)):
    return db.query(models.Task).all()

# DELETE a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(database.get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_status=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}
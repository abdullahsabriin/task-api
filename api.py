from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()

# --- Database setup ---
DATABASE_URL = "sqlite:///./tasks.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# --- Model ---
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)

Base.metadata.create_all(bind=engine)

# --- Routes ---
@app.get("/")
def home():
    return {"message": "API working"}

@app.get("/tasks")
def get_tasks():
    db = SessionLocal()
    try:
        tasks = db.query(Task).order_by(Task.id.desc()).all()
        return {
    "count": len(tasks),
    "tasks": [{"id": t.id, "title": t.title} for t in tasks]
}
    finally:
        db.close()

@app.post("/tasks")
def add_task(title: str):
    db = SessionLocal()
    try:
	if title.strip() == "":
    		return {"error": "Title cannot be empty"}~
        new_task = Task(title=title)
        db.add(new_task)
        db.commit()
        return {"id": new_task.id, "title": new_task.title}
    finally:
        db.close()

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    db = SessionLocal()
    try:
        task = db.query(Task).filter(Task.id == task_id).first()

        if task:
            db.delete(task)
            db.commit()
            return {"message": "Deleted"}

        return {"error": "Not found"}
    finally:
        db.close()

# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud 
from database import engine, SessionLocal, Base
from fastapi.middleware.cors import CORSMiddleware
import os

DATABASE_URL = os.getenv("DATABASE_URL")

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS settings
origins = [
    "https://dave7103.github.io",  # Make sure your frontend domain is listed
]

# CORS (for React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Replace with frontend URL in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/todos", response_model=list[schemas.TodoInDB])
def read_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)

@app.get("/todos/{todo_id}", response_model=schemas.TodoInDB)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return todo

@app.get("/todos/filter/{completed}", response_model=list[schemas.TodoInDB])
def filter_todo(completed: bool, db: Session = Depends(get_db)):
    return crud.filter_todos(db, completed)

@app.post("/todos", response_model=schemas.TodoInDB)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)

@app.put("/todos/{todo_id}", response_model=schemas.TodoInDB)
def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    return crud.update_todo(db, todo_id, todo)

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    crud.delete_todo(db, todo_id)
    return {"detail": "ToDo deleted"}

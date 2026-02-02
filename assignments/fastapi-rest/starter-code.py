from typing import Optional, List
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Todo API - Starter")

class Todo(BaseModel):
    id: Optional[int] = None
    title: str
    completed: bool = False

# simple in-memory storage
db: List[Todo] = []
next_id = 1

@app.post("/todos", status_code=status.HTTP_201_CREATED, response_model=Todo)
def create_todo(todo: Todo):
    global next_id
    todo.id = next_id
    next_id += 1
    db.append(todo)
    return todo

@app.get("/todos", response_model=List[Todo])
def list_todos():
    return db

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for t in db:
        if t.id == todo_id:
            return t
    raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated: Todo):
    for i, t in enumerate(db):
        if t.id == todo_id:
            updated.id = todo_id
            db[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int):
    for i, t in enumerate(db):
        if t.id == todo_id:
            db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Todo not found")

# Run with: uvicorn starter-code:app --reload

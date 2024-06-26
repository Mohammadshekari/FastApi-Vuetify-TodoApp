from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class TodoItem(BaseModel):
    id: int
    title: str
    completed: bool


# In-memory storage for todo items
todo_items: List[TodoItem] = []


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/add")
async def add_todo_item(item: TodoItem):
    todo_items.append(item)
    return {"message": "Todo item added successfully"}


@app.post("/delete")
async def delete_todo_item(item_id: int):
    global todo_items
    todo_items = [item for item in todo_items if item.id != item_id]
    return {"message": "Todo item deleted successfully"}


@app.post("/complete")
async def complete_todo_item(item_id: int):
    for item in todo_items:
        if item.id == item_id:
            item.completed = True
            break
    return {"message": "Todo item marked as completed"}

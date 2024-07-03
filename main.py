import datetime
from enum import Enum

from fastapi import FastAPI, Request, Body, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class TodoLevel(Enum):
    critical = 'critical'
    normal = 'normal'
    low = 'low'


class TodoAction(Enum):
    delete = 'delete'
    complete = 'complete'
    not_completed = 'not_completed'


class TodoItem(BaseModel):
    id: int
    title: str
    person: str
    description: str
    completed: bool
    level: TodoLevel
    date: datetime.date


# In-memory storage for todo items
todo_items: List[TodoItem] = []

# Add 5 example todo items to the list
todo_items.append(
    TodoItem(id=1, title="Fix server bug", person="Alice", description="Fix the critical bug in the server code",
             completed=True, level=TodoLevel.critical, date=datetime.date(2024, 7, 1)))

todo_items.append(
    TodoItem(id=2, title="Write documentation", person="Bob", description="Write documentation for the new API",
             completed=False, level=TodoLevel.normal, date=datetime.date(2024, 7, 2)))

todo_items.append(TodoItem(id=3, title="Team meeting", person="Carol",
                           description="Attend the team meeting to discuss project status", completed=False,
                           level=TodoLevel.low,
                           date=datetime.date(2024, 7, 3)))

todo_items.append(
    TodoItem(id=4, title="Code review", person="Dave", description="Review the code submitted by the team",
             completed=True, level=TodoLevel.normal, date=datetime.date(2024, 7, 4)))

todo_items.append(TodoItem(id=5, title="Deploy to production", person="Eve",
                           description="Deploy the new release to production environment", completed=True,
                           level=TodoLevel.critical,
                           date=datetime.date(2024, 7, 5)))


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/list")
async def get_todos():
    return todo_items


@app.post("/add")
async def add_todo_item(item: TodoItem):
    item.id = todo_items[-1].id + 1
    todo_items.append(item)
    return item


@app.delete("/delete/{item_id}")
async def delete_todo_item(item_id: int):
    global todo_items
    todo_items = [item for item in todo_items if item.id != item_id]
    return {"message": "Todo item deleted successfully"}


@app.post("/complete/{item_id}")
async def complete_todo_item(item_id: int):
    for item in todo_items:
        if item.id == item_id:
            item.completed = True
            break
    return {"message": "Todo item marked as completed"}


@app.post("/plural")
async def complete_todo_item(ids: List[int] = Body(...), action: TodoAction = Body()):
    global todo_items
    if action == TodoAction.delete:
        todo_items = [item for item in todo_items if item.id not in ids]
        print(todo_items)
    else:
        for index, todo in enumerate(todo_items):
            if todo_items[index].id in ids:
                todo_items[index].completed = action == TodoAction.complete
    return todo_items

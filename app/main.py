from typing import List
from fastapi import FastAPI

from schemas.todo_item_schema import TodoItem
from routers import todo_router

app = FastAPI()
app.include_router(todo_router.router)
from typing import List
from fastapi import FastAPI

from schemas.todo_item_schema import TodoItem

app = FastAPI()

todos: List[TodoItem] = []

@app.get('/')
async def get_all_todos():
    return {'todos': todos}

@app.post('/', status_code=201)
async def create_todo(data: TodoItem):
    todos.append(data)
    return {'todo_item': data}

@app.get('/{todo_id}')
async def get_todo_item(todo_id: int):
    for item in todos:
        if item.id == todo_id:
            return {'todo_item': item}
    return {'msg': 'todo not found.'}
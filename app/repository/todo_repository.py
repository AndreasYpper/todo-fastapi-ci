from typing import List
from schemas.todo_item_schema import TodoItem

todos: List[TodoItem] = []


async def get_all() -> List[TodoItem]:
    return todos


async def get(todo_id: int) -> TodoItem:
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return None


async def create(todo_item: TodoItem) -> TodoItem:
    todos.append(todo_item)
    return todo_item


async def update(todo_item: TodoItem) -> TodoItem:
    for todo in todos:
        if todo.id == todo_item.id:
            todos.remove(todo)

    todos.append(todo_item)
    return todo_item

async def delete(todo_id: int) -> TodoItem:
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return todo
    return None

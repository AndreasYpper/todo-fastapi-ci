from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from schemas.todo_item_schema import TodoItemDto, TodoItemCreate
from models import TodoItem


async def get_all(db: Session) -> List[TodoItemDto]:
    todos = db.query(TodoItem).all()
    return todos


async def get(todo_id: int, db: Session) -> TodoItemDto:
    todo_item = db.query(TodoItem).filter(TodoItem.id == todo_id).first()

    if not todo_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo item with id {id} is not available.",
        )

    return todo_item


async def create(todo_item: TodoItemCreate, db: Session) -> TodoItemDto:
    new_todo = TodoItem(
        title=todo_item.title,
        body=todo_item.body,
        completed=todo_item.completed
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo


async def update(todo_item: TodoItemDto, db: Session) -> TodoItemDto:
    update_item = db.query(TodoItem).filter(TodoItem.id == todo_item.id).first()
    
    if not update_item:
        new_todo = TodoItem(
            id = todo_item.id,
            title = todo_item.title,
            body = todo_item.body,
            completed = todo_item.completed
        )

        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)

        return new_todo
    
    update_item.title = todo_item.title
    update_item.body = todo_item.body
    update_item.completed = todo_item.completed
    
    db.commit()
    db.refresh(update_item)
    
    return update_item

async def delete(todo_id: int, db: Session) -> TodoItemDto:
    delete_todo = db.query(TodoItem).filter(TodoItem.id == todo_id).first()

    if not delete_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo item with id {id} is not available.",
        )
    
    db.delete(delete_todo)
    db.commit()

    return {'msg': f'TodoItem with id {todo_id} was deleted successfully.'}

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from schemas.todo_item_schema import TodoItemDto, TodoItemCreate
from repository import todo_repository
from services.database import get_db

router = APIRouter(prefix='/todo', tags=['todo'])


@router.get('/', status_code=status.HTTP_200_OK)
async def get_all_todos(db: Session = Depends(get_db)):
    return await todo_repository.get_all(db)


@router.get('/{todo_id}', status_code=status.HTTP_200_OK)
async def get_todo(todo_id: int, db: Session = Depends(get_db)):
    return await todo_repository.get(todo_id, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_todo(todo_item: TodoItemCreate, db: Session = Depends(get_db)):
    return await todo_repository.create(todo_item, db)


@router.put('/', status_code=status.HTTP_202_ACCEPTED)
async def update_todo(todo_item: TodoItemDto, db: Session = Depends(get_db)):
    return await todo_repository.update(todo_item, db)


@router.delete('/{todo_id}', status_code=status.HTTP_202_ACCEPTED)
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    return await todo_repository.delete(todo_id, db)

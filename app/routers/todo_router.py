from fastapi import APIRouter, status

from schemas.todo_item_schema import TodoItem
from repository import todo_repository

router = APIRouter(prefix='/todo', tags=['todo'])


@router.get('/', status_code=status.HTTP_200_OK)
async def get_all_todos():
    todos = await todo_repository.get_all()

    return {'todos': todos}


@router.get('/{todo_id}', status_code=status.HTTP_200_OK)
async def get_todo(todo_id: int):
    todo = await todo_repository.get(todo_id)

    if todo is None:
        return {'msg': f'Todo item with id: {todo_id} was not found.'}
    return {'todo_item': todo}


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_todo(todo_item: TodoItem):
    created_todo = await todo_repository.create(todo_item)
    return {'todo_item': created_todo}


@router.put('/', status_code=status.HTTP_202_ACCEPTED)
async def update_todo(todo_item: TodoItem):
    update_todo = await todo_repository.update(todo_item)
    return {'todo_item': todo_item}


@router.delete('/{todo_id}', status_code=status.HTTP_202_ACCEPTED)
async def delete_todo(todo_id: int):
    todo = await todo_repository.delete(todo_id)

    if todo is None:
        return {'msg': f'Todo item with id: {todo_id} was not found.'}
    return {'deleted': todo}

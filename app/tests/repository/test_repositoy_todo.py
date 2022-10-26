from http.client import HTTPException
import pytest
import pytest_asyncio

from schemas.todo_item_schema import TodoItemCreate, TodoItemDto
from repository import todo_repository

@pytest.mark.asyncio
async def test_add_todo(async_client, db):
    todo = TodoItemCreate(
        title='test title',
        body='test body',
        completed=False
    )

    result = await todo_repository.create(todo, db)

    assert result.id == 1
    assert result.title == 'test title'
    assert result.body == 'test body'
    assert result.completed == False


@pytest.mark.asyncio
async def test_get_all(async_client, db):
    result = await todo_repository.get_all(db)

    assert result == []

@pytest.mark.asyncio
async def test_get_one(async_client, db):
    todo = TodoItemCreate(
        title='test title',
        body='test body',
        completed=False
    )

    result = await todo_repository.create(todo, db)

    assert result.id == 1
    assert result.title == 'test title'
    assert result.body == 'test body'
    assert result.completed == False

    get_result = await todo_repository.get(1, db)

    assert get_result.id == 1
    assert get_result.title == 'test title'
    assert get_result.body == 'test body'
    assert get_result.completed == False

# @pytest.mark.asyncio
# async def test_get_none_existing(async_client, db):
#     with pytest.raises(HTTPException) as exc_info:
#         await todo_repository.get(1, db)

#         assert isinstance(exc_info.value, HTTPException)
#         assert exc_info.value.status_code == 404
    # assert exc_info.value.detail == "Bucket Does Not Exist!"

    

@pytest.mark.asyncio
async def test_update_todo(async_client, db):
    todo = TodoItemCreate(
        title='test title',
        body='test body',
        completed=False
    )

    result = await todo_repository.create(todo, db)

    assert result.id == 1
    assert result.title == 'test title'
    assert result.body == 'test body'
    assert result.completed == False

    update_todo_item = TodoItemDto(
        id=1,
        title='test title',
        body='test body',
        completed=True
    )

    get_result = await todo_repository.update(update_todo_item, db)

    assert get_result.id == 1
    assert get_result.title == 'test title'
    assert get_result.body == 'test body'
    assert get_result.completed == True
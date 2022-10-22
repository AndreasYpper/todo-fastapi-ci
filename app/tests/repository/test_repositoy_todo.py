import pytest
import pytest_asyncio

from models import TodoItem
from schemas.todo_item_schema import TodoItemCreate
from repository import todo_repository
from tests.conftest import async_client

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


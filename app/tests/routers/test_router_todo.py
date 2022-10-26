from http.client import HTTPException
from urllib import response
import pytest
import pytest_asyncio

@pytest.mark.asyncio
async def test_get_all(async_client, db, mocker):
    mocker.patch('repository.todo_repository.get_all', return_value='hello')
    response = await async_client.get('/todo/')

    assert response.json() == 'hello'

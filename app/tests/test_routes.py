import pytest
from httpx import AsyncClient
from main import get_todo_item

from main import app
from schemas.todo_item_schema import TodoItem

@pytest.mark.asyncio
async def test_no_todos_when_get_all_todos_then_return_empty_list():
    async with AsyncClient(app=app, base_url='http://test') as client:
        response = await client.get('/')
    assert response.status_code == 200
    assert response.json() == {'todos': []}

@pytest.mark.asyncio
async def test_valid_todo_when_create_todo_then_return_201_and_created_todo_item():
    # Assign
    data = TodoItem(
        id=1,
        title='Test',
        body='Test body',
        completed=False
    )
    async with AsyncClient(app=app, base_url='http://test') as client:
        
        # Act
        response = await client.post('/', data=data.json())
    
    # Assert
    assert response.status_code == 201
    assert response.json() == {'todo_item': data}


@pytest.mark.asyncio
async def test_invalid_todo_when_create_todo_then_return_401():
    # Assign
    data = {
        'not': 'correct',
        'data': 'input'
    }

    async with AsyncClient(app=app, base_url='http://test') as client:
        # Act
        response = await client.post('/', data=data)

    # Assert
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_created_todo_when_get_all_todos_then_return_todo_in_list():
    # Assign
    expectedTodos = TodoItem(
        id=1,
        title='Test',
        body='Test body',
        completed=False
    )

    async with AsyncClient(app=app, base_url='http://test') as client:
        
        # Act
        response = await client.get('/')
    
    # Assert
    assert response.status_code == 200
    assert response.json() == {'todos': [expectedTodos]}

@pytest.mark.asyncio
async def test_valid_id_when_get_by_id_then_return_correct_todo():
    # Assign
    data = 1
    expectedTodo = TodoItem(
        id=1,
        title='Test',
        body='Test body',
        completed=False
    )

    async with AsyncClient(app=app, base_url='http://test') as client:
        # Act
        response = await client.get(f'/{data}')

    # Assert
    assert response.status_code == 200
    assert response.json() == {'todo_item': expectedTodo}
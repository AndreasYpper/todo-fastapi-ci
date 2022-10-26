from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import Session
from httpx import AsyncClient
import pytest_asyncio
import pytest

from services.database import Base, get_db
from main import app
from models import TodoItem

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"


@pytest.fixture(scope="session")
def db_engine():
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    if not database_exists:
        create_database(engine.url)

    Base.metadata.create_all(bind=engine)
    yield engine


@pytest.fixture(scope="function")
def db(db_engine):
    connection = db_engine.connect()

    # begin a non-ORM transaction
    connection.begin()

    # bind an individual Session to the connection
    db = Session(bind=connection, )
    # db = Session(db_engine)
    app.dependency_overrides[get_db] = lambda: db

    yield db

    db.rollback()
    connection.close()


@pytest_asyncio.fixture(scope="function")
async def async_client():
    app.dependency_overrides[get_db] = lambda: db
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client
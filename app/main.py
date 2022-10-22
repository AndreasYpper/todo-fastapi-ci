from fastapi import FastAPI

from routers import todo_router
from services.database import engine
from models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(todo_router.router)
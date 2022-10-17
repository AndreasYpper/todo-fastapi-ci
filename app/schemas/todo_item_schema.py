from pydantic import BaseModel

class TodoItem(BaseModel):
    id: int
    title: str
    body: str
    completed: bool
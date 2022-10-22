from pydantic import BaseModel

class TodoItemBase(BaseModel):
    title: str
    body: str
    completed: bool

class TodoItemCreate(TodoItemBase):
    pass

class TodoItemDto(TodoItemBase):
    id: int

    class Config:
        orm_mode = True
from sqlalchemy import Column, Integer, String, Boolean

from services.database import Base

class TodoItem(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    completed = Column(Boolean, default=False)
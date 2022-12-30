from pydantic import BaseModel
from typing import Union

class TodoModel(BaseModel):
    name: str
    description: str

class DeleteTodoModel(BaseModel):
    id: str

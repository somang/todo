from datetime import date
from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class TodoBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()


# this will be used to validate data while creating a Pod
class TodoCreate(TodoBase):
    title: str
    description: str


# this will be used to format the response to not to have id,owner_id etc
class ShowTodo(TodoBase):
    id: int
    title: str
    description: str    
    date_posted: date    

    class Config:  # to convert non dict obj to json
        orm_mode = True

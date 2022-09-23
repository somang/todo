from typing import List
from typing import Optional

from db.models.todo import Todo
from db.repository.todo_item import create_todo
from db.repository.todo_item import list_todos
from db.repository.todo_item import get_todo_by_id
from db.repository.todo_item import update_todo_item
from db.repository.todo_item import remove_todo
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from schemas.todo_item import TodoCreate
from schemas.todo_item import ShowTodo
from sqlalchemy.orm import Session

app = APIRouter()


@app.post("/todo/", response_model=ShowTodo)
async def post_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    response = await create_todo(todo=todo, db=db)
    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@app.get("/all", response_model=List[ShowTodo])
async def get_all_todo(db: Session = Depends(get_db)):
    response = await list_todos(db=db)
    return response
    

@app.put("/todo/{id}/")
async def update_todo(id: int, title: str, desc: str, todo: TodoCreate, db: Session = Depends(get_db)):
    response = await update_todo_item(id, title, desc, todo=todo, db=db)
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no todo with the id={id}"
        )
    return {"msg": "Successfully updated data."}


@app.get("/todo/{it}", response_model=ShowTodo)
async def get_todo_by_id(id:int, db: Session = Depends(get_db)):
    response = await get_todo_by_id(id=id, db=db)
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no todo with the id={id}"
        )
    return {"msg": "Successfully received data."}
    


@app.delete("/todo/{id}")
async def delete_todo(id:int, db: Session = Depends(get_db)):
    todo = get_todo_by_id(id=id, db=db)
    if not todo:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"There is no todo with the id={id}",
        )
    else:
        remove_todo(id=id, db=db)
        return {"detail": "Successfully deleted."}
    
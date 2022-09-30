from db.models.todo import Todo
from schemas.todo_item import TodoCreate
from sqlalchemy.orm import Session


async def create_todo(todo: TodoCreate, db: Session):
    todo_object = Todo(**todo.dict())
    db.add(todo_object)
    db.commit()
    db.refresh(todo_object)
    return todo_object
    

async def list_todos(db: Session):
    pods = db.query(Todo).filter(Todo.is_active == True).all()
    return pods


async def get_todo(id: int, db: Session):
    item = db.query(Todo).filter(Todo.id == id).first()
    return item


async def update_todo_item(id:int, title: str, desc: str, todo: TodoCreate, db: Session):
    existing_todo = db.query(Todo).filter(Todo.id == id)  # get the element first
    if not existing_todo.first():
        return False
    todo.__dict__.update(
        title=title,
        description=desc
    )  # update dictionary with new key value of owner_id
    existing_todo.update(todo.__dict__)
    db.commit()
    return True


async def remove_todo(id: int, db: Session):
    existing_item = db.query(Todo).filter(Todo.id == id)

    if not existing_item.first():
        return False
    existing_item.delete(synchronize_session=False)
    db.commit()
    return True
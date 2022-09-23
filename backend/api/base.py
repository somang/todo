from api import route_todo
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(route_todo.app, prefix="", tags=["todo"])

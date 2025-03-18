from fastapi import APIRouter

import crud
from app.users.schemas import CreateUser

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/")
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)
from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel
from typing import List

testApp = FastAPI()


class User(BaseModel):
    id: int
    username: str
    age: int


users: List[User] = [
    User(id=1, username="FirstUser", age=24)
]


@testApp.get('/users')
async def get_users():
    return users


@testApp.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
                      age: Annotated[int, Path(ge=18, le=120, title="user age", description="Enter age")]):
    new_id = max((t.id for t in users), default=0) + 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@testApp.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(description="Enter user id")],
                      username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
                      age: Annotated[int, Path(ge=18, le=120, title="user age", description="Enter age")]):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="Пользователь не найден")


@testApp.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(description="Enter user id")]):
    for i,user in enumerate(users):
        if user.id == user_id:
            del users[i]
            return user
    raise HTTPException(status_code=404, detail="Пользователь не найден")

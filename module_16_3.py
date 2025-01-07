from fastapi import FastAPI, Path
from typing import Annotated

testApp = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@testApp.get('/users')
async def get_users():
    return users


@testApp.post("/user/{username}/{age}")
async def new_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
               age: Annotated[int, Path(ge=18, le=120, title="user age", description="Enter age")]):
    new_id = int(list(users.keys())[-1]) + 1
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


@testApp.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(description="Enter user id")],
               username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
               age: Annotated[int, Path(ge=18, le=120, title="user age", description="Enter age")]):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@testApp.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(description="Enter user id")]):
    del users[user_id]
    return f"The user {user_id} is deleted"

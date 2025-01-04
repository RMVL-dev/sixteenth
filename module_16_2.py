from fastapi import FastAPI, Path
from typing import Annotated

testApp = FastAPI()


@testApp.get('/')
async def root():
    return {"Main page"}


@testApp.get('/user/admin')
async def user_admin():
    return "You are logged as administrator"


@testApp.get("/user/{user_id}")
async def user(user_id: Annotated[int, Path(ge=1, le=100, title="User ID", description="Enter User ID")]):
    return f"You are logged as user № {user_id}"


@testApp.get("/user/{username}/{age}")
async def user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")], age: Annotated[int, Path(ge=18, le=120,title="user age",description="Enter age")]):
    return f"Information about user. Username:{username} age:{age} "

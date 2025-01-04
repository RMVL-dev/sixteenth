from fastapi import FastAPI

testApp = FastAPI()


@testApp.get('/')
async def root():
    return {"Main page"}


@testApp.get('/user/admin')
async def user_admin():
    return "You are logged as administrator"


@testApp.get("/user/{user_id}")
async def user(user_id: int):
    return f"You are logged as user № {user_id}"


@testApp.get("/user/")
async def user(username: str, age: int) -> str:
    return f"Information about user. Username:{username} age:{age} "

from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/")
async def root():
    return "Главная страница"


@app.get("/users")
async def root_adm():
    return users


@app.post("/user/{username}/{age}")
async def root_us_param(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    keys_int = list(map(int, users.keys()))
    user_id = max(keys_int) + 1
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def root_us_param(
        user_id: Annotated[int, Path(ge=1, le=1000, description='Enter user_id', example='1')],
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    if user_id in list(map(int, users.keys())):
        users[str(user_id)] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} has been updated"
    else:
        return f"User {user_id} does not exist"


@app.delete("/user/{user_id}")
async def root_us(user_id: Annotated[int, Path(ge=1, le=1000, description='Enter User ID', example='1')]):
    if user_id in list(map(int, users.keys())):
        del users[str(user_id)]
        return f"User {user_id} has been deleted"
    else:
        return f"User {user_id} does not exist"

# python -m uvicorn 1.module_16_3:app --reload

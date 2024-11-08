from typing import Annotated
from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


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
    if users:
        user_id = users[-1].id + 1
    else:
        user_id = 1
    user = User(username=username, age=age, id=user_id)
    users.append(user)
    return users[-1]


@app.put("/user/{user_id}/{username}/{age}")
async def root_us_param(
        user_id: Annotated[int, Path(ge=0, le=1000, description='Enter user_id', example='1')],
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    try:
        is_in_list = False
        idx = None
        for i in range(len(users)):
            if users[i].id == user_id:
                users[i].username = username
                users[i].age = age
                is_in_list = True
                idx = i
                break
        if is_in_list:
            return users[idx]
        else:
            raise HTTPException(status_code=404, detail='User was not found')

    finally:
        pass


@app.delete("/user/{user_id}")
async def root_us(user_id: Annotated[int, Path(ge=0, le=1000, description='Enter User ID', example='1')]):
    try:
        is_in_list = False
        idx = None
        for i in range(len(users)):
            if users[i].id == user_id:
                idx = i
                is_in_list = True
                break
        if is_in_list:
            return users.pop(idx)
        else:
            raise HTTPException(status_code=404, detail='User was not found')
    finally:
        pass

# python -m uvicorn 1.module_16_4:app --reload

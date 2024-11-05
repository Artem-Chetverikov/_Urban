from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/")
async def root():
    return "Главная страница"


@app.get("/user/admin")
async def root_adm():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def root_us(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/{age}")
async def root_us_param(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

# python -m uvicorn 1.module_16_2:app --reload

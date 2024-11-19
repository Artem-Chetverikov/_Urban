from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "Главная страница"


@app.get("/user/admin")
async def root_adm():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def root_us(user_id):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def root_us_param(username, age):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

# python -m uvicorn 1.module_16_1:app --reload

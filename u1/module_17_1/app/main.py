import sys

sys.path.insert(0, './u1/module_17_1/app')

from fastapi import FastAPI
from routers import task, user

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router_task)
app.include_router(user.router_user)

# python -m uvicorn 1.module_17_1.app.main:app

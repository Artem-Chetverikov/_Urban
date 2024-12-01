import sys

sys.path.insert(0, './1/module_17_5/app')

from fastapi import FastAPI
from u1.module_17_5.app.routers import task, user

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router_task)
app.include_router(user.router_user)

# python -m uvicorn u1.module_17_5.app.main:app

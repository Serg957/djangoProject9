from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def homepage() -> str:
    return  "Главная страница"

@app.get("/user/admin")
async def news() ->dict:
    return {'message': f"Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_id(user_id : int) -> str:
    return f"Вы вошли как пользователь №{user_id}"

@app.get("/user")
async def id_paginator(username: str, age:int) -> str:
    return f"Информация о пользователе. Имя:{ username}, Возраст: {age}"

from fastapi import FastAPI,Path,status, Body, HTTPException
from pydantic import BaseModel
from typing import Annotated,List

app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get("/users")
def get_all_users() -> List[User]:
    return  users


@app.post("/user/{username}/{age}")
def created_user(
                 username: Annotated[str,  Path(min_length=5, max_length=20, description="Enter username", example= "UrbanUser")],
                 age:int= Path(ge=18, le=120, description="Enter age",example="67")) ->User:

    user_id =  max(users, key=lambda x :int(x.id)).id + 1 if users else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
def updated_user(user_id : Annotated[ int, Path(ge=1, le=100, description="Enter User ID",example="75")],
                       username: Annotated[str,  Path(min_length=5, max_length=20, description="Enter username", example= "UrbanUser")],
                       age:int= Path(ge=18, le=120, description="Enter age",example="67")
) -> User:

        for user in users:
            if user.id == user_id:
                user.username = username
                user.age = age
                return user
        raise HTTPException(status_code=404, detail="User not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id : Annotated[ int, Path(ge=1, le=100, description="Enter User ID",example="75")]
) ->User:
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user

    raise HTTPException(status_code=404, detail="User was not found")







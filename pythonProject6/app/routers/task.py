from fastapi import APIRouter,Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from app.models.user import User
from app.models.task import Task
from app.schemas import CreateTask, UpdateTask
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/")
async def get_all_tasks(db: Annotated[Session, Depends(get_db)]):
    get_all_tasks = db.scalars(select(Task)).all()
    return get_all_tasks


@router.get("/task_id")
async def get_task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalars(select(Task).where(Task.id == task_id))
    if task is not None:
        return task
    raise HTTPException()



@router.post("/create")
async def create_task(db: Annotated[Session, Depends(get_db)], user_id: int, create_task: CreateTask):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if user is not None:
        db.execute(insert(Task).values(title = create_task.title,
                                      content = create_task.content,
                                      user_id = user_id,
                                      slug= slugify(create_task.title)))
        db.commit()
        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'Successful'
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='User was not found'
    )


@router.put(" /update")
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, update_task: UpdateTask):
    task = db.scalars(select(Task).where(Task.id == task_id))

    if task is not None:
        db.execute(update(Task).where(Task.id == task_id).values(title = update_task.title,
                                                                 content = update_task.content,
                                                                 slug= slugify(update_task.title),
                                                                 priority =update_task.priority))
        db.commit()

        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'Successful'
            }
    raise HTTPException(status_code=404, detail='Task not found')

@router. delete("/delete")
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    delete_task = db.scalars(select(Task).where(Task.id == task_id))

    if delete_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')

    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'Successful'
            }
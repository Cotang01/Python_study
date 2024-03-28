"""
Необходимо создать API для управления списком задач. Каждая задача должна
содержать заголовок и описание. Для каждой задачи должна быть возможность
указать статус (выполнена/не выполнена).

API должен содержать следующие конечные точки:
— GET /tasks — возвращает список всех задач.
— GET /tasks/{id} — возвращает задачу с указанным идентификатором.
— POST /tasks — добавляет новую задачу.
— PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
— DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.

Для каждой конечной точки необходимо проводить валидацию данных запроса и
ответа. Для этого использовать библиотеку Pydantic.
"""
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


app = FastAPI()
templates = Jinja2Templates(directory="templates")


class Task(BaseModel):
    title: str
    content: str
    is_done: bool = False


all_tasks = {"1": Task(title="New Task", content="Some content", is_done=False)}


@app.get("/")
async def index():
    return {"Hello": "World"}


@app.get("/tasks")
async def tasks():
    return all_tasks


@app.get("/tasks/{tid}")
async def get_task_by_id(tid: int):
    return all_tasks.get(str(tid), None)


@app.post("/tasks")
async def add_task(task: Task):
    all_tasks[str(len(all_tasks) + 1)] = task
    return task


@app.put("/tasks/{tid}")
async def update_task_by_id(tid: int, task: Task):
    all_tasks[tid] = task
    return task


@app.delete("/tasks/{tid}")
async def delete_task_by_id(tid: int):
    removed_task = all_tasks.pop(str(tid))
    return removed_task

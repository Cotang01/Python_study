"""
Необходимо создать базу данных для интернет-магазина. База данных должна
состоять из трёх таблиц: товары, заказы и пользователи.
— Таблица «Товары» должна содержать информацию о доступных товарах, их
описаниях и ценах.
— Таблица «Заказы» должна содержать информацию о заказах, сделанных
пользователями.
— Таблица «Пользователи» должна содержать информацию о зарегистрированных
пользователях магазина.
• Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY),
имя, фамилия, адрес электронной почты и пароль.
• Таблица заказов должна содержать следующие поля: id (PRIMARY KEY),
id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и
статус заказа.
• Таблица товаров должна содержать следующие поля: id (PRIMARY KEY),
название, описание и цена.

Создайте модели pydantic для получения новых данных и возврата существующих
в БД для каждой из трёх таблиц.
Реализуйте CRUD операции для каждой из таблиц через создание маршрутов,
REST API.
"""
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
import crud
from database import SessionLocal, engine
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def index():
    return "Hello World"


@app.get("/users/", response_model=List[schemas.User])
async def read_users(skip: int = 0, limit: int = 1_000,
                     db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)


@app.get("/users/{user_id}")
async def read_user_by_id(user_id: int,
                          db: Session = Depends(get_db)):
    return crud.get_user_by_id(db, user_id=user_id)


@app.post("/users/", response_model=schemas.User)
async def create_user(new_user: schemas.UserCreate,
                      db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, user_email=new_user.email)
    if user:
        raise HTTPException(status_code=400,
                            detail=f"User with email {user.email} exists")
    return crud.create_user(db, user=new_user)


@app.put("/users/{user_id}", response_model=None)
async def change_user_password(user_id: int, new_password: str,
                               db: Session = Depends(get_db)):
    if not crud.change_user_password(db, user_id=user_id,
                                     new_password=new_password):
        raise HTTPException(status_code=400,
                            detail=f"No such user with id {user_id}")


@app.delete("/users/{user_id}", response_model=None)
async def delete_user(user_id: int,
                      db: Session = Depends(get_db)):
    if not crud.delete_user(db, user_id=user_id):
        raise HTTPException(status_code=400,
                            detail=f"No such user with id {user_id}")


@app.get("/products/", response_model=List[schemas.Product])
async def read_products(skip: int = 0, limit: int = 1_000,
                        db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)


@app.get("/products/{product_id}", response_model=schemas.Product)
async def read_product_by_id(product_id: int,
                             db: Session = Depends(get_db)):
    return crud.get_product_by_id(db, product_id=product_id)


@app.post("/products/", response_model=schemas.Product)
async def create_product(product: schemas.ProductCreate,
                         db: Session = Depends(get_db)):
    return crud.create_product(db, product=product)


@app.put("/products/{product_id}", response_model=bool)
async def change_product_price(product_id: int, new_price: float,
                               db: Session = Depends(get_db)):
    return crud.change_product_price(db, product_id=product_id,
                                     new_price=new_price)


@app.delete("/products/{product_id}", response_model=bool)
async def delete_product(product_id: int,
                         db: Session = Depends(get_db)):
    return crud.delete_product_by_id(db, product_id=product_id)


@app.get("/orders/", response_model=List[schemas.Order])
async def read_orders(skip: int = 0, limit: int = 1_000,
                      db: Session = Depends(get_db)):
    return crud.get_orders(db, skip=skip, limit=limit)


@app.get("/orders/order_id", response_model=schemas.Order)
async def read_order_by_id(order_id: int,
                           db: Session = Depends(get_db)):
    return crud.get_order_by_id(db, order_id=order_id)


@app.post("/orders/", response_model=bool)
async def create_order(order: schemas.OrderCreate,
                       user_id: int,
                       product_id: int,
                       db: Session = Depends(get_db)):
    return crud.create_order(db, order=order, user_id=user_id,
                             product_id=product_id)


@app.put("/orders/{order_id}", response_model=bool | None)
async def change_order_status(order_id: int,
                              db: Session = Depends(get_db)):
    if not crud.change_order_status(db, order_id=order_id):
        raise HTTPException(400, detail=f"No such order with id {order_id}")


@app.delete("/orders/{order_id}", response_model=bool | None)
async def delete_order(order_id: int,
                       db: Session = Depends(get_db)):
    if not crud.delete_order(db, order_id=order_id):
        raise HTTPException(400, detail=f"No such order with id {order_id}")


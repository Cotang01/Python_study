from typing import List
from datetime import datetime
from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    desc: str
    price: float


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    status: bool = False


class OrderCreate(OrderBase):
    date: datetime = datetime.now()


class Order(OrderBase):
    id: int
    user_id: int
    product_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    fname: str
    sname: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    orders: List[Order] = []

    class Config:
        orm_mode = True

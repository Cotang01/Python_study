from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime,\
    Boolean, Text
from database import Base


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True, nullable=False)
    desc = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    fname = Column(String(20), nullable=False)
    sname = Column(String(20), nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    date = Column(DateTime, nullable=False)
    status = Column(Boolean, nullable=False)

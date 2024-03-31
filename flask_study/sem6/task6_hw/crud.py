from sqlalchemy.orm import Session
import models, schemas
# from jose import JWTError, jwt
from passlib.context import CryptContext
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from datetime import datetime

pswd_context = CryptContext(schemes=["bcrypt"])
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_users(db: Session, skip: int = 0, limit: int = 1_000):
    return db \
        .query(models.User) \
        .offset(skip) \
        .limit(limit) \
        .all()


def get_user_by_id(db: Session, user_id: int):
    return db.get(models.User, user_id)


def get_user_by_email(db: Session, user_email: str):
    return db \
        .query(models.User) \
        .filter(models.User.email == user_email) \
        .first()


def create_user(db: Session, user: schemas.UserCreate):
    hash_password = pswd_context.hash(user.password)
    new_user = models.User(fname=user.fname, sname=user.sname,
                           email=user.email, password=hash_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def change_user_fname(db: Session, user_id: int, new_fname: str):
    user = db.get(models.User, user_id)
    if user:
        user.fname = new_fname
        db.commit()
        return True
    return False


def change_user_sname(db: Session, user_id: int, new_sname: str):
    user = db.get(models.User, user_id)
    if user:
        user.sname = new_sname
        db.commit()
        return True
    return False


def change_user_email(db: Session, user_id: int, new_email: str):
    user = db.get(models.User, user_id)
    email_duplicate = db \
        .query(models.User) \
        .filter(models.User.email == new_email) \
        .first()
    if email_duplicate:
        return False
    user.email = new_email
    db.commit()
    return True


def change_user_password(db: Session, user_id: int, new_password: str):
    user = db.get(models.User, user_id)
    if user:
        user.password = pswd_context.hash(new_password)
        db.commit()
        return True
    return False


def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False


def get_products(db: Session, skip: int = 0, limit: int = 1_000):
    return db \
        .query(models.Product) \
        .offset(skip) \
        .limit(limit) \
        .all()


def get_product_by_id(db: Session, product_id: int):
    return db.get(models.Product, product_id)


def get_product_by_name(db: Session, product_name: str):
    return db \
        .query(models.Product) \
        .filter(models.Product.name == product_name) \
        .first()


def create_product(db: Session, product: schemas.ProductCreate):
    cur_product = get_product_by_name(db, product.name)
    if cur_product:
        cur_product.quantity += 1
    else:
        cur_product = models.Product(name=product.name, desc=product.desc,
                                     price=product.price, quantity=1)
        db.add(cur_product)
    db.commit()
    db.refresh(cur_product)
    return cur_product


def change_product_name(db: Session, product_id: int, new_name: str):
    product = db.get(models.Product, product_id)
    if product:
        product.name = new_name
        db.commit()
        return True
    return False


def change_product_desc(db: Session, product_id: int, new_desc: str):
    product = db.get(models.Product, product_id)
    if product:
        product.desc = new_desc
        db.commit()
        return True
    return False


def change_product_price(db: Session, product_id: int, new_price: float):
    product = db.get(models.Product, product_id)
    if product:
        product.desc = new_price
        db.commit()
        return True
    return False


def delete_product_by_id(db: Session, product_id: int):
    product = db.get(models.Product, product_id)
    if product:
        db.delete(product)
        db.commit()
        return True
    return False


def get_orders(db: Session, skip: int = 0, limit: int = 1_000):
    return db.query(models.Order).offset(skip).limit(limit).all()


def get_order_by_id(db: Session, order_id: int):
    return db.get(models.Order, order_id)


def create_order(db: Session,
                 order: schemas.OrderCreate,
                 user_id: int,
                 product_id: int):
    new_order = models.Order(user_id=user_id, product_id=product_id,
                             date=order.date, status=order.status)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)


def change_order_status(db: Session, order_id: int):
    order = db.get(models.Order, order_id)
    if order:
        order.status = True
        db.commit()
        db.refresh(order)
        return True
    return False


def delete_order(db: Session, order_id: int):
    order = db.get(models.Order, order_id)
    if order:
        db.delete(order)
        db.commit()
        return True
    return False

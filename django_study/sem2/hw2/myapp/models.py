from django.db import models
"""
Создайте три модели Django: клиент, товар и заказ.

Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.

Поля модели «Клиент»:
— имя клиента
— электронная почта клиента
— номер телефона клиента
— адрес клиента
— дата регистрации клиента

Поля модели «Товар»:
— название товара
— описание товара
— цена товара
— количество товара
— дата добавления товара

Поля модели «Заказ»:
— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
— связь с моделью «Товар», указывает на товары, входящие в заказ
— общая сумма заказа
— дата оформления заказа
"""


class Customer(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.PositiveIntegerField(blank=False, null=False)
    address = models.CharField(max_length=50, blank=True, null=True)
    registration_date = models.DateField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    desc = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(blank=False, null=False)
    quantity = models.PositiveIntegerField(blank=False, null=False)
    publish_date = models.DateField(auto_now=True)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.FloatField(blank=False, null=False)
    creation_date = models.DateField(auto_now=True)


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_customer', views.create_customer, name='create_customer'),
    path('customers', views.show_customers, name='show_customers'),
    path('create_product', views.create_product),
    path('products', views.show_products),
]

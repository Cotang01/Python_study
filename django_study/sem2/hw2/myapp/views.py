from django.shortcuts import render
from . import forms
from . import models


def index(request):
    return render(request, "index.html")


def create_customer(request):
    context = {}
    form = forms.CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "create_customer.html", context)


def show_customers(request):
    context = {"customers": models.Customer.objects.all()}
    return render(request, "customers.html", context)


def create_product(request):
    context = {}
    form = forms.ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "create_product.html", context)


def show_products(request):
    context = {"products": models.Product.objects.all()}
    return render(request, "products.html", context)

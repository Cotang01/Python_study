from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone

from . import forms
from . import models


def index(request):
    return render(request, "index.html")


def customer(request):
    return render(request, "customer_panel.html")


def product(request):
    return render(request, "product_panel.html")


def order(request):
    return render(request, "order_panel.html")


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


def create_order(request):
    context = {}
    if request.method == "POST":
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.OrderForm()
        form.fields["products"].queryset = models.Product.objects.all()
    context["form"] = form
    return render(request, "create_order.html", context)


def show_orders(request):
    context = {"orders": models.Order.objects.all()}
    return render(request, "orders.html", context)


def show_customer_products(request, customer_id):
    customer_ = models.Customer.objects.get(id=customer_id)
    time_period = int(request.POST.get('time_period', 7))
    start_date = timezone.now() - timedelta(days=time_period)
    customer_orders = models.Order.objects\
        .filter(customer=customer_, creation_date__gte=start_date)\
        .prefetch_related('products')
    product_list = set()
    for o in customer_orders:
        p_list = o.products.all()
        for p in p_list:
            product_list.add(p)
    context = {'customer': customer_, 'ordered_products': product_list}
    return render(request, 'customer_products.html', context)

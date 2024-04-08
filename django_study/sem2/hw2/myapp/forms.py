from django import forms
from . import models


class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer

        fields = [
            "name",
            "email",
            "phone",
            "address",
        ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product

        fields = [
            "name",
            "desc",
            "price",
            "quantity",
        ]

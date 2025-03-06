from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView

from .models import Product, ProductType


def product_list(request):
    products = Product.objects.all()
    product_types = ProductType.objects.all()

    ctx = {
        "products": products,
        "product_types": product_types
    }

    return render(request, "product_list.html", ctx)


class ProductDetailView(DetailView):
    model = Product
    template_name = "product.html"

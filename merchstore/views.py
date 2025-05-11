"""Receives web requests and returns the necessary web response."""

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

from .models import Product, ProductType, Transaction
from .forms import ProductCreateForm, TransactionForm, ProductEditForm


def product_list(request):
    """Return product_list html file with apt context."""

    products = Product.objects.all()
    product_types = ProductType.objects.all()

    ctx = {
        "products": products,
        "product_types": product_types
    }

    return render(request, "product_list.html", ctx)

@login_required
def cart_list(request):
    """Return cart_list html file with apt context."""
    sellers = set()
    items_on_cart = Transaction.objects.filter(
        buyer=request.user.profile,
        status='on_cart'
    )
    for item in items_on_cart:
        sellers.add(item.product.owner)

    ctx = {
        "items_on_cart": items_on_cart,
        "sellers":sellers,
    }

    return render(request, "cart_list.html", ctx)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = TransactionForm()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = TransactionForm(request.POST)

    if form.is_valid():
        transaction = form.save(commit=False)
        if transaction.amount > product.stock:
            return render(request, 'product_detail.html', {
                    'form': form,
                    'product': product,
                    'error_message': f"Cannot add more than {product.stock} item(s) to the cart."
                })
        elif transaction.amount == 0:
            return render(request, 'product_detail.html', {
                    'form': form,
                    'product': product,
                    'error_message': f"Cannot add 0 items to the cart."
                })
        
        transaction.buyer = request.user.profile
        transaction.product = product
        transaction.status = 'on_cart'
        transaction.save()

        product.stock -= transaction.amount
        if product.stock == 0:
            product.status = 'out_of_stock'
        product.save()

        return redirect('merchstore:cart-list')
        
    ctx = {
        'form': form,
        'product': product
    }
    return render(request, 'product_detail.html', ctx)


@login_required
def create_product(request):
    form = ProductCreateForm()
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
    if form.is_valid():
        product = form.save(commit=False)
        product.owner = request.user.profile
        product.save()
        return redirect('merchstore:product-detail', pk=product.pk)
    ctx = {"form": form}
    return render(request, 'product_create.html', ctx)

@login_required
def edit_product(request,pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductEditForm()
    if request.method == 'POST':
        form = ProductEditForm(request.POST, instance=product)
        if form.is_valid():
            updated_product = form.save(commit=False)
            if updated_product.owner != request.user.profile:
                return render(request, 'product_detail.html', {
                    'form': form,
                    'product': product,
                    'error_message': "You are not authorized to edit this product."
                })
            updated_product.status = 'out_of_stock' if updated_product.stock == 0 else 'available'
            updated_product.save()
            return redirect('merchstore:product-detail', pk=product.pk)
    else:
        form = ProductEditForm(instance=product)

    ctx = {"form": form, "product":product}
    return render(request, 'product_create.html', ctx)

@login_required
def transactions_list(request):
    buyers= set()
    transactions_sold = Transaction.objects.filter(
        product__owner = request.user.profile,
        status='on_cart'
    )
    for item in transactions_sold:
        buyers.add(item.buyer)

    ctx = {
        "transactions_sold": transactions_sold,
        "buyers":buyers,
    }

    return render(request, "transaction_list.html", ctx)

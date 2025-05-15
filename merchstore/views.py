"""Receives web requests and returns the necessary web response."""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Product, Transaction, ProductType
from .forms import ProductCreateForm, TransactionForm, ProductEditForm

from user_management.models import Profile


def product_list(request):
    """Return product_list html file with apt context."""
    products = Product.objects.all()
    user_products = Product.objects.filter(owner=request.user.profile)
    other_products = Product.objects.exclude(owner=request.user.profile)

    user_product_types = ProductType.objects.filter(
        product__in=user_products
    ).distinct()

    other_product_types = ProductType.objects.filter(
        product__in=other_products
    ).distinct()

    ctx = {
        "products": products,
        "user_product_types": user_product_types,
        "other_product_types": other_product_types,
        "user_products": user_products,
        "other_products": other_products
    }

    return render(request, "product_list.html", ctx)


@login_required
def cart_list(request):
    """Return cart_list html file with apt context."""
        
    items_on_cart = Transaction.objects.filter(
        buyer=request.user.profile,
        status='on_cart'
    )

    seller_ids = items_on_cart.values_list('product__owner__id', flat=True).distinct()

    sellers = Profile.objects.filter(id__in=seller_ids)

    total_price = sum(item.amount * item.product.price for item in items_on_cart)

    ctx = {
        "items_on_cart": items_on_cart,
        "sellers": sellers,
        "total_price": total_price,
    }
    return render(request, "cart_list.html", ctx)


def product_detail(request, pk):
    """Return product_detail html file with apt context."""
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
                'error_message': (
                    f"Cannot add more than {product.stock} item(s) to the cart."
                ),
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
    """Return product_create html file with apt context."""
    form = ProductCreateForm()
    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
    if form.is_valid():
        product = form.save(commit=False)
        product.owner = request.user.profile
        product.save()
        return redirect('merchstore:product-detail', pk=product.pk)
    ctx = {"form": form}
    return render(request, 'product_create.html', ctx)


@login_required
def edit_product(request, pk):
    """Return product_create html file with apt context."""
    product = get_object_or_404(Product, pk=pk)
    form = ProductEditForm()
    if request.method == 'POST':
        form = ProductEditForm(request.POST, request.FILES, instance=product, )
        if form.is_valid():
            updated_product = form.save(commit=False)
            if updated_product.owner != request.user.profile:
                return render(request, 'product_detail.html', {
                    'form': form,
                    'product': product,
                    'error_message': (
                        "You are not authorized to edit this product."
                    ),
                })
            updated_product.status = 'out_of_stock' if updated_product.stock == 0 else 'available'
            updated_product.save()
            return redirect('merchstore:product-detail', pk=product.pk)
    else:
        form = ProductEditForm(instance=product)

    ctx = {"form": form, "product": product}
    return render(request, 'product_create.html', ctx)


@login_required
def transactions_list(request):
    transactions_sold = Transaction.objects.filter(
            product__owner=request.user.profile,
            status='on_cart'
        )

    buyer_ids = transactions_sold.values_list('buyer__id', flat=True).distinct()
    buyers = Profile.objects.filter(id__in=buyer_ids)
    projected_earnings = sum(item.amount * item.product.price for item in transactions_sold)

    ctx = {
        "transactions_sold": transactions_sold,
        "buyers": buyers,
        "projected_earnings": projected_earnings,
    }

    return render(request, "transaction_list.html", ctx)


@login_required
def edit_cart_item(request, pk):
    """Return cart_edit html file with apt context."""
    transaction = get_object_or_404(
        Transaction, pk=pk, buyer=request.user.profile, status='on_cart')
    product = transaction.product
    old_amount = transaction.amount
    old_stock = product.stock
    total_product = old_amount + old_stock
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            new_transaction = form.save(commit=False)

            if new_transaction.amount > total_product:
                return render(request, 'cart_list.html', get_cart_context(request.user,
                                                                          f"Cannot add more than {total_product} item(s)."))
            elif new_transaction.amount == 0:
                product.stock += old_amount
                product.save()
                transaction.delete()
                return redirect('merchstore:cart-list')

            product.stock += old_amount - new_transaction.amount

            if product.stock == 0:
                product.status = 'out_of_stock'
            else:
                product.status = 'available'

            product.save()

            new_transaction.save()
            return redirect('merchstore:cart-list')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'cart_edit.html', {'form': form,
                                              'transaction': transaction, 'product': product})


def get_cart_context(user, error_message=None):
    """Return cart context."""
    items_on_cart = Transaction.objects.filter(
        buyer=user.profile, status='on_cart')
    sellers = set(item.product.owner for item in items_on_cart)
    ctx = {'items_on_cart': items_on_cart, 'sellers': sellers}
    if error_message:
        ctx['error_message'] = error_message
    return ctx

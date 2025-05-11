"""Direct users to appropriate urls depending on needs."""

from django.urls import path
from .views import product_list, product_detail, create_product, cart_list, edit_product, transactions_list, edit_cart_item


urlpatterns = [

    path('items', product_list, name='product-list'),
    path('item/<int:pk>', product_detail, name='product-detail'),
    path('item/add', create_product, name='product-create'),
    path('cart', cart_list, name='cart-list'),
    path('item/<int:pk>/edit', edit_product, name='product-edit'),
    path('transactions', transactions_list, name='transactions'),
    path('cart/item/<int:pk>/edit', edit_cart_item, name='cart-item-edit'),

]

app_name = 'merchstore'

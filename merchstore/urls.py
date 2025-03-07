"""Direct users to appropriate urls depending on needs."""

from django.urls import path
from .views import product_list, ProductDetailView


urlpatterns = [

    path('items', product_list, name='product-list'),
    path('item/<int:pk>', ProductDetailView.as_view(), name='product-detail'),

]

app_name = 'merchstore'

"""Create needed models and their admin."""

from django.contrib import admin
from .models import Product, ProductType, Transaction

class TransactionInlineAdmin(admin.StackedInline):
    model = Transaction

class ProductAdmin(admin.ModelAdmin):
    """Create admin for Product."""
    model = Product
    search_fields = ('name',)
    list_display = ('name',)
    inlines=[TransactionInlineAdmin,]


class ProductTypeAdmin(admin.ModelAdmin):
    """Create admin for ProductType."""
    model = ProductType
    search_fields = ('name',)
    list_display = ('name',)




admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)

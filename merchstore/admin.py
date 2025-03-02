from django.contrib import admin
from .models import Product,ProductType


class ProductAdmin(admin.ModelAdmin):
    model = Product
    search_fields = ('name',)
    list_display = ('name',)


class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    search_fields = ('name',)
    list_display = ('name',)



admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)

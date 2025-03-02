from django.db import models
from django.urls import reverse

# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
    )
    description = models.TextField()
    price = models.DecimalField(decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('merchstore:product-detail', args=[self.pk])
"""Create models ProductType and Product with appropriate fields."""

from django.db import models
from django.urls import reverse

# Create your models here.


class ProductType(models.Model):
    """Create ProductType with appropriate field, sorted alphabetically."""

    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        """Return the name of the Product Type."""

        return self.name

    class Meta:
        """Order the product types alphabetically."""

        ordering = ["name"]


class Product(models.Model):
    """Create Product model with appropriate field, sorted alphabetically."""

    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        null=True,
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        """Return the name of the Product."""

        return self.name

    def get_absolute_url(self):
        """Return the url of the Product."""

        return reverse('merchstore:product-detail', args=[self.pk])

    class Meta:
        """Order the products by name."""

        ordering = ["name"]

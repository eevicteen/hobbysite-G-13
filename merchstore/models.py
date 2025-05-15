"""Create models ProductType and Product with appropriate fields."""

from django.db import models
from django.urls import reverse

from user_management.models import Profile


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
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    STATUS_CHOICES = [
        ('available', 'Available'),
        ('on_sale', 'On sale'),
        ('out_of_stock', 'Out of stock'),
    ]
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='available')

    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        """Return the name of the Product."""
        return self.name

    def get_absolute_url(self):
        """Return the url of the Product."""
        return reverse('merchstore:product-detail', args=[self.pk])

    class Meta:
        """Order the products by name."""

        ordering = ["name"]


class Transaction(models.Model):
    """Create Transaction Model with appropriate fields."""

    buyer = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True
    )
    amount = models.PositiveIntegerField(default=0)

    STATUS_CHOICES = [
        ('on_cart', 'On Cart'),
        ('to_pay', 'To Pay'),
        ('to_ship', 'To Ship'),
        ('to_receive', 'To Receive'),
        ('delivered', 'Delivered'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)

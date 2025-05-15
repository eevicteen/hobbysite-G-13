"""Create forms with appropriate fields."""

from django import forms
from django.contrib.auth.models import User

from .models import Product, Transaction

class ProductCreateForm(forms.ModelForm):
    """Create a form to Create a Product"""

    class Meta:
        """Create fields for the form and link Product model."""

        model = Product
        fields = ['name','product_type','description','price','stock','status','image']

class RegisterForm(forms.ModelForm):
    """Create a form to register"""

    class Meta:
        """Create fields for the form and link User model."""

        model = User
        fields = ['password','username','email']

class TransactionForm(forms.ModelForm):
    """Create a form for Transactions"""

    class Meta:
        """Create field for the form and link Transaction model."""

        model = Transaction
        fields = ['amount']

class ProductEditForm(forms.ModelForm):
    """Create a form to edit products"""

    class Meta:
        """Create field for the form and link Transaction model."""

        model = Product
        fields = ['name','product_type','description','price','stock','image']
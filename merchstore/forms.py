from django import forms
from django.contrib.auth.models import User

from .models import Product, Transaction

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','product_type','description','price','stock','status']

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password','username','email']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount']

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','product_type','description','price','stock']
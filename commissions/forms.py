from django import forms
from django.contrib.auth.models import User

from .models import Commission

class CommissionCreateForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['title','author','description','status']

# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['password','username','email']

# class TransactionForm(forms.ModelForm):
#     class Meta:
#         model = Transaction
#         fields = ['amount']

# class ProductEditForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name','product_type','description','price','stock']
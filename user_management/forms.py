from django import forms
from django.contrib.auth.models import User

from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'email_address']

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password','username','email']
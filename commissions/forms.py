from django import forms
from django.contrib.auth.models import User

from .models import Commission, Job, JobApplication

class CommissionCreateForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['title','description']

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        exclude = ['job','applicant','status',]

# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['password','username','email']

# class TransactionForm(forms.ModelForm):
#     class Meta:
#         model = Transaction
#         fields = ['amount']

class CommissionEditForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['title','description']
class JobCreateForm(forms.ModelForm):
    model = Job
    fields = ['role','manpower_required']
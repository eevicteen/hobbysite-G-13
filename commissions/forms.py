from django import forms
from django.contrib.auth.models import User

from .models import Commission, Job, JobApplication

class CommissionCreateForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['title','description','status']

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        exclude = ['job','applicant','status',]



class CommissionEditForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['title','description','status']
class JobCreateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['role','manpower_required']
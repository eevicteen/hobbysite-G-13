from django import forms
from django.contrib.auth.models import User

from .models import Commission, Job, JobApplication


class CommissionCreateForm(forms.ModelForm):
    """Create a form to Create a Commission."""

    class Meta:
        model = Commission
        fields = ['title', 'description', 'status']


class JobApplicationForm(forms.ModelForm):
    """Create a form to apply for a Job."""

    class Meta:
        model = JobApplication
        exclude = ['job', 'applicant', 'status',]


class CommissionEditForm(forms.ModelForm):
    """Create a form to edit a Commission."""

    class Meta:
        model = Commission
        fields = ['title', 'description', 'status']


class JobCreateForm(forms.ModelForm):
    """Create a form to create a Job."""

    class Meta:
        model = Job
        fields = ['role', 'manpower_required']

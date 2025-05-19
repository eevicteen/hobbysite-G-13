"""Create needed models and their admin."""

from django.contrib import admin
from .models import Commission, Job, JobApplication


class JobApplicationAdmin(admin.ModelAdmin):
    """Creates admin for job application."""
    model = JobApplication
    search_fields = ('applied_on',)
    list_display = ('applicant',)


class JobApplicationAdminInLine(admin.TabularInline):
    """Creates tabular inline for job application under job."""
    model = JobApplication


class JobAdmin(admin.ModelAdmin):
    """Creates admin for job."""
    model = Job
    search_fields = ('role',)
    list_display = ('role',)
    inlines = [JobApplicationAdminInLine]


class JobAdminInLine(admin.TabularInline):
    """Creates tabular inline for job under commission."""
    model = Job


class CommissionAdmin(admin.ModelAdmin):
    """Creates admin for commission."""
    model = Commission
    search_fields = ('title',)
    list_display = ('title',)
    inlines = [JobAdminInLine]


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)

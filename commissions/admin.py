"""Create needed models and their admin."""

from django.contrib import admin
from .models import Comments, Commission, Job, JobApplication

class CommentsAdmin(admin.ModelAdmin):
    """Creates admin for comments."""
    
    model = Comments
    search_fields = ('created_on',)
    list_display = ('entry',)
    
class CommentInLine(admin.TabularInline):
    """Creates tabular inline for comments under commission."""

    model = Comments


class CommissionAdmin(admin.ModelAdmin):
    """Creates admin for commission."""

    model = Commission
    search_fields = ('title',)
    list_display = ('title',)
    inlines = [CommentInLine]

class JobAdmin(admin.ModelAdmin):
    """Creates admin for job."""
    model=Job
    search_fields = ('role',)
    list_display = ('role',)

class JobApplicationAdmin(admin.ModelAdmin):
    """Creates admin for job application."""
    model=JobApplication
    search_fields = ('applied_on',)
    list_display = ('applicant',)


admin.site.register(Comments, CommentsAdmin)
admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)



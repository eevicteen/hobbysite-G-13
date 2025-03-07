"""Create needed models and their admin."""

from django.contrib import admin
from .models import Comments, Commission


class CommentInLine(admin.TabularInline):
    """Creates tabular inline for comments under commission."""

    model = Comments


class CommissionAdmin(admin.ModelAdmin):
    """Creates admin for commission."""

    model = Commission
    search_fields = ('title',)
    list_display = ('title',)
    inlines = [CommentInLine]


class CommentsAdmin(admin.ModelAdmin):
    """Creates admin for comments."""
    
    model = Comments
    search_fields = ('created_on',)
    list_display = ('entry',)


admin.site.register(Comments, CommentsAdmin)
admin.site.register(Commission, CommissionAdmin)

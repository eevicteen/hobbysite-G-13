"""Create needed models and their admin."""

from django.contrib import admin
from .models import Post, PostCategory


class PostCategoryAdmin(admin.ModelAdmin):
    """Create admin for ArticleCategory."""

    model = PostCategory


class PostAdmin(admin.ModelAdmin):
    """Create admin for Article."""

    model = Post


admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
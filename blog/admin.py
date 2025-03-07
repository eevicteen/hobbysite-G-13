"""Create needed models and their admin."""

from django.contrib import admin
from .models import Article, ArticleCategory


class ArticleCategoryAdmin(admin.ModelAdmin):
    """Create admin for ArticleCategory."""

    model = ArticleCategory


class ArticleAdmin(admin.ModelAdmin):
    """Create admin for Article."""

    model = Article


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)

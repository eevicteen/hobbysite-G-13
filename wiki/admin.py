# wiki/admin.py
"""Admin panel setup for the Wiki app."""

from django.contrib import admin

from .models import ArticleCategory, Article


class ArticleCategoryAdmin(admin.ModelAdmin):
    """
    Admin panel config for ArticleCategory.

    Displays name and description for each category.
    """

    model = ArticleCategory
    search_fields = ('name',)
    list_display = ('name', 'description')


class ArticleAdmin(admin.ModelAdmin):
    """
    Admin panel config for Article.

    Displays title and category.
    Provides filters for categories.
    """

    model = Article
    search_fields = ('title',)
    list_display = ('title', 'category')
    list_filter = ('category',)


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)

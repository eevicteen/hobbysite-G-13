# wiki/admin.py
"""Admin panel setup for the Wiki app."""

from django.contrib import admin

from .models import ArticleCategory, Article, Comment


class ArticleInLine(admin.TabularInline):
    """Tabular inline for articles."""

    model = Article


class CommentInLine(admin.TabularInline):
    """Tabular inline for comments under articles."""

    model = Comment


class ArticleCategoryAdmin(admin.ModelAdmin):
    """
    Admin panel config for ArticleCategory.

    Displays name and description for each category.
    """

    model = ArticleCategory
    search_fields = ('name',)
    list_display = ('name', 'description')
    inlines = [ArticleInLine]


class ArticleAdmin(admin.ModelAdmin):
    """
    Admin panel config for Article.

    Displays title and category.
    Provides filters for categories.
    """

    model = Article
    search_fields = ('title',)
    list_display = ('title', 'category', 'created_on', 'updated_on')
    list_filter = ('category',)
    readonly_fields = ('created_on', 'updated_on')
    inlines = [CommentInLine]


class CommentAdmin(admin.ModelAdmin):
    """
    Admin panel config for Comment.
    
    Searches using username, title, and entry.
    Displays author, associated article, and dates.
    Provides filters for author, associated article,
    and the creation date.
    """

    model = Comment
    search_fields = ('author__display_name', 'article__title', 'entry')
    list_display = ('author', 'article', 'created_on', 'updated_on')
    list_filter = ('author', 'article', 'created_on')
    readonly_fields = ('created_on', 'updated_on')


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

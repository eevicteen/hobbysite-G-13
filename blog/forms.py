"""Create forms with appropriate fields."""

from django import forms
from .models import Article, ArticleCategory, Comment, ArticleImage


class ArticleForm(forms.ModelForm):
    """Creates a form to add details for the Recipe"""
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']


class ArticleImageForm(forms.ModelForm):
    """Creates a form to update image for the Recipe"""
    class Meta:
        model = ArticleImage
        fields = ['image', 'description']


class CommentForm(forms.ModelForm):
    """Creates a form to write a comment"""
    class Meta:
        model = Comment
        fields = ['entry']


class ArticleCategoryForm(forms.ModelForm):
    """Creates a form to create a new article category"""
    class Meta:
        model = ArticleCategory
        fields = ['name', 'description']

class ArticleUpdateForm(forms.ModelForm):
    """Creates a form to update an article"""
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']
# wiki/forms.py
"""Forms for creating/updating Article and Comment instances."""

from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    """Form for creating new articles."""
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']


class CommentForm(forms.ModelForm):
    """Form for posting comments."""
    class Meta:
        model = Comment
        fields = ['entry']


class ArticleUpdateForm(forms.ModelForm):
    """Form for updating article contents."""
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']

class CommentUpdateForm(forms.ModelForm):
    """Form for updating comment contents."""
    class Meta:
        model = Comment
        fields = ['entry']

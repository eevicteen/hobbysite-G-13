"""Create forms with appropriate fields."""

from django import forms
from .models import Article, Comment, ArticleImage


class ArticleForm(forms.ModelForm):
    """Create a form to add details for the Article."""

    class Meta:
        """Create fields for the form and link Article model."""

        model = Article
        fields = ['title', 'category', 'entry', 'header_image']


class ArticleImageForm(forms.ModelForm):
    """Creates a form to update image for the Article."""

    class Meta:
        """Create fields for the form and link ArticleImage model."""

        model = ArticleImage
        fields = ['image', 'description']


class CommentForm(forms.ModelForm):
    """Creates a form to write a comment."""

    class Meta:
        """Create fields for the form and link Comment model."""

        model = Comment
        fields = ['entry']

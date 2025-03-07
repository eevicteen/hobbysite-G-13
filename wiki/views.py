# wiki/views.py
"""List and detail views for Wiki articles."""

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import ArticleCategory, Article


class ArticleListView(ListView):
    """
    View for the list of article categories.

    Connects corresponding template to the category model.
    """

    model = ArticleCategory
    template_name = 'wiki_list.html'
    context_object_name = 'articlecategory'


class ArticleDetailView(DetailView):
    """
    View for the article(s).
    
    Connects corresponding template to the article model.
    """

    model = Article
    template_name = 'wiki_details.html'
    context_object_name = 'article'
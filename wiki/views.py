# wiki/views.py
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import ArticleCategory, Article


class ArticleListView(ListView):
    model = ArticleCategory
    template_name = 'wiki_list.html'
    context_object_name = 'articlecategory'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'wiki_details.html'
    context_object_name = 'article'
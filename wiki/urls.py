# ledger/urls.py
"""Defines namespace (wiki) and matches views to corresponding URLs."""

from django.urls import path

from .views import ArticleListView, ArticleDetailView


app_name = 'wiki'


urlpatterns = [
    path('articles/', ArticleListView.as_view(), name="article_list"),
    path('article/<int:id>/', ArticleDetailView.as_view(), name="article_details"),
]

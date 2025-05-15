# ledger/urls.py
"""Defines namespace (wiki) and matches views to corresponding URLs."""

from django.urls import path

from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, CommentUpdateView


app_name = 'wiki'


urlpatterns = [
    path('articles/', ArticleListView.as_view(), name="article_list"),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="article_details"),
    path('article/add/', ArticleCreateView.as_view(), name="article_create"),
    path('article/<int:pk>/edit/', ArticleUpdateView.as_view(), name="article_update"),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name="comment_edit")
]

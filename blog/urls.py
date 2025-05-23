"""Direct users to appropriate urls depending on needs."""
from django.urls import path
from .views import blog_list, blog_details, add_article, article_update

app_name = "blog"

urlpatterns = [
    path('articles/', blog_list, name='blog_list'),
    path('article/<int:id>/', blog_details, name='blog_detail'),
    path('article/add/', add_article, name="add_article"),
    path('article/<int:id>/edit', article_update, name="article_update"),
]

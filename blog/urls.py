"""Direct users to appropriate urls depending on needs."""
from django.urls import path
from .views import blog_list, blog_details


app_name = "blog"

urlpatterns = [
    path('blog/articles/', blog_list, name='blog_list'),
    path('blog/articles/<int:id>/', blog_details, name='blog_detail'),
]

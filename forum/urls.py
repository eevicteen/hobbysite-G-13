"""Direct users to appropriate urls depending on needs."""

from django.urls import path
from .views import forum_list, forum_details


app_name = "forum"


urlpatterns = [
    path('forum/threads/', forum_list, name='forum_list'),
    path('forum/threads/<int:id>/', forum_details, name='forum_detail'),
]

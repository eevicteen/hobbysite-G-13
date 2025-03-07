"""Direct users to appropriate urls depending on needs."""

from django.urls import path
from .views import forum_list, forum_details


app_name = "forum"


urlpatterns = [
    path('threads/', forum_list, name='forum_list'),
    path('threads/<int:id>/', forum_details, name='forum_detail'),
]

from django.urls import path
from .views import threads, thread

urlpatterns = [
    path('threads', threads, name='list'),
    path('thread/<int:pk>', thread, name='recipe1'),
]
app_name = "forum"
"""Direct users to home urls depending on needs."""

from django.urls import path
from .views import home_view


urlpatterns = [

    path('', home_view, name='home')

]

app_name = 'home'

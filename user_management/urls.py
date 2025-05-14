from django.urls import path

from .views import profile_update
app_name = "user_management"

urlpatterns = [
    path('<str:username>/', profile_update, name='profile-update'),

]

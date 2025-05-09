from django.urls import path

from .views import profile_update, register
app_name = "user_management"

urlpatterns = [
    path('<str:username>/', profile_update, name='profile-update'),
    # path('login', login, name='login'),
    path('register', register, name='profile-create'),
]

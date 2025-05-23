"""
URL configuration for hobbysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('wiki/', include('wiki.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('wiki/', include('wiki.urls', namespace='wiki')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('commissions/', include('commissions.urls', namespace='commissions')),
    path('merchstore/', include('merchstore.urls', namespace='merchstore')),
    path('forum/', include('forum.urls', namespace='forum')),
    path('accounts/',include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', include('user_management.urls', namespace='profile')),
    path('', include('home.urls', namespace='home')),
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

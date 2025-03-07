"""Direct users to appropriate urls depending on needs."""

from django.urls import path
from .views import CommissionListView, commission_detail

urlpatterns = [

    path('list', CommissionListView.as_view(), name='commissions-list'),
    path('detail/<int:pk>', commission_detail, name='commission-detail'),

]

app_name = 'commissions'

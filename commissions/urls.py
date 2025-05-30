"""Direct users to appropriate urls depending on needs."""

from django.urls import path
from .views import CommissionListView, commission_detail, create_commission, edit_commission

urlpatterns = [

    path('list', CommissionListView.as_view(), name='commissions-list'),
    path('detail/<int:pk>', commission_detail, name='commission-detail'),
    path('add', create_commission, name='commissions-create'),
    path('<int:pk>/edit', edit_commission, name='commission-edit'),

]

app_name = 'commissions'

from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('success_checkout/<order_number>', views.success_checkout, name='success_checkout'),
    path('cache_data_checkout/', views.cache_data_checkout, name='cache_data_checkout'),
    path('wh/', webhook, name='webhook'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('newsletters/', views.newsletters, name='newsletters'),
    path(
        '<int:newsletter_id>/',
        views.newsletter_view, name='newsletter_view'
        ),
    path('add/', views.new_newsletter, name='new_newsletter'),
    path(
        'delete/<int:newsletter_id>/',
        views.newsletter_delete, name='newsletter_delete'
        ),
]

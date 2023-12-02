from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('show_items/', views.show_items, name='show_items'),
]

from django.urls import path
from .views import category_list, filter_by_brand 

urlpatterns = [
    path('list/', category_list, name='category_list'),
    path('filter_by_brand/<slug:brand_slug>/', filter_by_brand, name='filter_by_brand'),
]
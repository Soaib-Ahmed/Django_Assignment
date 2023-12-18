from django.urls import path
from .views import BuyNowView, CarDetailView,CarListView


urlpatterns = [
    path('<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('buy_now/<int:car_id>/', BuyNowView.as_view(), name='buy_now'),
    path('cars/', CarListView.as_view(), name='car_list'),
]
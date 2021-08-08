from django.urls import path

from .views import RestaurantListAPIView, RestaurantDetailAPIView

app_name = 'restaurants-api'

urlpatterns = [
    path('', RestaurantListAPIView.as_view(), name='restaurants-list'),
    path('<int:pk>/', RestaurantDetailAPIView.as_view(), name='restaurants-detail'),
]

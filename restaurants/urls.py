from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import RestaurantsListView, RestaurantsDetailView

# router = DefaultRouter()
# router.register('restaurants', RestaurantViewSet)

app_name = 'restaurant'

urlpatterns = [
    path('', RestaurantsListView.as_view(), name='list'),
    path('<int:pk>/', RestaurantsDetailView.as_view(), name='detail'),
    # path('api/', RestaurantViewSet.as_view()),
    # path('api', include(router.urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

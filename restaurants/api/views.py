from rest_framework import generics, filters

from django_filters import FilterSet, MultipleChoiceFilter, NumberFilter
from django_filters.rest_framework import DjangoFilterBackend

from restaurants.models import Restaurant, Rating
from .serializers import RestaurantSerializer


class RestaurantFilter(FilterSet):

    north = NumberFilter(field_name='lat', lookup_expr='lt')
    south = NumberFilter(field_name='lat', lookup_expr='gt')
    east = NumberFilter(field_name='lng', lookup_expr='lt')
    west = NumberFilter(field_name='lng', lookup_expr='gt')

    rating = MultipleChoiceFilter(
        choices=Rating.choices,
    )


class RestaurantListAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Restaurant.objects.all().order_by('-id')
    serializer_class = RestaurantSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    search_fields = ['name', 'rating']
    ordering_fields = ['name']
    filterset_class = RestaurantFilter


class RestaurantDetailAPIView(generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

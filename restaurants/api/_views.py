from rest_framework import pagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

from restaurants.models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantListAPIView(APIView, LimitOffsetPagination):
    permission_classes = []
    authentication_classes = []
    pagination_class = LimitOffsetPagination

    def get(self, request, format=None):
        qs = Restaurant.objects.all().order_by('-id')

        results = self.paginate_queryset(qs, request, view=self)

        serializer = RestaurantSerializer(results, many=True, context={'request': request})
        # serializer = RestaurantSerializer(qs, many=True)
        # return Response(serializer.data)
        return self.get_paginated_response(serializer.data)

    def get_queryset(self):
        request = self.request
        qs = Restaurant.objects.all()
        query = request.GET.get('q')
        print(query)
        if query is not None:
            qs = qs.filter(rating__icontains=query)
        return qs

    def get_serializer_context(self):
        return {'request': self.request}

    def post(self, request, format=None):
        north = request.data.get('north')
        south = request.data.get('south')
        east = request.data.get('east')
        west = request.data.get('west')
        qs = Restaurant.objects.filter(
            Q(lat__range=(south, north)) &
            Q(lng__range=(west, east))
            )
        serializer = RestaurantSerializer(qs, many=True)
        return Response(serializer.data)


class RestaurantDetailAPIView(APIView):
    permission_classes = []
    authentication_classes = []
    # serializer = RestaurantSerializer

    # def get(self, request, format=None):
    def get(self, request, pk, format=None):
        qs = Restaurant.objects.filter(pk=pk)
        serializer = RestaurantSerializer(qs, many=True, context={'request': request})
        return Response(serializer.data)
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from restaurants.models import Restaurant

from restaurants.api.serializers import RestaurantSerializer


RESTAURANTS_URL = reverse('api-restaurant:restaurants-list')


def sample_restaurant(**params):
    """Create and return a sample restaurant"""
    defaults = {
        'name': 'Sample restaurant',
        'name_en': 'Sample restaurant EN',
        'category': 'Sushi',
        'rating': 'ONE',
        'lat': '35.6654183',
        'lng': '139.7736446'
    }
    defaults.update(params)

    return Restaurant.objects.create(**defaults)


class PublicRestaurantTests(APITestCase):
    """Test unauthenticated restaurant API access"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_restaurants(self):
        """Test retrieving a list of recipes"""
        sample_restaurant()
        sample_restaurant()

        res = self.client.get(RESTAURANTS_URL)

        # restaurants = Restaurant.objects.all().order_by('-id')
        # serializer = RestaurantSerializer(restaurants, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Restaurant.objects.count(), 2)

    # data 作成　post でデータ返却されるか確認
    def test_retrieve_restaurant_POST_by_coordinate(self):
        """Test retrieving a shop from coordinate"""
        sample_restaurant()
        payload = {
            'north': 35.729982806137485,
            'south': 35.64482440464725,
            'east': 140.0478995450652,
            'west': 139.65857154213552,
        }
        res = self.client.post(RESTAURANTS_URL, payload)
        self.assertEqual(len(res.data), 1)

    def test_retrieve_restaurant_POST_by_coordinate_with_rating(self):
        """Test retrieving a shop from coordinate"""
        sample_restaurant()
        payload = {
            'rating[]': 'ONE',
            'north': 35.729982806137485,
            'south': 35.64482440464725,
            'east': 140.0478995450652,
            'west': 139.65857154213552,
        }
        res = self.client.post(RESTAURANTS_URL, payload)
        self.assertEqual(len(res.data), 1)


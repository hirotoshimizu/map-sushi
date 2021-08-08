from django.test import TestCase

from restaurants.models import Restaurant


class ModelTests(TestCase):

    def test_restaurant_str(self):
        """Test the restaurant string representation"""
        restaurant = Restaurant.objects.create(
            name='Test Restaurant',
            name_en='Test Restaurant En',
            category='sushi',
        )
        self.assertEqual(str(restaurant), restaurant.name)
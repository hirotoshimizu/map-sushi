from django.test import TestCase
from django.urls import reverse

from restaurants.models import Restaurant

RESTAURANTS_LIST_URL = reverse('restaurant:list')


class HomePageTest(TestCase):

    def test_restaurants_list_returns_correct_html(self):
        response = self.client.get(RESTAURANTS_LIST_URL)
        html = response.content.decode('utf8')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<title>sushi map</title>', html)
        self.assertTemplateUsed(response, 'restaurants/list.html')

    def test_restaurants_detail_returns_correct_html(self):
        restaurant = Restaurant.objects.create(
            name='Sample restaurant',
            name_en='Sample restaurant EN',
            category='sushi',
            rating='ONE',
            lat=35.6654183,
            lng=139.7736446
        )
        response = self.client.get(f'/restaurants/{restaurant.id}/')
        html = response.content.decode('utf8')
        self.assertEqual(response.status_code, 200)
        self.assertIn(f'<h1>{restaurant}</h1>', html)
        self.assertTemplateUsed(response, 'restaurants/detail.html')

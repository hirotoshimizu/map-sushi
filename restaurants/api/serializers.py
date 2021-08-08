from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from restaurants.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    # uri = serializers.HyperlinkedIdentityField(view_name='restaurants-detail')

    class Meta:
        model = Restaurant
        fields = [
            'id', 'name', 'lat', 'lng', 'rating', 'price', 'uri'
        ]

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse(
            'api-restaurant:restaurants-detail',
            args=[obj.id],
            request=request
        )

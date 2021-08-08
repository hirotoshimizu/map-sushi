from django import forms
from django.conf import settings
from django.contrib import admin
from django.shortcuts import render
from django.urls import path

from .models import Restaurant


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ('name', 'pref', 'city',)
    list_display = ('name', 'category', 'rating', 'pref', 'city', 'price', 'lat', 'lng',)
    list_editable = ('category',)
    list_filter = ('rating', 'pref', 'city',)

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'coordinate.js',
                )

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path('upload-csv/', self.upload_csv),
        ]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == 'POST':
            csv_file = request.FILES['csv_upload']

            file_data = csv_file.read().decode('utf-8')
            restaurants_data = file_data.split('\n')

            for i, restaurant_data in enumerate(restaurants_data):
                if i == 0:
                    continue
                fields = restaurant_data.split(",")
                Restaurant.objects.update_or_create(
                    name=fields[0],
                    name_en=fields[1],
                    category=fields[2],
                    url=fields[3],
                    rating=fields[4],
                    description=fields[5],
                    business_hour=fields[6],
                    closed=fields[7],
                    price=fields[8],
                    pref=fields[9],
                    city=fields[10],
                    street_address=fields[11],
                    website=fields[12],
                    access=fields[13],
                    tel=fields[14],
                    fax=fields[15],
                    business_hour_detail=fields[16],
                    closed_detail=fields[17],
                    credit_cards=fields[18],
                    seats=fields[19],
                    rooms=fields[20],
                    smoking=fields[21],
                    take_out=fields[22],
                    signal=fields[23],
                    facility_services=fields[24],
                    sales_point=fields[25],
                    cancel=fields[26])
     
        form = CsvImportForm()
        data = {'form': form}
        return render(request, 'admin/csv_upload.html', data)


admin.site.register(Restaurant, RestaurantAdmin)

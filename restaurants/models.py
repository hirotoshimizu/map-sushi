from django.db import models


class Rating(models.TextChoices):
    THREESTARS = 'THREE', '三つ星'
    TWOSTARS = 'TWO', '二つ星'
    ONESTAR = 'ONE', '一つ星'
    BIBGOURMAND = 'BIB', 'ビブグルマン'
    THEMICHELINPLATE = 'TMP', 'ミシュランプレート'


class Restaurant(models.Model):
    name = models.CharField(max_length=70)
    name_en = models.CharField(max_length=70)
    category = models.CharField(max_length=20)
    url = models.CharField(max_length=250, null=True, blank=True)
    # rating = models.CharField(max_length=20, null=True, blank=True)
    rating = models.CharField(
        max_length=5, choices=Rating.choices,
        default=Rating.BIBGOURMAND
    )
    description = models.TextField(null=True, blank=True)
    business_hour = models.CharField(max_length=100, null=True, blank=True)
    closed = models.CharField(max_length=20, null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    pref = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=70, null=True, blank=True)
    street_address = models.CharField(max_length=70, null=True, blank=True)
    website = models.CharField(max_length=250, null=True, blank=True)
    access = models.CharField(max_length=250, null=True, blank=True)
    tel = models.CharField(max_length=13, null=True, blank=True)
    fax = models.CharField(max_length=13, null=True, blank=True)
    business_hour_detail = models.TextField(null=True, blank=True)
    closed_detail = models.CharField(max_length=100, null=True, blank=True)
    credit_cards = models.CharField(max_length=100, null=True, blank=True)
    seats = models.CharField(max_length=100, null=True, blank=True)
    rooms = models.CharField(max_length=100, null=True, blank=True)
    smoking = models.CharField(max_length=100, null=True, blank=True)
    take_out = models.CharField(max_length=70, null=True, blank=True)
    signal = models.CharField(max_length=100, null=True, blank=True)
    facility_services = models.CharField(max_length=100, null=True, blank=True)
    sales_point = models.CharField(max_length=250, null=True, blank=True)
    cancel = models.TextField(null=True, blank=True)
    lat = models.DecimalField(
        max_digits=10, decimal_places=7,
        null=True, blank=True
    )
    lng = models.DecimalField(
        max_digits=10, decimal_places=7,
        null=True, blank=True
    )

    def __str__(self):
        return self.name

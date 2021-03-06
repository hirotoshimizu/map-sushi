# Generated by Django 3.2.5 on 2021-07-23 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_alter_restaurant_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]

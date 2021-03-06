# Generated by Django 3.2.5 on 2021-07-23 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_auto_20210723_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True),
        ),
    ]

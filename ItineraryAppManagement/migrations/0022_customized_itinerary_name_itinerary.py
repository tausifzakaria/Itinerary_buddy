# Generated by Django 4.0.5 on 2022-06-11 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ItineraryAppManagement', '0021_order_countryphone_code_alter_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customized_itinerary',
            name='name_itinerary',
            field=models.CharField(default='', max_length=50),
        ),
    ]

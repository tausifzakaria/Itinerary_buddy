# Generated by Django 4.0 on 2022-05-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='country',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='account',
            name='mobile',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='account',
            name='nationality',
            field=models.CharField(default='', max_length=10),
        ),
    ]

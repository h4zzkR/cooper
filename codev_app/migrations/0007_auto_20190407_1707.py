# Generated by Django 2.2 on 2019-04-07 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codev_app', '0006_auto_20190407_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 7, 17, 7, 43, 640368)),
        ),
        migrations.AlterField(
            model_name='token',
            name='creation_date',
            field=models.CharField(default=datetime.time(17, 7, 43, 641120), max_length=20),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='4b8dc9c38d9544da9cc23dbf97c93f31', max_length=30),
        ),
    ]
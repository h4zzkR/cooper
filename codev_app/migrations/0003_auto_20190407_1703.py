# Generated by Django 2.2 on 2019-04-07 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codev_app', '0002_auto_20190407_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 7, 17, 3, 43, 582195)),
        ),
        migrations.AlterField(
            model_name='token',
            name='creation_date',
            field=models.CharField(default=datetime.time(17, 3, 43, 582948), max_length=20),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='96613a4c5ba84a38b8d3e2ee0b8b5825', max_length=30),
        ),
    ]

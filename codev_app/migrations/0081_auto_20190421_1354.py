# Generated by Django 2.2 on 2019-04-21 13:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codev_app', '0080_auto_20190421_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 21, 13, 54, 9, 468835)),
        ),
        migrations.AlterField(
            model_name='token',
            name='creation_date',
            field=models.CharField(default=datetime.time(13, 54, 9, 472426), max_length=20),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='3dc9e61772a74ee39dfeacad2d5015c5', max_length=30),
        ),
    ]

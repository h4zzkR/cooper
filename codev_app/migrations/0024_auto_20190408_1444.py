# Generated by Django 2.2 on 2019-04-08 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codev_app', '0023_auto_20190408_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 8, 14, 44, 28, 795796)),
        ),
        migrations.AlterField(
            model_name='token',
            name='creation_date',
            field=models.CharField(default=datetime.time(14, 44, 28, 796567), max_length=20),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='5dca3401236945e09c8c19f1beccb047', max_length=30),
        ),
    ]
# Generated by Django 2.2 on 2019-04-21 14:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codev_app', '0094_auto_20190421_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 21, 14, 8, 37, 931510)),
        ),
        migrations.AlterField(
            model_name='token',
            name='creation_date',
            field=models.CharField(default=datetime.time(14, 8, 37, 933924), max_length=20),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='d1fc243e25ce4622aa7b554e1688c464', max_length=30),
        ),
    ]
# Generated by Django 2.2 on 2019-04-21 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codev_app', '0078_auto_20190421_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 21, 13, 52, 40, 179037)),
        ),
        migrations.AlterField(
            model_name='token',
            name='creation_date',
            field=models.CharField(default=datetime.time(13, 52, 40, 182943), max_length=20),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='5514ec2c8745419ea81712ee0d1a38aa', max_length=30),
        ),
    ]

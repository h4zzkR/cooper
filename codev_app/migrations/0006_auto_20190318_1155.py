# Generated by Django 2.1.7 on 2019-03-18 11:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codev_app', '0005_auto_20190318_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 18, 11, 55, 5, 13941)),
        ),
    ]

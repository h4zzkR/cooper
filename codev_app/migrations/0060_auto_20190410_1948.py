# Generated by Django 2.2 on 2019-04-10 19:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codev_app', '0059_auto_20190410_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 10, 19, 48, 54, 281880)),
        ),
        migrations.AlterField(
            model_name='token',
            name='creation_date',
            field=models.CharField(default=datetime.time(19, 48, 54, 284670), max_length=20),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='ea08f4cc6f214a19b1307e2c5b3f7c12', max_length=30),
        ),
    ]

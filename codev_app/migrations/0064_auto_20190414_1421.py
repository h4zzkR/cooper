# Generated by Django 2.1.7 on 2019-04-14 14:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codev_app', '0063_auto_20190414_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 14, 14, 21, 36, 428710)),
        ),
        migrations.AlterField(
            model_name='token',
            name='creation_date',
            field=models.CharField(default=datetime.time(14, 21, 36, 429945), max_length=20),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='8ac79256bec74ff3a6a1ea6e461b0525', max_length=30),
        ),
    ]

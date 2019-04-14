# Generated by Django 2.2 on 2019-04-14 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codev_app', '0064_auto_20190414_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tag',
            new_name='tags',
        ),
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 14, 15, 57, 42, 948283)),
        ),
        migrations.AlterField(
            model_name='token',
            name='creation_date',
            field=models.CharField(default=datetime.time(15, 57, 42, 951376), max_length=20),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='e9911fc396864b179d2c723c14a3e775', max_length=30),
        ),
    ]

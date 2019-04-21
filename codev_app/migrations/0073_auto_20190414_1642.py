# Generated by Django 2.1.7 on 2019-04-14 16:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codev_app', '0072_auto_20190414_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 14, 16, 42, 11, 623573)),
        ),
        migrations.AlterField(
            model_name='token',
            name='creation_date',
            field=models.CharField(default=datetime.time(16, 42, 11, 625069), max_length=20),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='af2c7427de714bd28747a3235a4bbe0a', max_length=30),
        ),
    ]
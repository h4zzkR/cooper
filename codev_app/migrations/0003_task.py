# Generated by Django 2.1.7 on 2019-03-17 22:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codev_app', '0002_auto_20190317_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea', models.CharField(max_length=200)),
                ('body', models.TextField(max_length=10000)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2019, 3, 17, 22, 1, 8, 640102))),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 2.2 on 2019-04-07 14:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modules.user_manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='surname')),
                ('nickname', models.CharField(max_length=30, unique=True)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='registered')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='users/avatars/')),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', modules.user_manager.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default='04d60a6ceab8446bb682980ae790793f', max_length=30)),
                ('creation_date', models.CharField(default=datetime.time(14, 24, 44, 677812), max_length=20)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea', models.CharField(max_length=200)),
                ('body', models.TextField(max_length=20000)),
                ('simple_about', models.TextField(default='Краткое описание', max_length=100)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2019, 4, 7, 14, 24, 44, 677028))),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

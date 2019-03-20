from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from modules.user_manager import UserManager
import datetime


class User(AbstractBaseUser):

    email = models.EmailField(_('email'), unique=True)
    first_name = models.CharField(_('name'), max_length=30, blank=True)
    last_name = models.CharField(_('surname'), max_length=30, blank=True)
    nickname = models.CharField(max_length=30, unique=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(_('registered'), auto_now_add=True)
    is_active = models.BooleanField(_('is_active'), default=True)
    avatar = models.ImageField(upload_to='users/avatars/', null=True, blank=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = [first_name, last_name, nickname, email]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Возвращает first_name и last_name с пробелом между ними.
        '''
        full_name = '{}{}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_nickname(self):
        '''
        Возвращает ник пользователя
        '''
        return self.nickname

    def email_user(self, subject, message, email_receiver):
        '''
        Отправляет электронное письмо этому пользователю.
        '''
        send_mail(subject, message, self.email, email_receiver)


class Task(models.Model):
    idea = models.CharField(max_length=200)
    body = models.TextField(max_length=10000)
    creation_date = models.DateTimeField(default=datetime.datetime.now())
    author = models.ForeignKey(to=User, blank=True, on_delete=models.CASCADE, null=True)

# class PropertyImage(models.Model):
#     name = models.ForeignKey(Task, related_name='Task', on_delete=models.CASCADE, blank=True, null=True)
#     image = models.ImageField(upload_to='images')
#
#     def __str__(self):  # __unicode__ on Python 2
#         return self.name
#
#     class Meta:
#         ordering = ('name',)

# class Token(models.Model):
#     token = models.CharField(max_length=30)
#     user = models.ForeignKey(to=User, blank=True, on_delete=models.CASCADE, null=True)
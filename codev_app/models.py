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
import modules.stuff as stuff

class Message(models.Model):
    text = models.CharField(max_length=20000)

class Chat(models.Model):
    name = models.CharField(max_length=2000)
    messages = models.ManyToManyField(Message)

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
    chats = models.ManyToManyField(Chat)

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

    @property
    def has_perm(self, perm, obj=None):
        return self.is_superuser

class Task(models.Model):
    idea = models.CharField(max_length=200)
    body = models.TextField(max_length=20000)
    simple_about = models.TextField(max_length=100, default='Краткое описание')
    creation_date = models.DateTimeField(default=datetime.datetime.now())
    author = models.ForeignKey(to=User, blank=True, on_delete=models.CASCADE, null=True)

class Token(models.Model):
    token = models.CharField(max_length=30, default=stuff.token_generator(), null=False)
    user = models.ForeignKey(to=User, blank=True, on_delete=models.PROTECT, null=True)
    creation_date = models.CharField(max_length=20, default=datetime.datetime.now().time(),
                                     null=False)
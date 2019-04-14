from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from modules.user_manager import UserManager
import datetime
import modules.stuff as stuff
from django.db import models
import django.utils.timezone as time
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

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

    @property
    def has_perm(self, perm, obj=None):
        return self.is_superuser

class Task(models.Model):
    idea = models.CharField(max_length=1000)
    body = models.TextField(max_length=20000)
    simple_about = models.TextField(max_length=100, default='Краткое описание')
    creation_date = models.DateTimeField(default=datetime.datetime.now())
    author = models.ForeignKey(to=User, blank=True, on_delete=models.PROTECT, null=True)
    max_subs = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(300)])

class Subscribe(models.Model):
    user = models.ForeignKey(to=User, blank=True, null=True, on_delete=models.DO_NOTHING, default=None)
    task = models.ForeignKey(to=Task, blank=True, null=True, on_delete=models.DO_NOTHING, default=None)
    time_subscribed = models.DateTimeField(auto_now=True)

class Token(models.Model):
    token = models.CharField(max_length=30, default=stuff.token_generator(), null=False)
    user = models.ForeignKey(to=User, blank=True, on_delete=models.PROTECT, null=True)
    creation_date = models.CharField(max_length=20, default=datetime.datetime.now().time(),
                                     null=False)
from django import forms
from .models import User
from django.conf import settings
from django.core.files import File
from codev_app.models import *
import modules.stuff as stuff
import modules.avatars as avatars
from django.contrib.auth import login as auth_login
import os
from codev_app.views import *

from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Логин',
            }
        )
    )
    password = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
            }
        )
    )


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('nickname', 'password', 'email', 'first_name', 'last_name')


    def save_avatar_and_login(self, request, user):
        hash = stuff.avatar_generator()
        get_avatar(hash, user)
        return user


class MakeTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['idea', 'body', 'simple_about']
        # fields.remove('creation_date')
        # fields.append('author')


class AddTaskForm(forms.Form):
    idea = forms.CharField(
        # label='Название',
        # max_length=200,
        # widget=forms.TextInput()
    )

    body = forms.CharField(
        label='Опишите вашу идею здесь',
        max_length=10000,
        widget=forms.Textarea()
    )

    def is_valid(self):
        idea = self.data['idea']
        body = self.data['body']
        simple_about = self.data['simple_about']
        max_subs = int(self.data['max_subs'])
        if isinstance(idea, str) and isinstance(body, str) and isinstance(simple_about, str)\
                and max_subs <= 40 and max_subs >= 1:
            return True
        else:
            return False


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('nickname', 'first_name', 'last_name', 'email', 'location', 'bio', 'avatar')

    def save_avatar(self, request):
        user = User.objects.get(nickname=request.user.nickname)
        # os.system('rm -rf {}'.format(user.avatar))
        try:
            image = request.FILES['avatar']
        except KeyError:
            return None
        # image = stuff.image_preproc(image)
        user.avatar = File(image)

        # r = open(path, 'rb')
        # avatar = File(r)
        # user.avatar = image
        # path = settings.MEDIA_ROOT + '/users/'
        # os.system('rm -rf {}'.format(path + str(user.id) + '_avatar.png'))
        # user.avatar.save(str(user.id) + '_avatar.png', avatar)
        # user.save()
        # os.system('rm -rf {}'.format(path))
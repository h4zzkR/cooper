from django import forms
from .models import User
from django.conf import settings
from django.core.files import File
from codev_app.models import *
import modules.stuff as stuff
import modules.avatars as avatars
from django.contrib.auth import login as auth_login
import os

#
#
# class LoginForm(forms.Form):
#     username = forms.CharField(
#         max_length=20,
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Логин',
#             }
#         )
#     )
#     password = forms.CharField(
#         max_length=20,
#         required=True,
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Пароль',
#             }
#         )
#     )


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('nickname', 'password', 'email', 'first_name', 'last_name')

    def get_avatar(self, hash):
        """
        get random avatar from hash for new
        user
        :param hash:
        :return:
        """
        avatars.Identicon(hash).generate()

    def save_avatar_and_login(self, request, user):
        hash = stuff.avatar_generator()
        self.get_avatar(hash)
        r = open('media/tmp.png', 'rb')
        avatar = File(r)
        user.avatar.save(str(user.id) + '_avatar.png', avatar)
        os.remove('media/tmp.png')
        r.close()
        return user
        # widgets = {
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        #     'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}),
        #     'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
        # }

#
# class MakeTask(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['idea', 'body']
#         # fields.remove('creation_date')
#         # fields.append('author')
#
#
# class AddTaskForm(forms.Form):
#     idea = forms.CharField(
#         # label='Название',
#         # max_length=200,
#         # widget=forms.TextInput()
#     )
#
#     body = forms.CharField(
#         label='Опишите вашу идею здесь',
#         max_length=10000,
#         widget=forms.Textarea()
#     )
#
#
# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('nickname', 'first_name', 'last_name', 'email')
#
#     def save_avatar(self, request):
#         user = User.objects.get(username=request.user.username)
#         image =  self.cleaned_data['avatar']
#         stuff.image_preproc(image)
#         r = open('media/tmp.png', 'rb')
#         avatar = File(r)
#         path = settings.MEDIA_ROOT + '/users/'
#         os.system('rm -rf {}'.format(path + str(user.id) + '_avatar.png'))
#         user.profile.avatar.save(str(user.id) + '_avatar.png', avatar)
#         user.profile.save()
#         os.system('rm -rf {}tmp.img'.format(settings.MEDIA_ROOT))
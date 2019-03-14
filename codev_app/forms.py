from django import forms
from .models import User
from codev_app.models import *


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
        fields = ('username', 'password', 'email')
        # widgets = {
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        #     'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}),
        #     'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
        # }


class MakeTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['idea', 'body']
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


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location')

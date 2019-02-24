from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth
from codev_app.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from codev_app.models import *


def get_context(request, pagename):
    return {
        'pagename': pagename,
        'loginform': LoginForm(),
        'user': request.user,
        'registerform': RegistrationForm(request.POST)
    }


def index(request):
    return render(request, 'index.html')


def login_page(request):
    return render(request, 'login_page.html', get_context(request, 'login page'))


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу
        return redirect("/")
    else:
        # Отображение страницы с ошибкой
        return Http404

def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return redirect("/")

def register(request):
    if request.method == "POST":
        name = request.POST.get('username')
        mail = request.POST.get('mail')
        password = request.POST.get('password')
        user = User.objects.create_user(name, mail, password)
        user.save()
    return redirect("/")

def test_corner(request):
    # if request.method == "POST":
    #TODO заприватьте это дерьмо, нужны права юзеров
    # else:
    #     return Http404
    if request.method == "POST":
        form = MakeTask(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = MakeTask()
    return render(request, 'test_corner.html', {'form': form})


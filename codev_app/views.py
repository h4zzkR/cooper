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
import datetime
import modules.avatars as avatars
import modules.stuff as stuff
from django.core.files import File
import os


def get_context(request, pagename):
    context = {
        'pagename': pagename,
        'loginform': LoginForm(),
        'user': request.user,
        'registerform': RegistrationForm(request.POST)
    }
    if request.user.is_authenticated:
        context.update({'avatar': request.user.userprofile.avatar})

    return context


def index(request):
    if request.user.is_authenticated:
        context = get_context(request, 'hab')
        return render(request, 'hab.html', context)
    else:
        return render(request, 'index.html')

def get_avatar(hash):
    avatars.Identicon(hash).generate()

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
        #return random avatar from hash
        get_avatar(stuff.avatar_generator())
        r = open('media/tmp.png', 'rb')
        avatar = File(r)
        user.userprofile.avatar.save(name + '_avatar.png', avatar)
        r.close(); os.remove('media/tmp.png')
    return redirect("/")

def add_task(request):
    username = request.user.username
    context = get_context(request, 'make_task')
    if request.method == "POST":
        form = AddTaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = Task(
            idea = form.data['idea'],
            body = form.data['body'],
            creation_date = datetime.datetime.now(),
            author = request.user
            )
            task.save()
        else:
            return redirect('add_task')
    else:
        context = get_context(request, 'make_task')
        context.update({'form' : AddTaskForm()})
    return render(request, 'add_task.html', context)


def my_tasks(request):
    context = get_context(request, 'tasks')
    context.update({'tasks' : Task.objects.filter(author=request.user)})
    return render(request, 'tasks.html', context)
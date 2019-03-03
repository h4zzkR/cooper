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

def add_task(request):

    username = request.user.username

    if request.method == "POST":
        form = AddTaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = Task(
            idea = form.data['idea'],
            body = form.data['body'],
            creation_date = datetime.datetime.now(),
            author = request.user
            )

            print(form)
            task.save()
        else:
            messages.add_message(request, messages.ERROR, "Некорректные данные в форме")
            return redirect('add_task')
    else:
        form = AddTaskForm()
    return render(request, 'add_task.html', {'form': form})


def my_tasks(request):
    tasks = Task.objects.filter(author=request.user)
    return render(request, 'tasks.html', {'tasks': tasks})
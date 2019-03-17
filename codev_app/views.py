"""
Views for cooper project
"""

import datetime
import os
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.files import File
from django.contrib.auth import login as auth_login
import modules.avatars as avatars
import modules.stuff as stuff
from codev_app.forms import *
from codev_app.models import *


def get_context(request, pagename):
    """
    function for getting standart context
    :param request:
    :param pagename:
    :return:
    """
    context = {
        'pagename': pagename,
        'loginform': LoginForm(),
        'user': request.user,
        'registerform': RegistrationForm(request.POST)
    }
    if request.user.is_authenticated:
        context.update({'avatar': request.user.profile.avatar})

    return context

def hub(request):
    # context = Task.objects.all()
    context = get_context(request, 'hab')
    return context

def index(request):
    """
    main page
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        context = hub(request)
        return render(request, 'hab.html', context)
    return render(request, 'index.html')


def get_avatar(hash):
    """
    get random avatar from hash for new
    user
    :param hash:
    :return:
    """
    avatars.Identicon(hash).generate()


def login_page(request):
    """
    login page
    :param request:
    :return:
    """
    return render(request, 'login_page.html', get_context(request, 'login page'))


def login(request):
    """
    login user function
    if User is not - 404
    :param request:
    :return:
    """
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу
        return redirect("/")
        # Отображение страницы с ошибкой
    raise Http404


def logout(request):
    """
    logout func
    :param request:
    :return:
    """
    auth.logout(request)
    # Перенаправление на страницу.
    return redirect("/")


def register(request):
    """
    Register new user.
    User have name, mail, password, last-name
    and avatar, that gen randomly
    If user created, then log into
    :param request:
    :return:
    """
    if request.method == 'POST':
        name = request.POST.get('username')
        mail = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(name, mail, password)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        # return random avatar from hash
        get_avatar(stuff.avatar_generator())
        r = open('media/tmp.png', 'rb')
        avatar = File(r)
        user.profile.avatar.save(str(user.id) + '_avatar.png', avatar)
        auth_login(request, user)
        r.close()
        os.remove('media/tmp.png')
    return redirect("/")


def new_user(request):
    """
    function for render register page
    :param request:
    :return:
    """
    return render(request, 'register.html', get_context(request, 'register_page'))


def add_task(request):
    """
    Add task. Task have title (idea), body (about)
    and creation date wirh auto filling.
    All tasks have own authors.
    :param request:
    :return:
    """
    username = request.user.username
    context = get_context(request, 'make_task')
    if request.method == "POST":
        form = AddTaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = Task(
                idea=form.data['idea'],
                body=form.data['body'],
                creation_date=datetime.datetime.now(),
                author=request.user
            )
            task.save()
        else:
            return redirect('add_task')
    else:
        context = get_context(request, 'make_task')
        context.update({'form': AddTaskForm()})
    return render(request, 'add_task.html', context)


def my_tasks(request):
    """
    func for displaying all user's task
    :param request:
    :return:
    """
    context = get_context(request, 'tasks')
    tasks = Task.objects.filter(author=request.user)
    for t in range(len(tasks)):
        tasks[t].body = tasks[t].body[0:2000]
    context.update({'tasks': tasks})
    return render(request, 'tasks.html', context)


def delete_task(request, id):
    """
    delete task function
    :param request:
    :param id:
    :return:
    """
    Task.objects.filter(id=id).delete()
    context = get_context(request, 'my_tasks')
    context.update({'tasks': Task.objects.filter(author=request.user)})
    return render(request, 'tasks.html', context)


def profile(request, user):
    """
    func for displaying profile
    getting user object and avatar if request user == profile's user
    You can show as profile for current user, as profile for another user
    (without editing).
    :param request:
    :param user:
    :return:
    """
    context = get_context(request, 'profile')
    if request.user.username == user:
        context = get_context(request, 'profile')
        try:
            context.update({'user_profile': User.objects.get(username=user)})
            if context['user_profile'] != request.user:
                context.update({'pagename': 'other_profile'})
        except:
            raise Http404
    else:
        request_user = User.objects.get(username=user)
        context.update({'request_avatar': request_user.profile.avatar})
        context.update({'user_profile': request_user})
    return render(request, 'profile.html', context)


def profile_edit(request, user):
    """
    :param request:
    :param user:
    :return:
    """
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        print(user_form.is_valid(), profile_form.is_valid())
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/profile/' + user_form.data['username'])
        raise Http404
    else:
        if user == request.user.username:
            context = get_context(request, 'profile_edit')
            form = ProfileForm()
            form1 = UserForm()
            context.update({'profile_form': form, 'user_form': form1})
            return render(request, 'profile_edit.html', context)
        raise PermissionDenied


def show(request, task_id):
    """
    :param request:
    :param id:
    :return:
    """
    task = Task.objects.get(id=task_id)
    context = get_context(request, 'show_task')
    context.update({'task': task})
    if task.author == request.user.username:
        if request.method == "POST":
            task.idea = request.POST.get('idea')
            task.body = request.POST.get('body')
            task.creation_date = datetime.datetime.now()
            task.author = request.user
            task.save()
    else:
        context.update({'author': task.author.username})
    return render(request, 'show_task.html', context)
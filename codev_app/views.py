from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect, HttpResponseForbidden
from django.core.exceptions import PermissionDenied
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
        context.update({'avatar': request.user.profile.avatar})

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

def delete_task(request, id):
    #<li class="pokes">{{ p.name }} <a href="/remove/{{ p.id }}">*</a> </li>
    Task.objects.filter(id=id).delete()
    return HttpResponseRedirect("/tasks")
    context.update({'tasks': Task.objects.filter(author=request.user)})
    return render(request, 'tasks.html', context)


def profile(request, user):
    context = get_context(request, 'profile')
    try:
        context.update({'user_profile': User.objects.get(username=user)})
        if context['user_profile'] != request.user:
            context.update({'pagename': 'other_profile'})
    except:
        raise Http404
    return render(request, 'profile.html', context)


def profile_edit(request, user):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        print(user_form.is_valid(), profile_form.is_valid())
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/profile/'+user)
        else:
            raise Http404
    else:
        if user == request.user.username:
            context = get_context(request, 'profile_edit')
            form = ProfileForm()
            form1 = UserForm()
            context.update({'profile_form': form, 'user_form': form1})
            return render(request, 'profile_edit.html', context)
        else:
            raise PermissionDenied

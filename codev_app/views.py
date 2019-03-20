"""
Views for cooper project
"""

import datetime
import os
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.files import File
from django.contrib.auth import login as auth_login
from django.shortcuts import render_to_response
import modules.avatars as avatars
from codev_app.forms import *
from codev_app.models import *
from django.contrib.auth.tokens import default_token_generator
# from codev_app.models import User
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password


def get_context(request, pagename):
    """
    function for getting standart context
    :param request:
    :param pagename:
    :return:r
    """
    context = {
        'pagename': pagename,
        # 'loginform': LoginForm(),
        'user': request.user,
        'registerform': RegistrationForm(request.POST)
    }
    if request.user.is_authenticated:
        context.update({'avatar': request.user.avatar})

    return context


@login_required
def hab(request):
    tasks = Task.objects.filter(~Q(author = request.user))
    print(tasks)
    context = get_context(request, 'hab')
    context.update({'tasks': tasks})
    return context


def index(request):
    """
    main page
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        context = get_context(request, 'index')
        context = hab(request)
        print(context['tasks'])
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
    #print(User.objects.get(nickname='m0r0zk01').password)
    return render(request, 'login_page.html', get_context(request, 'login page'))

def login(request):
    """
    login user function
    if User is not - 404
    :param request:
    :return:
    """
    print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(nickname=username, password=password)
    if user is not None:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу
        return redirect("/")
        # Отображение страницы с ошибкой
    elif user is None:
        context = get_context(request, 'one_more')
        return redirect("/u/login_page")
    raise Http404



@login_required
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
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        user = User.objects.create_user(nick=name, email=mail, password=password, first_name=first_name, last_name=last_name)
        # return random avatar from hash
        get_avatar(stuff.avatar_generator())
        r = open('media/tmp.png', 'rb')
        avatar = File(r)
        user.avatar.save(str(user.id) + '_avatar.png', avatar)
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



@login_required
def add_task(request):
    """
    Add task. Task have title (idea), body (about)
    and creation date wirh auto filling.
    All tasks have own authors.
    :param request:
    :return:
    """
    username = request.user.nickname
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


@login_required
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
    context.update({'tasks': tasks, 'len':len(tasks)})
    return render(request, 'tasks.html', context)

@login_required
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


@login_required
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
    if request.user.nickname == user:
        context = get_context(request, 'profile')
        try:
            context.update({'user_profile': User.objects.get(nickname=user)})
            if context['user_profile'] != request.user:
                context.update({'pagename': 'other_profile'})
        except:
            raise Http404
    else:
        request_user = User.objects.get(nickname=user)
        context.update({'request_avatar': request.user.profile.avatar})
        context.update({'user_profile': request_user})
    return render(request, 'profile.html', context)


@login_required
def profile_edit(request, user):
    """
    :param request:
    :param user:
    :return:
    """
    context = get_context(request, 'profile_edit')
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        print(user_form.is_valid())
        print(user_form.errors)
        if user_form.is_valid():
            # os.system()
            user_form.save()
            # user_form.save_avatar(request)
            return redirect('/profile/' + user_form.data['nickname'])
        raise Http404
    else:
        if user == request.user.nickname:
            form1 = UserEditForm()
            context.update({'user_form': form1})
            return render(request, 'profile_edit.html', context)
        raise PermissionDenied
    #return render(request, 'profile_edit.html', context)

@login_required
def show(request, task_id):
    """
    :param request:
    :param id:
    :return:
    """
    task = Task.objects.get(id=task_id)
    context = get_context(request, 'show_task')
    context.update({'task': task})
    if task.author == request.user.nickname:
        if request.method == "POST":
            task.idea = request.POST.get('idea')
            task.body = request.POST.get('body')
            task.creation_date = datetime.datetime.now()
            task.author = request.user
            task.save()
    else:
        context.update({'author': task.author.nickname})
    return render(request, 'show_task.html', context)


def recover_password_page(request):
    if request.method == 'POST':
        user = User.objects.get(email=request.POST.get('email'))
        token_object = Token.objects.create(user=user)
        token = token_object.token
        data = """
            Привет, похоже вы запросили восстановление/смену пароля.\n
            Если вы этого не делали, проигнорируйте сообщение!\n
            Для восстановления пароля перейдите по ссылке:\n"""\
            + 'http://127.0.0.1:8000/u/reset/' + '?token=' + token
        send_mail('Password Recover', data, 'codev.no.reply@gmail.com', [request.POST.get('email')], fail_silently=False)
        return redirect('/awaiting')
    else:
        return render(request, 'recover_password.html')

def awaiting(request):
    return render(request, 'awaiting.html')

def new_password_token(request):
    if request.method == 'GET':
        token = request.GET.get('token')
        try:
            user = Token.objects.get(token=token)
        except:
            raise Http404
        return render(request, 'new_password.html', {'nick': user.user.nickname, 'token': user.token})

    if request.method == 'POST':
        user = Token.objects.get(token=request.GET.get('token'))
        print(user)
        model_user = User.objects.get(nickname = user.user.nickname)
        model_user.password = make_password(request.POST.get('password'), salt=None, hasher='default')
        model_user.save()
        #Delete on reset
        user.delete()
        return redirect('/')
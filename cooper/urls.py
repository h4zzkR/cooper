"""cooper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from codev_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index),
    path('u/login_page', login_page),
    path('u/login/', login),
    path('u/register/', register),
    path('u/logout/', logout),
    path('tasks', my_tasks),
    path('add_task', add_task),
    path('remove/<int:id>', delete_task),
    path('profile/<str:user>', profile),
    path('profile/edit/<str:user>', profile_edit),
    path('u/new_user', new_user),
    path('task/<int:task_id>', show),    # path('task/<int:task_id>', show),
    path('u/recover_password', recover_password_page),
    path('u/reset/', new_password_token),
    path('chats/', chats),
    path('create_chat/', create_chat),
    path('chat/<int:id>', chat),
    path('sub/<int:task_id>', subscribe),
    path('unsub/<int:task_id>', unsubscribe),
    path('awaiting', awaiting),
    path('control', admin_panel),
    path('gen_avatar', gen_avatar_prepare),
    path('subscribtions', subscriptions)
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

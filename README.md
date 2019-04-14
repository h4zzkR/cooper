# CooperationDevelopmentNetwork
Веб-приложение для поиска разработчиков для работы над проектами.
описание в процессе.

Web-app for developers searching for the working on projects.
We continue to write readme, keep in touch.

## Reqs:
- npm install simplemde --save
- pip3 install django_extensions
- pip3 install validate_email
- pip3 install py3dns
- pip3 install pillow
- pip3 install django


Инструкция по запуску проекта
1). Создаем виртуальное окружение:
    а). $ sudo apt-get install python3-venv
    б). $ python3 -m venv django_venv, где django_venv - название    виртуального окружения

2). Активируем виртуальное окружение:
    $ source django_venv/bin/activate
Примечание: для выхода из виртуального окружения venv наберите: $ deactivate

3). Обновляем pip:
    (django_venv) ~$ python3 -m pip install --upgrade pip

4). Устанавливаем Django:
    (django_venv) ~$ pip install django
Если Вы сделали всё правильно, то Вам должно высветиться:
Successfully installed django-2.1.3

5). Клонируем внешний репозиторий проекта:
    $ git clone https://github.com/m0r0zk01/cooper.git

6). Устанавливаем django-extensions:
    (django_venv) ~$ pip install django-extensions

7). Устанавливаем pillow:
    (django_venv) ~$ pip install  pillow

8). Запускаем сервер:
    (django_venv) ~$ python manage.py runserver

[Documentation(RU)](https://docs.google.com/document/d/11DQPLyEXO4wGiOjyCECmzDpbmLmXNg7N-2RFP4ph8sQ/edit?usp=sharing)
[Instruction(RU)](https://docs.google.com/document/d/1ZeIIt4ALY7MvFpI23MWpzHaIglnV7sHKuklzxL1pE88/edit?usp=sharing)

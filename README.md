# CooperationDevelopmentNetwork
Веб-приложение для поиска разработчиков для работы над проектами.
Описание в процессе.

Web-app for developers searching for the working on projects.
We continue to write readme, keep in touch.


<h2>Инструкция по запуску проекта</h2>

1). Создаем виртуальное окружение:<br>
    а). `$ sudo apt-get install python3-venv`<br>
    б). `$ python3 -m venv django_venv`, где django_venv - название виртуального окружения

2). Активируем виртуальное окружение:<br>
    `$ source django_venv/bin/activate`<br>
Примечание: для выхода из виртуального окружения venv наберите: `$ deactivate`

3). Обновляем pip:<br>
    `(django_venv) ~$ python3 -m pip install --upgrade pip`

4). Устанавливаем Django:<br>
    `(django_venv) ~$ pip install django`<br>
Если Вы сделали всё правильно, то Вам должно высветиться:<br>
*Successfully installed django-2.1.3*

5). Клонируем внешний репозиторий проекта:<br>
    `$ git clone https://github.com/m0r0zk01/cooper.git`

6). Устанавливаем django-extensions:<br>
    `(django_venv) ~$ pip install django-extensions`

7). Устанавливаем pillow:<br>
    `(django_venv) ~$ pip install  pillow`

8). Устанавливаем validate_email:<br>
    `(django_venv) ~$ pip install validate_email`

9). Устанавливаем DNS-библиотеку Python 3: <br>
    `(django_venv) ~$ pip install py3dns`

10). Устанавливаем SimpleMDE:<br>
    `(django_venv) ~$ npm install simplemde --save`

11). Запускаем сервер:<br>
    `(django_venv) ~$ python manage.py runserver`


[Documentation(RU)](https://docs.google.com/document/d/11DQPLyEXO4wGiOjyCECmzDpbmLmXNg7N-2RFP4ph8sQ/edit?usp=sharing)

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

4). Устанавливаем все необходимые библиотеки:<br>
    `pip3 install -r requirements.txt`<br>

5). Клонируем внешний репозиторий проекта:<br>
    `$ git clone https://github.com/m0r0zk01/cooper.git`

6). Запускаем сервер:<br>
    `(django_venv) ~$ python manage.py runserver`


[Documentation(RU)](https://docs.google.com/document/d/11DQPLyEXO4wGiOjyCECmzDpbmLmXNg7N-2RFP4ph8sQ/edit?usp=sharing)<br>
[Instruction(RU)](https://docs.google.com/document/d/15N0qXsD3UGp7n-QGkrbwM8OwvEICX4U3ac61v1lfGPs/edit?usp=sharing)

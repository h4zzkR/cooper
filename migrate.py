"""
Script for full clean migration
"""
import os

print('Cleaning...')
os.system('rm -rf /codev_app/migrations')
os.system('rm -rf /codev_app/__pycache__')
os.system('rm -rf /cooper/__pycache__')
os.system('rm -rf media/users/avatars')
os.system('rm db.sqlite3')
print('Make zero migrations...')
os.system('source venv/bin/activate')
os.system('python manage.py migrate admin zero')
os.system('python manage.py migrate auth zero')
os.system('python manage.py migrate contenttypes zero')
os.system('python manage.py migrate sessions zero')
os.system('python manage.py makemigrations codev_app')
os.system('python manage.py migrate codev_app')
os.system('python manage.py migrate')
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')
os.system('python manage.py create_super_template')
print("That's all!")

from django.core.management.base import BaseCommand, CommandError
from codev_app.models import User
from codev_app.views import create_user

class Command(BaseCommand):

    def handle(self, *args, **options):

        # mail, password, name, first_name, last_name = options['mail'], \
        #                                               options['password'], options['name'], 'admin', 'admin'
        name = input('Name: '); mail = input('Email: '); password = input('Password: ')
        create_user(name=name, mail=mail, password=password, is_super=True)
        self.stdout.write(self.style.SUCCESS('Superuser created'))
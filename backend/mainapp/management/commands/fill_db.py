import json
import os
from django.contrib.auth.models import Group, Permission
from django.core.management import call_command
from django.core.management.base import BaseCommand
from authapp.models import User
from houseapp.models import PartString
from mainapp.models import MenuItem


def load_from_json(file_name):
    try:
        with open(file_name, mode='r', encoding='utf-8') as infile:
            return json.load(infile)
    except UnicodeDecodeError:
        with open(file_name, mode='r', encoding='windows-1251') as infile:
            return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command('makemigrations')
        call_command('migrate')
        try:
            user = User.objects.create_superuser(username=os.getenv('SUPER_USER_USERNAME'),
                                                 password=os.getenv('SUPER_USER_PASSWORD'),
                                                 birth="1991-08-14")
            family_group = Group.objects.create(name='Family')
            for u in ['testuser', 'familyuser']:
                userfortest = User.objects.create(username=u, password=u, birth='2000-01-01')
                userfortest.set_password(u)
                userfortest.save()
                family_group.user_set.add(userfortest)

            for name in ['houseapp']:
                filename = f'{os.getcwd()}/{name}/fixtures/{name}.json'
                try:
                    call_command('loaddata', filename, app_label=name)
                except Exception as e:
                    print(e)
            PartString.objects.create(name='passuser', body=os.getenv('PASS_USER'))

            MenuItem.objects.create(name='Умный дом', link='/home')

            for perm, model_name in [('change', 'user'), ('view', 'user'), ('view', 'nodemcu')]:
                family_group.permissions.add(Permission.objects.get(codename=f'{perm}_{model_name}'))

        except Exception as e:
            print(f'fill_db Error: {e}')

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

import os

class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username=os.environ.get["PG_USERNAME"],
                password=os.environ.get["PG_PASSWORD"],
            )
        print('Superuser has been created.')
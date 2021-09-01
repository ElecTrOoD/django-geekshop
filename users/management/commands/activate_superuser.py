from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.get(pk=1)
        if user:
            user.is_active = True
            user.save()
            print(f'User: {user.username} activated')

from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Создает группу модераторов с правами публикации и удаления продукта'

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='Moderators')

        unpublish_perm = Permission.objects.get(codename='can_unpublish_product')
        delete_perm = Permission.objects.get(codename='delete_product')

        group.permissions.add(unpublish_perm, delete_perm)

from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add test products to the db'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        category, _ = Category.objects.get_or_create(name='Тестовая категория 1')

        products = [
            {'name': 'Тестовый продукт 1', 'price': 100, 'category': category},
            {'name': 'Тестовый продукт 2', 'price': 200, 'category': category},
            {'name': 'Тестовый продукт 3', 'price': 300, 'category': category},
        ]

        for product_data in products:
            product = Product.objects.create(**product_data)
            self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))

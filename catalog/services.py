from django.shortcuts import get_object_or_404

from catalog.models import Product, Category


class ProductService:
    @staticmethod
    def get_products_by_category(category_id):
        """
        Сервисная функция для получения продуктов по выбранной категории
        """
        category = get_object_or_404(Category, id=category_id)

        return Product.objects.filter(category=category)

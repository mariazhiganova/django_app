from django.db import models
from django.db.models import DateTimeField, ForeignKey, CharField, BooleanField

from config import settings


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.CharField(max_length=300, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']


class Product(models.Model):
    name = CharField(max_length=200, verbose_name='Наименование')
    description = models.CharField(max_length=300, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/images/', blank=True, verbose_name='Изображение')
    category = ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField(verbose_name='Цена')
    created_at = DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')
    is_publicate = BooleanField(verbose_name='Опубликовать', default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец продукта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name', 'price', 'created_at']
        permissions = [('can_unpublish_product', 'Can unpublish product')]

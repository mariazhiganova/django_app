from django.db import models
from django.db.models import DateTimeField, BooleanField
from django.db.models.fields import PositiveIntegerField


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/images/', blank=True, verbose_name='Изображение')
    created_at = DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_publicate = BooleanField(verbose_name='Опубликовать', default=False)
    views_counter = PositiveIntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['title', 'is_publicate', 'created_at', 'views_counter']

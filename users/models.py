from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, help_text='Введите номер телефона')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name='Страна',
                               help_text='Введите название вашей страны')
    username = models.CharField(max_length=150, blank=True, null=True, unique=False, default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser


@admin.register(CustomUser)
class CategoryAdmin(UserAdmin):
    list_display = ('email', 'phone_number', 'avatar', 'country', 'first_name', 'last_name')
    list_filter = ('email', 'country', 'last_name')
    search_fields = ('email', 'last_name')

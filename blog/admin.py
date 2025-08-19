from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'views_counter')
    list_filter = ('title', 'views_counter')
    search_fields = ('title', 'content')

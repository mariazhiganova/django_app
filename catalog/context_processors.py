from .models import Category


def categories(request):
    """
    Функция для добавления в контекст основного меню контекстной переменной со всеми категориями
    """
    return {
        'categories': Category.objects.all()
    }

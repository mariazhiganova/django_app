from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, ArticleDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('home/', ArticleListView.as_view(), name='home'),  # /blog/
    path('create/article/', ArticleCreateView.as_view(), name='add_article'),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='update_article'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='delete_article'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='detail_article'),
]

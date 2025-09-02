from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from blog.models import Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'content', 'preview', 'is_publicate']
    template_name = 'add_article.html'
    success_url = reverse_lazy('blog:home')


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_publicate=True)

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'content', 'preview', 'is_publicate']
    template_name = 'add_article.html'

    def get_success_url(self):
        return reverse_lazy('blog:detail_article', kwargs={'pk': self.object.pk})


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:home')
    template_name = 'article_confirm_delete.html'

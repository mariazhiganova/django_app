from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView

from catalog.forms import ProductForm, ProductModeratorsForm
from catalog.models import Product, Category
from catalog.services import ProductService


class ProductListView(ListView):
    model = Product
    template_name = 'main.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = cache.get('cached_product_list')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('cached_product_list', queryset, 60 * 15)

        return queryset


class ContactView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):
        user_message = request.POST.get('message')
        context = self.get_context_data()
        context['message_sent'] = True
        context['user_message'] = user_message
        return self.render_to_response(context)


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        can_edit = (obj.owner == self.request.user or
                    self.request.user.has_perm('catalog.can_unpublish_product') or
                    self.request.user.is_superuser)

        if not can_edit:
            raise PermissionDenied('Вы не можете редактировать этот продукт')

        return obj

    def get_form_class(self):
        if self.request.user == self.object.owner or self.request.user.is_superuser:
            return ProductForm

        if self.request.user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorsForm

        raise PermissionDenied

    def get_success_url(self):
        return reverse_lazy('catalog:details', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')
    context_object_name = 'product'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        can_edit = (obj.owner == self.request.user or
                    self.request.user.has_perm('catalog.delete_product') or
                    self.request.user.is_superuser)

        if not can_edit:
            raise PermissionDenied('Вы не можете удалить этот продукт')

        return obj


class ProductsByCategoryView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products_by_category_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        cache_key = f'products_category_{category_id}'

        products_list = cache.get(cache_key)

        if not products_list:
            products_list = ProductService.get_products_by_category(category_id)
            cache.set(cache_key, products_list, 60 * 15)

        return products_list

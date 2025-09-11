from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView

from catalog.forms import ProductForm, ProductModeratorsForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'main.html'
    context_object_name = 'products'


class ContactView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):
        user_message = request.POST.get('message')
        context = self.get_context_data()
        context['message_sent'] = True
        context['user_message'] = user_message
        return self.render_to_response(context)


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


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.delete_product'
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')
    context_object_name = 'product'

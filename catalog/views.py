from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView

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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'image', 'category', 'price']
    template_name = 'add_product.html'
    success_url = reverse_lazy('catalog:product_list')

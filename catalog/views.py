from django.shortcuts import render, get_object_or_404, redirect

from catalog.forms import ProductForm
from catalog.models import Product


def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')

def products_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'home.html', context)

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product_details.html', context)

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
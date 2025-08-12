from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, products_list, product_details, add_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', products_list, name='product_list'),  # /catalog/
    path('contacts/', contacts, name='contacts'),
    path('details/<int:pk>/', product_details, name='details'),
    path('products/add/', add_product, name='add_product'),
]

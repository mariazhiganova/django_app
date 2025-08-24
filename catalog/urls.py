from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ContactView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),  # /catalog/
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('details/<int:pk>/', ProductDetailView.as_view(), name='details'),
    path('products/add/', ProductCreateView.as_view(), name='add_product'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='update_product'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='delete_product'),
]

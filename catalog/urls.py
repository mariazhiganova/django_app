from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ContactView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),  # /catalog/
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('details/<int:pk>/', ProductDetailView.as_view(), name='details'),
    path('products/add/', ProductCreateView.as_view(), name='add_product'),
]

import os

from django.contrib import admin
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.urls import path, include

from config import settings
from config.settings import BASE_DIR

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('/catalog/')),
    path('catalog/', include('catalog.urls', namespace='catalog'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(BASE_DIR, 'static'))

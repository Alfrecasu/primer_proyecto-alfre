from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name = 'inicio'),
    path("contacto/", contacto, name= 'contacto'),
    path("usuarios/", include('apps.usuarios.urls')),
    path("discos/", include('apps.discos.urls')),
    path("opiniones/", include('apps.opiniones.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
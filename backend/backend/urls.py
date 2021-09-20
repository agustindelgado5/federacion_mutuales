from django.contrib import admin
from django.urls import path, re_path, include


urlpatterns = [
<<<<<<< HEAD
    path("admin/", admin.site.urls),
    # re_path("", include("users.urls")),
    path("", include("Socios.urls")),
    path("", include("Farmacias.urls")),
    path("", include("Profesionales.urls")),
    path("", include("Medicamentos.urls")),
    path("", include("Ordenes.urls")),
    path("", include("Mutuales.urls")),
    path("", include("Cuotas.urls")),
=======
    path('admin/', admin.site.urls),
    path('',include('Farmacias.urls')),
    path('', include('Profesionales.urls')),
    path('',include('Medicamentos.urls')),
    path('', include('Administracion.urls')),
    path('',include('Socios.urls')),
    path('',include('Ordenes.urls')),
    path('',include('Mutuales.urls')),
    path('',include('Cobradores.urls')),
    path('',include('Cuotas.urls')),
    # path('profesional/',include('Profesionales.urls')),
    # path('medicamento/',include('Medicamentos.urls')),
>>>>>>> 22136aa83e79bce7ac841c370c6af768e1d784f5
]

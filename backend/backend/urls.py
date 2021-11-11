from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),
    # re_path("", include("users.urls")),
    path("", include("Socios.urls")),
    path("", include("Farmacias.urls")),
    path("", include("Profesionales.urls")),
    path("", include("Medicamentos.urls")),
    path("", include("Ordenes.urls")),
    path("", include("Mutuales.urls")),
    path("", include("Cuotas.urls")),
    path("", include("Cobradores.urls")),
    path("", include("Estudios.urls")),
    path("", include("GastosSalientes.urls")),
    path("", include("Cirugias.urls")),
    path("", include("Institutos.urls")),
    path("", include("Lentes.urls")),
    path("", include("VentasOpticas.urls")),
]

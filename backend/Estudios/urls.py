from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"proveedor_estudios", views.ProveedorViewSet, basename="proveedor_estudios")
router.register(r"estudios", views.EstudiosViewSet, basename="estudios")
router.register(r"estudios_socios", views.EstudiosSociosViewSet, basename="estudios_socios")

urlpatterns = [
    path("", include(router.urls)),
]

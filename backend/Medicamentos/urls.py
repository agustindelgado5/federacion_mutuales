from django.urls import path, include
from . import views

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"medicamentos", views.MedicamentosViewSet, basename="medicamentos")
router.register(r"recetas", views.RecetasViewSet, basename="recetas")

urlpatterns = [
    path("", include(router.urls)),
]

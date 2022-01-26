from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"institutos", views.InstitutosViewSet, basename="institutos")
router.register(r"institutos_profesional", views.InstitutosProfesionalesViewSet, basename="consultorios")

urlpatterns = [
    path("", include(router.urls)),
]

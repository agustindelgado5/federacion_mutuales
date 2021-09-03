from django.urls import path, include
from . import views


from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"cobradores", views.CobradoresViewSet, basename="cobradores")

urlpatterns = [
    path("", include(router.urls)),
]

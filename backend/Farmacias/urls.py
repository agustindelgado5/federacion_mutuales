from django.urls import path, include
from . import views


from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"farmacias", views.FarmaciasViewSet, basename="farmacias")

urlpatterns = [
    path("", include(router.urls)),
]

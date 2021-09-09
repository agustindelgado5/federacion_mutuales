from django.urls import path, include
from . import views


from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"socios", views.SociosViewSet, basename="socios")
router.register(r"familiar", views.FamiliarViewSet, basename="familiar")

urlpatterns = [
    path("", include(router.urls)),
]

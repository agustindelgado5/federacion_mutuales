from django.urls import path, include
from . import views


from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"mutuales", views.MutualesViewSet, basename="mutuales")

urlpatterns = [
    path("", include(router.urls)),
]

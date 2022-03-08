from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"cristales", views.CristalesViewSet, basename="cristales")

urlpatterns = [
    path("", include(router.urls)),
]

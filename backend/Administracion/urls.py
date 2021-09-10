# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from Administracion import views

router = DefaultRouter()
router.register(r'login', views.LoginView, basename='login')
router.register(r'logout', views.LogoutView, basename='logout')
router.register(r'alta', views.SignupView, basename='alta')

urlpatterns = [
    path('', include(router.urls))
]
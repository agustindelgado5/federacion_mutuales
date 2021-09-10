# Django
from django.urls import include, path

# Django REST Framework
#from rest_framework.routers import DefaultRouter

# Views
#from Administracion import views
from .views import *


#router = DefaultRouter()
#router.register(r'login', views.LoginView, basename='login')
#router.register(r'logout', views.LogoutView, basename='logout')
#router.register(r'alta', views.SignupView, basename='alta')
"""
urlpatterns = [
    path('', include(router.urls))
]
"""
urlpatterns = [
    # Auth views
    path('auth/login/',LoginView.as_view(), name='login'),
    path('auth/logout/',LogoutView.as_view(), name='logout'),
    path('auth/alta/',SignupView.as_view(), name='alta'),
]
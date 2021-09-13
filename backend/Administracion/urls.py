# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.authtoken import views

# Views
from .views import *

urlpatterns = [
    # Auth views
    path('auth/login/',LoginView.as_view(), name='login'),
    path('auth/logout/',LogoutView.as_view(), name='logout'),
    path('auth/alta/',SignupView.as_view(), name='alta'),
    path('token/',views.obtain_auth_token),
]
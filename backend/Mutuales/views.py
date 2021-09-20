from rest_framework import viewsets
from django.contrib.auth.mixins import PermissionRequiredMixin

# from rest_framework.decorators import action
# from rest_framework.response import Response

from Mutuales.models import mutuales, servicios
from Mutuales.serializers import MutualesSerializer, ServiciosSerializer

# from django.contrib.auth.models import User


class ServiciosViewSet(viewsets.ModelViewSet):
    queryset = servicios.objects.all()
    serializer_class = ServiciosSerializer
<<<<<<< HEAD
=======
    permission_required = (
    #    'Servicios.view_servicios',
    #    'Servicios.add_servicios',
    #    'Servicios.change_servicios',
    #    'Servicios.delete_servicios',
    )
    #login_url = '/auth/login/'
    #redirect_field_name = 'redirect_to'
>>>>>>> 22136aa83e79bce7ac841c370c6af768e1d784f5


class MutualesViewSet(viewsets.ModelViewSet):
    serializer_class = MutualesSerializer
    queryset = mutuales.objects.all()
<<<<<<< HEAD
=======
    permission_required = (
    #    'Mutuales.view_mutuales',
    #    'Mutuales.add_mutuales',
    #    'Mutuales.change_mutuales',
    #    'Mutuales.delete_mutuales',
    )
    #login_url = '/auth/login/'
    #redirect_field_name = 'redirect_to'

    
>>>>>>> 22136aa83e79bce7ac841c370c6af768e1d784f5

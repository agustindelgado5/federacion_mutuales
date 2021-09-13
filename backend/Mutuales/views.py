from rest_framework import  viewsets
from django.contrib.auth.mixins import PermissionRequiredMixin
#from rest_framework.decorators import action
#from rest_framework.response import Response

from Mutuales.models import mutuales, servicios
from Mutuales.serializers import  MutualesSerializer, ServiciosSerializer
#from django.contrib.auth.models import User


class ServiciosViewSet(PermissionRequiredMixin,viewsets.ModelViewSet):
    queryset = servicios.objects.all()
    serializer_class = ServiciosSerializer
    permission_required = (
        'Servicios.view_servicios',
        'Servicios.add_servicios',
        'Servicios.change_servicios',
        'Servicios.delete_servicios',
    )
    login_url = '/auth/login/'
    redirect_field_name = 'redirect_to'



class MutualesViewSet(PermissionRequiredMixin,viewsets.ModelViewSet):
    serializer_class = MutualesSerializer
    queryset = mutuales.objects.all()
    permission_required = (
        'Mutuales.view_mutuales',
        'Mutuales.add_mutuales',
        'Mutuales.change_mutuales',
        'Mutuales.delete_mutuales',
    )
    login_url = '/auth/login/'
    redirect_field_name = 'redirect_to'

    
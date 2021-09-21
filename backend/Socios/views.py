from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from .utils import calcular_edad
from datetime import datetime
from Socios.models import socios, familiar
from Socios.serializers import SociosSerializer, FamiliarSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from Cuotas.models import cuotas
from Cuotas.serializers import CuotasSerializer
from rest_framework.test import APIRequestFactory

class SociosViewSet(viewsets.ModelViewSet):
    serializer_class = SociosSerializer
    queryset = socios.objects.all()
    @action(methods=['GET'], detail = True)
    def aldia(self, request, pk=None):
        ultimopagado1 = cuotas.objects.filter(numero_socio = pk).order_by('fecharealizacion').last()
        if(ultimopagado1 == None):
            return Response(-1)
        else:
            ultimopagado = ultimopagado1.fecharealizacion
        a = datetime.now().date()
        date = ultimopagado.date()
        diff = a - date
        return Response(diff.days)

    permission_required = (
    #    'Socios.view_socios',
    #    'Socios.add_socios',
    #    'Socios.change_socios',
    #    'Socios.delete_socios',
    )
    #login_url = '/auth/login/'
    #redirect_field_name = 'redirect_to'
    """
    def perform_create(self, serializers):
        _edad = calcular_edad(datetime.strptime(self.request.POST['fecha_nacimiento'],'%Y-%m-%d'))
        serializers.save(edad=_edad)
        
    def perform_update(self, serializers):
        _edad = calcular_edad(datetime.strptime(self.request.POST['fecha_nacimiento'],'%Y-%m-%d'))
        serializers.save(edad=_edad)
    """


class FamiliarViewSet(viewsets.ModelViewSet):
    serializer_class = FamiliarSerializer
    queryset = familiar.objects.all()

    # permission_required = (
    #     'Socios.view_familiar',
    #     'Socios.add_familiar',
    #     'Socios.change_familiar',
    #     'Socios.delete_familiar',
    # )
    # login_url = '/auth/login/'
    # redirect_field_name = 'redirect_to'

    """
    def perform_create(self, serializers):
        _edad = calcular_edad(datetime.strptime(self.request.POST['fecha_nacimiento'],'%Y-%m-%d'))
        serializers.save(edad=_edad)
        
    def perform_update(self, serializers):
        _edad = calcular_edad(datetime.strptime(self.request.POST['fecha_nacimiento'],'%Y-%m-%d'))
        serializers.save(edad=_edad)
    """

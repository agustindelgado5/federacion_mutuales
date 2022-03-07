from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from .utils import calcular_edad
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from Socios.models import socios, familiar
from Socios.serializers import SociosSerializer, FamiliarSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from Cuotas.models import cuotas
from Cuotas.serializers import CuotasSerializer
from rest_framework.test import APIRequestFactory
from django.db.models import Avg,Window,F,Count,OuterRef,Sum,FloatField,Q,Subquery

class SociosViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    # queryset = socios.objects.all()
    serializer_class = SociosSerializer

    def get_queryset(self):
        queryset2 = cuotas.objects.filter(pagado=False).values("numero_socio").annotate(m=Sum('monto'))
        queryset = socios.objects\
        .annotate(monto=Subquery(queryset2.filter(numero_socio=OuterRef('numero_socio')).values('m')))\
        .order_by()
        print("cuotas: ",*queryset,sep='\n')

        cobrador = self.request.query_params.get('cobrador')
        cobrador2 = self.request.query_params
        print("Cobrador: ",cobrador2)
        if cobrador is not None:
            queryset = queryset.filter(cobrador=cobrador)
        return queryset
    
    @action(methods=['GET'], detail = True)
    def aldia(self, request, pk=None):
        ultimopagado1 = cuotas.objects.filter(numero_socio = pk).filter(pagado=True).order_by('fecharealizacion').last()
        if(ultimopagado1 == None):
            return Response(-1)
        else:
            ultimopagado = ultimopagado1.fecharealizacion
        a = datetime.now().date()
        date = ultimopagado
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
"""
class ServiciosSocioViewSet(viewsets.ModelViewSet):
    serializer_class = ServiciosSociosSerializer
    queryset = servicio_socio.objects.all()
"""
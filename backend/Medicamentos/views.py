from rest_framework import  viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Medicamentos.models import medicamentos,receta
from Medicamentos.serializers import MedicamentosSerializer, RecetasSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin


class MedicamentosViewSet(PermissionRequiredMixin,viewsets.ModelViewSet):
    serializer_class = MedicamentosSerializer
    queryset = medicamentos.objects.all()
    permission_required = (
        'Medicamentos.view_medicamentos',
        'Medicamentos.add_medicamentos',
        'Medicamentos.change_medicamentos',
        'Medicamentos.delete_medicamentos',
    )
    login_url = '/auth/login/'
    redirect_field_name = 'redirect_to'



class RecetasViewSet(PermissionRequiredMixin,viewsets.ModelViewSet):
    serializer_class = RecetasSerializer
    queryset = receta.objects.all()
    permission_required = (
        'Medicamentos.view_recetas',
        'Medicamentos.add_recetas',
        'Medicamentos.change_recetas',
        'Medicamentos.delete_recetas',
    )
    #login_url = '/auth/login/'
    #redirect_field_name = 'redirect_to'



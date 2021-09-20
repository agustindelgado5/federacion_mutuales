from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Medicamentos.models import medicamentos, receta
from Medicamentos.serializers import MedicamentosSerializer, RecetasSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin


class MedicamentosViewSet(viewsets.ModelViewSet):
    serializer_class = MedicamentosSerializer
    queryset = medicamentos.objects.all()


class RecetasViewSet(viewsets.ModelViewSet):
    serializer_class = RecetasSerializer
    queryset = receta.objects.all()

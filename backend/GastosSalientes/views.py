from rest_framework import viewsets

from GastosSalientes.models import gastosSalientes
from GastosSalientes.serializers import GastosSalientesSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin


class GastosSalientesViewSet(viewsets.ModelViewSet):
    serializer_class = GastosSalientesSerializer
    queryset = gastosSalientes.objects.all()

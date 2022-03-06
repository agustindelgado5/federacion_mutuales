from rest_framework import viewsets

from PagadoProfesionales.models import pagadoProfesionales
from PagadoProfesionales.serializers import PagadoProfesionalesSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin


class PagadoProfesionalesViewSet(viewsets.ModelViewSet):
    serializer_class = PagadoProfesionalesSerializer
    queryset = pagadoProfesionales.objects.all()

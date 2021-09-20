from rest_framework import viewsets

from Cobradores.models import cobradores
from Cobradores.serializers import CobradoresSerializer

# Create your views here.


class CobradoresViewSet(viewsets.ModelViewSet):
    serializer_class = CobradoresSerializer
    queryset = cobradores.objects.all()


# from django.shortcuts import render

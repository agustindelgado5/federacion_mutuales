from rest_framework import viewsets

from VentasOpticas.models import ventasOpticas
from VentasOpticas.serializers import VentasOpticasSerializer

# Create your views here.


class VentasOpticasViewSet(viewsets.ModelViewSet):
    serializer_class = VentasOpticasSerializer
    queryset = ventasOpticas.objects.all()


# from django.shortcuts import render

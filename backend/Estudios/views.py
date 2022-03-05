from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Estudios.models import estudios, estudio_socio, proveedor
from Estudios.serializers import EstudiosSerializer, EstudiosSociosSerializer, ProveedorSerializer

# Create your views here.

class ProveedorViewSet(viewsets.ModelViewSet):
    serializer_class = ProveedorSerializer
    queryset = proveedor.objects.all()



class EstudiosViewSet(viewsets.ModelViewSet):
    serializer_class = EstudiosSerializer
    queryset = estudios.objects.all()


class EstudiosSociosViewSet(viewsets.ModelViewSet):
    serializer_class = EstudiosSociosSerializer
    queryset = estudio_socio.objects.all()

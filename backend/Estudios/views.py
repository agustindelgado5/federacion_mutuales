from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Estudios.models import estudios
from Estudios.serializers import EstudiosSerializer

# Create your views here.


class EstudiosViewSet(viewsets.ModelViewSet):
    serializer_class = EstudiosSerializer
    queryset = estudios.objects.all()

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Institutos.models import institutos, institutos_profesionales
from Institutos.serializers import InstitutosSerializer, InstitutosProfesionalesSerializer

# Create your views here.


class InstitutosViewSet(viewsets.ModelViewSet):
    serializer_class = InstitutosSerializer
    queryset = institutos.objects.all()


class InstitutosProfesionalesViewSet(viewsets.ModelViewSet):
    serializer_class = InstitutosProfesionalesSerializer
    queryset = institutos_profesionales.objects.all()



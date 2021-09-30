from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Institutos.models import institutos
from Institutos.serializers import InstitutosSerializer

# Create your views here.


class InstitutosViewSet(viewsets.ModelViewSet):
    serializer_class = InstitutosSerializer
    queryset = institutos.objects.all()

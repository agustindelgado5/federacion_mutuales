from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Lentes.models import lentes
from Lentes.serializers import LentesSerializer

# Create your views here.


class LentesViewSet(viewsets.ModelViewSet):
    serializer_class = LentesSerializer
    queryset = lentes.objects.all()

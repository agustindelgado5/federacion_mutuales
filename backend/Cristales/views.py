from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Cristales.models import cristales
from Cristales.serializers import CristalesSerializer

# Create your views here.


class CristalesViewSet(viewsets.ModelViewSet):
    serializer_class = CristalesSerializer
    queryset = cristales.objects.all()

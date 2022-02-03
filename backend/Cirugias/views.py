from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Cirugias.models import cirugias
from Cirugias.serializers import CirugiasSerializer

# Create your views here.


class CirugiasViewSet(viewsets.ModelViewSet):
    serializer_class = CirugiasSerializer
    queryset = cirugias.objects.all()
    
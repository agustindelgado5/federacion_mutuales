from django.shortcuts import render
from rest_framework import  viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Ordenes.models import ordenes
from Ordenes.serializers import OrdenesSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin


# Create your views here.

class OrdenesViewSet(viewsets.ModelViewSet):
    serializer_class = OrdenesSerializer
    queryset = ordenes.objects.all()
    #login_url = '/auth/login/'
    #redirect_field_name = 'redirect_to'




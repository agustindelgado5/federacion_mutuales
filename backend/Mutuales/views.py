from rest_framework import  viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Mutuales.models import mutuales
from Mutuales.serializers import MutualesSerializer


class MutualesViewSet(viewsets.ModelViewSet):
    serializer_class = MutualesSerializer
    queryset = mutuales.objects.all()
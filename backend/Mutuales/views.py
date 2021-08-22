from rest_framework import  viewsets
#from rest_framework.decorators import action
#from rest_framework.response import Response

from Mutuales.models import mutuales, servicios
from Mutuales.serializers import MutualesSerializer, ServiciosSerializer


class ServiciosViewSet(viewsets.ModelViewSet):
    serializer_class = ServiciosSerializer
    queryset = servicios.objects.all()


class MutualesViewSet(viewsets.ModelViewSet):
    serializer_class = MutualesSerializer
    queryset = mutuales.objects.all()
    
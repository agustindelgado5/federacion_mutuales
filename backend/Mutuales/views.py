from rest_framework import  viewsets
#from rest_framework.decorators import action
#from rest_framework.response import Response

from Mutuales.models import mutuales, servicios
from Mutuales.serializers import ServiciosSerializer, MutualesSerializer


class ServiciosViewSet(viewsets.ModelViewSet):
    queryset = servicios.objects.all()
    serializer_class = ServiciosSerializer
    


class MutualesViewSet(viewsets.ModelViewSet):
    serializer_class = MutualesSerializer
    queryset = mutuales.objects.all()
    
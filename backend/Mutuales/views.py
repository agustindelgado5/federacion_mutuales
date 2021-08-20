from rest_framework import viewsets

from Mutuales.models import mutuales
from Mutuales.serializers import MutualesSerializer


class MutualesViewSet(viewsets.ModelViewSet):
    serializer_class = MutualesSerializer
    queryset = mutuales.objects.all()

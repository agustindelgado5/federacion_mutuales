from rest_framework import viewsets

from .models import vendedores
from .serializers import VendedoresSerializer


class VendedoresViewSet(viewsets.ModelViewSet):
    serializer_class = VendedoresSerializer
    queryset = vendedores.objects.all()

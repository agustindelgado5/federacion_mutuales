from rest_framework import viewsets

from Farmacias.models import farmacias
from Farmacias.serializers import FarmaciasSerializer


class FarmaciasViewSet(viewsets.ModelViewSet):
    serializer_class = FarmaciasSerializer
    queryset = farmacias.objects.all()

from rest_framework import viewsets


from Socios.models import socios, familiar
from Socios.serializers import SociosSerializer, FamiliarSerializer


class SociosViewSet(viewsets.ModelViewSet):
    serializer_class = SociosSerializer
    queryset = socios.objects.all()


class FamiliarViewSet(viewsets.ModelViewSet):
    serializer_class = FamiliarSerializer
    queryset = familiar.objects.all()

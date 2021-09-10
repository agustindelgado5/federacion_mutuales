from rest_framework import viewsets


from Cuotas.models import cuotas
from Cuotas.serializers import CuotasSerializer


class CuotasViewSet(viewsets.ModelViewSet):
    serializer_class = CuotasSerializer
    queryset = cuotas.objects.all()

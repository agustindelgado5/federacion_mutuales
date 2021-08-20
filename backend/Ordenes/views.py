from rest_framework import viewsets


from Ordenes.models import ordenes
from Ordenes.serializers import OrdenesSerializer

# Create your views here.


class OrdenesViewSet(viewsets.ModelViewSet):
    serializer_class = OrdenesSerializer
    queryset = ordenes.objects.all()

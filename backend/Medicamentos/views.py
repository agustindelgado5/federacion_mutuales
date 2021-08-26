from rest_framework import viewsets


from Medicamentos.models import medicamentos, receta
from Medicamentos.serializers import MedicamentosSerializer, RecetasSerializer


class MedicamentosViewSet(viewsets.ModelViewSet):
    serializer_class = MedicamentosSerializer
    queryset = medicamentos.objects.all()


class RecetasViewSet(viewsets.ModelViewSet):
    serializer_class = RecetasSerializer
    queryset = receta.objects.all()

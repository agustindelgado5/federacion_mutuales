from rest_framework import viewsets


from Profesionales.models import profesionales
from Profesionales.serializers import ProfesionalesSerializer


class ProfesionalesViewSet(viewsets.ModelViewSet):
    serializer_class = ProfesionalesSerializer
    queryset = profesionales.objects.all()

from rest_framework import viewsets


from Servicios.models import servicios
from Servicios.serializers import ServiciosSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin

class ServiciosViewSet(PermissionRequiredMixin, viewsets.ModelViewSet):
    serializer_class = ServiciosSerializer
    queryset = servicios.objects.all()
    permission_required = (
        'Servicios.view_servicios',
        'Servicios.add_servicios',
        'Servicios.change_servicios',
        'Servicios.delete_servicios',
    )
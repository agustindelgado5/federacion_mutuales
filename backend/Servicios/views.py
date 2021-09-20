from rest_framework import viewsets


from Servicios.models import servicios
from Servicios.serializers import ServiciosSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin


class ServiciosViewSet(PermissionRequiredMixin, viewsets.ModelViewSet):
    serializer_class = ServiciosSerializer
    queryset = servicios.objects.all()
    permission_required = (
<<<<<<< HEAD
        "Servicios.view_servicios",
        "Servicios.add_servicios",
        "Servicios.change_servicios",
        "Servicios.delete_servicios",
    )
=======
    #    'Servicios.view_servicios',
    #    'Servicios.add_servicios',
    #    'Servicios.change_servicios',
    #    'Servicios.delete_servicios',
    )
>>>>>>> 22136aa83e79bce7ac841c370c6af768e1d784f5

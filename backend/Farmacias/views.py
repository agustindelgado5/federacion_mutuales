from rest_framework import viewsets

from Farmacias.models import farmacias
from Farmacias.serializers import FarmaciasSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin


class FarmaciasViewSet(viewsets.ModelViewSet):
    serializer_class = FarmaciasSerializer
    queryset = farmacias.objects.all()
<<<<<<< HEAD
=======
    permission_required = (
    #    'Farmacias.view_farmacias',
    #    'Farmacias.add_farmacias',
    #    'Farmacias.change_farmacias',
    #    'Farmacias.delete_farmacias',
    )
>>>>>>> 22136aa83e79bce7ac841c370c6af768e1d784f5

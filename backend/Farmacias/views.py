from rest_framework import viewsets

from Farmacias.models import farmacias
from Farmacias.serializers import FarmaciasSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin

class FarmaciasViewSet(PermissionRequiredMixin, viewsets.ModelViewSet):
    serializer_class = FarmaciasSerializer
    queryset = farmacias.objects.all()
    permission_required = (
    #    'Farmacias.view_farmacias',
    #    'Farmacias.add_farmacias',
    #    'Farmacias.change_farmacias',
    #    'Farmacias.delete_farmacias',
    )

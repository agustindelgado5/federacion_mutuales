from rest_framework import viewsets

from Farmacias.models import farmacias
from Farmacias.serializers import FarmaciasSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin


class FarmaciasViewSet(viewsets.ModelViewSet):
    serializer_class = FarmaciasSerializer
    queryset = farmacias.objects.all()

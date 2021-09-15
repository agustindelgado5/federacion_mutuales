from rest_framework import serializers
from .models import servicios


class ServiciosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = servicios
        fields = (
            "id_servicio",
            "nombre",
        )

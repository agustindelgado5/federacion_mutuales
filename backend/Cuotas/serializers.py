from rest_framework import serializers
from Cuotas.models import cuotas


class CuotasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cuotas
        fields = (
            "id_cuota",
            "personapago",
            "monto",
            "fecharealizacion",
            "numero_socio",
        )
        read_only_fields = ["created ", "updated"]

from rest_framework import serializers
from Cuotas.models import cuotas
from django.db.models.functions import TruncMonth

class CuotasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cuotas
        periodo=TruncMonth('periodo')
        fields = (
            "id_cuota",
            "personapago",
            "monto",
            "fecharealizacion",
            "numero_socio",
            "periodo",
            "pagado",
            "metodoPago",
        )
        read_only_fields = ["created ", "updated"]

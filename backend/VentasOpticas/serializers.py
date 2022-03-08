from rest_framework import serializers
from .models import ventasOpticas


class VentasOpticasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ventasOpticas
        fields = (
            "id_venta",
            "numero_socio",
            "lente",
            "cristal_derecho",
            "cristal_izquierdo",
            "fecha_receta",
            "fecha_venta",
        )
        read_only_fields = ["created ", "updated"]

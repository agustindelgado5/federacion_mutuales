from rest_framework import serializers
from Lentes.models import lentes


class LentesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = lentes
        fields = (
            "codigo_optica",
            #"codigo_seguimiento",
            "medida_lente",
            "patillas",
            "marca",
            "descripcion",
            "precio_laboratorio",
            "precio_optica",
            "precio_mutual",
            "precio_venta",
            "precio_tarjeta",
            "stock",
            
        )
        read_only_fields = ["created ", "updated"]

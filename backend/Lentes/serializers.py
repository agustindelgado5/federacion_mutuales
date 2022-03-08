from rest_framework import serializers
from Lentes.models import lentes


class LentesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = lentes
        fields = (
            "id_lente",
            "diametro_cristal",
            "largo_patillas",
            "ancho_puente",
            "marca",
            "color",
            "material",
            "descripcion",
            "precio_optica",
            "precio_mutual",
            "precio_venta",
            "precio_tarjeta",
            "stock"
        )
        read_only_fields = ["created ", "updated"]

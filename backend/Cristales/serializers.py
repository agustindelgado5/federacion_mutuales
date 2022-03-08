from rest_framework import serializers
from Cristales.models import cristales


class CristalesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cristales
        fields = (
            "id_cristal",
            "material",
            "esfera",
            "cilindro",
            "eje",
            "precio_laboratorio",
            "precio_optica",
            "precio_mutual",
            "precio_venta",
            "precio_tarjeta",
            "stock"
        )
        read_only_fields = ["created ", "updated"]

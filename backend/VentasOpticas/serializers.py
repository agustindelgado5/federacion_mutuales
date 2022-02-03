from rest_framework import serializers
from .models import ventasOpticas


class VentasOpticasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ventasOpticas
        fields = (
            "codigo_seguimiento",
            "numero_socio",
        )
        read_only_fields = ["created ", "updated"]

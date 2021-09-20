from rest_framework import serializers
from .models import cobradores


class CobradoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cobradores
        fields = (
            "id_cobrador",
            "numero_socio",
            "nombre",
            "apellido",
            "dni",
            "fecha_cobro",
        )
        read_only_fields = ["created ", "updated"]

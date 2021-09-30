from rest_framework import serializers
from .models import gastosSalientes


class GastosSalientesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = gastosSalientes
        fields = (
            "id_gasto",
            "nro_ticket",
            "descripcion",
            "total",
            "fecha",
        )

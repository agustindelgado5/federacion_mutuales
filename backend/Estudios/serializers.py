from rest_framework import serializers
from Estudios.models import estudios


class EstudiosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = estudios
        fields = (
            "id_estudio",
            "tipo",
            "cod_estudio",
            "abreviatura",
            "ub",
            "activo",
            "descripcion",
            "denominación",
        )
        read_only_fields = ["created ", "updated"]

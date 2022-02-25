from rest_framework import serializers
from Estudios.models import estudios


class EstudiosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = estudios
        fields = (
            "id_estudio",
            "tipo",
            "abreviatura",
            "ub",
            "nbu",
            "proveedor",
            "descripcion",
            "denominación",
            "precio_socio",
            "precio_federacion",  
        )
        read_only_fields = ["created ", "updated"]

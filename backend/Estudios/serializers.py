from rest_framework import serializers
from Estudios.models import estudios, estudio_socio


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


class EstudiosSociosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = estudio_socio
        fields = (
            "id_estudio_socio",
            "id_estudio",
            "numero_socio",
            "created",
            "updated",
            
        )
        #read_only_fields = ["created ", "updated"]
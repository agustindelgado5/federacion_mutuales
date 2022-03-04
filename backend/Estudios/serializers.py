from rest_framework import serializers
from Estudios.models import proveedor, estudios, estudio_socio


class ProveedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = proveedor
        fields = (
            "id_proveedor",
            "nombre",
            "cuit",
            "direccion",
            "localidad",
            "provincia",
            "email",
            "tel_fijo",
            "tel_celular",
            "created",
            "updated",
        )


class EstudiosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = estudios
        fields = (
            "id_estudio",
            "tipo",
            "abreviatura",
            "ub",
            "nbu",
            "id_proveedor",
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
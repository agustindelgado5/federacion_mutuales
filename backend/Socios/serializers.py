from rest_framework import serializers
from Socios.models import socios, familiar


class SociosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = socios
        # edad = serializers.DateField(read_only=True)
        fields = (
            "numero_socio",
            "apellido",
            "nombre",
            "dni",
            "fecha_nacimiento",
            #'edad',
            "calle",
            "localidad",
            "departamento",
            "cod_postal",
            "email",
            "tel_fijo",
            "tel_celular",
            "carencia",
        )
        read_only_fields = ["edad", "created ", "updated"]


class FamiliarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = familiar

        fields = (
            "dni_familiar",
            "apellido",
            "nombre",
            "fecha_nacimiento",
            "edad",
            "carencia",
            "numero_socio",
        )
        read_only_fields = ["edad", "created ", "updated"]

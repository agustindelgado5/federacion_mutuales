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
            "fecha_asociacion",
            "edad",
            "calle",
            "localidad",
            "departamento",
            "cod_postal",
            "email",
            "tel_fijo",
            "tel_celular",
            "carencia",
            "id_mutual",
            "tieneObraSocial",
            # "plan",
            # "vendedor",
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
            "fecha_asociacion",
            "edad",
            "carencia",
            "numero_socio",
            "tieneObraSocial",
            # "plan",

        )
        read_only_fields = ["edad","created ", "updated"]

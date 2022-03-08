from rest_framework import serializers
from Socios.models import socios, familiar





class SociosSerializer(serializers.HyperlinkedModelSerializer):
    monto = serializers.DecimalField(max_digits=9, decimal_places=2,read_only=True)
    class Meta:
        model = socios
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
            "metodopago",
            "cobrador",
            "monto"
            # "plan",
            # "vendedor",
        )
        read_only_fields = ["edad", "created ", "updated","monto"]

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

"""
class ServiciosSociosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = servicio_socio
        fields = (
            "numero_socio",
            "id_servicio",
        )
        read_only_fields = ["created ", "updated"]
"""
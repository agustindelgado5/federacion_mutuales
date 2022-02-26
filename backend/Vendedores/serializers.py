from rest_framework import serializers

from .models import vendedores


class VendedoresSerializer(serializers.ModelSerializer):

    class Meta:
        model = vendedores
        fields = (
            "apellido",
            "nombre",
            "dni",
            "fecha_nacimiento",
            "calle",
            "localidad",
            "departamento",
            "cod_postal",
            "tel_fijo",
            "tel_celular",

        )
        read_only_fields = ["created ", "updated"]
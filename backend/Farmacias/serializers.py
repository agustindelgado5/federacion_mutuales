from rest_framework import serializers
from .models import farmacias


class FarmaciasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = farmacias
        fields = (
            "cod_farmacia",
            "matricula_farm",
            "farmacia",
            "cuit",
            "direccion",
            "localidad",
            "cod_postal",
            "email",
            "tel_fijo",
            "representante",
            "tel_celular",
        )

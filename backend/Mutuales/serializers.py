from rest_framework import serializers
from Mutuales.models import mutuales


class MutualesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = mutuales
        fields = (
            "id_mutual",
            "nombre",
            "sucursal",
        )
        read_only_fields = ["id_mutual", "created ", "updated"]

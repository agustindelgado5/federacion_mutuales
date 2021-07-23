from rest_framework import serializers
from Mutuales.models import mutuales


class MutualesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = mutuales
        fields = (
            'nombre',
            'sucursal',
        )
        read_only_fields = ['created ','updated']




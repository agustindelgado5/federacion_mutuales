from rest_framework import serializers
from Ordenes.models import ordenes


class OrdenesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ordenes
        fields = (
            'numero_socio',
            'paciente',
            'servicio',
            'id_medico',
            'mutual',
            'fecha',
            'precio',
            'realizado',
        )
        read_only_fields = ['created ','updated']




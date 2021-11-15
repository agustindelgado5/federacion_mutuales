from rest_framework import serializers
from Mutuales.models import mutuales, servicios, servicio_mutual

class ServiciosSerializer(serializers.ModelSerializer):

    class Meta:
        model = servicios
        fields = (
            'id_servicio',
            'servicio',
        )
        read_only_fields = ['id_servicio','created ','updated']


class MutualesSerializer(serializers.ModelSerializer):

    class Meta:
        model = mutuales
        fields = (
            'id_mutual',
            'nombre',
            'direccion',
            'localidad',
            'sucursal',
            'matricula',
            'cuit',
            'email',
            'telefono',
            'representante',
            'fecha_inicio',
        )
        read_only_fields = ['id_mutual','created ','updated']


class ServiciosMutualSerializer(serializers.ModelSerializer):

    class Meta:
        model = servicio_mutual
        fields = (
            'id_serv_mut',
            'id_mutual',
            'id_servicio',
        )
        #read_only_fields = ['id_mutual','id_servicio']








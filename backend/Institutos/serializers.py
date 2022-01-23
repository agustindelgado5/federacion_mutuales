from rest_framework import serializers
from Institutos.models import institutos


class InstitutosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = institutos
        fields = (
            "codigo_institucion",
            "nombre",
            "cuit",
            "direccion",
            "localidad", 
            "provincia", 
            "telefono",
            "horarios",
            "responsable",
            "telefono_responsable",
        )
        read_only_fields = ["created ", "updated"]

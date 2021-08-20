from rest_framework import serializers
from Ordenes.models import ordenes


class OrdenesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ordenes
        fields = (
            "numero_orden",
            "numero_socio",
            "paciente",
            "servicio",
            "id_medico",
            "id_mutual",
            "fecha",
            "hora",
            "precio",
            "realizado",
        )
        read_only_fields = ["created ", "updated"]

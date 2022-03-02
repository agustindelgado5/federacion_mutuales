from rest_framework import serializers
from Cirugias.models import cirugias


class CirugiasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cirugias
        fields = (
            "codigo_intervencion",
            "numero_socio",
            "codigo_institucion",
            "descripcion",
            "nivel",
            "numero_ayudantes",
            "honorario_cirujano",
            "honorario_ayudante",
            "honorario_total",
            "observacion",
            
        )
        read_only_fields = ["honorario_total","created ", "updated"]

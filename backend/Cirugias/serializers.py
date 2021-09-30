from rest_framework import serializers
from Cirugias.models import cirugias


class CirugiasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cirugias
        fields = (
            "codigo_intervencion",
            "descripcion",
            "nivel",
            "honorario_cirujano",
            "honorario_ayudante",
            "observacion",
            
        )
        read_only_fields = ["created ", "updated"]

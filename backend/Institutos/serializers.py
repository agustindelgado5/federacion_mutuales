from rest_framework import serializers
from Institutos.models import institutos


class InstitutosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = institutos
        fields = (
            "codigo_institucion",
            "id_medico",
            
            
        )
        read_only_fields = ["created ", "updated"]

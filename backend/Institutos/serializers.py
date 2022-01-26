from rest_framework import serializers
from Institutos.models import institutos, institutos_profesionales


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



class InstitutosProfesionalesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = institutos_profesionales
        fields = (

            "id_inst_prof",
            "codigo_institucion",
            "id_medico",
        
        )
        #read_only_fields = ["created ", "updated"]

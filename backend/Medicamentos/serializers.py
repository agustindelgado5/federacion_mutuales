from rest_framework import serializers
from Medicamentos.models import medicamentos, receta


class MedicamentosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = medicamentos
        fields = (
            "id_medicamento",
            "nombre",
            "presentacion",
            "laboratorio",
            "cod_farmacia",
        )


class RecetasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = receta
        fields = (
            'id_receta',
            'numero_socio',
            'diagnostico', 
            'paciente',
            'id_medico',
            'id_medicamento',
            'cod_farmacia',
            'fecha',            
            'carencia'

        )
        read_only_fields = ["created ", "updated"]

from rest_framework import serializers
from Medicamentos.models import medicamentos, receta

class MedicamentosSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = medicamentos
        fields = (
            'id_medicamento',
            'nombre', 
            'presentacion',
            'laboratorio',
            'cod_farmacia'
        )

class RecetasSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = receta
        fields = (
            'numero_socio',
            'dni_familiar',
            'diagnostico', 
            'id_medicamento',
            'cod_farmacia',
            'fecha',
            'carencia'
            
        )
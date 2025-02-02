from rest_framework import serializers
from Profesionales.models import profesionales


class ProfesionalesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = profesionales
        fields = (
            "id_medico",
            "apellido",
            "nombre",
            "dni",
            "domicilio",
            "localidad",
            "provincia",
            "fecha_ingreso",
            "especialidad",
            "email",
            "tel_fijo",
            "tel_celular",
            "matricula",
            "diasliquidacion",
            "cbu",
            "alias_cbu",
            "titular_cuenta", 
            "tipo_cuenta", 
            "banco",
            "totalapagar",
            "created",
            "updated",
        )

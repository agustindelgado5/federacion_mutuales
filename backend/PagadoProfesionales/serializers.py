from rest_framework import serializers
from .models import pagadoProfesionales


class PagadoProfesionalesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pagadoProfesionales
        fields = (
            "id_pagoprofesional",
            "id_medico",
            "total",
            "fecha",
            "modo_pago",
            "periodo",
        )

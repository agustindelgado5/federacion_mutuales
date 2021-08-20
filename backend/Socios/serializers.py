from rest_framework import serializers
from Socios.models import socios, familiar

# from .utils import calcular_edad


class SociosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = socios
        edad = serializers.DateField(read_only=True)
        fields = (
            "numero_socio",
            "apellido",
            "nombre",
            "dni",
            "fecha_nacimiento",
            "edad",
            "calle",
            "localidad",
            "departamento",
            "cod_postal",
            "email",
            "tel_fijo",
            "tel_celular",
            "carencia",
        )
        read_only_fields = ["created ", "updated"]

        def edad_socio(self, serializers):
            # return 0
            _edad = self.calcular_edad(self.request.POST["fecha_nacimiento"])
            serializers.save(edad=_edad)
            # return calcular_edad(self.fecha_nacimiento)

        """
        def save(self):
            self.edad=self.edad_socio
            super (socios,self).save()
        """


class FamiliarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = familiar

        fields = (
            "dni_familiar",
            "apellido",
            "nombre",
            "fecha_nacimiento",
            "carencia",
            "numero_socio",
        )
        read_only_fields = ["edad", "created ", "updated"]

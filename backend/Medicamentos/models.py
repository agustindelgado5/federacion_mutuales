from django.db import models
from django.db.models.fields import AutoField
from Farmacias.models import farmacias
from Profesionales.models import profesionales
from Socios.models import socios

# Create your models here.
"""
Construyo la entidad medicamentos con sus atributos
"""


class medicamentos(models.Model):
    id_medicamento = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    presentacion = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=30)
    cod_farmacia = models.ForeignKey(farmacias, on_delete=models.DO_NOTHING)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "medicamentos"
        verbose_name = "medicamento"
        verbose_name_plural = "medicamentos"
        ordering = ["id_medicamento"]

    def __str__(self):
        cadena = (
            str(self.id_medicamento)
            + " - "
            + str(self.nombre)
            + " - "
            + str(self.cod_farmacia)
        )
        return cadena


"""
Construyo la entidad para la receta con sus atributos
"""


class receta(models.Model):
    id_receta = models.AutoField(primary_key=True)
    numero_socio = models.ForeignKey(socios, on_delete=models.DO_NOTHING)
    cod_farmacia = models.ForeignKey(farmacias, on_delete=models.DO_NOTHING)
    id_medicamento = models.ForeignKey(medicamentos, on_delete=models.DO_NOTHING)
    paciente = models.CharField(max_length=60)
    diagnostico = models.TextField(max_length=200)
    id_medico = models.ForeignKey(profesionales, on_delete=models.DO_NOTHING)
    fecha = models.DateField()
    carencia = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "recetas"
        verbose_name = "receta"
        verbose_name_plural = "recetas"
        ordering = ["numero_socio"]

    def __str__(self):
        cadena = str(self.numero_socio)
        return cadena

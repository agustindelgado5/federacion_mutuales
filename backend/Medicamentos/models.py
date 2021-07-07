from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from Farmacias.models import farmacias
from Socios.models import socios, familiar
# Create your models here.
"""
Construyo la entidad medicamentos con sus atributos
"""
class medicamentos(models.Model):
    id_medicamento=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    presentacion=models.CharField(max_length=100)
    laboratorio=models.CharField(max_length=30)
    cod_farmacia=models.ForeignKey(farmacias, on_delete=models.DO_NOTHING)
    numero_socio=models.ForeignKey(socios,on_delete=models.DO_NOTHING)
    dni_familiar=models.ForeignKey(familiar,on_delete=models.DO_NOTHING)

    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='medicamentos'
        verbose_name='medicamento'
        verbose_name_plural='medicamentos'
        ordering=['id_medicamento']

    def __str__(self):
        cadena = str(self.id_medicamento)+str(self.nombre)+'-'+ str(self.cod_farmacia)+'-'+ str(self.numero_socio)+'-'+ str(self.dni_familiar)
        return cadena

"""
Construyo la entidad para el grupo familiar con sus atributos
"""
class receta(models.Model):
    dni_familiar=models.IntegerField(primary_key=True)
    numero_socio=models.ForeignKey(socios, on_delete=models.DO_NOTHING)
    dni_familiar=models.ForeignKey(familiar, on_delete=models.DO_NOTHING)
    cod_farmacia=models.ForeignKey(farmacias, on_delete=models.DO_NOTHING)
    id_medicamento=models.ForeignKey(medicamentos, on_delete=models.DO_NOTHING)
    diagnostico = models.TextField(max_length=200)
    fecha=models.DateField()
    carencia=models.DateField(null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table='recetas'
        verbose_name='receta'
        verbose_name_plural='recetas'
        ordering=['numero_socio']

    def __str__(self):
        cadena = str(self.numero_socio)
        return cadena
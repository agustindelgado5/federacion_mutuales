from django.db import models

from backend.deptos import provincias
from backend.datos_pagos import cuentas
from backend.datos_pagos import modos
from django.db.models.fields import AutoField

# Create your models here.

"""
Construyo la entidad farmacias con sus atributos
"""


class farmacias(models.Model):
    cod_farmacia = AutoField(primary_key=True)
    matricula_farm = models.IntegerField(unique=True)
    farmacia = models.CharField(max_length=50)
    cuit = models.IntegerField(unique=True)
    direccion = models.CharField(max_length=80)
    localidad = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30, choices=provincias)
    cod_postal = models.IntegerField()
    email = models.EmailField()
    tel_fijo = models.IntegerField(null=True, blank=True)
    # --Representante de la farmacia
    representante = models.CharField(max_length=50)
    tel_celular = models.IntegerField(null=True, blank=True)
    # carencia=models.DateField(null=True, blank=True)
    cbu=models.CharField(unique=True, max_length=22)
    entidad_bancaria=models.CharField(max_length=80)
    nro_cuenta=models.IntegerField()
    tipo_cuenta=models.CharField(max_length=20, choices=cuentas)
    modalidad_pago=models.CharField(max_length=20, choices=modos)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "farmacias"
        verbose_name = "famacia"
        verbose_name_plural = "farmacias"
        ordering = ["cod_farmacia"]

    def __str__(self):
        cadena = (
            str(self.cod_farmacia)
            + "-"
            + str(self.matricula_farm)
            + "-"
            + self.farmacia
        )
        return cadena

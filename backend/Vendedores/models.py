from django.db import models
from django.db.models.fields import AutoField
from backend.deptos import deptos_tucuman, comumas_municipios


class vendedores(models.Model):

    id_vendedor = AutoField(primary_key=True)
    apellido = models.CharField(max_length=80)
    nombre = models.CharField(max_length=80)
    dni = models.IntegerField(unique=True)
    fecha_nacimiento = models.DateField()
    calle = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50, choices=comumas_municipios)
    departamento = models.CharField(max_length=30, choices=deptos_tucuman)
    cod_postal = models.IntegerField()
    tel_fijo = models.IntegerField(null=True, blank=True)
    tel_celular = models.IntegerField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "vendedores"
        verbose_name = "vendedor"
        verbose_name_plural = "vendedores"
        ordering = ["id_vendedor"]
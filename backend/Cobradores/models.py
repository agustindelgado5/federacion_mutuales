from django.db import models
from django.db.models.fields import AutoField
#from Socios.models import socios

# Create your models here.

"""
Construyo la entidad para los cobradores
"""


class cobradores(models.Model):
    id_cobrador = AutoField(primary_key=True)
    #numero_socio = models.ForeignKey(socios, on_delete=models.DO_NOTHING) #Un cobrador no sirve para un solo socio
    apellido = models.CharField(max_length=80)
    nombre = models.CharField(max_length=80)
    dni = models.CharField(unique=True, max_length=8)
    fecha_cobro = models.DateField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "cobradores"
        verbose_name = "cobrador"
        verbose_name_plural = "cobradores"
        ordering = ["id_cobrador"]

    def __str__(self):
        cadena = (
            str(self.id_cobrador)
            + "-"
            + self.apellido
            + "-"
            + self.nombre
            + "-"
            + self.dni
        )
        return cadena

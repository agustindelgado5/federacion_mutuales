from django.db import models
from Socios.models import socios

# Create your models here.

"""
Construyo la entidad para los cobradores
"""


class cobradores(models.Model):
    id_cobrador = models.IntegerField(primary_key=True)
    numero_socio = models.ForeignKey(socios, on_delete=models.DO_NOTHING)
    apellido = models.CharField(max_length=80)
    nombre = models.CharField(max_length=80)
    dni = models.IntegerField(unique=True)
    fecha_cobro = models.DateField()

    realizado = models.BooleanField(default=False)
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
            + str(self.dni)
        )
        return cadena

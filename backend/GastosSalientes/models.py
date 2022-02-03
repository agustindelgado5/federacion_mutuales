from django.db import models
from datetime import datetime

# Create your models here.

"""
Construyo la entidad gastosSalientes con sus atributos
"""


class gastosSalientes(models.Model):
    id_gasto = models.AutoField(primary_key=True)
    nro_ticket = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    total = models.DecimalField(decimal_places=2, max_digits=6)
    fecha = models.DateField(default=datetime.now)
    
    class Meta:
        db_table = "gastosSalientes"
        verbose_name = "gastosSaliente"
        verbose_name_plural = "gastosSalientes"
        ordering = ["id_gasto"]

    def __str__(self):
        cadena = (
            str(self.id_gasto)
            + "-"
            + str(self.nro_ticket)
            + "-"
            + str(self.descripcion)
            + "-"
            + str(self.fecha)
            + "-"
            + self.total
        )
        return cadena

from django.db import models
from Socios.models import socios

# Create your models here.

"""
Construyo la entidad para Ventas Opticas
"""


class ventasOpticas(models.Model):
    codigo_seguimiento = models.IntegerField(primary_key=True)
    numero_socio = models.ForeignKey(socios, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "ventasOpticas"
        verbose_name = "ventaOptica"
        verbose_name_plural = "ventasOpticas"
        ordering = ["codigo_seguimiento"]

    def __str__(self):
        cadena = (
            str(self.codigo_seguimiento)
           
        )
        return cadena

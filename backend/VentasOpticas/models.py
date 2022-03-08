from django.db import models
from Socios.models import socios
from Cristales.models import cristales
from Lentes.models import lentes
from datetime import datetime

# Create your models here.

"""
Construyo la entidad para Ventas Opticas
"""


class ventasOpticas(models.Model):
    id_venta = models.AutoField(primary_key=True)
    numero_socio = models.ForeignKey(socios, on_delete=models.DO_NOTHING)
    lente = models.ForeignKey(lentes, on_delete=models.DO_NOTHING)
    cristal_derecho = models.ForeignKey(cristales, on_delete=models.DO_NOTHING,related_name="cristal_derecho")
    cristal_izquierdo = models.ForeignKey(cristales, on_delete=models.DO_NOTHING,related_name="cristal_izquierdo")
    fecha_receta = models.DateField(default=datetime.now)
    fecha_venta = models.DateField(default=datetime.now)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "ventasOpticas"
        verbose_name = "ventaOptica"
        verbose_name_plural = "ventasOpticas"
        ordering = ["id_venta"]

    def __str__(self):
        cadena = (
            str(self.id_venta)
           
        )
        return cadena

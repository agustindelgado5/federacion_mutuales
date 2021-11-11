from django.db import models
from VentasOpticas.models import ventasOpticas

# Create your models here.

"""
Construyo la entidad para Lente

"""


class lentes(models.Model):
    codigo_optica = models.AutoField(primary_key=True) #id interno
    codigo_seguimiento = models.ForeignKey(ventasOpticas, on_delete=models.DO_NOTHING)
    medida_lente = models.CharField(max_length=30) #codigo mostrado al usuario
    patillas = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    descripcion=models.CharField(max_length=60)
    precio_laboratorio=models.DecimalField(null=True,max_digits=8, decimal_places=2)
    precio_optica=models.DecimalField(null=True,max_digits=8, decimal_places=2)
    precio_mutual=models.DecimalField(null=True,max_digits=8, decimal_places=2)
    precio_venta=models.DecimalField(null=True,max_digits=8, decimal_places=2)
    precio_tarjeta=models.DecimalField(null=True,max_digits=8, decimal_places=2)
    stock=models.DecimalField(null=True,max_digits=8, decimal_places=2)
    
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "lentes"
        verbose_name = "lente"
        verbose_name_plural = "lentes"
        ordering = ["codigo_optica"]

    def __str__(self):
        cadena = (
            str(self.codigo_optica)
            + " - "
            
            + str(self.descripcion)
        )
        return cadena

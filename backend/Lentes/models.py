from django.db import models

# Create your models here.

"""
Construyo la entidad para Lente

"""


class lentes(models.Model):
    id_lente = models.AutoField(primary_key=True) #id interno
    diametro_cristal = models.PositiveSmallIntegerField()
    largo_patillas = models.PositiveSmallIntegerField()
    ancho_puente = models.PositiveSmallIntegerField()
    marca = models.CharField(max_length=30,null=True, blank=True)
    color = models.CharField(max_length=30,null=True, blank=True)
    material=models.CharField(max_length=30,null=True, blank=True)
    descripcion=models.CharField(max_length=60,null=True, blank=True)
    precio_optica=models.DecimalField(null=True,max_digits=8, decimal_places=2)
    precio_mutual=models.DecimalField(null=True,max_digits=8, decimal_places=2)
    precio_venta=models.DecimalField(null=True,max_digits=8, decimal_places=2)
    precio_tarjeta=models.DecimalField(null=True,max_digits=8, decimal_places=2)
    stock=models.IntegerField(default=0)
    
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "lentes"
        verbose_name = "lente"
        verbose_name_plural = "lentes"
        ordering = ["id_lente"]

    def __str__(self):
        cadena = (
            str(self.id_lente)
            + " - "
            
            + str(self.descripcion)
        )
        return cadena

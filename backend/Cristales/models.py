from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.

"""
Construyo la entidad para Cristal

"""


class cristales(models.Model):
    id_cristal = models.AutoField(primary_key=True) #id interno
    material = models.CharField(max_length=30)
    esfera=models.DecimalField(max_digits=4, decimal_places=2)
    cilindro=models.DecimalField(max_digits=4, decimal_places=2)
    eje=models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(180)])
    precio_laboratorio=models.DecimalField(null=True,max_digits=8, decimal_places=2)
    precio_optica=models.DecimalField(null=True,max_digits=8, decimal_places=2)
    precio_mutual=models.DecimalField(null=True,max_digits=8, decimal_places=2)
    precio_venta=models.DecimalField(null=True,max_digits=8, decimal_places=2)
    precio_tarjeta=models.DecimalField(null=True,max_digits=8, decimal_places=2)
    stock=models.IntegerField(default=0)
    
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "cristales"
        verbose_name = "cristal"
        verbose_name_plural = "cristales"
        ordering = ["id_cristal"]

    def __str__(self):
        cadena = (
            str(self.id_cristal)
            + " - "
            
            + str(self.material)
        )
        return cadena

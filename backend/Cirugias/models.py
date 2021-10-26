from django.db import models


# Create your models here.

"""
Construyo la entidad para Cirugia

"""


class cirugias(models.Model):
    codigo_intervencion = models.AutoField(primary_key=True) #id interno
    descripcion = models.CharField(max_length=30) #codigo mostrado al usuario
    nivel = models.IntegerField()
    numero_ayudantes = models.IntegerField()
    honorario_cirujano = models.DecimalField(null=True,max_digits=8, decimal_places=2)
    honorario_ayudante = models.DecimalField(null=True,max_digits=8, decimal_places=2)
    
    observacion=models.CharField(max_length=60)
    
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "cirugias"
        verbose_name = "cirugia"
        verbose_name_plural = "cirugias"
        ordering = ["codigo_intervencion"]

    def __str__(self):
        cadena = (
            str(self.codigo_intervencion)
            + " - "
            
            + str(self.descripcion)
        )
        return cadena

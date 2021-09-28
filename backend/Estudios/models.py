from django.db import models
from backend.tipos_Estudios import estudios_tipos

# Create your models here.

"""
Construyo la entidad para estudios, éstos pueden ser de análisis bioquimico, diagnóstico
por imagen, estudio oftalmológico, etc
"""


class estudios(models.Model):
    id_estudio = models.AutoField(primary_key=True) #id interno
    tipo = models.CharField(max_length=60,choices=estudios_tipos)
    cod_estudio = models.CharField(max_length=30) #codigo mostrado al usuario
    abreviatura = models.CharField(null=True,max_length=30)
    UB = models.DecimalField(null=True,max_digits=8, decimal_places=2)
    activo = models.BooleanField(default=True) #para un borrado lógico
    descripcion=models.CharField(max_length=60)
    denominación=models.CharField(null=True,max_length=30)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "estudios"
        verbose_name = "estudio"
        verbose_name_plural = "estudios"
        ordering = ["id_estudio"]

    def __str__(self):
        cadena = (
            str(self.cod_estudio)
            + " - "
            + str(self.tipo)
            + " - "
            + str(self.descripcion)
        )
        return cadena

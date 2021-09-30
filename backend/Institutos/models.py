from django.db import models
from Profesionales.models import profesionales

# Create your models here.

"""
Construyo la entidad para Institutos

"""


class institutos(models.Model):
    codigo_institucion = models.AutoField(primary_key=True) #id interno
    id_medico = models.ForeignKey(profesionales, on_delete=models.DO_NOTHING) #codigo mostrado al usuario
    
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "institutos"
        verbose_name = "instituto"
        verbose_name_plural = "institutos"
        ordering = ["codigo_institucion"]

    def __str__(self):
        cadena = (
            str(self.codigo_institucion)
            
        )
        return cadena

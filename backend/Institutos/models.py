from django.db import models
from django.db.models.fields import AutoField
from Profesionales.models import profesionales
from backend.deptos import provincias
# Create your models here.

"""
Construyo la entidad para Institutos

"""


class institutos(models.Model):
    codigo_institucion = models.AutoField(primary_key=True) #id interno
    #id_medico = models.ForeignKey(profesionales, on_delete=models.DO_NOTHING) #codigo mostrado al usuario
    nombre = models.CharField(max_length=80, unique=True)
    cuit = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    localidad = models.CharField(max_length=30)
    provincia = models.CharField(choices=provincias, max_length=30)

    telefono= models.CharField(max_length=10)
    horarios = models.TextField()

    responsable = models.CharField(max_length=80)
    telefono_responsable = models.CharField(max_length=10)

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


class institutos_profesionales(models.Model):
    id_inst_prof  = AutoField(primary_key=True)
    codigo_institucion = models.ForeignKey(institutos, on_delete=models.CASCADE) 
    id_medico = models.ForeignKey(profesionales, on_delete=models.CASCADE) #codigo mostrado al usuario
    horarios = models.TextField(null=True)
    #created = models.DateTimeField(auto_now_add=True)
    #updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "institutos_profesionales"
        verbose_name = "instituto_profesionales"
        verbose_name_plural = "institutos_profesionales"
        ordering = ["codigo_institucion"]
        unique_together = (('codigo_institucion', 'id_medico'),)
        




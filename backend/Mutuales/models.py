from django.db import models
from backend.deptos import deptos_tucuman

# Create your models here.

"""
Construyo la entidad para las ordenes mutuales
"""


class mutuales(models.Model):
    id_mutual = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    sucursal = models.CharField(max_length=30, choices=deptos_tucuman)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "mutuales"
        verbose_name = "mutual"
        verbose_name_plural = "mutuales"
        ordering = ["id_mutual"]

    def __str__(self):
        cadena = (
            str(self.id_mutual) + " - " + str(self.nombre) + " - " + str(self.sucursal)
        )
        return cadena

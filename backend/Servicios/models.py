from django.db import models


"""
Construyo la entidad servicio con sus atributos
"""


class servicios(models.Model):
    id_servicio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "servicios"
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ["id_servicio"]

    def __str__(self):
        cadena = str(self.id_servicio) + "-" + self.nombre
        return cadena

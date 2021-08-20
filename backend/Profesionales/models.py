from django.db import models
from backend.deptos import provincias

# Create your models here.


class profesionales(models.Model):
    id_medico = models.IntegerField(primary_key=True)
    apellido = models.CharField(max_length=80)
    nombre = models.CharField(max_length=80)
    dni = models.IntegerField(unique=True)
    domicilio = models.CharField(max_length=50)
    localidad = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30, choices=provincias)
    fecha_ingreso = models.DateField()
    especialidad = models.CharField(max_length=40, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    tel_fijo = models.IntegerField(null=True, blank=True)
    tel_celular = models.IntegerField(null=True, blank=True)
    matricula = models.IntegerField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "profesionales"
        verbose_name = "profesional"
        verbose_name_plural = "profesionales"
        ordering = ["id_medico"]

    def __str__(self):
        cadena = (
            str(self.id_medico)
            + "-"
            + self.apellido
            + "-"
            + self.nombre
            + "-"
            + str(self.dni)
        )
        return cadena

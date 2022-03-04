from django.db import models
from backend.deptos import provincias
from backend.datos_bancarios import bancos_argentina
from django.db.models.fields import AutoField
# Create your models here.


class profesionales(models.Model):
    id_medico = AutoField(primary_key=True)
    #Datos personales
    apellido = models.CharField(max_length=80)
    nombre = models.CharField(max_length=80)
    dni = models.IntegerField(unique=True)

    #Domicilio particular
    domicilio = models.CharField(max_length=50)
    localidad = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30, choices=provincias)

    #Contacto
    email = models.EmailField(null=True, blank=True)
    tel_fijo = models.IntegerField(null=True, blank=True)
    tel_celular = models.IntegerField(null=True, blank=True)

    #Datos Laborales
    fecha_ingreso = models.DateField()
    especialidad = models.CharField(max_length=40, null=True, blank=True)
    matricula = models.IntegerField(unique=True)
    diasliquidacion = models.PositiveIntegerField(default=30)

    #Datos bancarios
    cbu=models.CharField(unique=True, max_length=22)
    alias_cbu=models.CharField(unique=True,max_length=20)
    titular_cuenta = models.CharField(max_length=80)
    tipo_cuenta = models.CharField(max_length=20)
    banco=models.CharField(max_length=100, choices=bancos_argentina)

    #Datos en el sistema
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

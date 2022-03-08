from django.db import models
from backend.deptos import provincias
from backend.tipos_Estudios import estudios_tipos
from django.db.models.fields import AutoField
from Socios.models import socios

# Create your models here.

"""
Construyo la entidad del Proveedor para proveer un estudio
"""


class proveedor(models.Model):
    id_proveedor = AutoField(primary_key=True)
    #Datos personales
    nombre = models.CharField(max_length=100)
    cuit = models.CharField(unique=True, max_length=11)

    #Direccion particular
    direccion = models.CharField(max_length=50)
    localidad = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30, choices=provincias)

    #Contacto
    email = models.EmailField(null=True, blank=True)
    tel_fijo = models.IntegerField(null=True, blank=True)
    tel_celular = models.IntegerField(null=True, blank=True)


    #Datos en el sistema
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "proveedores"
        verbose_name = "proveedor"
        verbose_name_plural = "proveedores"
        ordering = ["id_proveedor"]

    def __str__(self):
        cadena = (
            str(self.id_proveedor)
            + "-"
            + self.nombre
            + "-"
            + str(self.cuit)
        )
        return cadena


"""
Construyo la entidad para estudios, éstos pueden ser de análisis bioquimico, diagnóstico
por imagen, estudio oftalmológico, etc
"""


class estudios(models.Model):
    id_estudio = models.AutoField(primary_key=True) #id interno
    tipo = models.CharField(max_length=60,choices=estudios_tipos)
    abreviatura = models.CharField(null=True, blank=True, max_length=30)
    descripcion=models.CharField(max_length=60)
    denominación=models.CharField(null=True, blank=True, max_length=30)
    nbu = models.IntegerField(null=True, blank=True)
    id_proveedor = models.ForeignKey(proveedor, models.DO_NOTHING)
    precio_socio = models.DecimalField(max_digits=8, decimal_places=2)
    precio_federacion = models.DecimalField(max_digits=8, decimal_places=2)
    ub = models.DecimalField(null=True, blank=True,max_digits=8, decimal_places=2)
    
    #Datos del sistema
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "estudios"
        verbose_name = "estudio"
        verbose_name_plural = "estudios"
        ordering = ["id_estudio"]

    def __str__(self):
        cadena = (
            str(self.id_estudio)
            + " - "
            + str(self.tipo)
            + " - "
            + str(self.descripcion)
        )
        return cadena



class estudio_socio(models.Model):
    id_estudio_socio = AutoField(primary_key=True)
    numero_socio=models.ForeignKey(socios, on_delete=models.CASCADE)
    id_estudio=models.ForeignKey(estudios, on_delete=models.CASCADE)
    #Datos del sistema
    created  = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True) 

    class Meta:
        db_table='estudios_socios'
        verbose_name='estudio_socio'
        verbose_name_plural='estudios_socios'
        ordering=['numero_socio']
        unique_together = ('numero_socio', 'id_estudio', 'created')

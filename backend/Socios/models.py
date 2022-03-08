from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField
from backend.deptos import deptos_tucuman, comumas_municipios

# from django import forms
from django.contrib.postgres.fields import ArrayField
from .utils import calcular_edad
from Mutuales.models import mutuales, servicios
from Cobradores.models import cobradores


# Create your models here.


CHOICES = [(servicios.id_servicio, servicios.servicio)]
"""
Construyo la entidad socios con sus atributos
"""


class socios(models.Model):
    numero_socio = AutoField(primary_key=True)
    #Datos personales
    apellido = models.CharField(max_length=80)
    nombre = models.CharField(max_length=80)
    dni = models.IntegerField(unique=True)
    fecha_nacimiento = models.DateField()
    #edad = models.IntegerField(blank=True, null=True, editable=False)

    #Direccion
    calle = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50, choices=comumas_municipios)
    departamento = models.CharField(max_length=30, choices=deptos_tucuman)
    cod_postal = models.IntegerField()

    #Contacto
    email = models.EmailField()
    tel_fijo = models.IntegerField(null=True, blank=True)
    tel_celular = models.IntegerField(null=True, blank=True)

    #Datos de la asociacion
    fecha_asociacion = models.DateField() 
    id_mutual = models.ForeignKey(mutuales,null=True, blank=True, on_delete=models.DO_NOTHING)
    tieneObraSocial = models.BooleanField()
    #plan = models.ForeignKey(planes, on_delete=models.DO_NOTHING)
    #vendedor = models.ForeignKey(vendedores, on_delete=models.DO_NOTHING)
    metodopago = models.CharField(max_length=50) # transferencia, link, o por cobrador
    cobrador = models.ForeignKey(cobradores,null=True, blank=True, on_delete=models.DO_NOTHING)
    #servicios_socio = models.ManyToManyField(servicios) #Atributo multivaludo
    # servicios = ArrayField(models.CharField(choices=CHOICES, max_length=20),20)

    carencia = models.DateField(null=True, blank=True)
    #Datos del sistema
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    @property
    def edad(self):
        #return 0
        return calcular_edad(self.fecha_nacimiento)
    class Meta:
        db_table = "socios"
        verbose_name = "socio"
        verbose_name_plural = "socios"
        ordering = ["numero_socio"]

    
    """
    def save(self):
        self.edad=self.edad_socio
        super (socios,self).save() 
    """
    def __str__(self):
        cadena = (
            str(self.numero_socio)
            + " - "
            + self.apellido
            + " - "
            + self.nombre
            + " - "
            + str(self.dni)
        )
        return cadena


"""
Construyo la entidad para el grupo familiar con sus atributos
"""


class familiar(models.Model):
    dni_familiar = models.IntegerField(primary_key=True)
    apellido = models.CharField(max_length=80)
    nombre = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField()
    #edad = models.IntegerField(null=True, blank=True)
    carencia = models.DateField(null=True, blank=True)
    fecha_asociacion = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    # relacion 1:N, BORRADO: NOT ACTION
    numero_socio = models.ForeignKey(socios, on_delete=models.DO_NOTHING)
    tieneObraSocial = models.BooleanField()
    #plan = models.ForeignKey(planes, on_delete=models.DO_NOTHING)

    @property
    def edad(self):
        return calcular_edad(self.fecha_nacimiento)
    
    class Meta:
        db_table = "familiares"
        verbose_name = "familiar"
        verbose_name_plural = "familiares"
        ordering = ["numero_socio"]

    """
    def save(self):
        self.edad=self.edad_socio
        super (familiar,self).save()

    """

    def __str__(self):
        cadena = (
            str(self.dni_familiar)
            + " - "
            + self.apellido
            + " - "
            + self.nombre
            + " - "
            + str(self.carencia)
        )
        return cadena



from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from Federacion.deptos import deptos_tucuman
# Create your models here.

class socios(models.Model):
    #nombre=models.CharField(max_length=50)
    numero_socio=models.IntegerField(primary_key=True)
    apellido_y_nombre=models.CharField(max_length=80)
    dni=models.IntegerField(unique=True)
    calle=models.CharField(max_length=50)
    localidad=models.CharField(max_length=30)
    departamento=models.CharField(max_length=30, choices=deptos_tucuman)
    cod_postal=models.IntegerField()
    fecha_nacimiento=models.DateField()
    edad=models.IntegerField()
    email=models.EmailField()   
    tel_fijo=models.IntegerField(null=True, blank=True)
    tel_celular=models.IntegerField(null=True, blank=True)
    #imagen_dni=models.ImageField(upload_to='blog', null=True, blank=True)
    carencia=models.DateField(null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='socio'
        verbose_name_plural='socios'

    def __str__(self):
        cadena = str(self.numero_socio)+'-'+self.apellido_y_nombre+'-'+str(self.dni)  
        return cadena
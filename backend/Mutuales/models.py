from django.db import models
from django.db.models.fields import AutoField
from backend.deptos import deptos_tucuman, comumas_municipios
# Create your models here.

"""
Construyo la entidad para los servicios
"""
class servicios(models.Model):
    id_servicio=models.AutoField(primary_key=True)
    servicio=models.CharField(max_length=20)
    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table='servicios'
        verbose_name='servicio'
        verbose_name_plural='servicios'
        ordering=['servicio']

    def __str__(self):
        cadena = str(self.id_servicio) + ' - '  + str(self.servicio) 
        return cadena

"""
Construyo la entidad para las mutuales
"""
class mutuales(models.Model):
    id_mutual=models.AutoField(primary_key=True)
    matricula=models.IntegerField(unique=True)
    nombre=models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    localidad=models.CharField(max_length=50, choices=comumas_municipios)
    sucursal=models.CharField(max_length=30, choices=deptos_tucuman)
    cuit=models.CharField(max_length=11, unique=True)
    email=models.EmailField(blank=True, null=True)
    telefono=models.CharField(max_length=10, blank=True, null=True)
    representante=models.CharField(max_length=100)
    fecha_inicio=models.DateField()
    fecha_ingreso=models.DateField()  
    ##id_servicio=models.ForeignKey(servicios, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='mutuales'
        verbose_name='mutual'
        verbose_name_plural='mutuales'
        ordering=['id_mutual']

    def __str__(self):
        cadena = str(self.id_mutual) + ' - '  + str(self.nombre) + ' - '  + str(self.sucursal)
        return cadena

class servicio_mutual(models.Model):
    id_serv_mut = AutoField(primary_key=True)
    id_mutual=models.ForeignKey(mutuales, on_delete=models.CASCADE)
    id_servicio=models.ForeignKey(servicios, on_delete=models.CASCADE) 

    class Meta:
        db_table='servicio_mutuales'
        verbose_name='servicio_mutual'
        verbose_name_plural='servicios_mutual'
        ordering=['id_mutual']
        unique_together = ('id_mutual', 'id_servicio',)

from django.db import models
from backend.deptos import deptos_tucuman
from .utils import calcular_edad
# Create your models here.

"""
Construyo la entidad socios con sus atributos
"""
class socios(models.Model):
    #nombre=models.CharField(max_length=50)
    numero_socio=models.IntegerField(primary_key=True)
    apellido=models.CharField(max_length=80)
    nombre=models.CharField(max_length=80)
    dni=models.IntegerField(unique=True)
    calle=models.CharField(max_length=50)
    localidad=models.CharField(max_length=30)
    departamento=models.CharField(max_length=30, choices=deptos_tucuman)
    cod_postal=models.IntegerField()
    fecha_nacimiento=models.DateField()
    edad=models.IntegerField(blank=True, null=True)
    email=models.EmailField()   
    tel_fijo=models.IntegerField(null=True, blank=True)
    tel_celular=models.IntegerField(null=True, blank=True)
    carencia=models.DateField(null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='socios'
        verbose_name='socio'
        verbose_name_plural='socios'
        ordering=['numero_socio']
   
    @property
    def edad_socio(self):
        #return 0
        return calcular_edad(self.fecha_nacimiento)
    
    def save(self):
        self.edad=self.edad_socio
        super (socios,self).save() 
   
    def __str__(self):
        cadena = str(self.numero_socio)+' - '+self.apellido+' - '+self.nombre+' - '+str(self.dni)  
        return cadena


"""
Construyo la entidad para el grupo familiar con sus atributos
"""
class familiar(models.Model):
    dni_familiar =models.IntegerField(primary_key=True)
    apellido=models.CharField(max_length=80)
    nombre=models.CharField(max_length=80)
    fecha_nacimiento=models.DateField()
    edad=models.IntegerField(null=True,blank=True)
    carencia=models.DateField(null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now_add=True)
    #relacion 1:N, BORRADO: NOT ACTION
    numero_socio=models.ForeignKey(socios, on_delete=models.DO_NOTHING)


    class Meta:
        db_table='familiares'
        verbose_name='familiar'
        verbose_name_plural='familiares'
        ordering=['numero_socio']

    @property
    def edad_socio(self):
        #return 0
        return calcular_edad(self.fecha_nacimiento)
    
    def save(self):
        self.edad=self.edad_socio
        super (familiar,self).save() 
   
    def __str__(self):
        cadena = str(self.dni_familiar)+' - '+self.apellido+' - '+self.nombre+' - '+str(self.carencia)  
        return cadena
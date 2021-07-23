from django.db import models
from Socios.models import socios, familiar
from Profesionales.models import profesionales

# Create your models here.

"""
Construyo la entidad para las ordenes medicas
"""
class ordenes(models.Model):
    numero_orden=models.IntegerField(primary_key=True)
    numero_socio=models.ManyToManyField(socios)
    paciente=models.CharField(max_length=60)
    servicio=models.CharField(max_length=30)
    id_medico=models.ManyToManyField(profesionales)
    mutual=models.CharField(max_length=30)
    fecha=models.DateTimeField()
    precio=models.DecimalField(max_digits=8, decimal_places=2)
    realizado=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='ordenes'
        verbose_name='orden'
        verbose_name_plural='ordenes'
        #ordering=['id_medicamento']

    def __str__(self):
        cadena = str(self.numero_orden) + ' - '  + str(self.numero_socio) + ' - ' + str(self.id_medico)
        return cadena
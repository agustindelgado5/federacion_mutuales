from django.db import models
from Socios.models import socios
from django.db.models.fields import AutoField
from datetime import datetime

# Create your models here.
"""
Construyo la entidad medicamentos con sus atributos
"""


class cuotas(models.Model):
    id_cuota = AutoField(primary_key=True)
    monto = models.DecimalField(decimal_places=2, max_digits=6)
    periodo = models.DateField(default=datetime.now)
    pagado = models.BooleanField(default=False)
    numero_socio = models.ForeignKey(
        socios, on_delete=models.DO_NOTHING, related_name="numsociocuotas"
    )
    personapago = models.CharField(max_length=60,null=True,blank=True)
    fecharealizacion = models.DateField(null=True,blank=True)
    metodoPago = models.CharField(max_length=50,null=True,blank=True) # transferencia, link, por cobrador, etc

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "cuotas"
        verbose_name = "cuota"
        verbose_name_plural = "cuotas"
        ordering = ["id_cuota"]

    def __str__(self):
        cadena = (
            str(self.id_cuota)
            + " - "
            + str(self.personapago)
            + " - "
            + str(self.monto)
            + " - "
            + str(self.fecharealizacion)
        )
        return cadena

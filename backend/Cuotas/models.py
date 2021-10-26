from django.db import models
from Socios.models import socios

# Create your models here.
"""
Construyo la entidad medicamentos con sus atributos
"""


class cuotas(models.Model):
    id_cuota = models.IntegerField(primary_key=True)
    personapago = models.CharField(max_length=60)
    monto = models.DecimalField(decimal_places=2, max_digits=6)
    fecharealizacion = models.DateTimeField(auto_now_add=True)
    numero_socio = models.ForeignKey(
        socios, on_delete=models.DO_NOTHING, related_name="numsociocuotas"
    )

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

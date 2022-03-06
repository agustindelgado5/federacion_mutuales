from django.db import models
from datetime import datetime
from Profesionales.models import profesionales
from backend.datos_GastosSalientes import modos_pagos
from backend.datos_pagos import meses
# Create your models here.

"""
Construyo la entidad gastosSalientes con sus atributos
"""


class pagadoProfesionales(models.Model):
    id_pagoprofesional = models.AutoField(primary_key=True)
    id_medico = models.ForeignKey(profesionales, on_delete=models.DO_NOTHING)
    total = models.DecimalField(decimal_places=2, max_digits=6)
    fecha = models.DateField(default=datetime.now)
    modo_pago=models.CharField(max_length=20, choices=modos_pagos)
    mespagado=models.CharField(max_length=40, choices=meses)
    
    class Meta:
        db_table = "pagadoProfesionales"
        verbose_name = "pagadoProfesionales"
        verbose_name_plural = "pagadoProfesionales"
        ordering = ["id_medico"]

    def __str__(self):
        cadena = (
            str(self.id_medico)
            + "-"
            + str(self.id_medico)
            + "-"
            + str(self.fecha)
            + "-"
            + self.total
            + "-"
            + str(self.mespagado)
        )
        return cadena

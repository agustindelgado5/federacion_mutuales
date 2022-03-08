from django.contrib import admin
from .models import pagadoProfesionales

# Register your models here.


class pagadoProfesionalesAdmin(admin.ModelAdmin):
    list_display = ("id_pagoprofesional", "id_medico", "total", "fecha", "modo_pago", "mespagado")
    search_fields = ("id_pagoprofesional", "id_medico", "total", "fecha", "modo_pago", "mespagado")
    ordering = ["id_pagoprofesional"]
    readonly_fields = ("created", "updated")


admin.site.register(pagadoProfesionales)

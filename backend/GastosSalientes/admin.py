from django.contrib import admin
from .models import gastosSalientes

# Register your models here.


class gastosSalientesAdmin(admin.ModelAdmin):
    list_display = ("id_gasto", "nro_ticket", "descripcion")
    search_fields = ("id_gasto", "nro_ticket", "descripcion")
    ordering = ["id_gasto"]
    readonly_fields = ("created", "updated")


admin.site.register(gastosSalientes)

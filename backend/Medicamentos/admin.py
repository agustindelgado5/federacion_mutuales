from django.contrib import admin

from .models import medicamentos, receta

# Register your models here.


class medicamentosAdmin(admin.ModelAdmin):
    list_display = ("id_medicamento", "nombre", "presentacion")
    search_fields = ("id_medicamento", "nombre", "presentacion")
    ordering = ["id_medicamento"]
    # autocomplete_fields=['cod_farmacia']
    readonly_fields = ("created", "updated")


class recetasAdmin(admin.ModelAdmin):
    list_display = ("id_receta", "id_medicamento", "numero_socio")
    search_fields = ("id_receta", "id_medicamento", "numero_socio")
    ordering = ["id_receta"]
    autocomplete_fields = ["id_medicamento", "numero_socio"]
    readonly_fields = ("created", "updated")


admin.site.register(medicamentos, medicamentosAdmin)
admin.site.register(receta, recetasAdmin)

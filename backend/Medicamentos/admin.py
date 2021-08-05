from Profesionales.admin import medicosAdmin
from django.contrib import admin
from django.contrib.admin.sites import site
from .models import medicamentos,receta
# Register your models here.

class medicamentosAdmin(admin.ModelAdmin):
    list_display=('id_medicamento','nombre', 'presentacion')
    search_fields=('id_medicamento','nombre', 'presentacion')
    ordering=['id_medicamento']
    #autocomplete_fields=['cod_farmacia']
    readonly_fields=('created', 'updated')



class recetasAdmin(admin.ModelAdmin):
    list_display=('id_medicamento','numero_socio', 'dni_familiar')
    search_fields=('id_medicamento','numero_socio', 'dni_familiar')
    ordering=['id_medicamento']
    autocomplete_fields=['id_medicamento','numero_socio', 'dni_familiar']
    readonly_fields=('created', 'updated')

admin.site.register(medicamentos, medicamentosAdmin)
admin.site.register(receta, recetasAdmin)

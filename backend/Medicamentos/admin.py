from django.contrib import admin
from django.contrib.admin.sites import site
from .models import medicamentos
# Register your models here.

class recetasAdmin(admin.ModelAdmin):
    list_display=('id_medicamento','nombre','numero_socio', 'dni_familiar')
    search_fields=('id_medicamento','nombre','numero_socio', 'dni_familiar')
    ordering=['id_medicamento']
    #autocomplete_fields=['departamento']
    readonly_fields=('created', 'updated')

admin.site.register(medicamentos, recetasAdmin)
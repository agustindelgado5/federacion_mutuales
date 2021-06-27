from django.contrib import admin
from django.contrib.admin.sites import site
from .models import socios
# Register your models here.

class sociosAdmin(admin.ModelAdmin):
    list_display=('numero_socio','apellido_y_nombre','dni')
    search_fields=('numero_socio','apellido_y_nombre','dni')
    ordering=['numero_socio']
    #autocomplete_fields=['departamento']
    readonly_fields=('created', 'updated')

admin.site.register(socios, sociosAdmin)

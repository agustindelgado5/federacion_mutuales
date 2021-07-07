from django.contrib import admin
from django.contrib.admin.sites import site
from .models import profesionales
# Register your models here.

# class medicosAdmin(admin.ModelAdmin):
#     list_display=('id_medico','apellido_y_nombre','matricula')
#     search_fields=('id_medico','apellido_y_nombre','matricula')
#     ordering=['id_medico']
#     #autocomplete_fields=['departamento']
#     readonly_fields=('created', 'updated')

admin.site.register(profesionales)

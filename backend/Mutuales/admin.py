from django.contrib import admin
from .models import mutuales, servicios, servicio_mutual
# Register your models here.

class serviciosAdmin(admin.ModelAdmin):
    list_display=('id_servicio','servicio')
    search_fields=('id_servicio','servicio')
    ordering=['id_servicio']
    readonly_fields=('created', 'updated')

class mutualesAdmin(admin.ModelAdmin):
    list_display=('id_mutual','nombre','sucursal')
    search_fields=('id_mutual','nombre','sucursal')
    ordering=['id_mutual']
    #autocomplete_fields=['id_servicio']
    readonly_fields=('created', 'updated')

class servicios_mutualesAdmin(admin.ModelAdmin):
    list_display=('id_mutual','id_servicio')
    search_fields=('id_mutual','id_servicio')
    ordering=['id_mutual', 'id_servicio']
    unique_together = ['id_mutual', 'id_servicio']
    #autocomplete_fields=['id_servicio']
    #readonly_fields=('created', 'updated')

admin.site.register(servicios, serviciosAdmin)
admin.site.register(servicio_mutual, servicios_mutualesAdmin)
admin.site.register(mutuales, mutualesAdmin)

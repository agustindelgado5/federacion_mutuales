from django.contrib import admin
from .models import mutuales
# Register your models here.

class mutualesAdmin(admin.ModelAdmin):
    list_display=('id_mutual','nombre','sucursal')
    search_fields=('id_mutual','nombre','sucursal')
    ordering=['id_mutual']
    #autocomplete_fields=['numero_socio', 'id_medico']
    readonly_fields=('created', 'updated')

admin.site.register(mutuales, mutualesAdmin)
from django.contrib import admin
from .models import ordenes

# Register your models here.


class ordenesAdmin(admin.ModelAdmin):
    list_display = ("numero_orden", "numero_socio", "paciente", "id_medico", "fecha")
    search_fields = ("numero_orden", "numero_socio", "paciente", "id_medico", "fecha")
    ordering = ["numero_orden"]
    autocomplete_fields = ["numero_socio"]
    readonly_fields = ("created", "updated")


admin.site.register(ordenes, ordenesAdmin)
